#!/home/pph/.venv/bin/python
"""The guides and the user guide, made from Markdown in src/:

  src/guides/<slug>.md   ->  guides/<slug>/index.html and index.md    https://walletfeed.app/guides/<slug>/
  src/docs/<slug>.md     ->  docs/<slug>/index.html and index.md      https://walletfeed.app/docs/<slug>/
  (hubs)                 ->  guides/index.html, docs/index.html
  pages.json             ->  the generated pages, for scripts/agent_files.py

Each source starts with TOML front matter between +++ lines:

  title = "Send Apple Card transactions to Google Sheets"   # the page's h1
  nav_title = "Google Sheets"                                 # breadcrumbs and hub lists
  description = "…"                                           # meta description, 155 characters at most
  group = "Sheets and databases"                              # the hub section it's listed under
  order = 10                                                  # position in its group or in the user guide
  related = ["guides/apple-card-to-airtable", "docs/destinations"]
  updated = 2026-10-30

Images are Markdown images with a source prefix. The build converts each to WebP beside the page:

  ![Alt text.](app:docs-setup-google-sheets)      an app screen from build/docs-shots/raw or build/screenshots/raw
  ![Alt text.](web:pocketsmith/02-developer-keys)  a third-party screen from build/docs-capture/<service>/

Both folders are in the app repo (WALLETFEED_REPO, default ~/walletfeed), and are made by its
DocsScreenshotTests and by the capture workflow. A missing image stops the build.

  ~/.venv/bin/python scripts/build_pages.py && ~/.venv/bin/python scripts/agent_files.py
  ~/.venv/bin/python scripts/build_pages.py --check src/guides/<slug>.md   # one page, nothing written to the site
"""
import html
import json
import os
import re
import sys
import tomllib
from dataclasses import dataclass, field
from datetime import date
from pathlib import Path

from markdown_it import MarkdownIt
from mdit_py_plugins.anchors import anchors_plugin
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
SITE = "https://walletfeed.app/"
APP_REPO = Path(os.environ.get("WALLETFEED_REPO", Path.home() / "walletfeed"))
APP_SHOTS = [APP_REPO / "build/docs-shots/raw", APP_REPO / "build/screenshots/raw"]
WEB_SHOTS = APP_REPO / "build/docs-capture"

SECTIONS = {
    "guides": {"title": "Guides", "nav": "Guides",
               "description": "Step-by-step guides to send Apple Card, Apple Cash and Savings transactions from your iPhone to budgeting apps, spreadsheets, files and automations with WalletFeed.",
               "lead": "Each guide shows how to send Apple Card, Apple Cash and Savings transactions from your iPhone to one app or file type with WalletFeed."},
    "docs": {"title": "WalletFeed User Guide", "nav": "User Guide",
             "description": "How to use WalletFeed on iPhone: Wallet accounts, Spending, Ask Spending, Search, Recurring Charges, destinations, Background Sync and WalletFeed Pro.",
             "lead": "How to use each part of WalletFeed on your iPhone."},
}
# The guides hub lists its groups in this order. Any other group follows, alphabetically.
GUIDE_GROUPS = ["Budgeting apps", "Sheets and databases", "Files and desktop apps", "Automations", "Developers", "Free features", "Export"]

TRADEMARKS = ("Apple, Apple Card, Apple Cash, Apple Intelligence, Face ID, iCloud, iPhone, Siri and Wallet are trademarks of Apple Inc. "
              "WalletFeed isn’t affiliated with Apple. Other product names are trademarks of their owners.")


@dataclass
class Page:
    section: str
    slug: str
    meta: dict
    body: str
    source: Path
    images: list = field(default_factory=list)

    @property
    def path(self) -> str:
        return f"{self.section}/{self.slug}/"

    @property
    def url(self) -> str:
        return SITE + self.path

    @property
    def title(self) -> str:
        return self.meta["title"]

    @property
    def nav_title(self) -> str:
        return self.meta.get("nav_title", self.title)


def read_page(section: str, source: Path) -> Page:
    text = source.read_text()
    match = re.match(r"\+\+\+\n(.*?)\n\+\+\+\n", text, re.S)
    if not match:
        sys.exit(f"{source}: no +++ front matter")
    meta = tomllib.loads(match.group(1))
    for key in ("title", "description"):
        if key not in meta:
            sys.exit(f"{source}: front matter needs {key}")
    if len(meta["description"]) > 160:
        sys.exit(f"{source}: description is {len(meta['description'])} characters (160 at most)")
    return Page(section, source.stem, meta, text[match.end():], source)


# Images

