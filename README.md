# walletfeed-site

The WalletFeed website: landing page, privacy policy, support and webhook format. Plain HTML and
CSS, served by GitHub Pages from `main` at https://walletfeed.app. The domain is on Cloudflare, and
`CNAME` holds it. There's no build step, and no cookies or analytics.

The privacy policy repeats the app's privacy statement (`PrivacyView.swift` in the app repo), so
change both together and update the date on each. The public contact address is
support@walletfeed.app.

The icons in `assets/` come from `scripts/brand_icons.py` in the app repo, which writes them here
(`--flat --site PATH` renders them on any OS). The cover comes from `scripts/brand_cover.py`.

For crawlers and AI agents, `robots.txt` (by hand) allows everything. `scripts/agent_files.py` makes
`llms.txt`, `llms-full.txt`, `sitemap.xml` and a Markdown copy of each page (`index.md` beside its
`index.html`, linked from the page's `<head>`). Run it after changing a page and commit what it writes.
