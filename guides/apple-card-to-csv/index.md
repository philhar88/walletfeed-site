# Save Apple Card transactions to a CSV file automatically

WalletFeed writes your Apple Card, Apple Cash and Savings transactions from your iPhone to a CSV file in a folder that you select. When your transactions change, WalletFeed updates the file automatically.

## Before you start

For a CSV file that WalletFeed updates, you must have:

- An iPhone with iOS 26 or a newer version
- WalletFeed, with access to your Apple Card, Apple Cash or Savings account
- [WalletFeed Pro](/docs/walletfeed-pro/)
- A folder for the file in iCloud Drive, in **On My iPhone** or in a different file app, for example Dropbox.

WalletFeed is available only in the US.

WalletFeed Pro is a subscription with a 1-week free trial, or a one-time Lifetime purchase. Without WalletFeed Pro, you can [make one CSV file](#make-one-csv-file-without-walletfeed-pro), but WalletFeed does not update that file.

## Step 1: Add a CSV file in WalletFeed

1. On your iPhone, open WalletFeed.
2. Tap **Destinations** at the bottom of the screen.
3. Tap **+** at the top of the screen.

   ![The Destinations screen with no destinations and the + button at the top.](https://walletfeed.app/guides/apple-card-to-csv/walletfeed-destinations-empty-pro.webp)

4. In the search field, type `CSV`.

   ![The Add Destination screen with the Destinations search field above the Budgeting list.](https://walletfeed.app/guides/apple-card-to-csv/walletfeed-add-destination.webp)

5. Tap **CSV File**.

   If you do not have WalletFeed Pro, the **WalletFeed Pro** screen opens. After you get WalletFeed Pro on that screen, the **Files** screen opens.

6. Make sure that **Format** is **CSV**.
7. Make sure that **Save As** is **One File**.

   ![The Files screen shows CSV in Format, One File in Save As and WalletFeed Transactions in Name.](https://walletfeed.app/guides/apple-card-to-csv/walletfeed-setup-csv-file.webp)

   With **One File**, WalletFeed writes all your transactions to one file. The newest transaction is at the top of the file. If you select **One File per Month** in **Save As**, WalletFeed writes one file for each month. Each file has its month in the name, for example `WalletFeed 2026-10.csv`.

8. Tap **Folder**.
9. Select a folder, for example in iCloud Drive.

   **Folder** then shows the name of the folder.

10. To give the file a different name, change the text in **Name**.

    The name of the file then has `.csv` at the end. For example, if **Name** is `Budget` or `Budget.csv`, the file is `Budget.csv`.

11. Tap **Add** at the top of the screen.

    If you did not select a folder, you cannot tap **Add**.

12. When WalletFeed shows **Save Transactions to Files?**, tap **Save**.

    The message tells you the folder, the data that the folder receives, the accounts and the period. If you tap **Cancel**, WalletFeed removes the new destination.

WalletFeed then writes your transactions to the file. WalletFeed does not keep your transactions in the app.

## Step 2: Open the file

1. On your iPhone, open the Files app.
2. Open the folder that you selected in Step 1.
3. Tap the file, for example `WalletFeed Transactions.csv`.

   With **One File per Month**, each month has a file, for example `WalletFeed 2026-10.csv`.

If the folder is in iCloud Drive, you can also open the file on a computer that has access to your iCloud Drive. For the steps to use the file in a spreadsheet, refer to [the Numbers guide](/guides/apple-card-to-numbers/) or [the Excel guide](/guides/apple-card-to-excel/).

## Make one CSV file without WalletFeed Pro

[Export CSV](/docs/export-csv/) makes one CSV file with the transactions from a period that you select. You can use **Export CSV** without WalletFeed Pro. The file does not change after you save it.

1. On your iPhone, open WalletFeed.
2. Tap **Settings** (the gear button) at the top of the screen.
3. In the **Data** section, tap **Export CSV**.

   ![The Settings screen with Export CSV in the Data section.](https://walletfeed.app/guides/apple-card-to-csv/walletfeed-settings-3.webp)

4. Tap **Range**.

   ![The Export CSV screen shows This Month in Range, 29 transactions and the Export button.](https://walletfeed.app/guides/apple-card-to-csv/walletfeed-export-csv.webp)

5. Select **This Month**, **Last Month**, **Last 90 Days**, **This Year** or **All**.

   **Transactions** shows the number of transactions in that period.

6. Tap **Export**.
7. Tap **Save to Files**.
8. Select a folder.
9. Tap **Save**.

The name of the file has the period in it, for example `Apple Card Last Month.csv`. If the file has Apple Cash or Savings transactions, the name also starts with `Apple Card`. The file has the same columns as the file that WalletFeed updates.

## Columns in the file

Each CSV file from WalletFeed is UTF-8 text in the RFC 4180 CSV format. The file has one row for each transaction, and these columns:

| Column | Data |
| --- | --- |
| **Date** | The date of the transaction in the time zone of your iPhone, for example 2026-10-28. |
| **Posted Date** | The date when the charge posted. This cell is empty until the charge posts. |
| **Merchant** | The merchant name. If Wallet has no merchant name, this cell has the description. |
| **Description** | The description of the transaction in Wallet. |
| **Original Description** | The text of the transaction from the card network. |
| **Amount** | The value, for example -23.40. The value is a negative number for purchases and fees, and a positive number for payments and refunds. |
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

WalletFeed finds each column by its name. Thus, WalletFeed can update `WalletFeed Transactions.csv` after you move its columns. When WalletFeed updates the file, it writes the columns in the sequence that the table shows.

> **Caution:** Do not add columns or rows to `WalletFeed Transactions.csv`. WalletFeed writes only the columns in the table. When WalletFeed updates the file, it removes all other columns and all rows that have no **WalletFeed ID**.

## Changes to the file

While WalletFeed is open, the file receives changes in seconds. When WalletFeed is not open, iOS starts WalletFeed approximately 1 hour or less after a change in Wallet. If [Background Sync](/docs/background-sync/) is on in **Settings** › **Sync**, WalletFeed then updates the file.

If WalletFeed cannot open the folder at that time, the file does not change. WalletFeed then updates the file at these times:

- When you open WalletFeed
- When an automation from **Settings** › **Sync** › **Automations** starts WalletFeed
- While your iPhone is on a charger, at a time that iOS selects.

A pending charge is in the file with the status `pending` or `authorized`. When the charge posts, WalletFeed updates the same row. The status changes to `booked`, and the row stays in its position.

WalletFeed removes the rows of declined charges and the rows of transactions that Wallet removes. A refund is a different transaction. In its row, **Amount** is a positive number and **Direction** is `credit`.

With **One File per Month**, when a transaction in a month changes, WalletFeed writes all the transactions of that month to the file again. If a month has no transactions, WalletFeed does not write a file for that month.

## Send previous transactions

A new CSV file also receives previous transactions from the start date in **Settings** › **Sync** › **Initial History**. **Initial History** is **All** until you change it. You can select **Today**, **30 Days**, **90 Days**, **1 Year** or **All**.

To add transactions from before that date, use [Send History](/docs/send-history/):

1. In WalletFeed, tap **Destinations**.
2. Tap the destination, for example **WalletFeed Transactions**.
3. Tap **Send History**.
4. Select **30 Days**, **90 Days**, **1 Year** or **All**.

Because WalletFeed finds each row by its **WalletFeed ID**, the file has only one row for each transaction.

## Change or remove the destination

1. In WalletFeed, tap **Destinations**.
2. Tap the destination, for example **WalletFeed Transactions**.

If you change **Name** on the screen of the destination, the name of the file does not change.

### Send only some transactions to the file

1. On the screen of the destination, set **Filter** to on.
2. Set **Include**, **Minimum**, **Include Pending**, **Accounts**, **Categories** or **Exclude**.

### Use a different folder

1. On the screen of the destination, tap **Change Folder**.
2. Select the new folder.

   Then WalletFeed writes the transactions from the start date to a file in the new folder.

### Stop the changes to the file

1. On the screen of the destination, set **Enabled** to off.

### Remove the destination

1. On the screen of the destination, tap **Delete**.
2. Tap **Delete** again.

   The file stays in the folder. WalletFeed does not remove the transactions that it wrote to the file.

## If there is a problem

### If WalletFeed shows “Couldn't open this folder.”

WalletFeed cannot get access to the folder that you selected.

1. Tap **Folder** (or **Change Folder** on the screen of the destination).
2. Select a different folder.

### If WalletFeed shows “Can't open the folder. Choose it again.”

WalletFeed does not have access to the folder of the destination at this time.

1. In WalletFeed, tap **Destinations**.
2. Tap the destination.
3. Tap **Change Folder**.
4. Select the same folder again.

### If WalletFeed shows “The file has no WalletFeed ID column. Rename it to start a new one.”

WalletFeed does not change a file that has no **WalletFeed ID** column.

1. On your iPhone, open the Files app.
2. Open the folder of the destination.
3. Touch and hold `WalletFeed Transactions.csv`.
4. Tap **Rename**.
5. Type a different name, for example `WalletFeed Transactions 1`.
6. In WalletFeed, tap **Destinations**.
7. Tap the destination.
8. Tap **Send History**.
9. Tap **All**.

WalletFeed makes a new `WalletFeed Transactions.csv` with all your transactions.

### If the folder has no CSV file

WalletFeed did not write the file to the folder.

1. In WalletFeed, tap **Destinations**.
2. Tap the destination.
3. Tap **Send Test**.

   The folder then gets `WalletFeed Test.csv` with a test transaction. If the Files app shows this file in the folder, WalletFeed can write to the folder.

4. To get all your transactions in the file, tap **Send History**.
5. Tap **All**.

### If new transactions are not in the file

WalletFeed did not update the file, or the app that shows the file did not read the file again after the change.

1. On your iPhone, open WalletFeed.
2. Tap **Settings** (the gear button).
3. In the **Sync** section, tap **Sync Now**.
4. Open the file again, for example `WalletFeed Transactions.csv`.

### If a name or description starts with an apostrophe

WalletFeed puts an apostrophe (`'`) before text that starts with `=`, `+`, `-` or `@`. Thus, a spreadsheet app does not use the text as a formula.

### If you cannot tap **Export**

WalletFeed disables **Export** while it reads the transactions, or when the period has no transactions.

1. Wait until **Transactions** shows a number.
2. If the number is 0, tap **Range**.
3. Select a different period, for example **All**.
