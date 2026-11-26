+++
title = "Connect Apple Card to Monarch"
nav_title = "Monarch"
seo_title = "Connect Apple Card to Monarch: steps, limits and checks"
description = "Monarch can connect to Apple Card, Apple Cash and Savings in its iPhone app. The steps, the limits, and what to do if Apple Card does not sync in Monarch."
group = "Budgeting apps"
order = 86
related = ["guides/apple-card-plaid", "guides/apple-card-budget-apps", "guides/apple-card-rocket-money", "guides/apple-card-copilot", "guides/export-apple-card-transactions"]
updated = 2026-11-26
+++

Monarch connects to your Apple Card, Apple Cash and Savings accounts in its app for iPhone. You cannot connect these accounts on the Monarch website. But you can import a CSV file there.

The steps on this page come from three pages of the Monarch help center:

- [Syncing Your Apple Card, Cash, and Savings](https://help.monarch.com/hc/en-us/articles/24178098173076-Syncing-Your-Apple-Card-Cash-and-Savings)
- [Troubleshooting Your Apple Card Accounts](https://help.monarch.com/hc/en-us/articles/25195805450772-Troubleshooting-your-Apple-Card-accounts)
- [Importing Transactions Manually](https://help.monarch.com/hc/en-us/articles/4409682789908-Importing-Transactions-Manually).

## Before you start

You must have these items:

- An iPhone with the newest iOS version
- The newest version of the Monarch app
- Your Apple Card, Apple Cash or Savings account in Wallet on that iPhone.

## Step 1: Prepare your iPhone

Monarch updates your Apple Card in the background only with these two settings.

1. On your iPhone, open **Settings**.
2. Tap **General** › **Background App Refresh**.
3. Find **Monarch**, then set its switch to on.
4. Go back to the first screen of **Settings**.
5. Tap **Monarch**, or **Apps** › **Monarch**.
6. Tap **Notifications**.
7. Set **Allow Notifications** to on.

Monarch tells you that, without **Allow Notifications**, your Apple Card gets updates only while the app is open. In the Monarch app, you can select the types of notification that you get.

## Step 2: Connect your Apple Card in Monarch

1. On your iPhone, open Monarch.
2. Tap the **Accounts** tab.
3. Tap **+ Add account** at the top right.
4. In the search field, type `Apple Card`.
5. Tap **Apple Card, Cash, and Savings**.
6. Do the steps on the screen to give access.
7. Select your accounts.
8. Select the date from which Monarch gets your transactions.
9. Stay in the app until Monarch completes the first update.

Result: Monarch updates your Apple Card in the background.

## Limits of the connection

Monarch gives these limits:

- You can connect Apple Card only in the Monarch app on an iPhone.
- Each Monarch login has one Apple connection. Each person in your household can add a connection with a different login.
- Monarch gets the data of an Apple account only from the iPhone that gave the access.
- The connection brings only the transactions of the person who gave the access.
- When you first connect, Monarch gets all available transaction data one time. After that, each update gets only the transactions from the last two weeks.

The background updates stop when you remove Monarch from the App Switcher. They start again when you open Monarch.

The balance in Monarch can be different from the balance in Wallet. Apple gives Monarch your **Total Balance**. This balance does not include pending transactions. It includes Apple Card Monthly Installments.

## If Apple Card does not get updates in Monarch

Do not delete the Apple account that you have in Monarch. Monarch tells you to connect the same accounts again, and not to add a second set of accounts.

### If Monarch shows "Some settings need updating"

After 7 days or more with no update, the account page on your iPhone can show a **Connection issue** banner.

1. Tap **Update**.

   Result: Monarch opens **Reconnect Apple accounts**, which shows the settings that you must change.

2. If Monarch shows **Connect Apple Wallet** or **Allow account access**, tap **Open settings**.
3. Tap **Wallet**.
4. Select **All Available Activity** for each account that you want in Monarch.
5. If Monarch shows **Allow notifications**, tap **Allow access** or **Open settings**.
6. If Monarch shows **Allow background app refresh**, tap **Open settings**.
7. Set **Background App Refresh** to on for Monarch.

Result: Each row shows **Permission granted**. The Wallet row shows **Apple account connected**.

### If Monarch shows no banner

1. On your iPhone, open **Settings** › **Apps** › **Monarch** › **Wallet**.

   On iOS 18 or an earlier version, open **Settings** › **Privacy & Security** › **Wallet** › **Monarch**.

2. Make sure that each account that you want in Monarch shows **All Available Activity**.
3. In Monarch, tap **+ Add account**.
4. Do the **Apple Card, Cash, and Savings** steps again.

Monarch tells you that these steps connect your Apple Card again. Your transactions stay in Monarch.

If your Apple Card gets no updates after these steps, refer to "If you already have an Apple Card connected" in the first help page.

### If you have a new iPhone

Monarch gets each Apple account from one iPhone. Thus, you must add the accounts again on a new iPhone.

1. On the new iPhone, open **Settings** › **Apps** › **Monarch** › **Wallet**.

   On iOS 18 or an earlier version, open **Settings** › **Privacy & Security** › **Wallet**.

2. If **Settings** does not show Monarch, do [Step 2](#step-2-connect-your-apple-card-in-monarch) on the new iPhone.
3. Select **All Available Activity** for each account.
4. Open Monarch.
5. Refresh your accounts.
6. If you continue to use the first iPhone, remove the Wallet access of Monarch on that iPhone.

Monarch keeps your transactions, categories and notes.

### If Monarch shows a transaction two times

After you add your Apple accounts again, Monarch finds the transactions that it has. Monarch tells you that some transactions can come two times. You can delete the second copy of a transaction.

### More steps from Monarch

The [Monarch page for problems](https://help.monarch.com/hc/en-us/articles/25195805450772-Troubleshooting-your-Apple-Card-accounts) has more steps. For example, it tells you to delete the Monarch app and install it again.

## Import a CSV file on the Monarch website

If the connection does not bring some transactions into Monarch, you can import a CSV file. Monarch can import a file only on its website, not in its app.

> **Caution:** Make sure that the file is correct before you import it. Monarch cannot undo an import. To remove the transactions, you must delete them, or you must delete the account.

Monarch tells you that you can do a test first with a smaller CSV file.

1. On a computer, open Monarch in a web browser.
2. Click **Accounts**.
3. Click **+ Add Account**.
4. Click **Import transaction & balance history**.
5. Click **Import transactions**.
6. Upload your CSV file.
7. Make sure that Monarch gives the correct name to each column.
8. If the file has categories or tags, give a Monarch category or tag to each.
9. Give a Monarch account to each account name in the file.
10. Select an option for transactions that are in the file and in Monarch (refer to the table).
11. Click **Import transactions**.

| Option | Result in Monarch |
| --- | --- |
| **Prioritize CSV** | Monarch deletes all the transactions of the account between the first and last dates of the file. Then it adds the transactions from the file. |
| **Prioritize Monarch** | Monarch keeps its transactions and adds only earlier transactions that are missing. It is possible that Monarch does not import some transactions from the file. |
| **Import all** | Monarch adds all the transactions from the file. A transaction can then be in Monarch two times. |
| **Use transaction IDs to match transactions** | For a file that came from Monarch and has its **Id** column. Monarch changes the transactions that have the same ID. |

### Columns that Monarch must find in the file

The sequence of the columns is not important. Monarch finds each column by its name. These three column names are necessary:

| Column | Rule on the Monarch page |
| --- | --- |
| **Account** | The name of the account. It is optional when you import from the page of one account, with **Edit**. |
| **Amount** | One column for debits and credits. A debit has a minus sign or parentheses: -58.12 or (58.12). A credit has no sign: 58.12. |
| **Date** | "Any standard US-based date format will work (i.e. December 1, 2024 or 12/01/24)." |

**Category**, **Tags** and **Notes** columns are optional. Monarch does not use other columns. If one of the three necessary columns is missing, or is in the file two times, Monarch tells you to correct the file.

### A CSV file from WalletFeed

WalletFeed is a different app for iPhone. It reads your Apple Card, Apple Cash and Savings transactions from Wallet. WalletFeed does not send transactions to Monarch. But [Export CSV](/docs/export-csv/) in WalletFeed makes a CSV file of a period that you select. WalletFeed Pro is not necessary for this file.

The file has 17 columns. [Columns in the CSV file](/guides/export-apple-card-transactions/#columns-in-the-csv-file) gives the full list. These columns have the names that Monarch must find:

| Column in the WalletFeed file | Data |
| --- | --- |
| **Account** | The Wallet account, for example Apple Card. |
| **Amount** | The value of the transaction. Purchases and fees have a minus sign. Payments and refunds have no minus sign. |
| **Date** | The date of the transaction, for example 2026-10-28. |

The Monarch page does not tell you if Monarch accepts the WalletFeed file. Before you import the file, look at these differences:

- The examples of dates on the Monarch page do not include a date such as 2026-10-28.
- The WalletFeed file also has a **Posted Date** column and a **Foreign Amount** column. In Monarch, make sure that only **Date** and **Amount** have the names of the necessary columns.
- The WalletFeed file has a **Category** column with the WalletFeed categories. In Monarch, **Category** is an optional column.
- The WalletFeed file also has pending and declined transactions. The **Status** column shows `booked` for a posted transaction.

Thus, do a test first with a file of a short period, for example **This Month**.

WalletFeed is available only in the US, for an iPhone with iOS 26 or a newer version. WalletFeed has no account, and no WalletFeed server keeps your transactions.
