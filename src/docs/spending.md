+++
title = "Spending"
nav_title = "Spending"
description = "Spending in WalletFeed shows your Apple Card and Apple Cash purchases this month, your account balances and the totals by day, category and merchant."
order = 40
related = ["docs/ask-spending", "docs/recurring-charges"]
updated = 2026-11-24
+++

On your iPhone, Spending in WalletFeed shows the total of your Apple Card and Apple Cash purchases for this month. It also shows a bar for each day and the balances of your accounts. It shows your largest categories and merchants, and the charges that occur each month or each week. You can use Spending without [WalletFeed Pro](/docs/walletfeed-pro/).

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
- Below the total, if there are some, the pending purchases (for example, "Includes $84.00 pending") and the refunds (for example, "After $42.00 in refunds")
- A chart with one bar for each day of the month
- The Monthly Summary, below the chart
- **Other Currencies**, if you bought items in a different currency this month. It shows the total of these purchases in your currency and the currency codes (for example, "EUR, GBP").

An up arrow shows that the total increased, and a down arrow shows that it decreased. On the chart, the line with the label "Avg" shows the average for one day (for example, "Avg $45").

The total includes pending purchases. Refunds decrease the total. Transfers, bill payments and declined transactions are not in the total.

WalletFeed compares this month with the same days and time of the month before this month. For example, on October 15 at 2:00 PM, WalletFeed compares the total for October with the total from September 1 to September 15 at 2:00 PM. Spending shows the change only if the total for these days of the month before this month is more than zero.

The average is the total for this month divided by the number of days from the first day of the month to this day.

## Show the total for one day

1. On the chart, put your finger on the bar for a day.

   Result: The top of the section shows the date and the total for that day. The other bars become dim. The lines for pending purchases and refunds go away while you show one day.
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

