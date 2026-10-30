# Send Apple Card transactions to a webhook

WalletFeed sends your Apple Card, Apple Cash and Savings transactions from your iPhone to a webhook. A webhook is an `https://` URL in n8n or on your server. WalletFeed sends each new or changed transaction to that URL as JSON.

## Before you start

For this procedure, you must have:

- An iPhone with iOS 26 or a newer version. WalletFeed is available only in the US.
- Apple Card, Apple Cash or Savings in Wallet on that iPhone.
- WalletFeed with [WalletFeed Pro](/docs/walletfeed-pro/). WalletFeed Pro is a subscription with a 1-week free trial, or a one-time Lifetime purchase.
- An n8n workflow, or a server that can receive HTTPS requests. The URL must start with `https://`.
- A computer for the steps in n8n or on your server.

WalletFeed also sends transactions when your iPhone is away from your home network. Thus, your iPhone must connect to the URL from the internet.

## Step 1: Get a webhook URL

Do the steps for n8n, or the steps for your server.

### Get the URL in n8n

The Webhook node in n8n gives you the URL. With **Header auth**, the node also makes sure that each request has the correct `Authorization` value.

1. On your computer, open n8n.
2. Make a new workflow.
3. Click **Add first step...**.
4. Select the **Webhook** node.
5. In **HTTP Method**, select **POST**.
6. In **Authentication**, select **Header auth**.
7. Make a new Header auth credential.
8. In **Name**, type `Authorization`.
9. In **Value**, type `Bearer`, a space and a long password that you make.
10. Keep a copy of the full value.

    You use this value in WalletFeed in Step 2.
11. Save the credential.
12. In **Respond**, select **Immediately**.

    With **Immediately**, n8n sends the status code when the workflow starts. WalletFeed waits a maximum of 30 seconds for the status code. If the workflow then stops because of an error, WalletFeed does not send the data again.
13. Select **Production URL**.
14. Copy the URL that n8n shows.
15. Click **Publish**.

    Result: n8n shows a window with a name for the version.
16. In that window, click **Publish**.

    Result: n8n starts to receive requests at the **Production URL**.
17. Send the URL and the full header value to your iPhone, for example with AirDrop.

You must use the **Production URL** in WalletFeed. The **Test URL** operates only for 120 seconds after you click **Listen for test event**.

n8n uses only the version of the workflow that you published. If you change the workflow, you must publish it again.

> **Note:** If requests go to your n8n server through a reverse proxy, n8n gets the **Production URL** from the environment variable `N8N_WEBHOOK_URL`. Its value must be your `https://` address. Before n8n 2.35.0, the name of this variable was `WEBHOOK_URL`. From version 2.35.0, n8n also reads `WEBHOOK_URL`, but it writes a message about the previous name in its log.

### Use your server

Your server must do these tasks:

- Accept `POST` requests with a JSON body at an `https://` URL.
- Send a status code from 200 to 299 after the server saves the data. If WalletFeed gets a different code, it sends the same data again at the next sync.
- Use the `id` of each transaction to find a transaction that the server received previously. WalletFeed sends a transaction again when it changes.
- Remove the transactions that have their IDs in `data.deletedIDs`.

[Webhook format](/docs/webhooks/) gives the JSON format and the signature check. In Step 2, you get the secret for the signature check.

## Step 2: Add the webhook in WalletFeed

