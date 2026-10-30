# Support

Send an email to [support@walletfeed.app](mailto:support@walletfeed.app?subject=WalletFeed). In the email, include the model of your iPhone and the version of iOS on it. For a problem with a destination, also include the type of destination. Do not send API keys, tokens or data about your transactions.

To correct a problem, find it on this page or in [Troubleshooting](https://walletfeed.app/docs/troubleshooting/).

## If WalletFeed does not show your cards

WalletFeed is available only in the US. It reads only the Apple Card, Apple Cash and Savings accounts that you share with it.

To share accounts for the first time, tap **Settings** (the gear button) › **Choose Accounts** in WalletFeed. WalletFeed shows **Choose Accounts** until you tap **Share** or **Don’t Share** on the iOS screen **Share Wallet Data**.

After that, **Settings** › **Wallet** shows **Open Settings**, and you change the accounts in the Settings app:

1. On your iPhone, open the Settings app.
2. Tap **Privacy & Security** › **Wallet** › **WalletFeed**.
3. Select the accounts and the start date of each account.

Refer to [Select the Wallet accounts that WalletFeed reads](https://walletfeed.app/docs/wallet-accounts/).

## If WalletFeed does not show Ask Spending

These functions operate only on an iPhone that can use Apple Intelligence, with Apple Intelligence on:

- Ask Spending
- The Monthly Summary
- Search with Apple Intelligence
- Names in Recurring Charges

If your iPhone can use Apple Intelligence, set Apple Intelligence to on in the Settings app. Without Apple Intelligence, **Spending** and **Search** continue to operate, and **Search** finds the words that you type.

Use **Summarize Spending** in WalletFeed **Settings** to start or stop the summaries. Refer to [Ask Spending with Apple Intelligence](https://walletfeed.app/docs/ask-spending/).

## If a destination shows “Authentication failed”

The service did not accept the key, the token or the sign-in of the destination. A change to the access of the destination in the service can also cause this message.

1. In WalletFeed, tap **Destinations**.
2. Tap the destination.
3. Tap **Replace Key**, **Replace Token** or **Sign In Again**.
4. Paste a new key or token, or sign in again.

WalletFeed keeps the sync position and the history of the destination. Thus, the destination continues where it stopped. Refer to [Troubleshooting](https://walletfeed.app/docs/troubleshooting/#if-a-destination-shows-authentication-failed).

## If a destination receives changes only while WalletFeed is open

While WalletFeed is open, a destination receives changes in seconds. When WalletFeed is closed, iOS starts WalletFeed in approximately 1 hour or less after a change in Wallet. WalletFeed then updates the Spending widget and Recurring Charge Alerts. With WalletFeed Pro and **Background Sync** on, it also sends the change to your destinations.

1. In WalletFeed, tap **Settings** (the gear button) at the top of the screen.
2. In the **Sync** section, set **Background Sync** to on.

**Settings** shows the **Sync** section only with WalletFeed Pro. After your iPhone starts again, destinations do not receive changes until you type your passcode one time.

To send each purchase seconds after you tap your iPhone to make the purchase, do the steps for **After Each Card Tap** in **Settings** › **Sync** › **Automations**. Refer to [Background Sync](https://walletfeed.app/docs/background-sync/).

## If a file changes only when you open WalletFeed

If WalletFeed cannot open the folder of a CSV, OFX or QIF file in the background, it does not update the file. WalletFeed updates the file the next time that you open WalletFeed, or while your iPhone charges. Refer to [Troubleshooting](https://walletfeed.app/docs/troubleshooting/#if-a-file-changes-only-when-you-open-walletfeed).

## If a destination does not have your previous transactions

A new destination also receives previous transactions, from the start date in **Settings** › **Sync** › **Initial History**. **Initial History** is **All** until you change it.

If **Send** is **Each Transaction**, a new Zapier, Make or Linear destination receives a maximum of 30 days of previous transactions. In these services, each transaction runs a Zap, uses a Make credit or becomes an issue.

WalletFeed sends the newest transactions first, at the speed that each service accepts. The screen of the destination shows **Sending History** and the number of transactions that WalletFeed sent. The history continues in the background. A long history to a slow service can continue for some days.

To send more previous transactions to a destination, do these steps:

1. In WalletFeed, tap **Destinations**.
2. Tap the destination.
3. Tap **Send History**.
4. Select a period, for example **90 Days**.

To stop the history, tap **Send History** › **Stop Sending**. The destination keeps the transactions that it received before you stopped the history. Refer to [Send previous transactions](https://walletfeed.app/docs/send-history/).

## If you want to sign in with BankSync

1. In WalletFeed, tap **Destinations**.
2. Tap **+** at the top of the screen.
3. Tap **BankSync**.
4. Tap **Sign In with BankSync**.
5. Give your approval as the owner or an admin of the workspace.
6. Tap **Add**.

After your approval, BankSync makes an Apple Card table, and WalletFeed can see only that table. WalletFeed waits for the table for approximately 30 seconds.

If BankSync does not make the table, WalletFeed shows “You’re signed in, but BankSync hasn’t created or shared the Apple Card table.”

The BankSync Free plan has a limit of one table. If your plan is at its limit, delete a table in BankSync or change to a plan that has more tables. Then, in WalletFeed, tap **Try Again**.

To use an API key, tap **Use an API Key Instead**. API keys are available only on the Standard plan of BankSync or higher. Refer to [Send Apple Card transactions to BankSync](https://walletfeed.app/guides/apple-card-to-banksync/).

**Note:** Sign In with BankSync uses the referral link of WalletFeed. Thus, the BankSync screen in WalletFeed shows “WalletFeed may earn a commission if you pay for BankSync.”

## If a destination shows a pending charge

Most destinations receive a charge while it is pending. When the charge posts, WalletFeed updates it. WalletFeed removes declined and expired charges from the destination.

OFX and QIF files include a charge only after it posts.

A webhook, Zapier, Make and the AWS queues and streams receive a message for each change. Your server or automation must then update its data. Refer to [Destinations](https://walletfeed.app/docs/destinations/#new-and-changed-transactions).

## If you want a destination to receive only some transactions

1. In WalletFeed, tap **Destinations**.
2. Tap the destination.
3. Set the **Filter** switch to on.
4. Use **Accounts**, **Categories** or **Minimum** to select the transactions.

With Apple Intelligence, you can also type the filter as a sentence, for example “Travel over $50, not Uber”. Refer to [Choose what a destination receives](https://walletfeed.app/docs/choose-what-to-send/).

## If you want to change or cancel your plan

1. In WalletFeed, tap **Settings** (the gear button) at the top of the screen.
2. In the **Subscription** section, tap **Change Plan** or **Manage Subscription**.

You can also change or cancel the subscription in the Settings app:

1. Open the Settings app.
2. Tap your name.
3. Tap **Subscriptions**.

**Restore Purchases** is on the **WalletFeed Pro** screen. Refer to [WalletFeed Pro](https://walletfeed.app/docs/walletfeed-pro/).

## If you want to delete your data

WalletFeed has no account and no WalletFeed servers. Thus, there is no account data or server data to delete.

When you delete a destination, WalletFeed removes its credentials, its sync position and its sync status from your iPhone. The transactions that WalletFeed sent stay in that service.

Refer to [Privacy and security](https://walletfeed.app/docs/privacy-and-security/) and the [privacy policy](https://walletfeed.app/privacy/).
