+++
title = "Open Apple Card transactions in Excel"
nav_title = "Excel"
seo_title = "Apple Card to Excel: export transactions as a CSV file"
description = "WalletFeed exports your Apple Card transactions to a CSV file on your iPhone. Excel opens the file on a Mac or a PC."
group = "Sheets and databases"
order = 70
related = ["guides/apple-card-to-csv", "guides/apple-card-to-google-sheets", "docs/export-csv"]
updated = 2026-10-30
+++

WalletFeed exports your Apple Card, Apple Cash and Savings transactions from your iPhone to a CSV file that Excel opens on a Mac or a PC. You can export a file with [**Export CSV**](/docs/export-csv/), or get [WalletFeed Pro](/docs/walletfeed-pro/) and let WalletFeed update a file in iCloud Drive for you.

## Before you start

You must have these items:

- An iPhone with iOS 26 or a newer version
- WalletFeed on your iPhone
- Excel on a Mac or a PC
- iCloud Drive on your iPhone and on your computer
- WalletFeed Pro, for a file that WalletFeed updates.

WalletFeed is available only in the US. WalletFeed Pro is a subscription with a 1-week free trial, or a one-time Lifetime purchase. You can also use a different location in Files, for example Dropbox.

## Step 1: Make a CSV file on your iPhone

Use one of these methods.

### Export a file one time

WalletFeed Pro is not necessary for **Export CSV**.

1. On your iPhone, open WalletFeed.
2. At the top of the screen, tap **Settings** (the gear button).
3. In the **Data** section, tap **Export CSV**.

   ![The Settings screen shows Export CSV below Data.](app:docs-settings-3)

4. Tap **Range**.
5. Select **This Month**, **Last Month**, **Last 90 Days**, **This Year** or **All**.

   **Transactions** shows the number of transactions in the range.

   ![The Export CSV screen shows the range This Month and 29 transactions.](app:docs-export-csv)

6. Tap **Export**.

   The share sheet opens.

7. Tap **Save to Files**.
8. Save the file in a folder in iCloud Drive.

   The name of the file includes the range, for example `Apple Card This Month.csv`.

> **Note:** In the share sheet, you can also tap a different app to send the file to your computer. WalletFeed keeps no copy of the file. The file goes only to the location that you select.

### Update a file in iCloud Drive (WalletFeed Pro)

With WalletFeed Pro, WalletFeed writes your transactions to a CSV file in a folder that you select. When your transactions change, WalletFeed updates the file.

1. On your iPhone, open WalletFeed.
2. Tap **Destinations**.
3. Tap **+**.

   ![The Destinations screen has no destinations and shows the + button at the top.](app:docs-destinations-empty-pro)

4. In the search field, type `Excel`.
5. Tap **CSV File**.

   If you do not have WalletFeed Pro, WalletFeed shows the WalletFeed Pro screen first. After you start the free trial or get WalletFeed Pro, the **Files** screen opens.

6. Make sure that **Format** is **CSV**.
7. Make sure that **Save As** is **One File**.

   With **One File**, all your transactions are in one file, and WalletFeed puts the newest transaction first.

   ![The Files screen shows CSV in Format and One File in Save As.](app:docs-setup-csv-file)

   > **Note:** With **One File per Month**, each month has a different file, for example `WalletFeed 2026-10.csv`.

8. Tap **Folder**.
9. Select a folder in iCloud Drive.

   **Add** is available after you select a folder.

10. If you want a different name for the file, type the name in **Name**.

    If you do not change the name, the file is `WalletFeed Transactions.csv`.

11. Tap **Add**.

    The message **Save Transactions to Files?** opens. It shows the data that the folder receives, the accounts and the start date.

12. Tap **Save**.

    Then, WalletFeed writes your transactions to the file.

> **Note:** WalletFeed has no account and no WalletFeed servers. WalletFeed keeps no copy of the file. The file is in the folder that you selected.

## Step 2: Open the file in Excel

1. On your Mac or PC, find the file, for example in iCloud Drive.
2. Open the file in Excel.

   Excel shows one row for each transaction.

3. If WalletFeed updates the file for you, save your changes in a copy that has a different name.

> **Note:** When WalletFeed updates the file, it removes the columns that it does not write. It also removes the rows that have no WalletFeed ID. With **One File per Month**, WalletFeed writes the full file for a month again, and your changes to that file do not stay.

## Columns in the file

The first row has the names of the columns. Each row after it is one transaction. The file has these columns:

