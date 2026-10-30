+++
title = "First steps with WalletFeed"
nav_title = "First steps"
description = "Open WalletFeed on your iPhone for the first time and select the Wallet accounts that it can read. Then look at your Apple Card transactions."
order = 10
related = ["docs/wallet-accounts", "docs/spending", "docs/destinations"]
updated = 2026-10-30
+++

WalletFeed shows the transactions from your Apple Card, Apple Cash and Savings accounts on your iPhone. To start, you open WalletFeed and select the Wallet accounts that it can read.

## Before you start

WalletFeed is available only in the US. You must have these items:

- An iPhone with iOS 26 or a newer version
- An Apple Card, Apple Cash or Savings account in Wallet on the iPhone
- WalletFeed on the iPhone (from the App Store).

If you do not have an Apple Card, Apple Cash or Savings account, refer to [Use WalletFeed with sample transactions](#use-walletfeed-with-sample-transactions).

## Open WalletFeed for the first time

1. On your iPhone, open WalletFeed.

   The **Welcome to WalletFeed** screen opens. This screen tells you about **Ask Spending**, **Destinations**, **On-Device Privacy** and **Background Sync**. If Apple Intelligence is not available on your iPhone, the first item is **Spending and Search**.

   ![The Welcome to WalletFeed screen with the Continue button at the bottom.](app:docs-welcome)

2. Tap **Continue**.

   **Transactions** opens, and iOS shows a message with the buttons **Don't Allow** and **Select Accounts**.

## Select the Wallet accounts for WalletFeed

After you give WalletFeed access to your accounts or tap **Don't Allow**, iOS does not show the message with **Select Accounts** again. Then you can change the accounts for WalletFeed only in the Settings app.

1. Tap **Select Accounts**.

   The list of Wallet accounts opens.

2. Select the accounts for WalletFeed (for example, your Apple Card).

   You can also select a start date for each account. WalletFeed can read only the transactions that occur on or after that date.

3. Tap the **Share with** button.

   **Transactions** shows the transactions from the accounts that you selected.

If you tap **Don't Allow**, **Transactions** shows **Wallet Access Off**. To let WalletFeed read Wallet after that, refer to [If Transactions shows "Wallet Access Off"](#if-transactions-shows-wallet-access-off).

If you tap **Cancel** in the list of Wallet accounts, **Transactions** shows **No Cards**. To select the accounts again, refer to [If Transactions shows "No Cards"](#if-transactions-shows-no-cards).

> **Note:** WalletFeed reads your transactions from Wallet on your iPhone, but it does not keep these transactions. WalletFeed has no account and no WalletFeed servers.

## Look at your transactions

**Transactions** shows your transactions below the name of each month. The newest transactions are at the top.

![The Transactions screen with the October transactions and the tabs at the bottom of the screen.](app:06-transactions)

Each row shows the merchant and the amount. The day is below the amount. Below the merchant, a row can also show "Pending". If a transaction is not from the account that has the most transactions, its row also shows the account name (for example, Apple Cash).

At the end of the list, WalletFeed shows the date of the first transaction that it can read. To let WalletFeed read the transactions from before that date, refer to [Change the accounts that WalletFeed reads](/docs/wallet-accounts/#change-the-accounts-that-walletfeed-reads).

## Use the other tabs

The tabs and the search button at the bottom of the screen open the other parts of WalletFeed:

- The [**Spending**](/docs/spending/) tab shows the total amount of your purchases this month, for each day, category and merchant.
- The [**Destinations**](/docs/destinations/) tab shows the destinations that receive your transactions from WalletFeed (for example, a budget app or a spreadsheet).
- The search button opens [**Search**](/docs/search/). Search finds the transactions that have the merchant or the amount that you type.

You can use Spending, [Ask Spending](/docs/ask-spending/), Search, [Recurring Charges](/docs/recurring-charges/), the [Spending widget](/docs/spending-widget/) and [CSV export](/docs/export-csv/) without [WalletFeed Pro](/docs/walletfeed-pro/). To send transactions to a destination, you must have WalletFeed Pro. WalletFeed Pro is a subscription with a 1-week free trial, or a one-time Lifetime purchase.

## Use WalletFeed with sample transactions

If you do not have an Apple Card, Apple Cash or Savings account, you can use WalletFeed with sample transactions. WalletFeed shows **Sample Data** in **Settings** only if you have no destinations or if **Sample Data** is on.

1. In WalletFeed, tap **Settings** (the gear button) at the top of the screen.
2. Scroll to the **Data** section.
3. Set **Sample Data** to on.
4. Tap **Done**.

   **Transactions** shows two months of sample transactions. It does not show the transactions from your Wallet.

When you set **Sample Data** to off, WalletFeed shows the transactions from your Wallet again.

## Correct problems with Wallet accounts

### If Transactions shows "Wallet Access Off"

WalletFeed cannot read your Wallet accounts. This problem occurs after you tap **Don't Allow**, or after you remove the Wallet access for WalletFeed in the Settings app.

1. On your iPhone, open the Settings app.
2. Tap **Privacy & Security** › **Wallet** › **WalletFeed**.
3. Select the accounts for WalletFeed.
4. Open WalletFeed again.

   **Transactions** shows your transactions.

### If Transactions shows "No Cards"

You did not give WalletFeed access to your Wallet accounts, and you did not tap **Don't Allow**. This problem occurs after you tap **Cancel** in the list of Wallet accounts.

1. In **Transactions**, tap **Choose Accounts**.
2. Do the steps in [Select the Wallet accounts for WalletFeed](#select-the-wallet-accounts-for-walletfeed).

### If Transactions shows "No Transactions"

WalletFeed can read Wallet, but it finds no transactions in the accounts that you selected.

1. On your iPhone, open the Settings app.
2. Tap **Privacy & Security** › **Wallet** › **WalletFeed**.
3. Select more Wallet accounts for WalletFeed.
4. Open WalletFeed again.

### If Transactions shows "Wallet Unavailable"

On this iPhone, WalletFeed cannot read transactions from Wallet. Below **Wallet Unavailable**, WalletFeed shows "This iPhone can't share Wallet data." To use WalletFeed without Wallet data, refer to [Use WalletFeed with sample transactions](#use-walletfeed-with-sample-transactions).
