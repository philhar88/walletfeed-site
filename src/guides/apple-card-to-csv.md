+++
title = "Export Apple Card transactions to a CSV file automatically"
nav_title = "CSV file"
seo_title = "Apple Card to CSV: export transactions automatically"
description = "Export your Apple Card transactions from your iPhone to a CSV file. WalletFeed writes the file in a folder that you select and updates it automatically."
group = "Files and desktop apps"
order = 10
related = ["guides/export-apple-card-transactions", "guides/apple-card-to-excel", "docs/export-csv"]
updated = 2026-10-30
+++

WalletFeed exports your Apple Card, Apple Cash and Savings transactions from your iPhone to a CSV file, and updates the file automatically when your transactions change. You select a folder, for example in iCloud Drive, and WalletFeed writes one row for each transaction to `WalletFeed Transactions.csv` in that folder.

## Before you start

- An iPhone with iOS 26 or a newer version. WalletFeed is available only in the US.
- WalletFeed, with access to your Apple Card, Apple Cash or Savings account.
- [WalletFeed Pro](/docs/walletfeed-pro/), for a file that WalletFeed updates. WalletFeed Pro is a subscription with a 1-week free trial, or a one-time Lifetime purchase.
- A folder for the file. The folder can be in iCloud Drive, in **On My iPhone** or in a different file app, for example Dropbox.

