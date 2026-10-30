# Recurring Charges and alerts

WalletFeed finds the recurring charges on your Apple Card, such as subscriptions and bills, and shows them on the [Spending](/docs/spending/) screen. Recurring Charge Alerts can send you a notification when a new recurring charge starts, or when the price of a recurring charge changes.

[WalletFeed Pro](/docs/walletfeed-pro/) is not necessary for Recurring Charges or for Recurring Charge Alerts.

## Find your recurring charges

1. On your iPhone, open WalletFeed.
2. Tap **Spending**.
3. Scroll to **Recurring Charges**.

   ![The Recurring Charges section of the Spending screen shows PG&E, Netflix and Spotify, with the price of each charge.](https://walletfeed.app/docs/recurring-charges/walletfeed-recurring.webp)

Each row in the list shows these items:

- An icon for the category of the charge
- The name of the charge
- The word **Monthly** or **Weekly**
- The price of the last charge.

With Apple Intelligence, the row can show the type of service before **Monthly** or **Weekly**, for example **Streaming · Monthly**.

The first charge in the list has the largest total for one month. For a **Weekly** charge, this total is approximately 4.3 times the price of the last charge.

If WalletFeed finds no recurring charges, **Spending** does not show the **Recurring Charges** section.

## Rules for a recurring charge

WalletFeed reads your transactions from this month and from the two months before it. WalletFeed puts the charges from one merchant in **Recurring Charges** in these conditions:

- All the charges have the same merchant name. For example, “Netflix.com” and “NETFLIX.COM” are the same merchant.
- The price of each charge is not more than 15% different from the price of the last charge.
- For **Monthly**, there are two or more charges. Each charge is 26 to 35 days after the charge before it.
- For **Weekly**, there are three or more charges. Each charge is 6 to 8 days after the charge before it.

For example, if a month between two charges has no charge from the merchant, **Recurring Charges** does not show the merchant.

These transactions are not in **Recurring Charges**:

- Refunds, transfers, bill payments and declined transactions
- Apple Card Monthly Installments (**Spending** shows them in the **Monthly Installments** section)
- Charges that occur each year (WalletFeed finds only **Monthly** and **Weekly** charges).

## Names from Apple Intelligence

For names from Apple Intelligence, you must have an iPhone that can use Apple Intelligence. Apple Intelligence must be active on that iPhone.

Wallet can show a merchant name such as “NETFLIX.COM 866-579”. With Apple Intelligence, WalletFeed shows a short name, such as Netflix. WalletFeed can also show a type of service, such as **Streaming**. When the list has names from Apple Intelligence, WalletFeed shows **Apple Intelligence suggested these names.** below the list.

WalletFeed uses a name only if the first word of the name is in the merchant name from Wallet. WalletFeed gets names for only the first 12 charges in the list. If a charge has no name from Apple Intelligence, the row shows the merchant name from Wallet.

## Activate Recurring Charge Alerts

1. On your iPhone, open WalletFeed.
2. Tap **Settings** (the gear button) at the top of the screen.
3. In the **Notifications** section, set the **Recurring Charge Alerts** switch to on.

   ![The WalletFeed Settings screen with the Recurring Charge Alerts switch in the Notifications section.](https://walletfeed.app/docs/recurring-charges/walletfeed-settings.webp)

4. If iOS shows a message about notifications, tap **Allow**.

   If you do not let WalletFeed send notifications, the switch stays off.

5. Tap **Done**.

When you set the **Recurring Charge Alerts** switch to on, WalletFeed sends no notifications for the charges that are in Wallet at that time. You get notifications only for new charges.

## Notifications for recurring charges

WalletFeed sends a notification for these changes:

| Change | Title of the notification | Text of the notification |
|---|---|---|
| A charge becomes a recurring charge | “Netflix repeats monthly” or “Netflix repeats weekly” | “$15.49 each month” or “$15.49 each week” |
| The price of a recurring charge increases | “Netflix costs more” | “$17.99, up from $15.49” |
| The price of a recurring charge decreases | “Netflix costs less” | “$15.49, down from $17.99” |

WalletFeed sends a notification about a price change only in these conditions:

- The charges from the merchant were in **Recurring Charges** before the new charge.
- The new charge is 26 to 35 days after the charge before it (6 to 8 days for a **Weekly** charge).
- The new price is more than 2% different from the price before it.

After a price change of more than 15%, WalletFeed can remove the charge from **Recurring Charges**. WalletFeed shows the charge again when each price in the three months that WalletFeed reads is not more than 15% different from the new price.

WalletFeed sends a notification only for a charge from the last 7 days. It sends only one notification for each charge. The notification uses the name from Apple Intelligence. If the charge has no name from Apple Intelligence, the notification uses the merchant name from Wallet.

When you open WalletFeed, it reads your transactions and sends the new notifications. When WalletFeed is not open, iOS starts WalletFeed approximately 1 hour or less after a change in Wallet. **Background Sync** is not necessary for these notifications.

## Stop Recurring Charge Alerts

1. On your iPhone, open WalletFeed.
2. Tap **Settings** (the gear button) at the top of the screen.
3. In the **Notifications** section, set the **Recurring Charge Alerts** switch to off.
4. Tap **Done**.

## Privacy

WalletFeed finds your recurring charges on your iPhone. Each time that it does this, it reads your transactions from Wallet. WalletFeed does not keep a copy of your transactions.

To give names to the charges, Apple Intelligence gets only the merchant names. Apple Intelligence makes the names on your iPhone. WalletFeed sends nothing to a server.

For Recurring Charge Alerts, WalletFeed keeps only transaction IDs. It keeps no prices and no merchant names.

A notification shows the name of the charge and its prices. Notification Center keeps the notification until you remove it. When notification previews are off, iOS does not show the text of the notification on the Lock Screen.

For more information, refer to the [WalletFeed privacy policy](/privacy/).

## If there is a problem

### If a new subscription is not in Recurring Charges

WalletFeed shows a **Monthly** charge only after the second charge from the merchant. It shows a **Weekly** charge only after the third charge.

1. When Wallet shows the next charge from the merchant, open WalletFeed.
2. Tap **Spending**.
3. If **Recurring Charges** does not show the charge, refer to [Rules for a recurring charge](#rules-for-a-recurring-charge).

### If the Recurring Charge Alerts switch does not stay on

iOS does not let WalletFeed send notifications.

1. On your iPhone, open the Settings app.
2. Tap **Notifications** › **WalletFeed**.
3. Set the **Allow Notifications** switch to on.
4. Open WalletFeed.
5. Tap **Settings** (the gear button) at the top of the screen.
6. In the **Notifications** section, set the **Recurring Charge Alerts** switch to on.

### If you get no notification

WalletFeed sends a notification only for a new recurring charge or a price change from the last 7 days.

1. On your iPhone, open WalletFeed.
2. Tap **Settings** (the gear button) at the top of the screen.
3. Make sure that the **Recurring Charge Alerts** switch is on.
4. If the switch is on, open the Settings app on your iPhone.
5. Tap **Notifications** › **WalletFeed**.
6. Make sure that the **Allow Notifications** switch is on.
