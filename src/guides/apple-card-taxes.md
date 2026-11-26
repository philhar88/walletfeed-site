+++
title = "Get your Apple Card totals and transactions for your taxes"
nav_title = "Taxes"
seo_title = "Apple Card for taxes: year-end totals and transactions"
description = "Get the year-end totals of your Apple Card and Savings transactions for your taxes: interest, fees, purchases and refunds, and a file of all transactions."
group = "Free features"
order = 50
related = ["guides/apple-card-year-end-summary", "docs/tax-pack", "docs/export-csv", "guides/export-apple-card-transactions"]
updated = 2026-11-26

[video]
name = "Apple Card transactions and totals for your taxes"
description = "WalletFeed makes one file of a year of Apple Card transactions with Export CSV. Tax Pack gives the totals of the year: interest, fees, purchases and refunds. With WalletFeed Pro, Background Sync sends new transactions to a destination."
uploaded = 2026-11-25
duration = "PT30S"
+++

For your taxes, WalletFeed gives the year-end totals of your Apple Card, Apple Cash and Savings transactions on your iPhone. The [Tax Pack](/docs/tax-pack/) screen shows the annual totals of the interest, the fees, the purchases and the refunds. With [Export CSV](/docs/export-csv/), you make one file of all the transactions of last year.

> **Note:** WalletFeed does not give tax advice. The totals are sums of the records in Wallet. They are not a tax form.

This video (30 seconds) shows the file from **Export CSV**, the totals in **Tax Pack** and [Background Sync](/docs/background-sync/) with WalletFeed Pro.

![Video: one file of a year of Apple Card transactions, and the totals in Tax Pack (30 seconds).](video:apple-card-taxes)

## Before you start

You must have these items:

- An iPhone with iOS 26 or a newer version. WalletFeed is available only in the US.
- WalletFeed on your iPhone, with [access to your Wallet accounts](/docs/wallet-accounts/). These accounts are Apple Card, Apple Cash and Savings.
- For each account, a start date before January 1 of the year. Wallet gives transactions to WalletFeed only from that date.