| Column | Value |
| --- | --- |
| Date | The date of the transaction, for example 2026-10-30. |
| Posted Date | The date that the transaction posted. This cell is empty while the transaction is pending. |
| Merchant | The name of the merchant. If Wallet has no merchant name, this cell has the text from Description. |
| Description | The description of the transaction from Wallet. |
| Original Description | The text of the transaction from the card network. |
| Amount | The value, for example `-23.40`. It is less than zero for a purchase and more than zero for a payment or a refund. |
| Currency | The currency code, for example USD. |
| Direction | `debit` if Amount is less than zero, or `credit` if Amount is more than zero. |
| Status | The status from Wallet, for example `pending`, or `booked` for a posted transaction. A file from **Export CSV** can also have `rejected` for a declined transaction. |
| Type | The type from Wallet, for example `pointOfSale` or `refund`. |
| Category | The WalletFeed category, for example Groceries. |
| MCC | The merchant category code, for example 5411. |
| Account | The name of the Wallet account, for example Apple Card. |
| Foreign Amount | For a transaction in a different currency, the value in that currency. |
| Foreign Currency | The code of the currency in Foreign Amount, for example EUR. |
| WalletFeed ID | The ID of the transaction. WalletFeed uses it to find the row of a transaction that changes. |

If the first character in a text cell is `=`, `+`, `-` or `@`, WalletFeed puts an apostrophe (`'`) before the text. As a result, Excel reads the cell as text and does not use it as a formula.

## Changes to the file

While WalletFeed is open, the file in iCloud Drive receives changes in seconds. When WalletFeed is closed, iOS starts WalletFeed in approximately 1 hour or less after a change in Wallet. For this, [Background Sync](/docs/background-sync/) must be on in **Settings** › **Sync**.

If WalletFeed cannot open the folder at that time, the file receives the changes when one of these conditions occurs:

- You open WalletFeed.
- A Shortcuts automation starts WalletFeed.
- iOS starts WalletFeed while your iPhone charges.

A pending transaction is in the file with the status `pending` or `authorized`. When the transaction posts, WalletFeed changes the same row. WalletFeed removes declined transactions from the file. A refund is a new row that has a value more than zero in Amount.

With **One File per Month**, WalletFeed writes the file for a month again each time that a transaction in that month changes.

## Send previous transactions

A new CSV File destination also receives your previous transactions, from the start date in **Settings** › **Sync** › **Initial History**. **Initial History** is **All** until you change it. You can select **Today**, **30 Days**, **90 Days**, **1 Year** or **All**.

To send previous transactions to a destination after you add it:

1. On your iPhone, open WalletFeed.
2. Tap **Destinations**.
3. Tap the destination, for example **WalletFeed Transactions**.
4. Tap **Send History**.
5. Select **30 Days**, **90 Days**, **1 Year** or **All**.

WalletFeed does not make two rows for one transaction. With **One File**, it finds the row that has the WalletFeed ID of the transaction and changes that row. For more information, refer to [Send History](/docs/send-history/).

## Change or remove the destination

To change the destination, tap it in [**Destinations**](/docs/destinations/). You can make these changes:

- To write only some transactions to the file, set **Filter** to on. Then, select accounts in **Accounts** or categories in **Categories**, or type a value in **Minimum**.
- To use a different folder, tap **Change Folder**. WalletFeed then writes your transactions from the start date to a file in that folder.
- To stop the updates to the file but keep the destination, set **Enabled** to off.
- To change the name of the destination, type a different name in **Name**. The name of the file does not change.

With **One File**, WalletFeed does not remove the rows that it wrote before you changed the filter. With **One File per Month**, WalletFeed uses the filter each time that it writes the file for a month again. It then removes the transactions that the filter does not include.

To remove the destination:

1. In **Destinations**, tap the destination.
2. Tap **Delete**.
3. In the message, tap **Delete** again.

The file and the transactions that WalletFeed wrote to it stay in the folder.

## If there is a problem

### If you cannot tap Export

You cannot tap **Export** while WalletFeed reads the transactions, or if the range has no transactions.

1. Wait until **Transactions** shows a number.
2. If the number is 0, tap **Range**.
3. Select a longer range, for example **All**.

### If the destination shows "Can't open the folder. Choose it again."

WalletFeed cannot open the folder that you selected.

1. In **Destinations**, tap the destination.
2. Tap **Change Folder**.
3. Select the folder again.

WalletFeed writes your transactions to the file again. It does not make two rows for one transaction.

### If the destination shows "The file has no WalletFeed ID column."

WalletFeed cannot find the rows that it wrote, because the file has no WalletFeed ID column. For example, this problem occurs if you remove the column in Excel.

1. On your computer, change the name of the file.
2. On your iPhone, in **Destinations**, tap the destination.
3. Tap **Send History**.
4. Select **All**.

WalletFeed makes a new file and writes your transactions to it.

### If the file on your computer does not show new transactions

WalletFeed did not update the file after the last change in Wallet.

1. On your iPhone, open WalletFeed.
2. At the top of the screen, tap **Settings** (the gear button).
3. In the **Sync** section, tap **Sync Now**.

   **Sync Now** shows the time of the last sync.

4. On your computer, open the file in Excel again.

### If Destinations shows "Sync Requires Pro"

You do not have WalletFeed Pro at this time. WalletFeed keeps the destination, but it does not update the file.

1. In **Destinations**, tap **Upgrade**.
2. Start the free trial, or get WalletFeed Pro.
