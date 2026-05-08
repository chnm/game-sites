# game-sites

Hugo sites for RRCHNM games, sharing a single theme:

- **`games-hub/`** → production target `games.rrchnm.org` — RRCHNM Red `#C32A26`
- **`plague-site/`** → production target `1665plague.rrchnm.org` — GMU Teal `#008285` (Pantone 321C)
- **`shipping-site/`** → production target `1812shipping.rrchnm.org` — GMU Navy `#004F71` (Pantone 653C)
- **`illuminated-site/`** → production target `illuminated.rrchnm.org` — Manuscript Olive `#8B6F1F`
- **`themes/rrchnm/`** — shared theme. The sites differ in colors, content, and which page layouts they override.

Brand fonts: Figtree · Noto Serif · Open Sans (GMU brand stack).

## Quick links

- Repo: <https://github.com/jmotis/game-sites>
- Live preview (until production domains are configured):
  - Landing: <https://jmotis.github.io/game-sites/>
  - Hub: <https://jmotis.github.io/game-sites/hub/>
  - Plague: <https://jmotis.github.io/game-sites/plague/>
  - Shipping (Learning the Ropes): <https://jmotis.github.io/game-sites/shipping/>
  - Illuminated (Adventures in Illuminating): <https://jmotis.github.io/game-sites/illuminated/>
- Plague Twine game (external): <https://jmotis.github.io/GamingtheGreatPlague>
- Adventures in Illuminating Twine game (external): <https://jmotis.github.io/Adventures-in-Illuminating.html>

---

## Local development

### 1. Install Hugo (extended edition)

