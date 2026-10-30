+++
title = "Add an Apple Card spending widget"
nav_title = "Spending widget"
seo_title = "Apple Card spending widget for the iPhone Home Screen"
description = "Add an Apple Card spending widget to your iPhone Home Screen or Lock Screen. It shows this month and the month before this month, to the same day and time."
group = "Free features"
order = 40
related = ["docs/spending-widget", "docs/spending"]
updated = 2026-10-30
+++

The WalletFeed [Spending widget](/docs/spending-widget/) shows the total of your Apple Card and Apple Cash charges for this month on the Home Screen or the Lock Screen of your iPhone. It can also show the total for the month before this month, to the same day and time.

## Before you start

You must have these items:

- An iPhone with iOS 26 or a newer version. WalletFeed is available only in the US.
- Your Apple Card, Apple Cash or Savings account in Wallet on your iPhone.
- WalletFeed, from the App Store.

[WalletFeed Pro](/docs/walletfeed-pro/) and destinations are not necessary for the widget.

## Step 1: Give WalletFeed access to Wallet

The widget shows totals only after WalletFeed gets [access to your Wallet accounts](/docs/wallet-accounts/) and reads your transactions. If WalletFeed shows your transactions, WalletFeed has this access. Then you can go to [Step 2](#step-2-add-the-widget-to-the-home-screen). If WalletFeed shows **Wallet Access Off**, the steps are in [If WalletFeed shows “Wallet Access Off”](#if-walletfeed-shows-wallet-access-off).

1. On your iPhone, open WalletFeed.
2. If WalletFeed shows **Welcome to WalletFeed**, tap **Continue**.

   ![The Welcome to WalletFeed screen with the Continue button at the bottom.](app:docs-welcome)

3. If **Transactions** shows **No Cards**, tap **Choose Accounts**.
4. On the **Share Wallet Data** screen, select the accounts that WalletFeed can read.

   ![The Share Wallet Data screen with switches for Apple Card, Apple Cash and Savings, and the Share button.](app:docs-wallet-access)

5. For each account, select the start date.
6. Tap **Share**. WalletFeed then reads your transactions and calculates the totals for the widget.

## Step 2: Add the widget to the Home Screen

1. On your iPhone, go to the Home Screen page where you will put the widget.
2. Touch and hold an empty area of the screen until the apps move.
3. Tap **Edit** at the top of the screen.
4. Tap **Add Widget**.
5. In the search field, type `WalletFeed`.
6. Tap **WalletFeed**.
7. Swipe to the small or the medium **Spending** widget.
8. Tap **Add Widget**.
9. To move the widget, drag it to a different position.
10. Tap **Done**.

> **Note:** When you swipe in step 7, iOS also shows the **Sync Status** widget. This widget shows the status of your destinations. Destinations are part of WalletFeed Pro.

## Add the widget to the Lock Screen

On the Lock Screen, the **Spending** widget can be below the time or above it.

1. If your iPhone shows the Home Screen or an app, push the side button.
2. If iOS does not show the Lock Screen, push the side button.
3. Touch and hold the Lock Screen until iOS shows **Customize** at the bottom of the screen.
4. Tap **Customize**.
5. If iOS shows the Lock Screen and the Home Screen, tap the Lock Screen.
6. To put the rectangular widget below the time, tap **Add Widgets** or the widgets below the time.
7. To put the one-line widget above the time, tap the date above the time.
8. Tap **WalletFeed**.
9. Tap the **Spending** widget.
10. Tap **Done**.

## Totals in each widget

The **Spending** widgets show these totals:

| Widget | Position | Totals |
| --- | --- | --- |
| Small | Home Screen | The **This Month** total, with the **Same Point Last Month** total below it. |
| Medium | Home Screen | The **This Month** and **Same Point Last Month** totals, and the change between the two totals, for example “↓ 14% vs Sep”. |
| Rectangular | Lock Screen, below the time | The total for this month and the change from the **Same Point Last Month** total. |
| One-line | Lock Screen, above the time | The total for this month, for example “$1,234.56 this month”. |

If the **This Month** total is less than the **Same Point Last Month** total, the change has a “↓” arrow. If the **Same Point Last Month** total is 0 or less than 0, the widget does not show the change.

The widget shows the same totals as the [Spending](/docs/spending/) tab in WalletFeed. The totals include each account that you gave WalletFeed access to in [Step 1](#step-1-give-walletfeed-access-to-wallet). The total for this month starts on the first day of the month. The **Same Point Last Month** total is from the first day of the month before this month to the same day and time in that month. Purchases and other charges increase the totals, and refunds decrease them. Transfers, payments and rejected purchases do not change the totals.

When a new month starts, the widget shows 0 for this month. Until WalletFeed updates the widget, the widget does not show the **Same Point Last Month** total or the change.

To look at the same totals in a chart with a bar for each day:

1. Open WalletFeed.
2. Tap **Spending**.

   ![The Spending tab with the total for October, the change from September and a chart with a bar for each day.](app:02-spending)

## Widget updates

WalletFeed updates the widget when you open WalletFeed. When WalletFeed is not open, iOS starts WalletFeed approximately 1 hour or less after a change in Wallet. WalletFeed then updates the widget.

WalletFeed Pro and [Background Sync](/docs/background-sync/) are not necessary for these updates.

## Data in the widget

For the widget, WalletFeed keeps only two totals on your iPhone, with their currency and the time of the update. The widget has no transactions, merchants or categories. iOS keeps a copy of the data that the widget shows.

On a locked iPhone, iOS can show the widget without the totals and the change.

## Change or remove the widget

To change the accounts in the totals:

1. On your iPhone, open the Settings app.
2. Tap **Privacy & Security**.
3. Tap **Wallet**.
4. Tap **WalletFeed**.
5. Select the accounts that WalletFeed can read.
6. Open WalletFeed. WalletFeed then updates the widget.

If you select no accounts in step 5, WalletFeed clears the totals from the widget in step 6.

To remove the widget from the Home Screen:

1. Touch and hold the widget.
2. Tap **Remove Widget**.
3. If iOS shows a message, tap **Remove**.

To change the small widget to the medium widget:

1. Remove the small widget.
2. Add the medium widget, as in [Step 2](#step-2-add-the-widget-to-the-home-screen).

To remove the rectangular widget from the Lock Screen:

1. If your iPhone shows the Home Screen or an app, push the side button.
2. If iOS does not show the Lock Screen, push the side button.
3. Touch and hold the Lock Screen until iOS shows **Customize** at the bottom of the screen.
4. Tap **Customize**.
5. If iOS shows the Lock Screen and the Home Screen, tap the Lock Screen.
6. Tap the widgets below the time.
7. Tap **−** on the **Spending** widget.
8. Tap **Done**.

## If there is a problem

### If the widget shows “Open WalletFeed to see your spending.”

WalletFeed did not read your transactions in Wallet, or WalletFeed does not have access to Wallet. The one-line widget shows only “Open WalletFeed”.

1. Open WalletFeed.
2. Tap **Transactions**.

If **Transactions** shows your transactions, WalletFeed updated the widget when WalletFeed opened. If **Transactions** shows **No Cards**, do these steps:

1. Tap **Choose Accounts**.
2. On the **Share Wallet Data** screen, select the accounts that WalletFeed can read.
3. For each account, select the start date.
4. Tap **Share**.

If **Transactions** shows **Wallet Access Off**, the steps are in [If WalletFeed shows “Wallet Access Off”](#if-walletfeed-shows-wallet-access-off).

### If WalletFeed shows “Wallet Access Off”

WalletFeed does not have access to Wallet. After you tap **Share** or **Don't Share**, iOS does not show the **Share Wallet Data** screen again.

1. On your iPhone, open the Settings app.
2. Tap **Privacy & Security**.
3. Tap **Wallet**.
4. Tap **WalletFeed**.
5. Select the accounts that WalletFeed can read.
6. Open WalletFeed. WalletFeed then updates the widget.

### If the widget does not show a new purchase

WalletFeed did not update the widget after the purchase. When WalletFeed is not open, iOS starts WalletFeed approximately 1 hour or less after a change in Wallet.

1. Open WalletFeed. WalletFeed then updates the widget.
2. Go to the Home Screen.

### If the widget shows totals that are not from your accounts

The widget shows the totals of the sample transactions because **Sample Data** is on.

1. Open WalletFeed.
2. Tap **Settings** (the gear button) at the top of the screen.
3. In the **Data** section, set **Sample Data** to off. WalletFeed then clears the sample totals and calculates your totals from Wallet.
