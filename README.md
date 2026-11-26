# walletfeed-site

The WalletFeed website: landing page, privacy policy, support and webhook format. Plain HTML and
CSS, served by GitHub Pages from `main` at https://walletfeed.app. The domain is on Cloudflare, and
`CNAME` holds it. There's no build step, and no cookies or analytics.

The privacy policy repeats the app's privacy statement (`PrivacyView.swift` in the app repo) for the
version on the App Store. Change both together, with a new date on each, when that version ships. A
change that arrives with the next app version waits on the site's `release-<version>` branch. The public contact address is
support@walletfeed.app.

The icons in `assets/` come from `scripts/brand_icons.py` in the app repo, which writes them here
(`--flat --site PATH` renders them on any OS). The cover comes from `scripts/brand_cover.py`.

A sale notice is in `index.html` twice, hidden: at the top and above the plans in Pricing.
`assets/sale.js` shows it only between the sale's two instants, by the visitor's clock, and sets no
cookie, stores nothing and sends nothing. Outside those dates, and without JavaScript, the page is
unchanged, and the notice isn't in the page's Markdown copy. For a new sale, change the dates in the
script and the words in the page.

Each guide has a plain link to the App Store below its lead and Apple's badge at its foot. Beside the
badge, a reader on a computer sees a QR code for the same App Store page (`qr_svg` in
`scripts/build_pages.py`; the home page's copy is made by `app_store_badge` too). Every page has Safari's
Smart App Banner. All of these carry `ct=site`: Apple hides a source with under five downloads.

After a change is live, `scripts/indexnow.py HEAD~1` tells Bing and the other IndexNow search engines
which pages changed. Google reads `sitemap.xml`.

For crawlers and AI agents, `robots.txt` (by hand) allows everything. `scripts/agent_files.py` makes
`llms.txt`, `llms-full.txt`, `sitemap.xml` and a Markdown copy of each page (`index.md` beside its
`index.html`, linked from the page's `<head>`). Run it after changing a page and commit what it writes.

## Guides and the user guide

`src/guides/*.md` and `src/docs/*.md` hold the sources, with TOML front matter. `scripts/build_pages.py` builds the pages and their screenshots, and `scripts/ste_lint.py` checks ASD-STE100, which must show 0 errors. The pages describe the app version on the App Store. The app repo's `docs/writing/guide-changes-<version>.md` lists the changes for the next version, which go on `release-<version>` and merge when that version ships. The app repo's `.claude/skills/add-destination` skill covers adding a destination and its guide.
