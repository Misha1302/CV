from __future__ import annotations

import argparse
import base64
import io
import re
import json
import shutil
import threading
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

from PIL import Image
from playwright.sync_api import Browser, Page, sync_playwright

from build_site import ROOT, load_data

BASELINE_PATH = ROOT / "data" / "visual-baseline.json"
CASES = [
    {"file": "ru-compiler.html", "mode": "desktop", "width": 1440, "height": 1100, "js": True, "media": "screen"},
    {"file": "en-compiler.html", "mode": "desktop", "width": 1440, "height": 1100, "js": True, "media": "screen"},
    {"file": "ru-backend.html", "mode": "desktop", "width": 1440, "height": 1100, "js": True, "media": "screen"},
    {"file": "ru-compiler.html", "mode": "mobile-320", "width": 320, "height": 780, "js": True, "media": "screen"},
    {"file": "en-compiler.html", "mode": "mobile-320", "width": 320, "height": 780, "js": True, "media": "screen"},
    {"file": "ru-compiler.html", "mode": "no-js-320", "width": 320, "height": 780, "js": False, "media": "screen"},
    {"file": "ru-compiler.html", "mode": "no-js-desktop", "width": 1440, "height": 1100, "js": False, "media": "screen"},
    {"file": "ru-compiler.html", "mode": "zoom-200", "width": 640, "height": 900, "js": True, "media": "screen"},
    {"file": "ru-compiler.html", "mode": "print", "width": 1050, "height": 1485, "js": False, "media": "print"},
    {"file": "index.html", "mode": "mobile-320", "width": 320, "height": 780, "js": False, "media": "screen"}
]


def dhash(png: bytes, hash_size: int = 16) -> str:
    image = Image.open(io.BytesIO(png)).convert("L").resize((hash_size + 1, hash_size))
    pixels = list(image.get_flattened_data())
    value = 0
    for row in range(hash_size):
        offset = row * (hash_size + 1)
        for column in range(hash_size):
            value = (value << 1) | int(pixels[offset + column] > pixels[offset + column + 1])
    return f"{value:0{hash_size * hash_size // 4}x}"


def hamming(left: str, right: str) -> int:
    return (int(left, 16) ^ int(right, 16)).bit_count()


def metrics(page: Page) -> dict:
    return page.evaluate("""() => {
      const html = document.documentElement;
      const body = document.body;
      const viewport = window.innerWidth;
      const offenders = [];
      for (const el of document.querySelectorAll('body *')) {
        const style = getComputedStyle(el);
        if (style.display === 'none' || style.visibility === 'hidden' || style.position === 'fixed') continue;
        const rect = el.getBoundingClientRect();
        if (rect.width > 1 && (rect.right > viewport + 1.5 || rect.left < -1.5)) {
          offenders.push({tag: el.tagName, cls: String(el.className || ''), left: rect.left, right: rect.right, text: (el.textContent || '').trim().slice(0, 60)});
          if (offenders.length >= 8) break;
        }
      }
      const main = document.querySelector('main');
      return {
        viewport,
        scrollWidth: Math.max(html.scrollWidth, body.scrollWidth),
        scrollHeight: Math.max(html.scrollHeight, body.scrollHeight),
        h1Count: document.querySelectorAll('h1').length,
        h1: document.querySelector('h1')?.textContent?.trim() || '',
        role: document.querySelector('.role')?.textContent?.trim() || '',
        mainTextLength: (main?.innerText || main?.textContent || '').trim().length,
        sectionIds: Array.from(document.querySelectorAll('main section[id]')).map(x => x.id),
        offenders
      };
    }""")


def verify_focus(page: Page, filename: str, mode: str) -> dict:
    page.locator("body").click(position={"x": 2, "y": 2})
    page.keyboard.press("Tab")
    result = page.evaluate("""() => {
      const el = document.activeElement;
      const style = getComputedStyle(el);
      return {
        tag: el?.tagName || '',
        text: (el?.textContent || '').trim().slice(0, 80),
        outlineStyle: style.outlineStyle,
        outlineWidth: style.outlineWidth,
        outlineColor: style.outlineColor
      };
    }""")
    width = float(str(result["outlineWidth"]).replace("px", "") or 0)
    if result["tag"] not in {"A", "BUTTON", "SUMMARY"} or result["outlineStyle"] == "none" or width < 2:
        raise RuntimeError(f"focus not visibly exposed for {filename}/{mode}: {result}")
    return result