When **Summarize Spending** is off, [Ask Spending](/docs/ask-spending/) and [Monthly Recap](#activate-monthly-recap) also show facts from WalletFeed.

To start the Monthly Summary from Apple Intelligence again, set the **Summarize Spending** switch to on.

> **Note:** On the large screen of iPhone Duo, when you hold it sideways, Spending shows two columns. Ask Spending, the month, **Accounts** and **Categories** are on the left. **Recurring Charges**, **Monthly Installments** and **Merchants** are on the right.

## Accounts

The **Accounts** section is below the section for the month. It shows the balance of each account that you give WalletFeed access to. Spending shows this section also when you have no purchases this month.

For Apple Card, the section shows these items:

- The name of the card. If Wallet gives the date that you opened the card, the date is below the name (for example, "Since Mar 2021").
- **Balance**: the amount that you owe, with the pending transactions, as Wallet shows it. If Apple owes you money, "In credit" is below the amount. Below the balance, a line shows the balance for about the last three months.
- **Available Credit**: the credit that you can use, as Wallet shows it. This is your credit limit minus the balance. Below the amount is your credit limit (for example, "of $8,000 limit"). A bar shows the part of your credit limit that you use.
- **Minimum Payment**: the minimum amount of your next payment. Below the amount is the date that the payment is due (for example, "Due Nov 30"). Spending shows the date only while a payment is due. If Wallet gives only the date, Spending shows **Payment Due** and the date. If no payment is due, **Minimum Payment** shows the figure from Wallet and no date.
- **Overdue**: the amount of a payment that is late. Spending shows this item only if a payment is late.
- **Interest This Year**: the interest that Apple charged on your card since January 1.
- **Fees This Year**: the fees that Apple charged on your card since January 1.

For Apple Cash and Savings, the section shows the name and the balance. For Savings, the section also shows a line that shows the balance for about the last three months.

If an account got interest since January 1, the section shows **Interest Earned** with "This year" below it.

The last row of the section is **Tax Pack**. It opens [Tax Pack](/docs/tax-pack/), which gives the totals of a year for each account.

If you bought items with two or more accounts this month, the section shows the amount for each account below its name (for example, "Spent $1,180.00 this month").

Spending shows an item only if Wallet gives it. Spending shows **Interest This Year**, **Fees This Year**, **Interest Earned** and the amount for each account only if the amount is more than zero. Spending shows the line for the balance only if Wallet has balances for 5 or more days.

Spending reads the balances from Wallet each time that it opens. For the [Spending widget](/docs/spending-widget/), WalletFeed keeps only your Apple Card balance and the payment due date. To read them again, swipe down on Spending.

## Activate Monthly Recap

Monthly Recap sends you one notification each month about your purchases in the month before. You can use Monthly Recap without WalletFeed Pro. Monthly Recap is off until you set it to on.

1. On your iPhone, open WalletFeed.
2. Tap **Settings** (the gear button) at the top of the screen.
3. In the **Notifications** section, set the **Monthly Recap** switch to on.
4. If iOS shows a message about notifications, tap **Allow**.

   If you do not let WalletFeed send notifications, the switch stays off.
5. Tap **Done**.

If you set notifications for WalletFeed to off in the iOS Settings app, the switch stays on, but you do not get notifications. For the steps to set them to on again, refer to [If WalletFeed shows "Notifications are off for WalletFeed."](/docs/troubleshooting/#if-walletfeed-shows-notifications-are-off-for-walletfeed).

If you set the switch to on after the 2nd day of a month, WalletFeed sends the notification for the month before at that time.

## The Monthly Recap notification

WalletFeed sends the notification about a month on the 3rd day of the next month. Thus, most pending purchases of that month are complete before WalletFeed calculates the total.

The title of the notification has the name of the month, for example "October Recap". The text gives these facts:

- The total of your purchases in the month
- The change from the month before that month, in percent
- The category with the largest total.

An example of the text is "You spent $2,340, 12% less than in September. Dining led, at $480." WalletFeed calculates the total as Spending does. Refunds decrease the total. Transfers, bill payments and declined transactions are not in the total.

If Apple Intelligence is active on your iPhone and **Summarize Spending** is on, Apple Intelligence writes the text of the notification. It uses the totals and the categories that WalletFeed calculates. It does not get the names of your merchants.

> **Note:** Apple Intelligence can write an incorrect value in the notification. The values on Spending are correct.

WalletFeed sends the notification when you open it, or when iOS starts WalletFeed after a change in Wallet. Thus, the notification can come after the 3rd day. **Background Sync** is not necessary for this notification.

WalletFeed sends only one notification for each month. It sends no notification for a month without purchases. While **Sample Data** is on, WalletFeed sends no Monthly Recap.

For Monthly Recap, WalletFeed keeps only the month of the last notification (for example, 2026-10). It keeps no amounts. Notification Center keeps the notification until you remove it. When notification previews are off, iOS does not show the text of the notification on the Lock Screen.

## Stop Monthly Recap

1. On your iPhone, open WalletFeed.
2. Tap **Settings** (the gear button) at the top of the screen.
3. In the **Notifications** section, set the **Monthly Recap** switch to off.
4. Tap **Done**.

## Activate Payment Due Reminder

Payment Due Reminder sends you one notification the day before your Apple Card payment is due. You can use Payment Due Reminder without WalletFeed Pro. Payment Due Reminder is off until you set it to on.

1. On your iPhone, open WalletFeed.
2. Tap **Settings** (the gear button) at the top of the screen.
3. In the **Notifications** section, set the **Payment Due Reminder** switch to on.
4. If iOS shows a message about notifications, tap **Allow**.

   If you do not let WalletFeed send notifications, the switch stays off.
5. Tap **Done**.

If you set notifications for WalletFeed to off in the iOS Settings app, the switch stays on, but you do not get notifications. For the steps to set them to on again, refer to [If WalletFeed shows "Notifications are off for WalletFeed."](/docs/troubleshooting/#if-walletfeed-shows-notifications-are-off-for-walletfeed).

## The Payment Due Reminder notification

WalletFeed sends the notification at 9:00 on the day before the payment is due. If you set the switch to on after that time, WalletFeed sends the notification at 9:00 on the due date.

The title of the notification is "Apple Card Payment Due Tomorrow" or "Apple Card Payment Due Today". The text is "You can pay it in Wallet." The notification shows no amount.

The due day is the same day as in **Accounts** and in the Spending widget, in each time zone of your iPhone. Perhaps you set the switch to off and then to on after the notification came. If the notification is still in Notification Center, WalletFeed sends no second notification.

WalletFeed sends one notification for each due date. It sends no notification when Wallet shows no payment due. If Wallet shows no payment due before the notification comes (for example, after Wallet records your payment), WalletFeed removes the notification. While **Sample Data** is on, WalletFeed sends no Payment Due Reminder.

WalletFeed reads the balance and the due date from Wallet when you open WalletFeed. iOS also starts WalletFeed after a change in Wallet.

**Background Sync** is not necessary for this notification.

For Payment Due Reminder, WalletFeed keeps only the switch. iOS keeps the notification until it comes.

## Stop Payment Due Reminder

1. On your iPhone, open WalletFeed.
2. Tap **Settings** (the gear button) at the top of the screen.
3. In the **Notifications** section, set the **Payment Due Reminder** switch to off.
4. Tap **Done**.

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
