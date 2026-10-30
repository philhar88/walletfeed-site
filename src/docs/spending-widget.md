+++
title = "Spending widget"
nav_title = "Spending widget"
description = "Put the WalletFeed Spending widget on your iPhone Home Screen or Lock Screen. It shows this month's total and last month's total to the same day and time."
order = 80
related = ["docs/spending", "docs/privacy-and-security"]
updated = 2026-10-30
+++

The Spending widget shows this month's total on your Home Screen or Lock Screen. You can use the widget without [WalletFeed Pro](/docs/walletfeed-pro/) and without a [destination](/docs/destinations/).

## Totals in the widget

The widget and the [**Spending**](/docs/spending/) tab use the same totals from all the [Wallet accounts that WalletFeed reads](/docs/wallet-accounts/). The **This Month** total is from the start of this month to the last update. The **Same Point Last Month** total is from the start of last month to the same day and time last month.

The totals include pending purchases. Refunds decrease the totals. Transfers, bill payments and declined transactions are not in the totals.

## Widget shapes

The widget has these shapes:

| Widget | Shows |
| --- | --- |
| Small, on the Home Screen | **This Month** and **Same Point Last Month**. |
| Medium, on the Home Screen | **This Month**, **Same Point Last Month** and the change from last month. |
| On the Lock Screen | **Spending**, this month's total and the change from last month. |
| One line on the Lock Screen | This month's total, for example "$1,234.56 this month". |

The medium widget and the Lock Screen widget show the change from last month with an arrow, for example "↓ 14% vs Sep". The arrow points down when the **This Month** total is less than the **Same Point Last Month** total. It points up when the **This Month** total is the same or more. If the **Same Point Last Month** total is $0.00 or less, the widget does not show the change.

iOS can also show the widget in [StandBy](https://support.apple.com/guide/iphone/use-standby-iph878d77632/ios) while your iPhone charges on its side.

## Add the widget to your Home Screen

1. On your iPhone, go to the Home Screen page where you want the widget.
2. Touch and hold an area with no apps until the apps start to move.
3. Tap **Edit** at the top of the screen.
4. Tap **Add Widget**.
5. In the search field, type `WalletFeed`.
6. Tap **WalletFeed**.

   iOS shows the small **Spending** widget. Until WalletFeed has your totals, the widget on this screen shows example totals.

7. To add the medium widget, swipe to it.
8. Tap **Add Widget**.
9. To move the widget, drag it to a different position.
10. Tap **Done**.

Apple gives more information in [Add, edit, and remove widgets on iPhone](https://support.apple.com/guide/iphone/add-edit-and-remove-widgets-iphb8f1bf206/ios).

## Add the widget to your Lock Screen

1. To show the Lock Screen, push the side button of your iPhone.
2. If the Lock Screen does not show, push the side button again.
3. Touch and hold the Lock Screen until **Customize** shows at the bottom of the screen.
4. Tap **Customize**.
5. Tap **Add Widgets**.
6. In the list of apps, tap **WalletFeed**.
7. Tap the **Spending** widget.
8. To close the list of widgets, swipe down.
9. Tap **Done**.

Apple gives more information in [Create a custom iPhone Lock Screen](https://support.apple.com/guide/iphone/create-a-custom-lock-screen-iph4d0e6c351/ios).

## Updates to the widget

WalletFeed updates the widget when you open WalletFeed. When WalletFeed is closed, iOS starts WalletFeed in approximately 1 hour or less after a change in Wallet. WalletFeed then updates the widget.

WalletFeed Pro is not necessary for these updates. The [**Background Sync**](/docs/background-sync/) switch in **Settings** › **Sync** has no effect on the widget.

At the start of a month, the widget shows $0.00 for this month. It does not show the **Same Point Last Month** total or the change. After the next update, the widget shows the totals again.

> **Note:** When **Sample Data** is on in **Settings**, the widget shows the totals of the sample transactions.

## Privacy

For the widget, WalletFeed keeps only this information on your iPhone:

- The two totals.
- The currency of the totals.
- The time of the last update.

iOS keeps a copy of the information that the widget shows. Because of this, the widget has only the two totals. It has no transactions, merchants or categories.

On a locked iPhone, iOS can remove the totals and the change from the widget.

If you stop WalletFeed's access to Wallet, WalletFeed removes the totals from the widget the next time that you open WalletFeed.

## If there is a problem

### If the widget shows "Open WalletFeed"

The widget shows this text before WalletFeed reads Wallet for the first time, and after WalletFeed's access to Wallet stops.

1. Open WalletFeed.
2. If WalletFeed shows **No Cards** or **Wallet Access Off**, give WalletFeed [access to Wallet](/docs/wallet-accounts/).

### If the widget does not show a new purchase

When WalletFeed is closed, the widget can show a new purchase in approximately 1 hour or less.

To update the widget, open WalletFeed.

### If the widget shows no totals on a locked iPhone

On a locked iPhone, iOS can remove the totals and the change from the widget.

Make sure that your iPhone is not locked.
