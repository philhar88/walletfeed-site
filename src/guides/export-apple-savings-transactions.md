+++
title = "Make an export file of your Savings transactions"
nav_title = "Savings"
seo_title = "Export Apple Savings transactions and statements"
description = "Download your Savings statements or an export file of your transactions in Wallet. Export CSV in WalletFeed makes a CSV file of a period that you select."
group = "Export"
order = 30
related = ["guides/export-apple-card-transactions", "guides/export-apple-cash-transactions", "guides/apple-card-to-csv", "docs/export-csv", "docs/tax-pack"]
updated = 2026-11-26
+++

Wallet makes an export file of the transactions of your Apple Card Savings account from each monthly statement. Wallet also gives you each statement as a PDF file. In WalletFeed, **Export CSV** makes a CSV file of your Savings transactions from a period that you select, for example **This Month**.

WalletFeed Pro is not necessary for **Export CSV**. With WalletFeed Pro, WalletFeed also updates a CSV file when your Savings transactions change.

## Before you start

You must have:

- Your Savings account in Wallet on your iPhone
- For card.apple.com/savings, a computer with a web browser
- For WalletFeed, an iPhone with iOS 26 or a newer version
- WalletFeed, with [access to your Savings account](/docs/wallet-accounts/)
- For a file that WalletFeed updates, [WalletFeed Pro](/docs/walletfeed-pro/).

WalletFeed is available only in the US.

## Download the transactions of a statement in Wallet

A statement shows the transactions of your Savings account for the statement period. Apple tells you that the monthly statement is usually available on day 1 of each month.

1. On your iPhone, open Wallet.
2. Tap your Apple Card.
3. Tap **Savings account**.
4. Tap the More button.
5. Tap **Documents**.
6. Tap **Statements**.
7. Tap the month of the statement.
8. Tap **Export Transactions**.
9. Select a file format.

Wallet shows the file formats that you can select.

## Download a PDF statement in Wallet