def capture(browser: Browser, output_dir: Path) -> dict[str, dict]:
    results: dict[str, dict] = {}
    for case in CASES:
        context = browser.new_context(
            viewport={"width": case["width"], "height": case["height"]},
            device_scale_factor=1,
            java_script_enabled=case["js"],
            reduced_motion="reduce",
        )
        page = context.new_page()
        page.emulate_media(media=case["media"])
        raw = (ROOT / case["file"]).read_text(encoding="utf-8")
        css = (ROOT / "style.css").read_text(encoding="utf-8")
        raw = re.sub(r'<link[^>]+rel="stylesheet"[^>]*>', f"<style>{css}</style>", raw, flags=re.I)
        portrait = base64.b64encode((ROOT / "assets" / "portrait.svg").read_bytes()).decode("ascii")
        raw = raw.replace('src="assets/portrait.svg"', f'src="data:image/svg+xml;base64,{portrait}"')
        if case["js"]:
            script = (ROOT / "script.js").read_text(encoding="utf-8")
            raw = re.sub(r'<script[^>]+src="script\.js"[^>]*></script>', f"<script>{script}</script>", raw, flags=re.I)
        else:
            raw = re.sub(r'<script[^>]+src="script\.js"[^>]*></script>', "", raw, flags=re.I)
        page.set_content(raw, wait_until="domcontentloaded", timeout=20000)
        if case["js"]:
            page.add_style_tag(content="*{animation:none!important;transition:none!important;caret-color:transparent!important}")
        page.wait_for_timeout(150)
        current = metrics(page)
        if current["scrollWidth"] > current["viewport"] + 1:
            raise RuntimeError(f"horizontal scroll {case['file']}/{case['mode']}: {current}")
        if current["offenders"]:
            raise RuntimeError(f"overflowing elements {case['file']}/{case['mode']}: {current['offenders']}")
        if current["h1Count"] != 1 or not current["h1"]:
            raise RuntimeError(f"H1 invalid {case['file']}/{case['mode']}: {current}")
        if case["file"] != "index.html" and not current["role"]:
            raise RuntimeError(f"role missing {case['file']}/{case['mode']}")
        minimum_text = 3400 if "compiler" in case["file"] else 1800
        if case["file"] != "index.html" and current["mainTextLength"] < minimum_text:
            raise RuntimeError(f"critical static content missing {case['file']}/{case['mode']}: {current['mainTextLength']}")
        if case["file"] != "index.html" and case["media"] == "screen":
            expected_sections = ["profile", "evidence", "experience", "projects", "skills", "education"]
            if current["sectionIds"] != expected_sections:
                raise RuntimeError(f"section order changed {case['file']}/{case['mode']}: {current['sectionIds']}")
        focus = None
        if case["js"] and case["media"] == "screen":
            focus = verify_focus(page, case["file"], case["mode"])
        png = page.screenshot(full_page=True, timeout=20000)
        key = f"{case['file']}|{case['mode']}"
        output = output_dir / f"{case['file'].replace('.html', '')}-{case['mode']}.png"
        output.write_bytes(png)
        image = Image.open(io.BytesIO(png))
        results[key] = {
            "dhash": dhash(png),
            "image_width": image.width,
            "image_height": image.height,
            "viewport_width": case["width"],
            "viewport_height": case["height"],
            "page_height": current["scrollHeight"],
            "main_text_length": current["mainTextLength"],
            "focus": focus,
        }
        context.close()
    return results


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", type=Path, default=ROOT / "evidence" / "visual")
    parser.add_argument("--update", action="store_true")
    parser.add_argument("--update-if-missing", action="store_true")
    parser.add_argument("--max-hamming", type=int, default=64)
    parser.add_argument("--report", type=Path)
    args = parser.parse_args()
    args.output_dir.mkdir(parents=True, exist_ok=True)
    load_data()

    with sync_playwright() as playwright:
        executable = shutil.which("chromium") or shutil.which("chromium-browser")
        launch_args = {"headless": True, "args": ["--no-sandbox", "--no-proxy-server"]}
        if executable:
            launch_args["executable_path"] = executable
        browser = playwright.chromium.launch(**launch_args)
        current = capture(browser, args.output_dir)
        browser.close()

    update = args.update or (args.update_if_missing and not BASELINE_PATH.exists())
    if update:
        BASELINE_PATH.write_text(json.dumps(current, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        status = {"status": "UPDATED", "cases": len(current), "baseline": str(BASELINE_PATH.relative_to(ROOT))}
    else:
        if not BASELINE_PATH.exists():
            raise RuntimeError("visual baseline missing; use --update")
        baseline = json.loads(BASELINE_PATH.read_text(encoding="utf-8"))
        if baseline.keys() != current.keys():
            raise RuntimeError("visual case set changed; update baseline intentionally")
        failures = []
        comparisons = []
        for key in current:
            distance = hamming(baseline[key]["dhash"], current[key]["dhash"])
            base_height = int(baseline[key]["page_height"])
            current_height = int(current[key]["page_height"])
            delta = abs(current_height - base_height) / max(base_height, 1)
            comparisons.append({"case": key, "hamming": distance, "height_delta": round(delta, 5)})
            if distance > args.max_hamming or delta > .05:
                failures.append(comparisons[-1])
        if failures:
            raise RuntimeError("visual regression detected: " + json.dumps(failures, ensure_ascii=False))
        status = {"status": "PASS", "cases": len(current), "comparisons": comparisons}
    report_path = args.report or (args.output_dir / "visual-report.json")
    report_path.write_text(json.dumps(status, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(status, ensure_ascii=False))


if __name__ == "__main__":
    main()
