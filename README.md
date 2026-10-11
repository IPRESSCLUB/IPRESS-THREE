# IPRESS — Stay curious. Create together.

The claymorphism redesign of the IPRESS link-in-bio website: a cushioned identity badge, a sculpted camera and newspaper, soft speech bubbles, expressive typography and two tactile invitation cards. No framework, backend, installation or build step.

## Update your GitHub Pages project

This package is configured for the repository shown in your screenshots: **`IPRESSCLUB/IPRESS-THREE`**.

1. Extract **`IPRESS-Link-in-Bio.zip`** on your computer.
2. Open **https://github.com/IPRESSCLUB/IPRESS-THREE** and choose **Add file → Upload files**.
3. Upload the extracted **contents**, replacing the existing files. Keep the **`assets`** and **`scripts`** folders intact. `index.html`, `styles.css` and `script.js` belong directly at the repository root. Do not upload the ZIP itself, add an extra containing folder, or flatten the assets folder.
4. Commit the update to **`main`**.
5. In **Settings → Pages**, select **Deploy from a branch**, **`main`**, **`/(root)`**, then **Save** if those settings are not already selected.
6. When GitHub finishes deployment, open **https://ipressclub.github.io/IPRESS-THREE/**. If an older design appears, perform a hard refresh.

The package contains the whole site. No files from the older design are needed. Old loose font or helper files at the repository root can remain unused; the new page reads its assets from `assets/`.

Official reference: [GitHub Pages publishing-source instructions](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site).

### A different repository or custom domain

The page's local asset paths are relative. If you host it elsewhere, update the four absolute URL tags in `index.html`: `canonical`, `og:url`, `og:image` and `twitter:image`. Alternatively, the included optional Node.js helper updates them:

```sh
node scripts/configure-url.mjs https://your-final-domain.example/your-project/
```

The sharing image can be fetched only after the site is publicly deployed. Social apps may cache an older preview.

## Exactly two destinations

| Card | Destination |
| --- | --- |
| Explore IPRESS | https://workingharde9-ship-it.github.io/IPRESS/ |
| Join our community | https://chat.whatsapp.com/GarYt66WwYnEFJseaH64WM |

The entire card is a native link. Both open a new tab, announce that behavior to screen readers, and include `noopener noreferrer`. The links work with JavaScript disabled. No educational features, forms, galleries, testimonials or extra navigation were added.

## What changed

- A completely rebuilt, centered composition with asymmetrical media sculptures and a tilted logo cushion.
- Thick rounded cards with sculpted edge highlights, inset shading, physical-looking depth and separate clay arrow keys.
- Locally hosted **Bricolage Grotesque** for expressive headings and **DM Sans** for readable supporting text.
- A custom blue camera/newspaper illustration with transparency, optimized into a 608 × 608 WebP. Speech bubbles, the clay globe, decorative beads and cards are made in CSS/SVG.
- Short, spring-like entrance transitions, restrained desktop parallax, bounded card tilt and compressed press states. There are no continuous animation loops or animation libraries.
- A distinct mobile composition: the props move below and around the logo, typography becomes compact, and the two cards stack with subtle opposing angles.
- White, blue and green throughout the interface, including their light and dark variants and tinted shadows.

## Original logo

`assets/ipress-logo-original.png` is your complete 519 × 481 upload, preserved byte for byte. `assets/ipress-logo.png` contains the identical 296 × 61 visible logo artwork without the surrounding empty transparent margins. No visible logo pixels were redrawn, recolored or retouched. Only the surrounding cushion and decorative scene have changed.

## Accessibility and performance

- Semantic main, section, navigation and footer elements; one descriptive main heading.
- Large whole-card touch targets and visible keyboard focus.
- Descriptive native links and decorative graphics hidden from assistive technology.
- Core text colors meet a 4.5:1 contrast target against their flat base surfaces.
- `prefers-reduced-motion` disables animation and transitions, including live preference changes; pointer effects are omitted for touch/coarse pointers.
- Forced-colors rules preserve clear link and focus boundaries.
- Fonts and illustrations are local. No analytics, cookies, remote font requests or third-party runtime dependencies.

See **`VERIFICATION.md`** for completed checks and the browser-testing limitation. The included 1200 × 630 social preview is a designed sharing graphic, not a screenshot of the website.

## Files

| File or folder | Purpose |
| --- | --- |
| `index.html` | Page content, exact links, accessibility and SEO/social metadata |
| `styles.css` | New responsive claymorphism layout, visual effects and motion preferences |
| `script.js` | Optional progressive pointer enhancement |
| `assets/ipress-logo*.png` | Original logo files |
| `assets/clay-camera.webp` | Optimized website illustration |
| `assets/clay-camera-source.png` | Original full-resolution generated illustration |
| `assets/bricolage-grotesque.*` | Local display font, WOFF and source TTF |
| `assets/dm-sans*.woff` | Local text fonts |
| `assets/dm-sans*.ttf` | Source text fonts |
| `assets/*-OFL.txt` | SIL Open Font License notices |
| `assets/social-preview.png` | New sharing graphic |
| `scripts/configure-url.mjs` | Optional hosting URL updater |
| `scripts/create-social-preview.py` | Sharing-graphic source; requires Pillow only to regenerate |
| `scripts/check-project.py` | Dependency-free asset, link, logo, metadata and contrast checks |
| `scripts/check-motion.cjs` | Dependency-free JavaScript interaction checks |
| `ASSETS.md` | Artwork source, generation method and original prompt |
| `.nojekyll` | Static GitHub Pages publishing marker |

The working checkout stores public files in `dist/`. This downloadable ZIP places them at its root for direct upload.

## Optional local preview and checks

Open `index.html` directly, or serve the extracted folder with `python3 -m http.server 8080` and visit `http://localhost:8080`.

```sh
python3 scripts/check-project.py
node --check script.js
node scripts/check-motion.cjs
```

To regenerate the sharing graphic, install Pillow in your own Python environment and run `python3 scripts/create-social-preview.py`. The shipped PNG is already complete; the live site needs neither Python nor Node.js.

IPRESS branding belongs to its respective owner. Font licenses are supplied alongside the font files.
