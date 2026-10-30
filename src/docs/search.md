+++
title = "Search"
nav_title = "Search"
seo_title = "Search: find Apple Card transactions in WalletFeed"
description = "Find your Apple Card, Apple Cash and Savings transactions with Search in WalletFeed. Type a merchant name or an amount, or use Apple Intelligence."
order = 60
related = ["docs/transactions", "docs/ask-spending"]
updated = 2026-10-30
+++

Search in WalletFeed finds your Apple Card, Apple Cash and Savings transactions. You type a part of a merchant name, a description, a category or an amount. Search then shows each transaction that has your text. With Apple Intelligence, Search can also make filters from your text, for example from `Dining over $50 last month`. You can use Search without [WalletFeed Pro](/docs/walletfeed-pro/).

Search uses the transactions of the [Wallet accounts](/docs/wallet-accounts/) that WalletFeed can read. When you open Search, WalletFeed reads these transactions on your iPhone. WalletFeed does not store these transactions.

## Find a transaction

1. On your iPhone, open WalletFeed.
2. Tap the search button at the bottom of the screen.

   ![The Transactions screen, with the tab bar and the search button at the bottom of the screen.](app:06-transactions)

   Search shows the search field and the keyboard.

3. Type a part of a merchant name, a category or an amount, for example `Uber`, `Dining` or `23.40`.

   Search shows the results while you type.

Search finds the same transactions for `uber`, `Uber` and `UBER`.

The results are in one section for each month. [Transactions](/docs/transactions/) has the same sections.

To type different text, tap the clear button in the search field. To close Search, tap the close button (X). Then WalletFeed shows the tab that you used before you opened Search.

## Find transactions in a category

When the search field is empty, Search shows **Categories**. This list has the categories of your transactions.

1. On your iPhone, open WalletFeed.
2. Tap the search button at the bottom of the screen.
3. If the search field has text, tap the clear button in the search field.
4. In **Categories**, tap a category, for example **Groceries**.

   Search puts the name of the category in the search field and shows the results.

## Find transactions with Apple Intelligence

Search with Apple Intelligence reads your text and makes filters from it. For example, `Dining over $50 last month` gives the filters **Dining · Over $50.00 · Last month**. Search with Apple Intelligence is available only if your iPhone can use Apple Intelligence and Apple Intelligence is active. On these iPhones, the empty search field shows **Dining over $50 last month** as an example.

1. On your iPhone, open WalletFeed.
2. Tap the search button at the bottom of the screen.
3. Type a category, a merchant name, an amount or a period, for example `Dining over $50 last month`.

   While you type, Search shows the transactions that have your text. If no transaction has your text, Search shows **Tap Search to use Apple Intelligence.**

4. Tap **Search** on the keyboard.

   While Apple Intelligence reads your text, Search shows the Apple Intelligence icon and a progress indicator above the results.

   ![The Search screen with the filters Groceries, Over $50.00 and Last 30 days, and a row with 4 transactions and a total amount of $277.57.](app:04-search)

At the top of the results, Search shows the filters that Apple Intelligence found in your text, for example **Groceries · Over $50.00 · Last 30 days**. Below the filters, a row shows the number of transactions and their total amount. If Search finds no transactions for the filters, the row shows **0 transactions** and $0.00.

Apple Intelligence can find these filters in your text:

- One or more categories, for example **Dining** or **Groceries**
- A merchant, for example `Uber`
- Only purchases (**Purchases**), or only money that you received (**Money in**)
- An amount with `over` or `under`, for example `over $50`
- One period (**Last 7 days**, **Last 30 days**, **This month** or **Last month**).

A word that is not a category name can also give a category. For example, `restaurants` gives **Dining**, and `gas` gives **Fuel**.

WalletFeed uses a merchant or an amount only if it is in your text. If Apple Intelligence gives a different merchant or amount, or cannot read your text, Search shows **Couldn't read this search. Showing text matches.** Then the list shows the transactions that have your text.

