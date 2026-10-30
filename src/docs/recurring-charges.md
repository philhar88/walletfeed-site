+++
title = "Recurring Charges and alerts"
nav_title = "Recurring Charges"
description = "WalletFeed finds the recurring charges on your Apple Card, such as subscriptions, and can send a notification when a new one starts or a price changes."
order = 70
related = ["docs/spending", "guides/find-apple-card-subscriptions"]
updated = 2026-10-30
+++

WalletFeed finds the recurring charges on your Apple Card, such as subscriptions and monthly bills, and shows them on the [Spending](/docs/spending/) screen. Recurring Charge Alerts can send you a notification when a new recurring charge starts or a price changes.

[WalletFeed Pro](/docs/walletfeed-pro/) is not necessary for Recurring Charges or for Recurring Charge Alerts.

## Find your recurring charges

1. On your iPhone, open WalletFeed.
2. Tap **Spending**.
3. Scroll down to **Recurring Charges**.

   ![The Recurring Charges section of the Spending screen, with PG&E, Netflix and Spotify and the price of each charge.](app:05-recurring)

Each row shows these items:

- An icon for the category of the charge.
- The name of the charge.
- The word **Monthly** or **Weekly**. With Apple Intelligence, the type of service comes first, for example **Streaming · Monthly**.
- The price of the last charge.

The first charge in the list has the largest total for one month. For a weekly charge, this total is approximately 4.3 times the weekly price.

If WalletFeed finds no recurring charges, the **Recurring Charges** section does not show.

## Rules for a recurring charge

WalletFeed reads your purchases from this month and from the two months before it. It puts the charges from one merchant in **Recurring Charges** when they agree with these rules:

- All the charges have the same merchant name. For example, “Netflix.com” and “NETFLIX.COM” are the same merchant.
- The difference between the price of each charge and the price of the last charge is 15% or less.
- For **Monthly**, there is a minimum of two charges. Each charge is 26 to 35 days after the charge before it.
- For **Weekly**, there is a minimum of three charges. Each charge is 6 to 8 days after the charge before it.

For example, if a month between two charges has no charge from the merchant, the merchant does not show in the list.

These transactions are not in **Recurring Charges**:

- Refunds, transfers, bill payments and rejected transactions.
- Apple Card Monthly Installments. **Spending** shows them in the **Monthly Installments** section.
- Charges that occur each year. WalletFeed finds only monthly and weekly charges.

## Names from Apple Intelligence

Wallet can show a merchant name such as “NETFLIX.COM 866-579”. With Apple Intelligence, WalletFeed shows a short name, such as Netflix. It can also show a type of service, such as Streaming. Below the list, WalletFeed then shows **Apple Intelligence suggested these names.**

WalletFeed uses a name only if the first word of the name is in the merchant name from Wallet. It gets names for the first 12 charges in the list only. If a charge has no name from Apple Intelligence, the row shows the merchant name from Wallet.

For these names, you must have an iPhone that is compatible with Apple Intelligence, and Apple Intelligence must be on.

## Start Recurring Charge Alerts

1. On your iPhone, open WalletFeed.
2. Tap **Settings** (the gear button) at the top of the screen.
3. In **Notifications**, set the **Recurring Charge Alerts** switch to on.

   ![WalletFeed Settings with the Recurring Charge Alerts switch in the Notifications section.](app:docs-settings)

4. If iOS shows a message about notifications, let WalletFeed send them.

   If you do not let WalletFeed send notifications, the switch stays off.

5. Tap **Done**.

When you set the switch to on, WalletFeed sends no notifications for the charges that are in Wallet at that time. You get notifications only for new charges.

## Notifications for recurring charges

WalletFeed sends a notification for these changes:

| Change | Title of the notification | Text of the notification |
|---|---|---|
| A charge becomes a recurring charge | “Netflix repeats monthly” or “Netflix repeats weekly” | “$15.49 each month” or “$15.49 each week” |
| The price of a recurring charge increases | “Netflix costs more” | “$17.99, up from $15.49” |
| The price of a recurring charge decreases | “Netflix costs less” | “$15.49, down from $17.99” |

WalletFeed sends a notification about a price change only in these conditions:

- The charges from the merchant were in **Recurring Charges** before the new charge.
- The new charge comes at the usual time. This is 26 to 35 days after the charge before it, or 6 to 8 days for a weekly charge.
- The new price is more than 2% different from the price before it.

After a price change of more than 15%, the charge can go out of **Recurring Charges**. It comes back when all the charges in the three months have the new price.

WalletFeed sends a notification only for a charge from the last 7 days, and only one notification for each charge. The notification uses the name from Apple Intelligence if it is available. If not, it uses the merchant name from Wallet.

WalletFeed examines your transactions when you open it. When WalletFeed is closed, iOS starts WalletFeed in approximately 1 hour or less after a change in Wallet. WalletFeed Pro and **Background Sync** are not necessary for this.

## Stop Recurring Charge Alerts

1. In WalletFeed, tap **Settings** (the gear button) at the top of the screen.
2. In **Notifications**, set the **Recurring Charge Alerts** switch to off.
3. Tap **Done**.

## Privacy

WalletFeed finds your recurring charges on your iPhone. It reads your transactions from Wallet each time, and it does not keep a copy.

To give names to the charges, Apple Intelligence gets only the merchant names. It runs on your iPhone, and WalletFeed sends nothing to a server.

For Recurring Charge Alerts, WalletFeed keeps only the IDs of the transactions that it sent a notification for. It keeps no prices and no merchant names.

A notification shows the name of the charge and its prices. Notification Center keeps the notification until you remove it. When notification previews are off, iOS does not show the text on the Lock Screen.

For more information, refer to the [WalletFeed privacy policy](/privacy/).

## If something goes wrong

### If a new subscription is not in Recurring Charges

WalletFeed shows a monthly charge only after its second charge, and a weekly charge only after its third charge.

After the next charge from the merchant, open **Spending** again. If the list does not show the charge after that, refer to [Rules for a recurring charge](#rules-for-a-recurring-charge).

### If the switch does not stay on

iOS does not let WalletFeed send notifications.

1. In the Settings app on your iPhone, let WalletFeed send notifications.
2. In WalletFeed, set the **Recurring Charge Alerts** switch to on again.

### If no notification comes

WalletFeed sends a notification only for a new recurring charge or a price change from the last 7 days.

1. In WalletFeed, tap **Settings** (the gear button) at the top of the screen.
2. Make sure that the **Recurring Charge Alerts** switch is on.
