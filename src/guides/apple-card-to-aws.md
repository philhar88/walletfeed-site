+++
title = "Send Apple Card transactions to AWS"
nav_title = "AWS"
seo_title = "Apple Card to AWS: S3, SQS, Kinesis, DynamoDB, EventBridge"
description = "Send your Apple Card transactions from your iPhone to Amazon S3, SQS, Kinesis Data Streams, DynamoDB or EventBridge in your AWS account with WalletFeed."
group = "Developers"
order = 10
related = ["guides/apple-card-to-supabase", "guides/apple-card-api"]
updated = 2026-10-30
+++

WalletFeed sends your Apple Card, Apple Cash and Savings transactions from your iPhone to Amazon S3, Amazon SQS, Kinesis Data Streams, DynamoDB or EventBridge in your AWS account. You make a user in AWS with a policy from WalletFeed, then you paste an access key for that user into WalletFeed.

## Before you start

You must have:

- An iPhone with iOS 26 or a newer version
- WalletFeed, with access to your [Wallet accounts](/docs/wallet-accounts/)
- [WalletFeed Pro](/docs/walletfeed-pro/), a subscription with a 1-week free trial, or a one-time Lifetime purchase
- An AWS account that lets you make users and access keys in AWS Identity and Access Management (IAM)
- A web browser, on a computer or on your iPhone.

WalletFeed is available only in the US.

WalletFeed can use only the commercial AWS Regions. It cannot use the AWS GovCloud (US) Regions or the China Regions.

## Step 1: Make the AWS resource

WalletFeed sends your transactions to a bucket, a queue, a stream, a table or an event bus in your AWS account. Each of these is a resource in AWS.

