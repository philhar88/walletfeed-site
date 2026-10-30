# Search Apple Card transactions

On your iPhone, [Search](/docs/search/) in WalletFeed finds a purchase in your Apple Card, Apple Cash and Savings transactions. You type the merchant, the amount or the category of the purchase. With Apple Intelligence, one search can have more than one filter, for example `dining over $50 last month`.

## Before you start

You must have these items:

- An iPhone with iOS 26 or a newer version. WalletFeed is available only in the US.
- WalletFeed on your iPhone, with access to your Apple Card, Apple Cash or Savings account. You can use Search without [WalletFeed Pro](/docs/walletfeed-pro/).
- An iPhone that can use Apple Intelligence, with Apple Intelligence active (necessary only for Search with Apple Intelligence).

## Step 1: Open Search

1. On your iPhone, open WalletFeed.
2. Tap the search button in the bottom right corner of the screen.

   ![The Transactions screen with the tab bar and the search button at the bottom of the screen.](https://walletfeed.app/guides/search-apple-card-transactions/walletfeed-transactions.webp)

   Then WalletFeed opens the search field and the keyboard. When the search field is empty, WalletFeed shows the categories of your transactions below **Categories**.

## Step 2: Find a purchase

1. Type a merchant name (`Uber`), an amount (`23.40`) or a category (`Dining`).

   When you type, WalletFeed shows the transactions that have your text in their merchant, description, category or amount.

   The results have one section for each month. In each section, the newest transaction is at the top. The rows are the same as in [Transactions](/docs/transactions/).

2. To start a different search, tap the clear button (x) in the search field.

When the search field is empty, you can also tap a category below **Categories**. Then WalletFeed puts the name of the category in the search field. The results show all the transactions in that category. The results can also include transactions that have the name of the category in their merchant or description.

## Step 3: Use Apple Intelligence in Search

If your iPhone can use Apple Intelligence and Apple Intelligence is active, the empty search field shows the example "Dining over $50 last month". If the empty search field shows "Transactions", Apple Intelligence is not available (refer to [If Apple Intelligence does not read the search](#if-apple-intelligence-does-not-read-the-search)).

1. In the search field, type your search, for example `dining over $50 last month`.
2. Tap **Search** on the keyboard.

   When Apple Intelligence reads the search, WalletFeed shows the Apple Intelligence icon and a progress indicator.

   At the top of the results, WalletFeed shows the filters that Apple Intelligence found, for example "Groceries · Over $50.00 · Last 30 days". Below the filters, a row shows the number of transactions and their total.

   ![The search results with the filters Groceries, Over $50.00 and Last 30 days, and a row that shows 4 transactions and a total of $277.57.](https://walletfeed.app/guides/search-apple-card-transactions/walletfeed-search.webp)

3. If you change the search, tap **Search** on the keyboard again.

   Until you tap **Search**, WalletFeed shows only the transactions that have your text.

> **Note:** On your iPhone, Apple Intelligence reads only your search. WalletFeed finds the transactions and calculates the total.

## Searches that Apple Intelligence can read

Apple Intelligence finds filters in your search. Then WalletFeed uses these filters to find your transactions. A search can have:

- One or more categories, for example **Dining** or **Groceries**
- A merchant, for example "Uber"
- An amount, with "over" or "under", for example "over $50"
- One period (**Last 7 days**, **Last 30 days**, **This month** or **Last month**)
- Only purchases (**Purchases**) or only money that you received (**Money in**).

Apple Intelligence can also find a category from a word that is not the name of the category. For example, it finds **Dining** for "restaurants" and **Fuel** for "gas".

For a merchant in the search, capital letters, accents, punctuation and an "s" at the end do not change the results. For example, "Ubers" finds Uber, and "trader joes" finds Trader Joe's.

WalletFeed calculates the number of transactions and the total. If the top of the results shows **Money in**, the total is the money that you received. If the top of the results does not show **Money in**, WalletFeed adds the amounts of your purchases. A refund decreases this total. Transfers and card payments do not change this total.

If WalletFeed finds no transactions for the filters, the row shows "0 transactions" and $0.00.

## Start a search with Siri

1. Tell [Siri](/docs/siri-and-shortcuts/) "Search WalletFeed" or "Find a transaction in WalletFeed".
2. When you hear "What are you looking for?", tell Siri your search, for example "dining over $50 last month".

   Then WalletFeed opens Search and shows your search in the search field. If your iPhone can use Apple Intelligence and Apple Intelligence is active, Apple Intelligence reads the search.

Siri does not get the results of the search or the total.

## If there is a problem

### If Search shows "No Cards"

You did not tap **Share** or **Don't Share** on the Wallet access screen.

1. Tap **Choose Accounts**.

   Then iOS shows the Wallet access screen (**Share Wallet Data**).

2. Select the accounts that WalletFeed can read.

   ![The Share Wallet Data screen, with the switches for Apple Card, Apple Cash and Savings set to on.](https://walletfeed.app/guides/search-apple-card-transactions/walletfeed-wallet-access.webp)

3. Tap **Share**.

### If Search shows "Wallet Access Off"

You tapped **Don't Share**, or you stopped Wallet access for WalletFeed in the Settings app. iOS shows the Wallet access screen only one time. After this, you can change the access only in the Settings app.

1. On your iPhone, open the Settings app.
2. Tap **Privacy & Security** › **Wallet** › **WalletFeed**.
3. Select the accounts that WalletFeed can read.
4. Open WalletFeed.

### If Search finds no transactions

No transaction has the text that you typed. Search shows "No Results for" and your search.

1. Make sure that the name of the merchant is correct.
2. Type a shorter search, for example only the first part of the name.
3. If WalletFeed shows "Tap Search to use Apple Intelligence.", tap **Search** on the keyboard.

### If Apple Intelligence does not read the search

Apple Intelligence reads a search only when Apple Intelligence is active and the search has 2 to 200 characters. If the empty search field shows "Transactions", Apple Intelligence is not available.

1. Make sure that your iPhone model is on the list in [Get started with the next generation of Apple Intelligence](https://support.apple.com/en-us/121115).
2. On your iPhone, open the Settings app.
3. Tap **Apple Intelligence & Siri**.
4. Set **Apple Intelligence** to on, or tap **Turn on Apple Intelligence**.
5. Open WalletFeed.
6. Make sure that the search has 2 to 200 characters.
7. Tap **Search** on the keyboard.

### If Search shows "Couldn't read this search. Showing text matches."

In your search, Apple Intelligence did not find filters that WalletFeed can use. Then WalletFeed shows the transactions that have your text.

1. Type a short search with a category, a merchant, an amount or a period, for example `groceries this month`.
2. Tap **Search** on the keyboard.

### If a purchase is not in the results

Search finds only the transactions of the [Wallet accounts](/docs/wallet-accounts/) that you selected for WalletFeed. For each account, iOS gives WalletFeed the transactions from the start date that you selected.

1. On your iPhone, open the Settings app.
2. Tap **Privacy & Security** › **Wallet** › **WalletFeed**.
3. Change the accounts or the start date of each account.
4. Open WalletFeed.
5. Do the search again.
