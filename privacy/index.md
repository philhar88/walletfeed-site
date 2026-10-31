# Privacy policy

Last updated October 31, 2026

WalletFeed needs no account, and no WalletFeed server keeps your transactions or keys. It reads your transactions from Wallet on your iPhone, holds them in memory only while it uses them, and doesn't keep a copy.

## Developer

WalletFeed is made by Phillip Harrison, an independent developer. Send questions about this policy to [support@walletfeed.app](mailto:support@walletfeed.app).

WalletFeed's servers keep no data about you, so the developer holds none to access, export or delete. If you email support, your message is used only to reply to you and is deleted once your question is resolved.

## Wallet data

WalletFeed reads transactions and account names from the Wallet accounts you choose to share through Apple's FinanceKit: Apple Card, Apple Cash and Savings. iOS asks for your permission first.

You can change what you share at any time in the Settings app.

## Data on your iPhone

WalletFeed keeps only this on your iPhone:

- Sync positions (FinanceKit history tokens), so each destination receives only new changes.
- Your settings and each destination's settings, such as its name and filter.
- Destination credentials, such as API keys, webhook URLs and secrets, and folder access, in the Keychain. They stay on this iPhone and don't sync to iCloud Keychain.
- Sync status without transaction details: when each destination last synced, how many changes were sent, how far back its history has been sent, and a short error description if it failed. WalletFeed's widget can show this status.
- When WalletFeed's Shortcuts actions last ran, so Settings can show whether your automations work.
- For the Spending widget, two totals: your spending this month and at the same point last month, with their currency and the time they were updated. iOS keeps a copy of what the widget shows.
- If you turn on Recurring Charge Alerts, the IDs of transactions WalletFeed has already alerted on, so no alert comes twice. No amounts or merchants are kept for alerts.

WalletFeed doesn't keep a copy of your transactions. A Files destination saves them in the folder you choose.

## Destinations and exports

WalletFeed sends transactions only where you tell it to:

- A Files destination saves transactions in a folder you choose, such as one in iCloud Drive or On My iPhone, as one CSV file or as one CSV, OFX or QIF file per month.
- Services you connect, such as Lunch Money, Notion or AWS, receive transactions over HTTPS directly from your iPhone. WalletFeed connects with the key you paste, which stays in the Keychain on this iPhone.
- Google Sheets uses Google sign-in instead of a key, and the sign-in stays in the Keychain on this iPhone. WalletFeed asks Google only for access to files it creates, so it can open only its own spreadsheet in your Google Drive, where it adds and updates your transactions. It doesn't read, keep or share anything else from your Google Account. WalletFeed's use of information received from Google APIs adheres to the [Google API Services User Data Policy](https://developers.google.com/terms/api-services-user-data-policy), including the Limited Use requirements.
- BankSync can use Sign In with BankSync instead of a key. The sign-in stays in the Keychain on this iPhone, and WalletFeed can open only its own Apple Card table in your workspace.
- For services whose sign-in needs it, WalletFeed's sign-in service completes the sign-in and keeps nothing. The sign-in stays in the Keychain on this iPhone.
- Webhooks, Zapier and Make receive each change at the address you paste. Webhook requests are signed with a secret made on your iPhone, which you share with your server.
- When you export a CSV, the file goes only where you send it from the share sheet.
- If you use WalletFeed's actions in Shortcuts, your shortcut receives the transactions they return.

Before a new destination receives anything, WalletFeed shows what it will get: which details of each transaction, from which accounts and from what date. Nothing is sent unless you agree.

Once data reaches a destination, that service's own terms and privacy policy apply. Removing a destination stops new data from going there, but WalletFeed can't delete what it already sent.

## Apple Intelligence and Siri

When Apple Intelligence is available, WalletFeed uses Apple's on-device model to write your monthly summary and a summary of each request on Spending, interpret searches and requests, name recurring charges and turn a rule you describe into a filter. It all runs on your iPhone, and nothing is sent to a server.

WalletFeed calculates every chart, total and list itself. The model writes the summaries in its own words from figures WalletFeed works out, such as your totals, the change from last month, categories, merchants and largest purchases, and for a request, the words you typed. It can get a figure wrong, so rely on the page's figures. To read a search, request or rule, the model gets only the words you type or say, and to name recurring charges, only their merchant names. Examples you tap on Spending are read by WalletFeed without the model. Nothing the model writes is saved, except the filter a rule creates.

Summarize Spending in Settings turns off both summaries. A request you send on Spending still goes to the model to be read.

When you ask Siri to show your spending or search WalletFeed, Siri opens the app and receives none of your transactions or spending. The Get Recent Card Transactions action is different: it returns transactions to the shortcut or Siri request that runs it.

## Analytics and tracking

WalletFeed has no analytics, advertising or third-party SDKs, and doesn't track you across apps or websites. If you share analytics with app developers in iOS Settings, Apple may share crash reports with the developer.

Sign In with BankSync goes through WalletFeed's referral link, so WalletFeed may earn a commission if you then pay for a BankSync plan.

## Purchases and notifications

Apple handles purchases and payments. WalletFeed checks on your iPhone which plan you have and whether it's active, and never sees your payment details.

If you turn on Remind If Sync Stops, WalletFeed schedules a local notification on your iPhone. It contains no transaction details.

If you turn on Recurring Charge Alerts, WalletFeed works out on your iPhone when a charge starts repeating or changes price, and posts a local notification with the charge's name and amounts. Notification Center keeps it until you clear it.

## Security

- WalletFeed covers its screen when you leave the app, so transactions don't appear in the app switcher.
- Transactions and spending are hidden while your screen is recorded or mirrored.
- The Spending widget's amounts are marked as private, so iOS can hide them while your iPhone is locked.
- You can require Face ID, Touch ID or your passcode to open WalletFeed.
- WalletFeed doesn't cache network responses on disk.

## Your choices

- Delete a destination in Destinations, or remove all of them in Settings. WalletFeed then deletes their credentials, sync positions and sync status from your iPhone.
- Stop sharing Wallet accounts in the Settings app. WalletFeed then clears the Spending widget's totals the next time it runs.
- Turn off Recurring Charge Alerts in Settings, or remove the Spending widget from your Home Screen or Lock Screen.
- Deleting WalletFeed removes its settings and sync status. Keychain items can remain after an app is deleted; if you install WalletFeed again, it erases them when it first opens.

## Children

WalletFeed is a personal finance app for adults and isn't directed at children under 13.

## This website

This site has no cookies, analytics or trackers. It's hosted on GitHub Pages, which may log visits under [GitHub's privacy statement](https://docs.github.com/site-policy/privacy-policies/github-general-privacy-statement).

## Changes

When this policy changes, this page and the app's privacy statement change together, with a new date.
