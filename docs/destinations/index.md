# Destinations

A destination is an app, a spreadsheet, a file or a server that receives your Apple Card, Apple Cash and Savings transactions from WalletFeed. After you add a destination, WalletFeed sends your new and changed transactions to it from your iPhone.

To send transactions to a destination, you must have [WalletFeed Pro](/docs/walletfeed-pro/). WalletFeed Pro is a subscription with a 1-week free trial, or a one-time Lifetime purchase. You can see the list of destination types without WalletFeed Pro.

## Destination types

**Add Destination** shows the destination types in these sections. Each type has a guide with all the steps:

| Section | Destinations |
|---|---|
| **Budgeting** | [BankSync](/guides/apple-card-to-banksync/), [Lunch Money](/guides/apple-card-to-lunch-money/), [PocketSmith](/guides/apple-card-to-pocketsmith/), [Firefly III](/guides/apple-card-to-firefly-iii/), [Sure](/guides/apple-card-to-sure/), [Toshl Finance](/guides/apple-card-to-toshl/) |
| **Sheets & Databases** | [Google Sheets](/guides/apple-card-to-google-sheets/), [Airtable](/guides/apple-card-to-airtable/), [Notion](/guides/apple-card-to-notion/), [Coda](/guides/apple-card-to-coda/), [Supabase](/guides/apple-card-to-supabase/), [Linear](/guides/apple-card-to-linear/) |
| **Automations** | [Zapier](/guides/apple-card-to-zapier/), [Make](/guides/apple-card-to-make/) |
| **Files** | [CSV File](/guides/apple-card-to-csv/), [OFX File](/guides/apple-card-to-ofx/), [QIF File](/guides/apple-card-to-qif/) |
| **Developers** | [AWS](/guides/apple-card-to-aws/) (Amazon S3, Amazon SQS, Kinesis Data Streams, DynamoDB and EventBridge), [Webhook](/guides/apple-card-to-webhook/) |

**Files** and **AWS** show as one row each. In the setup form, you select the file format in **Format**, or the AWS service in **Service**. OFX and QIF files include a charge only after it posts.

Firefly III and Sure show **Self-hosted**. You install them on a server.

You can add more than one destination of the same type. For example, you can send each Wallet account to a different CSV file.

To find a destination, type its name in the search field at the top of **Add Destination**. The search also finds a file format from the name of an app that uses it. For example, "GnuCash" finds **OFX File** and **QIF File**.

