#!/home/pph/.venv/bin/python
"""The files that tell crawlers and AI agents about the site, made from the pages themselves:

  index.md, privacy/index.md, …   each page's <main> as Markdown, linked from its <head>
  llms.txt                        what WalletFeed is, and a link to each page's Markdown (llmstxt.org)
  llms-full.txt                   every page's Markdown in one file
  sitemap.xml                     every page, with the date of its last commit

robots.txt is written by hand. Run this after changing a page, and commit what it writes:

  ~/.venv/bin/python scripts/agent_files.py

Standard library only.
"""
import re
import subprocess
from html import unescape
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urljoin

ROOT = Path(__file__).resolve().parents[1]
SITE = "https://walletfeed.app/"
PAGES = ["index.html", "privacy/index.html", "support/index.html", "docs/webhooks/index.html"]
SUMMARY = (
    "WalletFeed is an iPhone app for Apple Card, Apple Cash and Savings. It shows your spending, and "
    "with Apple Intelligence on the iPhone it answers questions about it, summarizes each month and "
    "searches transactions. The optional WalletFeed Pro subscription sends new transactions from the "
    "iPhone to budgeting apps, spreadsheets, files, automations and AWS. WalletFeed has no account, no "
    "analytics and no servers of its own. Support: support@walletfeed.app."
)
VOID = {"br", "img", "meta", "link", "hr", "input", "source"}


class Node:
    def __init__(self, tag, attrs=None, parent=None):
        self.tag, self.attrs, self.parent, self.children = tag, dict(attrs or {}), parent, []

    @property
    def classes(self):
        return self.attrs.get("class", "").split()


class Tree(HTMLParser):
    """A plain element tree, enough for these hand-written pages."""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.root = self.node = Node("#root")

    def handle_starttag(self, tag, attrs):
        child = Node(tag, attrs, self.node)
        self.node.children.append(child)
        if tag not in VOID:
            self.node = child

    def handle_endtag(self, tag):
        node = self.node
        while node.parent and node.tag != tag:
            node = node.parent
        if node.parent:
            self.node = node.parent

    def handle_data(self, data):
        self.node.children.append(data)


def find(node, tag):
    for child in node.children:
        if isinstance(child, Node):
            if child.tag == tag:
                return child
            found = find(child, tag)
            if found:
                return found
    return None


def text(node):
    return "".join(c if isinstance(c, str) else text(c) for c in node.children)