[WalletFeed Pro](/docs/walletfeed-pro/) is not necessary for the totals on the screen or for **Export CSV**. Some plans include the files of the Tax Pack (refer to [Step 3](#step-3-send-the-files-of-the-tax-pack)).

## Tax documents and statements from Apple

For a Savings account, Apple says: "Tax documents are available by January 31 for customers that have reportable interest." You get them in Wallet or at card.apple.com/savings. In Wallet, **Tax Documents** is in **Documents** for the Savings account. Apple gives the steps in [View and update your Savings account information in Apple Wallet](https://support.apple.com/en-us/102163).

For Apple Card, Wallet has a statement for each month. Wallet can also make a file of the transactions between two dates. Apple gives the steps in [Download your Apple Card statements or export your transactions](https://support.apple.com/en-us/102284).

That Apple page does not name a year-end statement or an annual summary for Apple Card. For the items that Wallet has for a year, refer to [Get an Apple Card year-end summary](/guides/apple-card-year-end-summary/).

The tax documents from the bank are the tax record.

## Step 1: Find the totals of the year

1. On your iPhone, open WalletFeed.
2. Tap **Settings** (the gear button) at the top of the screen.

   ![The Transactions screen with the gear button at the top.](app:06-transactions)

3. In the **Data** section, tap **Tax Pack**.
4. Tap **Year**.
5. Select the year.

   The screen shows the totals of each Wallet account for that year.

You can also open **Tax Pack** from the **Tax Reports** section, at the end of the **Spending** tab.

The screen shows these totals:

| Account | Totals |
| --- | --- |
| Apple Card | **Purchases**, **Refunds**, **Interest charged**, **Fees** and **Payments to the card** |
| Apple Cash and Savings | **Interest earned**, **Money in, without interest** and **Money out** |

You can select this year or one of the two years before it. Only posted transactions are in the totals. Before the end of a year, the screen shows the totals up to that day. For each total and its limits, refer to [Tax Pack](/docs/tax-pack/).

## Step 2: Make a file of all the transactions of last year

1. In WalletFeed, tap **Settings** (the gear button) at the top of the screen.
2. In the **Data** section, tap **Export CSV**.
3. Tap **Range**.
4. Select **Last Year**.

   **Transactions** shows the number of transactions in the year.

5. Tap **Export**.

   The iOS menu opens with the file `Apple Card Last Year.csv`.

6. Tap **Save to Files**, or select AirDrop, Mail or a different app.

The file has one row for each transaction of the year before this year, from each Wallet account that WalletFeed can read. The columns include the date, the merchant, the amount, the category and the account. For all the columns, refer to [Export CSV](/docs/export-csv/#columns-in-the-file).

## Step 3: Send the files of the Tax Pack

These plans of [WalletFeed Pro](/docs/walletfeed-pro/) include **Share Pack** and **Share Summary for AI**:

- **Yearly**, but not during its free trial
- **Lifetime**.

Without one of these plans, the **Tax Pack** screen shows **Upgrade** or **Change Plan**.

1. In **Tax Pack**, select the year in **Year**.
2. Tap **Share Pack**.

   The iOS menu opens with four files: a PDF summary, a Markdown summary for AI and two CSV files.

3. Tap **Save to Files**, or select AirDrop, Mail or a different app.

The files have the totals from the screen. They also have the purchases minus the refunds for each category and for each month, and a total for each merchant. For the contents of each file, refer to [Files in the pack](/docs/tax-pack/#files-in-the-pack).

## Give the files to a tax preparer or an AI assistant

For a tax preparer, send the PDF file. It is a summary of one or two pages. If the tax preparer must have each transaction, send the transactions file also.

For an AI assistant, tap **Share Summary for AI** on the **Tax Pack** screen. The iOS menu opens with only the Markdown file. Select the app of the AI assistant, or save the file and add it to a conversation.

The files go only to the app or person that you select. WalletFeed makes the files on your iPhone and does not keep a copy. After a service receives a file, the terms and the privacy policy of that service are applicable to the file.

WalletFeed can also keep a Google Sheet of your transactions up to date for an AI chatbot. Refer to the guides for [ChatGPT](/guides/apple-card-to-chatgpt/), [Claude](/guides/apple-card-to-claude/) and [Gemini](/guides/apple-card-to-gemini/).

## Get a notification when the year is completed

Tax Pack Ready sends one notification at 9:00 on January 3. Most pending charges of December post before that time. WalletFeed Pro is not necessary for this notification.

1. In WalletFeed, tap **Settings** (the gear button) at the top of the screen.
2. In the **Notifications** section, set the **Tax Pack Ready** switch to on.
3. If iOS shows a message about notifications, tap **Allow**.
4. Tap **Done**.

## Limits of the totals

The **Tax Pack** screen and the files show "WalletFeed doesn't give tax advice." The totals are sums of the records in Wallet, and they have these limits:

- **Interest earned** is the sum of the interest transactions in Wallet. The Form 1099-INT from the bank is the tax record.
- Pending transactions and transactions in a different currency are not in the totals.
- If more than one person uses your Apple Card, the transactions do not show the person who made them.
- Wallet does not identify Daily Cash. Thus, Daily Cash has no total of its own.

[Tax Pack](/docs/tax-pack/#limits-of-the-totals) gives all the limits.

## If there is a problem

### If the year shows 0 transactions

The year has no posted transactions, or WalletFeed cannot read the transactions of your Wallet accounts.

1. Select a different year in **Year**.
2. If each year shows 0, do the steps in [If each period has 0 transactions](/docs/export-csv/#if-each-period-has-0-transactions).

### If the first months of a year are missing

Wallet gives transactions to WalletFeed from the start date of each account.

1. On your iPhone, open the Settings app.
2. Tap **Privacy & Security** › **Wallet** › **WalletFeed**.
3. For each account, select a start date before January 1 of the year.
4. Open WalletFeed.

### If the Tax Pack screen shows **Upgrade** or **Change Plan**

Your plan does not include the files. The totals on the screen and **Export CSV** stay free.

For the plans, refer to [Plans that include the files](/docs/tax-pack/#plans-that-include-the-files).
