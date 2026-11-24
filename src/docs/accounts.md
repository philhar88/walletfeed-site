+++
title = "Account balances and their history"
nav_title = "Accounts"
seo_title = "Apple Card balance history in a chart"
description = "In WalletFeed, the screen of an account shows the balance of your Apple Card, Apple Cash or Savings account in a chart, for one week to one year."
order = 45
related = ["docs/spending", "docs/wallet-accounts", "docs/spending-widget"]
updated = 2026-11-24
+++

In WalletFeed, the screen of an account shows the balance of your Apple Card, Apple Cash or Savings account in a chart. The chart shows a period of one week to one year. You open the screen from the **Accounts** section of [Spending](/docs/spending/). [WalletFeed Pro](/docs/walletfeed-pro/) is not necessary for this screen.

## Open the screen of an account

1. On your iPhone, open WalletFeed.
2. Tap **Spending**.
3. In the **Accounts** section, tap an account, for example Apple Card.

   The screen of the account opens. The title of the screen is the name of the account.

WalletFeed reads the balance records from Wallet each time that you open the screen. To read them again, swipe down on the screen.

## Select a period

At the top of the screen, a control shows five periods. Each period stops today. The screen opens with **3M**.

| Control | Period |
| --- | --- |
| **W** | The last 7 days |
| **M** | The last month |
| **3M** | The last 3 months |
| **6M** | The last 6 months |
| **Y** | The last year |

To change the period, tap a different period in the control.

## Balance and chart

Above the chart, the screen shows these items:

- The name of the period, for example "Past 3 Months"
- The balance of the account today
- A line about the balance in the period.

The line about the balance is one of these texts:

| Text | Condition |
| --- | --- |
| "Low $5,000.00 · High $5,230.00" | The line gives the lowest balance and the highest balance of the period. |
| "Records begin Nov 5, 2026" | The balance records in Wallet start after the first day of the period. |
| "No change" | The balance did not change in the period. |
| "No balance history" | Wallet has no balance records for the account. |

If Apple owes you money on Apple Card, "In credit" is at the start of the line.

The chart shows a line for the balance. The line has a step on each day that the balance changed. At the side of the chart are the lowest balance and the highest balance of the period. The dates are below the chart.

## Show the balance of one day

1. Touch and hold the chart.
2. Move your finger to a day.

   Above the chart, the screen shows the date and the balance of that day. A dot on the line shows the day.

When you lift your finger, the screen shows the period and the balance of today again.

## Details of the account

The **Details** section shows the values that Wallet gives today. These values do not change with the period. For Apple Card, the section shows these items:

- **Available Credit**: the credit that you can use, as Wallet shows it. Below the name is your credit limit (for example, "of $8,000 limit"). If Wallet gives only the limit, the screen shows **Credit Limit**.
- **Minimum Payment**: the minimum amount of your next payment. Below the name is the date that the payment is due (for example, "Due Nov 30"). If Wallet gives only the date, the screen shows **Payment Due** and the date.
- **Overdue**: the amount of a payment that is late. The screen shows this item only if a payment is late.

For each account, the section can also show these items:

- **Spent This Month**: your purchases with this account this month. The screen shows this item only if you bought items with two or more accounts this month.
- **Opened**: the month and the year that you opened the account, if Wallet gives the date.

The **This Year** section shows the amounts since January 1. The screen shows each amount only if it is more than zero.

- **Interest Charged**: the interest that Apple charged on your card.
- **Fees**: the fees that Apple charged on your card.
- **Interest Earned**: the interest that Savings or Apple Cash got.

## Trend

**Trend** is the last section. It gives a short text about the balance in the period. WalletFeed calculates each amount and each date in this text on your iPhone.

If Apple Intelligence is active on your iPhone and **Summarize Spending** is on, Apple Intelligence writes two to four sentences from these amounts and dates. If not, WalletFeed shows two sentences of its own. An example is "Your Apple Card balance is $1,300.00. It's $200.00 lower than on Nov 20."

The Trend tells you the balance and its changes. It does not give advice.

> **Note:** Apple Intelligence can write an incorrect value in the Trend. WalletFeed calculates all other values on the screen.

To stop the text from Apple Intelligence, refer to [Stop the Monthly Summary from Apple Intelligence](/docs/spending/#stop-the-monthly-summary-from-apple-intelligence).

## Limits of the history

The chart has these limits:

- The history starts with the first balance record in Wallet. WalletFeed cannot change the records that Wallet has.
- The chart has one balance for each day. This balance is the last record of the day.
- For Apple Card, WalletFeed calculates a balance in the past from the credit limit of today. Thus, a balance from before a change of your credit limit can be incorrect. Below the chart, the screen shows "Past balances are read against today's credit limit."

## Privacy

WalletFeed reads the balance records from Wallet on your iPhone each time that you open the screen. It does not keep them.

Apple Intelligence writes the Trend on your iPhone. WalletFeed sends nothing to a server.

For more information, refer to the [WalletFeed privacy policy](/privacy/).

## If there is a problem

### If the screen shows "No balance history"

Wallet has no balance records for the account. The screen then shows no chart. The **Details** section continues to show the values from Wallet.

WalletFeed cannot make these records. To read Wallet again, swipe down on the screen.

### If the screen shows "Records begin" and a date

The balance records in Wallet start after the first day of the period. The chart starts on the date in the text.

To show a full period, tap a shorter period in the control, for example **M** or **W**.

### If the screen shows "Couldn't read the balance history. Pull down to try again."

WalletFeed cannot read the balance records from Wallet.

To make WalletFeed read Wallet again, swipe down on the screen.
