# Claymorphism redesign — verification record

## Automated checks completed

- Exactly two native destination links, with the exact official website and WhatsApp URLs from the brief.
- New-tab behavior includes `noopener noreferrer` and screen-reader descriptions.
- Unique IDs and valid references for accessible link names and descriptions.
- Original upload preserved byte for byte: SHA-256 `3d9f9084d84835f366f69b583e956c51243e5776b6c908a917c19558f997d26e`.
- Display logo pixels retained unchanged: SHA-256 `244a4daafd21f384e1bbaa777c5664ab366a311c27701edc9bb26e50dc0fcdd6`.
- Every local image, font, stylesheet and script reference resolves.
- Principal text/base-background contrast pairs range from 5.12:1 to 9.93:1. These numerical tests use flat base colors; they do not substitute for visual checks over rendered shadow effects.
- Canonical, Open Graph and social metadata target `https://ipressclub.github.io/IPRESS-THREE/`, matching the repository shown in the supplied screenshots.
- The social PNG is 1200 × 630; the runtime camera WebP is 608 × 608 with transparency preserved.
- JavaScript syntax checked with Node.js.
- Fine-pointer and reduced-motion gating checked, including live preference changes.
- Pointer events are coalesced to one pending animation frame per tracked element.
- Card tilt is bounded to ±2.5° vertically and ±3° horizontally.
- Pointer cancellation, leaving and preference changes clear pending frames and inline effects; listeners do not accumulate.
- Touch pointer events do not trigger cursor-driven effects.
- Visible focus, forced-colors and reduced-motion styles are present.
- No continuous animation loops, third-party JavaScript, remote font requests, tracking, forms or extra navigation.
- Both links remain native HTML anchors and work independently of JavaScript.
- Initial page resources total approximately 153 KB before HTTP compression. The 40 KB camera image is the only generated image loaded by the live page; the full-resolution source PNG, source TTF fonts and sharing preview are not loaded by the page.

## Visual and responsive review

The new camera artwork and the designed sharing graphic were visually inspected. The stylesheet was reviewed for layout and text-fit risks: desktop and tablet use two opposing, angled cards; screens up to 640 px use a separate stacked composition with repositioned props; a further rule adapts screens up to 360 px. Font-metric checks were used to refine narrow card-title spacing. Short-height desktop adjustments are restricted to wider screens so they do not enlarge tablet decorations into the logo area.

**Browser rendering and real-device testing could not be performed because the supported browser-testing capability was unavailable in this session.** Source, color and interaction checks do not establish that actual viewport layouts, hover appearance, touch behavior, zoom or cross-browser rendering have been exercised.

Recommended final browser checks after upload: 320 × 568, 375 × 812, 390 × 844, 768 × 1024, 1024 × 768, 1440 × 900 and 1920 × 1080. Check horizontal overflow, both destination links, keyboard focus, 200% zoom and reduced motion in Safari/iOS, Chrome/Android and Firefox.

The social preview is a separately designed sharing graphic, not a website screenshot. The complete original logo is included unchanged; the display logo removes only the original transparent margins.

## Repeatable checks

From the extracted ZIP:

```sh
python3 scripts/check-project.py
node --check script.js
node scripts/check-motion.cjs
```

These checks use the Python and Node.js standard libraries. Regenerating the sharing PNG is optional and separately requires Pillow.
