# Privacy and security

WalletFeed has no account and no WalletFeed servers. It reads your Apple Card, Apple Cash and Savings transactions from Wallet on your iPhone. It sends them directly from your iPhone to the [destinations](/docs/destinations/) that you add. For the full text, refer to the [WalletFeed privacy policy](/privacy/).

## Data that WalletFeed keeps

WalletFeed keeps your transactions in memory only while it uses them. It does not save a copy of them.

WalletFeed keeps some settings and status data on your iPhone. For example, it keeps these items:

- Your settings, and the settings of each destination, such as its name and [filter](/docs/choose-what-to-send/).
- The keys, webhook addresses and sign-ins of your destinations. They stay in the Keychain on your iPhone, and they do not go to iCloud Keychain.
- The sync status of each destination, without transaction data. For example, the time of the last sync and the number of changes that WalletFeed sent.
- Two totals for the [Spending widget](/docs/spending-widget/): this month, and the same days of last month. iOS also keeps the data that the widget shows.

## Data that WalletFeed sends

WalletFeed sends your transactions only to the services, folders and apps that you select:

- A service that you connect, such as Lunch Money or Notion, receives the transactions over HTTPS directly from your iPhone.
- A Files destination saves the transactions in a folder that you select, for example a folder in iCloud Drive.
- When you [export a CSV file](/docs/export-csv/), the file goes only to the app that you select in the share sheet.
- When a [shortcut](/docs/siri-and-shortcuts/) or Siri runs the **Get Recent Card Transactions** action, that shortcut or Siri receives your transactions.

If you tell Siri to show Spending or to search WalletFeed, Siri opens WalletFeed. Siri receives none of your transactions.

Before a new destination receives transactions, WalletFeed shows a message, for example "Send Transactions to Lunch Money?". The message tells you which data the destination receives, from which accounts and from which date. For a service, it also tells you "It keeps what it receives." WalletFeed sends nothing until you tap **Send**, or **Save** for a Files destination. If you tap **Cancel**, WalletFeed removes the destination.

After a service receives your data, the terms and privacy policy of that service are applicable to it. If you delete a destination, WalletFeed does not send more data to it. But WalletFeed cannot delete the data that it sent before.

## Apple Intelligence

If Apple Intelligence is available on your iPhone, WalletFeed uses it for these features:

- The [Monthly Summary](/docs/spending/), and the summary of each answer in [Ask Spending](/docs/ask-spending/).
- Your searches, your questions in Ask Spending, and the rules that you write for a destination filter.
- The names of your [recurring charges](/docs/recurring-charges/).

Apple Intelligence operates on your iPhone, and WalletFeed sends nothing to a server for these features. To read a search, a question or a rule, Apple Intelligence gets only the words that you type or speak. To give names to recurring charges, it gets only the merchant names.

WalletFeed calculates all the charts, totals and lists. Apple Intelligence can write an incorrect number in a summary. If a summary and the numbers on the screen are different, use the numbers on the screen.

WalletFeed does not keep the text that Apple Intelligence writes. It keeps only the filter that a rule makes.

## Stop the Apple Intelligence summaries

**Summarize Spending** shows in **Settings** only if Apple Intelligence is available on your iPhone.

