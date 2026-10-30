+++
title = "Spending"
nav_title = "Spending"
description = "Spending in WalletFeed shows the total of your Apple Card and Apple Cash purchases this month. It also shows the totals by day, category and merchant."
order = 40
related = ["docs/ask-spending", "docs/recurring-charges"]
updated = 2026-10-30
+++

On your iPhone, Spending in WalletFeed shows the total of your Apple Card and Apple Cash purchases for this month. It also shows a bar for each day, your largest categories and merchants, and the charges that occur each month or each week. You can use Spending without [WalletFeed Pro](/docs/walletfeed-pro/).

## Open Spending

1. On your iPhone, open WalletFeed.
2. At the bottom of the screen, tap **Spending**.

   ![Spending with the October total of $1,317.68, a chart with a bar for each day, and the Monthly Summary.](app:02-spending)

   Result: WalletFeed reads your transactions from Wallet. Then Spending shows the total and the chart for this month.

WalletFeed calculates the values for Spending on your iPhone and does not keep your transactions.

If Spending does not show a total, refer to [If there is a problem](#if-there-is-a-problem).

## The total for this month

The section for the month shows these items:

- The name of the month
- The change from the total at the same day and time of the month before this month (for example, "70% VS SEP" with an up arrow)
- The total for this month
- A chart with one bar for each day of the month
- The Monthly Summary, below the chart.

An up arrow shows that the total increased, and a down arrow shows that it decreased. On the chart, the line with the label "Avg" shows the average for one day (for example, "Avg $45").

The total includes pending purchases. Refunds decrease the total. Transfers, bill payments and declined transactions are not in the total.

WalletFeed compares this month with the same days and time of the month before this month. For example, on October 15 at 2:00 PM, WalletFeed compares the total for October with the total from September 1 to September 15 at 2:00 PM. Spending shows the change only if the total for these days of the month before this month is more than zero.

The average is the total for this month divided by the number of days from the first day of the month to this day.

## Show the total for one day

1. On the chart, put your finger on the bar for a day.

   Result: The top of the section shows the date and the total for that day. The other bars become dim.
2. To show the total for a different day, move your finger to the bar for that day.

## Monthly Summary

The Monthly Summary is below the chart. It gives facts about your purchases this month.

If Apple Intelligence is active on your iPhone and **Summarize Spending** is on, Apple Intelligence writes the Monthly Summary. Apple Intelligence uses facts that WalletFeed calculates (for example, the total and your largest purchase). A Monthly Summary from Apple Intelligence has the Apple Intelligence icon.

> **Note:** Apple Intelligence can write an incorrect value in the Monthly Summary. WalletFeed calculates all other values on Spending.

Apple Intelligence operates on your iPhone. WalletFeed does not send your transactions to a server for the Monthly Summary.

In each of these conditions, the Monthly Summary shows a light bulb icon and the first two facts that WalletFeed calculates:

- Apple Intelligence is not available on your iPhone.
- **Summarize Spending** is off in **Settings**.
- Apple Intelligence cannot write the Monthly Summary.

An example of the two facts is "You've spent $1,318 so far this month. That's 70% more than at this point last month."

## Stop the Monthly Summary from Apple Intelligence

**Settings** shows **Summarize Spending** only when Apple Intelligence is available on your iPhone.

1. At the top of Spending, tap **Settings** (the gear button).
2. Scroll to **Privacy & Security**.
3. Set the **Summarize Spending** switch to off.

   ![Settings with Summarize Spending set to on in the Privacy & Security section.](app:docs-settings-2)

   Result: The Monthly Summary shows the two facts from WalletFeed.
4. Tap **Done**.

When **Summarize Spending** is off, [Ask Spending](/docs/ask-spending/) also shows two facts from WalletFeed.

To start the Monthly Summary from Apple Intelligence again, set the **Summarize Spending** switch to on.

## Categories and merchants

The **Categories** section shows the five categories with the largest totals this month. **Other** shows the total of all other categories. At the top of the section, a bar shows each category in a different color. The length of each color shows the part of the total for that category.

The **Merchants** section, at the bottom of Spending, shows the five merchants with the largest totals this month.

## Recurring Charges

The **Recurring Charges** section shows charges that occur again each month or each week (for example, subscriptions). Spending shows this section only when WalletFeed finds one or more of these charges. For each charge, the section shows the name, **Monthly** or **Weekly**, and the value of the last charge.

To find these charges, WalletFeed reads the transactions from this month and the two months before this month. Apple Intelligence can give each charge a type and a name that is easy to read. For example, "NETFLIX.COM 866-579" becomes "Netflix", and its type is "Streaming". When Apple Intelligence gives these names, the section shows "Apple Intelligence suggested these names."

![Recurring Charges with three monthly charges, and Merchants with five merchants.](app:05-recurring)

For more information, refer to [Recurring Charges](/docs/recurring-charges/).

## Monthly Installments

If you have Apple Card Monthly Installments, the **Monthly Installments** section shows your installment charges. The section shows the charges from the month of the last installment charge. The largest charge is first. For each charge, the section shows the name, the date (for example, "Sep 30") and the value.

Each installment charge has the date of the last day of a month. Thus, until the last day of this month, the section shows the charges from the month before this month. **Recurring Charges** does not show installment charges.

Wallet does not give WalletFeed the remaining payments or the remaining balance. Thus, the section does not show them.

## Use Ask Spending

If Apple Intelligence is available on your iPhone, Spending shows **Ask about your spending** at the top of the screen.

1. Tap **Ask about your spending**.
2. Type the transactions that you want to see (for example, "Dining this month vs last").
3. Tap **Go** on the keyboard.

   ![Spending with "Dining this month vs last" in the field, a total of $188.70 and a chart with the lines "This month" and "Last month".](app:01-ask-spending)

   Result: Spending shows the total, the chart, the categories and the transactions for the text that you typed.
4. To show the total for this month again, tap **Clear** (the x button).

For more information, refer to [Ask Spending](/docs/ask-spending/).

## Show new transactions

To show new transactions on Spending, swipe down on the screen.

## If there is a problem

### If Spending shows "No Cards"

You did not select Wallet accounts for WalletFeed.

1. Tap **Choose Accounts**.

   Result: iOS shows the Wallet access screen.
2. Select the accounts that WalletFeed reads.
3. For each account, select the start date.
4. Tap **Share**.

For more information, refer to [Wallet accounts](/docs/wallet-accounts/).

### If Spending shows "Wallet Access Off"

You did not let WalletFeed read Wallet, or you stopped its access to Wallet in the Settings app.

1. On your iPhone, open the Settings app.
2. Tap **Privacy & Security** › **Wallet** › **WalletFeed**.
3. Select the accounts that WalletFeed reads.
4. Open WalletFeed again.

### If Spending shows "No Spending"

The Wallet accounts that WalletFeed can read have no purchases this month, or the total for this month is zero or less than zero. For the transactions in the total, refer to [The total for this month](#the-total-for-this-month).

If Spending does not include a Wallet account, refer to [Wallet accounts](/docs/wallet-accounts/).

### If Spending shows "Couldn't Read Wallet"

WalletFeed cannot read your transactions from Wallet.

To make WalletFeed read Wallet again, swipe down on the screen.
