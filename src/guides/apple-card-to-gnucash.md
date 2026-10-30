+++
title = "Import Apple Card transactions into GnuCash"
nav_title = "GnuCash"
seo_title = "Apple Card to GnuCash: import transactions from OFX files"
description = "You can import your Apple Card transactions into GnuCash. WalletFeed writes an OFX file for each month from your iPhone, and you import the files."
group = "Files and desktop apps"
order = 60
related = ["guides/apple-card-to-ofx", "guides/apple-card-to-qif"]
updated = 2026-10-30
+++

You can import your Apple Card transactions into GnuCash with the OFX files that WalletFeed writes from your iPhone. WalletFeed writes one file for each month to a folder that you select, and you import each file in GnuCash on your computer.

## Before you start

You must have:

- An iPhone with iOS 26 or a newer version
- WalletFeed, with [access to your Apple Card, Apple Cash or Savings account](/docs/wallet-accounts/)
- [WalletFeed Pro](/docs/walletfeed-pro/), a subscription with a 1-week free trial, or a one-time Lifetime purchase
- GnuCash on your computer
- iCloud Drive on your iPhone and on your computer, or a different location that Files shows, for example Dropbox.

WalletFeed is available only in the US.

## Step 1: Add an OFX file in WalletFeed

1. On your iPhone, open WalletFeed.
2. Tap **Destinations**.
3. Tap **+** at the top of the screen.

   ![The Destinations screen with no destinations and the + button at the top.](app:docs-destinations-empty-pro)

4. In the **Destinations** search field, type `GnuCash`.

   ![The Add Destination screen with the Destinations search field above the Budgeting list.](app:08-add-destination)

   The list shows **OFX File** and **QIF File**. With an OFX file, GnuCash uses the transaction ID and does not import a transaction two times. A QIF file has no transaction ID.

5. Tap **OFX File**.

   If you do not have WalletFeed Pro, WalletFeed shows the **WalletFeed Pro** screen. After you get WalletFeed Pro, the **Files** screen opens.

6. Make sure that **Format** is **OFX**.

   ![The Files screen with OFX in Format, Choose… in Folder and WalletFeed in Name.](app:docs-setup-ofx-file)

7. Tap **Folder**.
8. Select a folder in iCloud Drive, or in the other location that you use.

   The **Folder** row shows the name of the folder. You can tap **Add** only after you select a folder.

9. To use a different name for the files, type it in **Name**.

   Each file name is that name with the month, for example `WalletFeed 2026-10.ofx`.

10. Tap **Add**.
11. When WalletFeed shows **Save Transactions to Files?**, tap **Save**.

    The message gives the folder, the data that the folder receives, the accounts and the period. If you tap **Cancel**, WalletFeed removes the new destination.

WalletFeed then writes one file for each month that has posted transactions, for example `WalletFeed 2026-09.ofx` and `WalletFeed 2026-10.ofx`.

> **Note:** WalletFeed writes the files only to the folder that you selected. It does not keep a copy of the files.

## Step 2: Import the file in GnuCash

1. On your computer, open GnuCash.
2. Click **File** › **Import** › **Import OFX/QFX…**.
3. Open the folder that you selected in WalletFeed.
4. Select the file for a month, for example `WalletFeed 2026-10.ofx`.

   To import more than one month, you can select more than one file.

5. Click **Import**.
6. In the **Select Account** window, select the GnuCash account for your Apple Card.

   You can also add a GnuCash account with **New Account…**. GnuCash shows this window only when it imports a Wallet account for the first time. If the file also has Apple Cash or Savings, GnuCash shows the window for each of them.

7. Click **OK**.

   GnuCash records the account that you selected. Then, GnuCash shows the transactions from the file in the **Generic import transaction matcher** window.

8. To set the transfer account of a new transaction, double-click its row.

   The transfer account is the account for the other part of the transaction, for example `Expenses:Groceries`.

9. Select the transfer account.
10. Click **OK**.
11. Do steps 8, 9 and 10 again for each new transaction.
12. In the **Generic import transaction matcher** window, click **OK**.

    GnuCash adds the transactions to your Apple Card account.

> **Note:** If a new transaction has no transfer account when you click **OK**, GnuCash puts it in an Imbalance account.

