+++
title = "Export Apple Card transactions"
nav_title = "Export transactions"
seo_title = "Export or download Apple Card transactions"
description = "Export or download your Apple Card transactions from Wallet, card.apple.com or WalletFeed. With WalletFeed Pro, WalletFeed can also update a file."
group = "Export"
order = 10
related = ["guides/apple-card-to-csv", "guides/apple-card-to-ofx", "docs/export-csv"]
updated = 2026-10-30
+++

You can export your Apple Card transactions as a file from Wallet on your iPhone, from card.apple.com or from WalletFeed. With WalletFeed Pro, WalletFeed also updates a file or a service when your transactions change.

## Before you start

- Your Apple Card in Wallet on your iPhone.
- For card.apple.com, a computer with a web browser.
- For WalletFeed, an iPhone with iOS 26 or a newer version. WalletFeed is available only in the US. You must [share your Apple Card with WalletFeed](/docs/wallet-accounts/).
- For a file or a service that WalletFeed updates, [WalletFeed Pro](/docs/walletfeed-pro/). It is a subscription with a 1-week free trial, or a one-time Lifetime purchase. WalletFeed Pro is not necessary for **Export CSV**.

## Export a statement in Wallet

Wallet has a statement for each previous month. You can export the transactions of a statement as a CSV, OFX, QFX or QBO file.

1. On your iPhone, open Wallet.
2. Tap your Apple Card.
3. Tap **Card Balance**.
4. Scroll down to **Statements**.
5. Tap a statement.
6. Tap **Export Transactions**.
7. Select a file format.

   For a spreadsheet, for example Numbers or Excel, select CSV.

8. To keep the file on your iPhone, tap **Save to Files**.

   You can also send the file with Mail or AirDrop.

9. Select a folder.
10. Tap **Save**.

To download a statement as a PDF file:

1. In Wallet, open a statement.
2. Tap **Download PDF Statement**.
3. When the PDF file opens, tap the share button.

   You can then save, print or send the file.

## Export transactions between two dates in Wallet

Wallet can also export the transactions between two dates that you select.

1. On your iPhone, open Wallet.
2. Tap your Apple Card.
3. Tap **Card Balance**.
4. Below **Statements**, tap **Export Transactions**.
5. Select a start date.
6. Select an end date.
7. Select a file format.
8. Tap the done button.

## Export transactions at card.apple.com

