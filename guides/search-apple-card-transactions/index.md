# Search Apple Card transactions

On your iPhone, [Search](/docs/search/) in WalletFeed finds a purchase in your Apple Card, Apple Cash and Savings transactions when you type its merchant, amount or category. With Apple Intelligence, a search can also include a category, an amount and a period together, for example `dining over $50 last month`.

## Before you start

- An iPhone with iOS 26 or a newer version. WalletFeed is available only in the US.
- WalletFeed with access to your Apple Card, Apple Cash or Savings account.
- For a search with Apple Intelligence, an iPhone that can use Apple Intelligence and has Apple Intelligence on.

You can use Search without [WalletFeed Pro](/docs/walletfeed-pro/).

## Step 1: Open Search

1. On your iPhone, open WalletFeed.
2. Tap the search button in the bottom right corner of the screen.

   ![The Transactions screen with the tab bar and the search button at the bottom of the screen.](https://walletfeed.app/guides/search-apple-card-transactions/walletfeed-transactions.webp)

   The search field opens, and the keyboard shows. While the field is empty, **Categories** shows the categories of your transactions.

## Step 2: Find a purchase

1. Type the name of a merchant, an amount or a category, for example `Uber`, `23.40` or `Dining`.

   While you type, WalletFeed shows the transactions that have your text in their merchant, description, category or amount.

   The results show in one section for each month. In each section, the newest transaction is at the top. Each row shows the merchant, the amount and the date. The rows are the same as in [Transactions](/docs/transactions/).

2. To start a different search, tap the clear button (x) in the search field.

While the search field is empty, you can also tap a category below **Categories**. WalletFeed then puts the name of the category in the search field. The results show all the transactions in that category. They can also show other transactions that have this name in their merchant or description.

## Step 3: Use Apple Intelligence in Search

If your iPhone can use Apple Intelligence and Apple Intelligence is on, the empty search field shows the example "Dining over $50 last month".

1. In the search field, type your search, for example `dining over $50 last month`.
2. Tap **Search** on the keyboard.

   While Apple Intelligence reads the search, WalletFeed shows the Apple Intelligence icon and a progress indicator.

   At the top of the results, WalletFeed shows the filters that Apple Intelligence found, for example "Groceries · Over $50.00 · Last 30 days". Below the filters, a row shows the number of transactions and their total.

   ![Search results with the filters Groceries, Over $50.00 and Last 30 days, and a row that shows 4 transactions and a total of $277.57.](https://walletfeed.app/guides/search-apple-card-transactions/walletfeed-search.webp)

3. If you change the search, tap **Search** on the keyboard again.

   Until you tap **Search**, WalletFeed shows only the transactions that have the text.

> **Note:** On your iPhone, Apple Intelligence reads only your search. WalletFeed finds the transactions and calculates the total.

## Searches that Apple Intelligence can read

Apple Intelligence changes your search into filters. WalletFeed then finds your transactions with these filters. A search can have:

- One or more categories, for example **Dining** or **Groceries**. Other text can also give a category. For example, "restaurants" gives **Dining**, and "gas" gives **Fuel**.
- A merchant, for example "Uber".
- An amount, with "over" or "under", for example "over $50".
- One period: **Last 7 days**, **Last 30 days**, **This month** or **Last month**.
- Only purchases (**Purchases**) or only money that you received (**Money in**).

For a merchant, capital letters, accents, punctuation and an "s" at the end do not change the results. For example, "Ubers" finds Uber, and "trader joes" finds Trader Joe's.

WalletFeed calculates the number of transactions and the total. If the top of the results shows **Money in**, the total is the money that you received. For all other searches, WalletFeed adds the amounts of your purchases. A refund decreases this total. Transfers and card payments do not change it.

If WalletFeed finds no transactions for the filters, the row shows "0 transactions" and $0.00.

## Start a search with Siri

1. Tell [Siri](/docs/siri-and-shortcuts/) "Search WalletFeed" or "Find a transaction in WalletFeed".
2. When you hear "What are you looking for?", tell Siri your search, for example "dining over $50 last month".

   Search opens in WalletFeed and shows your search in the search field. If your iPhone can use Apple Intelligence and Apple Intelligence is on, Apple Intelligence then reads the search.

Siri does not get the results of the search or the total. They show only in WalletFeed.

## If there is a problem

### If Search shows "No Cards"

You did not select the Wallet accounts to share with WalletFeed.

1. Tap **Choose Accounts**.
2. In the list of Wallet accounts that iOS shows, select your Apple Card, Apple Cash or Savings account.
3. Tap **Share**.

### If Search shows "Wallet Access Off"

You did not give WalletFeed access to Wallet. You can change the access only in the Settings app.

1. On your iPhone, open the Settings app.
2. Tap **Privacy & Security** › **Wallet** › **WalletFeed**.
3. Select the accounts to share with WalletFeed.
4. Open WalletFeed.

### If Search finds no transactions

No transaction has the text that you typed. Search then shows "No Results for" and your search.

1. Make sure that the name of the merchant is correct.
2. Type less text, for example only the first part of the name.
3. If WalletFeed shows "Tap Search to use Apple Intelligence.", tap **Search** on the keyboard.

### If Apple Intelligence does not read the search

Apple Intelligence reads a search only when Apple Intelligence is on and the search has 2 to 200 characters. If the empty search field shows "Transactions", Apple Intelligence is not available.

1. Make sure that your iPhone can use Apple Intelligence and that Apple Intelligence is on.
2. Make sure that the search has 2 to 200 characters.
3. Tap **Search** on the keyboard.

### If Search shows "Couldn't read this search. Showing text matches."

Apple Intelligence did not change your search into filters that WalletFeed can use. WalletFeed then shows the transactions that have the text.

1. Type a short search with a category, a merchant, an amount or a period, for example `groceries this month`.
2. Tap **Search** on the keyboard.

### If a purchase is not in the results

Search finds only the transactions of the [Wallet accounts](/docs/wallet-accounts/) that you share with WalletFeed. For each account, iOS shares the transactions from the start date that you selected.

1. On your iPhone, open the Settings app.
2. Tap **Privacy & Security** › **Wallet** › **WalletFeed**.
3. Change the accounts or the start date of each account.
4. Open WalletFeed.
5. Do the search again.
