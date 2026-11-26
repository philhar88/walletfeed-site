#!/home/pph/.venv/bin/python
"""Tells IndexNow (Bing, Yandex, Seznam, Naver and the others that share it) which pages changed, so they
crawl them soon. Google doesn't take part: it reads sitemap.xml. The key is the file named for it at the
site's root. Run it after the change is live on walletfeed.app.

  scripts/indexnow.py                 every page in sitemap.xml
  scripts/indexnow.py REV             the pages whose files changed since the git revision REV, such as HEAD~1
"""
import re
import subprocess
import sys
from pathlib import Path

import httpx

ROOT = Path(__file__).resolve().parents[1]
SITE = "https://walletfeed.app/"
KEY = "d13c49ff2edd7c0c5dc46bd0824109bc"


def main() -> None:
    assert (ROOT / f"{KEY}.txt").read_text().strip() == KEY
    urls = re.findall(r"<loc>([^<]+)</loc>", (ROOT / "sitemap.xml").read_text())
    if sys.argv[1:]:
        changed = subprocess.run(["git", "diff", "--name-only", sys.argv[1], "HEAD"], cwd=ROOT, capture_output=True, text=True, check=True).stdout.split()
        pages = {SITE + name.removesuffix("index.html") for name in changed if name.endswith("index.html")}
        urls = [u for u in urls if u in pages]
    if not urls:
        sys.exit("No pages to send.")
    r = httpx.post("https://api.indexnow.org/indexnow", timeout=60,
                   json={"host": "walletfeed.app", "key": KEY, "keyLocation": f"{SITE}{KEY}.txt", "urlList": urls})
    print(f"{len(urls)} pages sent: HTTP {r.status_code} {r.text[:200]}")


if __name__ == "__main__":
    main()