Do the steps for the service that you will use. If you have the resource, go to [Step 2](#step-2-open-the-aws-screen-in-walletfeed).

### Amazon S3: make a bucket

1. On your computer, open the [Amazon S3 console](https://console.aws.amazon.com/s3/).
2. In the navigation bar, select the AWS Region for the bucket.
3. Click **General purpose buckets**.
4. Click **Create bucket**.
5. In **Bucket name**, type a name for the bucket.
6. Do not change the other values on the page. As a result, all four controls in **Block Public Access settings for this bucket** stay on.
7. Click **Create bucket**.
8. Record the bucket name and the code of the region, for example `us-east-1`.

For more information, refer to [Creating a general purpose bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/create-bucket-overview.html) in the AWS documentation.

### Amazon SQS: make a queue

1. On your computer, open the [Amazon SQS console](https://console.aws.amazon.com/sqs/).
2. In the navigation bar, select the AWS Region for the queue.
3. Click **Create queue**.
4. For **Type**, keep **Standard**.
5. In **Name**, type a name for the queue.
6. Click **Create queue**. The **Details** page of the queue opens.
7. Copy the URL of the queue, for example `https://sqs.us-east-2.amazonaws.com/123456789012/MyQueue`.
8. Send the URL to your iPhone, for example with AirDrop.

You can also use a FIFO (first-in-first-out) queue. If the name of the queue has `.fifo` at the end, WalletFeed uses it as a FIFO queue.

For more information, refer to [Creating an Amazon SQS standard queue and sending a message](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/creating-sqs-standard-queues.html).

### Kinesis Data Streams: make a stream

1. On your computer, open the [Kinesis console](https://console.aws.amazon.com/kinesis).
2. In the navigation bar, select the AWS Region for the stream.
3. Click **Create data stream**.
4. Type a name for the stream.
5. Keep the **On-demand** capacity mode, or select **Provisioned**.
6. If you selected **Provisioned**, type the number of shards.
7. Click **Create Kinesis stream**.
8. Wait until the **Status** of the stream changes to **Active**.
9. Record the stream name and the code of the region.

For more information, refer to [Create a stream using the AWS Management Console](https://docs.aws.amazon.com/streams/latest/dev/how-do-i-create-a-stream.html).

### DynamoDB: make a table

WalletFeed can write only to a table with the partition key `id` of the type String, and with no sort key.

1. On your computer, open the [DynamoDB console](https://console.aws.amazon.com/dynamodb/).
2. In the navigation bar, select the AWS Region for the table.
3. Click **Tables**.
4. Click **Create table**.
5. In **Table name**, type a name for the table.
6. In **Partition key**, type `id`.
7. Make sure that the type of the partition key is String.
8. Do not type a value in **Sort key**.
9. For **Table settings**, keep **Default settings**.
10. Click **Create table**.
11. Record the table name and the code of the region.

For more information, refer to [Create a table in DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/getting-started-step-1.html).

### EventBridge: make a rule on the event bus

WalletFeed sends events to the `default` event bus, or to a different event bus that you type in WalletFeed. A rule selects events with an event pattern. EventBridge sends an event to a target only when a rule on the event bus selects the event. Thus, you must make a rule that selects all the events from WalletFeed.

1. Make the resource that will receive the events, for example a queue (refer to [Amazon SQS: make a queue](#amazon-sqs-make-a-queue)).
2. On your computer, open the [EventBridge console](https://console.aws.amazon.com/events/).
3. In the navigation bar, select the AWS Region for the rule.
4. Click **Rules**.
5. Click **Create rule**.
6. Click **Advanced Builder**.
7. In **Name**, type a name for the rule.
8. For **Event bus**, select **AWS default event bus** (the `default` event bus), or the event bus that you will type in WalletFeed.
9. For **Rule type**, select **Rule with an event pattern**.
10. Click **Next**.
11. For **Event source**, select **AWS events or EventBridge partner events**.
12. In the **Creation method** section, for **Method**, select **Custom pattern (JSON editor)**.
13. Copy this pattern:

    ```json
    {"source": ["app.walletfeed"]}
    ```
14. Paste the pattern in **Event pattern**.
15. Click **Next**.
16. For **Target type**, select **AWS service**.
17. For **Select a target**, select the service that receives the events, for example Amazon SQS.
18. Select the resource of that service, for example your queue.
19. Click **Next**.
20. Click **Next** again.
21. Click **Create rule**.
22. Record the code of the region.

For more information, refer to [Creating rules using the Advanced Builder](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-create-rule-wizard.html).

## Step 2: Open the AWS screen in WalletFeed

1. On your iPhone, open WalletFeed.
2. Tap **Destinations**.
3. Tap **+** at the top of the screen.

   ![The Destinations screen with no destinations, and the + button at the top.](app:docs-destinations-empty-pro)
4. Scroll to the **Developers** section at the end of the list.
5. Tap **AWS** (the row that shows **S3, SQS, Kinesis, DynamoDB, EventBridge**).
6. If WalletFeed shows the **WalletFeed Pro** screen, get WalletFeed Pro on that screen. Then the AWS screen opens.
7. Tap **Service**.
8. Tap the service that you used in Step 1, for example **Amazon S3**.
9. If your resource is not in `us-east-1`, replace `us-east-1` in **Region** with the code of its region.
10. If you selected **Amazon S3**, type the bucket name in **Bucket**.

    ![The AWS screen for Amazon S3, with the fields Access Key ID, Secret Access Key, Region, Endpoint, Bucket, Prefix and Format.](app:docs-setup-amazon-s3)
11. If you selected **Amazon S3**, do not type a value in **Endpoint**.
12. If you selected **Amazon SQS**, paste the queue URL in **Queue URL**. WalletFeed uses the region in the queue URL.

    ![The AWS screen for Amazon SQS, with the Queue URL field and the Share IAM Policy button.](app:docs-setup-amazon-sqs)
13. If you selected **Kinesis Data Streams**, type the stream name or the Amazon Resource Name (ARN) in **Stream**.

    ![The AWS screen for Kinesis Data Streams, with the Stream field and the Share IAM Policy button.](app:docs-setup-kinesis-data-streams)
14. If you selected **DynamoDB**, type the table name or ARN in **Table**.

    ![The AWS screen for DynamoDB, with the Table field and the message "The partition key must be a string named id."](app:docs-setup-dynamodb)
15. If you selected **EventBridge**, keep `default` in **Event Bus**, or type the name or ARN of your event bus.

    ![The AWS screen for EventBridge, with the value default in the Event Bus field.](app:docs-setup-eventbridge)

For Amazon S3, you can also change **Prefix** and **Format**. The format is **CSV** or **JSON Lines**. The prefix is the folder in the bucket. Its value is `walletfeed/` until you change it. The policy in Step 3 contains the prefix. Thus, you must set the prefix before you get the policy.

> **Note:** **Endpoint** is for a different storage service that uses the S3 API, for example Cloudflare R2 or Backblaze B2. The IAM steps on this page are only for AWS.

## Step 3: Make an IAM user with the policy

WalletFeed makes an IAM policy for the resource on the AWS screen. The policy lets the access key do only these actions on that resource:

| Service | Actions in the policy |
| --- | --- |
| Amazon S3 | `s3:PutObject` and `s3:DeleteObject` on the prefix in the bucket. WalletFeed deletes only its test file. |
| Amazon SQS | `sqs:SendMessage` on the queue |
| Kinesis Data Streams | `kinesis:PutRecords` on the stream |
| DynamoDB | `dynamodb:BatchWriteItem` and `dynamodb:DescribeTable` on the table |
| EventBridge | `events:PutEvents` on the event bus |

1. In WalletFeed, tap **Share IAM Policy**. iOS shows a menu to send or copy the policy.
2. If you use IAM on your computer, send the policy to your computer, for example with AirDrop.
3. If you use IAM on your iPhone, tap **Copy** in the menu.
4. Open the [IAM console](https://console.aws.amazon.com/iam/) (on your iPhone, you can also tap **Open IAM** on the AWS screen in WalletFeed).
5. Click **Users**.
6. Click **Create user**.
7. In **User name**, type a name for the user, for example `walletfeed`.
8. Click **Next**.
9. On the **Set Permissions** page, click **Next** (you add the policy after you make the user).
10. Click **Create user**.
11. Click **View user**.
12. Click the **Permissions** tab.
13. Click **Add permissions**.
14. Click **Create inline policy**.
15. In the **Policy editor**, select **JSON**.
16. Delete all the JSON in the editor.
17. If you sent the policy to your computer, copy the policy on your computer.
18. Paste the policy from WalletFeed in the editor.
19. Click **Next**.
20. In **Policy Name**, type a name for the policy, for example `walletfeed`.
21. Click **Create policy**.

> **Note:** AWS recommends temporary credentials for a person who uses AWS. For an app that cannot use an IAM role, the AWS documentation gives the steps to make an IAM user. WalletFeed accepts only the access key of an IAM user. It does not accept temporary credentials.

For more information, refer to [Create an IAM user for workloads that can't use IAM roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/getting-started-workloads.html).

## Step 4: Make an access key

1. On the page of the user, click the **Security credentials** tab.
2. In the **Access keys** section, click **Create access key**.
3. On the **Access key best practices & alternatives** page, select **Other**.
4. Click **Next**.
5. Type a description for the key, for example `WalletFeed on iPhone`, or keep the field empty.
6. Click **Create access key**.
7. Click **Show**. AWS shows the secret access key.
8. If you use IAM on your computer, send the access key ID and the secret access key to your iPhone.
9. Keep this page open until WalletFeed has the two values.

> **Note:** AWS shows the secret access key only one time. If you do not have it, you can make a new access key.

For more information, refer to [How an IAM administrator can manage IAM user access keys](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-keys-admin-managed.html).

## Step 5: Paste the key and start to send

1. On your iPhone, open WalletFeed again.
2. If the AWS screen is not open, do Step 2 again.
3. Copy the access key ID.
4. In WalletFeed, paste the access key ID in **Access Key ID**. The first letters of the ID in the field are `AKIA`.
5. Copy the secret access key.
6. In WalletFeed, paste the secret access key in **Secret Access Key**.
7. Tap **Add**. WalletFeed uses the key to do a test of the resource.
8. If WalletFeed shows an error message below **Share IAM Policy**, refer to [If there is a problem](#if-there-is-a-problem).
9. Read the message, for example **Send Transactions to Amazon S3?**

   The message tells you the data that the service will receive, the accounts and the start date.
10. Tap **Send**. WalletFeed adds the destination and starts to send your transactions.

The test after you tap **Add** is different for each service:

- For Amazon S3, WalletFeed writes a test file in the prefix, for example `walletfeed/walletfeed-test.csv`. Then it deletes the file.
- For Amazon SQS, Kinesis Data Streams and EventBridge, WalletFeed sends one test event with the description `WalletFeed test transaction`.
- For DynamoDB, WalletFeed reads the keys of the table. It does not write an item.

If you tap **Cancel** in the message, WalletFeed does not add the destination. The AWS screen stays open.

The name of the new destination contains the name of the service and the name of the resource, for example **Amazon S3 · my-bucket**.

> **Note:** WalletFeed keeps the access key in the Keychain on your iPhone. WalletFeed has no account and no WalletFeed servers. Your transactions go from your iPhone directly to your AWS account. After AWS receives your transactions, the terms of AWS are applicable to them.

## Data that AWS receives

| Service | Data |
| --- | --- |
| Amazon S3 | One file for each month, for example `walletfeed/transactions/2026-10.csv`, or `.jsonl` for JSON Lines. |
| Amazon SQS | One message for each change. The body of the message is the event. |
| Kinesis Data Streams | One record for each change. The data is the event, and the partition key is the `id` of the transaction. |
| DynamoDB | One item for each transaction, with the partition key `id`. A change replaces the item. |
| EventBridge | One event for each change, from the source `app.walletfeed`. The `detail` field is the WalletFeed event. |

In an EventBridge event, `detail-type` is `Transaction Created`, `Transaction Updated` or `Transaction Deleted`.

Each event is a JSON object with these fields:

| Field | Value |
| --- | --- |
| `event` | `created` the first time, then `updated` after each change. `deleted` if a transaction becomes declined or expired, or Wallet removes it. |
| `id` | The WalletFeed ID of the transaction. |
| `date` | The day of the transaction, in the time zone of your iPhone. |
| `merchant` | The merchant name, or the description if Wallet has no merchant name. |
| `amount` | The value of the transaction. For purchases and fees, the value is less than zero. For payments and refunds, it is more than zero. |
| `currency` | The currency code, for example `USD`. |
| `category` | The WalletFeed category, for example `Groceries` or `Dining`. |
| `status` | The status in Wallet, for example `pending`, `authorized` or `booked`. |
| `pending` | `true` when the status is `pending` or `authorized`, and `false` at other times. |
| `account` | The account name, for example Apple Card. |
| `description` | The description of the transaction in Wallet. |
| `type` | The transaction type in Wallet, for example `pointOfSale` or `refund`. |
| `mcc` | The merchant category code. |
| `foreignAmount` | For a purchase in a different currency, the value in that currency. It has the same sign (plus or minus) as `amount`. |
| `foreignCurrency` | The code of that different currency. |

If Wallet does not give a value, the value is `null`, for example `foreignAmount` for a purchase in dollars. A `deleted` event has only `event` and `id`.

WalletFeed sends the test event on one line. The `date` is the day of the test. For Amazon SQS, Kinesis Data Streams and EventBridge, the test event has these values:

```json
{
  "account": "Sample Card",
  "amount": -4.2,
  "category": "Shopping",
  "currency": "USD",
  "date": "2026-10-30",
  "description": "WalletFeed test transaction",
  "event": "created",
  "foreignAmount": null,
  "foreignCurrency": null,
  "id": "00000000-0000-0000-0000-000000000000",
  "mcc": 5734,
  "merchant": "WalletFeed",
  "pending": true,
  "status": "pending",
  "type": "purchase"
}
```

In DynamoDB, each field is an attribute of the item. Strings are type S, numbers are type N, and `true` or `false` is type BOOL. WalletFeed does not write the fields that have no value.

In Amazon S3, a JSON Lines file has one line for each transaction. Each line is an object with the same fields, but with no `event`.

In Amazon S3, a CSV file has 16 columns. The first columns are Date, Posted Date, Merchant, Description, Original Description, Amount, Currency and Direction. The last columns are Status, Type, Category, MCC, Account, Foreign Amount, Foreign Currency and WalletFeed ID.

## New and changed transactions

While WalletFeed is open, AWS receives changes in seconds. When WalletFeed is not open, iOS starts WalletFeed approximately 1 hour or less after a change in Wallet. If [Background Sync](/docs/background-sync/) is on in **Settings** › **Sync**, WalletFeed then sends the change. **Background Sync** is on until you set it to off.

When the status of a pending transaction changes to `booked`, WalletFeed sends the same transaction again. If a transaction becomes declined or expired, or if Wallet removes it, WalletFeed sends a `deleted` event. A refund is a different transaction, and its `amount` is more than zero.

In Amazon S3, when a month has a change, WalletFeed replaces the file of that month with a new file. The new file does not contain the deleted transactions. In DynamoDB, a change replaces the item, and a `deleted` event deletes the item. Thus, Amazon S3 and DynamoDB keep one copy of each transaction.

Amazon SQS, Kinesis Data Streams and EventBridge can receive the same event more than one time. You can use `id` to find the transaction in your data. If the `event` and `status` did not change, you can ignore the event. If WalletFeed sends a transaction to a FIFO queue again with no changes in 5 minutes or less, the queue ignores it.

If AWS does not accept some records, WalletFeed sends them again after 1 second. If AWS does not accept them again, the destination shows "AWS rejected" and the number of records. WalletFeed tries to send the records again when it sends more changes.

## Send previous transactions

A new destination also receives previous transactions from the start date in **Settings** › **Sync** › **Initial History**. **Initial History** is **All** until you change it.

To send transactions from a different period, use [Send History](/docs/send-history/):

1. In WalletFeed, tap **Destinations**.
2. Tap the AWS destination (the first part of its name is the name of the service, for example **Amazon S3 ·**).
3. Tap **Send History**.
4. Tap **30 Days**, **90 Days**, **1 Year** or **All**.

Amazon SQS, Kinesis Data Streams and EventBridge receive each transaction again, as a `created` event. Amazon S3 and DynamoDB keep one copy of each transaction.

To stop **Send History**, tap **Send History** › **Stop Sending**.

## Change or remove the destination

1. In WalletFeed, tap **Destinations**.
2. Tap the AWS destination.

   ![The screen of a Lunch Money destination, with Name, Enabled, Last Sync, Replace Token, Filter, Send History, Send Test and Delete.](app:docs-destination-detail)

The screen of an AWS destination has the same controls, but it has no **Replace Token**. It shows the resource, for example **Bucket** or **Queue**. Below the resource, it shows **Region**, **Share IAM Policy** and **Replace Key**.

To send only some transactions:

1. Set **Filter** to on.
2. Select the transactions with **Accounts**, **Categories**, **Minimum** and the other controls.

For more information, refer to [Choose what to send](/docs/choose-what-to-send/).

To stop the destination but keep it, set **Enabled** to off.

To use a different access key:

1. Tap **Replace Key**.
2. Paste the access key ID in **Access Key ID**.
3. Paste the secret access key in **Secret Access Key**.
4. Tap **Replace**.

When you tap **Replace**, WalletFeed does the same test that it does after you tap **Add**. WalletFeed keeps the new key only if the test is satisfactory. For Amazon SQS, Kinesis Data Streams and EventBridge, WalletFeed sends one test event.

You cannot change the region or the resource of a destination. You can have more than one AWS destination, for example a bucket and a queue.

To use a different resource:

1. Do Step 1 thru Step 5 again for the new resource.
2. Delete the destination that you do not use.

To remove the destination:

1. Tap **Delete**.
2. Tap **Delete** again.

WalletFeed tells you "Transactions already sent stay at the destination." The data stays in your AWS account until you delete it in AWS.

If no destination uses the access key, delete the key in IAM:

1. In the IAM console, click **Users**.
2. Click the name of the user.
3. Click the **Security credentials** tab.
4. In the **Access keys** section, click **Actions** for the key.
5. Click **Deactivate**.
6. In the dialog, click **Deactivate** again.
7. Click **Actions** for the key.
8. Click **Delete**.
9. In the dialog, type the access key ID.
10. Click **Delete**.

## If there is a problem

### If you cannot tap Add

WalletFeed lets you tap **Add** only when all the necessary fields have a value. **Region** must contain only letters, numbers and hyphens.

1. Make sure that **Access Key ID** and **Secret Access Key** are not empty.
2. Make sure that **Region** has a code, for example `us-east-1`, and not a name, for example US East.
3. For Amazon S3, make sure that **Bucket** is not empty.
4. If **Endpoint** has a value, make sure that its first part is not `http://`. WalletFeed accepts only HTTPS.
5. For Amazon SQS, paste all of the queue URL again. The first part of the URL is `https://sqs.`.
6. For Kinesis Data Streams or DynamoDB, make sure that **Stream** or **Table** is not empty.

### If WalletFeed shows "Key rejected"

AWS did not accept the key, or the IAM policy of the user does not let the key do the action. WalletFeed shows the HTTP code, for example "Key rejected (HTTP 403). Check the key and its IAM policy."

1. Copy the access key ID.
2. In WalletFeed, paste the access key ID in **Access Key ID**.
3. Copy the secret access key.
4. In WalletFeed, paste the secret access key in **Secret Access Key**.
5. In the IAM console, open the user.
6. On the **Permissions** tab, make sure that the user has the policy from **Share IAM Policy**.
7. If you changed the resource or the region after you got the policy, tap **Share IAM Policy** again.
8. If you got a new policy, replace the policy of the user with the new policy.
9. In WalletFeed, tap **Add**.

### If WalletFeed shows "Wrong region for this bucket."

The bucket is not in the region that **Region** shows.

1. In the Amazon S3 console, find the region of the bucket.
2. In WalletFeed, type the code of that region in **Region**.
3. Tap **Add**.

### If WalletFeed shows "Not found. Check the name and the region."

AWS did not find a bucket with the name in **Bucket**.

1. In WalletFeed, make sure that the name in **Bucket** is the same as the bucket name in AWS.
2. Make sure that **Region** has the code of the region of the bucket.
3. Tap **Add**.

### If WalletFeed shows a message about the partition key

If the DynamoDB table has a different partition key or a sort key, WalletFeed shows "The table's partition key must be a string named id."

1. Make a new DynamoDB table with the partition key `id` of the type String, and no sort key.
2. In WalletFeed, type the name of the new table in **Table**.
3. Tap **Share IAM Policy**.
4. Replace the policy of the user with the new policy.
5. Tap **Add**.

### If WalletFeed shows "Couldn't connect" with HTTP 400

WalletFeed shows "Couldn't connect: The server returned an error (HTTP 400)." AWS did not accept the data from WalletFeed. For example, the name of the queue, the stream, the table or the event bus is incorrect. The resource can also be in a different region.

1. In the AWS console, find the resource and its region.
2. In WalletFeed, type the name of the resource again, or paste the queue URL again.
3. In **Region**, type the code of the region of the resource.
4. Tap **Add**.

### If the destination shows "Authentication failed"

AWS did not accept the key the last time that WalletFeed sent changes. For example, a person deactivated or deleted the key, or removed the policy from the user.

1. In WalletFeed, tap **Destinations**.

   ![The Destinations list, with an n8n destination that shows Authentication failed.](app:docs-destinations-failure)
2. Tap the AWS destination.

   ![The screen of an n8n destination, with Authentication failed below Last Sync.](app:docs-destination-failure)
3. If the user has no policy from WalletFeed, add the policy to the user (refer to [Step 3](#step-3-make-an-iam-user-with-the-policy)).
4. If the user has no active access key, make a new access key (refer to [Step 4](#step-4-make-an-access-key)).
5. Tap **Replace Key**.
6. Paste the access key ID in **Access Key ID**.
7. Paste the secret access key in **Secret Access Key**.
8. Tap **Replace**.

### If the destination shows "AWS rejected" or "AWS throttled"

AWS did not accept some records, and it did not accept them again after 1 second. "AWS throttled" tells you that the resource received data too frequently. WalletFeed tries to send the records again when it sends more changes.

1. In WalletFeed, open the AWS destination.
2. Tap **Send Test**.
3. If **Send Test** shows HTTP 403, do the steps in [If the destination shows "Authentication failed"](#if-the-destination-shows-authentication-failed).
4. If the destination shows the error message again after WalletFeed sends more changes, examine the resource in the AWS console.

### If the EventBridge target receives no events

EventBridge sends an event to a target only when a rule on the event bus selects the event.

1. In the EventBridge console, make sure that the rule is on the same event bus as **Event Bus** in WalletFeed.
2. Make sure that the rule is in the same region as the destination.
3. Make sure that the event pattern of the rule is `{"source": ["app.walletfeed"]}`.
4. In WalletFeed, open the AWS destination.
5. Tap **Send Test**.

### If AWS does not receive new data

WalletFeed sends changes while it is open, or when iOS starts it in the background.

1. Open WalletFeed.
2. Make sure that **Background Sync** is on in **Settings** › **Sync**.
3. Open the AWS destination.
4. Make sure that the destination shows no error message below **Last Sync**.
5. Tap **Send Test**. AWS receives the test transaction with the description `WalletFeed test transaction`.

   For Amazon S3, WalletFeed writes the test file in the prefix, for example `walletfeed/walletfeed-test.csv`, and keeps the file. For DynamoDB, WalletFeed writes an item with the `id` `00000000-0000-0000-0000-000000000000`.
6. For Amazon S3 or DynamoDB, delete the test file or the test item in AWS.