To find a merchant, WalletFeed uses only the letters and numbers in your text. Uppercase letters and accents do not change the result. WalletFeed also finds the merchant if your text adds "s" or "es" to the end of the name. For example, `Ubers` finds Uber, and `trader joes` finds Trader Joe's.

WalletFeed calculates the number of transactions and the total amount. Apple Intelligence does not calculate them.

For **Money in**, the total amount is the money that you received. For the other filters, WalletFeed adds the amounts of your purchases. Refunds decrease the total amount. Payments and transfers do not change it.

When you change the text, WalletFeed removes the filters.

To use Apple Intelligence again, tap **Search** on the keyboard.

> **Note:** Apple Intelligence reads your text on your iPhone and receives only this text. Your transactions do not go to Apple Intelligence.

## Open Search with Siri

1. On your iPhone, start Siri.
2. Tell Siri "Search WalletFeed" or "Find a transaction in WalletFeed".

   You hear "What are you looking for?"

3. Tell Siri the transactions to find, for example "dining over $50 last month".

   Search opens with your text in the search field. If Search with Apple Intelligence is available, Apple Intelligence then reads the text.

Siri does not receive your transactions or the total amount. Only WalletFeed shows them.

In the Shortcuts app, the name of this action is **Search Transactions**. For more information, refer to [Siri and Shortcuts](/docs/siri-and-shortcuts/).

## If there is a problem

### If Search shows **No Cards**

You did not tap **Share** or **Don't Share** on the **Share Wallet Data** screen.

1. Tap **Choose Accounts**.

   The **Share Wallet Data** screen opens.

2. Select the accounts that WalletFeed can read.

   ![The Share Wallet Data screen, with the switches for Apple Card, Apple Cash and Savings set to on.](app:docs-wallet-access)

3. Tap **Share**.

### If Search shows **Wallet Access Off**

You tapped **Don't Share**, or you stopped Wallet access for WalletFeed in the Settings app. After you tap **Share** or **Don't Share**, iOS does not show the **Share Wallet Data** screen again.

1. On your iPhone, open the Settings app.
2. Tap **Privacy & Security** › **Wallet** › **WalletFeed**.
3. Select the accounts that WalletFeed can read.
4. Open WalletFeed again.

### If Search shows **No Results for “…”**

No transaction has your text in its merchant name, description, category or amount.

1. Make sure that your text is correct.
2. Type shorter text, for example only the first part of the merchant name.
3. If Search shows **Tap Search to use Apple Intelligence.**, tap **Search** on the keyboard.

### If Apple Intelligence does not read your text

Apple Intelligence reads only text that has 2 to 200 characters. If the empty search field shows **Transactions**, Search with Apple Intelligence is not available on your iPhone.

1. Make sure that your text has 2 to 200 characters.
2. Tap **Search** on the keyboard.

If the empty search field shows **Transactions**, do these steps:

1. Make sure that your iPhone model is on the list in [Get started with the next generation of Apple Intelligence](https://support.apple.com/en-us/121115).
2. On your iPhone, open the Settings app.
3. Tap **Apple Intelligence & Siri**.
4. Set **Apple Intelligence** to on, or tap **Turn on Apple Intelligence**.
5. Open WalletFeed again.

### If Search shows **Couldn't read this search. Showing text matches.**

In your text, Apple Intelligence did not find filters that WalletFeed can use. Search then shows the transactions that have your text.

1. Type shorter text that has a category, a merchant name, an amount or a period, for example `groceries this month`.
2. Tap **Search** on the keyboard.

### If a transaction is not in the results

Search finds only the transactions of the Wallet accounts that WalletFeed can read. Wallet gives WalletFeed the transactions of each account from the start date that you selected.

1. On your iPhone, open the Settings app.
2. Tap **Privacy & Security** › **Wallet** › **WalletFeed**.
3. Change the accounts that WalletFeed can read, or their start dates.
4. Open WalletFeed again.
5. Type your text in the search field again.