1. In Wallet, open a statement (refer to steps 1 to 7 in [Download the transactions of a statement in Wallet](#download-the-transactions-of-a-statement-in-wallet)).
2. Tap **View PDF Statement**.
3. Tap the **Share** button.

   You can then save, print or send the statement.

## Download a statement on a Mac or a PC

1. On your computer, open [card.apple.com/savings](https://card.apple.com/savings).
2. Get access to your Savings account with your Apple Account.
3. Click **Documents**.
4. Click **Statements**.
5. Click the download button for the month of the statement.

Apple gives these steps in [View and update your Savings account information in Apple Wallet](https://support.apple.com/en-us/102163). For card.apple.com/savings, this page gives no **Export Transactions** function.

> **Note:** The same page gives the steps for the tax documents of your Savings account, in **Documents** › **Tax Documents**. In WalletFeed, [Tax Pack](/docs/tax-pack/) gives the totals of a full year for each Wallet account.

## Make a CSV file with Export CSV

[Export CSV](/docs/export-csv/) in WalletFeed makes one CSV file with your transactions from a period that you select. You can use it without WalletFeed Pro. The file includes pending transactions. The file does not change after WalletFeed makes it.

1. On your iPhone, open WalletFeed.
2. Tap **Settings** (the gear button) at the top of the screen.
3. In the **Data** section, tap **Export CSV**.

   ![The Settings screen with Export CSV in the Data section.](app:docs-settings-3)

4. Tap **Range**.
5. Select a period: **This Month**, **Last Month**, **Last 90 Days**, **This Year**, **Last Year** or **All**.

   ![The Export CSV screen with Range set to This Month, the number of transactions and the Export button.](app:docs-export-csv)

   **Transactions** shows the number of transactions in the period.

6. Tap **Export**.
7. Tap **Save to Files**.
8. Select a folder.
9. Tap **Save**.

At step 7, you can also select AirDrop, Mail or a different app in the menu.

**This Month** has the transactions from the first day of this month. **All** has all the transactions that WalletFeed can read in Wallet.

WalletFeed makes the file on your iPhone and does not keep it. WalletFeed has no account, and no WalletFeed server keeps your transactions.

## Find your Savings transactions in the file

The file has the transactions from each Wallet account that WalletFeed can read. The **Account** column shows the name of the account of each transaction, for example Savings. Thus, in a spreadsheet, the rows with Savings in the **Account** column are your Savings transactions.

The name of the file starts with `Apple Card` and includes the period, for example `Apple Card Last Month.csv`. The name is the same when the file has Savings transactions.

You can open the file in [Numbers](/guides/apple-card-to-numbers/) or [Excel](/guides/apple-card-to-excel/).

## Columns in the CSV file

The first row has the names of the columns. Each row after it has one transaction. The newest transaction is first.

| Column | Data |
| --- | --- |
| **Date** | The date of the transaction in the time zone of your iPhone, for example 2026-10-28. |
| **Posted Date** | The date when the transaction posted. This cell is empty until the transaction posts. |
| **Merchant** | The name of the merchant. If Wallet has no merchant name, this cell has the text from **Description**. |
| **Description** | The text of the transaction in Wallet. |
| **Original Description** | The description of the transaction with no changes. |
| **Amount** | The value, for example -23.40. The value of a `debit` is less than zero. The value of a `credit` is more than zero. |
| **Currency** | The currency code, for example USD. |
| **Direction** | `debit` or `credit`. |
| **Status** | The status in Wallet, for example `pending` or `booked`. |
| **Type** | The type of transaction in Wallet, for example `transfer`. |
| **Category** | The WalletFeed category, for example Cash & Transfers. |
| **MCC** | The merchant category code. If Wallet has no code, this cell is empty. |
| **Account** | The name of the Wallet account, for example Savings. |
| **Foreign Amount** | For a transaction in a different currency, the value in this currency. |
| **Foreign Currency** | The code of the currency in **Foreign Amount**. |
| **Exchange Rate** | For a transaction in a different currency, the exchange rate from Wallet. |
| **WalletFeed ID** | The ID of the transaction. A transaction has the same ID in each file from **Export CSV**. |

[Make a CSV file with Export CSV](/docs/export-csv/#columns-in-the-file) gives more data about each column.

## Update a file with your Savings transactions

With [WalletFeed Pro](/docs/walletfeed-pro/), WalletFeed writes your transactions to a CSV file in a folder that you select. When your transactions change, WalletFeed updates the file. Thus, it is not necessary to make a new file.

WalletFeed Pro is a subscription with a 1-week free trial, or a one-time Lifetime purchase.

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

WalletFeed then writes your transactions to `WalletFeed Transactions.csv` in the folder. The file has the same columns as the file from **Export CSV**. [Save Apple Card transactions to a CSV file](/guides/apple-card-to-csv/) gives all the steps for this file.

### Send only your Savings transactions to the file

A new destination receives the transactions of each Wallet account that WalletFeed reads. A [filter](/docs/choose-what-to-send/) selects the accounts for a destination.

1. In WalletFeed, tap **Destinations**.
2. Tap the destination.
3. Set the **Filter** switch to on.
4. Tap **Accounts**.
5. Tap your Savings account.

   The **Accounts** screen shows a checkmark on the row of the account.

6. Tap the back button at the top of the screen.

After this, the file receives only your Savings transactions. The transactions that the file received before you set the filter stay in the file.

You can also set the filter before the file receives previous transactions. [Filter the history of a new destination](/docs/choose-what-to-send/#filter-the-history-of-a-new-destination) gives the steps.

### Changes to the file

While WalletFeed is open, the file receives changes in seconds. When WalletFeed is not open, iOS starts WalletFeed approximately 1 hour or less after a change in Wallet. If [Background Sync](/docs/background-sync/) is on in **Settings** › **Sync**, WalletFeed then updates the file. If WalletFeed cannot open the folder at that time, the file changes when you open WalletFeed, when an automation starts, or while your iPhone charges.

### Delete the destination

1. In WalletFeed, tap **Destinations**.
2. Tap the destination.
3. Tap **Delete**.
4. Tap **Delete** again.

After you delete the destination, the file and the transactions in it stay in the folder.

## If there is a problem

### If the file has no Savings transactions

WalletFeed cannot read your Savings account, or the period has no Savings transactions.

1. On your iPhone, open the Settings app.
2. Tap **Privacy & Security** › **Wallet** › **WalletFeed**.
3. Select your Savings account.
4. For the Savings account, select the start date.

   From this date, WalletFeed can read the transactions of the account.

5. Open WalletFeed.
6. Make the file again with a different period in **Range**, for example **All**.

[Wallet accounts](/docs/wallet-accounts/) gives all the steps.

### If you cannot tap **Export** in WalletFeed

You cannot tap **Export** while WalletFeed reads your transactions, or when the period has no transactions.

1. Make sure that **Transactions** shows a number.
2. If the number is 0, select a different period in **Range**.
