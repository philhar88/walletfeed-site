# Transactions

The **Transactions** tab in WalletFeed shows your Apple Card, Apple Cash and Savings transactions by month on your iPhone. WalletFeed reads the transactions from Wallet and does not keep them.

## Open your transactions

1. On your iPhone, open WalletFeed.
2. Tap **Transactions** at the bottom of the screen.

   ![The Transactions tab with the October transactions and a pending charge at the top.](https://walletfeed.app/docs/transactions/walletfeed-transactions.webp)

The list has a section for each month. The month of your last transaction is at the top. Each section starts with the last transaction of its month. The name of a month before this year also shows the year, for example "September 2025".

## Transaction rows

Each row shows these items:

- An icon for the category
- The merchant name
- The amount
- The date.

The icon shows the category, for example a car for **Transport**. WalletFeed sets the category from the merchant category code (MCC).

If Wallet gives no merchant name, the row shows the description of the transaction. Some rows have a second line below the merchant name. This line shows **Pending** until the transaction posts. If most transactions in the list are from a different account, the line also shows the account name. For example, Apple Cash rows show "Apple Cash" when most transactions are from Apple Card.

A credit, for example a refund, is green and has a plus sign (+).

For the last 7 days, the date is **Today**, **Yesterday** or the name of the day, for example "Tuesday". For a date before these 7 days, the row shows the month and the day, for example "Oct 3". A date before this year also shows the year.

The category name is not on the row, but VoiceOver reads it with the other items in the row. The row also does not show the person who used the card, because Wallet does not give this information to apps.

## Apple Card Monthly Installments

If you use Apple Card Monthly Installments, the list shows the charge for each month with your other transactions. Apple adds these charges on the last day of the month. In [Spending](/docs/spending/), the **Monthly Installments** section also shows the charges of the last month that has them. Wallet does not give apps other installment information, for example the item that you bought or the remaining balance.

## Show more transactions

WalletFeed reads 200 transactions first. When you scroll to the end of the list, WalletFeed reads 200 more transactions.

1. Scroll down the list.
2. Continue to scroll until a message shows at the end of the list.

   The message gives the date of the last row, for example "Showing transactions from March 4, 2025."

   If **Sample Data** is on, the message does not show.

Wallet shares the transactions of each account from a start date. You select this date for each account when you [share the account with WalletFeed](/docs/wallet-accounts/).

## Change the accounts or the start dates

You select the accounts and their start dates on the Wallet access screen, which iOS shows only one time. After that, you change them in the Settings app.

1. On your iPhone, open the Settings app.
2. Tap **Privacy & Security** › **Wallet** › **WalletFeed**.
3. Select the accounts to share with WalletFeed.
4. To get transactions from before the start date of an account, change its start date.
5. Open WalletFeed.

   When WalletFeed opens, it reads Wallet again.

## Update the list

WalletFeed reads your transactions again each time you open WalletFeed or the **Transactions** tab.

1. At the top of the list, swipe down.

   WalletFeed reads your transactions from Wallet again. If WalletFeed cannot read Wallet, the list does not change.

## Find a transaction

To find a transaction by its merchant, category or amount, use [Search](/docs/search/). Search shows its results in the same rows and month sections as **Transactions**.

## If there is a problem

### If WalletFeed shows "No Cards"

You did not share Wallet accounts with WalletFeed.

1. Tap **Choose Accounts**.

   iOS shows the Wallet access screen.

2. Select each account to share.
3. For each account, select the start date.
4. Tap **Share**.

### If WalletFeed shows "Wallet Access Off"

You did not let WalletFeed read Wallet, or you stopped its access to Wallet in the Settings app. The Wallet access screen opens only one time.

1. On your iPhone, open the Settings app.
2. Tap **Privacy & Security** › **Wallet** › **WalletFeed**.
3. Select the accounts to share with WalletFeed.
4. Open WalletFeed.

### If WalletFeed shows "No Transactions"

The accounts that you share with WalletFeed have no transactions. WalletFeed also shows this message if it cannot read Wallet.

1. On your iPhone, open the Settings app.
2. Tap **Privacy & Security** › **Wallet** › **WalletFeed**.
3. Select more accounts to share with WalletFeed.
4. Open WalletFeed.

   When WalletFeed opens, it reads Wallet again.

### If WalletFeed shows "Wallet Unavailable"

This iPhone cannot share Wallet data with apps. WalletFeed cannot show transactions on it. WalletFeed is for iPhone with iOS 26 or a newer version, and it is available only in the US.

### If a transaction is not in the list

WalletFeed shows only the Apple Card, Apple Cash and Savings transactions that Wallet shares with it.

1. At the top of the list, swipe down.
2. Scroll down the list until you find the transaction or until you are at the end of the list.
3. In the Wallet app, find the account and the date of the transaction.
4. If you do not share the account, or the date is before its start date, do the steps in [Change the accounts or the start dates](#change-the-accounts-or-the-start-dates).

### If the list shows transactions that you did not make

**Sample Data** is on. While it is on, WalletFeed shows two months of sample transactions and does not show your Wallet transactions.

1. In WalletFeed, tap **Settings** (the gear button) at the top of the screen.
2. In the **Data** section, set **Sample Data** to off.
3. Tap **Done**.