![The Add Destination search with PocketSmith in the search field and PocketSmith as the result.](https://walletfeed.app/docs/destinations/walletfeed-add-destination-search.webp)

## Add a destination

1. On your iPhone, open WalletFeed.
2. Tap **Destinations** at the bottom of the screen.
3. Tap **+** at the top of the screen.

   ![The empty Destinations screen with the + button at the top.](https://walletfeed.app/docs/destinations/walletfeed-destinations-empty-pro.webp)

4. Tap the destination type, for example **Lunch Money**.

   ![The Add Destination screen with the search field, and the Budgeting and Sheets & Databases sections.](https://walletfeed.app/docs/destinations/walletfeed-add-destination.webp)

   If you do not have WalletFeed Pro, the **WalletFeed Pro** screen opens. After you get WalletFeed Pro or tap **Restore Purchases**, the setup form opens.

5. Do the steps in the setup form.

   ![The Lunch Money setup form with the Access Token field, three numbered steps and the Open Developers link.](https://walletfeed.app/docs/destinations/walletfeed-setup-lunch-money.webp)

   The form shows numbered steps below its fields. For all the steps, refer to the guide for the destination type.

6. Tap **Add**.

   WalletFeed shows a message, for example **Send Transactions to Lunch Money?**

   The message tells you which data the destination receives, from which Wallet accounts and from which date.

7. Tap **Send**. For a Files destination, tap **Save**.

   WalletFeed closes **Add Destination** and starts to send transactions to the destination.

If you tap **Cancel** in the message, WalletFeed sends nothing and removes the destination. The setup form stays open, so you can change it. If you close **Add Destination** before you tap **Send**, WalletFeed also removes the destination.

A new destination also receives previous transactions, from the start date in **Settings** › **Sync** › **Initial History**. **Initial History** is **All** until you change it. If **Send** is **Each Transaction** for Zapier, Make or Linear, the destination receives a maximum of 30 days of previous transactions. To send more previous transactions after you add the destination, use [Send History](/docs/send-history/).

> **Note:** WalletFeed has no account and no WalletFeed servers. WalletFeed sends your transactions from your iPhone directly to the service that you select. The key or sign-in for each destination stays in the Keychain on your iPhone.

The service keeps the data that it receives. To know how the service uses your data, refer to the terms of that service.

## Destination status

**Destinations** shows each destination with its status below its name.

![The Destinations screen with three destinations. The n8n webhook shows Authentication failed and an orange exclamation mark.](https://walletfeed.app/docs/destinations/walletfeed-destinations-failure.webp)

The status can be one of these:

| Status | Description |
|---|---|
| A time, for example "2 minutes ago" | The time of the last sync. |
| "Sending history · 46%" | WalletFeed sends previous transactions to the destination. |
| "History paused · 46%" | WalletFeed does not send previous transactions now. Refer to [Send History](/docs/send-history/). |
| "Off" | **Enabled** is off. WalletFeed does not send transactions to the destination. |
| A failure, for example "Authentication failed" | The last sync had a failure. Some failures also tell you what to do. An orange exclamation mark shows on the row. |

## New and changed transactions

While WalletFeed is open, a destination receives changes in seconds. When WalletFeed is closed, iOS starts WalletFeed in approximately 1 hour or less after a change in Wallet.

For changes while WalletFeed is closed, **Background Sync** in **Settings** › **Sync** must be on. Refer to [Background Sync](/docs/background-sync/).

To sync all destinations now, pull down the list in **Destinations**. You can also tap **Settings** › **Sync** › **Sync Now**.

## Change a destination

To open a destination, tap it in **Destinations**.

![The Lunch Money destination with Name, Enabled, Last Sync, Replace Token, Filter, Send History, Send Test and Delete.](https://walletfeed.app/docs/destinations/walletfeed-destination-detail.webp)

The screen of the destination has these rows, from top to bottom:

| Rows | Purpose |
|---|---|
| **Name**, **Enabled** and **Last Sync** | Change the name, stop or start the destination, and see the time and result of the last sync. |
| **Replace Key**, **Replace Token**, **Sign In Again** or **Change Folder** | Repair the connection. The rows are different for each destination type. |
| **Filter** | Send only some transactions. Refer to [Choose what a destination receives](/docs/choose-what-to-send/). |
| **Send History** | Send previous transactions. Refer to [Send History](/docs/send-history/). |
| **Send Test** | Send a sample transaction to the destination. |
| **Delete** | Remove the destination. |

**Last Sync** shows the time of the last sync. If WalletFeed sent transactions in that sync, it also shows the number, for example "1 minute ago · 2 sent". If the last sync had a failure, the failure shows below **Last Sync**.

## Change the name of a destination

1. In **Destinations**, tap the destination.
2. Tap **Name**.
3. Type the new name.

   **Destinations** shows the new name.

## Stop and start a destination

1. In **Destinations**, tap the destination.
2. Set **Enabled** to off.

   In **Destinations**, the destination shows "Off". WalletFeed does not send transactions to it while **Enabled** is off.

To send transactions to the destination again, set **Enabled** to on.

## Send a test

1. In **Destinations**, tap the destination.
2. Tap **Send Test**.

   WalletFeed sends one sample transaction to the destination. If the destination receives it, a green check mark shows next to **Send Test**. If not, the failure shows below **Send Test**.

The sample transaction has the merchant name WalletFeed and the amount 4.20 USD. For a Files destination, WalletFeed writes a test file in the folder, for example `WalletFeed Test.csv`. You can delete the sample from the destination.

## Replace a key or sign in again

If you make a new key in the service, replace the key in WalletFeed. You do not have to remove the destination and add it again.

1. In **Destinations**, tap the destination.
2. Tap the row for the key, for example **Replace Key** or **Replace Token**.
3. Paste the new key.
4. Tap **Replace**.

   WalletFeed examines the new key with the service. If the key is correct, WalletFeed keeps it and shows a check mark.

For other destination types, use these rows at step 2:

- For Google Sheets and BankSync, tap **Sign In Again**.
- For Zapier and Make, tap **Replace URL**, then paste the new webhook URL.
- For a Files destination, tap **Change Folder**, then select the folder again.
- For a Webhook destination, tap **URL** or **Authorization**, type the new value, then tap **Save**.

## Remove a destination

1. In **Destinations**, tap the destination.
2. Tap **Delete**.

   WalletFeed shows a message with the name of the destination, for example **Delete Lunch Money?**

3. Tap **Delete**.

WalletFeed removes the destination and its key from your iPhone. The transactions that WalletFeed sent stay in the service. If you made a key in the service for WalletFeed, you can also delete the key in the service.

In **Destinations**, you can also swipe left on a destination, then tap **Delete**. WalletFeed then removes the destination without a message.

## Remove all destinations

1. In WalletFeed, tap **Settings** at the top of the screen.
2. In the **Data** section, tap **Remove All Destinations**.

   ![The Settings screen with Export CSV and Remove All Destinations in the Data section.](https://walletfeed.app/docs/destinations/walletfeed-settings-4.webp)

3. Tap **Remove All**.

   WalletFeed removes all your destinations. The transactions that WalletFeed sent stay at each destination.

## If something goes wrong

### If a destination shows "Authentication failed"

The service does not let WalletFeed use the key, token or sign-in of the destination. For example, you deleted the key in the service.

1. In **Destinations**, tap the destination.

   ![The n8n destination with Authentication failed below Last Sync, and the URL and Authorization rows.](https://walletfeed.app/docs/destinations/walletfeed-destination-failure.webp)

2. If the destination uses a key, make a new key in the service. For the steps, refer to the guide for the destination type.
3. In WalletFeed, replace the key or sign in again. Refer to [Replace a key or sign in again](#replace-a-key-or-sign-in-again).

### If a destination shows "Can't connect"

WalletFeed cannot connect to the service.

1. Make sure that your iPhone has an internet connection.
2. If the destination is on your server, make sure that the server operates.
3. In **Destinations**, pull down the list.

   WalletFeed syncs the destinations again.

### If a destination shows "Server error"

The service has a problem. WalletFeed does not lose the changes, and sends them at the next sync. To sync again, pull down the list in **Destinations** after some minutes.

### If a destination shows "Off"

The **Enabled** switch is off for the destination.

1. In **Destinations**, tap the destination.
2. Set **Enabled** to on.

### If Destinations shows "Sync Requires Pro"

You do not have WalletFeed Pro now, so WalletFeed does not send transactions to your destinations. Your destinations stay in the list.

1. In **Destinations**, tap **Upgrade**.

   The **WalletFeed Pro** screen opens.

2. Select a plan, or tap **Restore Purchases**.

### If a destination receives changes only while WalletFeed is open

The **Background Sync** switch is off.

1. In WalletFeed, tap **Settings** at the top of the screen.
2. In the **Sync** section, set **Background Sync** to on.

For more information, refer to [Background Sync](/docs/background-sync/).
