# Ask Spending with Apple Intelligence

Ask Spending lets you type a question about your Apple Card, Apple Cash and Savings transactions, for example `Dining this month vs last`. Apple Intelligence on your iPhone reads the question. WalletFeed calculates the result and shows it as a chart and a list. Apple Intelligence writes a summary of the result.

## Before you start

You must have these items:

- An iPhone that can use Apple Intelligence, with iOS 26 or a newer version. Apple Intelligence must be on.
- WalletFeed, with [access to your Wallet accounts](/docs/wallet-accounts/). WalletFeed is available only in the US.

[WalletFeed Pro](/docs/walletfeed-pro/) is not necessary for Ask Spending. If Apple Intelligence is not available, [**Spending**](/docs/spending/) shows this month without the question field.

## Type a question

1. On your iPhone, open WalletFeed.
2. Tap **Spending** at the bottom of the screen.
3. Tap the **Ask about your spending** field at the top of the screen.
4. Type a question, for example `Groceries over $50`.

   The question can have a maximum of 200 characters.

5. Tap **Go** on the keyboard.

   While WalletFeed gets the result, a progress indicator shows in the field. Then WalletFeed shows the result below the field.

   ![The result for Dining this month vs last, with 9 transactions, a total of $188.70 and a line chart of this month and last month.](https://walletfeed.app/docs/ask-spending/walletfeed-ask-spending.webp)

6. Optional: To see one day, week or month, move your finger along the chart.

   The top of the result then shows the date and the amount at that point on the chart.

## Use an example

When no result is on the screen, WalletFeed shows an example question below the field. The example starts with "Try". At intervals of 4 seconds, the next example shows. WalletFeed shows only the examples that give a result for your transactions from this month and the two months before this month.

1. Tap the example below the field.

   ![The Spending screen with the empty Ask about your spending field and the example Dining this month vs last below it.](https://walletfeed.app/docs/ask-spending/walletfeed-spending.webp)

   The example then shows in the field.

2. Optional: Change the question.
3. Tap **Go** on the keyboard.

If you do not change the example, WalletFeed reads it without Apple Intelligence.

> **Note:** The example stays the same while you type and while VoiceOver is on. With VoiceOver, the example button has the other examples as actions. With Reduce Motion, the next example shows at intervals of 8 seconds.

## Write a question that WalletFeed can read

A question can contain the items in this table. It can also start with `how much did I spend`.

| Item | Examples |
|---|---|
| A period | `today`, `this week`, `last 30 days`, `September`, `last year` |
| A period to compare with | `vs last month`, `vs last year` |
| A category | `dining`, `groceries`, `travel` |
| A merchant name, or a part of it | `coffee` |
| An amount limit for each transaction | `over $50`, `under $20`, `at least $50` |
| Refunds, money in or recurring charges | `refunds`, `money in`, `subscriptions` |
| A chart type | `by day`, `by week`, `by category`, `by merchant`, `trend` |
| The largest transactions first | `biggest purchases`, `largest purchases` |

WalletFeed uses these rules for periods:

- If the question has no period, WalletFeed uses this month.
- `last month` is the calendar month before this one, and `past month` is the last 30 days. Weeks and years have the same rule. For example, `past year` is the last 12 months.
- For a month name, for example `September`, WalletFeed uses the last September. If this month is September, WalletFeed uses this month.
- WalletFeed compares a period only with the previous period, or with the same period of the previous year.
- If the period has not ended, WalletFeed uses the other period only up to the same day and time. For example, on October 20, `Dining this month vs last` compares October 1 to 20 with September 1 to 20.

If a question contains one of these items, WalletFeed shows "Couldn't read this." below the field:

- A part that removes transactions, for example `except`, `not` or `without`.
- Two amount limits, for example `between $10 and $50`.
- Two types of transactions, for example `refunds and deposits`.
- Two categories or two merchants to compare, for example `dining vs groceries`.
- A period that WalletFeed cannot use, for example `yesterday`, `since March`, `this quarter` or `on Fridays`.
- A question about balances or budgets.

## Read the result

The result shows these items, from top to bottom:

- How WalletFeed read the question, with the Apple Intelligence icon, for example "Dining · This month · vs last month".
- The number of transactions and their total. If you compare two periods, the change also shows, for example "↑ 38% VS SEP". If the other period has a total of zero or less, the change does not show.
- A chart, by day, week, month, category or merchant. If you compare two periods by day, week or month, the chart usually shows the total from the start of each period.
- A summary. If the summary has the Apple Intelligence icon, Apple Intelligence wrote it. This summary can contain an incorrect number. A light bulb icon shows that WalletFeed wrote the summary from the facts that it calculates.
- The **Categories** section, with the five largest categories, and **Other** for the remaining categories. The category totals include refunds, and their sum is the total. If the refunds in a category are more than its purchases, the category total has a plus sign (+).
- The **Merchants** section, with the five merchants that have the largest totals. This section shows only if the result has two or more merchants and the chart does not show merchants. It does not show for recurring charges.
- The transactions, in a section for each month, with the last transaction first. If the question asks for the largest transactions, the **Largest** section shows them, largest first.

If the question is about recurring charges, the [**Recurring Charges**](/docs/recurring-charges/) section shows above **Categories**. If the question also has no period and does not compare two periods, the total is the sum of the charges for one month. The top of the result then shows the number of recurring charges, and the total has "a month" after it.

If no transactions agree with the question, the result shows "0 TRANSACTIONS" and $0.00.

## Change the question

When you change the question, WalletFeed removes the result and shows this month again.

1. Tap **Clear** (the x button) in the field.
2. Type a different question.
3. Tap **Go** on the keyboard.

## Update the result

WalletFeed reads Wallet each time you go back to WalletFeed, and when you pull down on **Spending**. Then WalletFeed calculates the result again from the transactions that it reads. Apple Intelligence does not read the question again.

To update the result now, pull down on **Spending**.

## Set Summarize Spending to off

If you set **Summarize Spending** to off, Apple Intelligence does not write the summary of each result or the Monthly Summary. WalletFeed then shows a light bulb icon and two facts that it calculates. Apple Intelligence continues to read each question that you type.

1. Tap **Settings** (the gear button) at the top of the screen.
2. In **Privacy & Security**, set **Summarize Spending** to off.

   ![Settings with the Privacy & Security section, where Summarize Spending is on.](https://walletfeed.app/docs/ask-spending/walletfeed-settings-2.webp)

3. Tap **Done**.

**Settings** shows **Summarize Spending** only when Apple Intelligence is available on your iPhone.

## Privacy

Apple Intelligence operates on your iPhone. Ask Spending does not send data to a server. To read a question, Apple Intelligence gets only the question. To write a summary, it gets the question and the data that WalletFeed calculates. This data includes your totals, the change between two periods, the categories, the merchants and the largest purchases.

WalletFeed does not keep your questions, results or summaries. For more information, refer to the [WalletFeed privacy policy](/privacy/).

## If there is a problem

### If WalletFeed shows "Couldn't read this."

WalletFeed cannot get a result from the question. The question stays in the field, and an example shows below it.

1. Change the question to use the items in [Write a question that WalletFeed can read](#write-a-question-that-walletfeed-can-read).
2. Tap **Go** on the keyboard.

You can also tap the example below the field.

### If WalletFeed shows "Couldn't read Wallet. Pull down to try again."

WalletFeed did not get the transactions for the result from Wallet. To try again, pull down on **Spending**. WalletFeed then reads Wallet and the question again.

### If Spending does not show "Ask about your spending"

The field shows only if Apple Intelligence is available on your iPhone.

1. Make sure that your iPhone can use Apple Intelligence.

   Apple gives the list of iPhone models in [How to get Apple Intelligence](https://support.apple.com/en-us/121115).

2. In the Settings app, tap **Apple Intelligence & Siri**.
3. Set **Apple Intelligence** to on.

When Apple Intelligence becomes available, **Spending** shows the field.

### If the result shows "0 TRANSACTIONS"

WalletFeed read the question, but no transactions agree with it.

1. Make sure that the text above the result shows the correct period and category.
2. If this text is not correct, change the question.
3. Tap **Go** on the keyboard.

### If the summary has an incorrect number

Apple Intelligence writes the summary from the numbers that WalletFeed calculates. WalletFeed does not examine the summary.

1. Use the total, the chart and the list, because WalletFeed calculates them.
2. To get the summary from WalletFeed, [set Summarize Spending to off](#set-summarize-spending-to-off).
