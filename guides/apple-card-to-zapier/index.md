# Send Apple Card transactions to Zapier

WalletFeed sends your Apple Card, Apple Cash and Savings transactions from your iPhone to Zapier. You make a Zap with a **Catch Hook** trigger in Zapier, then you paste the webhook URL of the trigger in WalletFeed.

## Before you start

You must have these items:

- An iPhone with iOS 26 or a newer version. WalletFeed is available only in the US.
- WalletFeed on your iPhone. WalletFeed must have access to your Apple Card, Apple Cash or Savings account.
- [WalletFeed Pro](/docs/walletfeed-pro/) (a subscription with a 1-week free trial, or a one-time Lifetime purchase). WalletFeed Pro is necessary for all destinations.
- A Zapier account on a Professional, Team or Enterprise plan. These plans include **Webhooks by Zapier**. The Free plan of Zapier does not include it.
- A computer for the steps on the Zapier website.

> **Note:** A new Zapier account starts with a 14-day Professional trial. A payment card is not necessary for the trial. During the trial, you can use **Webhooks by Zapier**. After the trial, the account changes to the Free plan. Then your Zap cannot use **Webhooks by Zapier**.

## Your URL stays on your iPhone

- WalletFeed keeps the webhook URL in the Keychain on your iPhone. iOS encrypts the Keychain.
- The webhook URL does not go to iCloud Keychain or to your other devices.
- WalletFeed has no account, and no WalletFeed server keeps the webhook URL. No person at WalletFeed can see or get the webhook URL.
- Your iPhone sends the webhook URL only to Zapier, in each request to Zapier.
- When you delete the destination, WalletFeed deletes the webhook URL from your iPhone.

## Monthly or Each Transaction

In WalletFeed, a Zapier destination has two values for **Send**:

| **Send** | Zapier receives |
| --- | --- |
| **Monthly** | One event for each month, with all the transactions of that month. The Zap starts one time for each month. |
| **Each Transaction** | One event for each new transaction and for each change to a transaction. The Zap starts one time for each event. |

