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

For crawlers and AI agents, `robots.txt` (by hand) allows everything. `scripts/agent_files.py` makes
`llms.txt`, `llms-full.txt`, `sitemap.xml` and a Markdown copy of each page (`index.md` beside its
`index.html`, linked from the page's `<head>`). Run it after changing a page and commit what it writes.

## Guides and the user guide

`src/guides/*.md` and `src/docs/*.md` hold the sources, with TOML front matter. `scripts/build_pages.py` builds the pages and their screenshots, and `scripts/ste_lint.py` checks ASD-STE100, which must show 0 errors. The pages describe the app version on the App Store. The app repo's `docs/writing/guide-changes-<version>.md` lists the changes for the next version, which go on `release-<version>` and merge when that version ships. The app repo's `.claude/skills/add-destination` skill covers adding a destination and its guide.
