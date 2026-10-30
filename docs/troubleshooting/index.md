# Troubleshooting

WalletFeed shows a message when it cannot read Wallet or send transactions to a destination. To correct a problem with WalletFeed on your iPhone, find the message or the problem on this page, then do the steps below it.

## Correct problems with Wallet and Apple Intelligence

### If WalletFeed does not show your cards

WalletFeed shows only the Wallet accounts that you share with it, and it reads only Apple Card, Apple Cash and Savings in the US.

Until you tap **Share** or **Don't Share** on the iOS screen **Share Wallet Data**, **Settings** › **Wallet** shows **Choose Accounts**. To share your accounts, do these steps:

1. In WalletFeed, tap **Settings** (the gear button) at the top of the screen.
2. In the **Wallet** section, tap **Choose Accounts**.

   ![WalletFeed Settings, with Choose Accounts in the Wallet section.](https://walletfeed.app/docs/troubleshooting/walletfeed-settings.webp)

   iOS shows **Share Wallet Data**.

3. For each account that WalletFeed can read, set the switch to on.

   ![The Share Wallet Data screen, with switches for Apple Card, Apple Cash and Savings, and the Share button.](https://walletfeed.app/docs/troubleshooting/walletfeed-wallet-access.webp)

4. Tap **Share**.

After that, iOS does not show **Share Wallet Data** again, and **Settings** › **Wallet** shows **Open Settings**. To change the accounts that you share, do these steps:

1. On your iPhone, open the Settings app.
2. Tap **Privacy & Security** › **Wallet** › **WalletFeed**.
3. Select the accounts that WalletFeed can read.
4. Select the start date of each account.
5. Open WalletFeed.

For more information, refer to [Wallet accounts](/docs/wallet-accounts/).

### If WalletFeed does not show Ask Spending

WalletFeed shows Ask Spending only on an iPhone that can use Apple Intelligence, with Apple Intelligence on.

1. On your iPhone, open the Settings app.
2. Set Apple Intelligence to on.
3. Open WalletFeed.
4. Tap **Settings** (the gear button) at the top of the screen.
5. In the **Privacy & Security** section, find **Summarize Spending**.

   ![WalletFeed Settings, with the Summarize Spending switch in the Privacy & Security section.](https://walletfeed.app/docs/troubleshooting/walletfeed-settings-2.webp)

   WalletFeed shows **Summarize Spending** only when it can use Apple Intelligence. Then **Spending** shows the field **Ask about your spending**. If WalletFeed does not show **Summarize Spending**, it cannot use Apple Intelligence at this time.

When **Summarize Spending** is off, **Spending** shows no summaries, but it continues to show Ask Spending.

Without Apple Intelligence, **Spending** and **Search** continue to operate. **Search** then finds the words that you type. Refer to [Ask Spending](/docs/ask-spending/).

## Correct problems with destinations

### If a destination shows "Authentication failed"

The service did not accept the key, the token or the sign-in of the destination.

For example, someone deleted the key, or the key is expired. A key that can only read, such as a **Read Only** key in Sure, also causes this message. BankSync stops a key after 90 days if you do not select a different **Expiration** when you make it.

The screen of the destination has a button to correct the problem:

| Destination | Button |
| --- | --- |
| A destination with an API key, for example Sure | **Replace Key** |
| A destination with a token, for example Lunch Money | **Replace Token** |
| A destination with a sign-in, for example Google Sheets | **Sign In Again** |
| Zapier or Make | **Replace URL** |
| Webhook | **URL** and **Authorization** |

To use a new key, token or URL, do these steps:

1. In the service, make a new key, token or URL. The [guide for your destination](/guides/) gives the steps.
2. In WalletFeed, tap **Destinations**.

   ![The Destinations screen, with "Authentication failed" below the n8n destination.](https://walletfeed.app/docs/troubleshooting/walletfeed-destinations-failure.webp)

3. Tap the destination.

   ![The n8n destination screen, with "Authentication failed" below Last Sync, and the URL and Authorization rows.](https://walletfeed.app/docs/troubleshooting/walletfeed-destination-failure.webp)

4. Tap **Replace Key**, **Replace Token** or **Replace URL**.
5. Paste the new key, token or URL.
6. Tap **Replace**.

For a webhook, tap **URL** or **Authorization** in step 4. Type the new value. Then tap **Save**.

A destination with a sign-in can also show "Signed out. Sign in again in the destination's settings." To sign in again, do these steps:

1. In WalletFeed, tap **Destinations**.
2. Tap the destination.
3. Tap **Sign In Again**.
4. Sign in to the same account that you used before.

You do not have to delete the destination. After you correct the problem, WalletFeed sends the changes that the destination did not receive. If the screen shows **Sending History** and **Try Again**, tap **Try Again**.

### If Destinations shows "Sync Requires Pro"

You do not have WalletFeed Pro at this time, and WalletFeed sends transactions to destinations only with WalletFeed Pro.

1. In **Destinations**, tap **Upgrade**.
2. Select a plan.
3. Complete the purchase.

The WalletFeed Pro screen also has **Restore Purchases**. For the plans, refer to [WalletFeed Pro](/docs/walletfeed-pro/).

### If a destination shows "Off"

The **Enabled** switch of the destination is off, and WalletFeed does not send transactions to it.

1. In **Destinations**, tap the destination.
2. Set the **Enabled** switch to on.

   ![The Lunch Money destination screen, with the Enabled switch on.](https://walletfeed.app/docs/troubleshooting/walletfeed-destination-detail.webp)

### If destinations receive changes only while WalletFeed is open

**Background Sync** is off, or your iPhone started again and you did not type its passcode after that.

While WalletFeed is open, destinations receive changes in seconds. When WalletFeed is closed, iOS starts WalletFeed in approximately 1 hour or less after a change in Wallet.

1. In WalletFeed, tap **Settings** (the gear button) at the top of the screen.
2. In the **Sync** section, set the **Background Sync** switch to on.

   ![WalletFeed Settings, with the Background Sync switch on in the Sync section.](https://walletfeed.app/docs/troubleshooting/walletfeed-background-sync.webp)

3. After your iPhone starts again, type its passcode one time.

**Settings** shows the **Sync** section only with WalletFeed Pro. For more information, refer to [Background Sync](/docs/background-sync/).

To send each purchase seconds after you tap your iPhone to pay, do these steps:

1. In **Settings** › **Sync**, tap **Automations**.

   ![The Automations screen, with the steps for After Each Card Tap.](https://walletfeed.app/docs/troubleshooting/walletfeed-automations.webp)

2. In **After Each Card Tap**, do the steps on the screen.

### If you get the notification "Sync Stopped"

WalletFeed did not complete a sync for 3 days, and **Remind If Sync Stops** is on in **Settings** › **Sync**.

The notification tells you "WalletFeed hasn't synced in 3 days. Open it to catch up."

1. Open WalletFeed.

   While WalletFeed is open, it sends the changes to your destinations.

2. Tap **Destinations**.
3. If a destination shows a message, find the message on this page.

**Remind If Sync Stops** stays off until you let WalletFeed send notifications.

### If a destination shows "Can't open the folder. Choose it again."

WalletFeed cannot open the folder of a CSV, OFX or QIF file at this time.

1. In WalletFeed, tap **Destinations**.
2. Tap the destination.
3. Tap **Change Folder**.
4. Select the same folder again.

WalletFeed then writes all the transactions of the destination to the folder again. If WalletFeed shows "Couldn't open this folder.", select a different folder.

### If a file changes only when you open WalletFeed

WalletFeed did not get access to the folder in the background. WalletFeed does not show a message for this.

1. Open WalletFeed.

   The file changes while WalletFeed is open.

WalletFeed also changes the file while your iPhone charges. An automation from **Settings** › **Sync** › **Automations** also changes it.

### If BankSync does not make the Apple Card table

BankSync did not make the table in approximately 30 seconds, for example because the workspace has the maximum number of tables for its plan.

WalletFeed shows "You're signed in, but BankSync hasn't created or shared the Apple Card table."

The message also gives the table limit of your plan, for example "The Free plan allows one table."

1. Tap **Open BankSync**.
2. In BankSync, delete a table that you do not use, or change to a plan that has more tables.
3. In WalletFeed, tap **Try Again**.
4. If WalletFeed continues to show the message, tap **Sign In Again**.
5. Give your approval as the owner or an admin of the workspace.
6. Tap **Add**.

To use an API key, tap **Use an API Key Instead**. API keys are available only on the Standard plan of BankSync or higher. Refer to [Send Apple Card transactions to BankSync](/guides/apple-card-to-banksync/).

> **Note:** Sign In with BankSync uses the referral link of WalletFeed. The form tells you this with the text "WalletFeed may earn a commission if you pay for BankSync."

## Prevent copies of transactions

### If Zapier, Make or a webhook receives a transaction two times

If a sync stops before it sends all the changes, WalletFeed sends the same changes again at the next sync.

Zapier and Make do not find copies. Thus, a Zap or a scenario that adds a row for each change can add a transaction two times. **Send History** also sends previous transactions again.

1. Open the Zap or the scenario.
2. Before the step that adds a row, add a step that finds the row by its `id`.
3. If the step finds the row, update that row.
4. If the step does not find the row, add a new row.

A webhook server must update the row that has the same `id`. To find a request that WalletFeed sent two times, use its `webhook-id` header. Refer to [Webhook format](/docs/webhooks/).

### If your app shows each transaction two times after an import

You imported the same QIF file two times, and a QIF file has no transaction ID.

1. In your app, delete the transactions that you imported the second time.
2. Import each QIF file only one time, after the end of its month.

An OFX file has an ID for each transaction. Actual, GnuCash and Moneydance use this ID and do not import a transaction two times. A CSV file has a **WalletFeed ID** column, but only some apps use it to find copies.

### If a destination shows a transaction two times

WalletFeed finds each transaction by the ID that it wrote, and it adds the transaction again if it cannot find that ID.

WalletFeed keeps the ID in these locations:

- Google Sheets: column A, **WalletFeed ID**
- Airtable, Notion and Coda: the **WalletFeed ID** field, property or column
- PocketSmith: the `wf:` note
- Linear: the **WalletFeed ID** row and the WalletFeed attachment, in the team that you selected

In Notion, WalletFeed also cannot find a row that you moved to the archive.

1. In the service, find the two copies of the transaction.
2. Delete the copy that has no ID, or a changed ID.
3. Do not change or delete the ID of the other transactions.

## Send an email to support

If the steps on this page do not correct the problem, send an email to [support@walletfeed.app](mailto:support@walletfeed.app). In the email, include these items:

- The model of your iPhone
- The version of iOS on your iPhone
- For a problem with a destination, the type of destination, for example Google Sheets

Do not send API keys, tokens or the details of your transactions. In WalletFeed, **Settings** › **Support** opens the support page.