When you add a Zapier destination, **Send** is **Monthly** until you change it. A Zapier destination from WalletFeed 1.0 keeps **Each Transaction**. You can change **Send** after you add the destination (refer to [Change Send](#change-send)).

With **Monthly**, WalletFeed sends each month 5 days after the month ends. It sends the month the first time that it sends data on or after the 6th day of the next month, in your time zone. Thus, most charges from the end of the month have posted.

## Step 1: Make a Zap with a Catch Hook trigger

The Catch Hook trigger has a webhook URL. When WalletFeed sends data to this URL, the Zap starts.

1. On your computer, open [Zapier](https://zapier.com/app/home).
2. If you have a Zapier account, get access to it.
3. If you do not have a Zapier account, make an account on [Zapier's sign-up page](https://zapier.com/sign-up).
4. Click **+** at the top of the left sidebar.

   ![The Zapier home page, with the + button at the top of the left sidebar highlighted.](https://walletfeed.app/guides/apple-card-to-zapier/zapier-home-create.webp)

5. Click **Zaps**.
6. Click the **Trigger** box.
7. In the search box, type `Webhooks`.
8. Click **Webhooks**. Zapier then shows the app as **Webhooks by Zapier**.

   ![The app list in Zapier, with Webhooks in the search box and the Webhooks result highlighted.](https://walletfeed.app/guides/apple-card-to-zapier/zapier-search-webhooks.webp)

9. Under **Trigger event**, click **Choose an event**.
10. Click **Catch Hook**. Do not click **Catch Raw Hook**.

    With **Catch Raw Hook**, the Zap gets all the changes of one request in one run.

    ![The list of Webhooks by Zapier trigger events, with Catch Hook highlighted.](https://walletfeed.app/guides/apple-card-to-zapier/zapier-catch-hook.webp)

11. Click **Continue**.

    Zapier can show a box about **API by Zapier**. WalletFeed does not use **API by Zapier**. You can close the box with **×**.

12. On the **Configure** tab, make sure that the **Pick off a Child Key** field has no text. If this field has text, Zapier keeps only a part of each transaction.
13. Click **Continue**.

    ![The Configure tab with no text in the Pick off a Child Key field, and the Continue button highlighted.](https://walletfeed.app/guides/apple-card-to-zapier/zapier-configure-continue.webp)

14. On the **Test** tab, under **Your webhook URL**, click **Copy**.

    ![The Test tab with the webhook URL, and the Copy button highlighted.](https://walletfeed.app/guides/apple-card-to-zapier/zapier-copy-webhook-url.webp)

    The field shows only the first part of the URL. But **Copy** copies all of the URL.

15. Keep this page open. You will use it again in Step 3.

> **Note:** The URL stays on the **Test** tab of the trigger. You can open the Zap again at a different time and copy the URL.

> **Note:** If you use a Mac with the same Apple Account as your iPhone, you can paste the URL on your iPhone with [Universal Clipboard](https://support.apple.com/en-us/102430).

## Step 2: Add Zapier in WalletFeed

With **Send** set to **Each Transaction**, Zapier receives a maximum of 30 days of previous transactions. If you will use **Each Transaction**, you can set **Initial History** to **Today** before you add Zapier. Then Zapier receives no previous transactions. With **Monthly**, refer to [Send previous transactions](#send-previous-transactions). To set **Initial History**, do these steps:

1. On your iPhone, open WalletFeed.
2. Tap **Settings** (the gear button) at the top of the screen.
3. In the **Sync** section, set **Initial History** to **Today**.

   **Settings** shows the **Sync** section only with WalletFeed Pro.

4. Tap **Done**.

To add Zapier, do these steps:

1. On your iPhone, open WalletFeed.
2. Tap **Destinations**.
3. Tap **+** at the top of the screen.

   ![The Destinations screen in WalletFeed with the + button and no destinations.](https://walletfeed.app/guides/apple-card-to-zapier/walletfeed-destinations-empty-pro.webp)

4. Under **Automations**, tap **Zapier**. You can also type `Zapier` in the search field.
5. If WalletFeed shows the **WalletFeed Pro** screen, get WalletFeed Pro on that screen. WalletFeed then opens the **Zapier** screen.
6. Paste the URL in **Catch Hook URL**.

   ![The Zapier screen in WalletFeed with the Catch Hook URL field, Send set to Monthly, four steps, and the Zapier Help and User Guide links.](https://walletfeed.app/guides/apple-card-to-zapier/walletfeed-setup-zapier.webp)

   Because a person with the URL can start your Zap, WalletFeed keeps the URL in the Keychain on your iPhone.

7. In **Send**, select **Monthly** or **Each Transaction**.

   With **Monthly**, WalletFeed shows “Your Zap runs 5 days after each month ends, with all its transactions.” With **Each Transaction**, WalletFeed shows “Each transaction runs your Zap. Add a filter later to send fewer.”

8. Tap **Add**. WalletFeed sends a sample to Zapier.

   With **Monthly**, the sample is a month with one sample transaction. With **Each Transaction**, the sample is one transaction.

9. Read the message **Send Transactions to Zapier?**

   The message tells you the data that Zapier receives. It also tells you the accounts and the start date of the data. With **Monthly**, the message starts with “Zapier receives one event 5 days after each month ends”.

10. Tap **Send**.

    If you tap **Cancel**, WalletFeed does not add the destination.

**Destinations** then shows the new Zapier destination.

## Step 3: Find the sample in Zapier

1. On your computer, in the Zap editor, click **Test trigger**.
2. Click **request A**.

   ![The Test tab with the record request A highlighted.](https://walletfeed.app/guides/apple-card-to-zapier/zapier-request-found.webp)

   Zapier shows the fields of the sample. With **Each Transaction**, **Merchant** is WalletFeed, and **Amount** is -4.2. With **Monthly**, `event` is `month`, `count` is 1, and `transactions` contains the sample transaction.

3. Click **Continue with selected record**. Zapier then shows the apps for the **Action** step.

## Step 4: Add the Action step in Zapier

The **Action** step uses the data in an app. For example, the step can add a row to a Google Sheets spreadsheet.

1. Select the app that receives the data, for example **Google Sheets**.
2. Do the steps that Zapier shows for this app.
3. If the action must have a value from the transaction, use the fields from Step 3, for example **Merchant** and **Amount**.
4. Click **Publish** at the top right of the editor.
5. In **Automations** › **Zaps**, make sure that the **Status** of your Zap is on.

With **Monthly**, Zapier shows the transactions of the month as line items. To use each transaction, select an action that accepts line items, for example **Create Multiple Spreadsheet Rows** in Google Sheets. You can also use **Looping by Zapier**. Each action in a loop uses tasks.

Each time that the Zap does an action step, it uses one task in Zapier. The trigger uses no task. With **Monthly**, the Zap starts one time for each month. With **Each Transaction**, the Zap starts one time for each new transaction and for each change to a transaction.

**Zap history** in Zapier shows each time that the Zap started, and the tasks that it used.

![The Zap runs tab of Zap history in Zapier, with four runs of the WalletFeed test Zap that each show Successful and 1 task.](https://walletfeed.app/guides/apple-card-to-zapier/zapier-walletfeed-result.webp)

## Data that Zapier receives

Your transactions go from your iPhone directly to Zapier. WalletFeed has no account, and no WalletFeed server keeps your transactions or keys. After Zapier receives your transactions, the terms of Zapier are applicable to them.

With **Monthly**, the event of a month has these fields:

| Field | Value |
| --- | --- |
| `event` | `month` |
| `month` | The month in your time zone, for example 2026-10 |
| `count` | The number of transactions in `transactions` |
| `total` | The sum of the amounts. Purchases are negative. If the month has more than one currency, `total` has no value. |
| `currency` | The currency code of `total`, for example USD. If the month has more than one currency, `currency` has no value. |
| `transactions` | The transactions of the month, newest first. Each transaction has the fields in the subsequent table, but no **Event**. |

If the filter of the destination includes no transactions of a month, Zapier receives no event for that month.

With **Each Transaction**, WalletFeed sends a maximum of 100 changes in one request. Zapier starts the Zap one time for each change. In the Zap, the data of each change has these fields:

| Field in Zapier | Value from Wallet |
| --- | --- |
| **Event** | `created` for a new transaction and for each transaction from **Initial History** or **Send History**, `updated` for each subsequent change, and `deleted` when Wallet removes the transaction |
| **ID** | The transaction ID from Wallet. It stays the same when the transaction changes. |
| **Date** | The date of the purchase in your time zone, for example 2026-10-29 |
| **Merchant** | The merchant name, or the description if Wallet has no merchant name |
| **Amount** | Negative for a purchase, for example -84.12, and positive for a refund or a payment, for example 49 |
| **Currency** | The currency code, for example USD |
| **Category** | The WalletFeed category, for example Groceries |
| **Status** | The Wallet status: `pending`, `authorized` or `booked` |
| **Pending** | `true` while the purchase is pending or authorized, and `false` after the status changes to `booked` |
| **Account** | The Wallet account, for example Apple Card |
| **Description** | The description from Wallet |
| **Type** | The type of transaction, for example `pointOfSale` or `refund` |
| **Mcc** | The merchant category code, for example 5411 |
| **Foreign Amount** and **Foreign Currency** | The amount and the currency code of a purchase in a different currency |
| **querystring** | A field that Zapier adds. It always has no value. |

![A Whole Foods Market transaction from WalletFeed in the Zapier test results, with one field on each line.](https://walletfeed.app/guides/apple-card-to-zapier/zapier-result-transaction-fields.webp)

For a deleted transaction, the data has only **Event** and **ID**. If Wallet does not give a value for a field, the field has no value in Zapier. An example is **Foreign Amount** for a purchase in dollars. In Zapier, an amount has no zeros at the end, for example 49 for $49.00.

## New and changed transactions

With **Each Transaction**, while WalletFeed is open, Zapier receives changes in seconds. When WalletFeed is not open, iOS starts WalletFeed approximately 1 hour or less after a change in Wallet. If [Background Sync](/docs/background-sync/) is on in **Settings** › **Sync**, WalletFeed then sends the change.

**Background Sync** is on until you set it to off.

With **Monthly**, Zapier receives each month one time, 5 days after the month ends. A charge that is pending at that time has `pending` `true`, and Zapier does not receive it again when it posts. Zapier also does not receive a change to a month after it received the month, for example a refund with a date in that month. If WalletFeed stops while it sends a month, Zapier can receive the same month two times. A Zap can use `month` to find a month that it received before.

With **Each Transaction**, one transaction can start the Zap more than one time:

- Zapier receives a new purchase with **Event** `created` and **Status** `pending`.
- When the **Status** changes to `booked`, Zapier receives the same **ID** again with **Event** `updated`.
- If the bank does not accept a pending charge, or Wallet removes a transaction, Zapier receives **Event** `deleted` and the **ID**.

A refund is a different transaction. It has a positive **Amount** and the **Type** `refund`.

With **Each Transaction**, if WalletFeed stops while it sends changes, it sends the same changes again at a subsequent time. Zapier starts the Zap again for each change that it received before. Thus, a Zap that adds a row for each change can add a transaction two times. A Zap that first finds the row by **ID**, and then updates it, keeps one row for each transaction. This Zap uses two tasks for each change.

Zapier can start the Zap for some changes at the same time. Thus, the Zap does not always get the changes in the sequence that WalletFeed sends them.

## Send previous transactions

A new Zapier destination also receives previous transactions from the start date in **Settings** › **Sync** › **Initial History**. **Initial History** is **All** until you change it.

With **Monthly**, a new destination receives all the months from the start date. WalletFeed starts at the first day of the month of the start date. Each previous month is one event, and WalletFeed waits 2 seconds between two months. WalletFeed sends the month in which you add the destination, and each subsequent month, 5 days after the month ends. If you add the destination in the first 5 days of a month, WalletFeed also sends the previous month in this way.

With **Each Transaction**, Zapier receives a maximum of 30 days of previous transactions.

To send transactions from a longer period, use [Send History](/docs/send-history/):

1. In **Destinations**, tap the Zapier destination.
2. Tap **Send History**.
3. Select a period (**30 Days**, **90 Days**, **1 Year** or **All**).

   With **Monthly**, the period starts on the first day of its month.

4. In the message **Send History to Zapier?**, tap **Send**.

   With **Monthly**, the message shows "Each month runs your Zap once." With **Each Transaction**, the message shows "Each transaction runs your Zap."

WalletFeed sends the newest transactions first. With **Monthly**, each month starts the Zap one time. **Send History** does not send again the months that WalletFeed sent 5 days after they ended. With **Each Transaction**, each transaction starts the Zap one time. Each action step uses one task in Zapier.

With **Each Transaction**, **Send History** sends each transaction with **Event** `created`. Thus, Zapier can receive the same transaction two times as `created`.

To stop **Send History**, do these steps:

1. Tap **Send History**.
2. Tap **Stop Sending**.

## Change or remove the destination

### Change Send

1. In **Destinations**, tap the Zapier destination.
2. In **Send**, select **Monthly** or **Each Transaction**.
3. Optional: If you selected **Each Transaction** and the destination has no filter, tap **Turn On Filter** below **Send**.
4. Tap **Send Test**.

   Result: WalletFeed sends a sample with the data of the new **Send** value.

5. On your computer, open the Zap in Zapier.
6. In the Catch Hook trigger, on the **Test** tab, click **Find new records**.
7. Select the new sample.
8. In the **Action** step, select the fields again.

After you change **Send** to **Monthly**, Zapier receives the month in which you change **Send** 5 days after it ends. This month has all its transactions, also the transactions that Zapier received before. After you change **Send** to **Each Transaction**, Zapier receives the changes from that time. To send previous transactions, use **Send History**.

### Send only some transactions

1. In **Destinations**, tap the Zapier destination.
2. Set **Filter** to on.
3. Change **Include**, **Minimum**, **Include Pending**, **Accounts**, **Categories** or **Exclude**.

For more information, refer to [Choose what a destination receives](/docs/choose-what-to-send/).

To stop the destination for a time, set **Enabled** to off.

### Replace the URL

If you make a new Zap, give its URL to WalletFeed:

1. In Zapier, copy the webhook URL of the new Zap (refer to Step 1).
2. In WalletFeed, open the Zapier destination.
3. Tap **Replace URL**.
4. Paste the new URL in **Catch Hook URL**.
5. Tap **Replace**. WalletFeed sends a sample to the new URL before it keeps the URL.

The destination screen shows **Webhook** with `hooks.zapier.com`. It does not show all of the URL.

### Delete the destination

1. In WalletFeed, open the Zapier destination.
2. Tap **Delete**.
3. In the message, tap **Delete** again.

The transactions that WalletFeed sent stay in Zapier. They also stay in the apps that received them from your Zap.

When the Zap is off or deleted, it does not start for your transactions. But Zapier can accept requests at the URL for some hours, and WalletFeed shows no error.

To delete the Zap, do these steps:

1. Open the Zap in Zapier.
2. Click the Zap name at the top of the editor.
3. Click **Delete**.
4. If Zapier shows a message, click the button that deletes the Zap.

## If there is a problem

### If you cannot tap Add

The text in **Catch Hook URL** is not a full Zapier webhook URL. The URL must start with `https://hooks.zapier.com/hooks/catch/`, and then have the ID of your account and the ID of the hook. If you copy the text in the Zapier field, you get only the first part of the URL.

1. In Zapier, open the **Test** tab of the Catch Hook trigger.
2. Click **Copy**.
3. In WalletFeed, delete the text in **Catch Hook URL**.
4. Paste the URL again.

### If WalletFeed shows "The webhook refused the test"

Zapier did not accept the sample, because the URL is not correct or Zapier stopped the URL.

1. In Zapier, open **Automations** › **Zaps**.
2. If your Zap is not in the list, make a new Zap (refer to Step 1). Then do step 6.
3. Click your Zap in the list.
4. Click the **Catch Hook** trigger.
5. On the **Test** tab, click **Copy**.
6. In WalletFeed, delete the text in **Catch Hook URL**.
7. Paste the URL in **Catch Hook URL**.
8. Tap **Add**.

### If WalletFeed shows "Zapier refused the test (HTTP 404). Turn on the Zap, or copy the URL again."

Zapier did not accept the sample, because the Zap is off or deleted, and Zapier stopped the URL.

1. In Zapier, open **Automations** › **Zaps**.
2. If your Zap is in the list, set its **Status** to on.
3. If your Zap is not in the list, make a new Zap and copy its URL (refer to Step 1).
4. In WalletFeed, paste the URL in **Catch Hook URL** again.
5. Tap **Add** or **Replace** again.

### If the destination shows "Rejected (HTTP 404)"

Zapier did not accept the transactions, because the Zap is off or deleted. After the Zap is off, Zapier can wait some hours before it stops the URL.

1. In Zapier, open **Automations** › **Zaps**.
2. If your Zap is in the list, set its **Status** to on.
3. If your Zap is not in the list, make a new Zap (refer to Step 1).
4. If you made a new Zap, give its URL to WalletFeed (refer to [Replace the URL](#replace-the-url)).

### If Zapier finds no request

You clicked **Test trigger** before WalletFeed sent the sample.

1. In WalletFeed, open the Zapier destination.
2. Tap **Send Test**. WalletFeed sends the sample again.
3. In Zapier, click **Find new records**.

Zapier loads a maximum of 3 records at a time, and it does not always load the newest records. This limit is only for the test. When the Zap is on, it starts for each event.

### If the Zap does not do its action

The Zap is a draft, or it is off. Zapier accepts the requests for the Zap, but the Zap does not do its action. WalletFeed shows no error.

1. In Zapier, open the Zap.
2. Click **Publish**.
3. In **Automations** › **Zaps**, set the **Status** of the Zap to on.

   ![The list of Zaps in Zapier, with the WalletFeed Zap and its Status switch in the off position.](https://walletfeed.app/guides/apple-card-to-zapier/zapier-zap-list-off.webp)

### If the Zap stops after the Zapier trial

After the 14-day trial, the Zapier account is on the Free plan. The Free plan does not include **Webhooks by Zapier**.

1. In Zapier, click **Upgrade** at the top of the page.
2. Select a plan that includes **Webhooks by Zapier**, for example Professional.

### If one transaction makes two rows

The Zap starts for each change to a transaction. WalletFeed can also send the same change two times.

1. In the Zap, before the step that adds a row, add a step that finds the row by **ID**.
2. If the step finds a row, update that row.

### If Zapier receives transactions only while WalletFeed is open

**Background Sync** is off.

1. In WalletFeed, open **Settings** › **Sync**.
2. Set **Background Sync** to on.

[Download WalletFeed on the App Store](https://apps.apple.com/app/apple-store/id6827429675?pt=125538749&ct=site&mt=8)