class Markdown:
    def __init__(self, url, title):
        self.url, self.title = url, title

    def inline(self, node):
        out = []
        for c in node.children:
            if isinstance(c, str):
                out.append(re.sub(r"\s+", " ", c))
            elif c.tag == "a":
                out.append(f"[{self.inline(c).strip()}]({urljoin(self.url, c.attrs.get('href', ''))})")
            elif c.tag == "code":
                out.append(f"`{text(c)}`")
            elif c.tag in ("strong", "b"):
                out.append(f"**{self.inline(c).strip()}**")
            elif c.tag in ("em", "i"):
                out.append(f"*{self.inline(c).strip()}*")
            elif c.tag == "br":
                out.append("\n")
            elif c.tag != "img":
                out.append(self.inline(c))
        return "".join(out)

    def item(self, li):
        """A row of the pages' grouped lists: a name and its description, or plain text."""
        parts = [c for c in li.children if isinstance(c, Node) or c.strip()]
        if len(parts) >= 2 and isinstance(parts[0], Node) and parts[0].tag == "strong":
            rest = [self.inline(p) if isinstance(p, Node) else p for p in parts[1:]]
            details = ", ".join(r.strip() for r in rest if r.strip())
            return f"{self.inline(parts[0]).strip()}: {details}"
        return self.inline(li).strip()

    def blocks(self, node):
        out = []
        for c in node.children:
            if isinstance(c, str):
                if c.strip():
                    out.append(re.sub(r"\s+", " ", c).strip())
                continue
            match c.tag:
                case "h1":
                    heading = self.inline(c).strip()
                    if heading != self.title:
                        out.append(heading)  # the landing page's tagline
                case "h2" | "h3" | "h4":
                    out.append("#" * int(c.tag[1]) + " " + self.inline(c).strip())
                case "p":
                    out.append(self.inline(c).strip())
                case "ul" | "ol":
                    marker = (lambda i: f"{i}.") if c.tag == "ol" else (lambda i: "-")
                    items = [n for n in c.children if isinstance(n, Node) and n.tag == "li"]
                    out.append("\n".join(f"{marker(i)} {self.item(li)}" for i, li in enumerate(items, 1)))
                case "pre":
                    out.append(f"```\n{unescape(text(c)).strip(chr(10))}\n```")
                case "table":
                    rows = [r for r in self.rows(c)]
                    if rows:
                        lines = ["| " + " | ".join(rows[0]) + " |", "|" + " --- |" * len(rows[0])]
                        lines += ["| " + " | ".join(r) + " |" for r in rows[1:]]
                        out.append("\n".join(lines))
                case "div" if "plans" in c.classes:
                    plans = [n for n in c.children if isinstance(n, Node) and "plan" in n.classes]
                    out.append("\n".join(f"- {self.item(p)}" for p in plans))
                case "span" if "badge" in c.classes:
                    out.append(self.inline(c).strip())
                case "img":
                    pass
                case _:
                    out.extend(self.blocks(c))
        return [b for b in out if b]

    def rows(self, table):
        for tr in self.walk(table, "tr"):
            yield [self.inline(cell).strip().replace("|", "\\|") for cell in tr.children
                   if isinstance(cell, Node) and cell.tag in ("th", "td")]

    def walk(self, node, tag):
        for c in node.children:
            if isinstance(c, Node):
                if c.tag == tag:
                    yield c
                else:
                    yield from self.walk(c, tag)


def page(path):
    html = (ROOT / path).read_text()
    tree = Tree()
    tree.feed(html)
    title_node = find(tree.root, "title")
    title = text(title_node).replace(" · WalletFeed", "").strip() if title_node else "WalletFeed"
    description = re.search(r'<meta name="description" content="([^"]*)"', html)
    url = urljoin(SITE, path.removesuffix("index.html"))
    body = Markdown(url, title).blocks(find(tree.root, "main"))
    markdown = f"# {title}\n\n" + "\n\n".join(body) + "\n"
    return {"path": path, "url": url, "title": title, "description": unescape(description.group(1)) if description else "",
            "markdown": markdown, "md_path": path.removesuffix(".html") + ".md"}


def last_commit(path):
    out = subprocess.run(["git", "log", "-1", "--format=%cs", "--", path], cwd=ROOT, capture_output=True, text=True).stdout.strip()
    return out or None


def main():
    pages = [page(p) for p in PAGES]
    for p in pages:
        (ROOT / p["md_path"]).write_text(p["markdown"])

    links = "\n".join(f"- [{p['title']}]({urljoin(SITE, p['md_path'])}): {p['description']}" for p in pages)
    (ROOT / "llms.txt").write_text(
        f"# WalletFeed\n\n> {pages[0]['description']}\n\n{SUMMARY}\n\n## Pages\n\n{links}\n\n"
        f"## Optional\n\n- [Every page in one file]({SITE}llms-full.txt): the pages above, in Markdown\n"
    )
    (ROOT / "llms-full.txt").write_text(
        "\n\n".join(f"<!-- {p['url']} -->\n{p['markdown'].rstrip()}" for p in pages) + "\n"
    )

    entries = []
    for p in pages:
        lastmod = last_commit(p["path"])
        entries.append(f"  <url><loc>{p['url']}</loc>" + (f"<lastmod>{lastmod}</lastmod>" if lastmod else "") + "</url>")
    (ROOT / "sitemap.xml").write_text(
        '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        + "\n".join(entries) + "\n</urlset>\n"
    )
    for name in [p["md_path"] for p in pages] + ["llms.txt", "llms-full.txt", "sitemap.xml"]:
        print(name)


if __name__ == "__main__":
    main()
