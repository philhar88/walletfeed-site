# Open Apple Card transactions in Numbers

WalletFeed saves your Apple Card, Apple Cash and Savings transactions from your iPhone to a CSV file that you open in Numbers as a spreadsheet. With WalletFeed Pro, WalletFeed updates the file when your transactions change.

## Before you start

To do the steps on this page, you must have:

- An iPhone with iOS 26 or a newer version
- WalletFeed, with access to your Apple Card, Apple Cash or Savings account
- Numbers on your iPhone, or on a Mac that has access to your iCloud Drive
- [WalletFeed Pro](/docs/walletfeed-pro/), for a file that WalletFeed updates.

WalletFeed is available only in the US. WalletFeed Pro is a subscription with a 1-week free trial, or a one-time Lifetime purchase. Without WalletFeed Pro, you can [export one CSV file](#export-one-csv-file-without-walletfeed-pro), but WalletFeed does not update that file.

## Step 1: Add a CSV file in WalletFeed

1. On your iPhone, open WalletFeed.
2. Tap **Destinations**.
3. Tap **+** at the top of the screen.

   ![The Destinations screen with no destinations and the + button at the top.](https://walletfeed.app/guides/apple-card-to-numbers/walletfeed-destinations-empty-pro.webp)

4. In the search field, type `Numbers`.

   ![The Add Destination screen with the Destinations search field above the Budgeting list.](https://walletfeed.app/guides/apple-card-to-numbers/walletfeed-add-destination.webp)

5. Tap **CSV File**.

   If you do not have WalletFeed Pro, the **WalletFeed Pro** screen opens. After you get WalletFeed Pro, the **Files** screen opens.

6. Make sure that **Format** is **CSV**.
7. Make sure that **Save As** is **One File**.

   ![The Files screen with Format set to CSV, Save As set to One File and the name WalletFeed Transactions.](https://walletfeed.app/guides/apple-card-to-numbers/walletfeed-setup-csv-file.webp)

   With **One File**, WalletFeed writes all your transactions to one file. The rows are in date sequence, and the row with the last date is at the top. You can also select **One File per Month**. Then each file has its month in the name, for example `WalletFeed 2026-10.csv`.

8. Tap **Folder**.
9. Select a folder in iCloud Drive.

   **Folder** then shows the name of the folder.

10. To use a different file name, type it in **Name**.

    WalletFeed adds `.csv` to the name, for example `WalletFeed Transactions.csv`.

11. Tap **Add** at the top of the screen.

    You can tap **Add** only after you select a folder.

12. When WalletFeed shows **Save Transactions to Files?**, tap **Save**.

    The message tells you the data that the folder receives. It also gives the accounts and the period of the transactions. If you tap **Cancel**, WalletFeed removes the new destination.

WalletFeed then writes your transactions to the file.

## Step 2: Open the file in Numbers

1. On your iPhone, open Numbers.
2. Tap **Browse** at the bottom of the screen.
3. Open the folder that you selected in Step 1.
4. Tap `WalletFeed Transactions.csv`, or the file with the name that you typed.

Numbers shows each transaction as a row in the spreadsheet. If WalletFeed changes the file after you open it, Numbers shows the changes only after you open the file again.

## Export one CSV file without WalletFeed Pro

[Export CSV](/docs/export-csv/) makes one CSV file with the transactions from a period that you select. You can use Export CSV without WalletFeed Pro. The file does not change after you export it.

1. On your iPhone, open WalletFeed.
2. Tap **Settings** (the gear button) at the top of the screen.
3. Tap **Export CSV**.

   ![Settings with Export CSV in the Data section.](https://walletfeed.app/guides/apple-card-to-numbers/walletfeed-settings-3.webp)

4. Tap **Range**.
5. Select a period: **This Month**, **Last Month**, **Last 90 Days**, **This Year** or **All**.

   ![The Export CSV screen with Range set to This Month, 29 transactions and the Export button.](https://walletfeed.app/guides/apple-card-to-numbers/walletfeed-export-csv.webp)

   **Transactions** shows the number of transactions in the period.

6. Tap **Export**.
7. In the share sheet, tap **Save to Files**.
8. Select a folder in iCloud Drive.
9. Save the file in that folder.

   The name of the file has the period in it, for example `Apple Card Last Month.csv`.

10. To open the file in Numbers, do the steps in [Step 2](#step-2-open-the-file-in-numbers).

## Columns in the file

Each CSV file from WalletFeed has one row for each transaction, and these columns:

| Column | Data |
| --- | --- |
| **Date** | The date of the transaction, for example 2026-10-28. |
| **Posted Date** | The date that the charge posted. It is empty while the charge is pending. |
| **Merchant** | The merchant name. If Wallet has no merchant name, this column has the text from **Description**. |
| **Description** | The text of the transaction in Wallet. |
| **Original Description** | The card statement text from the card network. |
| **Amount** | The value of the transaction, for example -23.40. It has a minus sign for purchases and fees, and no minus sign for payments and refunds. |
| **Currency** | The currency code, for example USD. |
| **Direction** | `debit` for purchases and fees, or `credit` for refunds, payments and deposits. |
| **Status** | The condition of the transaction in Wallet: `authorized`, `pending`, `booked` (posted) or `memo`. A file from **Export CSV** can also have `rejected`, for a declined charge. |
| **Type** | The transaction type in Wallet, for example `pointOfSale` (a purchase), `refund`, `billPayment` (a payment) or `transfer`. |
| **Category** | The WalletFeed category, for example Groceries, Dining or Cash & Transfers. |
| **MCC** | The merchant category code from the card network. |
| **Account** | The Wallet account, for example Apple Card. |
| **Foreign Amount** | For a purchase in a different currency, the value in that currency. |
| **Foreign Currency** | The code of that different currency. |
| **WalletFeed ID** | The ID of the transaction. WalletFeed uses it to find and update each row. |

> **Note:** WalletFeed writes only these columns. When it updates `WalletFeed Transactions.csv`, it removes all other columns.

## Changes to the file

While WalletFeed is open, `WalletFeed Transactions.csv` receives changes in seconds. When WalletFeed is closed, iOS starts WalletFeed in approximately 1 hour or less after a change in Wallet. WalletFeed then updates the file. For this, [Background Sync](/docs/background-sync/) must be on in **Settings** › **Sync**. If WalletFeed cannot open the folder at that time, the file changes the next time that you open WalletFeed, or while your iPhone charges.

A pending charge is in the file with `pending` or `authorized` in **Status**. When the charge posts, WalletFeed updates the same row. WalletFeed removes declined charges and the transactions that Wallet deletes. A refund is a different transaction. Its **Amount** has no minus sign.

## Send previous transactions

A new CSV file also receives your previous transactions, from the start date in **Settings** › **Sync** › **Initial History**. **Initial History** is **All** until you change it. To add transactions from before that date, use [Send History](/docs/send-history/):

1. In WalletFeed, tap **Destinations**.
2. Tap **WalletFeed Transactions**, or the name that you typed.
3. Tap **Send History**.
4. Tap **30 Days**, **90 Days**, **1 Year** or **All**.

Because WalletFeed finds each row by its **WalletFeed ID**, a transaction does not get a second row.

## Change or remove the destination

1. In WalletFeed, tap **Destinations**.
2. Tap **WalletFeed Transactions**, or the name that you typed.
3. Do one of these steps:
   - To send only some transactions, turn on **Filter**. Then set **Include**, **Minimum**, **Accounts**, **Categories** or **Exclude**.
   - To put the file in a different folder, tap **Change Folder**. Then select the folder.
   - To stop the changes to the file, turn off **Enabled**.
   - To remove the destination, tap **Delete**. Then tap **Delete** again.

After you select a different folder, WalletFeed writes the file again in the new folder the next time that it updates the destination. If you delete the destination, the file and its transactions stay in the folder.

## If there is a problem

### If WalletFeed shows “Couldn't open this folder.”

WalletFeed cannot get access to the folder that you selected on the **Files** screen.

1. Tap **Folder**.
2. Select a different folder in iCloud Drive.

### If WalletFeed shows “Can't open the folder. Choose it again.”

WalletFeed does not have access to the folder of the destination.

1. In WalletFeed, tap **Destinations**.
2. Tap the destination.
3. Tap **Change Folder**.
4. Select the folder again.

### If WalletFeed shows “The file has no WalletFeed ID column.”

Because the file in the folder does not have the **WalletFeed ID** column, WalletFeed cannot find its rows.

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

WalletFeed writes the file only when there are transactions to put in the file.

1. In WalletFeed, tap **Destinations**.
2. Tap the destination.
3. Tap **Send Test**.

   WalletFeed then writes `WalletFeed Test.csv` to the folder. This file has a sample transaction. If this file is in the folder, WalletFeed can write to the folder.

4. To write all your transactions to the file, tap **Send History**.
5. Tap **All**.

### If new transactions are not in Numbers

WalletFeed did not update the file, or Numbers does not show the changes that WalletFeed made after you opened the file.

1. On your iPhone, open WalletFeed.
2. Tap **Settings** (the gear button) at the top of the screen.
3. Tap **Sync Now**.
4. In Numbers, open `WalletFeed Transactions.csv` again.

### If text in a cell starts with an apostrophe

WalletFeed puts an apostrophe (`'`) before text that starts with `=`, `+`, `-` or `@`. Because of the apostrophe, a spreadsheet does not use the text as a formula.

### If you cannot tap Export

**Export** is not available while WalletFeed reads the transactions, or when the period has no transactions.

1. Look at **Transactions**.
2. If it shows 0, select a different **Range**.
