+++
title = "Send previous transactions"
nav_title = "Send History"
description = "Send your previous Apple Card transactions to a WalletFeed destination with Send History, and set the start date of new destinations with Initial History."
order = 150
related = ["docs/destinations", "docs/background-sync"]
updated = 2026-10-30
+++

A WalletFeed [destination](/docs/destinations/) can also receive your previous Apple Card, Apple Cash and Savings transactions. In WalletFeed, **Initial History** sets the start date of each new destination, and **Send History** sends previous transactions to one of your destinations.

Destinations and **Send History** are part of [WalletFeed Pro](/docs/walletfeed-pro/). WalletFeed Pro is a subscription with a 1-week free trial, or a one-time Lifetime purchase. If you do not have WalletFeed Pro, **Send History** opens the **WalletFeed Pro** screen.

## Set the start date for new destinations

When you add a destination, it receives your transactions from the date that **Initial History** sets. **Initial History** is **All** until you change it. If you change **Initial History**, only the destinations that you add after the change use the new period. WalletFeed shows the **Sync** section only if you have WalletFeed Pro.

1. In WalletFeed, tap **Settings** (the gear button) at the top of the screen.
2. In the **Sync** section, tap **Initial History**.

   ![The WalletFeed Settings screen, where Initial History shows All in the Sync section.](app:docs-settings)

3. Select a period.
4. Tap **Done**.

These are the periods of **Initial History**:

| Period | A new destination receives |
| --- | --- |
| **Today** | The transactions from the day that you add the destination. |
| **30 Days** | The transactions from the last 30 days. |
| **90 Days** | The transactions from the last 90 days. |
| **1 Year** | The transactions from the last 12 months. |
| **All** | All the transactions that WalletFeed can read. |

If **Send** is **Each Transaction** for Zapier, Make or Linear, each transaction starts a Zap, uses a Make credit or becomes an issue. Thus, the start date is a maximum of 30 days before you add the destination. To send previous transactions to it, use **Send History**. If **Send** is **Monthly**, there is no 30-day limit, and the start date is the first day of a month.

WalletFeed can read only the Wallet accounts and the period that you select in iOS. You can change them in the Settings app, in **Privacy & Security** › **Wallet** › **WalletFeed**.

## Send to a new destination

Before a new destination receives transactions, WalletFeed shows a message. The message tells you the data that the destination receives, the accounts and the start date.

