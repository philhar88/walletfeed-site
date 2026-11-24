+++
title = "Privacy and security"
nav_title = "Privacy and security"
description = "This page about WalletFeed privacy and security tells you which data WalletFeed keeps and sends, and how to lock the app with Face ID."
order = 160
related = ["docs/wallet-accounts","docs/destinations"]
updated = 2026-11-24
+++

WalletFeed has no account, and no WalletFeed server keeps your transactions or keys. It reads your Apple Card, Apple Cash and Savings transactions from Wallet on your iPhone. It sends your transactions directly from your iPhone to the [destinations](/docs/destinations/) that you add. For Spending, the widget and Payment Due Reminder, it also reads the balances of your accounts, your Apple Card credit limit and your next Apple Card payment. For the full text, refer to the [WalletFeed privacy policy](/privacy/).

## Data that WalletFeed keeps

WalletFeed keeps your transactions in memory only while it uses them. It does not save a copy of them.

WalletFeed keeps some settings and status data:

- Your settings and the settings of each destination stay on your iPhone. These include the name and the [filter](/docs/choose-what-to-send/) of each destination.
- The keys, webhook addresses and sign-ins of your destinations stay in the Keychain on your iPhone. iOS encrypts the Keychain. These items do not go to iCloud Keychain or to your other devices.
- No person at WalletFeed can see or get your keys. Your iPhone sends each key only to its service.
- The status of each destination contains no transaction data. For example, the status gives the **Last Sync** time and the number of changes that WalletFeed sent. It also gives the type and the time of the last error. WalletFeed deletes the status when you delete the destination.
- WalletFeed keeps two totals for the [Spending widget](/docs/spending-widget/), one for this month and one for the same days of last month. It also keeps your Apple Card balance and the date that the payment is due. The widget shows these amounts, and iOS keeps a copy of them.
- If [Payment Due Reminder](/docs/spending/#activate-payment-due-reminder) is on, WalletFeed keeps the switch. iOS keeps the next notification until it comes. The notification shows no amount.
- If [Monthly Recap](/docs/spending/#activate-monthly-recap) is on, WalletFeed keeps the month of the last notification (for example, 2026-10). It keeps no amounts.
- If [Tax Pack Ready](/docs/tax-pack/#activate-tax-pack-ready) is on, WalletFeed keeps the switch. iOS keeps the next notification until it comes. The notification shows no amount.
- For the App Store review message from Apple, WalletFeed keeps some dates and the version of WalletFeed. The dates are the first day that you opened WalletFeed and the day of the last message. WalletFeed also keeps up to 3 days that it showed your purchases or sent transactions.

## Data that WalletFeed sends

WalletFeed sends your transactions only to the destinations and apps that you select:

- A service that you connect (for example, Lunch Money or Notion) receives the transactions directly from your iPhone through HTTPS.
- A Files destination saves the transactions in a folder that you select (for example, a folder in iCloud Drive).
- A CSV file from [Export CSV](/docs/export-csv/) goes only to the app that you select in the iOS menu.
- The files from [Tax Pack](/docs/tax-pack/) go only to the app or person that you select in the iOS menu. WalletFeed makes the files on your iPhone and does not keep a copy.
- When a [shortcut](/docs/siri-and-shortcuts/) or Siri uses **Get Recent Card Transactions**, WalletFeed gives your transactions to that shortcut or to Siri.
- When a shortcut uses **Export Transactions** or **Get Balances**, WalletFeed gives a file of your transactions or the balances of your accounts to that shortcut.

If you tell Siri to show Spending, to do a search in WalletFeed or to start **Ask Spending**, Siri opens WalletFeed. Siri receives none of your transactions. WalletFeed keeps your instruction in memory only.

**Report a Problem** in **Settings** makes an e-mail that you send from your e-mail account. The e-mail contains the text that you type. If **Include Diagnostics** is on, it also contains diagnostics.

The diagnostics give the versions of WalletFeed and iOS, the model of your iPhone, some settings and the status of each destination. For a destination that could not send, they give the type of the last error and its time. They do not include transactions, keys, web addresses or the names of your accounts and destinations. Refer to [Send an e-mail to customer support](/docs/troubleshooting/#send-an-e-mail-to-customer-support).

Before a new destination receives transactions, WalletFeed shows a message, for example "Send Transactions to Lunch Money?". The message tells you which data the destination will receive, from which accounts and from which date. For a service, the message also tells you "It keeps what it receives." WalletFeed does not send data until you tap **Send**. For a Files destination, the button is **Save**. If you tap **Cancel**, WalletFeed removes the destination.

After a service receives your data, the terms and the privacy policy of that service are applicable to the data. If you delete a destination, WalletFeed does not send more data to it. But WalletFeed cannot delete the data that the destination received.

## Apple Intelligence

If Apple Intelligence is available on your iPhone, WalletFeed uses it for these features:

- The [Monthly Summary](/docs/spending/) and the summary of each result in [Ask Spending](/docs/ask-spending/)
- The text of the [Monthly Recap](/docs/spending/#the-monthly-recap-notification) notification
- The [Trend](/docs/accounts/#trend) on the screen of an account
- Your searches, the text that you type in Ask Spending, and the rules that you write for a destination filter
- The names of your [recurring charges](/docs/recurring-charges/).

Apple Intelligence operates on your iPhone. For these features, WalletFeed does not send data to a server. To read your text, Apple Intelligence gets only the words that you type or speak. To give names to recurring charges, it gets only the merchant names.

WalletFeed calculates all the charts, totals and lists. Apple Intelligence can write an incorrect number in a summary. If a summary and the totals on the screen are different, the totals are correct.

WalletFeed does not keep the text that Apple Intelligence writes. It keeps only the filter that Apple Intelligence makes from a rule.

## Stop the Apple Intelligence summaries

**Settings** shows **Summarize Spending** only if Apple Intelligence is available on your iPhone. If it is not available, WalletFeed does not write these summaries.

1. On your iPhone, open WalletFeed.
2. Tap **Settings** (the gear button) at the top of the screen.
3. In the **Privacy & Security** section, set **Summarize Spending** to off.

   ![The Settings screen in WalletFeed, with Require Face ID, Summarize Spending and Privacy in the Privacy & Security section.](app:docs-settings-2)

4. Tap **Done**.

After you set **Summarize Spending** to off, Apple Intelligence does not write the Monthly Summary or the summary of each result in Ask Spending. It also does not write the text of the Monthly Recap notification or the Trend of an account. But Apple Intelligence continues to read the text that you send in Ask Spending.

## Lock WalletFeed with Face ID

You can lock WalletFeed with Face ID, Touch ID or your passcode. The label in **Settings** changes with the type of iPhone:

- On an iPhone with Face ID, the label is **Require Face ID**.
- On an iPhone with Touch ID, the label is **Require Touch ID**. iPhone Duo has Touch ID in the side button.
- On an iPhone without Face ID or Touch ID, the label is **Require Passcode**.

1. On your iPhone, open WalletFeed.
2. Tap **Settings** (the gear button) at the top of the screen.
3. In the **Privacy & Security** section, set **Require Face ID** (or **Require Touch ID** or **Require Passcode**) to on.

   ![The Settings screen in WalletFeed, with the Require Face ID switch in the Privacy & Security section.](app:docs-settings-2)

4. Use Face ID, Touch ID or your passcode.

   If Face ID does not identify you, **Require Face ID** stays off.

5. Tap **Done**.

WalletFeed locks each time that you close it or go to a different app. When you open WalletFeed again, it starts Face ID one time.

If Face ID does not identify you, tap **Unlock** to try again.

If you set **Require Face ID** to off, WalletFeed does not lock.

## Screen protection

In these conditions, your iPhone does not show your transactions or amounts:

- When WalletFeed is not the active app, it puts a cover on its screen. Thus, the app switcher does not show your transactions.
- While you record the screen of your iPhone, or show it on a different screen, WalletFeed does not show your transactions or amounts.
- While your iPhone is locked, iOS can show the Spending widget without its amounts, which include the card balance.

## Notifications

If you set **Recurring Charge Alerts** to on in **Settings**, WalletFeed finds new and changed recurring charges on your iPhone. Then WalletFeed shows a notification with the name and the amounts of the charge. Notification Center keeps the notification until you clear it.

If you set **Monthly Recap** to on in **Settings**, WalletFeed calculates the total of last month on your iPhone. On the 3rd day of each month, WalletFeed shows a notification with the total, the change from the month before and the largest category. Notification Center keeps the notification until you clear it.

If you set **Payment Due Reminder** to on in **Settings**, WalletFeed reads the Apple Card balance and payment due date on your iPhone. It asks iOS to show a notification the day before the payment is due. The notification contains no amount. WalletFeed keeps only the switch.

If you set **Tax Pack Ready** to on in **Settings**, WalletFeed asks iOS to show a notification on January 3. The notification gives the year of the Tax Pack and no amount. WalletFeed keeps only the switch.

A **Remind If Sync Stops** notification contains no transaction data. A **Failure Alerts** notification contains the name of the destination and the failure, and no transaction data.

## Analytics and purchases

WalletFeed has no analytics, advertisements or third-party SDKs (code from other companies). It does not monitor you in different apps or on websites.

If you let Apple give analytics data to app developers (in the Settings app), Apple can give crash reports to the developer of WalletFeed.

Apple processes the purchases of [WalletFeed Pro](/docs/walletfeed-pro/). WalletFeed does not receive your payment information.

## Delete a destination

When you delete a destination, WalletFeed erases its settings, its key and its status from your iPhone.

1. On your iPhone, open WalletFeed.
2. Tap **Destinations** at the bottom of the screen.
3. Tap the destination.
4. Tap **Delete**.

   ![The screen of a Lunch Money destination, with Delete at the bottom.](app:docs-destination-detail)

5. In the message, tap **Delete** again.

The message tells you "Transactions already sent stay at the destination." WalletFeed cannot delete these transactions.

## Remove all destinations

**Settings** shows **Remove All Destinations** only if you have a destination.

1. On your iPhone, open WalletFeed.
2. Tap **Settings** (the gear button) at the top of the screen.
3. In the **Data** section, tap **Remove All Destinations**.

   ![The Settings screen in WalletFeed, with Export CSV and Remove All Destinations in the Data section.](app:docs-settings-3)

4. In the message, tap **Remove All**.

WalletFeed erases the settings, the keys and the status of all your destinations from your iPhone. The transactions that WalletFeed sent stay at each destination.

## Change the Wallet accounts that WalletFeed reads

To remove an account from WalletFeed, deselect it in the Settings app. Refer to [Change the accounts that WalletFeed reads](/docs/wallet-accounts/#change-the-accounts-that-walletfeed-reads).

If WalletFeed cannot get access to Wallet, it erases the totals and the card balance of the Spending widget the next time that it operates.

## Data after you delete WalletFeed

When you delete WalletFeed, iOS removes the settings of WalletFeed and the status of your destinations. But the WalletFeed items in the Keychain can stay on your iPhone. If you install WalletFeed again, it erases these items when it opens for the first time.

## Read the privacy statement in WalletFeed

1. On your iPhone, open WalletFeed.
2. Tap **Settings** (the gear button) at the top of the screen.
3. In the **Privacy & Security** section, tap **Privacy**.

   ![The Privacy screen in WalletFeed, with the Wallet data and Data on your iPhone sections.](app:03-privacy)

In the **About** section of **Settings**, **Privacy Policy** opens the [privacy policy](/privacy/) on this website.