| Platform | Command |
|---|---|
| macOS | `brew install hugo` |
| Windows | `winget install Hugo.Hugo.Extended` |
| Linux | Download `.deb` from [Hugo releases](https://github.com/gohugoio/hugo/releases) and `sudo dpkg -i hugo_extended_*.deb` |

Verify: `hugo version` should print `v0.100+ … extended`.

### 2. Run a site

```bash
cd games-hub        && hugo server          # → http://localhost:1313
cd plague-site      && hugo server -p 1314  # → http://localhost:1314
cd shipping-site    && hugo server -p 1315  # → http://localhost:1315
cd illuminated-site && hugo server -p 1316  # → http://localhost:1316
```

`hugo server` watches files and live-reloads.

### 3. Build for production

```bash
cd games-hub        && hugo
cd plague-site      && hugo
cd shipping-site    && hugo
cd illuminated-site && hugo
```

Output goes to each site's `public/` (gitignored). The GitHub Actions workflow does this for you on every push to `main`.

---

## Project structure

```
.
├── themes/rrchnm/                  Shared theme (used by all four sites)
│   ├── theme.toml
│   ├── layouts/
│   │   ├── _default/
│   │   │   ├── baseof.html         HTML shell (head/header/main/footer)
│   │   │   └── single.html         Generic fallback for content/*.md
│   │   ├── about/
│   │   │   └── list.html           About page (used by all sites)
│   │   ├── pedagogical-materials/
│   │   │   ├── list.html           Lesson index — iterates section page bundles
│   │   │   └── single.html         Lesson detail page (uses .article-page CSS)
│   │   ├── partials/
│   │   │   ├── head.html           <head>: meta, fonts, CSS, theme color vars
│   │   │   ├── header.html         Top nav (brand mark + menu)
│   │   │   ├── footer.html         Coloured separator + copyright + Contact Us
│   │   │   ├── rrchnm-mark.html    SVG: 4-square C/H/N/M logo
│   │   │   └── orn-rule.html       Decorative section divider (h2)
│   │   └── shortcodes/
│   │       ├── bundleimg.html      Image lookup against the page bundle
│   │       └── staticimg.html      Image under static/, resolved via relURL
│   └── static/css/
│       └── style.css               Full design system (CSS custom properties)
│
├── games-hub/                      games.rrchnm.org
│   ├── config.toml                 Site name, palette, menu, contactEmail
│   ├── content/                    Page bodies (Markdown)
│   │   ├── _index.md               Home page intro paragraph (drop cap)
│   │   ├── about/_index.md         About page title
│   │   ├── bibliography/_index.md  Bibliography title
│   │   └── games/_index.md         Current Games title
│   ├── data/                       Structured content (YAML)
│   │   ├── games.yaml              Current games (featured: true → home hero)
│   │   ├── in_development.yaml     Upcoming games (smaller cards, list page only)
│   │   ├── bibliography.yaml       Sectioned bibliography (label + entries)
│   │   └── about_sections.yaml     Project Team / RRCHNM / GMU blocks
│   ├── layouts/                    Hub-only page layouts
│   │   ├── index.html              Home (hero, drop-cap intro, Featured Game, Quick Facts)
│   │   ├── games/list.html         Current Games page
│   │   └── bibliography/list.html  Bibliography page
│   └── static/images/              Hero, period images, game cover art
│
├── plague-site/                    1665plague.rrchnm.org
│   ├── config.toml                 (markup.goldmark.renderer.unsafe = true so
│   │                                glossary's <dl> renders rather than escapes)
│   ├── content/
│   │   ├── _index.md               Home drop-cap intro
│   │   ├── about/_index.md
│   │   └── pedagogical-materials/
│   │       ├── _index.md           Pedagogy index title + subtitle
│   │       ├── student-organizer-worksheet/
│   │       │   ├── index.md        Page bundle — content + front-matter pdf:
│   │       │   └── PlagueGameOrganizer-Worksheet.pdf
│   │       ├── learning-activity/
│   │       │   ├── index.md
│   │       │   ├── Belson.png      Primary source images, referenced via
│   │       │   └── TheCure.png     {{< bundleimg src="…" >}} from the markdown
│   │       └── glossary/
│   │           ├── index.md        <dl> of historical terms
│   │           └── glossary.pdf
│   ├── data/
│   │   └── about_sections.yaml     (per-site — sites may diverge over time)
│   ├── layouts/
│   │   └── index.html              Home (hero, CTA bar, drop cap, pillars,
│   │                                closing period image)
│   └── static/images/              lord-have-mercy (hero), runaways-fleeing (closing)
│
├── shipping-site/                  1812shipping.rrchnm.org
│   ├── config.toml                 Includes primaryOnDark = "#FFC733" (gold) so
│   │                                the deep-navy primary doesn't fail SC 1.4.11
│   │                                contrast on the dark header surface
│   ├── content/
│   │   ├── _index.md
│   │   ├── about/_index.md
│   │   └── pedagogical-materials/_index.md  (no lesson bundles yet)
│   ├── data/
│   │   └── about_sections.yaml
│   ├── layouts/
│   │   └── index.html              Home (hero, CTA bar, drop cap, pillars,
│   │                                closing period image)
│   └── static/images/              harbour (hero), World-1812 (closing)
│
├── illuminated-site/               illuminated.rrchnm.org
│   ├── config.toml                 Olive palette + primaryOnDark = "#FFC733"
│   │                                (same dark-header rationale as shipping)
│   ├── content/
│   │   ├── _index.md
│   │   ├── about/_index.md
│   │   └── pedagogical-materials/_index.md  (no lesson bundles yet)
│   ├── data/
│   │   └── about_sections.yaml
│   ├── layouts/
│   │   └── index.html              Home (gradient hero placeholder, CTA bar,
│   │                                drop cap, pillars; no closing image yet)
│   └── static/images/              empty — drop hero / closing art when ready
│
├── landing/                        Root index for the GitHub Pages preview
│   └── index.html                  Four-card preview at jmotis.github.io/game-sites/
│
├── .github/workflows/
│   └── deploy.yml                  Builds all four sites & deploys to Pages
│
└── .gitignore                      Excludes public/, resources/, .hugo_build.lock
```

---

## Editing content

The pattern across the codebase: **structured/repeating items live in `data/*.yaml`; pages with their own URL or substantive prose live in `content/*.md`**. Layouts read from both. Most edits are pure data — no template changes required.

### Add a new current game (hub)

1. Open `games-hub/data/games.yaml`.
2. Append a new entry. Required: `title`, `url`. Optional: `subtitle`, `description`, `image`, `image_alt`, `image_caption`, `cover`, `featured`, `teachers_url`.
3. If you want it to be the home page's "★ Featured Game" hero block, set `featured: true` (and clear it on the previous featured entry — only one should be true).
4. Drop a **square (1:1)** cover image into `games-hub/static/images/`. Reference it in `image: "your-file.jpg"`. Set `cover: true` to skip the sepia filter and treat it as a logo, not a historical engraving.

```yaml
- title:        "Game Title"
  subtitle:     "Place · Century · MS / HS / Undergrad"   # CSS uppercases on render
  description:  "One sentence — what's the game about?"
  url:          "https://example.com/play-the-game"
  teachers_url: "https://example.com/pedagogy"            # optional, adds For Teachers → button
  image:        "filename.jpg"                            # in static/images/
  image_alt:    "Description of the cover art for screen readers"
  cover:        true                                      # game logo (1:1, no sepia)
  featured:     false                                     # true → home-page hero
```

The new game appears automatically on the `/games/` Current Games page (always) and on the hub home (only if `featured: true`).

### Add an in-development game

`games-hub/data/in_development.yaml`. Same shape as games but smaller cards, no image, no `teachers_url`. Renders only on the `/games/` page (the hub home now uses **Quick Facts** instead — see below).

```yaml
- title:       "Game Title"
  subtitle:    "Place · Century · MS / HS / Undergrad"
  description: "One sentence pitch."
```

### Quick Facts list (hub home)

The hub home page's bottom block is hard-coded in `games-hub/layouts/index.html` as a `<ul class="quick-facts">` (red-square bullets, mirrors the bibliography style). Edit the bullets directly in the layout. The "bibliography" link in the last bullet uses `relURL` so it works under both production and preview baseURLs.

### Update bibliography (hub)

`games-hub/data/bibliography.yaml` is a list of **sections**, each with a `label` (rendered as an `<h2>` divider — same eyebrow treatment as the about page) and a list of `entries`. Each entry has a `text` field (HTML allowed via `safeHTML`) and an optional `url`.

```yaml
- label: "Scholarship"
  entries:
    - text: 'Author. (Year). <em>Title</em>. Publisher.'
      url:  'https://example.com/'
    - text: '...'

- label: "Primary Sources"
  entries:
    - text: '...'
```

Add or split sections by adding more top-level `- label:` blocks. Entries within a section render as a `<ul>` with red-square bullets.

### Update About sections (per site)

Each site has its own `data/about_sections.yaml` (`games-hub/`, `plague-site/`, `shipping-site/`, `illuminated-site/`). They were originally near-identical but the sites are expected to diverge over time as each game's project team and credits evolve. Edit per site as needed; no automatic sync.

Each section: `label` (eyebrow, becomes an `<h2>`) + `body` (HTML allowed via `safeHTML`).

### Add or edit a pedagogical-materials lesson (plague, future shipping)

Lessons are **Hugo page bundles** under each site's `content/pedagogical-materials/`. Each lesson is a folder with an `index.md` and any co-located assets (PDFs, images).

To add a lesson:

```
plague-site/content/pedagogical-materials/your-new-lesson/
├── index.md
└── your-new-lesson.pdf      # opened directly by the list's "View" button
```

`index.md` front matter:

```yaml
---
title: "Lesson Title"
description: "One-sentence subtitle, shown on the list and as a page intro."
weight: 4                              # ordering on the index page
meta: "Worksheet"                      # small label on the index row
pdf: "your-new-lesson.pdf"             # bundle-relative filename
---

Markdown body, including any inline images. (Currently only rendered if a
visitor navigates to the lesson's detail URL directly — the index links
straight to the PDF.)
```

Inline images that live next to `index.md` use the `bundleimg` shortcode (errors loudly if the file isn't found — catches typos at build time):

```markdown
{{< bundleimg src="diagram.png" alt="…" >}}
```

The lesson appears automatically on `/pedagogical-materials/` (sorted by `weight`) with the meta label and a `View →` button. When `pdf:` is set, that button links straight to the bundled PDF, so visitors land in the browser's built-in PDF viewer (with its native download control); when `pdf:` is omitted the button falls back to the lesson's detail page.

### Update the navigation menu

Each site's `config.toml` → `[[menus.main]]` blocks. Each: `name`, `url`, `weight` (sort order). External links pass through `relURL` unchanged; internal paths like `/about/` get the right baseURL prefix automatically via the menu template.

### Update the home-page drop-cap intro

Each site's `content/_index.md`. The drop cap is rendered via CSS `::first-letter` — write normal prose, the first letter becomes large automatically. **Don't** quote or otherwise prefix the text or `::first-letter` won't match.

### Update the footer / contact email

Each site's `config.toml` → `[params].contactEmail`. Used in the mailto link and the visible button text.

---

## Adding a new game info site (cookbook)

Suppose you want a dedicated site for *Adventures in Illuminating* (like `plague-site/` and `shipping-site/`), to live at e.g. `illuminating.rrchnm.org`.

**Standard subsite home-page layout.** Every game subsite home page follows the same six-section order, with images only at the top and bottom:

1. Hero (full-bleed image + dark gradient + title)
2. CTA bar (Play the Game / For Teachers buttons)
3. Drop-cap intro paragraph (from `content/_index.md`)
4. "Inside the Game" ornamental divider
5. Three pillar callouts
6. Closing period image (`.period-block` with caption bar)

### Steps

1. **Copy a sibling site as the template:**
   ```bash
   cp -r shipping-site illuminating-site
   ```
2. **Update `illuminating-site/config.toml`:**
   - `baseURL` → production URL
   - `title`, `[params].siteName`, `[params].tagline`
   - `[params].primary` and the related `primaryDark` / `primaryDeep` / `primarySoft` shades. Use brand-palette values; derive AA-compliant variants.
   - **If your `primary` colour fails 3:1 contrast on the dark header surface (`#1F1B16`)**, set `primaryOnDark` to a brand-approved colour that clears 3:1 (the shipping site uses GMU Gold `#FFC733`). Otherwise omit and the nav underline / focus ring will inherit `--primary`.
   - `[[menus.main]]` items → home, game URL, pedagogical-materials, about
3. **Replace content & data.** Edit each file under `content/` (home prose, about title) and `data/` (about_sections). Keep `data/about_sections.yaml` even if it duplicates a sibling site for now — the sites may diverge.
4. **Drop in the new site's two images** at `illuminating-site/static/images/`. The standard subsite home uses exactly two images: a full-bleed **hero** at the top and a **closing period image** at the bottom (a `.period-block` with caption bar). Edit `layouts/index.html` to point at your filenames, or rename your files to match. There are no mid-page images on the home page.
5. **Hook it into the build & landing page:**
   - In `.github/workflows/deploy.yml`, add a Build step modeled on the existing ones:
     ```yaml
     - name: Build illuminating-site → public/illuminating/
       env:
         HUGO_ENVIRONMENT: production
       run: |
         hugo --gc --minify \
           --source illuminating-site \
           --destination "${GITHUB_WORKSPACE}/public/illuminating" \
           --baseURL "${{ steps.pages.outputs.base_url }}/illuminating/"
     ```
   - In `landing/index.html`, add a card linking to `illuminating/` (mirror the existing three; add a `.card--illuminating` background colour).
6. **Add to the hub.** In `games-hub/data/games.yaml`, set the Adventures entry's `teachers_url` to the new site's `/pedagogical-materials/` URL.
7. **(Optional) Add lessons.** Drop content/pedagogical-materials/<slug>/index.md page bundles when you have real materials. The shared theme layouts will render them automatically.

That's it — push and the new site appears at `https://jmotis.github.io/game-sites/illuminating/`. When the production domain is configured, the workflow's `--baseURL` override is what matters, not the value baked into the site's `config.toml`.

---

## Theme architecture

### One theme, many sites — colors via custom properties

`themes/rrchnm/static/css/style.css` defines a complete design system using CSS custom properties:

```css
:root {
  --primary:         #C32A26;     /* defaults — overridden per site */
  --primary-dark:    …;
  --primary-deep:    …;
  --primary-soft:    …;
  --primary-on-dark: var(--primary);   /* per-site override if primary
                                          fails 3:1 on dark header */
  --sans:   'Figtree', …;
  --serif:  'Noto Serif', …;
  --body:   'Open Sans', …;
}
```

Per-site overrides come from `themes/rrchnm/layouts/partials/head.html`, which injects an inline `<style>` block reading `.Site.Params.primary` etc. from each site's `config.toml`. The whole site re-themes by changing four hex codes (plus the optional `primaryOnDark`) in the config.

### Page-bundle convention for content with assets

Sections that have detail pages with co-located assets (currently: plague's `pedagogical-materials/`) use Hugo **page bundles** — a folder with `index.md` plus any PDFs / images. Pros: lifecycle is unified (delete the page, its assets go with it); URLs are semantic (`/pedagogical-materials/glossary/glossary.pdf`); Hugo's `.Resources.GetMatch` resolves bundle-relative paths under any baseURL.

The shared theme's `pedagogical-materials/list.html` reads each lesson's optional `pdf:` front-matter value via `.Resources.GetMatch`; when present, the `View →` button links directly to the bundled PDF (browser-native viewer, native download control). The fallback `pedagogical-materials/single.html` still exists for lessons without a PDF and renders a Download PDF button when one is attached.

### Shortcodes

| Shortcode | Use when… |
|---|---|
| `{{< bundleimg src="…" alt="…" >}}` | image lives next to the page's `index.md` (page bundle) |
| `{{< staticimg src="…" alt="…" >}}` | image lives under `static/` (e.g. layout-side hero / period art) |

`bundleimg` errors loudly at build time if the named resource isn't in the bundle (catches typos). `staticimg` strips a leading `/` and pipes through `relURL` so the URL works under both production and Pages-preview baseURLs.

### URL handling — Hugo's `relURL` quirks

Both the production deploy (root domain) and the Pages preview (subpath like `/game-sites/hub/`) need to work. Three non-obvious rules:

1. **Hugo's `relURL "/about/"` returns `/about/` unchanged** (it treats leading-slash strings as already-absolute paths). To get subpath-aware URLs, drop the leading slash: `relURL "about/"` correctly returns `/game-sites/hub/about/` under a subpath baseURL.
2. **The brand link's home URL** uses `.Site.Home.RelPermalink` (not `relURL "/"`) for the same reason.
3. **Menu items configured with `url = "/about/"`** *do* get processed correctly by Hugo's menu system — those leading slashes are fine. The menu-only quirk: pipe `.URL` through `relURL` in the template (`{{ .URL | relURL }}`).

If you need to hardcode a path in a layout, use `{{ "path/" | relURL }}` (no leading slash). External URLs with a scheme (`https://…`) pass through `relURL` unchanged.

### Cover art convention

Two image styles, distinguished by the `--cover` CSS modifier:

- **`.hist-img`** (default) — historical engravings. Sepia tinted (`filter: sepia(0.18) contrast(1.05)`), `object-fit: cover` (will crop). Used for hero images, period plates, banners.
- **`.hist-img--cover`** — modern game cover art. No sepia, square 280×280 slot, centered in its column, `object-fit: contain`. Triggered by `cover: true` in `data/games.yaml`.

The shipping-site's hero image (a Dominic-Serres-style oil painting) explicitly disables the sepia filter inline in the layout, since the painting is already aged-warm and the brand navy accent reads better against true colour.

### Optional data fields

Layouts use `{{ with .field }}` to gracefully skip rendering when a field is empty or missing. This is why a game can be added with only `title` + `url` and still render correctly. Pattern:

```html
{{- with $game.subtitle }}
<p class="featured-game__meta">{{ . }}</p>
{{- end }}
```

When you add a new optional field to YAML, follow the same pattern in the template.

### Page-level layout overrides

Hugo searches each site's `layouts/` directory before falling back to the theme's. The theme provides:

- `_default/single.html` (generic fallback)
- `about/list.html` (About page)
- `pedagogical-materials/list.html` and `single.html` (lessons)

Each site overrides home (`index.html`) and any other page that needs custom design. To override a theme layout for one site only, copy the file from `themes/rrchnm/layouts/…` to `<site>/layouts/…` and edit.

### Markdown raw-HTML

The plague site sets `[markup.goldmark.renderer] unsafe = true` in `config.toml` so the glossary's `<dl>` markup renders rather than being escaped. Add the same setting in any site that needs raw HTML in markdown content.

---

## Design system reference

### Brand palette (source of truth)

The official brand palette these sites draw from. These are the canonical hex values; the per-site `--primary*` tokens below are derived from them.

| Name | Hex |
|---|---|
| George Mason Green | `#005239` |
| George Mason Gold | `#FFC733` |
| PANTONE Black 7C (Black) | `#333333` |
| PANTONE 173C (Red) | `#CC4824` |
| PANTONE 321C (Teal) | `#008285` |
| PANTONE 653C (Navy) | `#004F71` |
| PANTONE Cool Grey 10 | `#727579` |
| True Black | `#000000` |
| RRCHNM Red | `#C32A26` |

Don't substitute approximations — the brand wordmark, primary buttons, and per-site accents must use these exact values.

### Per-site colour tokens

| Token | Hub (Red) | Plague (Teal) | Shipping (Navy) | Illuminated (Olive) |
|---|---|---|---|---|
| `--primary` | `#C32A26` | `#008285` | `#004F71` | `#8B6F1F` |
| `--primary-dark` (AA on white) | `#A02220` | `#006568` | `#003B58` | `#6F5818` |
| `--primary-deep` | `#761815` | `#00484A` | `#002A40` | `#463710` |
| `--primary-soft` (subtle bg) | `#F7E7E6` | `#E5F1F1` | `#E5EDF2` | `#F0E9D2` |
| `--primary-on-dark` (header surface) | inherits `--primary` | inherits `--primary` | `#FFC733` (gold) | `#FFC733` (gold) |

Shared across all sites: `--ink #1A1A1A`, `--deep #004F71`, `--page-bg #FFFDF8`, `--dark-bg #0F0E0C`.

WCAG 2.1 AA was a hard requirement. The dark/light pairings have been hand-checked but should be re-verified with axe DevTools or Lighthouse before launch (focus states on links are the most likely audit finding).

### Page-width convention

Three site-wide content widths, picked by content density:

| Width | Used by |
|---|---|
| 880px | `.about-inner` — most reading-focused |
| 980px | `.bib-inner`, `.article-page` — text-heavy detail content |
| 1080px | `.pedagogy-inner` — section index / list / overview |

All three sit inside `.page-body` (max-width 1280px, padding 0 48px), centred via `margin: 0 auto`.

### End-of-content gap convention

`.site-footer` has `margin-top: 80px`. Inner-wrapper bottom padding is intentionally `0` so the wrapper's last child's `margin-bottom` collapses with the footer's `margin-top` (the larger wins → 80px visible). The plague/shipping `.period-block` and the hub `.card-section` use `margin-bottom` (not `padding-bottom`) for the same reason. Don't add `padding-bottom` to inner wrappers — it stacks on top of the 80px footer margin instead of collapsing into it.

### Fonts

| Token | Stack | Used for |
|---|---|---|
| `--serif` | Noto Serif, Cambria, Georgia | Headlines, page titles, drop caps, brand wordmark |
| `--sans` | Figtree, Open Sans, Franklin Gothic, system-ui | Eyebrow labels, nav, buttons, meta |
| `--body` | Open Sans, Figtree, Franklin Gothic, system-ui | Reading copy, body paragraphs |

Loaded from Google Fonts via `themes/rrchnm/layouts/partials/head.html`. Fallbacks are GMU's "approved alternates" (Cambria, Franklin Gothic).

### Reusable components / class names

- `.site-header` / `.site-nav` — top bar
- `.hero` + `.hero__img` + `.hero__title` — full-bleed hero with gradient overlay
- `.cta-bar` — light bar below hero with two centered buttons (plague, shipping)
- `.btn` + `.btn--primary` / `.btn--inverse` / `.btn--ghost` / `.btn--contact` / `.btn--download`
- `.btn-row` — flex container for two adjacent buttons (e.g. Play the Game + For Teachers)
- `.featured-game` + `.featured-game__grid` — hub home Featured Game block
- `.featured-game__grid--solo` — single-column variant when a game has no image yet
- `.card` + `.card__meta` + `.card__title` + `.card__desc` — In Development mini-cards (Current Games page)
- `.orn-rule` — decorative section divider, **is the `<h2>`** (line + ornament + label + ornament + line)
- `.pillars` + `.pillar` — three-column inside-the-game block (plague, shipping)
- `.bib-list` + `.bib-entry` — bibliography list with red-square bullets
- `.quick-facts` + `.quick-facts__item` — same red-square bullet treatment for the hub home Quick Facts list
- `.lessons` + `.lesson` (+ `.lesson--alt`) — alternating-row pedagogy index grid
- `.about-section` + `.about-section__label` + `.about-section__body` — about page sections; label is an `<h2>`
- `.article-page` + `.article-page__header` / `__pdf` / `__body` — generic prose detail page (used by pedagogy lessons; reusable for any future single-page content section)
- `.page-rule` — `<hr>` divider with the `1px solid var(--dark-bg)` styling and standard 80/56 vertical rhythm
- `.hist-img` (sepia) / `.hist-img--cover` (no sepia, square)
- `.drop-cap-section` (+ `--plague` for larger cap) — first-letter drop cap via CSS `::first-letter`

---

## Deployment

### GitHub Pages (current)

Pushes to `main` trigger `.github/workflows/deploy.yml`. The workflow:

1. Installs Hugo extended.
2. Builds `games-hub/` with `--baseURL "<pages-base>/hub/"` → `public/hub/`.
3. Builds `plague-site/` with `--baseURL "<pages-base>/plague/"` → `public/plague/`.
4. Builds `shipping-site/` with `--baseURL "<pages-base>/shipping/"` → `public/shipping/`.
5. Builds `illuminated-site/` with `--baseURL "<pages-base>/illuminated/"` → `public/illuminated/`.
6. Copies `landing/index.html` to `public/index.html`.
7. Uploads & deploys the combined `public/` to GitHub Pages.

**One-time setup** (already done): repo Settings → Pages → Build and deployment → Source: **GitHub Actions** (not "Deploy from a branch").

### Production (custom domains)

When the production domains are ready:

1. Each site needs its own deploy (separate hosting, separate repo, or a different workflow that targets each domain).
2. The `baseURL` in each site's `config.toml` is already correct for production. The Pages workflow's `--baseURL` flag overrides it for the preview.
3. **Update the `teachers_url` in `games-hub/data/games.yaml`** from the github.io subpath to the production URL `https://1665plague.rrchnm.org/pedagogical-materials/`. There's a `TODO` comment marking the line.
4. Production won't need the subpath URL gymnastics in the templates — the existing path-handling works correctly at root.

---

## Open TODOs

Search the codebase for `TODO` to find the live list. Currently:

- `games-hub/data/games.yaml` — Plague `teachers_url` to swap to production at deploy
- `games-hub/data/games.yaml` — Adventures in Illuminating still needs a `teachers_url` if pedagogy materials exist
- `games-hub/data/about_sections.yaml`, `plague-site/data/about_sections.yaml`, `shipping-site/data/about_sections.yaml` — RRCHNM blurb has a probable typo: *"the center which as developed"* → likely *"which has developed"*
- Shipping has no real lesson content yet — `content/pedagogical-materials/` has only the section `_index.md`. Add lesson page bundles when materials exist.

### Things never built (in the original design but unimplemented)

- Plague About page styling beyond the inherited About template (currently uses generic title "About"; consider a stylistically-parallel title like "Behind the game.")
- Skip-link styling beyond the basic visible-on-focus; visible focus states on nav links could be more pronounced
- Mobile/responsive review — the layout is desktop-first; narrow viewports haven't been audited beyond ad-hoc fixes
- Real 404 page (Hugo defaults to a basic one)

---

## Working in a new Claude session

If you want to continue this work in a new chat, here's what an AI assistant needs to know up front:

1. **Source of design intent.** The original prototypes from Claude Design (HTML/JSX in a separate handoff bundle) are *not* in this repo. They've been faithfully translated into the Hugo theme; the theme's CSS is now the source of truth for the design. Direction D was the chosen direction (Broadside-style body + editorial header).

2. **Four sites, one theme.** Don't duplicate logic across `games-hub/`, `plague-site/`, `shipping-site/`, and `illuminated-site/` — most things belong in `themes/rrchnm/`. Site-level overrides exist only for layouts that genuinely differ (home pages, hub-specific list pages).

3. **Data-driven content.** Adding a game, in-dev card, bibliography entry, or about section is a YAML edit. Adding a lesson is a page-bundle edit (folder + index.md + assets). Resist the urge to hardcode content into layouts.

4. **Hugo gotchas already encountered.**
   - `relURL "/path/"` doesn't add the subpath — drop the leading slash (or use the `bundleimg` / `staticimg` shortcodes for images).
   - `.Site.Home.RelPermalink` for the brand-link home URL.
   - `with` shadows the context — capture the loop variable (`{{ $game := . }}`) before entering a `with` / `if` block if you need its sibling fields.
   - Bundle resources resolve via `.Page.Resources.GetMatch` in templates and via the `bundleimg` shortcode in markdown.
   - Plague enables `markup.goldmark.renderer.unsafe = true` so raw `<dl>` etc. in markdown isn't escaped. Other sites don't need it unless they use raw HTML in content.
   - Commit signing fails in this environment — use `git -c commit.gpgsign=false commit …` (or set `commit.gpgsign=false` locally).

5. **The site builds clean** under both root baseURL (production) and subpath baseURL (Pages preview). Test under both before pushing template changes:
   ```bash
   hugo -s games-hub --destination /tmp/test-root
   hugo -s games-hub --baseURL "https://jmotis.github.io/game-sites/hub/" --destination /tmp/test-sub
   ```

6. **Audience.** High-school and college history teachers (and their students). WCAG 2.1 AA is a hard requirement. Tone is academic-editorial, not playful.

7. **Asset conventions.**
   - Game cover art: 1:1 square, modern logo style (no sepia applied).
   - Historical engravings / paintings: any aspect ratio, sepia-tinted by default; can be disabled per-image when warm-toned source art doesn't want further warming.
   - Layout-side images live in each site's `static/images/` (not in the theme).
   - Lesson-side images and PDFs live next to the lesson's `index.md` as page-bundle resources.

8. **Deploy = push to main.** GitHub Actions handles the rest. Don't commit `public/` (gitignored).

9. **Tokens / secrets.** When pushing on the user's behalf, use a personal access token *they* provide. Don't store it; scrub it from the git remote URL after the push. Tokens shared in chat should be revoked after use.
