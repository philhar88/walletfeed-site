+++
title = "Save Apple Card transactions as QIF files"
nav_title = "QIF file"
seo_title = "Apple Card QIF export: monthly QIF files from iPhone"
description = "Export your Apple Card transactions as QIF files. WalletFeed saves one QIF file for each month from your iPhone to a folder that you select."
group = "Files and desktop apps"
order = 30
related = ["guides/apple-card-to-ofx", "guides/apple-card-to-quicken"]
updated = 2026-10-30
+++

WalletFeed writes your Apple Card, Apple Cash and Savings transactions from your iPhone to QIF files in a folder that you select. There is one file for each month. You import each file into an app, for example GnuCash or Banktivity.

## Before you start

You must have:

- An iPhone with iOS 26 or a newer version
- WalletFeed, with [access to your Apple Card, Apple Cash or Savings account](/docs/wallet-accounts/)
- [WalletFeed Pro](/docs/walletfeed-pro/) (a subscription with a 1-week free trial, or a one-time Lifetime purchase)
- A folder in iCloud Drive, in **On My iPhone** or in a different app that the Files app shows, for example Dropbox
- An app that can import QIF files, for example GnuCash, Moneydance, Banktivity, Actual or YNAB.

WalletFeed is available only in the US. If your app is on a computer, the computer must have access to the folder.

> **Note:** Quicken for Windows cannot import a QIF file into a credit card, checking or savings account. The [Quicken guide](/guides/apple-card-to-quicken/) tells you the files that Quicken can import.

## Step 1: Add a QIF file in WalletFeed

1. On your iPhone, open WalletFeed.
2. Tap **Destinations**.
3. Tap **+** at the top of the screen.

   ![The Destinations screen with no destinations and the + button at the top.](app:docs-destinations-empty-pro)

4. In the **Destinations** search field, type `QIF`.

   ![The Add Destination screen with the Destinations search field above the Budgeting list.](app:08-add-destination)

5. Tap **QIF File**.

   If you do not have WalletFeed Pro, the **WalletFeed Pro** screen opens. After you get WalletFeed Pro, the **Files** screen opens.

6. Make sure that **Format** is **QIF**.

   ![The Files screen with QIF in Format, no folder in Folder and WalletFeed in Name.](app:docs-setup-qif-file)

7. Tap **Folder**.
8. Select a folder, for example a folder in iCloud Drive.

   **Folder** then shows the name of the folder.

9. To use a different name for the files, type it in **Name**.

   Each file gets the name, the month and `.qif`, for example `WalletFeed 2026-10.qif`.

10. Tap **Add**.
11. When WalletFeed shows **Save Transactions to Files?**, tap **Save**.

    The message tells you the data that the folder receives, the accounts and the period. It also tells you that the folder receives only posted transactions. If you tap **Cancel**, WalletFeed removes the new destination.

WalletFeed then writes a QIF file for each month that has posted transactions. WalletFeed keeps no copy of the files.

## Step 2: Import a QIF file into your app

A QIF file has no ID for each transaction. Thus, your app can import the same transaction two times.

1. Wait until the end of the month.

   Each charge goes into the file for the month of its date, but only after the charge posts. As a result, the file can change after the end of the month.

2. Open your app on the computer or iPhone that has access to the folder.
3. In your app, import the file for the month, for example `WalletFeed 2026-10.qif`.
4. If your app lets you select a date format, select month, day, year (`MM/DD/YYYY`).
5. If your app lets you select an account, select the account for the transactions in the file.
6. Do not import the file for that month again.

   If you import a month two times, your app can show each transaction two times.

