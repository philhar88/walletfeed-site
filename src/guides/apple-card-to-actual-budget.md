+++
title = "Import Apple Card transactions into Actual Budget"
nav_title = "Actual Budget"
seo_title = "Apple Card to Actual Budget: import a monthly OFX file"
description = "Import Apple Card transactions into Actual Budget. WalletFeed saves them from your iPhone to an OFX file each month, and you import the file on a computer."
group = "Files and desktop apps"
order = 50
related = ["guides/apple-card-to-ofx", "guides/apple-card-to-firefly-iii"]
updated = 2026-10-30
+++

To import Apple Card transactions into Actual Budget, WalletFeed saves them from your iPhone to iCloud Drive as one OFX file for each month. Then, on a computer, you import the file into an Apple Card account in Actual Budget.

## Before you start

- An iPhone with iOS 26 or a newer version. WalletFeed is available only in the US.
- Apple Card in Wallet on that iPhone, and WalletFeed with [access to your Wallet accounts](/docs/wallet-accounts/).
- [WalletFeed Pro](/docs/walletfeed-pro/), which is necessary for destinations. WalletFeed Pro is a subscription with a 1-week free trial, or a one-time Lifetime purchase.
- iCloud Drive on your iPhone.
- A computer with access to your iCloud Drive. On a Mac, iCloud Drive is in Finder. On Windows, you can use iCloud for Windows or iCloud.com.
- Actual Budget, open in a web browser on that computer.

Actual Budget does not show the **Import** button on a phone screen. Thus, you import the files on a computer.

## Step 1: Add an OFX file in WalletFeed

1. On your iPhone, open WalletFeed.
2. Tap **Destinations**.
3. Tap **+** at the top of the screen.

   ![The Destinations screen with no destinations and the + button at the top.](app:docs-destinations-empty-pro)

4. In the **Destinations** search field, type `Actual`.

   ![The Add Destination screen with the Destinations search field above the Budgeting list.](app:08-add-destination)

5. Tap **OFX File**.

   If you do not have WalletFeed Pro, the **WalletFeed Pro** screen opens. After you get WalletFeed Pro, the **Files** screen opens.

6. Make sure that **Format** is **OFX**.

   ![The Files screen with Format set to OFX, the Folder row, the name WalletFeed and three steps.](app:docs-setup-ofx-file)

   Do not use **QIF** for Actual Budget. A QIF file has no transaction IDs. If you import a QIF file two times, Actual Budget adds each transaction two times.

7. Tap **Folder**.
8. Select a folder in iCloud Drive.

   The name of the folder shows next to **Folder**. You open this folder on your computer in Step 3.

9. To use a different name for the files, type it in **Name**.

   Each month has one file. The files get names such as `WalletFeed 2026-10.ofx`.

10. Tap **Add**.
11. When WalletFeed shows **Save Transactions to Files?**, tap **Save**.

    The message tells you which data the folder receives, from which accounts and from which date. If you tap **Cancel**, WalletFeed removes the new destination.

WalletFeed adds the destination to **Destinations** with the name **WalletFeed**, or the name that you typed. Then it writes a file for each month that has posted transactions.

