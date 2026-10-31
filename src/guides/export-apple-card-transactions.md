+++
title = "Make an export file of your Apple Card transactions"
nav_title = "Export files"
seo_title = "Export or download Apple Card transactions"
description = "You can get an export file of your Apple Card transactions from Wallet, card.apple.com or WalletFeed. With WalletFeed Pro, WalletFeed also updates a file."
group = "Export"
order = 10
related = ["guides/apple-card-to-csv", "guides/apple-card-to-ofx", "guides/apple-card-plaid", "docs/export-csv"]
updated = 2026-10-31
+++

You can make an export file of your Apple Card transactions in Wallet on your iPhone, at card.apple.com or in WalletFeed. With WalletFeed Pro, WalletFeed also updates a file or a service when your transactions change.

In Wallet, you can make a file from a statement. A statement has the transactions of one month. Wallet and card.apple.com can also make a file with the transactions between two dates. Apple does not tell you if these dates can include this month. In WalletFeed, [Export CSV](#make-a-csv-file-with-export-csv) makes a CSV file of a period that you select, for example **This Month** or **All**. WalletFeed Pro is not necessary for **Export CSV**.

## Before you start

You must have:

- Your Apple Card in Wallet on your iPhone
- For card.apple.com, a computer with a web browser
- For WalletFeed, an iPhone with iOS 26 or a newer version
- For a file or a service that WalletFeed updates, [WalletFeed Pro](/docs/walletfeed-pro/).

WalletFeed is available only in the US. WalletFeed must have [access to your Apple Card](/docs/wallet-accounts/).

WalletFeed Pro is a subscription with a 1-week free trial, or a one-time Lifetime purchase. WalletFeed Pro is not necessary for **Export CSV**.

## Make a file from a statement in Wallet

Wallet has a statement for each previous month. **Export Transactions** makes a CSV, OFX, QFX or QBO file with the transactions of a statement.

1. On your iPhone, open Wallet.
2. Tap your Apple Card.
3. Tap **Card Balance**.
4. Scroll to **Statements**.
5. Tap a statement.
6. Tap **Export Transactions**.
7. Select a file format (for example, CSV for a spreadsheet in Numbers or Excel).
8. To save the file in the Files app, tap **Save to Files**.

   You can also send the file with Mail or AirDrop.

9. Select a folder.
10. Tap **Save**.

To download a PDF file of a statement:

1. In Wallet, open a statement (refer to steps 1 to 5 in this section).
2. Tap **Download PDF Statement**.
3. When the PDF file opens, tap the **Share** button.

   You can then save, print or send the file.

## Make a file of transactions between two dates in Wallet

1. On your iPhone, open Wallet.
2. Tap your Apple Card.
3. Tap **Card Balance**.
4. Below **Statements**, tap **Export Transactions**.
5. Select a start date.
6. Select an end date.
7. Select a file format.
8. Tap the done button.

## Make a file at card.apple.com

1. On your computer, open [card.apple.com](https://card.apple.com).
2. Get access to your Apple Card with your Apple Account.
3. Click **Statements**.
4. Click **Export Transactions**.
5. Select a start date.
6. Select an end date.
7. Select a file format.
8. Click **Export**.

To download a PDF file of a statement:

1. In the sidebar, click **Statements**.
2. Click the download button for a statement.

Apple gives the steps for Wallet and card.apple.com in [Download your Apple Card statements or export your transactions](https://support.apple.com/en-us/102284).

## Make a CSV file with Export CSV

[Export CSV](/docs/export-csv/) in WalletFeed makes one CSV file with your transactions from a period that you select. You can use it without WalletFeed Pro. The file includes pending transactions. The file does not change after WalletFeed makes it.

1. On your iPhone, open WalletFeed.
2. Tap **Settings** (the gear button) at the top of the screen.
3. In the **Data** section, tap **Export CSV**.

   ![The Settings screen with Export CSV in the Data section.](app:docs-settings-3)

4. Tap **Range**.
5. Select a period: **This Month**, **Last Month**, **Last 90 Days**, **This Year** or **All**.

   ![The Export CSV screen with Range set to This Month, 29 transactions and the Export button.](app:docs-export-csv)

   **Transactions** shows the number of transactions in the period.

6. Tap **Export**.
7. Tap **Save to Files**.
8. Select a folder.
9. Tap **Save**.

**This Month** has the transactions from the first day of this month, with the pending transactions. **All** has all the transactions that WalletFeed can read in Wallet, from each month.

The name of the file includes the period, for example `Apple Card Last Month.csv`. The file has the transactions from each Wallet account that WalletFeed can read. The **Account** column shows the account of each transaction. WalletFeed makes the file on your iPhone and does not keep it.

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
| **Category** | The WalletFeed category, for example `Groceries`, `Dining` or `Cash & Transfers`. |
| **MCC** | The merchant category code (ISO 18245), for example 5411 for a grocery store. It is empty if Wallet has no code. |
| **Account** | The Wallet account, for example Apple Card. |
| **Foreign Amount** | For a purchase in a different currency, the value in that currency. |
| **Foreign Currency** | For a purchase in a different currency, the code of that currency. |
| **WalletFeed ID** | The ID of the transaction. You can use it to find the same transaction in a different file. |

## Update a file or a service with WalletFeed Pro

With WalletFeed Pro, WalletFeed sends your transactions from your iPhone to a [destination](/docs/destinations/). When your transactions change, WalletFeed updates the destination. Thus, it is not necessary to make a new file.

WalletFeed has no account and no WalletFeed servers. Your transactions go from your iPhone directly to the folder or the service that you select.

Some of the destinations are:

- A [CSV file](/guides/apple-card-to-csv/) in a folder, for example in iCloud Drive
- An [OFX file](/guides/apple-card-to-ofx/) or a [QIF file](/guides/apple-card-to-qif/) for each month
- A spreadsheet in [Google Sheets](/guides/apple-card-to-google-sheets/)
- A budget app, for example [Lunch Money](/guides/apple-card-to-lunch-money/) or [PocketSmith](/guides/apple-card-to-pocketsmith/).

For a CSV file, WalletFeed writes one file, or one file for each month. You can open a CSV file in [Excel](/guides/apple-card-to-excel/) or [Numbers](/guides/apple-card-to-numbers/).

An OFX or QIF file from WalletFeed includes a charge only after the charge posts.

> **Note:** WalletFeed writes CSV, OFX and QIF files. It does not write QFX or QBO files. Quicken for Windows cannot use the OFX files from WalletFeed, but it can use the CSV files.

To add a CSV file that WalletFeed updates:

1. On your iPhone, open WalletFeed.
2. Tap **Destinations**.
3. Tap **+** at the top of the screen.

   ![The Destinations screen with no destinations and the + button at the top.](app:docs-destinations-empty-pro)

4. In the search field, type `CSV`.
5. Tap **CSV File**.

   If you do not have WalletFeed Pro, the **WalletFeed Pro** screen opens. After you get WalletFeed Pro on that screen, the **Files** screen opens.

   ![The Files screen with Format set to CSV, Save As set to One File and the name WalletFeed Transactions.](app:docs-setup-csv-file)

6. Tap **Folder**.
7. Select a folder, for example in iCloud Drive.

   **Folder** then shows the name of the folder.

8. Tap **Add**.
9. When WalletFeed shows **Save Transactions to Files?**, tap **Save**.

   The message tells you the data that the folder will receive. It also gives the accounts and the period of the transactions. If you tap **Cancel**, WalletFeed removes the new destination.

WalletFeed then writes your transactions to `WalletFeed Transactions.csv` in the folder.

## Changes to the file

While WalletFeed is open, the file receives changes in seconds. When WalletFeed is not open, iOS starts WalletFeed approximately 1 hour or less after a change in Wallet. If [Background Sync](/docs/background-sync/) is on in **Settings** › **Sync**, WalletFeed then updates the file. If WalletFeed cannot open the folder at that time, the file changes when you open WalletFeed, when an automation starts, or while your iPhone charges.

## Send previous transactions

A new destination also receives previous transactions from the start date in **Settings** › **Sync** › **Initial History**. **Initial History** is **All** until you change it. After you add the destination, you can send the transactions of a different period with [Send History](/docs/send-history/) on the destination screen. You can select **30 Days**, **90 Days**, **1 Year** or **All**.

## Delete a destination

1. In WalletFeed, tap **Destinations**.
2. Tap the destination.
3. Tap **Delete**.
4. Tap **Delete** again.

After you delete the destination, the file and the transactions in it stay in the folder. A service keeps the transactions that it received. The terms of that service are applicable to these transactions.

## If there is a problem

### If this month has no statement in Wallet

Wallet makes a statement only after the end of the month. **Export CSV** in WalletFeed can make a file with the transactions of this month.

1. On your iPhone, open WalletFeed.
2. Tap **Settings** (the gear button) at the top of the screen.
3. In the **Data** section, tap **Export CSV**.
4. Tap **Range**.
5. Select **This Month**.
6. Tap **Export**.
7. Tap **Save to Files**.
8. Select a folder.
9. Tap **Save**.

### If you cannot tap **Export** in WalletFeed

You cannot tap **Export** while WalletFeed reads your transactions, or when the period has no transactions.

1. Make sure that **Transactions** shows a number.
2. If the number is 0, select a different period in **Range**.

### If there is an apostrophe before a name or a description

In the **Merchant**, **Description**, **Original Description** and **Account** columns, WalletFeed puts an apostrophe (`'`) before text that starts with `=`, `+`, `-` or `@`. Thus, a spreadsheet does not use the text as a formula. WalletFeed does not put an apostrophe before an amount.