> **Note:** Actual shows its **Import** button only on a computer, not on a phone. Actual can import a QIF file only if the file has one Wallet account. [Get one file for each account](#get-one-file-for-each-account) tells you how to make these files.

## Data in the QIF files

Each file contains the posted transactions of one month from the Wallet accounts that the destination gets. Each transaction has these fields:

| Field | Data |
| --- | --- |
| Date (`D`) | The date of the transaction, as month, day, year, for example `10/28/2026`. |
| Amount (`T`) | The amount of the transaction. Purchases have a minus sign, for example `-23.40`. Payments and refunds have no minus sign. |
| Cleared (`C`) | `*` for each transaction, because each transaction in the file posted. |
| Payee (`P`) | The merchant name. If Wallet has no merchant name, the payee is the description. |
| Memo (`M`) | The description and the card statement text, if they are different from the payee. |
| Category (`L`) | The WalletFeed category, for example Groceries or Dining. A transaction in Other has no category. |

For a transaction in a different currency, the memo also contains the amount in that currency and the currency code. The file does not contain the currency, the posted date, the merchant category code or a transaction ID.

A file with one Wallet account has one section. In the file, your Apple Card is a credit card account (`CCard`). Your Apple Cash and Savings accounts are bank accounts (`Bank`). A file with more than one Wallet account has one section for each account. Each section starts with the name of the account.

## Changes to the files

While WalletFeed is open, the files receive changes in seconds. When WalletFeed is closed, iOS starts WalletFeed in approximately 1 hour or less after a change in Wallet. For this, [Background Sync](/docs/background-sync/) must be on in **Settings** › **Sync**. If WalletFeed cannot open the folder at that time, the files change when you open WalletFeed, when an [automation](/docs/siri-and-shortcuts/#send-transactions-with-an-automation) starts, or while your iPhone charges.

A pending charge is not in the file. When the charge posts, WalletFeed adds it to the file for the month of its date. Declined charges do not go into the file. A refund is a different transaction. Its amount has no minus sign.

When a transaction in a month changes, WalletFeed writes the full file for that month again. Changes that you make to a file stay only until WalletFeed writes the file again. If Wallet deletes a transaction from this month or last month, WalletFeed removes it from the file. If you previously imported that transaction into your app, it stays in your app until you delete it.

## Send previous transactions

A new QIF destination also receives your previous transactions, from the start date in **Settings** › **Sync** › **Initial History**. **Initial History** is **All** until you change it. With [Send History](/docs/send-history/), WalletFeed writes the files again for a period that you select:

1. In WalletFeed, tap **Destinations**.
2. Tap **WalletFeed**, or the name that you typed in **Name**.
3. Tap **Send History**.
4. Tap **30 Days**, **90 Days**, **1 Year** or **All**.

WalletFeed then writes the files of those months again.

> **Note:** If you import a month again after **Send History**, your app can show each transaction of that month two times.

## Change or remove the destination

In WalletFeed, the destination has the name **WalletFeed**, or the name that you typed in **Name**. A change to **Name** on the screen of the destination does not change the names of the files.

### Send only some transactions

1. In **Destinations**, tap the destination.
2. Set the **Filter** switch to on.
3. Set **Include**, **Minimum**, **Accounts**, **Categories** or **Exclude**.

WalletFeed uses the new [filter](/docs/choose-what-to-send/) for the files that it writes after the change. QIF files contain only posted transactions. **Include Pending** does not change this.

### Get one file for each account

Each file of a destination contains the transactions of all the Wallet accounts that the destination gets. To get a different file for each account, use one destination for each account:

1. In WalletFeed, tap **Destinations**.
2. Tap the QIF destination.
3. Set the **Filter** switch to on.
4. Tap **Accounts**.
5. Tap the account that this destination gets.
6. On your iPhone, open the Files app.
7. In the folder, delete the QIF files of this destination, for example `WalletFeed 2026-10.qif`.
8. In WalletFeed, on the screen of the destination, tap **Send History**.
9. Tap **All**.
10. For each of the other accounts, do [Step 1](#step-1-add-a-qif-file-in-walletfeed) again with a different name in **Name**.
11. For each new destination, do steps 1 to 9 of this list again.

### Put the files in a different folder

1. In **Destinations**, tap the destination.
2. Tap **Change Folder**.
3. Select the folder.

   Then WalletFeed writes all the files again in the new folder.

### Stop the changes to the files

1. In **Destinations**, tap the destination.
2. Set the **Enabled** switch to off.

### Remove the destination

1. In **Destinations**, tap the destination.
2. Tap **Delete**.
3. Tap **Delete** again.

   The files stay in the folder.

## If there is a problem

### If your app shows each transaction two times

Your app cannot find the transactions that you imported before, because a QIF file has no transaction ID.

1. In your app, delete the transactions that you imported the second time.
2. Do not import that month again.

An OFX file has an ID for each transaction. GnuCash, Moneydance and Actual use this ID and do not import a transaction two times. If your app can import OFX files, you can use an [OFX file](/guides/apple-card-to-ofx/).

### If Actual shows "Failed parsing: doesn't look like a valid QIF file."

Actual cannot import a QIF file that has more than one Wallet account.

1. Do the steps in [Get one file for each account](#get-one-file-for-each-account).
2. In Actual, import each file into a different account.

### If your app puts the transactions of all accounts into one account

Some apps, for example YNAB, put all the transactions of a file into one account.

1. Do the steps in [Get one file for each account](#get-one-file-for-each-account).
2. In your app, import each file into a different account.

### If a charge is not in the file

The charge is pending. A QIF file includes a charge only after it posts.

1. Wait until the charge posts in Wallet.
2. In WalletFeed, tap **Settings** (the gear button) at the top of the screen.
3. Tap **Sync Now**.

If the destination has a filter, make sure that the filter includes the charge.

### If the folder has no QIF file

WalletFeed writes a file only for a month that has posted transactions.

1. In WalletFeed, tap **Destinations**.
2. Tap the destination.
3. Tap **Send Test**.

   The folder then gets `WalletFeed Test.qif` with a sample transaction. If this file is in the folder, WalletFeed can write there.

4. Do not import `WalletFeed Test.qif` into your app.
5. To write all your transactions to the files, tap **Send History**.
6. Tap **All**.

### If the dates in your app are not correct

The file uses US dates in the sequence month, day, year (`MM/DD/YYYY`).

1. In your app, delete the transactions with the incorrect dates.
2. Import the file again.
3. If your app lets you select a date format, select month, day, year.

### If WalletFeed shows "Couldn't open this folder."

WalletFeed cannot open the folder that you selected.

1. Tap **Folder**, or **Change Folder** on the screen of the destination.
2. Select a different folder.

### If the destination shows "Can't open the folder. Choose it again."

WalletFeed does not have access to the folder of the destination at this time.

1. In WalletFeed, tap **Destinations**.
2. Tap the destination.
3. Tap **Change Folder**.
4. Select the same folder again.

### If you cannot tap Add

**Add** is available only after you select a folder.

1. Tap **Folder**.
2. Select a folder.
