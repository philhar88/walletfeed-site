+++
title = "Put Apple Card transactions in YNAB"
nav_title = "YNAB"
seo_title = "Apple Card to YNAB: the YNAB app, or an OFX or CSV file"
description = "You can put your Apple Card transactions in YNAB with the YNAB app for iPhone. WalletFeed can also save them in OFX or CSV files that YNAB imports."
group = "Files and desktop apps"
order = 70
related = ["guides/apple-card-to-ofx", "guides/apple-card-to-csv"]
updated = 2026-10-30
+++

The YNAB app for iPhone can connect to Wallet and put your Apple Card transactions in YNAB. WalletFeed can also write your Apple Card, Apple Cash and Savings transactions to OFX or CSV files that YNAB can import on a computer.

## Connect YNAB to Wallet

The YNAB Help Center gives these steps for the newest YNAB app on iOS 17.4 or a newer version:

1. On your iPhone, open YNAB.
2. In the **Accounts** tab, tap **Add Account**.
3. In **Popular Options**, tap the Apple icon.
4. To connect YNAB to Wallet, do the steps that YNAB shows.
5. Select the Wallet accounts to connect to YNAB.
6. Tap **Next**.
7. To change the name or the type of an account, tap **Edit**.
8. Tap **Next**.

The YNAB Help Center tells you that YNAB gets the Wallet transactions only through the iPhone that you used to add the connection. On that iPhone, **Background App Refresh** must stay active in **Settings** › **Apps** › **YNAB**. The [YNAB Help Center page for Apple Card, Apple Cash and Savings](https://support.ynab.com/en_us/apple-connections-rkShEfrUh) gives all the steps and the error messages.

## Before you start

To import WalletFeed files into YNAB, you must have:

- WalletFeed on an iPhone with iOS 26 or a newer version
- [WalletFeed Pro](/docs/walletfeed-pro/) for files that WalletFeed updates (a subscription with a 1-week free trial, or a one-time Lifetime purchase)
- YNAB in a web browser on a computer, or YNAB in Safari on an iPad (YNAB does not import files on an iPhone)
- iCloud Drive on your iPhone and on your computer, or a different app that Files shows, for example Dropbox.

WalletFeed is available only in the US.

WalletFeed Pro is not necessary for **Export CSV**.

## Step 1: Add an OFX File destination in WalletFeed

1. On your iPhone, open WalletFeed.
2. Tap **Destinations**.
3. Tap **+** at the top of the screen.

   ![The Destinations screen has no destinations and shows the + button at the top.](app:docs-destinations-empty-pro)

4. In the **Destinations** search field, type `OFX`.
5. Tap **OFX File**.

   If you do not have WalletFeed Pro, the **WalletFeed Pro** screen opens. After you get WalletFeed Pro, the **Files** screen opens.

6. Make sure that **Format** is **OFX**.

   ![The Files screen shows OFX in Format and WalletFeed in Name.](app:docs-setup-ofx-file)

7. Tap **Folder**.
8. Select a folder in iCloud Drive.

   After you select a folder, you can tap **Add**.

9. To use a different name for the files, type the name in **Name**.

   Each month has one file. If the name is `WalletFeed`, the file for October 2026 is `WalletFeed 2026-10.ofx`.

10. Tap **Add**.

    Result: WalletFeed shows **Save Transactions to Files?** with a message. The message tells you that the folder receives the date, the merchant, the amount and other data of posted transactions. The message also gives the accounts and the period.

11. Tap **Save**.

    Result: WalletFeed writes your posted transactions to the files.

> **Note:** WalletFeed keeps no copy of the files. The files are in your iCloud Drive. WalletFeed has no account and no WalletFeed servers.

## Step 2: Keep only Apple Card transactions in the files

YNAB puts all the transactions in a file into one account. If WalletFeed reads only your Apple Card account, this step is not necessary.

1. In **Destinations**, tap the destination, for example **WalletFeed**.
2. Set **Filter** to on.
3. Tap **Accounts**.
4. Select your Apple Card account.
5. Tap the back button at the top of the screen.
6. Tap **Send History**.
7. Tap **All**.

   Result: WalletFeed writes the file again for each month that has Apple Card transactions. These files then have only your Apple Card transactions.

To put your Apple Cash transactions in a different YNAB account:

1. Add a second OFX File destination with a different name in **Name**, for example `Apple Cash` (refer to Step 1).
2. In **Destinations**, tap the new destination.
3. Set **Filter** to on.
4. Tap **Accounts**.
5. Select your Apple Cash account.
6. Tap the back button at the top of the screen.
7. Tap **Send History**.
8. Tap **All**.

## Step 3: Import a file in YNAB

1. On your computer, open YNAB in a web browser.
2. Open the iCloud Drive folder that has the files from WalletFeed.
3. Drag the file for a month, for example `WalletFeed 2026-10.ofx`, into YNAB.

   Result: YNAB shows **Import Transactions**. You can drag more than one OFX file at the same time.

4. At the top of **Import Transactions**, make sure that YNAB shows your Apple Card account.
5. To put the memos in YNAB, select **Import Memos**.

   The memo has the description and the card statement text, if they are different from the merchant name. If a transaction has a foreign amount, the memo also has it.

6. Import the file.

If you import a file again, YNAB does not add the transactions that have the same date and amount as transactions that it added before.

> **Note:** On an iPad, you can drag the file from Files into YNAB in Safari. The [YNAB Help Center page for file import](https://support.ynab.com/en_us/file-based-import-a-guide-Bkj4Sszyo) gives the steps.

YNAB does not keep the file, but it keeps the transactions from the file. The terms of YNAB are applicable to these transactions.

## Use a CSV file

YNAB also imports CSV files. The OFX file has only posted transactions. A CSV file from WalletFeed has posted and pending transactions. For a pending transaction, the Status column contains `pending` or `authorized`.

WalletFeed Pro is not necessary for **Export CSV**. To make a CSV file one time:

1. On your iPhone, open WalletFeed.
2. At the top of the screen, tap **Settings** (the gear button).
3. In the **Data** section, tap **Export CSV**.

   ![The Settings screen shows Export CSV in the Data section.](app:docs-settings-3)

4. Tap **Range**.

   ![The Export CSV screen shows the range This Month and 29 transactions.](app:docs-export-csv)

5. Select a range, for example **Last Month**.
6. Tap **Export**.
7. Tap **Save to Files**.
8. Save the file in iCloud Drive.

The file has the transactions of all the Wallet accounts that WalletFeed reads. YNAB puts all these transactions in the account that you select.

With WalletFeed Pro, a CSV File destination updates a file when your transactions change. The destination can have a filter for one account. The [guide for a CSV file](/guides/apple-card-to-csv/) gives the steps.

In YNAB, use these columns of the CSV file:

| YNAB field | Column in the CSV file |
| --- | --- |
| **Date** | Date |
| **Payee** | Merchant |
| **Memo** | Description |
| **Outflow** | Amount |
| **Inflow** | Amount |

To import the CSV file in YNAB:

1. On your computer, open YNAB in a web browser.
2. Drag the CSV file into YNAB.
3. At the top of **Import Transactions**, make sure that YNAB shows your Apple Card account.
4. Make sure that each YNAB field uses the CSV column that the table shows.

   The CSV file has one Amount column. A purchase is a negative amount. The YNAB Help Center tells you to select **Amount** for **Outflow** and for **Inflow**.

5. Import the file.

## Data that YNAB receives

The OFX file has this information for each posted transaction:

| Wallet data | In the OFX file | In YNAB |
| --- | --- | --- |
| Merchant | The merchant name, or the description if Wallet has no merchant name. The file keeps the first 32 characters. | **Payee** |
| Amount | A purchase is negative. A payment or a refund is more than zero. | **Outflow** or **Inflow** |
| Date and posted date | The date of the transaction and the date that it posted | **Date** |
| Description, card statement text and foreign amount | The memo of the transaction | **Memo**, if you select **Import Memos** |
| Account | One statement for each Wallet account | The YNAB account that you select |

The OFX file has no category. The YNAB Help Center tells you that YNAB changes the payee names from a file. YNAB also gives each transaction the category that its payee usually has. You can change the payee and the category of each transaction in YNAB.

## Changes to the files

While WalletFeed is open, its files in iCloud Drive receive changes in seconds. When WalletFeed is not open, iOS starts WalletFeed approximately 1 hour or less after a change in Wallet. If [Background Sync](/docs/background-sync/) is on in **Settings** › **Sync**, WalletFeed then updates the files.

If **Background Sync** is off, or if WalletFeed cannot open the folder at that time, the files get the changes when one of these occurs:

- You open WalletFeed.
- A Shortcuts automation starts WalletFeed.
- iOS starts WalletFeed when your iPhone gets power from a charger.

WalletFeed writes the file for a month again each time that a transaction in that month changes. YNAB gets the changes only when you import the file again.

A pending transaction is not in the file. When the transaction posts, WalletFeed adds it to the file for its month. A refund is a new transaction with an amount that is more than zero.

If Wallet removes a transaction, WalletFeed removes it from the file. If the transaction is in YNAB, you must delete it in YNAB.

## Send previous transactions

A new OFX File destination also receives previous posted transactions from the start date in **Settings** › **Sync** › **Initial History**. **Initial History** is **All** until you change it.

The YNAB Help Center recommends that a file has only transactions from the last 12 months. If a file has transactions from before the start date of your YNAB account, YNAB lets you include them. But it is not necessary to include them.

To write the previous transactions to the files again:

1. On your iPhone, open WalletFeed.
2. Tap **Destinations**.
3. Tap the destination, for example **WalletFeed**.
4. Tap **Send History**.
5. Tap **30 Days**, **90 Days**, **1 Year** or **All**.

   Result: WalletFeed writes the file for each month in that period again. The file for the first month then has only the transactions from the start of the period.

The [Send History](/docs/send-history/) page gives more information.

## Change or remove the destination

To change the destination, tap it in [**Destinations**](/docs/destinations/). You can make these changes:

- To send only some transactions, set **Filter** to on. Then select the accounts, the categories or a minimum amount. Refer to [Choose what a destination receives](/docs/choose-what-to-send/).
- To use a different folder, tap **Change Folder**. WalletFeed then writes all your transactions to new files in that folder.
- To stop the changes to the files for a time, set **Enabled** to off.
- To change the name of the destination, type a different name in **Name**. The names of the files stay the same.

To remove the destination:

1. In **Destinations**, tap the destination.
2. Tap **Delete**.
3. In the message, tap **Delete** again.

The files stay in iCloud Drive. The transactions from the files stay in YNAB.

## If there is a problem

### If YNAB puts Apple Cash transactions in your Apple Card account

The file has the transactions of more than one Wallet account.

1. In WalletFeed, set a filter for your Apple Card account (refer to Step 2).
2. In YNAB, delete the transactions that are not from your Apple Card account.

### If some transactions from a file are not in YNAB

YNAB does not add a transaction from a file if it added the same transaction before. If you deleted the transaction in YNAB, YNAB does not add it again.

1. In **Import Transactions**, look at the transactions above **Options**.

   For each transaction that YNAB did not add, YNAB shows the cause.

2. If you deleted the transactions in YNAB, type them in YNAB.

### If a pending transaction is not in the file

The OFX file has a transaction only after the transaction posts.

1. After the transaction posts, import the file for its month again.

### If the destination shows "Can't open the folder. Choose it again."

WalletFeed cannot open the folder that you selected.

1. In **Destinations**, tap the destination.
2. Tap **Change Folder**.
3. Select the folder again.

   Result: WalletFeed writes your transactions to the files again.

### If the files on your computer do not show new transactions

WalletFeed did not update the files after the last change in Wallet.

1. On your iPhone, open WalletFeed.
2. At the top of the screen, tap **Settings** (the gear button).
3. In the **Sync** section, tap **Sync Now**.

   Result: **Sync Now** shows the time of the last update.

### If Destinations shows "Sync Requires Pro"

You do not have WalletFeed Pro at this time. WalletFeed keeps the destination, but it does not update the files.

1. In **Destinations**, tap **Upgrade**.
2. Select a plan.
3. Tap **Start Free Trial**, **Subscribe** or **Buy Lifetime**.