1. On your iPhone, open WalletFeed.
2. Tap **Settings** (the gear button) at the top of the screen.
3. In **Privacy & Security**, set the **Summarize Spending** switch to off.

   ![WalletFeed Settings, with Require Face ID, Summarize Spending and Privacy in the Privacy & Security section.](https://walletfeed.app/docs/privacy-and-security/walletfeed-settings-2.webp)

4. Tap **Done**.

Apple Intelligence then does not write the Monthly Summary or the summary of each answer. It continues to read the questions that you send in Ask Spending.

## Lock WalletFeed with Face ID

You can lock WalletFeed with Face ID, Touch ID or your passcode. The name of the switch changes with the type of iPhone:

- **Require Face ID**, on an iPhone with Face ID.
- **Require Touch ID**, on an iPhone with Touch ID.
- **Require Passcode**, on an iPhone without Face ID or Touch ID.

1. On your iPhone, open WalletFeed.
2. Tap **Settings** (the gear button) at the top of the screen.
3. In **Privacy & Security**, set the **Require Face ID** switch to on.

   ![WalletFeed Settings, with the Require Face ID switch in the Privacy & Security section.](https://walletfeed.app/docs/privacy-and-security/walletfeed-settings-2.webp)

4. Use Face ID, Touch ID or your passcode.

   If Face ID does not identify you, the switch stays off.

5. Tap **Done**.

WalletFeed locks each time that you go away from it. When you open WalletFeed again, it starts Face ID one time. If Face ID does not identify you, tap **Unlock** to try again.

To open WalletFeed without Face ID again, set the **Require Face ID** switch to off.

## Screen protection

WalletFeed also keeps your transactions out of view in these conditions:

- When you go away from WalletFeed, it puts a cover on its screen. Thus the app switcher does not show your transactions.
- While you record the screen of your iPhone, or show it on a different screen, WalletFeed does not show your transactions or amounts.
- While your iPhone is locked, iOS can show the Spending widget without its amounts.

## Notifications

If you set the **Recurring Charge Alerts** switch to on, WalletFeed finds new and changed recurring charges on your iPhone. Each notification shows the name and the amounts of the charge. Notification Center keeps the notification until you clear it.

A **Remind If Sync Stops** notification contains no transaction data.

## Analytics and purchases

WalletFeed has no analytics, no advertisements and no third-party SDKs. It does not monitor what you do in other apps or on websites.

If you share analytics with app developers in the Settings app, Apple can share crash reports with the developer.

Purchases of [WalletFeed Pro](/docs/walletfeed-pro/) go through Apple. WalletFeed does not see your payment information.

## Delete a destination

When you delete a destination, WalletFeed erases its settings, its key and its sync status from your iPhone.

1. In WalletFeed, tap **Destinations**.
2. Tap the destination.
3. Tap **Delete**.

   ![The screen of a Lunch Money destination, with Delete at the bottom.](https://walletfeed.app/docs/privacy-and-security/walletfeed-destination-detail.webp)

4. In the message, tap **Delete** again.

The message tells you "Transactions already sent stay at the destination." WalletFeed cannot delete the data that the destination received.

## Remove all destinations

**Remove All Destinations** shows in **Settings** only if you have a destination.

1. On your iPhone, open WalletFeed.
2. Tap **Settings** (the gear button) at the top of the screen.
3. In **Data**, tap **Remove All Destinations**.

   ![WalletFeed Settings, with Export CSV and Remove All Destinations in the Data section.](https://walletfeed.app/docs/privacy-and-security/walletfeed-settings-3.webp)

4. Tap **Remove All**.

WalletFeed erases the keys and the sync status of all your destinations from your iPhone. The transactions that WalletFeed sent stay at each destination.

## Change the Wallet accounts that WalletFeed reads

To remove an account from WalletFeed, deselect it in the Settings app. Refer to [Change the accounts that you share](/docs/wallet-accounts/#change-the-accounts-that-you-share).

If WalletFeed cannot read a Wallet account, it erases the totals of the Spending widget the next time that it runs.

## Data after you delete WalletFeed

When you delete WalletFeed, iOS removes its settings and its sync status. Keychain items can stay on your iPhone after you delete the app. If you install WalletFeed again, it erases them when it opens for the first time.

## Read the privacy statement in WalletFeed

1. On your iPhone, open WalletFeed.
2. Tap **Settings** (the gear button) at the top of the screen.
3. In **Privacy & Security**, tap **Privacy**.

   ![The Privacy screen in WalletFeed, with the Wallet data and Data on your iPhone sections.](https://walletfeed.app/docs/privacy-and-security/walletfeed-privacy.webp)

In the **About** section of **Settings**, **Privacy Policy** opens the [privacy policy](/privacy/) on this website.