1. On your computer, open [card.apple.com](https://card.apple.com).
2. Sign in with your Apple Account.
3. Click **Statements**.
4. Click **Export Transactions**.
5. Select a start date.
6. Select an end date.
7. Select a file format.
8. Click **Export**.

To download a statement as a PDF file:

1. Click **Statements**.
2. Click the download button for a statement.

Apple gives the steps for Wallet and card.apple.com in [Download your Apple Card statements or export your transactions](https://support.apple.com/en-us/102284).

## Export a CSV file with WalletFeed

[Export CSV](/docs/export-csv/) in WalletFeed makes one CSV file with your transactions from a period that you select. You can use it without WalletFeed Pro. The file includes pending transactions, and it does not change after you export it.

1. On your iPhone, open WalletFeed.
2. Tap **Settings** (the gear button) at the top of the screen.
3. In the **Data** section, tap **Export CSV**.

   ![The Settings screen with Export CSV in the Data section.](app:docs-settings-3)

4. Tap **Range**.
5. Select a period: **This Month**, **Last Month**, **Last 90 Days**, **This Year** or **All**.

   ![The Export CSV screen with Range set to This Month, 29 transactions and the Export button.](app:docs-export-csv)

   **Transactions** shows the number of transactions in the period.

6. Tap **Export**.
7. In the share sheet, tap **Save to Files**.
8. Select a folder.
9. Tap **Save**.

The name of the file includes the period, for example `Apple Card Last Month.csv`. The file has the transactions from all the Wallet accounts that you share with WalletFeed. The **Account** column shows the account of each transaction. WalletFeed makes the file on your iPhone and does not keep it.

## Columns in the CSV file

Each CSV file from WalletFeed has one row for each transaction and these columns:

| Column | Data |
| --- | --- |
| **Date** | The date of the transaction, for example 2026-10-28. |
| **Posted Date** | The date that the charge posted. It is empty while the charge is pending. |
| **Merchant** | The merchant name, or the description if Wallet has no merchant name. |
| **Description** | The description of the transaction in Wallet. |
| **Original Description** | The description of the transaction with no changes. |
| **Amount** | The value of the transaction, for example -23.40. Purchases and fees have a minus sign. Payments and refunds have no minus sign. |
| **Currency** | The currency code, for example USD. |
| **Direction** | `debit` for purchases and fees, or `credit` for refunds, payments and deposits. |
| **Status** | The status in Wallet, for example `pending` or `authorized` before the charge posts, `booked` after it posts, or `rejected` for a declined charge. |
| **Type** | The type of transaction in Wallet, for example `pointOfSale` for a purchase, `refund`, `transfer` or `fee`. |
| **Category** | The WalletFeed category, for example Groceries, Dining or Cash & Transfers. |
| **MCC** | The merchant category code (ISO 18245), for example 5411 for a grocery store. It is empty if Wallet has no code. |
| **Account** | The Wallet account, for example Apple Card. |
| **Foreign Amount** | For a purchase in a different currency, the value in that currency. |
| **Foreign Currency** | The code of that different currency. |
| **WalletFeed ID** | The ID of the transaction. You can use it to find the same transaction in a different file. |

## Update a file or a service with WalletFeed Pro

With WalletFeed Pro, it is not necessary to export again. WalletFeed sends your transactions from your iPhone to a [destination](/docs/destinations/), and updates the destination when your transactions change. WalletFeed has no account and no WalletFeed servers. Your transactions go from your iPhone directly to the folder or the service that you select.

A destination can be one of these:

- A [CSV file](/guides/apple-card-to-csv/) in a folder, for example in iCloud Drive. WalletFeed writes one file or one file for each month. You can open a CSV file in [Excel](/guides/apple-card-to-excel/) or [Numbers](/guides/apple-card-to-numbers/).
- An [OFX file](/guides/apple-card-to-ofx/) or a [QIF file](/guides/apple-card-to-qif/) for each month. You can import these files into an app that reads OFX or QIF. These files include a charge only after the charge posts.
- A spreadsheet in [Google Sheets](/guides/apple-card-to-google-sheets/).
- A budget app, for example [Lunch Money](/guides/apple-card-to-lunch-money/) or [PocketSmith](/guides/apple-card-to-pocketsmith/).

> **Note:** WalletFeed writes CSV, OFX and QIF files. It does not write QFX or QBO files. Quicken for Windows cannot import the OFX files from WalletFeed, but it can import the CSV files.

To add a CSV file that WalletFeed updates:

1. On your iPhone, open WalletFeed.
2. Tap **Destinations**.
3. Tap **+** at the top of the screen.

   ![The Destinations screen with no destinations and the + button at the top.](app:docs-destinations-empty-pro)

4. In the search field, type `CSV`.
5. Tap **CSV File**.

   If you do not have WalletFeed Pro, the **WalletFeed Pro** screen opens. After you get WalletFeed Pro, the **Files** screen opens.

   ![The Files screen with Format set to CSV, Save As set to One File and the name WalletFeed Transactions.](app:docs-setup-csv-file)

6. Tap **Folder**.
7. Select a folder in iCloud Drive.
8. Tap **Add**.
9. When WalletFeed shows **Save Transactions to Files?**, tap **Save**.

   The message tells you the data that the folder will receive. It also gives the accounts and the period of the transactions. If you tap **Cancel**, WalletFeed removes the new destination.

WalletFeed then writes your transactions to `WalletFeed Transactions.csv` in the folder.

## Changes to the file

While WalletFeed is open, the file receives changes in seconds. When WalletFeed is closed, iOS starts WalletFeed in approximately 1 hour or less after a change in Wallet. If [Background Sync](/docs/background-sync/) is on in **Settings** › **Sync**, WalletFeed then updates the file. If WalletFeed cannot open the folder at that time, the file changes when you open WalletFeed, when an automation starts, or while your iPhone charges.

## Send previous transactions

A new destination also receives your previous transactions, from the start date in **Settings** › **Sync** › **Initial History**. **Initial History** is **All** until you change it. To send a different period after you add the destination, use [Send History](/docs/send-history/) on the screen of the destination. You can select **30 Days**, **90 Days**, **1 Year** or **All**.

## Delete a destination

1. In WalletFeed, tap **Destinations**.
2. Tap the destination.
3. Tap **Delete**.
4. Tap **Delete** again.

The file and the transactions in it stay in the folder. A service keeps the transactions that it received. The terms of that service are applicable to these transactions.

## If there is a problem

### If this month has no statement in Wallet

Wallet makes a statement only after the end of the month. To export the transactions of this month, use **Export CSV** in WalletFeed.

1. On your iPhone, open WalletFeed.
2. Tap **Settings** (the gear button) at the top of the screen.
3. In the **Data** section, tap **Export CSV**.
4. Set **Range** to **This Month**.
5. Tap **Export**.
6. In the share sheet, tap **Save to Files**.
7. Select a folder.
8. Tap **Save**.

### If you cannot tap Export in WalletFeed

**Export** is not available while WalletFeed reads your transactions, or when the period has no transactions.

1. Make sure that **Transactions** shows a number.
2. If the number is 0, select a different period in **Range**.

### If there is an apostrophe before a name or a description

If the text in a column has `=`, `+`, `-` or `@` as the first character, WalletFeed puts an apostrophe (`'`) before the text. Thus, a spreadsheet does not use the text as a formula.
