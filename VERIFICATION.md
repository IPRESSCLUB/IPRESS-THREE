# Verification record

## Passed automated checks

- Exactly two native navigation links, with the exact official website and WhatsApp invitation URLs from the brief.
- External links include `target="_blank"`, `noopener` and `noreferrer`.
- Both link names and new-tab descriptions resolve to existing, unique IDs.
- Original IPRESS logo SHA-256 matches the source project: `244a4daafd21f384e1bbaa777c5664ab366a311c27701edc9bb26e50dc0fcdd6`.
- Every referenced local page asset and font exists.
- All principal text/background color pairs exceed 4.5:1 contrast; measured range 5.43:1 to 10.60:1.
- Canonical, Open Graph and social metadata are present, with a real 1200 × 630 PNG preview.
- JavaScript syntax passes Node.js validation.
- Pointer events share one pending animation frame per tracked element.
- Pointer values are bounded; leaving or cancelling clears effects.
- Reduced-motion preferences prevent effects, cancel pending frames, and clean up event listeners when changed live.
- Touch/coarse-pointer environments do not get cursor-driven effects.
- CSS includes reduced-motion, visible keyboard focus, forced-colors handling, and responsive layout rules.
- No continuous animation loops, third-party JavaScript, remote font requests, form submissions or tracking code.
- The two HTML anchors do not depend on JavaScript to navigate.
- Initial page resources total approximately 82 KB before HTTP compression. The larger source TTF fonts and social preview are not loaded by the page.

## Visual review

The generated social-sharing graphic was visually inspected. The website source includes a mobile-first composition adjustment at 760 px, a narrow-screen refinement at 360 px, tablet styling and short-desktop-height rules.

**Browser rendering and real-device checks could not be performed in this session because the supported browser-testing capability was unavailable.** Static checks are not evidence that viewport layouts, touch behavior, focus appearance or browser compatibility have been exercised in a browser.

Recommended final browser checks after upload: 320 × 568, 375 × 812, 390 × 844, 768 × 1024, 1024 × 768, 1440 × 900 and 1920 × 1080. Confirm no horizontal overflow, try both links, tab through both cards, and enable reduced motion and 200% zoom. Also check Safari/iOS, Chrome/Android and Firefox.

The original logo is a 296 × 61 raster image. Its existing resolution is preserved rather than inventing a higher-resolution logo.

## Repeat the automated checks

From the extracted ZIP:

```sh
python3 scripts/check-project.py
node --check script.js
node scripts/check-motion.cjs
```

These tests use only standard Python and Node.js libraries. Regenerating the social-preview PNG is separate and optionally requires Pillow.
