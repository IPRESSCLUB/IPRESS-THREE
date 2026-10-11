# IPRESS — Create. Capture. Connect.

A compact, custom link-in-bio page for the journalism, photography and creative media club of IFMEREE Tanger. Exactly two navigation destinations, with no frameworks, package installation or build step.

## Publish on GitHub Pages

The downloadable ZIP is ready for a new repository named **`ipress-links`** in the **`workingharde9-ship-it`** account. This keeps the existing official IPRESS website at its current URL.

1. Create a **public** GitHub repository named **`ipress-links`**.
2. Extract `IPRESS-Link-in-Bio.zip` on your computer.
3. Open the repository and select **Add file → Upload files**. Upload the extracted **contents**, including the `assets` folder, then commit to `main`. **`index.html` must sit at the repository root**, alongside `styles.css` and `script.js`. Upload the files, not the ZIP itself.
4. Open **Settings → Pages**. Under **Build and deployment**, choose **Deploy from a branch**. Select **`main`** and **`/(root)`**, then **Save**.
5. When GitHub reports the deployment as complete, visit:

   **https://workingharde9-ship-it.github.io/ipress-links/**

Official reference: [Configuring a publishing source for GitHub Pages](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site).

### If you choose a different repository or domain

All visible assets use relative paths, so the page works in a repository subdirectory. The canonical URL and social-preview URLs must match the final address so sharing previews can load correctly.

Update the four URL tags in the `<head>` of `index.html` (`canonical`, `og:url`, `og:image`, and `twitter:image`), or run this optional helper with Node.js:

```sh
node scripts/configure-url.mjs https://your-final-domain.example/your-project/
```

This helper only updates metadata; no build step is required. Social apps may cache previews and may not display the new preview until the site is public and recrawled.

## Files in the download

| File | Purpose |
| --- | --- |
| `index.html` | Semantic page, exactly two native links, SEO and social metadata |
| `styles.css` | Responsive composition, typography, palette, focus styles and motion |
| `script.js` | Optional pointer-responsive highlights and restrained parallax |
| `assets/ipress-logo.png` | Display version: identical logo pixels, with only the surrounding transparent canvas omitted |
| `assets/ipress-logo-original.png` | Your complete uploaded PNG, preserved byte for byte |
| `assets/space-grotesk.woff` | Local display font |
| `assets/ibm-plex-mono.woff` | Local micro-typography font |
| `assets/social-preview.png` | Ready-made 1200 × 630 sharing preview |
| `assets/*-OFL.txt` | Font license notices |
| `assets/*.ttf` | Full fonts retained for the social-preview source script |
| `scripts/configure-url.mjs` | Optional hosting URL updater |
| `scripts/create-social-preview.py` | Social-preview source; requires Python and Pillow only if regenerating it |
| `scripts/check-project.py` | Asset, metadata, logo, link and contrast checks |
| `scripts/check-motion.cjs` | JavaScript interaction checks using Node.js |
| `VERIFICATION.md` | Checks performed and the remaining browser verification limit |
| `.nojekyll` | Tells GitHub Pages to serve the static files directly |

The working source repository stores the public files under `dist/`. The downloadable ZIP places those files directly at its root for upload.

## The two destinations

- **Explore our website** → https://workingharde9-ship-it.github.io/IPRESS/
- **Join our community** → https://chat.whatsapp.com/GarYt66WwYnEFJseaH64WM

Both are full-card links that open in a new tab with `noopener noreferrer`. Their screen-reader descriptions announce the new tab. No form, gallery, tracking, cookies, login or backend is included.

## Design and accessibility

- White, blue and green only, including tinted backgrounds and shadows.
- Space Grotesk paired with IBM Plex Mono; fonts are served locally.
- Your uploaded 519 × 481 PNG is preserved byte for byte as `assets/ipress-logo-original.png`. Its visible artwork occupies 296 × 61 pixels and matches the existing display asset pixel for pixel. The display version omits only empty transparent margins; no logo pixels are changed, recolored, redrawn or retouched.
- Desktop: editorial typography paired with the framed logo, then two equal-width destination cards.
- Mobile: logo first, a compact heading, and stacked cards with generous touch targets.
- Brief staggered entrance motion; no continuous animation loops.
- Hover effects only on compatible pointers. Touch devices retain native scrolling and tapping.
- `prefers-reduced-motion` disables animations, transitions and pointer motion, including when the preference changes while the page is open.
- High-contrast keyboard focus, semantic landmarks, image text alternative, decorative graphics hidden from assistive technology, and support for forced-colors mode.
- Both destinations remain functional without JavaScript. No remote font or animation service is required.

## Optional local preview and checks

Open `index.html` directly to preview it. For a local HTTP preview, run `python3 -m http.server 8080` in the extracted folder, then open `http://localhost:8080`.

```sh
python3 scripts/check-project.py
node --check script.js
node scripts/check-motion.cjs
```

To regenerate the social preview after changing its design, install Pillow in your own Python environment and run `python3 scripts/create-social-preview.py`. The shipped image is already generated and needs no setup.

## Rights and credits

IPRESS branding belongs to its respective owner. Your supplied `WhatsApp_Image_2025-11-28_at_7.27.21_PM__1_-removebg-preview (2).png` is included unchanged as `assets/ipress-logo-original.png`. The display asset from the earlier IPRESS project was verified against the upload: every pixel of the visible logo is identical. Space Grotesk and IBM Plex Mono are included under the SIL Open Font License; their license notices are retained alongside the fonts.
