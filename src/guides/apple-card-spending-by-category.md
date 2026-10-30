+++
title = "See Apple Card spending by category"
nav_title = "Spending by category"
seo_title = "Apple Card spending by category and month"
description = "See your Apple Card spending by category on your iPhone, with the total for the month and the merchants. You can use it without WalletFeed Pro."
group = "Free features"
order = 10
related = ["docs/spending", "docs/ask-spending"]
updated = 2026-10-30
+++

WalletFeed shows your Apple Card spending by category on your iPhone. The [**Spending**](/docs/spending/) tab shows this month's total, a chart with a bar for each day, the categories and the merchants with the largest totals.

## Before you start

You must have these items:

- An iPhone with iOS 26 or a newer version. WalletFeed is available only in the US.
- WalletFeed. You can use **Spending** without [WalletFeed Pro](/docs/walletfeed-pro/).
- An iPhone that can use Apple Intelligence, with Apple Intelligence turned on. This is necessary only to see a different month.

## Step 1: Give WalletFeed access to your Apple Card

If WalletFeed shows your transactions, go to [Step 2](#step-2-read-the-total-for-this-month).

1. On your iPhone, open WalletFeed.
2. If WalletFeed shows **Welcome to WalletFeed**, tap **Continue**.

   ![The Welcome to WalletFeed screen with the Continue button at the bottom.](app:docs-welcome)

3. If WalletFeed shows **No Cards**, tap **Choose Accounts**.
4. When iOS shows your Wallet accounts, make sure that your Apple Card is on.

   ![The Share Wallet Data screen with Apple Card, Apple Cash and Savings turned on.](app:docs-wallet-access)

5. Tap **Share**.

WalletFeed can read only the accounts that you share. You can change the accounts later in the Settings app, in **Privacy & Security** › **Wallet** › **WalletFeed**.

## Step 2: Read the total for this month

1. Tap **Spending** at the bottom of the screen.

   ![The Spending screen with the October total of $1,317.68, a chart with a bar for each day and the top of Categories.](app:02-spending)

2. To see the total for one day, touch the chart and move your finger to that day.

   **Spending** shows the date and the total for that day.

The top part of **Spending** shows these items:

- The name of the month and the total of your purchases in this month.
- An arrow and the change from the same time last month, for example "70% vs Sep".
- A chart with a bar for each day of the month. The line with the label "Avg $45" shows the average for each day, from the first day of the month to today.
- The Monthly Summary, a short text below the chart.

WalletFeed compares this month with the same days of last month. For example, on October 20, it compares October 1 to 20 with September 1 to 20.

If your iPhone can use Apple Intelligence, Apple Intelligence writes the Monthly Summary from the results that WalletFeed calculates. WalletFeed does not examine the text that Apple Intelligence writes. Without Apple Intelligence, WalletFeed writes the Monthly Summary. It usually gives the total and the change from last month.

To get the Monthly Summary from WalletFeed on an iPhone with Apple Intelligence, do these steps:

1. Tap **Settings** (the gear button) at the top of the screen.
2. In **Privacy & Security**, turn off **Summarize Spending**.

   ![Settings with Summarize Spending turned on in the Privacy & Security section.](app:docs-settings-2)

The Spending widget shows the total for this month and the total at the same time last month. You can put the widget on the Home Screen or the Lock Screen.

## Step 3: See the categories and the merchants

1. On **Spending**, scroll down to **Categories**.

   **Categories** shows a bar with one color for each category. Below the bar, each row shows a category and its total for this month.

2. Scroll down to **Merchants**.

   **Merchants** shows the five merchants with the largest totals this month.

   ![Spending with Other at the bottom of Categories, then Recurring Charges and Merchants.](app:05-recurring)

In **Categories**, WalletFeed shows your five largest categories, then **Other**. **Other** is the total of the remaining categories and of the transactions without a category. Between **Categories** and **Merchants**, **Spending** can also show **Recurring Charges** and **Monthly Installments**.

## Step 4: See a different month

If your iPhone can use Apple Intelligence, with Apple Intelligence turned on, **Spending** has the field **Ask about your spending** at the top. The name of this feature is [Ask Spending](/docs/ask-spending/). Without Apple Intelligence, **Spending** shows only this month.

1. Tap **Ask about your spending**.
2. Type what you want to see, for example `Spending by category last month`.
3. Tap **Go** on the keyboard.

   The result has a chart with a bar for each category. Below the chart, WalletFeed shows **Categories**, **Merchants** and the transactions.

4. To see one category, type the category and a period, for example `Dining this month vs last`.
5. Tap **Go**.

   ![The result for Dining this month vs last, with 9 transactions, a total of $188.70 and a line chart of this month and last month.](app:01-ask-spending)

6. To see this month again, tap **Clear** (the x button) in the field.

Above the result, WalletFeed shows how it read your text, for example "Dining · This month · vs last month". When no result shows, WalletFeed shows an example below the field. If you tap the example, WalletFeed puts its text in the field.

You can type a period, for example `today`, `this week`, `last 30 days`, `last month`, `last 3 months`, `this year` or the name of a month. To compare with last month, you can add `vs last month`.

Apple Intelligence operates on your iPhone. When it reads what you type, it gets only that text. WalletFeed calculates the totals, the charts and the lists. Apple Intelligence then writes the short text below the chart from the results that WalletFeed calculates.

## See the transactions in a category

1. Tap **Search** at the bottom of the screen.
2. In **Categories**, tap a category.

   Search puts the name of the category in the search field and shows the transactions that it finds, by month. Search looks at all the transactions that you share.

3. If your iPhone can use Apple Intelligence, type a category and a period, for example `Groceries last month`.
4. Tap **Search** on the keyboard.

   Above the transactions, Search shows the number of transactions and their total.

   ![Search with the result Groceries · Over $50.00 · Last 30 days, 4 transactions and a total of $277.57.](app:04-search)

## Categories and totals

WalletFeed sets the category of each transaction from its merchant category code (MCC). Wallet supplies the MCC with the transaction. If a transaction has no MCC, or an MCC that WalletFeed does not know, its category is **Other**.

WalletFeed uses these categories:

- **Groceries**
- **Dining**
- **Transport**
- **Fuel**
- **Travel**
- **Shopping**
- **Entertainment**
- **Subscriptions**
- **Utilities**
- **Health**
- **Services**
- **Cash & Transfers**
- **Other**

These rules apply to all the totals in **Spending**:

- WalletFeed adds purchases and fees, and subtracts refunds.
- Transfers and payments are not in the totals.
- Pending purchases are in the totals. Declined purchases are not.
- The totals include the purchases from all the Wallet accounts that you share, for example Apple Cash.

WalletFeed reads your transactions from Wallet on your iPhone when it shows **Spending**. It does not keep a copy of them.

## If something goes wrong

### If Spending shows "Wallet Access Off"

WalletFeed does not have access to Wallet. After the first time, you can give access only in the Settings app.

1. On your iPhone, open the Settings app.
2. Go to **Privacy & Security** › **Wallet**.
3. Give WalletFeed access to your Apple Card.

### If Spending shows "No Spending"

WalletFeed found no purchases for this month in the accounts that you share. This can occur on the first days of a month.

1. If your iPhone can use Apple Intelligence, type `Spending by category last month` in **Ask about your spending**.
2. Tap **Go**.
3. To share more Wallet accounts, go to **Privacy & Security** › **Wallet** in the Settings app.

### If Spending shows "Couldn't Read Wallet"

WalletFeed did not get your transactions from Wallet. In **Ask about your spending**, the same problem shows as "Couldn't read Wallet. Pull down to try again."

1. Pull down on **Spending**.

WalletFeed then reads Wallet again.

### If Spending does not show "Ask about your spending"

This field shows only on an iPhone that can use Apple Intelligence, with Apple Intelligence turned on.

1. Make sure that your iPhone can use Apple Intelligence.
2. In the Settings app on your iPhone, turn on Apple Intelligence.

Without Apple Intelligence, **Spending** shows this month. **Search** shows the transactions in a category.

### If WalletFeed shows "Couldn't read this."

WalletFeed could not read your text, or WalletFeed cannot show that result. WalletFeed cannot show these results:

- Two categories compared with each other, for example `Dining vs Groceries`.
- A result that does not include a category or a merchant, for example `not Uber` or `except Dining`.
- Two limits for a purchase, for example `over $20 and under $50`.

To get a result, do these steps:

1. Type a shorter text with one category and one period, for example `Travel this year`.
2. Tap **Go**.

### If a previous month shows no transactions

Wallet shares the history of an account only from the date that you selected when you gave access.

1. On your iPhone, open the Settings app.
2. Go to **Privacy & Security** › **Wallet** › **WalletFeed**.
3. Share more of the history of your Apple Card.