The next time that you import a file, GnuCash can set the transfer account of a new transaction from the accounts that you selected previously. For more information, refer to [Importing Transactions from Files](https://www.gnucash.org/docs/v5/C/gnucash-manual/trans-import.html) in the GnuCash manual.

## Data that GnuCash receives

Each OFX file has one statement for each Wallet account. Apple Card has a credit card statement. Apple Cash has a checking account statement, and Savings has a savings account statement.

Each transaction in the file has this data:

| Data | In the OFX file |
| --- | --- |
| Date | The date of the transaction in Wallet. |
| Posted date | The date that the transaction posted. GnuCash uses this date as the date of the transaction. |
| Merchant | The merchant name, or the description if Wallet has no merchant name. WalletFeed writes only the first 32 characters. |
| Amount | The amount of the transaction. Purchases have a minus sign. Payments and refunds have no minus sign. |
| Currency | The currency of the statement, for example USD. |
| Memo | The description and the card network text, if they are different from the merchant. The amount in a different currency, if there is one. |
| Type | The type of transaction, for example a purchase, a payment or a transfer. |
| Transaction ID | The ID of the transaction in Wallet. GnuCash uses it to find the transactions that it imported previously. |

The file does not include the WalletFeed category or the balance of the account. You set the transfer account of each transaction in GnuCash.

WalletFeed changes curly quotes, dashes and ellipses to ASCII characters. Some other characters change to a character that is almost the same, or to a question mark.

## New transactions and changes

While WalletFeed is open, the folder receives changes in seconds. When WalletFeed is closed, iOS starts WalletFeed in approximately 1 hour or less after a change in Wallet. For this, [Background Sync](/docs/background-sync/) must be on in **Settings** › **Sync**.

If WalletFeed cannot open the folder at that time, it writes the files when one of these occurs:

- You open WalletFeed.
- A Shortcuts automation starts WalletFeed.
- iOS starts WalletFeed while your iPhone charges.

At each sync, WalletFeed writes the full file again for each month that has a change. You can import the file of a month more than one time, for example the file of this month. GnuCash uses the transaction ID to find the transactions that it imported previously. It does not import them again. If GnuCash previously imported all the transactions in a file, it shows a message that the file has no new transactions.

An OFX file includes a transaction only after it posts. When a pending charge posts, WalletFeed adds it to the file with the same transaction ID. A charge that does not post, for example a declined charge, is not in the file.

A refund is a different transaction from the purchase. Its amount has no minus sign.

If Wallet removes a transaction from this month or last month, WalletFeed removes it from the file of that month. If GnuCash previously imported the transaction, the transaction stays in GnuCash until you delete it.

## Send previous transactions

A new OFX File destination also receives your previous transactions, from the start date in **Settings** › **Sync** › **Initial History**. **Initial History** is **All** until you change it.

[Send History](/docs/send-history/) writes the files again for a period that you select:

1. On your iPhone, open WalletFeed.
2. Tap **Destinations**.
3. Tap **WalletFeed**, or the name that you typed in **Name**.
4. Tap **Send History**.
5. Tap **30 Days**, **90 Days**, **1 Year** or **All**.
6. On your computer, import the files for the months in that period in GnuCash, as in [Step 2](#step-2-import-the-file-in-gnucash).

GnuCash does not import a transaction two times.

## Change or stop the destination

### Open the destination

1. On your iPhone, open WalletFeed.
2. Tap **Destinations**.
3. Tap **WalletFeed**, or the name that you typed in **Name**.

If you change **Name** on this screen, the names of the files stay the same.

### Send only some transactions

1. Open the destination.
2. Set **Filter** to on.
3. Set **Include**, **Minimum**, **Accounts**, **Categories** or **Exclude**.

For more information, refer to [Choose what to send](/docs/choose-what-to-send/).

### Use a different folder

1. Open the destination.
2. Tap **Change Folder**.
3. Select the new folder.

At the next sync, WalletFeed writes the files again in the new folder, from the same start date.

### Stop the destination temporarily

1. Open the destination.
2. Set **Enabled** to off.

### Remove the destination

1. Open the destination.
2. Tap **Delete**.
3. Tap **Delete** again.

The files stay in the folder. The transactions that you imported stay in GnuCash.

## If there is a problem

### If you cannot tap Add

You did not select a folder on the **Files** screen.

1. Tap **Folder**.
2. Select a folder in iCloud Drive.

### If WalletFeed shows “Couldn't open this folder.”

WalletFeed cannot get access to the folder that you selected on the **Files** screen.

1. Tap **Folder**.
2. Select a different folder in iCloud Drive.

### If the destination shows “Can't open the folder. Choose it again.”

WalletFeed does not have access to the folder of the destination.

1. Open the destination.
2. Tap **Change Folder**.
3. Select the folder again.

WalletFeed writes the files again. GnuCash does not import a transaction two times.

### If the folder has no file for a month

WalletFeed writes a file for a month only when the month has posted transactions.

1. Open the destination.
2. Tap **Send Test**.

   WalletFeed writes `WalletFeed Test.ofx` with one test transaction to the folder. This file shows that WalletFeed can write to the folder.

3. Do not import `WalletFeed Test.ofx` into GnuCash.
4. Tap **Send History**.
5. Tap **All**.

### If GnuCash does not show new transactions

WalletFeed did not write the file after the last change in Wallet, or the new charges are pending.

1. On your iPhone, open WalletFeed.
2. Tap **Settings** (the gear button) at the top of the screen.
3. Tap **Sync Now**.

   ![The Settings screen with Background Sync, Initial History and Sync Now in the Sync section.](app:docs-settings)

4. On your computer, import the file of the month again in GnuCash.

If the new charges are pending, WalletFeed adds them to the file after they post.

### If Destinations shows “Sync Requires Pro”

You do not have WalletFeed Pro at this time. WalletFeed keeps the destination, but it does not write the files.

1. In **Destinations**, tap **Upgrade**.
2. Select a plan.
3. Tap **Start Free Trial**, **Subscribe** or **Buy Lifetime**.
