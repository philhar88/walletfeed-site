# Upload Apple Card transactions to QuickBooks Online

You can put your Apple Card transactions in QuickBooks Online with a file that you upload. WalletFeed saves your Apple Card, Apple Cash and Savings transactions from your iPhone in one OFX file for each month, and you upload each file in QuickBooks Online.

> **Note:** This guide is for QuickBooks Online. For bank transactions from a file, QuickBooks Desktop uses Web Connect. Intuit tells you that Web Connect reads only QBO files. WalletFeed does not write QBO files.

## Before you start

You must have these items:

- An iPhone with iOS 26 or a newer version
- WalletFeed, with [access to your Apple Card](/docs/wallet-accounts/)
- [WalletFeed Pro](/docs/walletfeed-pro/) for the OFX files (a subscription with a 1-week free trial, or a one-time Lifetime purchase)
- QuickBooks Online in a web browser on a computer
- A folder that your iPhone and your computer can open, for example in iCloud Drive.

WalletFeed is available only in the US. WalletFeed Pro is not necessary for [Export CSV](/docs/export-csv/), which makes one CSV file (refer to [Use a CSV file](#use-a-csv-file)).

## Files that QuickBooks Online can upload

Intuit gives these rules in [Manually upload transactions into QuickBooks Online](https://quickbooks.intuit.com/learn-support/en-us/help-article/import-transactions/manually-upload-transactions-quickbooks-online/L0rE9OXBz_US_en_US) (updated August 24, 2026):

- QuickBooks Online can upload a list of transactions from a CSV, TXT, QBO, QFX or OFX file.
- The file must be in English and 350 KB or less.
- One upload has 1,000 transactions at most.
- A CSV file must have 3 columns (Date, Description and Amount) or 4 columns (Date, Description, Credit and Debit).

## Select a file

For QuickBooks Online, use the OFX files from WalletFeed. Intuit gives OFX as a file type that QuickBooks Online can upload. This table shows the differences between the OFX files and the CSV files:

| | OFX file | CSV file |
| --- | --- | --- |
| Changes before you upload the file | None | You make a copy with only 3 columns. |
| Pending transactions | Not in the file. A charge goes into the file after it posts. | In the file |
| Transaction ID | Each transaction has an ID. The ID stays the same each time that WalletFeed writes the file. | In the **WalletFeed ID** column, which you delete in the copy |
| WalletFeed Pro | Necessary | Not necessary for **Export CSV** |

## Step 1: Add an OFX file in WalletFeed

1. On your iPhone, open WalletFeed.
2. Tap **Destinations**.
3. Tap **+** at the top of the screen.

   ![The Destinations screen with no destinations and the + button at the top.](https://walletfeed.app/guides/apple-card-to-quickbooks/walletfeed-destinations-empty-pro.webp)

4. In the **Destinations** search field, type `OFX`.
5. Tap **OFX File**.

   If you do not have WalletFeed Pro, the **WalletFeed Pro** screen opens. After you get WalletFeed Pro, the **Files** screen opens.

6. Make sure that **Format** is **OFX**.

   ![The Files screen with OFX in Format, Choose… in Folder and WalletFeed in Name.](https://walletfeed.app/guides/apple-card-to-quickbooks/walletfeed-setup-ofx-file.webp)

7. Tap **Folder**.
8. Select a folder in iCloud Drive.

   **Folder** then shows the name of the folder.

9. To use a different name for the files, type the name in **Name**.

   Each file name contains this name, the month and `.ofx`. For example, the file for October 2026 is `WalletFeed 2026-10.ofx`.

10. Tap **Add**.
11. When WalletFeed shows **Save Transactions to Files?**, tap **Save**.

    The message tells you the data that the folder receives from each posted transaction. It also gives the accounts and the period. If you tap **Cancel**, WalletFeed removes the new destination.

WalletFeed then writes one file for each month that has posted transactions.

## Step 2: Keep only Apple Card transactions in the files

One OFX file has the transactions of each Wallet account that WalletFeed reads. In QuickBooks Online, you upload a file into one account. If WalletFeed reads only your Apple Card account, this step is not necessary.

1. In **Destinations**, tap the destination, for example **WalletFeed**.
2. Set the **Filter** switch to on.
3. Tap **Accounts**.
4. Select your Apple Card account.
5. Tap the back button at the top of the screen.
6. Tap **Send History**.
7. Tap **All**.

   WalletFeed then writes the files again with only your Apple Card transactions.

## Step 3: Upload a file in QuickBooks Online

Intuit gives these steps in [Manually upload transactions into QuickBooks Online](https://quickbooks.intuit.com/learn-support/en-us/help-article/import-transactions/manually-upload-transactions-quickbooks-online/L0rE9OXBz_US_en_US). The labels are from August 24, 2026.

1. On your computer, open QuickBooks Online in a web browser.
2. Click **All apps** › **Accounting** › **Bank transactions**.
3. If QuickBooks shows a tile for your Apple Card account, click the tile.
4. Click **Link account**.

   If your account in QuickBooks has no connection to online banking, click **Upload from file** or **Or upload transactions manually**. Then go to step 6.

5. Click **Upload from file**.
6. Click **Drag and drop or select files**.
7. In the folder from Step 1, select the file for a month, for example `WalletFeed 2026-10.ofx`.
8. Click **Continue**.
9. In **QuickBooks account**, select the credit card account for your Apple Card.

   If you do not have this account, select **Add New**. The OFX file gives your Apple Card as a credit card account.

10. Click **Continue**.
11. If QuickBooks shows the columns of the file, select the QuickBooks field for each column.
12. Click **Continue**.
13. Select the transactions to upload.
14. Click **Continue**.
15. Click **Yes**.
16. Click **Done**.

After the upload, Intuit tells you to match and categorize the transactions in **Bank transactions**.

> **Note:** Wallet can also make an export file of a monthly statement, or of a period between two dates. [Make an export file of your Apple Card transactions](/guides/export-apple-card-transactions/) gives the steps.

## Data in the OFX file

| Data in the file | From Wallet |
| --- | --- |
| Name | The merchant name, or the description if Wallet has no merchant name. The file keeps the first 32 characters. |
| Amount | The value of the transaction, for example -23.40. Purchases have a minus sign. Payments and refunds have no minus sign. |
| Posted date | The date when the transaction posted. |
| Transaction date | The date of the transaction in Wallet. |
| Memo | The description and the card statement text, if they are different from the name. A value in a different currency is also in the memo. |
| Transaction ID | The ID of the transaction in Wallet. |
| Account | A statement for each Wallet account. Apple Card is a credit card account. |

The file does not include the WalletFeed category or the balance of the account.

## Changes to the files

While WalletFeed is open, the files receive changes in seconds. When WalletFeed is not open, iOS starts WalletFeed approximately 1 hour or less after a change in Wallet. If [Background Sync](/docs/background-sync/) is on in **Settings** › **Sync**, WalletFeed then updates the files.

If **Background Sync** is off, or if WalletFeed cannot open the folder at that time, the files change at these times:

- When you open WalletFeed
- When an [automation](/docs/siri-and-shortcuts/#send-transactions-with-an-automation) starts
- While your iPhone is on a charger, at a time that iOS selects.

WalletFeed puts each transaction in the file for the month of the transaction date. After a pending charge posts, WalletFeed adds it to the file for its month. Thus, a file can change after the end of its month. WalletFeed does not write declined charges to the files.

QuickBooks Online gets the changes only when you upload a file again. Intuit tells you to upload files that start after the newest transaction in QuickBooks (refer to [Fix duplicate transactions in QuickBooks Online bank feeds](https://quickbooks.intuit.com/learn-support/en-us/help-article/duplicate-transactions/fix-duplicate-transactions-quickbooks-online-bank-feeds/L1fjxl88f_US_en_US)). If a file has transactions that are in QuickBooks, QuickBooks can show a transaction two times.

To upload a file for a month again:

1. Do steps 1 to 12 in [Step 3](#step-3-upload-a-file-in-quickbooks-online).
2. Select only the transactions that are not in QuickBooks.
3. Do steps 14 to 16 in Step 3.

## Send previous transactions

A new OFX File destination also receives previous transactions from the start date in **Settings** › **Sync** › **Initial History**. **Initial History** is **All** until you change it. With [Send History](/docs/send-history/), WalletFeed writes the files again for a period that you select.

1. In WalletFeed, tap **Destinations**.
2. Tap the destination, for example **WalletFeed**.
3. Tap **Send History**.
4. Tap **30 Days**, **90 Days**, **1 Year** or **All**.

   WalletFeed then writes the file for each month in that period. For the first month, the file has only the transactions from the start of the period.

5. In QuickBooks Online, upload only the files of the months that are not in QuickBooks.

## Use a CSV file

**Export CSV** in WalletFeed makes one CSV file. WalletFeed Pro is not necessary for **Export CSV**. The file has 16 columns, and it also has pending transactions. Thus, you must change a copy of the file before you upload it.

1. On your iPhone, open WalletFeed.
2. Tap **Settings** (the gear button) at the top of the screen.
3. In the **Data** section, tap **Export CSV**.

   ![The Settings screen with Export CSV in the Data section.](https://walletfeed.app/guides/apple-card-to-quickbooks/walletfeed-settings-3.webp)

4. Tap **Range**.
5. Select a period, for example **Last Month**.

   ![The Export CSV screen with Range set to This Month, 29 transactions and the Export button.](https://walletfeed.app/guides/apple-card-to-quickbooks/walletfeed-export-csv.webp)

6. Tap **Export**.
7. Tap **Save to Files**.
8. Select a folder in iCloud Drive.
9. Tap **Save**.
10. On your computer, make a copy of the file.
11. Open the copy in a spreadsheet app.
12. Delete each row with a **Status** that is not `booked`.

    `booked` is the status of a posted transaction.

13. Delete each row with an **Account** that is not Apple Card.
14. Delete all the columns except **Date**, **Merchant** and **Amount**.
15. Change the name of the **Merchant** column to `Description`.
16. Save the copy as a CSV file.
17. To upload the copy, do steps 1 to 10 in [Step 3](#step-3-upload-a-file-in-quickbooks-online).
18. When QuickBooks shows the columns, select **Date**, **Description** and **Amount** for the columns with these names.
19. Make sure that the date format in QuickBooks agrees with the dates in the file, for example 2026-10-28.
20. Do steps 12 to 16 in Step 3.

In the **Amount** column, a purchase has a minus sign. A payment or a refund has no minus sign.

With WalletFeed Pro, a [CSV File destination](/guides/apple-card-to-csv/) updates a CSV file when your transactions change. Before each upload, you must then make the same changes in a copy of the file.

For the CSV formats, refer to [Format CSV files in Excel to get bank transactions into QuickBooks](https://quickbooks.intuit.com/learn-support/en-us/help-article/bank-transactions/format-csv-files-excel-bank-transactions-quickbooks/L4BjLWckq_US_en_US).

## Change or remove the destination

1. In WalletFeed, tap **Destinations**.
2. Tap the destination, for example **WalletFeed**.
3. Make one of the changes in this table.

| Change | On the destination screen |
| --- | --- |
| Send only some transactions | Set **Filter** to on. Then set **Include**, **Minimum**, **Accounts**, **Categories** or **Exclude**. |
| Use a different folder | Tap **Change Folder**. Then select the folder. |
| Stop the changes to the files for a time | Set **Enabled** to off. |
| Remove the destination | Tap **Delete**. Then tap **Delete** again. |

When you remove the destination, the files stay in the folder. WalletFeed does not change the transactions in QuickBooks.

## If there is a problem

### If the folder has no OFX file

WalletFeed writes a file only for a month that has posted transactions.

1. In WalletFeed, tap **Destinations**.
2. Tap the destination.
3. Tap **Send Test**.

   The folder then gets `WalletFeed Test.ofx` with a sample transaction. If this file is in the folder, WalletFeed can write files in the folder.

4. Do not upload `WalletFeed Test.ofx` into QuickBooks.

### If QuickBooks shows "The uploaded file is of a different type than these accounts."

The account that you selected has a different type from the account in the file. For example, the file has an Apple Card credit card account, and you selected a checking account.

1. Click **Cancel**.
2. Select the credit card account for your Apple Card.
3. If the file also has Apple Cash or Savings transactions, do [Step 2](#step-2-keep-only-apple-card-transactions-in-the-files).

### If QuickBooks shows a transaction two times

You uploaded a transaction that was in QuickBooks. Intuit gives these steps in [Exclude duplicate transactions in QuickBooks Online](https://quickbooks.intuit.com/learn-support/en-us/help-article/bank-transactions/exclude-duplicate-transactions-quickbooks-online/L8jyr7WpC_US_en_US):

1. Click **All apps** › **Accounting** › **Bank transactions**.
2. In the **For review** tab, select the checkbox for each copy.
3. Click **Exclude**.

   QuickBooks moves the transactions to the **Excluded** tab.

If the copy is not in **For review**, refer to [Fix duplicate transactions in QuickBooks Online bank feeds](https://quickbooks.intuit.com/learn-support/en-us/help-article/duplicate-transactions/fix-duplicate-transactions-quickbooks-online-bank-feeds/L1fjxl88f_US_en_US).

### If a pending charge is not in QuickBooks

An OFX file has only posted transactions.

1. After the charge posts in Wallet, upload the file for that month again.
2. Select only the new transaction (refer to [Changes to the files](#changes-to-the-files)).

### If QuickBooks shows an error message for a CSV file

Intuit gives these corrections in [Format CSV files in Excel to get bank transactions into QuickBooks](https://quickbooks.intuit.com/learn-support/en-us/help-article/bank-transactions/format-csv-files-excel-bank-transactions-quickbooks/L4BjLWckq_US_en_US):

1. In the copy, change the dates in the **Date** column to the dd/mm/yyyy format.

   Intuit recommends this format.

2. Delete the numbers in the cells of the **Description** column.
3. If you use a Mac, save the copy as a Windows CSV file.
4. Upload the copy again.

### If QuickBooks does not upload the OFX file

1. Make sure that the file is 350 KB or less.
2. Make sure that you selected a credit card account in **QuickBooks account**.
3. If QuickBooks does not upload the file, use a CSV file (refer to [Use a CSV file](#use-a-csv-file)).

### If the destination shows "Can't open the folder. Choose it again."

WalletFeed cannot open the folder that the destination uses.

1. In **Destinations**, tap the destination.
2. Tap **Change Folder**.
3. Select the folder again.

### If Destinations shows "Sync Requires Pro"

You do not have WalletFeed Pro at this time. WalletFeed keeps the destination, but it does not write the files.

1. In **Destinations**, tap **Upgrade**.
2. Get a plan, or tap **Restore Purchases**.