If WalletFeed has access to Apple Cash or Savings, the files also contain their transactions. To write only Apple Card transactions, refer to [Change or remove the destination](#change-or-remove-the-destination).

## Step 2: Make an Apple Card account in Actual Budget

You do this step one time.

1. On your computer, open Actual Budget in a web browser.
2. If Actual Budget shows **Sign in to this Actual instance**, sign in with the password of your server.
3. If Actual Budget shows **Welcome to Actual**, click **Start budgeting**.

   ![The Actual Budget welcome page with the Start budgeting button.](web:actual-budget/03-start-budgeting)

   Actual Budget makes a budget with the name **My Finances**. Do not click **Import my budget**, because that link is not for OFX files.

4. At the bottom of the sidebar, click **Add account**.

   ![The Actual Budget sidebar with the Add account button at the bottom.](web:actual-budget/07-add-account)

5. Click **Create a local account**.

   ![The Add account dialog with the Create a local account button.](web:actual-budget/08-create-local-account)

6. In **Name:**, type `Apple Card`.
7. Make sure that **Off budget** is clear.

   You cannot change **Off budget** after you make the account.

8. Make sure that **Balance:** is `0`.
9. Click **Create**.

   ![The Create Local Account dialog with the name Apple Card, a clear Off budget box, a balance of 0 and the Create button.](web:actual-budget/09-account-name-apple-card)

Actual Budget opens the **Apple Card** account page. The sidebar shows **Apple Card** below **On budget**.

## Step 3: Import the file in Actual Budget

Do these steps each time that you want the new transactions in Actual Budget.

> **Note:** On a phone screen, Actual Budget does not show **Import**.

1. On your computer, in the Actual Budget sidebar, click **Apple Card**.

   Actual Budget puts all the transactions from the file into the account that is open.

2. Click **Import**.

   ![The Apple Card account page in Actual Budget with the Import button above the empty list of transactions.](web:actual-budget/10-account-import-button)

3. In the window that your browser opens, go to the folder in iCloud Drive that you selected in Step 1.
4. Open the file of the month, such as `WalletFeed 2026-10.ofx`.

   You can open only one file at a time. Do not open `WalletFeed Test.ofx`, because it has only a sample transaction.

5. In **Import transactions (OFX)**, make sure that each new transaction has a blue **+** icon.
6. Click **Import 6 transactions**.

   ![The Import transactions (OFX) window with six new Apple Card transactions and the Import 6 transactions button.](web:actual-budget/11-import-preview)

   The number in the button is the number of new transactions. It is not necessary to change the check boxes below the list.

7. Make sure that the transactions show on the **Apple Card** page.

   ![The Apple Card account in Actual Budget with six imported transactions in the Payment and Deposit columns.](web:actual-budget/12-imported-transactions)

   At the top of the page, Actual Budget shows the number of transactions without a category, such as **6 uncategorized transactions**.

## Import the same month again

WalletFeed updates the file of the month when your transactions change. You can import the file again at any time, also before the end of the month. Actual Budget uses the ID of each transaction to find the transactions that you imported before. It adds only the new transactions.

1. In the Actual Budget sidebar, click **Apple Card**.
2. Click **Import**.
3. Open the file of the month again, such as `WalletFeed 2026-10.ofx`.
4. Make sure that only the new transactions have a blue **+** icon.

   ![The Import transactions (OFX) window with one new transaction, Shell, and six dim rows that Actual Budget has from before.](web:actual-budget/14-reimport-updated-month)

   The transactions that you imported before show as dim rows with a clear check box.

5. Click the import button, such as **Import 1 transactions**.

   ![The Apple Card account in Actual Budget with seven different transactions.](web:actual-budget/15-after-second-import)

A transaction goes into the file of the month of the purchase. A purchase at the end of a month can post in the next month. WalletFeed then adds it to the file of the month of the purchase. Thus, import the file of each month again some days after the end of the month.

## Data that Actual Budget receives

Each OFX file has the posted transactions of one month. This table shows the column in Actual Budget for each Wallet field.

| Wallet | Actual Budget |
| --- | --- |
| Posted date | **Date**. This date can be one day after the date of the purchase in Wallet. |
| Merchant, or the description if Wallet has no merchant | **Payee**, with 32 characters at most |
| Description, card statement text and the value in a foreign currency | **Notes** |
| A purchase or a fee | **Payment**, without a minus sign |
| A refund, a payment or a deposit | **Deposit** |
| Transaction ID | Not shown. Actual Budget uses it to find the transactions that you imported before. |
| Category | Not in the file. **Category** shows **Categorize**. |

Purchases make the balance of the **Apple Card** account less than zero, such as -549.61.

When Actual Budget adds a new payee, it can change the letters of the name. For example, NETFLIX.COM 866-579 becomes Netflix.Com 866-579.

If **Notes** shows the same text as **Payee**, you can clear **Import notes from file** in the import window. Then **Notes** stays empty. Actual Budget then does not import the card statement text or the foreign value.

If WalletFeed has access to more than one Wallet account, each file has the transactions of all these accounts. Actual Budget puts all of them into the account that is open.

WalletFeed writes the files only to the folder that you select. WalletFeed has no account and no WalletFeed servers.

## Changes to the files

While WalletFeed is open, the file of the month receives changes in seconds. When WalletFeed is closed, iOS starts WalletFeed in approximately 1 hour or less after a change in Wallet. For this, [Background Sync](/docs/background-sync/) must be on in **Settings** › **Sync**. If WalletFeed cannot open the folder at that time, the file changes the next time that you open WalletFeed, or while your iPhone charges.

Actual Budget gets the changes only when you import the file again.

WalletFeed writes only posted transactions to an OFX file. A pending charge goes into the file after it posts, with the same ID. A declined charge does not post, so it is not in the file. A refund is a different transaction, in **Deposit**.

If Wallet deletes a transaction, WalletFeed removes it from the file. If you imported the transaction before, delete it in Actual Budget.

## Send previous transactions

A new destination also receives previous transactions, from the start date in **Settings** › **Sync** › **Initial History**. **Initial History** is **All** until you change it. WalletFeed then writes a file for each month with posted transactions. You can import only the months that you want.

To change **Initial History**, do these steps before you add the destination:

1. In WalletFeed, tap **Settings** (the gear button) at the top of the screen.
2. In **Sync**, tap **Initial History**, then select **Today**, **30 Days**, **90 Days**, **1 Year** or **All**.

   ![Settings, with Initial History set to All in the Sync section.](app:docs-settings)

To write the files of previous months again, use [Send History](/docs/send-history/):

1. In **Destinations**, tap your OFX destination, such as **WalletFeed**.
2. Tap **Send History**, then select **30 Days**, **90 Days**, **1 Year** or **All**.

WalletFeed writes the file of each month in that period again. When you import a file again, Actual Budget adds only the transactions that it does not have.

## Change or remove the destination

In **Destinations**, tap your OFX destination. Then use this table:

| Change | On the destination screen |
| --- | --- |
| Stop the changes to the files for a time | Set **Enabled** to off. |
| Write only Apple Card transactions | Set **Filter** to on, then select Apple Card in **Accounts**. Then tap **Send History** › **All**. |
| Write only some transactions | Set **Filter** to on. Then set **Include**, **Minimum**, **Accounts**, **Categories** or **Exclude**. |
| Use a different folder | Tap **Change Folder**, then select the folder. WalletFeed then writes all the files again in the new folder. |
| Make sure that WalletFeed can write to the folder | Tap **Send Test**. The folder gets `WalletFeed Test.ofx` with a sample transaction. Do not import this file. |
| Remove the destination | Tap **Delete**, then tap **Delete** again. The files stay in the folder, and the transactions stay in Actual Budget. |

To import Apple Cash or Savings into a different account in Actual Budget, add one more **OFX File** destination with a different **Name**. Then set its filter to that Wallet account.

For more information about the filter, refer to [Choose what a destination receives](/docs/choose-what-to-send/).

## If there is a problem

### If Actual Budget does not show Import

**Import** shows only on the page of an account, and not on a phone screen.

1. Open Actual Budget in a web browser on a computer.
2. In the sidebar, click **Apple Card**.

### If the button shows “Import 0 transactions”

Actual Budget has all the transactions in the file. This is not an error.

1. Click **×** to close the window.

   ![When you import the same file again, Actual Budget shows all the rows as dim, and you cannot click Import 0 transactions.](web:actual-budget/13-reimport-same-file)

### If a transaction that you deleted in Actual Budget shows again

Actual Budget selects **Reimport deleted transactions** if you do not change it. Thus, it shows deleted transactions as new when you import a month again.

1. In **Import transactions (OFX)**, clear **Reimport deleted transactions**.

   ![With Reimport deleted transactions clear, the deleted Nopa transaction is dim and the button shows Import 0 transactions.](web:actual-budget/17-reimport-deleted-off)

   You can also clear the check box of the deleted transaction.

2. Click the import button. If it shows **Import 0 transactions**, click **×**.

### If Apple Cash or Savings transactions are in the Apple Card account

The file has the transactions of all the Wallet accounts that the destination receives, and Actual Budget puts them into the open account.

1. In WalletFeed, tap **Destinations**.
2. Tap your OFX destination, such as **WalletFeed**.
3. Set **Filter** to on.
4. Tap **Accounts**, then select Apple Card.
5. On the destination screen, tap **Send History**, then tap **All**.
6. In Actual Budget, delete the transactions that are not from Apple Card.

### If the dates are one day after the dates in Wallet

Actual Budget shows the date that the charge posted, and Wallet shows the date of the purchase. This is not an error.

### If a pending charge is not in Actual Budget

WalletFeed writes a charge to the file only after it posts.

1. After the charge posts in Wallet, import the file of the month again.

### If the folder has no file for a month

WalletFeed writes a file only for a month that has posted transactions.

1. In WalletFeed, open the destination.
2. Tap **Send Test**.

   The folder then gets `WalletFeed Test.ofx`. If this file is in the folder, WalletFeed can write there.

3. To write the files of all months, tap **Send History**, then tap **All**.

### If WalletFeed shows “Couldn't open this folder.”

WalletFeed cannot get access to the folder that you selected on the **Files** screen.

1. Tap **Folder**.
2. Select a different folder in iCloud Drive.

### If the destination shows “Can't open the folder. Choose it again.”

WalletFeed does not have access to the folder of the destination.

1. In WalletFeed, tap **Destinations**.
2. Tap the destination.
3. Tap **Change Folder**.
4. Select the folder again.
