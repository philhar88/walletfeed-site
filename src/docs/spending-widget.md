+++
title = "Spending widget"
nav_title = "Spending widget"
description = "Put the WalletFeed Spending widget on your iPhone Home Screen or Lock Screen. It shows the This Month total and the Same Point Last Month total."
order = 80
related = ["docs/spending", "docs/privacy-and-security"]
updated = 2026-10-30
+++

The Spending widget shows the total of your purchases for this month on your Home Screen or Lock Screen. You can use the widget without [WalletFeed Pro](/docs/walletfeed-pro/) and without a [destination](/docs/destinations/).

## Totals in the widget

The widget and the [**Spending**](/docs/spending/) tab show the same totals for all the [Wallet accounts that WalletFeed reads](/docs/wallet-accounts/). The **This Month** total is from the first day of this month to the last update. The **Same Point Last Month** total is for the month before this month, from its first day to the same day and time.

The totals include pending purchases. Refunds decrease the totals. Transfers, bill payments and declined transactions are not in the totals.

## Widget shapes

| Widget | Shows |
| --- | --- |
| Small, on the Home Screen | **This Month** and **Same Point Last Month** |
| Medium, on the Home Screen | **This Month**, **Same Point Last Month** and the change |
| On the Lock Screen | **Spending**, this month's total and the change |
| One line on the Lock Screen | This month's total, for example "$1,234.56 this month" |

The medium widget and the Lock Screen widget show the change from the **Same Point Last Month** total with an arrow, for example "↓ 14% vs Sep". The arrow points down when the **This Month** total is less than the **Same Point Last Month** total. It points up when the **This Month** total is the same as or more than the **Same Point Last Month** total. If the **Same Point Last Month** total is $0.00 or less, the widget does not show the change.

When you charge your iPhone on its side, iOS can show the widget in [StandBy](https://support.apple.com/guide/iphone/use-standby-iph878d77632/ios).

## Add the widget to your Home Screen

1. On your iPhone, go to the Home Screen page that will show the widget.
2. Touch and hold an area with no apps until the apps start to move.
3. Tap **Edit** at the top of the screen.
4. Tap **Add Widget**.
5. In the search field, type `WalletFeed`.
6. Tap **WalletFeed**. iOS shows the small **Spending** widget.

   Until WalletFeed has your totals, the widget shows example totals before you add it.

7. To add the medium widget, swipe left to it.
8. Tap **Add Widget**.
9. To move the widget, drag it to a different position.
10. Tap **Done**.

Apple gives more information in [Add, edit, and remove widgets on iPhone](https://support.apple.com/guide/iphone/add-edit-and-remove-widgets-iphb8f1bf206/ios).

## Add the widget to your Lock Screen

1. To show the Lock Screen, push the side button of your iPhone.
2. If iOS does not show the Lock Screen, push the side button again.
3. Touch and hold the Lock Screen.
4. If iOS shows the passcode screen, type your passcode.
5. If iOS does not show **Customize** at the bottom of the screen, do step 3 again.
6. Tap **Customize**.
7. Tap **Add Widgets**. If the Lock Screen does not show **Add Widgets**, tap the widgets on the Lock Screen.
8. In the list of apps, tap **WalletFeed**.
9. Tap the **Spending** widget.
10. To close the list of widgets, swipe down.
11. Tap **Done**.

Apple gives more information in [Create a custom iPhone Lock Screen](https://support.apple.com/guide/iphone/create-a-custom-lock-screen-iph4d0e6c351/ios).

## Updates to the widget

WalletFeed updates the widget when you open WalletFeed. When WalletFeed is not open, iOS starts WalletFeed approximately 1 hour or less after a change in Wallet. WalletFeed then updates the widget.

WalletFeed Pro is not necessary for these updates. WalletFeed shows **Settings** › **Sync** only with WalletFeed Pro. If you set [**Background Sync**](/docs/background-sync/) to off there, WalletFeed continues to update the widget.

When a new month starts, the widget shows $0.00 for this month. The widget does not show the **Same Point Last Month** total or the change. After WalletFeed updates the widget, the widget shows the totals again.

> **Note:** When **Sample Data** is on in **Settings**, the widget shows the totals from **Sample Data**.

## Privacy

For the widget, WalletFeed keeps only this information on your iPhone:

- The two totals
- The currency of the totals
- The time of the last update.

iOS keeps a copy of the information that the widget shows. This copy has no transactions, merchants or categories.

On a locked iPhone, iOS can show the widget without the totals and the change.

If you stop WalletFeed's access to Wallet, WalletFeed removes the totals from the widget when you open WalletFeed again.

## If there is a problem

### If the widget tells you to open WalletFeed

The widget shows "Open WalletFeed to see your spending." before WalletFeed reads Wallet for the first time, and after WalletFeed's access to Wallet stops. The one-line widget shows "Open WalletFeed".

1. Open WalletFeed.
2. If WalletFeed shows **No Cards** or **Wallet Access Off**, give WalletFeed [access to Wallet](/docs/wallet-accounts/).

### If the widget total does not include a new purchase

When WalletFeed is not open, iOS starts WalletFeed approximately 1 hour or less after a change in Wallet.

1. Open WalletFeed. WalletFeed updates the widget.

### If the widget shows no totals on a locked iPhone

On a locked iPhone, iOS can show the widget without the totals and the change.

1. Make sure that your iPhone is not locked.
