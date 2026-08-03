(() => {
  "use strict";
  // The document is complete without JavaScript. This file intentionally
  // contains no content rewriting and only records enhanced navigation use.
  document.addEventListener("keydown", (event) => {
    if (event.key === "Tab") document.documentElement.dataset.keyboard = "true";
  }, { once: true });
})();
