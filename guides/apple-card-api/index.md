# Send Apple Card transactions to your app or server

There is no web API for your Apple Card transactions. Apple lets an app on your iPhone read them with the FinanceKit API, but only after you give your approval.

WalletFeed is an iPhone app that reads your Apple Card, Apple Cash and Savings transactions with FinanceKit. With WalletFeed Pro, it sends each change from your iPhone to your server, AWS, Supabase or BankSync.

## FinanceKit on iPhone

FinanceKit is the part of iOS that lets apps read data from Wallet. It is available only on iPhone. In the US, FinanceKit gives access to your Apple Card, Apple Cash and Savings accounts.

Before an app can read your data, iOS shows your Wallet accounts. You select the accounts that the app can read, and a start date for each account. After that, you can change them in the Settings app, in **Privacy & Security** › **Wallet**.

Apple has no bank feed for your Apple Card transactions, and a server cannot get them from Apple.

If you make an iPhone app, Apple must give approval before your app can use FinanceKit. To get this approval, the app must be in the Finance category of the App Store, for iPhone in the US or the UK. Apple also tells developers that the app must "provide financial management tools". For more information, refer to [FinanceKit on the Apple Developer site](https://developer.apple.com/financekit/).

## Destinations for your app or server

WalletFeed can send your transactions to the destinations in this table:

| Destination | Data that it receives |
| --- | --- |
| **Webhook** | JSON in a `POST` request to your HTTPS URL, with a maximum of 100 transactions in each request |
| **Amazon S3** | One CSV or JSON Lines file for each month, in your bucket |
| **Amazon SQS** | One message for each change |
| **Kinesis Data Streams** | One record for each change |
| **DynamoDB** | One item for each transaction |
| **EventBridge** | One event for each change |
| **Supabase** | One row for each transaction, in a Postgres table in your Supabase project |
| **BankSync** | One row for each transaction, in a BankSync table that your AI agents can read |

In the **Add Destination** list, **Amazon S3**, **Amazon SQS**, **Kinesis Data Streams**, **DynamoDB** and **EventBridge** are all in **AWS**. You can add more than one destination.

These pages give the full procedure for each destination:

- [Send Apple Card transactions to a webhook](/guides/apple-card-to-webhook/)
- [Send Apple Card transactions to AWS](/guides/apple-card-to-aws/)
- [Send Apple Card transactions to Supabase](/guides/apple-card-to-supabase/)
- [Send Apple Card transactions to BankSync](/guides/apple-card-to-banksync/).

## Before you start

You must have:

- An iPhone with iOS 26 or a newer version
- WalletFeed on that iPhone
- [WalletFeed Pro](/docs/walletfeed-pro/), a subscription with a 1-week free trial, or a one-time Lifetime purchase
- For a webhook, a server with an HTTPS URL that your iPhone can connect to from the internet
- For AWS, an AWS account in which you can make an IAM user and an access key
- For Supabase, a Supabase project
- For BankSync, a BankSync workspace in which you are the owner or an admin.

WalletFeed is available only in the US.

## Step 1: Give WalletFeed access to your Wallet accounts

If WalletFeed shows your transactions, go to [Step 2](#step-2-add-the-destination).

1. On your iPhone, open WalletFeed.
2. On the **Welcome to WalletFeed** screen, tap **Continue**. iOS shows your Wallet accounts.

   ![The Welcome to WalletFeed screen, with the Continue button at the bottom.](https://walletfeed.app/guides/apple-card-api/walletfeed-welcome.webp)
3. Select the accounts that WalletFeed can read.
4. For each account, select the start date of the transactions that WalletFeed can read.
5. Tap **Share**. **Transactions** shows the transactions of the accounts that you shared.

If WalletFeed shows **No Cards**, tap **Choose Accounts**. iOS shows your Wallet accounts. Then do steps 3 to 5. For more information, refer to [Choose the Wallet accounts WalletFeed reads](/docs/wallet-accounts/).

## Step 2: Add the destination

1. Tap **Destinations**.
2. Tap **+** at the top of the screen.

   ![The Destinations screen with no destinations, and the + button at the top.](https://walletfeed.app/guides/apple-card-api/walletfeed-destinations-empty-pro.webp)
3. Find the destination in the **Add Destination** list. You can also type its name in the search field.

   ![The Add Destination list, with the Budgeting section and the start of the Sheets & Databases section.](https://walletfeed.app/guides/apple-card-api/walletfeed-add-destination.webp)

   The **Developers** section has **Webhook** and **AWS**. **Supabase** is in **Sheets & Databases**, and **BankSync** is in **Budgeting**.
4. Tap the destination.
5. If WalletFeed shows **WalletFeed Pro**, get WalletFeed Pro. Then WalletFeed shows the setup screen of the destination.

## Step 3: Connect the destination

Do the steps for your destination. WalletFeed keeps each URL, key and secret in the Keychain on your iPhone.

### Webhook

1. **Optional:** In **Name**, type a different name for the destination.

   ![The Webhook screen in WalletFeed, with Name, the URL field, Authorization (Optional), Share Signing Secret, Send Test and the steps.](https://walletfeed.app/guides/apple-card-api/walletfeed-setup-webhook.webp)
2. Type the HTTPS URL of your server in the field that shows `https://example.com/hook`.
3. If your server must get an `Authorization` header, type its value in **Authorization (Optional)**.
4. Tap **Share Signing Secret**. iOS shows the share sheet.
5. Tap **Copy**, or send the secret to your computer, for example with AirDrop.
6. Add the secret to your server. Your server uses the secret to make sure that WalletFeed sent each request.
7. Tap **Send Test**. Your server receives a request with the type `walletfeed.test` and one test transaction.
8. Tap **Add**.

For the JSON fields and the signature check, refer to [Webhook format](/docs/webhooks/). WalletFeed uses [Standard Webhooks](https://www.standardwebhooks.com) signatures.

### AWS

For DynamoDB, the table must have a String partition key with the name `id`, and no sort key.

WalletFeed accepts only the access key of an IAM user. It does not accept temporary keys that have a session token.

1. In **Service**, select **Amazon S3**, **Amazon SQS**, **Kinesis Data Streams**, **DynamoDB** or **EventBridge**.

   ![The AWS screen in WalletFeed, with Service set to Amazon S3, and the Access Key ID, Secret Access Key, Region, Endpoint, Bucket, Prefix and Format fields.](https://walletfeed.app/guides/apple-card-api/walletfeed-setup-amazon-s3.webp)
2. If your service is not in the AWS region `us-east-1`, type its region in **Region**.
3. If you use Cloudflare R2, Backblaze B2 or a different service that is compatible with S3, type its URL in **Endpoint**.
4. Type the value for your service in **Bucket**, **Queue URL**, **Stream**, **Table** or **Event Bus**.
5. Tap **Share IAM Policy**.
6. Send the policy to your computer, for example with AirDrop.
7. On your computer, open [IAM in the AWS console](https://console.aws.amazon.com/iam/home#/users).
8. Make an IAM user that has the policy from WalletFeed.
9. Make an access key for the user.
10. Send the access key ID and the secret access key to your iPhone, for example with AirDrop.
11. In WalletFeed, paste the access key ID in **Access Key ID**.
12. Paste the secret access key in **Secret Access Key**.
13. Tap **Add**. WalletFeed does a test before it adds the destination.

For the test, WalletFeed writes and deletes a test file in S3. For DynamoDB, it makes sure that the table has the correct partition key. SQS, Kinesis Data Streams and EventBridge receive one test event.

### Supabase

1. In your Supabase project, open the **Connect** dialog.
2. If the project has no publishable key, make one in **Settings** › **API Keys**.
3. Copy the project URL and the publishable key. The key starts with `sb_publishable_`.
4. If Supabase is open on your computer, send the URL and the key to your iPhone, for example with AirDrop.
5. In WalletFeed, paste the key in **Publishable Key**.

   ![The Supabase screen in WalletFeed, with the Publishable Key field, the project URL field, Share SQL and the steps.](https://walletfeed.app/guides/apple-card-api/walletfeed-setup-supabase.webp)
6. Paste the project URL in the field below the key. When this field is empty, it shows `https://abcd.supabase.co`.
7. Tap **Share SQL**.
8. Tap **Copy**, or send the SQL to your computer, for example with AirDrop.
9. Paste the SQL in the **SQL Editor** of your Supabase project.
10. Click **Run**.
11. In WalletFeed, tap **Add**.

The SQL makes the table `walletfeed_transactions`. It also adds a policy that lets only this destination read and write the table. WalletFeed does not accept a secret key, which starts with `sb_secret_`.

### BankSync

1. Tap **Sign In with BankSync**.

   ![The BankSync screen in WalletFeed, with Sign In with BankSync and Use an API Key Instead.](https://walletfeed.app/guides/apple-card-api/walletfeed-setup-banksync.webp)
2. On the BankSync page, tap **Continue with Google**, or type your email address in **Email** and tap **Continue with email**.

   ![The BankSync sign-in page with Continue with Google, an Email field and Continue with email.](https://walletfeed.app/guides/apple-card-api/banksync-sign-in-with-banksync.webp)
3. If BankSync has no account for your email address, do the steps on the BankSync page to make one.
4. Give your approval to WalletFeed as the owner or an admin of the workspace. BankSync makes the **Apple Card** table, and WalletFeed shows **Signed In**.
5. Tap **Add**.

The **Sign In with BankSync** button uses WalletFeed's referral link. Below the button, WalletFeed shows the message "WalletFeed may earn a commission if you pay for BankSync."

On the Free plan, a workspace can have only one table. If the workspace has a different table, BankSync cannot make the **Apple Card** table. Then WalletFeed shows **Try Again** and **Open BankSync**.

As an alternative, you can tap **Use an API Key Instead**. API keys are available only on BankSync's Standard plan or a higher plan. In BankSync, the keys are in **Settings** › **Developers** › **API Keys**. [Send Apple Card transactions to BankSync](/guides/apple-card-to-banksync/) gives the steps for an API key.

## Step 4: Start to send transactions

After you tap **Add**, WalletFeed shows a message before it sends data. The message tells you the data that the destination receives. It also gives the accounts and the start date. For a webhook, the title of the message is "Send Transactions to Your Server?"

1. Read the message.
2. Tap **Send**. WalletFeed adds the destination and starts to send your transactions.

If you tap **Cancel**, WalletFeed does not add the destination.

## Transaction data

Each destination receives this data for a transaction:

- An ID that stays the same when the transaction changes
- The account name, for example Apple Card
- The date, the currency and the value of the transaction
- The description, the merchant name and the merchant category code (MCC), if Wallet has them
- The WalletFeed category, for example groceries or travel
- The status in Wallet, for example `pending` or `booked`
- For a purchase in a different currency, the value in that currency.

The table that follows gives the value of a purchase at each destination, and what WalletFeed does when Wallet removes a transaction.

| Destination | Value of a purchase | Removed transaction |
| --- | --- | --- |
| **Webhook** | A number more than zero, with `direction` set to `debit` | WalletFeed puts the ID of the transaction in `deletedIDs`. |
| **Amazon S3** | A number less than zero | WalletFeed writes the file of the month again, without the transaction. |
| **Amazon SQS**, **Kinesis Data Streams**, **EventBridge** | A number less than zero | WalletFeed sends an event with `event` set to `deleted` and only the `id`. |
| **DynamoDB** | A number less than zero | WalletFeed deletes the item. |
| **Supabase** | A number less than zero | WalletFeed deletes the row. |
| **BankSync** | A number less than zero | WalletFeed deletes the row, and BankSync moves it to its trash. |

If you do not change **Prefix** or **Format**, the S3 file for October 2026 is `walletfeed/transactions/2026-10.csv`.

In EventBridge, the `source` of each event is `app.walletfeed`. The `detail-type` is `Transaction Created`, `Transaction Updated` or `Transaction Deleted`.

Your transactions go from your iPhone directly to your server or service. WalletFeed has no account and no WalletFeed servers. After a service has the data, the terms of that service are applicable to the data.

## Sync times and pending charges

- While WalletFeed is open, a destination receives changes in seconds.
- When WalletFeed is closed, iOS starts WalletFeed in approximately 1 hour or less after a change in Wallet. This occurs only if [Background Sync](/docs/background-sync/) is on in **Settings** › **Sync**. **Background Sync** is on until you set it to off.
- A pending charge has the status `pending` or `authorized`. When the status changes to `booked`, the destination receives the transaction again, with the same ID and the value of the booked transaction.
- WalletFeed removes declined charges, expired charges and the transactions that Wallet removes.
- A refund is a different transaction. Its type is `refund`.
- For a webhook, if your server does not send a status code from 200 to 299, WalletFeed sends the same changes again at the next sync.

## Send previous transactions

A new destination also receives previous transactions, from the start date in **Settings** › **Sync** › **Initial History**. **Initial History** is **All** until you change it. WalletFeed sends the transactions from the last date to the first date.

To send previous transactions again, use [Send History](/docs/send-history/):

1. In WalletFeed, tap **Destinations**.
2. Tap the destination.
3. Tap **Send History**.
4. Tap **30 Days**, **90 Days**, **1 Year** or **All**.

While WalletFeed sends the history, you can stop it:

1. Tap **Send History**.
2. Tap **Stop Sending**.

WalletFeed can send only the transactions that iOS lets it read. To let WalletFeed read more previous transactions, change the start date in the Settings app, in **Privacy & Security** › **Wallet** › **WalletFeed**.

## Change or stop the destination

1. In WalletFeed, tap **Destinations**.
2. Tap the destination.

Then do one of these steps:

- To send only some transactions, set **Filter** to on (refer to [Choose what a destination receives](/docs/choose-what-to-send/)).
- To stop the destination for a period, set **Enabled** to off.
- To change the URL or the `Authorization` value of a webhook, tap **URL** or **Authorization**.
- To use a new AWS, Supabase or BankSync API key, tap **Replace Key**.

To remove the destination:

1. Tap **Delete**. WalletFeed shows the message "Transactions already sent stay at the destination."
2. Tap **Delete** again.

To remove the transactions that WalletFeed sent, delete them on your server or in the service.

## If something goes wrong

### If WalletFeed shows "Wallet Access Off"

WalletFeed cannot read Wallet, because you tapped **Don't Share** or you stopped its access in the Settings app.

1. On your iPhone, open the Settings app.
2. Tap **Privacy & Security** › **Wallet** › **WalletFeed**.
3. Select the accounts that WalletFeed can read.
4. Open WalletFeed.

### If WalletFeed does not show your Apple Card transactions

You did not select your Apple Card when iOS showed your Wallet accounts, or you are a participant in Apple Card Family. FinanceKit does not give participants access to the Apple Card account.

1. On your iPhone, open the Settings app.
2. Tap **Privacy & Security** › **Wallet** › **WalletFeed**.
3. Select your Apple Card.
4. Open WalletFeed.

### If the destination shows "Authentication failed"

Your server or the service did not accept the key, the sign-in or the `Authorization` value. The HTTP status code was 401 or 403.

1. In WalletFeed, tap **Destinations**.

   ![The Destinations list, with the destination n8n, which shows Authentication failed.](https://walletfeed.app/guides/apple-card-api/walletfeed-destinations-failure.webp)
2. Tap the destination.

   ![The screen of the webhook destination n8n, with Authentication failed below Last Sync, and the URL and Authorization rows.](https://walletfeed.app/guides/apple-card-api/walletfeed-destination-failure.webp)
3. Do the steps for your destination:

   - For a webhook, tap **Authorization**. Type the correct value. Then tap **Save**.
   - For AWS, tap **Replace Key**. Paste the access key ID and the secret access key. Then tap **Replace**.
   - For Supabase or a BankSync API key, tap **Replace Key**. Paste the correct key. Then tap **Replace**.
   - For Sign In with BankSync, tap **Sign In Again**.

4. Tap **Send Test**.

### If the destination shows "Can't connect"

WalletFeed did not get a response from your server or the service.

1. Make sure that your iPhone can connect to the internet.
2. For a webhook, make sure that your server is on and that it accepts HTTPS requests.
3. In WalletFeed, tap **Destinations**.
4. Tap the destination.
5. For a webhook, tap **URL** to make sure that the URL is correct.
6. Tap **Send Test**.

### If AWS shows "Wrong region for this bucket."

The S3 bucket is in a different AWS region.

1. In **Region**, type the region of the bucket.
2. Tap **Add**.

### If AWS shows "Key rejected"

AWS did not accept the access key, or the IAM policy of the user does not include the necessary action.

1. On your computer, open IAM.
2. Make sure that the user has the policy from **Share IAM Policy**.
3. In WalletFeed, paste the access key ID in **Access Key ID** again.
4. Paste the secret access key in **Secret Access Key** again.
5. Tap **Add**.

### If your software receives an event two times

SQS, Kinesis Data Streams and EventBridge can receive the same event again. This occurs when WalletFeed sends the same changes again. A FIFO queue in SQS removes the second copy of an event if the queue receives it 5 minutes or less after the first copy.

1. In the software that reads the events, use the `id` of the transaction as the key.
2. If an event has the same `event` and `status` as the last event for that `id`, ignore the event.
