+++
title = "Get Apple Card transactions into YNAB"
nav_title = "YNAB"
seo_title = "Apple Card to YNAB: the YNAB app, or an OFX or CSV file"
description = "Import your Apple Card transactions into YNAB with the YNAB app for iPhone, or with an OFX or CSV file that WalletFeed saves on your iPhone."
group = "Files and desktop apps"
order = 70
related = ["guides/apple-card-to-ofx", "guides/apple-card-to-csv"]
updated = 2026-10-30
+++

The YNAB app for iPhone can import your Apple Card transactions into YNAB through a connection to Wallet. WalletFeed can also save your Apple Card, Apple Cash and Savings transactions as OFX or CSV files, and YNAB can import these files on a computer.

## Import with the YNAB app

The YNAB Help Center gives these steps for an iPhone with iOS 17.4 or a newer version and an updated YNAB app:

1. On your iPhone, open YNAB.
2. In the **Accounts** tab, tap **Add Account**.
3. In **Popular Options**, tap the Apple icon.
4. Do the steps that YNAB shows to connect to Wallet.
5. Select the Wallet accounts that YNAB will import.

The YNAB Help Center says that the connection operates only with the iPhone that you used to add it. On that iPhone, **Background App Refresh** must stay on in **Settings** › **Apps** › **YNAB**. For all the steps and the error messages, refer to the [YNAB Help Center page for Apple Card, Apple Cash and Savings](https://support.ynab.com/en_us/apple-connections-rkShEfrUh).

## Before you start

To import WalletFeed files into YNAB, you must have:

- An iPhone with iOS 26 or a newer version, and WalletFeed. WalletFeed is available only in the US.
- For files that WalletFeed updates, [WalletFeed Pro](/docs/walletfeed-pro/). It is a subscription with a 1-week free trial, or a one-time Lifetime purchase. **Export CSV** is free.
- YNAB in a web browser on a computer, or YNAB in Safari on an iPad. YNAB does not import files on an iPhone.
- iCloud Drive on your iPhone and on your computer. You can also use a different app that Files shows, for example Dropbox.

## Step 1: Add an OFX File destination in WalletFeed

1. On your iPhone, open WalletFeed.
2. Tap **Destinations**.
3. Tap **+**.

   ![The Destinations screen has no destinations and shows the + button at the top.](app:docs-destinations-empty-pro)

4. In the search field, type `OFX`.
5. Tap **OFX File**.

   If you do not have WalletFeed Pro, WalletFeed shows the **WalletFeed Pro** screen first. After you start the free trial or get a plan, the **Files** screen opens.

6. Make sure that **Format** is **OFX**.

   ![The Files screen shows OFX in Format and WalletFeed in Name.](app:docs-setup-ofx-file)

7. Tap **Folder**, then select a folder in iCloud Drive.

   **Add** is available after you select a folder.

8. Optional: In **Name**, type a different name for the files.

   WalletFeed makes one file for each month. With the name `WalletFeed`, the file for October 2026 is `WalletFeed 2026-10.ofx`.

9. Tap **Add**.

   The message **Save Transactions to Files?** opens. It tells you that the folder receives the date, the merchant, the amount and other data of posted transactions. It also gives the accounts and the start date.

10. Tap **Save**.

    WalletFeed writes your posted transactions to the files.

> **Note:** WalletFeed keeps no copy of the files. The files are in your iCloud Drive. WalletFeed has no account and no WalletFeed servers.

## Step 2: Keep only Apple Card in the files

YNAB puts all the transactions in a file into one account. If WalletFeed reads only your Apple Card, go to step 3.

1. In **Destinations**, tap the destination, for example **WalletFeed**.
2. Set **Filter** to on.
3. Tap **Accounts**, then select your Apple Card account.
4. Go back to the destination.
5. Tap **Send History**.
6. Tap **All**.

   WalletFeed writes the file for each month again, with only your Apple Card transactions.

To import Apple Cash into a different YNAB account, add a second OFX File destination. In **Name**, type a different name, for example `Apple Cash`. Then set its filter to your Apple Cash account.

## Step 3: Import a file in YNAB

1. On your computer, open YNAB in a web browser.
2. Open the folder in iCloud Drive that has the files from WalletFeed.
3. Drag the file for a month, for example `WalletFeed 2026-10.ofx`, into YNAB.

   YNAB shows **Import Transactions**. You can drag more than one OFX file at the same time.

4. At the top, make sure that YNAB shows your Apple Card account.
5. Optional: Select **Import Memos**.

   The memo has the description from Wallet, the text from your card statement and the foreign amount.

6. Import the transactions.

If you import a file again, YNAB does not import the transactions that have the same date and amount as imported transactions.

> **Note:** On an iPad, you can drag the file from Files into YNAB in Safari. For the steps, refer to the [YNAB Help Center page for file import](https://support.ynab.com/en_us/file-based-import-a-guide-Bkj4Sszyo).

YNAB does not keep the file, but it keeps the transactions that you import. The terms of YNAB are applicable to these transactions.

## Use a CSV file

YNAB also imports CSV files. The OFX file has only posted transactions. A CSV file from WalletFeed has all transactions, with `pending` in the Status column for a pending transaction.

WalletFeed Pro is not necessary for **Export CSV**. To make a CSV file one time:

1. On your iPhone, open WalletFeed.
2. At the top of the screen, tap **Settings**.
3. In **Data**, tap **Export CSV**.

   ![The Settings screen shows Export CSV in the Data section.](app:docs-settings-3)

4. Tap **Range**, then select a range, for example **Last Month**.

   ![The Export CSV screen shows the range This Month and 29 transactions.](app:docs-export-csv)

5. Tap **Export**.
6. Tap **Save to Files**, then save the file in iCloud Drive.

The file has the transactions of all the Wallet accounts that WalletFeed reads. YNAB puts all of them in the account that you select. With WalletFeed Pro, a CSV File destination updates a file when your transactions change. It can have a filter for one account. For the steps, refer to the [guide for a CSV file](/guides/apple-card-to-csv/).

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
4. Make sure that each YNAB field uses the column in the table.

   The CSV file has one Amount column. A purchase is a negative amount. The YNAB Help Center tells you to select **Amount** for **Outflow** and for **Inflow**.

5. Import the transactions.

## The data that YNAB receives

The OFX file has this information for each posted transaction:

| Wallet data | In the OFX file | In YNAB |
| --- | --- | --- |
| Merchant | The name of the merchant, with a maximum of 32 characters | **Payee** |
| Amount | A purchase is negative. A payment or a refund is more than zero. | **Outflow** or **Inflow** |
| Date and Posted Date | The date of the transaction and the date that it posted | **Date** |
| Description, Original Description and Foreign Amount | The memo of the transaction | **Memo**, if you select **Import Memos** |
| Account | One statement for each Wallet account | The YNAB account that you select |

The OFX file has no category. YNAB says that it changes the payee names from a file. It also gives each transaction the category that its payee usually has. You can change the payee and the category of each transaction in YNAB.

## Changes to the files

While WalletFeed is open, its files in iCloud Drive receive changes in seconds. When WalletFeed is closed, iOS starts WalletFeed in approximately 1 hour or less after a change in Wallet. For this, [Background Sync](/docs/background-sync/) must be on in **Settings** › **Sync**.

If WalletFeed cannot open the folder at that time, the files get the changes when one of these occurs:

- You open WalletFeed.
- A Shortcuts automation starts WalletFeed.
- iOS starts WalletFeed while your iPhone charges.

WalletFeed writes the file for a month again each time that a transaction in that month changes. YNAB gets the changes only when you import the file again.

- A pending transaction is not in the file. When it posts, WalletFeed adds it to the file for its month.
- A refund is a new transaction with an amount that is more than zero.
- If Wallet removes a transaction, WalletFeed removes it from the file. If you imported it before, delete it in YNAB.

## Send previous transactions

A new OFX File destination also receives previous posted transactions, from the start date in **Settings** › **Sync** › **Initial History**. **Initial History** is **All** until you change it.

The YNAB Help Center tells you not to import transactions that are more than 1 year old. If a file has transactions from before the start date of your YNAB account, YNAB lets you include them or not.

To write the previous transactions to the files again:

1. On your iPhone, open WalletFeed.
2. Tap **Destinations**, then tap the destination, for example **WalletFeed**.
3. Tap **Send History**.
4. Select **30 Days**, **90 Days**, **1 Year** or **All**.

WalletFeed writes the file for each month in that period again. For more information, refer to [Send History](/docs/send-history/).

## Change or remove the destination

To change the destination, tap it in [**Destinations**](/docs/destinations/). These are the changes that you can make:

- Set **Filter** to on, and select the accounts, the categories or a minimum amount. For more information, refer to [Choose what to send](/docs/choose-what-to-send/).
- Tap **Change Folder** to use a different folder. WalletFeed writes all your transactions to new files in that folder.
- Set **Enabled** to off to stop the changes to the files for a time.
- Type a different name in **Name**. The names of the files stay the same.

To remove the destination:

1. In **Destinations**, tap the destination.
2. Tap **Delete**.
3. In the message, tap **Delete** again.

The files stay in iCloud Drive. The transactions that you imported stay in YNAB.

## If there is a problem

### If YNAB puts Apple Cash transactions in your Apple Card account

The file has the transactions of more than one Wallet account.

1. In WalletFeed, set a filter for your Apple Card account, as in step 2.
2. In YNAB, delete the transactions that are not from your Apple Card.

### If YNAB does not import some transactions

YNAB does not import a transaction that it imported before, or that you deleted in YNAB after an import.

1. In **Import Transactions**, look at the transactions above **Options**.

   YNAB shows why it did not import each transaction.

2. If you deleted the transactions in YNAB, type them in YNAB.

### If a pending transaction is not in the file

The OFX file has a transaction only after it posts.

1. After the transaction posts, import the file for its month again.

### If the destination shows "Can't open the folder. Choose it again."

WalletFeed cannot open the folder that you selected.

1. In **Destinations**, tap the destination.
2. Tap **Change Folder**.
3. Select the folder again.

WalletFeed writes your transactions to the files again.

### If the files on your computer do not show new transactions

WalletFeed did not update the files after the last change in Wallet.

1. On your iPhone, open WalletFeed.
2. At the top of the screen, tap **Settings**.
3. In **Sync**, tap **Sync Now**.

**Sync Now** shows the time of the last sync.

### If Destinations shows "Sync Requires Pro"

You do not have WalletFeed Pro at this time. WalletFeed keeps the destination, but it does not update the files.

1. In **Destinations**, tap **Upgrade**.
2. Start the free trial, or get a plan.
