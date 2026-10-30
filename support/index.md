# Support

Send an e-mail to [support@walletfeed.app](mailto:support@walletfeed.app?subject=WalletFeed). In the e-mail, give the model of your iPhone and the version of iOS on it. For a problem with a destination, also give the service or the file format, for example Notion or CSV. Do not send API keys, tokens or data about your transactions.

To correct a problem, find it on this page or in [Troubleshooting](https://walletfeed.app/docs/troubleshooting/).

## If WalletFeed does not show your cards

WalletFeed is available only in the US. WalletFeed can read Apple Card, Apple Cash and Savings accounts. It reads only the accounts that you select on the iOS screen for Wallet access.

Until you tap **Share** or **Don't Share** on this iOS screen, **Settings** › **Wallet** shows **Choose Accounts**. To select your accounts, do these steps:

1. In WalletFeed, tap **Settings** (the gear button) at the top of the screen.
2. In the **Wallet** section, tap **Choose Accounts**.
3. On the iOS screen, select the accounts and the start date of each account.
4. Tap **Share**.

After you tap **Share** or **Don't Share**, iOS does not show this screen again. Then **Settings** › **Wallet** shows **Open Settings**. To change the accounts, do these steps:

1. On your iPhone, open the Settings app.
2. Tap **Privacy & Security** › **Wallet** › **WalletFeed**.
3. Select the accounts and the start date of each account.
4. Open WalletFeed.

Refer to [Select the Wallet accounts that WalletFeed reads](https://walletfeed.app/docs/wallet-accounts/).

## If WalletFeed does not show Ask Spending

These functions are available only on an iPhone that can use Apple Intelligence, and only when Apple Intelligence is active:

- Ask Spending
- The Monthly Summary
- Search with Apple Intelligence
- The names in **Recurring Charges**
- A filter that you type as a sentence

If your iPhone can use Apple Intelligence, do these steps:

1. On your iPhone, open the Settings app.
2. Tap **Apple Intelligence & Siri**.
3. Activate Apple Intelligence.

Without Apple Intelligence, you can use **Spending** and **Search**. **Search** then finds the words that you type.

When WalletFeed can use Apple Intelligence, **Settings** shows **Summarize Spending** in the **Privacy & Security** section. If you deactivate **Summarize Spending**, Apple Intelligence does not make the Monthly Summary or the summaries in Ask Spending. Refer to [Ask Spending with Apple Intelligence](https://walletfeed.app/docs/ask-spending/).

## If a destination shows “Authentication failed”

The service did not let WalletFeed use the key, the token, the URL or the sign-in of the destination. Some causes are an expired key and a key that you deleted in the service.

1. In the service, make a new key, token or URL.
2. In WalletFeed, tap **Destinations**.
3. Tap the destination.
4. Tap **Replace Key**, **Replace Token** or **Replace URL**.
5. Paste the new key, token or URL.
6. Tap **Replace**.

For Google Sheets, and for BankSync with **Sign In with BankSync**, the destination screen shows **Sign In Again**. For a webhook, the destination screen shows **URL** and **Authorization**.

It is not necessary to delete the destination. After you correct the problem, WalletFeed sends the changes that the destination did not receive. Refer to [Troubleshooting](https://walletfeed.app/docs/troubleshooting/#if-a-destination-shows-authentication-failed).

## If a destination receives changes only while WalletFeed is open

While WalletFeed is open, a destination receives changes in seconds. When WalletFeed is not open, iOS starts WalletFeed approximately 1 hour or less after a change in Wallet. Then WalletFeed updates the Spending widget and **Recurring Charge Alerts**. If you have WalletFeed Pro and **Background Sync** is active, WalletFeed also sends the change to your destinations.

1. In WalletFeed, tap **Settings** (the gear button) at the top of the screen.
2. In the **Sync** section, activate **Background Sync**.

**Settings** shows the **Sync** section only with WalletFeed Pro. After your iPhone starts again, destinations do not receive changes until you type your passcode one time.

To send each purchase seconds after you tap your iPhone to make the purchase, make an **After Each Card Tap** automation. The steps are in **Settings** › **Sync** › **Automations**. Refer to [Background Sync](https://walletfeed.app/docs/background-sync/).

## If a file changes only when you open WalletFeed

If WalletFeed cannot open the folder of a CSV, OFX or QIF file in the background, WalletFeed does not update the file. WalletFeed updates the file when you open WalletFeed, when a Shortcuts automation starts a WalletFeed action, or while your iPhone charges. Refer to [Troubleshooting](https://walletfeed.app/docs/troubleshooting/#if-a-file-changes-only-when-you-open-walletfeed).

## If a destination does not have your previous transactions

A new destination also receives previous transactions, from the start date in **Settings** › **Sync** › **Initial History**. **Initial History** is **All** until you change it.

A new Zapier, Make or Linear destination receives no more than 30 days of previous transactions. In Zapier, each transaction starts your Zap. In Make, each transaction starts your scenario. In Linear, each transaction can become an issue.

WalletFeed sends the history from the last transaction back to the first transaction. WalletFeed obeys the limits of each service. The destination screen shows **Sending History** and the number of transactions that WalletFeed sent. WalletFeed also sends the history in the background.

To send more previous transactions to a destination, do these steps:

1. In WalletFeed, tap **Destinations**.
2. Tap the destination.
3. Tap **Send History**.
4. Select a time, for example **90 Days**.
5. For Zapier, Make or Linear, tap **Send** in the message.

To stop the history, tap **Send History** › **Stop Sending**. The destination keeps the transactions that it received before you stopped the history. Refer to [Send previous transactions](https://walletfeed.app/docs/send-history/).

## Connect WalletFeed to BankSync

With **Sign In with BankSync**, an API key is not necessary. You can use **Sign In with BankSync** on the Free plan of BankSync.

1. In WalletFeed, tap **Destinations**.
2. Tap **+** at the top of the screen.
3. In the **Budgeting** section, tap **BankSync**.
4. Tap **Sign In with BankSync**.
5. On the BankSync page, get access to your BankSync account.
6. Give WalletFeed access to your BankSync workspace. Only the owner or an admin of the workspace can give this access.
7. Tap **Add**.

After you give access, BankSync makes an “Apple Card” table. WalletFeed can get access only to that table.

If BankSync does not make the table in approximately 30 seconds, WalletFeed shows “You're signed in, but BankSync hasn't created or shared the Apple Card table.”

The message also gives the table limit of your plan, for example “The Free plan allows one table.” To correct the problem, do these steps:

1. Tap **Open BankSync**.
2. Delete a table that you do not use, or change your plan to a plan that has more tables.
3. In WalletFeed, tap **Try Again**.

To use an API key, tap **Use an API Key Instead**. The Free plan and the Starter plan of BankSync do not include API keys. Refer to [Send Apple Card transactions to BankSync](https://walletfeed.app/guides/apple-card-to-banksync/).

**Note:** **Sign In with BankSync** uses the referral URL of WalletFeed. Thus, the BankSync form in WalletFeed shows “WalletFeed may earn a commission if you pay for BankSync.”

## If a destination shows a pending charge

Most destinations receive a charge while it is pending. When the charge posts, WalletFeed updates the charge in the destination. WalletFeed removes declined and expired charges from the destination.

OFX and QIF files include a charge only after it posts. To send a charge to a destination only after the charge posts, deactivate **Include Pending** in the filter of the destination.

Zapier, Make, a webhook, Amazon SQS, Kinesis Data Streams and EventBridge receive a message for each change. Your server or automation must then update its data. Refer to [Send charges only after they post](https://walletfeed.app/docs/choose-what-to-send/#send-charges-only-after-they-post).

## Send only some transactions to a destination

1. In WalletFeed, tap **Destinations**.
2. Tap the destination.
3. Activate **Filter**.
4. Set the items of the filter, for example **Minimum**, **Accounts** or **Categories**.

With Apple Intelligence, you can also type the filter as a sentence, for example “Travel over $50, not Uber”. Refer to [Filter the transactions for a destination](https://walletfeed.app/docs/choose-what-to-send/).

## Change or cancel your plan

1. In WalletFeed, tap **Settings** (the gear button) at the top of the screen.
2. In the **Subscription** section, tap **Change Plan** or **Manage Subscription**.

WalletFeed shows **Change Plan** and **Manage Subscription** only for the **Monthly** plan and the **Yearly** plan. A Lifetime purchase has no subscription.

You can also change or cancel the subscription in the Settings app:

1. On your iPhone, open the Settings app.
2. Tap your name.
3. Tap **Subscriptions**.
4. Tap **WalletFeed**.

**Restore Purchases** is on the **WalletFeed Pro** screen. Refer to [WalletFeed Pro](https://walletfeed.app/docs/walletfeed-pro/).

## Delete your data

WalletFeed has no account and no WalletFeed servers. Thus, there is no account data or server data to delete.

To delete a destination, do these steps:

1. In WalletFeed, tap **Destinations**.
2. Tap the destination.
3. Tap **Delete**.
4. In the message, tap **Delete**.

WalletFeed removes the destination, its key or sign-in, and its status from your iPhone. The transactions that WalletFeed sent stay in the service. To delete all destinations, tap **Settings** › **Remove All Destinations** › **Remove All**.

Refer to [Privacy and security](https://walletfeed.app/docs/privacy-and-security/) and the [privacy policy](https://walletfeed.app/privacy/).
