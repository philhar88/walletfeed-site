+++
title = "Select the Wallet accounts that WalletFeed reads"
nav_title = "Wallet accounts"
description = "Share your Apple Card, Apple Cash or Savings account with WalletFeed on your iPhone. Change the accounts and their start dates in the Settings app."
order = 20
related = ["docs/get-started", "docs/privacy-and-security"]
updated = 2026-10-30
+++

WalletFeed reads the transactions of the Wallet accounts that you share with it on your iPhone. It can read your Apple Card, Apple Cash and Savings accounts. You select the accounts when you open WalletFeed for the first time. After that, you change them in the Settings app.

## Share your accounts for the first time

When you open WalletFeed for the first time, it shows **Welcome to WalletFeed**.

1. Tap **Continue**.

   ![The Welcome to WalletFeed screen, with the text "Next, choose the Wallet accounts to share." above the Continue button.](app:docs-welcome)

   **Transactions** opens, and iOS shows the Wallet access screen.

2. Select each account to share.
3. For each account, select the start date.

   From that date, WalletFeed can read the transactions of the account.

4. Tap **Share**.

   **Transactions** shows the transactions of the accounts that you shared.

If you tap **Don't Share**, WalletFeed cannot read Wallet, and **Transactions** shows **Wallet Access Off**. To share accounts after that, use the Settings app. Refer to [Change the accounts that you share](#change-the-accounts-that-you-share).

## Share accounts from WalletFeed

Until you tap **Share** or **Don't Share** on the Wallet access screen, WalletFeed shows **Choose Accounts**. **Choose Accounts** is in **Settings** › **Wallet**. It also shows below **No Cards** in **Transactions**, **Spending** and **Search**.

1. In WalletFeed, tap **Settings** (the gear button) at the top of the screen.
2. In the **Wallet** section, tap **Choose Accounts**.

   ![WalletFeed Settings, with Choose Accounts in the Wallet section.](app:docs-settings)

   iOS shows the Wallet access screen.

3. Do steps 2 to 4 in [Share your accounts for the first time](#share-your-accounts-for-the-first-time).

## Change the accounts that you share

After you tap **Share** or **Don't Share**, iOS does not show the Wallet access screen again. You change the accounts and their start dates in the Settings app.

At the end of the **Transactions** list, WalletFeed shows the date of the first transaction that it can read. If you select a start date before this date in step 4, WalletFeed can also read the transactions before this date.

1. On your iPhone, open the Settings app.
2. Tap **Privacy & Security** › **Wallet** › **WalletFeed**.
3. Select the accounts that WalletFeed can read.
4. Select the start date of each account.
5. Open WalletFeed.

   When WalletFeed opens, it reads the change.

If you do not select an account in step 3, WalletFeed cannot read the transactions of that account. A destination keeps the transactions that it received before this change.

> **Note:** After you tap **Share** or **Don't Share**, **Settings** › **Wallet** in WalletFeed shows **Open Settings**. **Open Settings** opens the WalletFeed page in the Settings app.

## Accounts and destinations

With [WalletFeed Pro](/docs/walletfeed-pro/), WalletFeed sends transactions to [destinations](/docs/destinations/), for example to Lunch Money or Google Sheets. A destination receives the transactions of the accounts that you share.

Before a new destination receives transactions, WalletFeed shows a message. The message tells you which data the destination receives and from which accounts. It also gives the start date, or tells you that the destination receives all the transactions from these accounts. After you tap **Send**, the destination starts to receive transactions. For a CSV, OFX or QIF file, the button is **Save**.

If you set the **Filter** switch of a destination to on, you can use **Accounts** to select the accounts that the destination receives. Refer to [Choose what a destination receives](/docs/choose-what-to-send/).

## Correct problems with Wallet access

### If WalletFeed shows Wallet Access Off

WalletFeed cannot read Wallet, because you tapped **Don't Share** or you stopped its access in the Settings app.

1. On your iPhone, open the Settings app.
2. Tap **Privacy & Security** › **Wallet** › **WalletFeed**.
3. Select the accounts that WalletFeed can read.
4. Open WalletFeed.

### If WalletFeed shows No Transactions

The accounts that you share have no transactions from their start dates. WalletFeed shows "To share more Wallet accounts, open Settings › Privacy & Security › Wallet."

If you did not share all your accounts, share more accounts. If an account has transactions before its start date, select a start date before these transactions. Refer to [Change the accounts that you share](#change-the-accounts-that-you-share).

### If an account does not show in WalletFeed

WalletFeed reads only your Apple Card, Apple Cash and Savings accounts. It does not show other cards in Wallet.

If the account is one of these accounts, share it in the Settings app. Refer to [Change the accounts that you share](#change-the-accounts-that-you-share).

### If WalletFeed shows Wallet Unavailable

This iPhone cannot share Wallet data with WalletFeed. WalletFeed is for iPhone with iOS 26 or a newer version, and it is available only in the US.
