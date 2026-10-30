# Troubleshooting

WalletFeed shows a message when it cannot read Wallet or send transactions to a destination.

## Correct problems with Wallet and Apple Intelligence

### If WalletFeed does not show your cards

WalletFeed shows only the Wallet accounts that you let it read. It can read only Apple Card, Apple Cash and Savings in the US.

Until you tap **Share** or **Don't Share** on the iOS screen **Share Wallet Data**, **Settings** › **Wallet** shows **Choose Accounts**. To let WalletFeed read your accounts, do these steps:

1. In WalletFeed, tap **Settings** (the gear button) at the top of the screen.
2. In the **Wallet** section, tap **Choose Accounts**.

   ![WalletFeed Settings, with Choose Accounts in the Wallet section.](https://walletfeed.app/docs/troubleshooting/walletfeed-settings.webp)

   Result: iOS shows **Share Wallet Data**.

3. Set the switch to on for each account that you let WalletFeed read.

   ![The Share Wallet Data screen, with switches for Apple Card, Apple Cash and Savings, and the Share button.](https://walletfeed.app/docs/troubleshooting/walletfeed-wallet-access.webp)

4. Tap **Share**.

After you tap **Share** or **Don't Share**, iOS does not show **Share Wallet Data** again. Then **Settings** › **Wallet** shows **Open Settings**. To change the accounts that WalletFeed can read, do these steps:

1. On your iPhone, open the Settings app.
2. Tap **Privacy & Security** › **Wallet** › **WalletFeed**.
3. Select the accounts that you let WalletFeed read.
4. Select the start date of each account.
5. Open WalletFeed.

For more information, refer to [Wallet accounts](/docs/wallet-accounts/).

### If WalletFeed does not show Ask Spending

WalletFeed shows Ask Spending only on an iPhone that can use Apple Intelligence, and only when Apple Intelligence is active.

1. On your iPhone, open the Settings app.
2. Tap **Apple Intelligence & Siri**.
3. Activate Apple Intelligence.
4. Open WalletFeed.
5. Tap **Settings** (the gear button) at the top of the screen.
6. In the **Privacy & Security** section, find **Summarize Spending**.

   ![WalletFeed Settings, with the Summarize Spending switch in the Privacy & Security section.](https://walletfeed.app/docs/troubleshooting/walletfeed-settings-2.webp)

   If WalletFeed shows **Summarize Spending**, WalletFeed can use Apple Intelligence. **Spending** then shows the field **Ask about your spending**.

   If WalletFeed does not show **Summarize Spending**, it cannot use Apple Intelligence at this time.

When **Summarize Spending** is off, **Spending** shows Ask Spending, but Apple Intelligence does not write the Monthly Summary. The Monthly Summary then shows two facts from WalletFeed.

Without Apple Intelligence, you can use **Spending** and **Search**. **Search** then finds the words that you type. For more information, refer to [Ask Spending](/docs/ask-spending/).

## Correct problems with destinations

### If a destination shows "Authentication failed"

The service did not let WalletFeed use the key, the token or the sign-in of the destination.

Some causes are:

- A deleted key
- An expired key
- A key that can only read data, for example a **Read Only** key in Sure.

If you do not select a different **Expiration** when you make a key in BankSync, BankSync stops the key after 90 days.

The destination screen has a button that corrects the problem:

| Destination | Button |
| --- | --- |
| A destination with an API key, for example Sure | **Replace Key** |
| A destination with a token, for example Lunch Money | **Replace Token** |
| A destination with a sign-in, for example Google Sheets | **Sign In Again** |
| Zapier or Make | **Replace URL** |
| Webhook | **URL** and **Authorization** |

To use a new key, token or URL, do these steps:

1. In the service, make a new key, token or URL (refer to the guide for the destination in [Destinations](/docs/destinations/)).
2. In WalletFeed, tap **Destinations**.

   ![The Destinations screen, with "Authentication failed" below the n8n destination.](https://walletfeed.app/docs/troubleshooting/walletfeed-destinations-failure.webp)

3. Tap the destination.

   ![The n8n destination screen, with "Authentication failed" below Last Sync, and the URL and Authorization rows.](https://walletfeed.app/docs/troubleshooting/walletfeed-destination-failure.webp)

4. Tap **Replace Key**, **Replace Token** or **Replace URL**.
5. Paste the new key, token or URL.
6. Tap **Replace**.

For a webhook, do steps 1, 2 and 3. Then do these steps:

1. Tap **URL** or **Authorization**.
2. Type the new value.
3. Tap **Save**.

A destination with a sign-in can also show "Signed out. Sign in again in the destination's settings." To correct this problem, do these steps:

1. In WalletFeed, tap **Destinations**.
2. Tap the destination.
3. Tap **Sign In Again**.
4. Get access to the same account that you used for the destination.

It is not necessary to delete the destination. After you correct the problem, WalletFeed sends the changes that the destination did not receive.

If the destination screen shows **Sending History** and **Try Again**, tap **Try Again**.

### If Destinations shows "Sync Requires Pro"

You do not have WalletFeed Pro at this time. WalletFeed sends transactions to destinations only with WalletFeed Pro.

1. In **Destinations**, tap **Upgrade**.
2. If you have a plan, tap **Restore Purchases** below the plans.

   Result: If the App Store finds your plan, the **WalletFeed Pro** screen closes.

3. If you do not have a plan, select a plan.
4. Complete the purchase.

For the plans, refer to [WalletFeed Pro](/docs/walletfeed-pro/).

### If a destination shows "Off"

On the destination screen, **Enabled** is off. Thus, WalletFeed does not send transactions to the destination.

1. In **Destinations**, tap the destination.
2. Set **Enabled** to on.

   ![The Lunch Money destination screen, with the Enabled switch on.](https://walletfeed.app/docs/troubleshooting/walletfeed-destination-detail.webp)

### If destinations receive changes only while WalletFeed is open

**Background Sync** is off, or your iPhone started again and you did not type its passcode after that.

While WalletFeed is open, destinations receive changes in seconds. When WalletFeed is not open, iOS starts WalletFeed approximately 1 hour or less after a change in Wallet.

WalletFeed shows the **Sync** section in **Settings** only with WalletFeed Pro.

1. In WalletFeed, tap **Settings** (the gear button) at the top of the screen.
2. In the **Sync** section, set **Background Sync** to on.

   ![WalletFeed Settings, with the Background Sync switch on in the Sync section.](https://walletfeed.app/docs/troubleshooting/walletfeed-background-sync.webp)

3. After your iPhone starts again, type its passcode one time.

For more information, refer to [Background Sync](/docs/background-sync/).

To send each purchase seconds after you tap your iPhone to make the purchase, do these steps:

1. In **Settings** › **Sync**, tap **Automations**.

   ![The Automations screen, with the steps for After Each Card Tap.](https://walletfeed.app/docs/troubleshooting/walletfeed-automations.webp)

2. In **After Each Card Tap**, do the steps on the screen.

### If you get the notification "Sync Stopped"

For 3 days, WalletFeed did not send the changes to all your destinations correctly, and **Remind If Sync Stops** is on in **Settings** › **Sync**.

The notification tells you "WalletFeed hasn't synced in 3 days. Open it to catch up."

1. Open WalletFeed.

   Result: WalletFeed sends the changes to your destinations.

2. Tap **Destinations**.
3. If a destination shows a message, find the message on this page.

If you do not let WalletFeed send notifications, **Remind If Sync Stops** stays off.

### If a destination shows "Can't open the folder. Choose it again."

At this time, WalletFeed cannot open the folder that contains the CSV, OFX or QIF file.

1. In WalletFeed, tap **Destinations**.
2. Tap the destination.
3. Tap **Change Folder**.
4. Select the same folder again.
5. If WalletFeed shows "Couldn't open this folder.", select a different folder.

After you select the folder, WalletFeed saves all the transactions of the destination in the folder again.

### If a file changes only when you open WalletFeed

WalletFeed did not get access to the folder in the background. WalletFeed does not show a message for this problem.

1. Open WalletFeed.

   Result: WalletFeed changes the file while WalletFeed is open.

iOS can also start WalletFeed to change the file while your iPhone gets power from a charger. An automation from **Settings** › **Sync** › **Automations** also changes the file.

### If BankSync does not make the Apple Card table

BankSync did not make the table in approximately 30 seconds, for example because the workspace is at the table limit of its plan.

WalletFeed shows "You're signed in, but BankSync hasn't created or shared the Apple Card table." The message also gives the table limit of your plan, for example "The Free plan allows one table."

1. Tap **Open BankSync**.
2. In BankSync, delete a table that you do not use, or select a plan that has more tables.
3. In WalletFeed, tap **Try Again**.
4. If WalletFeed does not show the message again, tap **Add**.

If WalletFeed shows the message again, do these steps:

1. Tap **Sign In Again**.
2. In BankSync, give WalletFeed access to the workspace. Only the owner or an admin of the workspace can give this access.
3. In WalletFeed, tap **Add**.

API keys are available only on BankSync's Standard plan or a higher plan. With one of these plans, you can tap **Use an API Key Instead**. For more information, refer to [Send Apple Card transactions to BankSync](/guides/apple-card-to-banksync/).

> **Note:** The **Sign In with BankSync** button uses WalletFeed's referral URL. Below the button, WalletFeed shows "WalletFeed may earn a commission if you pay for BankSync."

## Prevent copies of transactions

### If Zapier, Make or a webhook receives a transaction two times

If WalletFeed stops before it sends all the changes, WalletFeed sends the same changes a second time after it starts again.

Zapier and Make do not find copies. Thus, a Zap or a scenario that adds a row for each change can add a transaction two times. **Send History** also sends previous transactions again.

1. Open the Zap or the scenario.
2. Before the step that adds a row, add a step that finds the row by its `id`.
3. If the step finds the row, update that row.
4. If the step does not find the row, add a new row.

A webhook server must update the row that has the same `id` as the transaction. The server can use the `webhook-id` header to find a request that WalletFeed sent two times. For more information, refer to [Webhook format](/docs/webhooks/).

### If your app shows each imported transaction two times

You imported the same QIF file two times, and a QIF file has no transaction ID.

1. In your app, delete the second copy of each transaction.
2. Import each QIF file only one time, after the end of its month.

An OFX file has an ID for each transaction. Actual, GnuCash and Moneydance use this ID and do not add a transaction two times. A CSV file has a **WalletFeed ID** column, but only some apps use it to find copies.

### If a destination shows a transaction two times

WalletFeed finds each transaction in the destination by its ID. If WalletFeed cannot find that ID, it adds the transaction again.

WalletFeed keeps the ID in these locations:

| Destination | Location of the ID |
| --- | --- |
| Google Sheets | Column A, **WalletFeed ID** |
| Airtable, Notion and Coda | The **WalletFeed ID** field, property or column |
| PocketSmith | The `wf:` note |
| Linear | The **WalletFeed ID** row and the WalletFeed attachment, in the team that you selected |

In Notion, WalletFeed also cannot find a row that you moved to the archive.

1. In the service, find the two copies of the transaction.
2. Delete the copy that has no ID or a changed ID.
3. Do not change or delete the ID of the other transactions.

## Send an e-mail to customer support

If the steps on this page do not correct the problem, send an e-mail to [support@walletfeed.app](mailto:support@walletfeed.app). In the e-mail, include these items:

- The model of your iPhone
- The version of iOS on your iPhone
- The destination that has the problem, for example Google Sheets.

Do not send API keys, tokens or information about your transactions. In WalletFeed, **Settings** › **Support** opens the support page.
