#!/home/pph/.venv/bin/python
"""The press page's images (press/index.html): the app's own screens with a caption and alt text
each, the icon and the banners, and one ZIP of everything.

  ~/.venv/bin/python scripts/press_kit.py

It copies each screen in SHOTS from the app repo's newest Screenshots run (build/screenshots/raw,
1320 x 2868, sample data) to press/shots/, makes a WebP thumbnail beside it, copies the art in
LOGOS to press/logos/, writes press/walletfeed-press-kit.zip, and rewrites the part of
press/index.html between the two "press-kit" comments. The rest of the page is written by hand.
The screens must be of the version on the App Store: check each against its caption before you
publish, and change a caption here, never in the page.
"""
import html
import os
import zipfile
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
APP = Path(os.environ.get("WALLETFEED_REPO", Path.home() / "walletfeed"))
RAW = APP / "build/screenshots/raw"
PRESS = ROOT / "press"
THUMB_WIDTH = 440  # shown at 220 px

# (section, [(file name, source in RAW, caption title, caption, alt text)])
SHOTS = [
    ("Spending and Apple Intelligence", [
        ("01-ask-spending", "01-ask-spending", "Ask Spending",
         "Ask in your own words, such as “Dining this month vs last”. WalletFeed charts the answer and Apple Intelligence on the iPhone sums it up.",
         "The Spending screen after the question “Dining this month vs last”: $172.75 across 8 transactions, a line chart of this month against last month, and a summary that says dining is 27% higher than at this point last month."),
        ("02-monthly-summary", "02-spending", "Spending and Monthly Summary",
         "This month by day, against the same point last month, with the Apple Card balance and due date, and a short summary of the month.",
         "The Spending screen for November: $1,279.93 spent, 75% more than in October, a bar chart by day, the card balance of $1,291.12 due December 7, and a summary that travel is up $175 and the largest purchase was $389 at United Airlines."),
        ("03-accounts", "link-recurring", "Accounts",
         "Apple Card, Apple Cash and Savings on the Spending screen, each with its balance and its trend.",
         "The Accounts section of Spending: Apple Card at $1,291.12, Apple Cash at $142.50 and Savings at $5,230.18, each with a small chart of its balance, above the month's categories."),
        ("04-account", "docs-account", "An account’s own screen",
         "A balance over a week to a year, with available credit, the minimum payment and what was spent this month.",
         "The Apple Card screen: a three-month chart of the balance, now $1,291.12, with a low of $331.12 and a high of $1,434.12, then available credit of $6,708.88 of an $8,000 limit, a minimum payment of $35.00 due December 7 and $1,262.03 spent this month."),
        ("05-search", "04-search", "Search",
         "Type “Groceries over $50 in the last 30 days”. Apple Intelligence reads the request, and WalletFeed shows the transactions and their total.",
         "Search results for groceries over $50.00 in the last 30 days: 4 transactions totalling $277.57, at Whole Foods Market and Safeway, grouped by month."),
        ("06-transactions", "06-transactions", "Transactions",
         "Every transaction from the Wallet accounts you share, grouped by month, with pending charges marked.",
         "The Transactions screen for November: Blue Bottle Coffee $6.75 pending, Whole Foods Market $84.12, Tartine Bakery $12.40 from Apple Cash, Uber $23.40, Shell $52.08 and others, each with a category icon and its day."),
    ]),
    ("Subscriptions and taxes", [
        ("07-subscriptions", "docs-subscriptions", "Subscriptions",
         "Every charge that repeats: what they cost each month and each year, where the money goes, and when each is next due.",
         "The Subscriptions screen: $123.88 each month and $1,486.56 each year, split between Utilities and Subscriptions, then PG&E at $96.40 a month next due December 6, Netflix at $15.49 and Spotify at $11.99."),
        ("08-recurring-charges", "05-recurring", "Recurring Charges and merchants",
         "Recurring charges with the names Apple Intelligence suggests, the month’s top merchants, and the Tax Pack.",
         "Spending scrolled to Recurring Charges, with Netflix and Spotify named and All Subscriptions below them, then Merchants led by United Airlines at $389.20, and Tax Reports with the Tax Pack for 2026."),
        ("09-tax-pack", "docs-tax-pack", "Tax Pack",
         "A year’s totals for each account: purchases, refunds, interest and fees. The totals are free to see.",
         "The Tax Pack for 2026 with 45 transactions: for Apple Card, purchases of $2,189.49 and refunds of $49.00, with interest charged, fees and payments to the card at $0.00, then Apple Cash and Savings."),
        ("10-tax-pack-share", "docs-tax-pack-share", "Share the Tax Pack",
         "With Pro Yearly or Lifetime, share the year as a PDF, a summary for an AI assistant and two CSV files.",
         "The foot of the Tax Pack: Savings interest earned of $14.82, then Share Pack and Share Summary for AI, with the note that the pack is a PDF, a Markdown summary for AI and two CSV files, and that WalletFeed doesn’t give tax advice."),
    ]),
    ("Destinations, with WalletFeed Pro", [
        ("11-destinations", "07-destinations", "Destinations",
         "Each place your transactions go, with the time of its last sync.",
         "The Destinations screen with four destinations: Lunch Money, a Google Sheets spreadsheet named Budget 2026, a monthly CSV file and an n8n webhook, each synced minutes ago."),
        ("12-add-destination", "08-add-destination", "Add Destination",
         "Budgeting apps, accounting, spreadsheets, databases, automations, files and developer tools, each with its own logo.",
         "The Add Destination list: under Budgeting, BankSync, Lunch Money, PocketSmith, Firefly III, Sure, Toshl Finance, Wallet by BudgetBakers, YNAB and QuickBooks Online, then Sheets & Databases starting with Google Sheets."),
        ("13-google-sheets", "g-google-sheets", "Set up Google Sheets",
         "Sign in with Google, name the spreadsheet, and choose Summary Tabs for totals by month, category and merchant.",
         "The Google Sheets form: Sign In with Google, a Spreadsheet named WalletFeed Transactions, a Summary Tabs switch, and three steps that end with tapping Add."),
        ("14-consent", "docs-consent", "What a destination receives",
         "Before anything is sent, WalletFeed lists the fields the destination will receive, from which accounts and from when.",
         "An alert over the Webhook form, “Send Transactions to Your Server?”, listing the date, merchant, amount, category, status, account name and the other fields, from Apple Card, Apple Cash and Savings, with Cancel and Send."),
        ("15-send-history", "h-history", "Send History",
         "A new destination also gets your earlier transactions, at a pace the service accepts.",
         "A Google Sheets destination named Budget 2026 while it sends history: a progress bar at 27 of 46, now at November 2026, with Send History, Send Test and Delete below."),
        ("16-automations", "docs-automations", "Automations",
         "A Shortcuts automation syncs seconds after each card tap, and another once a day.",
         "The Automations screen: After Each Card Tap, with steps to copy a description, open Shortcuts and paste it, then Every Day at 9 PM, each with the time of its last run."),
        ("17-background-sync", "09-background-sync", "Background Sync and notifications",
         "Destinations update within the hour while WalletFeed is closed. Reminders and alerts are optional.",
         "Settings with Background Sync on, Automations, Remind If Sync Stops, Failure Alerts, Initial History set to All and Sync Now, then Require Face ID and Summarize Spending."),
        ("18-export-csv", "docs-export-csv", "Export CSV",
         "A CSV file of this month, last month, 90 days, a year or everything. Free.",
         "The Export CSV screen: Range set to This Month, 28 transactions, and an Export button."),
    ]),
    ("Privacy, and getting started", [
        ("19-privacy", "03-privacy", "Privacy",
         "The privacy statement is in the app: what WalletFeed reads, what stays on the iPhone, and what a destination gets.",
         "The Privacy screen: WalletFeed needs no account and no WalletFeed server keeps your transactions or keys, then sections on Wallet data and on the data kept on your iPhone."),
        ("20-wallet-access", "docs-wallet-access", "Share Wallet Data",
         "iOS asks which Wallet accounts WalletFeed can read. You can change it at any time in Settings.",
         "The iOS sheet Share Wallet Data for WalletFeed, with switches for Apple Card, Apple Cash and Savings, and the buttons Share and Don’t Share."),
        ("21-welcome", "docs-welcome", "Welcome",
         "The first screen: Ask Spending, Destinations, On-Device Privacy and Background Sync.",
         "The Welcome to WalletFeed screen with four points, Ask Spending, Destinations, On-Device Privacy and Background Sync, and a Continue button."),
        ("22-walletfeed-pro", "10-pro", "WalletFeed Pro",
         "Destinations, Background Sync, Send History and the Tax Pack’s files. Yearly, Monthly or Lifetime, with a free trial on the subscriptions.",
         "The WalletFeed Pro screen: Destinations, Background Sync, Send History and Tax Pack, then Yearly at $4.99 a year, Monthly at $0.99 a month and Lifetime at $19.99, with a Start Free Trial button."),
    ]),
]

