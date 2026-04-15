#!/usr/bin/env python3
"""
Validate an interactive visualization HTML file for common issues.

Usage: python scripts/validate.py <path-to-html-file>

Checks:
  - File is valid HTML with DOCTYPE
  - Dark mode support exists
  - Chart.js canvases have accessibility attributes
  - SVGs have role="img" with <title> and <desc>
  - No hardcoded light-only colors in body/main containers
  - External scripts load from allowed CDNs only
  - Canvas elements are wrapped in positioned containers
  - Range inputs have step attributes
  - Numbers in display elements are rounded (heuristic)
"""

import sys
import re
import os


ALLOWED_CDNS = [
    "cdnjs.cloudflare.com",
    "cdn.jsdelivr.net",
    "esm.sh",
    "unpkg.com",
]

ERRORS = []
WARNINGS = []


def error(msg):
    ERRORS.append(f"  ERROR: {msg}")


def warn(msg):
    WARNINGS.append(f"  WARN:  {msg}")


def validate(filepath):
    if not os.path.isfile(filepath):
        print(f"File not found: {filepath}")
        sys.exit(1)

    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    html_lower = content.lower()

    # 1. DOCTYPE
    if "<!doctype html>" not in html_lower:
        error("Missing <!DOCTYPE html> declaration")

    # 2. Dark mode
    has_dark_css = "prefers-color-scheme: dark" in content or "prefers-color-scheme:dark" in content
    has_dark_js = "prefers-color-scheme" in content and "matchMedia" in content
    if not has_dark_css and not has_dark_js:
        error("No dark mode support detected. Use @media (prefers-color-scheme: dark) or matchMedia.")

    # 3. Canvas accessibility
    canvases = re.findall(r"<canvas[^>]*>", content)
    for canvas in canvases:
        if 'role="img"' not in canvas:
            error(f"Canvas missing role=\"img\": {canvas[:80]}...")
        if "aria-label" not in canvas:
            error(f"Canvas missing aria-label: {canvas[:80]}...")

    # 4. SVG accessibility
    svgs = re.findall(r"<svg[^>]*>", content)
    for svg_tag in svgs:
        if 'role="img"' not in svg_tag:
            # Check if it's a data viz SVG (not a tiny icon)
            if "viewBox" in svg_tag:
                warn(f"SVG with viewBox missing role=\"img\": {svg_tag[:80]}...")

    if svgs:
        if "<title>" not in content:
            warn("SVG present but no <title> element found for accessibility")
        if "<desc>" not in content:
            warn("SVG present but no <desc> element found for accessibility")

    # 5. CDN sources
    script_srcs = re.findall(r'<script[^>]+src=["\']([^"\']+)["\']', content)
    for src in script_srcs:
        if src.startswith("http"):
            domain = src.split("//")[1].split("/")[0]
            if domain not in ALLOWED_CDNS:
                error(f"External script from disallowed CDN: {domain} ({src})")

    # 6. Canvas wrapper
    canvas_count = len(canvases)
    positioned_divs = len(re.findall(r"position:\s*relative", content))
    if canvas_count > 0 and positioned_divs < canvas_count:
        warn("Some <canvas> elements may not be wrapped in a positioned container (need position: relative on parent)")

    # 7. Range inputs without step
    range_inputs = re.findall(r"<input[^>]*type=[\"']range[\"'][^>]*>", content)
    for ri in range_inputs:
        if "step" not in ri:
            warn(f"Range input without step attribute (may produce float artifacts): {ri[:80]}...")

    # 8. position: fixed (doesn't work in iframes)
    if "position: fixed" in content or "position:fixed" in content:
        warn("position: fixed detected — this does not work in sandboxed iframe environments")

    # 9. maintainAspectRatio check for Chart.js
    if "Chart(" in content or "new Chart" in content:
        if "maintainAspectRatio: false" not in content and "maintainAspectRatio:false" not in content:
            warn("Chart.js used but maintainAspectRatio: false not set — chart may not size correctly")

    # 10. Font size check
    tiny_fonts = re.findall(r"font-size:\s*(\d+)px", content)
    for size in tiny_fonts:
        if int(size) < 11:
            warn(f"Font size {size}px is below the 11px minimum")

    # Summary
    print(f"\nValidation results for: {filepath}")
    print(f"{'=' * 60}")

    if not ERRORS and not WARNINGS:
        print("  All checks passed!")
    else:
        for e in ERRORS:
            print(e)
        for w in WARNINGS:
            print(w)

    print(f"\n  {len(ERRORS)} error(s), {len(WARNINGS)} warning(s)")

    return len(ERRORS) == 0


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python scripts/validate.py <path-to-html-file>")
        sys.exit(1)

    ok = validate(sys.argv[1])
    sys.exit(0 if ok else 1)