Without WalletFeed Pro, you can [export one CSV file](#export-one-csv-file-without-walletfeed-pro). WalletFeed does not update that file.

## Step 1: Add a CSV file in WalletFeed

1. On your iPhone, open WalletFeed.
2. Tap **Destinations**.
3. Tap **+** at the top of the screen.

   ![The Destinations screen with no destinations and the + button at the top.](app:docs-destinations-empty-pro)

4. In the search field, type `CSV`.

   ![The Add Destination screen with the Destinations search field above the Budgeting list.](app:08-add-destination)

5. Tap **CSV File**.

   If you do not have WalletFeed Pro, the **WalletFeed Pro** screen opens. After you get WalletFeed Pro on that screen, the **Files** screen opens.

6. Make sure that **Format** is **CSV**.
7. Make sure that **Save As** is **One File**.

   ![The Files screen with Format set to CSV, Save As set to One File and the name WalletFeed Transactions.](app:docs-setup-csv-file)

   With **One File**, WalletFeed writes all your transactions to one file. The newest transaction is at the top. To get one file for each month, tap **Save As**. Then select **One File per Month**. Each file then has its month in the name, for example `WalletFeed 2026-10.csv`.

8. Tap **Folder**.
9. Select a folder, for example in iCloud Drive.

   **Folder** then shows the name of the folder.

10. To use a different file name, type it in **Name**.

    The name of the file then has `.csv` at the end. For example, if you type `Budget` or `Budget.csv`, the file is `Budget.csv`.

11. Tap **Add**.

    You can tap **Add** only after you select a folder.

12. When WalletFeed shows **Save Transactions to Files?**, tap **Save**.

    The message tells you the folder, the data that the folder receives, the accounts and the period. If you tap **Cancel**, WalletFeed removes the new destination.

WalletFeed then writes your transactions to the file. WalletFeed does not keep your transactions in the app.

## Step 2: Open the file

1. On your iPhone, open the Files app.
2. Open the folder that you selected in Step 1.
3. Tap the file, for example `WalletFeed Transactions.csv`.

   With **One File per Month**, each month has a file, for example `WalletFeed 2026-10.csv`.

If the folder is in iCloud Drive, you can also open the file on a computer that has access to your iCloud Drive. For the steps to use the file in a spreadsheet, refer to [the Numbers guide](/guides/apple-card-to-numbers/) or [the Excel guide](/guides/apple-card-to-excel/).

## Export one CSV file without WalletFeed Pro

[Export CSV](/docs/export-csv/) makes one CSV file with the transactions from a period that you select. You can use Export CSV without WalletFeed Pro. The file does not change after you export it.

1. On your iPhone, open WalletFeed.
2. Tap **Settings** (the gear button) at the top of the screen.
3. Tap **Export CSV**.

   ![The Settings screen with Export CSV in the Data section.](app:docs-settings-3)

4. Tap **Range**.

   ![The Export CSV screen with Range set to This Month, 29 transactions and the Export button.](app:docs-export-csv)

5. Select **This Month**, **Last Month**, **Last 90 Days**, **This Year** or **All**.

   **Transactions** shows the number of transactions in that period.

6. Tap **Export**.
7. In the share sheet, tap **Save to Files**.
8. Select a folder.
9. Tap **Save**.

The name of the file has the period in it, for example `Apple Card Last Month.csv`. The name starts with `Apple Card`, also for a file with Apple Cash or Savings transactions. The file has the same columns as the file that WalletFeed updates.

## Columns in the file

Each CSV file from WalletFeed has one row for each transaction, and these columns:

| Column | Data |
| --- | --- |
| **Date** | The date of the transaction in the time zone of your iPhone, for example 2026-10-28. |
| **Posted Date** | The date when the charge posted. This cell is empty while the charge is pending. |
| **Merchant** | The merchant name. If Wallet has no merchant name, this cell has the description. |
| **Description** | The description of the transaction in Wallet. |
| **Original Description** | The text of the transaction from the card network. |
| **Amount** | The value, for example -23.40. Purchases and fees are negative numbers. Payments and refunds are positive numbers. |
| **Currency** | The currency code, for example USD. |
| **Direction** | `debit` for purchases and fees, or `credit` for payments and refunds. |
| **Status** | The status in Wallet: `authorized`, `pending`, `booked` (posted) or `memo`. A file from **Export CSV** can also have `rejected` (declined). |
| **Type** | The transaction type in Wallet, for example `pointOfSale`, `refund` or `transfer`. |
| **Category** | The WalletFeed category, for example **Groceries**, **Dining** or **Cash & Transfers**. |
| **MCC** | The merchant category code from the card network. |
| **Account** | The Wallet account, for example Apple Card. |
| **Foreign Amount** | For a purchase in a different currency, the value in that currency. |
| **Foreign Currency** | The code of that different currency. |
| **WalletFeed ID** | The ID of the transaction. WalletFeed uses it to find and update each row. |

The file is UTF-8 text in the RFC 4180 CSV format. If you move the columns in `WalletFeed Transactions.csv`, WalletFeed can continue to update the file, because WalletFeed finds each column by its name. WalletFeed then writes the columns in the sequence that the table shows.

> **Note:** WalletFeed writes only these columns. When WalletFeed updates `WalletFeed Transactions.csv`, it removes all other columns and all rows that have no **WalletFeed ID**.

## Changes to the file

While WalletFeed is open, the file receives changes in seconds. When WalletFeed is closed, iOS starts WalletFeed in approximately 1 hour or less after a change in Wallet. This occurs only if [Background Sync](/docs/background-sync/) is on in **Settings** › **Sync**.

If WalletFeed cannot open the folder at that time, the file does not change. WalletFeed then updates the file at these times:

- When you open WalletFeed.
- When an automation from **Settings** › **Sync** › **Automations** starts a sync.
- While your iPhone charges, at a time that iOS selects.

A pending charge is in the file with the status `pending` or `authorized`. When the charge posts, WalletFeed updates the same row, and the status changes to `booked`. The row stays in the same position.

WalletFeed removes the rows of declined charges and the rows of transactions that Wallet deletes. A refund is a different transaction. In its row, **Amount** is a positive number and **Direction** is `credit`.

With **One File per Month**, WalletFeed writes the full file of a month again when a transaction in that month changes. A month with no transactions gets no file.

## Send previous transactions

A new CSV file also receives your previous transactions, from the start date in **Settings** › **Sync** › **Initial History**. **Initial History** is **All** until you change it. You can select **Today**, **30 Days**, **90 Days**, **1 Year** or **All**.

To add transactions from before that date, use [Send History](/docs/send-history/):

1. In WalletFeed, tap **Destinations**.
2. Tap the destination, for example **WalletFeed Transactions**.
3. Tap **Send History**.
4. Select **30 Days**, **90 Days**, **1 Year** or **All**.

Because WalletFeed finds each row by its **WalletFeed ID**, the file has only one row for each transaction.

## Change or remove the destination

1. In WalletFeed, tap **Destinations**.
2. Tap the destination, for example **WalletFeed Transactions**.
3. Do one of these steps:
   - To write only some transactions to the file, set **Filter** to on. Then set **Include**, **Minimum**, **Include Pending**, **Accounts**, **Categories** or **Exclude**.
   - To put the file in a different folder, tap **Change Folder**. Then select the folder.
   - To stop the changes to the file, set **Enabled** to off.
   - To remove the destination, tap **Delete**. Then tap **Delete** again.

After you change the folder, WalletFeed writes the transactions from the first date to a file in the new folder. If you change **Name** on this screen, the name of the file does not change.

After you delete the destination, the file stays in the folder. WalletFeed does not remove the transactions that it wrote to the file.

## If there is a problem

### If WalletFeed shows “Couldn't open this folder.”

WalletFeed cannot get access to the folder that you selected.

1. Tap **Folder**, or tap **Change Folder** on the screen of the destination.
2. Select a different folder.

### If WalletFeed shows “Can't open the folder. Choose it again.”

WalletFeed does not have access to the folder of the destination at this time.

1. In WalletFeed, tap **Destinations**.
2. Tap the destination.
3. Tap **Change Folder**.
4. Select the same folder again.

### If WalletFeed shows “The file has no WalletFeed ID column.”

WalletFeed does not change a file that has no **WalletFeed ID** column.

1. On your iPhone, open the Files app.
2. Open the folder of the destination.
3. Change the name of `WalletFeed Transactions.csv`, for example to `WalletFeed Transactions 1.csv`.
4. In WalletFeed, tap **Destinations**.
5. Tap the destination.
6. Tap **Send History**.
7. Tap **All**.

WalletFeed makes a new `WalletFeed Transactions.csv` with all your transactions.

### If the folder has no CSV file

WalletFeed did not write the file to the folder.

1. In WalletFeed, tap **Destinations**.
2. Tap the destination.
3. Tap **Send Test**.

   The folder then gets `WalletFeed Test.csv` with a sample transaction. If this file is in the folder, WalletFeed can write to the folder.

4. To write all your transactions to the file, tap **Send History**.
5. Tap **All**.

### If new transactions are not in the file

WalletFeed did not update the file, or the app that shows the file did not read it again after WalletFeed changed it.

1. On your iPhone, open WalletFeed.
2. Tap **Settings** (the gear button).
3. Tap **Sync Now**.
4. Open the file again, for example `WalletFeed Transactions.csv`.

### If a name or description starts with an apostrophe

WalletFeed puts an apostrophe (`'`) before text that starts with `=`, `+`, `-` or `@`. With the apostrophe, a spreadsheet does not use the text as a formula.

### If you cannot tap Export

**Export** is not available while WalletFeed reads the transactions, or when the period has no transactions.

1. Wait until **Transactions** shows a number.
2. If the number is 0, tap **Range**.
3. Select a different period, for example **All**.