# (file name in press/logos, source, caption, alt text, shown width and height)
LOGOS = [
    ("walletfeed-icon-1024.png", APP / "metadata/art/app-store-icon-1024.png", "App icon, 1024 × 1024 px, square",
     "The WalletFeed app icon: a blue card with a chip, and a round sync symbol, on a near-black square.", 128, 128),
    ("walletfeed-banner-1500x500.png", ROOT / "assets/cover-1500x500.png", "Banner with the name, 1500 × 500 px",
     "A blue banner with the WalletFeed icon, the name WalletFeed and the line “Spending for Apple Card, Apple Cash and Savings, with Apple Intelligence.”", 360, 120),
    ("walletfeed-header-3840x1646.png", APP / "metadata/art/header-3840x1646.png", "Header art without text, 3840 × 1646 px",
     "Three cards and the sync symbol on a deep blue background, with no text.", 280, 120),
]


def rounded(source: Path, out: Path) -> None:
    """The icon in the Home Screen's shape, on a transparent background, for layouts that don't mask it."""
    from PIL import ImageDraw
    icon = Image.open(source).convert("RGBA")
    scale = 4
    mask = Image.new("L", (icon.width * scale, icon.height * scale), 0)
    ImageDraw.Draw(mask).rounded_rectangle((0, 0, mask.width - 1, mask.height - 1), radius=int(mask.width * 0.2237), fill=255)
    icon.putalpha(mask.resize(icon.size, Image.LANCZOS))
    icon.save(out, optimize=True)