1. To add the destination, do the steps in [Add a destination](/docs/destinations/#add-a-destination).
2. Read the message, for example **Send Transactions to Lunch Money?**

   If **Initial History** is **All**, the message shows "including earlier ones" and no date. If **Send** is **Each Transaction** for Zapier, Make or Linear, the message shows the start date.

   For a CSV, OFX or QIF file, the title of the message is **Save Transactions to Files?**, and the button is **Save**.

3. Tap **Send** or **Save**.

WalletFeed then sends your transactions to the destination. It sends the newest transactions first.

If you tap **Cancel**, WalletFeed removes the new destination and does not send transactions to it.

## Send previous transactions to a destination

You can send the transactions of a period to a destination at any time, for example after you change its [filter](/docs/choose-what-to-send/).

1. In WalletFeed, tap **Destinations** at the bottom of the screen.
2. Tap the destination.

   ![The Destinations tab with Lunch Money, Budget 2026, Monthly CSV and n8n.](app:07-destinations)

3. Tap **Send History**.

   ![The Lunch Money destination screen, with Send History below Filter.](app:docs-destination-detail)

4. Select **30 Days**, **90 Days**, **1 Year** or **All**.
5. If WalletFeed shows a message, for example **Send History to Zapier?**, tap **Send**.

   This message shows only for Zapier, Make and Linear. It tells you the result in the service, for example:

   - "Each month runs your Zap once."
   - "Each transaction runs your scenario."
   - "Each month becomes one issue."

WalletFeed then starts to send the history. Above **Send History**, the destination screen shows **Sending History** and a progress bar.

WalletFeed sends all the transactions of the period, and it starts with the newest transactions. It uses the filter of the destination and does not send declined transactions.

The first day of the period also becomes the start date of the destination. After that, WalletFeed sends changes only for transactions from that date. If **Send** is **Monthly** for Zapier, Make or Linear, the period starts on the first day of a month.

If a new transaction occurs while WalletFeed sends the history, WalletFeed sends the new transaction first.

Webhook, Zapier, Make, Amazon SQS, Kinesis Data Streams and EventBridge destinations receive each transaction again. If **Send** is **Monthly**, Zapier and Make receive each month again. Other destinations keep one copy of each transaction.

> **Note:** On the Linear Free plan, a workspace can have a maximum of 250 issues.

## Monitor the history

While WalletFeed sends the history, the destination screen shows **Sending History** above **Send History**. It also shows numbers and a month, for example "2,340 of 5,120 · back to March 2023":

- The first number is the number of transactions that WalletFeed sent. This number also includes the transactions that the destination had and the transactions that the filter does not include.
- The second number is the number of transactions in the period.
- The month tells you that WalletFeed sent all the transactions after a date in that month.

The progress bar shows less than 100% until WalletFeed completes the history. In **Destinations**, the row of the destination shows "Sending history · 46%". When WalletFeed waits or cannot continue the history, the row shows "History paused · 46%".

The destination screen shows one of these items above **Send History**:

| Item | Information |
| --- | --- |
| **Sending History** and numbers | WalletFeed sends the history. |
| "Paused" | WalletFeed does not send the history at this time. For example, **Enabled** is off, or you do not have WalletFeed Pro. |
| "Too many requests.", "Can't connect." or "Server error (502).", then "Trying again in 10 min." | The service has a problem or a limit, or WalletFeed cannot connect to it. WalletFeed tries again at the time that the message shows. |
| An orange symbol, a message and **Try Again** | WalletFeed cannot continue until you correct a problem. For the steps, refer to [Correct a problem with the history](#correct-a-problem-with-the-history). |
| **History** with "All sent" | WalletFeed sent all the transactions. |
| **History** with "Sent from March 3, 2023" | WalletFeed sent all the transactions from that date. |
| **History** with "Stopped" | You tapped **Stop Sending**. |

## History while WalletFeed is closed

While WalletFeed is open, it sends the history. When you go to a different app, iOS can let WalletFeed continue. This can occur after you select a period in **Send History**, or after you tap **Send** for a new destination.

iOS then shows a Live Activity, for example "Sending history to Lunch Money" with "2,340 of 5,120". In the Live Activity, **Cancel** does not stop the history. **Cancel** stops WalletFeed only until the next time that WalletFeed can send. If you close WalletFeed in the app switcher, the result is the same. To stop the history, do the steps in [Stop the history](#stop-the-history).

iOS can also let WalletFeed send the history while your iPhone charges and you do not use it. For short periods, iOS can start WalletFeed to send the history.

WalletFeed sends the history to each service at a speed that the service accepts. Thus, if a slow service receives a large history, the history can continue for some days.

## Stop the history

1. In **Destinations**, tap the destination.
2. Tap **Send History**.
3. Tap **Stop Sending**.

   **History** shows "Stopped".

WalletFeed shows **Stop Sending** only until it completes the history. The destination keeps the transactions that it received. WalletFeed continues to send new transactions to the destination.

To send the history again, select a period in **Send History**.

## Send previous transactions after a filter change

A change to the filter of a destination changes only the transactions that WalletFeed sends after the change.

If the new filter includes more transactions, WalletFeed does not send the previous transactions that the new filter adds. If the new filter does not include some transactions, the destination keeps the transactions that it received before the change.

To send the previous transactions with the new filter, do the steps in [Send previous transactions to a destination](#send-previous-transactions-to-a-destination).

## Correct a problem with the history

### If the history shows "Authentication failed"

The service did not accept the key, token or sign-in of the destination, or the permissions of the key changed.

1. If the message includes "Replace the key.", make a new key in the service. For the steps, refer to the [guide for the destination type](/guides/).
2. In WalletFeed, replace the key, sign in again or correct the connection. For the steps, refer to [Replace a key or sign in again](/docs/destinations/#replace-a-key-or-sign-in-again).
3. On the destination screen, tap **Try Again**.

WalletFeed also tries again after approximately 1 hour, and then after longer periods, to a maximum of 24 hours. When a new transaction goes to the destination correctly, the history also continues.

### If the history shows "Can't open the folder. Choose it again."

WalletFeed cannot open the folder of the CSV, OFX or QIF file.

1. In **Destinations**, tap the destination.
2. Tap **Change Folder**.
3. Select the folder.

   The history starts again, and WalletFeed writes the transactions to that folder.

### If the history shows "Check the destination, then try again."

The service rejected the transactions. The message starts with the cause, for example "Rejected (HTTP 404)".

These are some problems that can stop the history:

- On the Airtable Free plan, a base can have a maximum of 1,000 records.
- If a Make scenario is not active, Make keeps the transactions in a queue. On the Make Free plan, the queue can have a maximum of 50 items.
- If a Zap is off, Zapier rejects the transactions. Zapier can start to reject them some hours after you set the Zap to off.

1. Correct the problem in the service.
2. In WalletFeed, tap the destination in **Destinations**.
3. Tap **Try Again**.

WalletFeed also tries again after approximately 1 hour, and then after longer periods, to a maximum of 24 hours.

### If the history shows "Paused"

WalletFeed does not send the history at this time.

1. In **Destinations**, tap the destination.
2. Make sure that **Enabled** is on.
3. Make sure that you have WalletFeed Pro. In **Settings**, the **Subscription** section shows your plan.
4. Keep WalletFeed open.

   When WalletFeed continues the history, numbers replace "Paused".
