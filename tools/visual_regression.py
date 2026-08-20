from __future__ import annotations

import argparse
import io
import json
import threading
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

from PIL import Image
from playwright.sync_api import Browser, Page, sync_playwright

from build_site import ROOT, load_data

BASELINE_PATH = ROOT / "data" / "visual-baseline.json"
# Keep pixel baselines on stable CV pages. The landing selector is intentionally
# data-driven: adding or removing a profile changes its card grid by design, so
# it is exercised by the structural smoke matrix instead of a golden image.
REGRESSION_CASES = [
    ("ru.html", "desktop", 1440, 1100, True),
    ("ru-compiler.html", "desktop", 1440, 1100, True),
    ("ru-backend.html", "desktop", 1440, 1100, True),
    ("ru-cpp-systems.html", "desktop", 1440, 1100, True),
    ("ru.html", "mobile", 390, 844, True),
    ("ru-compiler.html", "mobile", 390, 844, True),
    ("ru-backend.html", "mobile", 390, 844, True),
    ("ru-cpp-systems.html", "mobile", 390, 844, True),
    ("ru.html", "no-js", 1440, 1100, False),
    ("ru-backend.html", "no-js", 390, 844, False),
]
VIEW_MODES = [
    ("desktop", 1440, 1100, True),
    ("mobile", 390, 844, True),
    ("no-js", 390, 844, False),
]


def smoke_cases(data: dict) -> list[tuple[str, str, int, int, bool]]:
    covered = {(filename, mode) for filename, mode, *_ in REGRESSION_CASES}
    cases: list[tuple[str, str, int, int, bool]] = []
    candidates = ["index.html"]
    for key in data["profile_order"]:
        for lang in ("ru", "en"):
            candidates.append(data["profiles"][key][lang]["filename"])
    for filename in candidates:
        for mode, width, height, js_enabled in VIEW_MODES:
            if (filename, mode) not in covered:
                cases.append((filename, mode, width, height, js_enabled))
    return cases


def dhash(png: bytes, hash_size: int = 16) -> str:
    image = Image.open(io.BytesIO(png)).convert("L").resize((hash_size + 1, hash_size))
    pixels = list(image.getdata())
    bits = []
    for row in range(hash_size):
        offset = row * (hash_size + 1)
        for col in range(hash_size):
            bits.append(pixels[offset + col] > pixels[offset + col + 1])
    value = 0
    for bit in bits:
        value = (value << 1) | int(bit)
    return f"{value:0{hash_size * hash_size // 4}x}"


def hamming(left: str, right: str) -> int:
    return (int(left, 16) ^ int(right, 16)).bit_count()


def page_metrics(page: Page) -> dict[str, float | int | str]:
    return page.evaluate("""() => {
      const html = document.documentElement;
      const body = document.body;
      const viewport = window.innerWidth;
      const offenders = [];
      for (const el of document.querySelectorAll('body *')) {
        const style = getComputedStyle(el);
        if (style.display === 'none' || style.visibility === 'hidden' || style.position === 'fixed') continue;
        const rect = el.getBoundingClientRect();
        if (rect.width > 1 && (rect.right > viewport + 1 || rect.left < -1)) {
          offenders.push({tag: el.tagName, cls: el.className || '', left: rect.left, right: rect.right});
          if (offenders.length >= 8) break;
        }
      }
      return {
        viewport,
        scrollWidth: Math.max(html.scrollWidth, body.scrollWidth),
        scrollHeight: Math.max(html.scrollHeight, body.scrollHeight),
        h1: document.querySelector('main h1')?.textContent?.trim() || '',
        role: document.querySelector('.hero-role')?.textContent?.trim() || '',
        offenders: JSON.stringify(offenders),
      };
    }""")