1. On your iPhone, open WalletFeed.
2. Tap **Destinations**.
3. Tap **+** at the top of the screen.

   ![The empty Destinations screen with the + button at the top.](https://walletfeed.app/guides/apple-card-to-webhook/walletfeed-destinations-empty-pro.webp)

4. Tap **Webhook**, below **Developers**.

   **Webhook** is at the bottom of the list. To find it with the search field, you can type `webhook` or `n8n`.

   Result: WalletFeed shows the **Webhook** screen. If you do not have WalletFeed Pro, it shows **WalletFeed Pro** first.
5. If WalletFeed shows **WalletFeed Pro**, get [WalletFeed Pro](/docs/walletfeed-pro/).
6. To give the destination a different name, for example n8n, type the name in **Name**.

   ![The Webhook screen in WalletFeed with Name, the URL field, Authorization (Optional), Share Signing Secret, Send Test and the Webhook Format link.](https://walletfeed.app/guides/apple-card-to-webhook/walletfeed-setup-webhook.webp)

7. Paste the URL into the field that shows `https://example.com/hook`.

   If the URL does not start with `https://`, you cannot tap **Send Test** or **Add**.
8. If you use n8n, paste the full header value into **Authorization (Optional)**.
9. If you do not use n8n, and your server examines the `Authorization` header, type the header value into **Authorization (Optional)**.
10. If your server does not examine the signature, go to step 14. For example, n8n with **Header auth** does not examine it.
11. Tap **Share Signing Secret**.

    Result: Your iPhone shows the share sheet. The secret starts with `whsec_`.
12. Tap **Copy**.
13. Add the secret to your server.
14. Tap **Send Test**.

    Result: WalletFeed sends one test transaction of $4.20 from the merchant WalletFeed. If the server accepts it, WalletFeed shows a green check mark.

    If the server does not accept it, WalletFeed shows the error below **Send Test**. In n8n, the **Executions** tab of the workflow shows the test.
15. Tap **Add**.

    Result: WalletFeed shows **Send Transactions to Your Server?** with a message. The message tells you the data that your server receives. It also gives the Wallet accounts and the start date.

    If you tap **Cancel**, WalletFeed removes the new destination and does not send data.
16. Tap **Send**.

    Result: WalletFeed starts to send transactions to the URL.

    ![The Destinations screen with the n8n webhook destination and three other destinations.](https://walletfeed.app/guides/apple-card-to-webhook/walletfeed-destinations.webp)

## Data that the webhook receives

WalletFeed sends each change to the URL as an HTTP `POST` request with a JSON body. One request contains a maximum of 100 transactions. The body has these items:

- `type` is `transactions.changed`. For **Send Test**, the value is `walletfeed.test`.
- `timestamp` is the date and time when WalletFeed sent the request.
- `data.upserted` is a list of the new and changed transactions.
- `data.deletedIDs` is a list of the IDs of the transactions to remove.

WalletFeed does not send the IDs to remove in the same request as the new and changed transactions. Thus, in each request, one of the two lists is empty.

This table shows the fields of each transaction in `data.upserted`.

| WalletFeed sends | JSON field |
| --- | --- |
| Transaction ID, which stays the same when the transaction changes | `id` |
| ID and name of the Wallet account, for example Apple Card | `accountID`, `accountName` |
| `liability` for Apple Card, or `asset` for Apple Cash and Savings | `accountType` |
| Date and time of the transaction | `date` |
| Date and time when the charge posted, if Wallet gives it | `postedDate` |
| Amount, as a positive number | `amount` |
| `debit` for purchases and fees, or `credit` for refunds, payments and deposits | `direction` |
| Currency code, for example `USD` | `currencyCode` |
| Amount and currency of a purchase in a different currency | `foreignAmount`, `foreignCurrencyCode` |
| Description from Wallet | `description` |
| Description from the card network | `originalDescription` |
| Merchant name, if Wallet has it | `merchantName` |
| Merchant category code (MCC), if Wallet has it | `merchantCategoryCode` |
| WalletFeed category, for example `dining` or `groceries` | `category` |
| Wallet status: `authorized`, `pending`, `booked` or `memo` | `status` |
| Transaction type from Wallet, for example `pointOfSale`, `refund`, `billPayment` or `transfer` | `type` |

If Wallet has no value for a field, the transaction does not include that field. The dates use the ISO 8601 format and UTC, for example `2026-10-30T06:29:40Z`.

Each request also has the Standard Webhooks headers `webhook-id`, `webhook-timestamp` and `webhook-signature`. The `User-Agent` header is `WalletFeed-Webhooks/1`. If you typed a value in **Authorization**, the request has that value in the `Authorization` header.

WalletFeed sends the data from your iPhone directly to the URL. WalletFeed has no account and no WalletFeed servers. It keeps the URL, the **Authorization** value and the secret in the Keychain on your iPhone. The server or service that receives the data keeps it. The terms of that service are applicable to the data.

### Get one item for each transaction in n8n

The Webhook node puts the JSON in `body`. To get one n8n item for each transaction, do these steps:

1. After the Webhook node, add a **Split Out** node.
2. In **Field to Split Out**, type `body.data.upserted`.
3. Click **Publish**.
4. In the window, click **Publish**.

The IDs of the transactions to remove are in `body.data.deletedIDs`.

The request from **Send Test** also starts the workflow. In that request, `body.type` is `walletfeed.test`.

## New and changed transactions

While WalletFeed is open, the webhook receives changes in seconds. When WalletFeed is closed, iOS starts WalletFeed in approximately 1 hour or less after a change in Wallet. Then WalletFeed sends the change. For this, [Background Sync](/docs/background-sync/) must be on in **Settings** › **Sync**.

Wallet shows a new charge as pending until the charge posts. WalletFeed sends it with `pending` or `authorized` in `status`. When the charge posts, WalletFeed sends the same `id` again with `booked` in `status` and the posted amount. To keep one item for each transaction, you must change the item that has the same `id`. If Wallet gives the posted charge a new ID, WalletFeed sends the previous ID in `deletedIDs` and the new transaction in `upserted`.

If **Include Pending** is off in the filter, WalletFeed sends charges only after they post. [Send only some transactions](#send-only-some-transactions) tells you how to set the filter.

A refund is a different transaction. Its `direction` is `credit`. If Wallet shows a charge as declined or expired, or removes a transaction, WalletFeed sends the ID of that transaction in `deletedIDs`.

If the server does not send a status code from 200 to 299, WalletFeed sends the same changes again at the next sync. Thus, the server can receive the same data two times. Two requests with the same data have the same `webhook-id`. The `webhook-timestamp` header, the `timestamp` value and the signature are different in each request.

## Send previous transactions

A new destination also receives previous transactions, from the start date in **Settings** › **Sync** › **Initial History**. **Initial History** is **All** until you change it. To start from a different date, you must set **Initial History** before you add the webhook.

To send more previous transactions after you add the webhook, use [Send History](/docs/send-history/):

1. In **Destinations**, tap the webhook destination.
2. Tap **Send History**.
3. Tap **30 Days**, **90 Days**, **1 Year** or **All**.

   Result: WalletFeed shows **Sending History** and a progress bar.

WalletFeed uses `transactions.changed` requests for previous transactions, and it sends the newest transactions first. It sends them in groups of approximately 500 and waits 1 second between groups. Each request contains a maximum of 100 transactions. n8n starts the workflow one time for each request.

To stop **Send History**:

1. In the destination, tap **Send History**.
2. Tap **Stop Sending**.

## Change or remove the destination

### Send only some transactions

1. In **Destinations**, tap the webhook destination.
2. Set **Filter** to on.
3. Set the filter controls. The table that follows gives each control and its result.

| Control | WalletFeed sends |
| --- | --- |
| **Include** | All transactions, only purchases or only credits. |
| **Minimum** | Only transactions of this amount or more. |
| **Include Pending** | If it is off, charges only after they post. |
| **Accounts** | Only transactions from the Wallet accounts that you select. |
| **Categories** | Only transactions in the categories that you select. |
| **Exclude** | No transactions from the merchants that you type. Put a comma between the merchants. |

If Apple Intelligence is on, you can also type a rule, for example "Travel over $50, not Uber". When you tap the Apple Intelligence symbol, WalletFeed makes the filter from the rule. For more data about the filter, refer to [Choose what to send](/docs/choose-what-to-send/).

WalletFeed uses the filter only for the transactions that it sends after you set the filter.

### Change the URL

1. In **Destinations**, tap the webhook destination.
2. Tap **URL**.

   Result: WalletFeed shows **Webhook URL** with the URL that the destination uses.
3. Delete the URL in the field.
4. Paste the new URL.

   If the URL does not start with `https://`, you cannot tap **Save**.
5. Tap **Save**.

   Result: WalletFeed starts a sync with the new URL.

The **URL** row shows only the server name from the URL. WalletFeed does not send the previous transactions to the new URL. You can send them with **Send History**.

### Change the Authorization value

1. In **Destinations**, tap the webhook destination.
2. Tap **Authorization**.
3. Delete the value in the field.
4. Type or paste the new value.
5. Tap **Save**.

If the field is empty when you tap **Save**, the destination has no value, and **Authorization** shows **None**.

You can get the secret again with **Share Signing Secret** in the destination. The destination always uses the same secret.

### Stop or delete the destination

To stop the destination for a period, set **Enabled** to off in the destination.

To delete the destination, do these steps:

1. In **Destinations**, tap the webhook destination.
2. Tap **Delete**.
3. Tap **Delete** again.

The transactions that WalletFeed sent stay on your server or in n8n.

If you do not use the n8n workflow again, do these steps in n8n:

1. Open the menu adjacent to **Publish**.
2. Select **Unpublish**.

## If there is a problem

### If you cannot tap Send Test or Add

**Send Test** and **Add** operate only with a full URL that starts with `https://`. For **Add**, a name is also necessary.

1. Make sure that the URL starts with `https://` and has a server name after it.
2. Make sure that **Name** is not empty.

### If WalletFeed shows "Rejected (HTTP 404)"

The server has no webhook at the URL. For example, the URL is the n8n **Test URL**, you did not publish the workflow, or **HTTP Method** is not **POST**. On the Webhook screen, **Send Test** shows "The server returned an error (HTTP 404)." for this problem.

1. In the n8n Webhook node, make sure that **HTTP Method** is **POST**.
2. Make sure that you published the workflow after your last change.
3. In the Webhook node, select **Production URL**.
4. Copy the URL again.
5. In WalletFeed, do the steps in [Change the URL](#change-the-url).
6. In the destination, tap **Send Test**.
7. If WalletFeed shows "Rejected (HTTP 404). Check the destination, then try again." below **Sending History**, tap **Try Again**.

If the HTTP code is not 404, the server did not accept the request because of a different problem. To find the problem, examine the log of your server, or the **Executions** tab in n8n.

### If the destination shows "Authentication failed"

The server did not accept the **Authorization** value (HTTP 401 or 403). In n8n, this problem occurs if the value is not the same as **Value** in the Header auth credential.

1. In **Destinations**, tap the destination.

   ![The n8n destination in WalletFeed, which shows Authentication failed below Last Sync and None for Authorization.](https://walletfeed.app/guides/apple-card-to-webhook/walletfeed-destination-failure.webp)

2. Tap **Authorization**.
3. Delete the value in the field.
4. Type the full header value from **Value** in n8n.
5. Tap **Save**.
6. If WalletFeed shows "Authentication failed. Check the connection." below **Sending History**, tap **Try Again**.

### If the destination shows "Can't connect"

Your iPhone cannot connect to the URL, or the server did not send a status code in 30 seconds. For example, the server is off, or the URL operates only on your home network.

1. Make sure that your server or n8n is on.
2. On your iPhone, set Wi-Fi to off.
3. In the destination, tap **Send Test**.

   If WalletFeed shows an error, the URL operates only on your home network. You must use a URL that operates from the internet.
4. Set Wi-Fi to on again.
5. In n8n, make sure that **Respond** is **Immediately**.

WalletFeed sends the changes again at the next sync.

### If the destination shows "Server error"

The server sent a status code of 500 or more. The destination shows the code, for example "Server error (500)". WalletFeed sends the same changes again at the next sync.

1. Examine the log of your server, or the **Executions** tab of the workflow in n8n.
2. Correct the error.
3. In the destination, tap **Send Test**.

### If the server receives a transaction two times

WalletFeed sends a transaction again when it changes, for example when a pending charge posts. It also sends a request again if it did not get a status code from 200 to 299.

1. Find the item that has the same `id` as the transaction.
2. Change that item. Do not add a new item.
3. To find a request that the server received two times, compare the `webhook-id` headers.

### If the webhook does not receive new transactions

WalletFeed does not send to the URL. For example, the destination is off, or **Background Sync** is off.

1. Open WalletFeed. While WalletFeed is open, it sends changes in seconds.
2. If **Destinations** shows **Sync Requires Pro**, tap **Upgrade**.
3. If the destination shows **Off**, set **Enabled** to on in the destination.
4. If **Filter** is on, make sure that the filter includes the transaction.
5. In n8n, make sure that you published the workflow.
6. In WalletFeed, tap **Settings** (the gear button) at the top of **Destinations**.
7. Make sure that **Background Sync** is on.
8. Tap **Sync Now**.

After your iPhone starts again, WalletFeed cannot send to destinations until you type your passcode one time.

To make sure that the connection operates, tap **Send Test** in the destination. If the server accepts the test transaction, WalletFeed shows a green check mark.