def resolve_image(ref: str, page: Page) -> tuple[Path, str]:
    """A source PNG and the WebP file name it becomes beside the page."""
    kind, _, name = ref.partition(":")
    if kind == "app":
        for folder in APP_SHOTS:
            if (folder / f"{name}.png").exists():
                return folder / f"{name}.png", "walletfeed-" + re.sub(r"^(docs-|\d\d-)", "", name) + ".webp"
        sys.exit(f"{page.source}: app screenshot {name}.png isn't in {', '.join(map(str, APP_SHOTS))}")
    if kind == "web":
        service, _, file = name.partition("/")
        png = WEB_SHOTS / service / f"{file}.png"
        if not png.exists():
            sys.exit(f"{page.source}: web screenshot {png} doesn't exist")
        return png, f"{service}-" + re.sub(r"^\d\d-", "", file) + ".webp"
    sys.exit(f"{page.source}: image {ref!r} needs an app: or web: prefix")


def convert_image(source: Path, out: Path) -> tuple[int, int, bool]:
    """Writes the WebP once (again only when the source is newer). Returns its size and whether
    it's a phone screen, which shows narrower."""
    with Image.open(source) as image:
        phone = image.height > image.width * 1.3
        width = 640 if phone else min(image.width, 1440)
        height = round(image.height * width / image.width)
        if not out.exists() or out.stat().st_mtime < source.stat().st_mtime:
            out.parent.mkdir(parents=True, exist_ok=True)
            image.convert("RGB").resize((width, height), Image.LANCZOS).save(out, "WEBP", quality=82, method=6)
    return width, height, phone


# Markdown

def markdown(page: Page) -> MarkdownIt:
    md = MarkdownIt("commonmark", {"html": False, "typographer": False}).enable("table")
    md.use(anchors_plugin, min_level=2, max_level=3, slug_func=slugify)

    def image(renderer, tokens, idx, options, env):
        token = tokens[idx]
        ref = token.attrGet("src")
        alt = "".join(child.content for child in token.children or [])
        source, name = resolve_image(ref, page)
        width, height, phone = convert_image(source, ROOT / page.path / name)
        page.images.append({"ref": ref, "file": name, "alt": alt, "phone": phone, "width": width, "height": height})
        css = "shot phone" if phone else "shot web"
        shown = (width // 2, height // 2)
        return (f'<img class="{css}" src="{name}" alt="{html.escape(alt)}" width="{shown[0]}" height="{shown[1]}" '
                f'loading="lazy" decoding="async">')

    md.add_render_rule("image", image)
    return md


def slugify(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


def postprocess(body: str) -> str:
    """Notes, links to other pages, and figures for images that stand alone."""
    body = re.sub(r"<blockquote>\s*<p><strong>(Note|Important|Caution|Warning):</strong>", r'<aside class="note"><p><strong>\1:</strong>', body)
    body = re.sub(r"(<aside class=\"note\">.*?)</blockquote>", r"\1</aside>", body, flags=re.S)
    body = re.sub(r"<p>(<img [^>]+>)</p>", r"<figure>\1</figure>", body)
    # Two phone screens in a row sit side by side.
    body = re.sub(r"(<figure><img class=\"shot phone\"[^>]+></figure>\s*){2,}",
                  lambda m: '<div class="pair">' + m.group(0) + "</div>", body)
    body = body.replace("<table>", '<div class="table"><table>').replace("</table>", "</table></div>")
    return body


# HTML

def page_html(page: Page, body: str, crumbs: list[tuple[str, str]], extra: str = "") -> str:
    meta = page.meta
    depth = page.path.count("/")
    up = "../" * depth
    image = next((i for i in page.images if not i["phone"]), page.images[0] if page.images else None)
    og_image = (page.url + image["file"]) if image else SITE + "assets/icon-512.png"
    updated = str(meta.get("updated", date.today()))
    breadcrumb_ld = {
        "@context": "https://schema.org", "@type": "BreadcrumbList",
        "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": name, "item": SITE + href}
                            for i, (name, href) in enumerate(crumbs)],
    }
    article_ld = {
        "@context": "https://schema.org", "@type": "TechArticle",
        "headline": page.title, "description": meta["description"], "url": page.url,
        "dateModified": updated, "datePublished": str(meta.get("published", updated)),
        "inLanguage": "en-US", "image": og_image,
        "author": {"@type": "Person", "name": "Phillip Harrison"},
        "publisher": {"@type": "Organization", "name": "WalletFeed", "url": SITE,
                      "logo": {"@type": "ImageObject", "url": SITE + "assets/icon-512.png"}},
        "about": {"@type": "SoftwareApplication", "name": "WalletFeed", "operatingSystem": "iOS 26",
                  "applicationCategory": "FinanceApplication"},
    }
    crumb_links = " <span>›</span> ".join(
        f'<a href="{up}{href}">{html.escape(name)}</a>' if i < len(crumbs) - 1 else f'<span aria-current="page">{html.escape(name)}</span>'
        for i, (name, href) in enumerate(crumbs))
    title = meta.get("seo_title", page.title)
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{html.escape(title)} · WalletFeed</title>
  <meta name="description" content="{html.escape(meta['description'])}">
  <meta name="theme-color" content="#f2f2f7" media="(prefers-color-scheme: light)">
  <meta name="theme-color" content="#000000" media="(prefers-color-scheme: dark)">
  <meta property="og:type" content="article">
  <meta property="og:site_name" content="WalletFeed">
  <meta property="og:url" content="{page.url}">
  <meta property="og:title" content="{html.escape(page.title)}">
  <meta property="og:description" content="{html.escape(meta['description'])}">
  <meta property="og:image" content="{og_image}">
  <meta name="twitter:card" content="summary_large_image">
  <link rel="canonical" href="{page.url}">
  <link rel="icon" href="{up}assets/favicon-64.png">
  <link rel="apple-touch-icon" href="{up}assets/apple-touch-icon.png">
  <link rel="alternate" type="text/markdown" href="index.md">
  <link rel="stylesheet" href="{up}assets/style.css">
  <script type="application/ld+json">{json.dumps(article_ld, ensure_ascii=False)}</script>
  <script type="application/ld+json">{json.dumps(breadcrumb_ld, ensure_ascii=False)}</script>
