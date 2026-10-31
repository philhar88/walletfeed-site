# Frequently asked questions

## Background Sync and history

### How do new purchases reach my apps while WalletFeed is closed?

With WalletFeed Pro, [Background Sync](https://walletfeed.app/docs/background-sync/) sends new and changed transactions to your destinations while WalletFeed is closed. After a change in Wallet, Apple’s FinanceKit starts WalletFeed’s background extension, and your destinations update within about an hour. Without Pro, the same run still keeps the Spending widget and Recurring Charge Alerts current.

While WalletFeed is open, changes go out in seconds. The After Each Card Tap automation in Settings › Sync › Automations does the same for a purchase you make by tapping your iPhone, even when WalletFeed is closed.

### Can anything delay Background Sync?

Yes. iOS sets the exact time of each background run, and opening WalletFeed always sends what’s waiting.

After your iPhone restarts, WalletFeed sends nothing until you unlock it once, because the Keychain that holds your keys stays locked until then. If WalletFeed can’t open the folder of a file in the background, the file updates the next time you open WalletFeed or charge your iPhone. Low Power Mode, and turning off Background App Refresh, can hold back some of WalletFeed’s background work, such as the catch-up while your iPhone charges.

### What happens when a charge posts, changes or is declined?

Wallet gives each transaction an ID that stays the same when the charge changes. WalletFeed uses that ID to update the transaction in place, so a pending charge that posts, or one whose amount changes, stays a single entry in your destination. A declined or expired charge is removed. If Wallet replaces a pending charge with a new one, WalletFeed removes the old entry and adds the new one. A refund is a separate transaction in Wallet, so it arrives as a new entry with money in.

Webhooks, Amazon SQS, Kinesis Data Streams and EventBridge receive a message for each change instead. Each message has the transaction’s ID, so your automation can update its own data. So do Zapier and Make with Send set to Each Transaction. OFX and QIF files list a charge only after it posts. A Quicken CSV file is written once, 5 days after its month ends, so later changes don’t reach it. To send every charge only once it posts, turn off Include Pending in the destination’s filter.

### Does a new destination get my earlier transactions?

Yes. A new destination also receives your earlier transactions, back to the start date in Settings › Sync › Initial History, which is All until you change it. With Send set to Each Transaction, Zapier, Make and Linear start 30 days back, because in those services each transaction runs an automation or becomes an issue. Later, [Send History](https://walletfeed.app/docs/send-history/) on a destination’s screen sends a longer period.

WalletFeed sends the newest transactions first, at a pace each service accepts, and new transactions always go ahead of the history. YNAB, for example, gets 100 transactions every 4 minutes, well inside its limit of 200 requests an hour. A large history to a slow service can take a few days. The destination’s screen shows the progress, and when you leave WalletFeed, iOS can let it keep sending in a Live Activity.

### Does WalletFeed stay within each service’s limits?

Yes. Where a service accepts several transactions in one request, WalletFeed sends them together, and it spaces its requests to fit each service’s limits. For example, 10 changes reach Zapier in one request, and Zapier still runs your Zap once for each change. In Linear, a batch of 25 changes takes at most 5 requests.

If a service limits requests, WalletFeed waits and sends the rest later. It moves past a batch only after the service accepts it.

### What’s the difference between Monthly and Each Transaction?

Linear, Zapier and Make destinations have a Send setting. Monthly, the default for new destinations, sends one item a month. In Linear, that’s an issue for the month with a table of its transactions, which WalletFeed updates as the month changes. Zapier and Make get one event with all of the month’s transactions, 5 days after the month ends, so most pending charges have posted by then.

Each Transaction sends every change as it happens, so each one runs your Zap or scenario, or becomes a Linear issue. With Monthly, a new destination receives every month from its start date. With Each Transaction, it receives at most 30 days. Destinations added before WalletFeed 1.1 keep Each Transaction until you change Send.

## Destinations

### Can WalletFeed send to my app?

With WalletFeed Pro, your transactions can go to these destinations:

- Budgeting apps: BankSync, Lunch Money, PocketSmith, Firefly III, Sure, Toshl Finance, Wallet by BudgetBakers and YNAB
- Sheets and databases: Google Sheets, Airtable, Notion, Coda, Supabase and Linear
- Files: CSV, OFX, QIF and Quicken CSV files in iCloud Drive or another folder, for apps that import them, such as Quicken, Actual Budget and GnuCash
- Automations: Zapier, Make and signed webhooks, for apps that WalletFeed doesn’t list
- AWS: Amazon S3, SQS, Kinesis Data Streams, DynamoDB and EventBridge

The [guides](https://walletfeed.app/guides/) give the steps for each one.

### Can I send only some transactions?

Yes. Each destination has its own [filter](https://walletfeed.app/docs/choose-what-to-send/), by account, category, merchant, minimum amount, purchases or credits, and pending charges. With Apple Intelligence, you can also type the filter as a sentence, such as “Travel over $50, not Uber”.

### Do changes I make in a destination come back to WalletFeed?

No. WalletFeed sends one way, from Wallet to your destinations. It doesn’t read your edits back, and it can’t change anything in Wallet.

### Can I open a transaction in WalletFeed from Linear?

Yes. Each issue that WalletFeed makes in Linear has a WalletFeed item under Resources. On your iPhone, tap it to open WalletFeed at that transaction, or at that month for a monthly issue. A link only opens a screen in WalletFeed. It never sends anything or changes a setting.

## Privacy

### Do I need an account?

No. There’s nothing to sign up for, and WalletFeed doesn’t know who you are. Apple handles purchases of WalletFeed Pro, and WalletFeed never sees your payment details.

### Where are my transactions kept?

WalletFeed reads your transactions from Wallet on your iPhone when it needs them, holds them in memory only while it uses them, and doesn’t keep a copy. No WalletFeed server keeps your transactions or keys. Your transactions go straight from your iPhone to the destinations you add.

A Files destination saves them in the folder you choose, and each service you connect keeps what it receives.

### Why do some services use sign-in and others a key?

WalletFeed offers sign-in where a service makes it possible, such as Google Sheets, BankSync and Sure. BankSync and Sure also accept a key. For other services, you create a key or token in the service and paste it into WalletFeed.

Either way, the key or sign-in stays in the Keychain on your iPhone, which iOS encrypts. It doesn’t sync to iCloud Keychain, and WalletFeed sends it only to its own service. No one at WalletFeed can see it.

Some services’ sign-in needs a secret that an app can’t hold. For those, WalletFeed’s sign-in service completes the sign-in and keeps nothing, and your transactions never go through it.

### Does WalletFeed track me?

No. WalletFeed has no analytics, advertising or third-party code, and it doesn’t track you across apps or websites. This website has no cookies or analytics either.

### Does Apple Intelligence send my spending to a server?

No. WalletFeed uses Apple’s on-device model, so Ask Spending, the Monthly Summary, Search and the names of recurring charges run on your iPhone. WalletFeed calculates every figure itself. The model reads what you type and writes the summaries. It can get a figure wrong, so rely on the charts and totals.

These features need an iPhone that supports Apple Intelligence, with Apple Intelligence turned on. Without it, Spending and Search still work. To stop the summaries, turn off Summarize Spending in Settings.

### What happens when I remove a destination?

WalletFeed stops sending to it, and deletes its key or sign-in and its sync status from your iPhone. The transactions it already received stay in the service, under that service’s terms.

## Accounts and devices

### Which accounts can WalletFeed read?

WalletFeed reads Apple Card, Apple Cash and Savings, the Wallet accounts that Apple’s FinanceKit lets apps read in the US. Other cards in Wallet aren’t available through FinanceKit.

iOS asks which accounts to share, and from what date. You can change that later in the Settings app, in Privacy & Security › Wallet › WalletFeed. A participant in Apple Card Family can’t share that Apple Card with apps. On a shared Apple Card, FinanceKit doesn’t say who made each purchase.

### What do I need to use WalletFeed?

WalletFeed needs an iPhone with iOS 26 or later, and it’s available only in the US. The Apple Intelligence features also need an iPhone that supports Apple Intelligence.

### Is there a version for iPad, Mac, Android or the web?

No. Apple makes Wallet transactions available to apps only on iPhone, so WalletFeed is an iPhone app. To see your transactions on another device, send them to a destination you can open there, such as Google Sheets or a CSV file in iCloud Drive.

## Price and support

### How much does WalletFeed cost?

WalletFeed is free to download. [WalletFeed Pro](https://walletfeed.app/docs/walletfeed-pro/), which sends your transactions to destinations, is $0.99 a month or $4.99 a year, each with a 1-week free trial, or $19.99 once for Lifetime. It works with Family Sharing.

To cancel a subscription, open the Settings app, tap your name, then tap Subscriptions.

### What can I use without WalletFeed Pro?

You can use all the spending features without Pro: Spending, Transactions, Search, Recurring Charges, Recurring Charge Alerts, the Spending widget, Export CSV and every Apple Intelligence feature. WalletFeed Pro adds destinations, with Background Sync, Send History and the Shortcuts actions that send or get transactions.

### How do I report a problem?

In WalletFeed, tap Settings › Report a Problem, describe what happened, then tap Send. Mail opens an email to support@walletfeed.app, which you send from your own account. WalletFeed adds diagnostics, such as the app and iOS versions and each destination’s status, which you can preview or turn off. They never include transactions, keys, or account or destination names.

Without Mail, you can share or copy the report and send it another way. The [Support](https://walletfeed.app/support/) page and [Troubleshooting](https://walletfeed.app/docs/troubleshooting/) cover common problems.
