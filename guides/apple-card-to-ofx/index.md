# Save Apple Card transactions as OFX files

WalletFeed saves your Apple Card, Apple Cash and Savings transactions from your iPhone in one OFX file for each month. WalletFeed updates the files automatically in a folder that you select, and you import them into your app, for example Quicken for Mac or Actual.

## Before you start

You must have:

- An iPhone with iOS 26 or a newer version
- WalletFeed, with [access to your Apple Card, Apple Cash or Savings account](/docs/wallet-accounts/)
- [WalletFeed Pro](/docs/walletfeed-pro/), which is necessary for destinations (a subscription with a 1-week free trial, or a one-time Lifetime purchase)
- An app that can import OFX files, for example Quicken for Mac, Actual, GnuCash, Moneydance, Banktivity, Goodbudget or YNAB
- If your app is on a computer, a folder that your iPhone and that computer can both open, for example in iCloud Drive

WalletFeed is available only in the US.

> **Note:** Quicken for Windows cannot import the OFX files from WalletFeed. WalletFeed does not write QFX files. Quicken for Windows can import a CSV file from WalletFeed. The [Quicken guide](/guides/apple-card-to-quicken/) has more information.

## Step 1: Add an OFX file in WalletFeed

1. On your iPhone, open WalletFeed.
2. Tap **Destinations**.
3. Tap **+** at the top of the screen.

   ![The Destinations screen with no destinations and the + button at the top.](https://walletfeed.app/guides/apple-card-to-ofx/walletfeed-destinations-empty-pro.webp)

4. In the **Destinations** search field, type `OFX`.

   ![The Add Destination screen with the Destinations search field above the Budgeting list.](https://walletfeed.app/guides/apple-card-to-ofx/walletfeed-add-destination.webp)

5. Tap **OFX File**.

   If you do not have WalletFeed Pro, the **WalletFeed Pro** screen opens. After you get WalletFeed Pro, the **Files** screen opens.

6. Make sure that **Format** is **OFX**.

   ![The Files screen with OFX in Format, no folder in Folder and WalletFeed in Name.](https://walletfeed.app/guides/apple-card-to-ofx/walletfeed-setup-ofx-file.webp)

7. Tap **Folder**.
8. Select a folder in iCloud Drive.

   **Folder** then shows the name of the folder.

9. To use a different name for the files, type the name in **Name**.

   Each file name contains this name, the month and `.ofx`. For example, the file for October 2026 is `WalletFeed 2026-10.ofx`.

10. Tap **Add**.
11. When WalletFeed shows **Save Transactions to Files?**, tap **Save**.

    The message tells you the data that the folder receives from each posted transaction. This data includes the date, the merchant and the amount. The message also tells you the accounts and the period. If you tap **Cancel**, WalletFeed removes the new destination.

WalletFeed then writes one file for each month that has posted transactions.

## Step 2: Import a file into your app

1. On your computer, open the folder that you selected in Step 1.
2. Find the file for the month, for example `WalletFeed 2026-10.ofx`.
3. In your app, import the file into the account for your Apple Card.

   In Quicken for Mac, **Bank or Brokerage File (OFX, QFX)** is in **File** › **Import**. In Actual, **Import** is on the page of the account. Actual does not show **Import** on a phone.

4. Make sure that the transactions are in the correct account.

   ![The Apple Card account in Actual with five transactions from an OFX file.](https://walletfeed.app/guides/apple-card-to-ofx/actual-budget-walletfeed-result.webp)

> **Note:** If a file has Apple Card transactions, Actual imports only the Apple Card transactions from it. Actual does not import the Apple Cash or Savings transactions in that file. With one destination for each account, Actual can import the transactions of each account. The steps are in [If Apple Cash or Savings transactions are not in the correct account](#if-apple-cash-or-savings-transactions-are-not-in-the-correct-account).

The file uses the same account ID each time. Thus, your app can put the transactions from each file into the same account.

You can import the file for a month again after WalletFeed updates it. Actual, GnuCash and Moneydance use the transaction ID to find the transactions that you imported previously. They do not import these transactions again.

## Data in the file

Each file has one statement for each Wallet account that has posted transactions in that month. A statement shows Apple Card as a credit card, Apple Cash as a checking account and Savings as a savings account. Each statement also has the currency code, for example USD, and an ID for the Wallet account. This ID is the same in each file.

Each transaction in a statement has this data:

| Data in the file | From Wallet |
| --- | --- |
| Type | The type of the transaction, for example a purchase, a fee, a payment or a transfer. |
| Posted date | The date when the transaction posted. |
| Transaction date | The date of the transaction in Wallet. |
| Amount | The value of the transaction, for example -23.40. Purchases have a minus sign. Payments and refunds have no minus sign. |
| Transaction ID | The ID of the transaction in Wallet. Apps use it to find the transactions that they imported previously. |
| Name | The merchant name, or the description if Wallet has no merchant name. The file keeps the first 32 characters. |
| Memo | The description and the card statement text, if they are different from the name. The memo also has any value in a different currency. |

Each date is the calendar day on your iPhone. The files do not include the account balance.

## Changes to the files

While WalletFeed is open, the files receive changes in seconds. When WalletFeed is closed, iOS starts WalletFeed in approximately 1 hour or less after a change in Wallet. WalletFeed then updates the files. For this, [Background Sync](/docs/background-sync/) must be on in **Settings** › **Sync**. If WalletFeed cannot open the folder at that time, the files change when you open WalletFeed, when an automation starts, or while your iPhone charges.

The files contain only posted transactions. After a pending charge posts, WalletFeed writes it to the file with the same transaction ID. WalletFeed does not write declined charges to the files. A refund has no minus sign.

When a transaction in a month changes, WalletFeed writes the full file for that month again. For a month without posted transactions, WalletFeed writes no file. If Wallet deletes a transaction, WalletFeed removes it from the file. But a transaction that you imported previously stays in your app.

## Send previous transactions

A new OFX destination also receives your previous transactions, from the start date in **Settings** › **Sync** › **Initial History**. **Initial History** is **All** until you change it. With [Send History](/docs/send-history/), WalletFeed writes the files again for a period that you select:

1. In WalletFeed, tap **Destinations**.
2. Tap **WalletFeed**, or the name that you typed in **Name**.
3. Tap **Send History**.
4. Tap **30 Days**, **90 Days**, **1 Year** or **All**.

WalletFeed then writes the file for each month in that period. If your app uses the transaction ID, it does not import a transaction two times.

## Change or remove the destination

You make all the changes in this section on the screen of the destination. The destination has the name **WalletFeed**, or the name that you typed in **Name**. A change to **Name** on that screen does not change the names of the files.

### Send only some transactions

1. In **Destinations**, tap the destination.
2. Set the **Filter** switch to on.
3. Set **Include**, **Minimum**, **Accounts**, **Categories** or **Exclude**.

### Put the files in a different folder

1. In **Destinations**, tap the destination.
2. Tap **Change Folder**.
3. Select the folder.

   At the next sync, WalletFeed writes all the files in the new folder.

### Stop the updates to the files

1. In **Destinations**, tap the destination.
2. Set the **Enabled** switch to off.

### Remove the destination

1. In **Destinations**, tap the destination.
2. Tap **Delete**.
3. Tap **Delete** again.

   The files stay in the folder.

## If there is a problem

### If WalletFeed shows “Couldn't open this folder.”

WalletFeed cannot open the folder that you selected.

1. Tap **Folder**, or **Change Folder** on the screen of the destination.
2. Select a different folder in iCloud Drive.

### If WalletFeed shows “Can't open the folder. Choose it again.”

WalletFeed cannot open the folder that the destination uses.

1. In WalletFeed, tap **Destinations**.
2. Tap the destination.
3. Tap **Change Folder**.
4. Select the folder again.

### If the folder has no OFX file

WalletFeed writes a file only for a month that has posted transactions.

1. In WalletFeed, tap **Destinations**.
2. Tap the destination.
3. Tap **Send Test**.

   The folder then gets `WalletFeed Test.ofx` with a sample transaction. If this file is in the folder, WalletFeed can write there.

4. Do not import `WalletFeed Test.ofx` into your app.
5. To write all your transactions to the files, tap **Send History**.
6. Tap **All**.

### If a pending charge is not in the file

The files contain only posted transactions.

1. Wait until the charge posts in Wallet.
2. Import the file for that month again.

### If Quicken for Windows does not import the file

Quicken for Windows cannot import the OFX files from WalletFeed.

1. In WalletFeed, add a **CSV File** destination.
2. Import the CSV file into Quicken for Windows.

The [Quicken guide](/guides/apple-card-to-quicken/) has more information.

### If a transaction has a different date in your app

Each transaction in the file has a posted date and a transaction date. Some apps show the posted date. For example, Actual shows the posted date, which can be one or more days after the date in Wallet.

### If a transaction that Wallet deleted stays in your app

WalletFeed removes the transaction from the file. But your app keeps the transactions that you imported previously.

1. In your app, find the transaction.
2. Delete the transaction.
3. If you use Actual and you import that month again, clear **Reimport deleted transactions**.

   If you do not clear **Reimport deleted transactions**, Actual shows the deleted transaction again as a new transaction.

### If Apple Cash or Savings transactions are not in the correct account

One file contains the transactions of all the Wallet accounts that WalletFeed reads. Some apps, for example YNAB, put all the transactions from one file into one account. If a file has Apple Card transactions, Actual imports only the Apple Card transactions from it.

1. In WalletFeed, tap **Destinations**.
2. Tap the destination.
3. Set the **Filter** switch to on.
4. Tap **Accounts**.
5. Select one account.
6. Go back to the destination.
7. Tap **Send History**.
8. Tap **All**.
9. For each of your other accounts, do [Step 1](#step-1-add-an-ofx-file-in-walletfeed) again with a different name in **Name**.
10. For each new destination, do steps 1 thru 8 again with a different account in step 5.

    Each destination then writes the files for one account only.

11. In your app, import the files of each destination into a different account.
