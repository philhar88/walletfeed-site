# Add an Apple Card spending widget

The WalletFeed [Spending widget](/docs/spending-widget/) shows your Apple Card spending for this month on the Home Screen or the Lock Screen of your iPhone. It compares this total with the same day and time last month, and you can use it without [WalletFeed Pro](/docs/walletfeed-pro/).

## Before you start

- An iPhone with iOS 26 or a newer version. WalletFeed is available only in the US.
- Your Apple Card, Apple Cash or Savings account in Wallet on your iPhone.
- WalletFeed, from the App Store.

WalletFeed Pro and destinations are not necessary for the widget.

## Step 1: Give WalletFeed access to Wallet

The widget shows totals only after WalletFeed gets [access to your Wallet accounts](/docs/wallet-accounts/) and reads your transactions. If WalletFeed shows your transactions, go to Step 2.

1. On your iPhone, open WalletFeed.
2. If WalletFeed shows **Welcome to WalletFeed**, tap **Continue**.

   ![The Welcome to WalletFeed screen with the Continue button at the bottom.](https://walletfeed.app/guides/apple-card-spending-widget/walletfeed-welcome.webp)

3. For each account to include, set the switch to on.

   ![The Share Wallet Data screen with switches for Apple Card, Apple Cash and Savings, and the Share button.](https://walletfeed.app/guides/apple-card-spending-widget/walletfeed-wallet-access.webp)

4. Tap **Share**.

WalletFeed then reads your transactions and calculates the totals for the widget.

## Step 2: Add the widget to the Home Screen

1. On your iPhone, go to the Home Screen page for the widget.
2. Touch and hold an empty area of the screen until the apps move.
3. Tap **Edit** at the top of the screen.
4. Tap **Add Widget**.
5. In the search field, type `WalletFeed`.
6. Tap **WalletFeed**.
7. Swipe to the small or the medium **Spending** widget.
8. Tap **Add Widget**.
9. To move the widget, drag it to a different position.
10. Tap **Done**.

> **Note:** The **Sync Status** widget in the same list shows the status of destinations, which are part of WalletFeed Pro.

## Add the widget to the Lock Screen

On the Lock Screen, the **Spending** widget can be below the time or above it.

1. Push the side button of your iPhone two times.
2. Touch and hold the Lock Screen until **Customize** shows at the bottom of the screen.
3. Tap **Customize**.
4. If iOS shows the Lock Screen and the Home Screen, tap the Lock Screen.
5. Select a position for the widget:
   - For the widget below the time, tap **Add Widgets**, or the widgets that are there.
   - For the one-line widget above the time, tap the date above the time.
6. Tap **WalletFeed**.
7. Tap the **Spending** widget.
8. Tap **Done**.

## Totals in each widget

The **Spending** widgets show these totals:

| Widget | Position | Totals |
| --- | --- | --- |
| Small | Home Screen | The **This Month** total, with the **Same Point Last Month** total below it. |
| Medium | Home Screen | The **This Month** and **Same Point Last Month** totals, and the change from last month, for example “↓ 14% vs Sep”. |
| Rectangular | Lock Screen, below the time | The total for this month and the change from last month. |
| One line | Lock Screen, above the time | The total for this month, for example “$1,234.56 this month”. |

The arrow points down if the **This Month** total is less than the **Same Point Last Month** total. If the **Same Point Last Month** total is 0, the widget does not show the change.

The widget shows the same totals as the [Spending](/docs/spending/) tab in WalletFeed. The total for this month starts on the first day of the month. The total for last month is from the first day of last month to the same day and time last month. Purchases and other charges increase the totals, and refunds decrease them. The totals do not include transfers, payments or declined purchases.

The totals include each account that you gave WalletFeed access to in Step 1. When a new month starts, the widget shows 0 for this month, without the other totals, until WalletFeed updates it.

To see the same totals with a chart for each day:

1. Open WalletFeed.
2. Tap **Spending**.

   ![The Spending tab with the total for October, the change from September and a chart for each day.](https://walletfeed.app/guides/apple-card-spending-widget/walletfeed-spending.webp)

## Widget updates

WalletFeed updates the widget when you open WalletFeed. When WalletFeed is closed, iOS starts WalletFeed in approximately 1 hour or less after a change in Wallet. WalletFeed then updates the widget.

WalletFeed Pro and [Background Sync](/docs/background-sync/) are not necessary for these updates.

## Data in the widget

For the widget, WalletFeed keeps only two totals on your iPhone, with their currency and the time of the update. The widget has no transactions, merchants or categories. iOS also keeps the data that the widget shows.

While your iPhone is locked, iOS can show the widget without the totals and the change.

## Change or remove the widget

To change the accounts in the totals:

1. On your iPhone, open the Settings app.
2. Tap **Privacy & Security**.
3. Tap **Wallet**.
4. Tap **WalletFeed**.
5. For each account, set the switch to on or off.

If you set all the switches to off, WalletFeed clears the totals from the widget the next time that it starts.

To remove the widget from the Home Screen:

1. Touch and hold the widget.
2. Tap **Remove Widget**.
3. If iOS shows a message, tap **Remove**.

To change the small widget to the medium widget, remove it. Then add the medium widget, as in Step 2.

To remove the widget from the Lock Screen:

1. Touch and hold the Lock Screen until **Customize** shows at the bottom of the screen.
2. Tap **Customize**.
3. Tap the widgets below the time.
4. Tap **−** on the **Spending** widget.
5. Tap **Done**.

## If something goes wrong

### If the widget shows “Open WalletFeed to see your spending.”

WalletFeed did not read your transactions in Wallet, or it does not have access to Wallet. The one-line widget shows only “Open WalletFeed”.

1. Open WalletFeed.
2. Tap **Transactions**.

If **Transactions** shows your transactions, WalletFeed updated the widget when it opened. If **Transactions** shows **No Cards**, do these steps:

1. Tap **Choose Accounts**.
2. For each account to include, set the switch to on.
3. Tap **Share**.

If **Transactions** shows **Wallet Access Off**, do the steps in the next section.

### If WalletFeed shows “Wallet Access Off”

WalletFeed does not have access to Wallet, and iOS shows the question about Wallet access only one time.

1. On your iPhone, open the Settings app.
2. Tap **Privacy & Security**.
3. Tap **Wallet**.
4. Tap **WalletFeed**.
5. For each account to include, set the switch to on.
6. Open WalletFeed.

### If the widget does not show a new purchase

WalletFeed did not update the widget after the purchase. When WalletFeed is closed, iOS starts WalletFeed in approximately 1 hour or less after a change in Wallet.

1. Open WalletFeed.
2. Go to the Home Screen.

WalletFeed updates the widget when it opens.

### If the widget shows totals that are not yours

**Sample Data** is on, so the widget shows the totals of the sample transactions.

1. Open WalletFeed.
2. Tap **Settings** (the gear button) at the top of the screen.
3. Set **Sample Data** to off.

WalletFeed then clears the sample totals and calculates your totals from Wallet.
