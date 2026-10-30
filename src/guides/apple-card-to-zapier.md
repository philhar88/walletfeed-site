+++
title = "Send Apple Card transactions to Zapier"
nav_title = "Zapier"
seo_title = "Apple Card to Zapier: start a Zap from your transactions"
description = "Send your Apple Card transactions from your iPhone to Zapier with WalletFeed. A Catch Hook trigger starts your Zap for each transaction and each change."
group = "Automations"
order = 10
related = ["guides/apple-card-to-make", "guides/apple-card-to-webhook"]
updated = 2026-10-30
+++

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
- WalletFeed has no account and no servers. No person at WalletFeed can see or get the webhook URL.
- Your iPhone sends the webhook URL only to Zapier, in each request to Zapier.
- When you delete the destination, WalletFeed deletes the webhook URL from your iPhone.

## Step 1: Make a Zap with a Catch Hook trigger

The Catch Hook trigger has a webhook URL. When WalletFeed sends data to this URL, the Zap starts.

1. On your computer, open [Zapier](https://zapier.com/app/home).
2. If you have a Zapier account, get access to it.
3. If you do not have a Zapier account, make an account on [Zapier's sign-up page](https://zapier.com/sign-up).
4. Click **+** at the top of the left sidebar.

   ![The Zapier home page, with the + button at the top of the left sidebar highlighted.](web:zapier/01-home-create)

5. Click **Zaps**.
6. Click the **Trigger** box.
7. In the search box, type `Webhooks`.
8. Click **Webhooks**. Zapier then shows the app as **Webhooks by Zapier**.

   ![The app list in Zapier, with Webhooks in the search box and the Webhooks result highlighted.](web:zapier/04-search-webhooks)

9. Under **Trigger event**, click **Choose an event**.
10. Click **Catch Hook**. Do not click **Catch Raw Hook**.

    ![The list of Webhooks by Zapier trigger events, with Catch Hook highlighted.](web:zapier/06-catch-hook)

11. Click **Continue**.

    Zapier can show a box about **API by Zapier**. WalletFeed does not use **API by Zapier**. You can close the box with **×**.

12. On the **Configure** tab, make sure that the **Pick off a Child Key** field has no text. If this field has text, Zapier keeps only a part of each transaction.
13. Click **Continue**.

    ![The Configure tab with no text in the Pick off a Child Key field, and the Continue button highlighted.](web:zapier/08-configure-continue)

14. On the **Test** tab, under **Your webhook URL**, click **Copy**.

    ![The Test tab with the webhook URL, and the Copy button highlighted.](web:zapier/09-copy-webhook-url)

    The field shows only the first part of the URL. But **Copy** copies all of the URL.

15. Keep this page open. You will use it again in Step 3.

> **Note:** The URL stays on the **Test** tab of the trigger. You can open the Zap again at a different time and copy the URL.

> **Note:** If you use a Mac with the same Apple Account as your iPhone, you can paste the URL on your iPhone with [Universal Clipboard](https://support.apple.com/en-us/102430).

## Step 2: Add Zapier in WalletFeed

Before you add Zapier, you can set **Initial History** to **Today**. Then Zapier receives no previous transactions. With a different value, Zapier receives a maximum of 30 days of previous transactions. To set **Initial History**, do these steps:

1. On your iPhone, open WalletFeed.
2. Tap **Settings** (the gear button) at the top of the screen.
3. In the **Sync** section, set **Initial History** to **Today**.

   **Settings** shows the **Sync** section only with WalletFeed Pro.

4. Tap **Done**.

To add Zapier, do these steps:

1. On your iPhone, open WalletFeed.
2. Tap **Destinations**.
3. Tap **+** at the top of the screen.

   ![The Destinations screen in WalletFeed with the + button and no destinations.](app:docs-destinations-empty-pro)

4. Under **Automations**, tap **Zapier**. You can also type `Zapier` in the search field.
5. If WalletFeed shows the **WalletFeed Pro** screen, get WalletFeed Pro on that screen. WalletFeed then opens the **Zapier** screen.
6. Paste the URL in **Catch Hook URL**.

   ![The Zapier screen in WalletFeed with the Catch Hook URL field, three steps and the Zapier Help link.](app:docs-setup-zapier)

   Because a person with the URL can start your Zap, WalletFeed keeps the URL in the Keychain on your iPhone.

7. Tap **Add**. WalletFeed sends a sample transaction to Zapier.
8. Read the message **Send Transactions to Zapier?**

   The message tells you the data that Zapier receives. It also tells you the accounts and the start date of the data.

9. Tap **Send**.

   If you tap **Cancel**, WalletFeed does not add the destination.

**Destinations** then shows the new Zapier destination.

## Step 3: Find the sample in Zapier

1. On your computer, in the Zap editor, click **Test trigger**.
2. Click **request A**.

   ![The Test tab with the record request A highlighted.](web:zapier/11-request-found)

   Zapier shows the fields of the sample. **Merchant** is WalletFeed, and **Amount** is -4.2.

3. Click **Continue with selected record**. Zapier then shows the apps for the **Action** step.

## Step 4: Add the Action step in Zapier

The **Action** step uses the data in an app. For example, the step can add a row to a Google Sheets spreadsheet.

1. Select the app that receives the data, for example **Google Sheets**.
2. Do the steps that Zapier shows for this app.
3. If the action must have a value from the transaction, use the fields from Step 3, for example **Merchant** and **Amount**.
4. Click **Publish** at the top right of the editor.
5. In **Automations** › **Zaps**, make sure that the **Status** of your Zap is on.

Each time that the Zap does an action step, it uses one task in Zapier. The trigger uses no task. The Zap starts one time for each new transaction and for each change to a transaction.

**Zap history** in Zapier shows each time that the Zap started, and the tasks that it used.

![The Zap runs tab of Zap history in Zapier, with four runs of the WalletFeed test Zap that each show Successful and 1 task.](web:zapier/90-walletfeed-result)

## Data that Zapier receives

Your transactions go from your iPhone directly to Zapier. WalletFeed has no account and no WalletFeed servers. After Zapier receives your transactions, the terms of Zapier are applicable to them.

In the Zap, the data of each change has these fields:

| Field in Zapier | Value from Wallet |
| --- | --- |
| **Event** | `created` for a new transaction and for each transaction from **Send History**, `updated` for each subsequent change, and `deleted` when Wallet removes the transaction |
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

![A Whole Foods Market transaction from WalletFeed in the Zapier test results, with one field on each line.](web:zapier/13-result-transaction-fields)

For a deleted transaction, the data has only **Event** and **ID**. If Wallet does not give a value for a field, the field has no value in Zapier. An example is **Foreign Amount** for a purchase in dollars. In Zapier, an amount has no zeros at the end, for example 49 for $49.00.

## New and changed transactions

While WalletFeed is open, Zapier receives changes in seconds. When WalletFeed is not open, iOS starts WalletFeed approximately 1 hour or less after a change in Wallet. If [Background Sync](/docs/background-sync/) is on in **Settings** › **Sync**, WalletFeed then sends the change.

**Background Sync** is on until you set it to off.

One transaction can start the Zap more than one time:

- Zapier receives a new purchase with **Event** `created` and **Status** `pending`.
- When the **Status** changes to `booked`, Zapier receives the same **ID** again with **Event** `updated`.
- If the bank does not accept a pending charge, or Wallet removes a transaction, Zapier receives **Event** `deleted` and the **ID**.

A refund is a different transaction. It has a positive **Amount** and the **Type** `refund`.

If WalletFeed stops while it sends changes, it sends the same changes again at a subsequent time. Zapier starts the Zap again for each change that it received before. Thus, a Zap that adds a row for each change can add a transaction two times. A Zap that first finds the row by **ID**, and then updates it, keeps one row for each transaction. This Zap uses two tasks for each change.

Zapier can start the Zap for some changes at the same time. Thus, the Zap does not always get the changes in the sequence that WalletFeed sends them.

## Send previous transactions

A new Zapier destination also receives previous transactions from the start date in **Settings** › **Sync** › **Initial History**. **Initial History** is **All** until you change it. But Zapier receives a maximum of 30 days of previous transactions.

To send more transactions, use [Send History](/docs/send-history/):

1. In **Destinations**, tap the Zapier destination.
2. Tap **Send History**.
3. Select a period (**30 Days**, **90 Days**, **1 Year** or **All**).
4. In the message **Send History to Zapier?**, tap **Send**.

   The message shows "Each transaction runs your Zap."

WalletFeed sends the newest transactions first. Each transaction starts the Zap one time. Each action step uses one task in Zapier.

**Send History** sends each transaction with **Event** `created`. Thus, Zapier can receive the same transaction two times as `created`.

To stop **Send History**, do these steps:

1. Tap **Send History**.
2. Tap **Stop Sending**.

## Change or remove the destination

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

The text in **Catch Hook URL** is not a Zapier webhook URL. The URL must start with `https://hooks.zapier.com/hooks/`.

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

Zapier loads a maximum of 3 records at a time, and it does not always load the newest records. This limit is only for the test. When the Zap is on, it starts for each change.

### If the Zap does not do its action

The Zap is a draft, or it is off. Zapier accepts the requests for the Zap, but the Zap does not do its action. WalletFeed shows no error.

1. In Zapier, open the Zap.
2. Click **Publish**.
3. In **Automations** › **Zaps**, set the **Status** of the Zap to on.

   ![The list of Zaps in Zapier, with the WalletFeed Zap and its Status switch in the off position.](web:zapier/16-zap-list-off)

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