</head>
<body>
{site_header(up)}
  <main class="document article">
    <nav class="crumbs" aria-label="Breadcrumb">{crumb_links}</nav>
    <h1>{html.escape(page.title)}</h1>
{body}
{extra}
    <p class="updated secondary">Updated {date.fromisoformat(updated).strftime('%B %-d, %Y')}</p>
  </main>
{site_footer(up)}
</body>
</html>
"""


def site_header(up: str) -> str:
    return (f'  <header><a href="{up}"><img src="{up}assets/apple-touch-icon.png" alt="">WalletFeed</a>'
            f'<nav><a href="{up}guides/">Guides</a><a href="{up}docs/">User Guide</a><a href="{up}support/">Support</a></nav></header>')


def site_footer(up: str) -> str:
    return (f'  <footer>\n    <nav><a href="{up}">WalletFeed</a><a href="{up}guides/">Guides</a><a href="{up}docs/">User Guide</a>'
            f'<a href="{up}support/">Support</a><a href="{up}privacy/">Privacy</a><a href="{up}terms/">Terms</a><a href="{up}docs/webhooks/">Webhook format</a></nav>\n'
            f'    <p>{TRADEMARKS}</p>\n    <p>© 2026 Phillip Harrison</p>\n  </footer>')


def related_html(page: Page, pages: dict) -> str:
    links = []
    for ref in page.meta.get("related", []):
        other = pages.get(ref.strip("/"))
        if not other:
            sys.exit(f"{page.source}: related page {ref} doesn't exist")
        links.append(f'<li><a href="../../{other.path}">{html.escape(other.title)}</a></li>')
    if page.section == "docs":
        ordered = sorted((p for p in pages.values() if p.section == "docs"), key=lambda p: (p.meta.get("order", 999), p.slug))
        index = ordered.index(page)
        if index + 1 < len(ordered):
            nxt = ordered[index + 1]
            links.insert(0, f'<li>Next: <a href="../../{nxt.path}">{html.escape(nxt.title)}</a></li>')
    return f'    <h2 id="related">Related</h2>\n    <ul class="related">{"".join(links)}</ul>' if links else ""


def markdown_copy(page: Page) -> str:
    """The page as Markdown for crawlers and AI agents: no front matter, absolute image URLs."""
    body = page.body
    for image in page.images:
        body = body.replace(f"]({image['ref']})", f"]({page.url}{image['file']})")
    return f"# {page.title}\n\n{body.strip()}\n"


def hub(section: str, pages: list[Page]) -> str:
    info = SECTIONS[section]
    if section == "guides":
        groups: dict[str, list[Page]] = {}
        for p in pages:
            groups.setdefault(p.meta.get("group", "Other"), []).append(p)
        order = GUIDE_GROUPS + sorted(g for g in groups if g not in GUIDE_GROUPS)
        parts = []
        for g in order:
            if g in groups:
                items = "".join(
                    f'<li><a href="{p.slug}/"><strong>{html.escape(p.nav_title)}</strong><span>{html.escape(p.meta["description"])}</span></a></li>'
                    for p in sorted(groups[g], key=lambda p: (p.meta.get("order", 999), p.nav_title)))
                parts.append(f'    <h2 id="{slugify(g)}">{html.escape(g)}</h2>\n    <ul class="group links">{items}</ul>')
        body = "\n".join(parts)
    else:
        items = "".join(
            f'<li><a href="{p.slug}/"><strong>{html.escape(p.title)}</strong><span>{html.escape(p.meta["description"])}</span></a></li>'
            for p in sorted(pages, key=lambda p: (p.meta.get("order", 999), p.slug)))
        items += '<li><a href="webhooks/"><strong>Webhook format</strong><span>The JSON a webhook destination receives, and how to verify its signature.</span></a></li>'
        body = f'    <ul class="group links">{items}</ul>'
    up = "../"
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{info['title']} · WalletFeed</title>
  <meta name="description" content="{html.escape(info['description'])}">
  <meta property="og:type" content="website">
  <meta property="og:url" content="{SITE}{section}/">
  <meta property="og:title" content="{info['title']}">
  <meta property="og:description" content="{html.escape(info['description'])}">
  <meta property="og:image" content="{SITE}assets/icon-512.png">
  <link rel="canonical" href="{SITE}{section}/">
  <link rel="icon" href="{up}assets/favicon-64.png">
  <link rel="apple-touch-icon" href="{up}assets/apple-touch-icon.png">
  <link rel="alternate" type="text/markdown" href="index.md">
  <link rel="stylesheet" href="{up}assets/style.css">
</head>
<body>
{site_header(up)}
  <main class="document article">
    <nav class="crumbs" aria-label="Breadcrumb"><a href="{up}">WalletFeed</a> <span>›</span> <span aria-current="page">{info['nav']}</span></nav>
    <h1>{info['title']}</h1>
    <p class="lead">{info['lead']}</p>
{body}
  </main>
{site_footer(up)}
</body>
</html>
"""