def capture(browser: Browser, base_url: str, output_dir: Path, cases: list[tuple[str, str, int, int, bool]]) -> dict[str, dict[str, object]]:
    results: dict[str, dict[str, object]] = {}
    for filename, mode, width, height, js_enabled in cases:
        context = browser.new_context(
            viewport={"width": width, "height": height},
            device_scale_factor=1,
            java_script_enabled=js_enabled,
            reduced_motion="reduce",
        )
        page = context.new_page()
        page.goto(base_url + filename, wait_until="domcontentloaded", timeout=15000)
        page.wait_for_timeout(150)
        if js_enabled:
            page.add_style_tag(content="*{animation:none!important;transition:none!important;caret-color:transparent!important}")
        metrics = page_metrics(page)
        if metrics["scrollWidth"] > metrics["viewport"] + 1:
            raise RuntimeError(f"Horizontal overflow {filename}/{mode}: {metrics}")
        if metrics["offenders"] != "[]":
            raise RuntimeError(f"Overflowing elements {filename}/{mode}: {metrics['offenders']}")
        if not metrics["h1"]:
            raise RuntimeError(f"Missing H1 without JS: {filename}/{mode}")
        if filename != "index.html" and not metrics["role"]:
            raise RuntimeError(f"Missing visible role: {filename}/{mode}")
        png = page.screenshot(full_page=(mode != "no-js"), timeout=15000)
        key = f"{filename}|{mode}"
        output_path = output_dir / f"{filename.replace('.html', '')}-{mode}.png"
        output_path.write_bytes(png)
        results[key] = {
            "dhash": dhash(png),
            "width": width,
            "viewport_height": height,
            "page_height": metrics["scrollHeight"],
            "h1": metrics["h1"],
            "role": metrics["role"],
        }
        context.close()
    return results


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", type=Path, default=ROOT / "visual-evidence")
    parser.add_argument("--update", action="store_true")
    parser.add_argument("--update-if-missing", action="store_true")
    parser.add_argument("--max-hamming", type=int, default=28)
    args = parser.parse_args()
    args.output_dir.mkdir(parents=True, exist_ok=True)
    data = load_data()

    handler = partial(SimpleHTTPRequestHandler, directory=str(ROOT))
    server = ThreadingHTTPServer(("127.0.0.1", 0), handler)
    server.daemon_threads = True
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    base_url = f"http://127.0.0.1:{server.server_port}/"
    try:
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(headless=True)
            regression = capture(browser, base_url, args.output_dir, REGRESSION_CASES)
            smoke = capture(browser, base_url, args.output_dir, smoke_cases(data))
            browser.close()
    finally:
        server.shutdown()
        server.server_close()

    current = regression | smoke
    (args.output_dir / "current.json").write_text(json.dumps(current, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    update = args.update or (args.update_if_missing and not BASELINE_PATH.exists())
    if update:
        BASELINE_PATH.write_text(json.dumps(regression, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(f"Updated {BASELINE_PATH}; smoke-checked {len(smoke)} additional views")
        return
    if not BASELINE_PATH.exists():
        raise RuntimeError("Visual baseline is missing; run with --update")
    baseline = json.loads(BASELINE_PATH.read_text(encoding="utf-8"))
    regression_keys = set(regression)
    missing = regression_keys - set(baseline)
    if missing:
        raise RuntimeError("Visual baseline is missing regression cases: " + ", ".join(sorted(missing)))
    # Obsolete golden entries are harmless: cases intentionally moved to smoke
    # remain structurally checked in all view modes without blessing new pixels.
    baseline = {key: baseline[key] for key in regression}
    failures = []
    for key in regression:
        distance = hamming(baseline[key]["dhash"], regression[key]["dhash"])
        base_height = int(baseline[key]["page_height"])
        current_height = int(regression[key]["page_height"])
        height_delta = abs(current_height - base_height) / max(1, base_height)
        if distance > args.max_hamming or height_delta > 0.08:
            failures.append({"case": key, "hamming": distance, "height_delta": round(height_delta, 4)})
    if failures:
        raise RuntimeError("Visual regression detected: " + json.dumps(failures, ensure_ascii=False))
    print(json.dumps({"regression_cases": len(regression), "smoke_views": len(smoke), "status": "PASS"}, ensure_ascii=False))


if __name__ == "__main__":
    main()
