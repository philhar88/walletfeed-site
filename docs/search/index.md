# Search

Search in WalletFeed finds your Apple Card, Apple Cash and Savings transactions. You type a part of a merchant name, a description, a category or an amount. Search then shows each transaction that has this text. With Apple Intelligence, Search can also read your text, for example `Dining over $50 last month`, and change it into filters. You can use Search without [WalletFeed Pro](/docs/walletfeed-pro/).

Search uses the transactions of the [Wallet accounts](/docs/wallet-accounts/) that you share with WalletFeed. When you open Search, WalletFeed reads these transactions on your iPhone. It does not keep a copy of them.

## Find a transaction

1. On your iPhone, open WalletFeed.
2. Tap the search button at the bottom of the screen.

   ![The Transactions screen, with the tab bar and the search button at the bottom of the screen.](https://walletfeed.app/docs/search/walletfeed-transactions.webp)

   Search shows the search field and the keyboard.

3. Type a part of a merchant name, a category or an amount, for example `Uber`, `Dining` or `23.40`.

   Search shows the results while you type.

Search finds the same transactions for `uber`, `Uber` and `UBER`. The results show in a section for each month, as in [Transactions](/docs/transactions/).

To type different text, tap the clear button in the search field. To close Search, tap the close button (X). WalletFeed then shows the last tab that you used.

## Find transactions in a category

When the search field is empty, Search shows **Categories**. This list has the categories of your transactions.

1. Tap the search button.
2. In **Categories**, tap a category, for example **Groceries**.

   Search puts the name of the category in the search field and shows the results.

## Find transactions with Apple Intelligence

Search with Apple Intelligence reads your text and changes it into filters. For example, it changes `Dining over $50 last month` into **Dining · Over $50.00 · Last month**. Search with Apple Intelligence is available only if your iPhone can use Apple Intelligence and Apple Intelligence is on. On these iPhones, the empty search field shows **Dining over $50 last month** as an example.

1. Tap the search button.
2. Type the category, merchant, amount or period to find, for example `Dining over $50 last month`.

   While you type, Search shows the transactions that have the text. If no transaction has the text, Search shows **Tap Search to use Apple Intelligence.**

3. Tap **Search** on the keyboard.

   While Apple Intelligence reads the text, the Apple Intelligence icon and a progress indicator show at the top of the list.

   ![The Search screen with the filters Groceries, Over $50.00 and Last 30 days, and a row with 4 transactions and a total of $277.57.](https://walletfeed.app/docs/search/walletfeed-search.webp)

At the top of the results, Search shows the filters that Apple Intelligence found in your text, for example **Groceries · Over $50.00 · Last 30 days**. Below the filters, a row shows the number of transactions and their total. If no transaction agrees with the filters, the row shows **0 transactions** and $0.00.

Apple Intelligence can find these filters in your text:

- One or more categories, for example **Dining** or **Groceries**. Other text can also give a category. For example, `restaurants` gives **Dining**, and `gas` gives **Fuel**.
- A merchant, for example `Uber`. WalletFeed uses the merchant only if it is in your text.
- Only purchases (**Purchases**), or only money that you received (**Money in**).
- An amount, with `over` or `under`, for example `over $50`. WalletFeed uses the amount only if it is in your text.
- One period: **Last 7 days**, **Last 30 days**, **This month** or **Last month**.

WalletFeed also finds a merchant when your text is not the same as the name. For example, `Ubers` finds Uber, and `trader joes` finds Trader Joe's.

WalletFeed calculates the number of transactions and the total. Apple Intelligence does not calculate them.

For **Money in**, the total is the money that you received. For all other filters, WalletFeed adds the amounts of your purchases. Refunds decrease the total. Payments and transfers do not change it.

If Apple Intelligence cannot read your text, Search shows **Couldn't read this search. Showing text matches.** The list then shows the transactions that have your text.

When you change the text, WalletFeed removes the filters. To use Apple Intelligence again, tap **Search** on the keyboard.

> **Note:** Apple Intelligence reads your text on your iPhone. It receives only the text that you type. It does not receive your transactions.

## Open Search with Siri

1. Tell Siri "Search WalletFeed" or "Find a transaction in WalletFeed".
2. When Siri shows **What are you looking for?**, tell Siri the transactions to find, for example "dining over $50 last month".

   Search opens with your text in the search field. If Search with Apple Intelligence is available, Apple Intelligence then reads the text.

Siri does not receive your transactions or the total. They show only in WalletFeed.

In the Shortcuts app, the same action has the name **Search Transactions**. For more information, refer to [Siri and Shortcuts](/docs/siri-and-shortcuts/).

## If there is a problem

### If Search shows **No Cards**

You did not tap **Share** or **Don't Share** on the Wallet access screen.

1. Tap **Choose Accounts**.

   The Wallet access screen opens.

2. Make sure that the switch for each account to share is on.

   ![The Share Wallet Data screen, with the switches for Apple Card, Apple Cash and Savings on.](https://walletfeed.app/docs/search/walletfeed-wallet-access.webp)

3. Tap **Share**.

### If Search shows **Wallet Access Off**

You tapped **Don't Share**, or you stopped Wallet access for WalletFeed in the Settings app. iOS shows the Wallet access screen only one time.

1. On your iPhone, open the Settings app.
2. Tap **Privacy & Security** › **Wallet** › **WalletFeed**.
3. Select the accounts to share with WalletFeed.
4. Open WalletFeed.

### If Search shows **No Results for “…”**

No transaction has your text in its merchant name, description, category or amount.

1. Make sure that the text is correct.
2. Type shorter text, for example only the first part of the merchant name.
3. If Search shows **Tap Search to use Apple Intelligence.**, tap **Search** on the keyboard.

### If Apple Intelligence does not read your text

Apple Intelligence reads text that has 2 to 200 characters. If the empty search field shows **Transactions**, Search with Apple Intelligence is not available on this iPhone.

1. Make sure that your iPhone can use Apple Intelligence.
2. Make sure that Apple Intelligence is on.
3. Make sure that the text has 2 to 200 characters.
4. Tap **Search** on the keyboard.

### If Search shows **Couldn't read this search. Showing text matches.**

Apple Intelligence did not find filters in your text that WalletFeed can use. Search then shows the transactions that have your text.

1. Type shorter text that has a category, a merchant, an amount or a period, for example `groceries this month`.
2. Tap **Search** on the keyboard.

### If a transaction is not in the results

Search finds only the transactions of the Wallet accounts that you share with WalletFeed. Wallet shares the transactions of each account from a start date that you selected.

1. On your iPhone, open the Settings app.
2. Tap **Privacy & Security** › **Wallet** › **WalletFeed**.
3. Change the accounts or the start dates that you share.
4. Open WalletFeed.
5. Type your text in the search field again.