def hub_markdown(section: str, pages: list[Page]) -> str:
    info = SECTIONS[section]
    lines = [f"# {info['title']}", "", info["lead"], ""]
    for p in sorted(pages, key=lambda p: (p.meta.get("group", ""), p.meta.get("order", 999), p.slug)):
        lines.append(f"- [{p.title}]({p.url}index.md): {p.meta['description']}")
    return "\n".join(lines) + "\n"


def check(paths: list[str]) -> None:
    """Renders single sources into a scratch folder, so a writer can test a page without touching
    the site: front matter, images and Markdown."""
    global ROOT
    site = ROOT
    for arg in paths:
        source = Path(arg).resolve()
        section = source.parent.name
        page = read_page(section, source)
        ROOT = Path("/tmp/wfdocs-check") / section
        body = postprocess(markdown(page).render(page.body))
        ROOT = site
        for ref in page.meta.get("related", []):
            if not (site / "src" / f"{ref.strip('/')}.md").exists():
                print(f"{source.name}: related page {ref} has no source yet (fine if another writer is making it)")
        print(f"{source.name}: OK, {len(page.images)} images, {len(body)} bytes of HTML, description {len(page.meta['description'])} characters")


def main():
    if sys.argv[1:2] == ["--check"]:
        check(sys.argv[2:])
        return
    pages: dict[str, Page] = {}
    for section in SECTIONS:
        for source in sorted((ROOT / "src" / section).glob("*.md")):
            page = read_page(section, source)
            pages[f"{section}/{page.slug}"] = page
    rendered = {}
    for key, page in pages.items():
        body = postprocess(markdown(page).render(page.body))
        rendered[key] = body
    for key, page in pages.items():
        crumbs = [("WalletFeed", ""), (SECTIONS[page.section]["nav"], f"{page.section}/"), (page.nav_title, page.path)]
        out = ROOT / page.path
        out.mkdir(parents=True, exist_ok=True)
        (out / "index.html").write_text(page_html(page, rendered[key], crumbs, related_html(page, pages)))
        (out / "index.md").write_text(markdown_copy(page))
        # WebP files a page no longer uses.
        used = {i["file"] for i in page.images}
        for stale in out.glob("*.webp"):
            if stale.name not in used:
                stale.unlink()
    for section in SECTIONS:
        members = [p for p in pages.values() if p.section == section]
        if members:
            (ROOT / section / "index.html").write_text(hub(section, members))
            (ROOT / section / "index.md").write_text(hub_markdown(section, members))
    manifest = [{"path": f"{p.path}index.html", "section": p.section, "title": p.title,
                 "description": p.meta["description"], "group": p.meta.get("group"), "updated": str(p.meta.get("updated", ""))}
                for p in pages.values()]
    manifest += [{"path": f"{s}/index.html", "section": s, "title": SECTIONS[s]["title"], "description": SECTIONS[s]["description"],
                  "group": None, "updated": ""} for s in SECTIONS if any(p.section == s for p in pages.values())]
    (ROOT / "pages.json").write_text(json.dumps(sorted(manifest, key=lambda m: m["path"]), indent=1) + "\n")
    print(f"{len(pages)} pages, {sum(len(p.images) for p in pages.values())} images")


if __name__ == "__main__":
    main()