def figure(link: str, thumb: str, title: str, caption: str, alt: str, width: int, height: int, classes: str = "shot phone") -> str:
    return (f'        <figure>\n          <a href="{link}"><img class="{classes}" src="{thumb}" width="{width}" height="{height}" loading="lazy" '
            f'alt="{html.escape(alt, quote=True)}"></a>\n'
            f'          <figcaption><strong>{html.escape(title)}</strong><span>{html.escape(caption)}</span></figcaption>\n        </figure>')


def main() -> None:
    shots, logos = PRESS / "shots", PRESS / "logos"
    shots.mkdir(exist_ok=True)
    logos.mkdir(exist_ok=True)
    parts, packed, count = [], [], 0
    for section, items in SHOTS:
        rows = []
        for name, source, title, caption, alt in items:
            image = Image.open(RAW / f"{source}.png").convert("RGB")
            full = shots / f"walletfeed-{name}.png"
            image.save(full, optimize=True)
            thumb = image.copy()
            thumb.thumbnail((THUMB_WIDTH, THUMB_WIDTH * 3))
            thumb.save(shots / f"walletfeed-{name}.webp", quality=82, method=6)
            rows.append(figure(f"shots/{full.name}", f"shots/walletfeed-{name}.webp", title, caption, alt,
                               THUMB_WIDTH // 2, round(THUMB_WIDTH / 2 * image.height / image.width)))
            packed.append((full, f"screenshots/{full.name}", f"{title}. {caption}\n   Alt text: {alt}"))
            count += 1
        parts.append(f'    <h3>{html.escape(section)}</h3>\n    <div class="gallery">\n' + "\n".join(rows) + "\n    </div>")

    logo_rows = []
    for name, source, caption, alt, width, height in LOGOS:
        Image.open(source).save(logos / name, optimize=True)
        style = ' style="border-radius:22.5%"' if "icon" in name else ' style="border-radius:10px"'
        logo_rows.append(f'      <figure>\n        <a href="logos/{name}"><img class="shot" src="logos/{name}" width="{width}" height="{height}" loading="lazy" '
                         f'alt="{html.escape(alt, quote=True)}"{style}></a>\n        <figcaption><span>{html.escape(caption)}</span></figcaption>\n      </figure>')
        packed.append((logos / name, f"logos/{name}", f"{caption}\n   Alt text: {alt}"))
    rounded(APP / "metadata/art/app-store-icon-1024.png", logos / "walletfeed-icon-rounded-1024.png")
    logo_rows.insert(1, '      <figure>\n        <a href="logos/walletfeed-icon-rounded-1024.png"><img class="shot" src="logos/walletfeed-icon-rounded-1024.png" '
                        'width="128" height="128" loading="lazy" alt="The WalletFeed app icon with rounded corners on a transparent background."></a>\n'
                        '        <figcaption><span>App icon, 1024 × 1024 px, rounded, transparent corners</span></figcaption>\n      </figure>')
    packed.append((logos / "walletfeed-icon-rounded-1024.png", "logos/walletfeed-icon-rounded-1024.png",
                   "App icon, 1024 x 1024 px, rounded, transparent corners\n   Alt text: The WalletFeed app icon with rounded corners on a transparent background."))

    readme = ["WalletFeed press kit", "https://walletfeed.app/press/", "",
              "Screenshots are 1320 x 2868 px, from an iPhone 17 Pro Max, with sample data. You may use these images",
              "to write about WalletFeed. Contact: support@walletfeed.app", ""]
    readme += [f"{path}\n   {text}\n" for _, path, text in packed]
    archive = PRESS / "walletfeed-press-kit.zip"
    with zipfile.ZipFile(archive, "w", zipfile.ZIP_DEFLATED) as kit:
        info = zipfile.ZipInfo("README.txt", date_time=(2026, 11, 27, 0, 0, 0))
        kit.writestr(info, "\n".join(readme))
        for source, path, _ in packed:
            info = zipfile.ZipInfo(path, date_time=(2026, 11, 27, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            kit.writestr(info, source.read_bytes())

    block = ('    <!-- press-kit: made by scripts/press_kit.py -->\n'
             f'    <p>{count} screens of the app, each with a caption and alt text you can use. Each image opens at full size, 1320 × 2868 px. '
             'They show sample data. '
             f'<a href="walletfeed-press-kit.zip">Download every image</a> ({archive.stat().st_size / 1e6:.0f} MB, with the captions and alt text in a text file).</p>\n'
             + "\n".join(parts) + '\n    <h2 id="logos">Icon and banners</h2>\n    <div class="gallery logos">\n' + "\n".join(logo_rows)
             + '\n    </div>\n    <!-- /press-kit -->')
    page = PRESS / "index.html"
    text = page.read_text()
    start, end = text.index("    <!-- press-kit"), text.index("<!-- /press-kit -->") + len("<!-- /press-kit -->")
    page.write_text(text[:start] + block + text[end:])
    print(f"{count} screens, {len(LOGOS) + 1} logo files, {archive.name} {archive.stat().st_size / 1e6:.1f} MB")


if __name__ == "__main__":
    main()
