+++
title = "Background Sync"
nav_title = "Background Sync"
seo_title = "Background Sync: send Apple Card transactions automatically"
description = "Send your Apple Card transactions to your destinations while WalletFeed is closed, with Background Sync and automations in Shortcuts on your iPhone."
order = 140
related = ["docs/send-history", "docs/troubleshooting"]
updated = 2026-10-30
+++

**Background Sync** sends your new and changed Apple Card, Apple Cash and Savings transactions to your destinations while WalletFeed is closed. To send transactions to [destinations](/docs/destinations/), you must have [WalletFeed Pro](/docs/walletfeed-pro/). WalletFeed Pro is a subscription with a 1-week free trial, or a one-time Lifetime purchase.

## Times that destinations receive changes

A destination receives a new or changed transaction at these times:

| Condition | A destination receives the change |
| --- | --- |
| WalletFeed is open. | In seconds. |
| WalletFeed is closed, and **Background Sync** is on. | In approximately 1 hour or less after the change in Wallet. |
| You tap your iPhone to make a purchase, and you have an **After Each Card Tap** automation. | Seconds after you tap your iPhone. |
| Your **Every Day** automation starts. | At the time that you set in Shortcuts. |
| You tap **Sync Now** in **Settings** › **Sync**. | In seconds. |
| Your iPhone charges. | At a time that iOS selects. |

While WalletFeed is closed, iOS also starts WalletFeed after a change in Wallet to update the Spending widget and Recurring Charge Alerts. WalletFeed does this without WalletFeed Pro, and also while **Background Sync** is off.

After your iPhone starts again, WalletFeed does not send changes to your destinations until you type your passcode one time.

If **Background Sync** cannot open the folder of a CSV, OFX or QIF file, it does not update the file. WalletFeed updates the file when you open WalletFeed, when an automation starts, or while your iPhone charges.

A new destination also receives previous transactions, from the start date in **Settings** › **Sync** › **Initial History**. **Initial History** is **All** until you change it. If **Send** is **Each Transaction** for Zapier, Make or Linear, the destination receives a maximum of 30 days of previous transactions. Refer to [Send History](/docs/send-history/).

## Make sure that Background Sync is on

**Background Sync** is on until you set it to off. **Settings** shows the **Sync** section only with WalletFeed Pro.

1. In WalletFeed, tap **Settings** (the gear button) at the top of the screen.
2. In the **Sync** section, make sure that **Background Sync** is on.

   ![The Sync section of WalletFeed Settings, with the Background Sync switch on.](app:docs-settings)

3. If **Background Sync** is off, set it to on.
4. Tap **Done**.

## Add an After Each Card Tap automation

An **After Each Card Tap** automation sends each purchase seconds after you tap your iPhone to make the purchase. While **Background Sync** is on, this automation is not necessary. Without the automation, a destination receives the purchase in approximately 1 hour or less while WalletFeed is closed.

iOS does not let apps make automations. Thus, you add the automation in the Shortcuts app, and WalletFeed gives you the steps.

1. In WalletFeed, tap **Settings** (the gear button) at the top of the screen.
2. In the **Sync** section, tap **Automations**.

   ![The Automations screen, with the steps for After Each Card Tap and Every Day.](app:docs-automations)

3. In the **After Each Card Tap** section, do the steps for your iPhone.

   The sections that follow give these steps. The steps are different on iOS 26 and on iOS 27. On iOS 27, they are also different with Apple Intelligence.

### Paste the text in Shortcuts

If step 1 in the **After Each Card Tap** section is **Copy Description**, do these steps. WalletFeed shows them on iOS 27 with Apple Intelligence, and after you tap **Describe It Instead**.

1. Tap **Copy Description**.

   **Copy Description** changes to **Copied**. WalletFeed copies the text `When I tap my Apple Card or Apple Cash card, run Sync New Purchase from WalletFeed without asking.`

2. Tap **Open Shortcuts**.
3. In Shortcuts, tap **+**.
4. Paste the text.
5. Make sure that the automation uses your cards.
6. Make sure that the automation does not wait for your approval.
7. Tap **Done**.

> **Note:** If Shortcuts does not make the automation from the text, **Set It Up Yourself** in WalletFeed gives a different procedure. This procedure is also in [Make the automation on iOS 27](#make-the-automation-on-ios-27).

### Make the automation on iOS 26

If step 2 in the **After Each Card Tap** section tells you to tap **Automation**, do these steps. WalletFeed shows them on iOS 26.

1. Tap **Open Shortcuts**.
2. In Shortcuts, tap **Automation**.
3. Tap **+** or **New Automation**.
4. Tap **Transaction**.
5. Select your cards.
6. Select **Run Immediately**.
7. Tap **Next**.
8. Tap **New Blank Automation** › **Add Action**.
9. Type WalletFeed in the search field.
10. Tap **Sync New Purchase**.
11. Tap **Done**.

### Make the automation on iOS 27

If step 2 in the **After Each Card Tap** section tells you to tap **Add Action**, do these steps. WalletFeed shows them on iOS 27 when Apple Intelligence is not available, and after you tap **Set It Up Yourself**.

1. Tap **Open Shortcuts**.
2. In Shortcuts, tap **Add Action**.
3. Type WalletFeed in the search field.
4. Tap **Sync New Purchase**.
5. In the action list, tap **Automation** › **Transaction**.
6. Select your cards.
7. Tap the arrow adjacent to the trigger.
8. Set **Confirm Before Run** to off.
9. Tap the information button **ⓘ** › **Privacy**.
10. Set **Allow Running When Locked** to on.
11. Tap **Done**.

### Automations and Last Run

iOS does not tell apps about the automations that you have. Thus, WalletFeed records the last time that **Sync New Purchase** and **Sync Transactions** started. **Last Run** shows this time. If Siri or a shortcut starts **Sync Transactions**, the **Last Run** of **Every Day** also changes. Until an action starts for the first time, its **Last Run** shows **Never**.

In **Settings** › **Sync**, **Automations** shows one of these values:

| Value | Condition |
| --- | --- |
| **On** | Each automation on the **Automations** screen started in its time limit. |
| **1 of 2** | One of the two automations started in its time limit. |
| **Off** | **Background Sync** is on, **Sample Data** is off, and **After Each Card Tap** did not start in its time limit. |
| **Set Up** | **Background Sync** is off or **Sample Data** is on, and no automation started in its time limit. |

The time limit is 14 days for **After Each Card Tap**, and 3 days for **Every Day**.

For the messages that the automations show, refer to [Siri and Shortcuts](/docs/siri-and-shortcuts/).

## Add an Every Day automation

An **Every Day** automation sends changes one time each day, at a time that you select. It sends the changes that an **After Each Card Tap** automation does not send, for example purchases on the internet and changes to pending transactions.

**Automations** shows **Every Day** only when **Background Sync** is off or **Sample Data** is on. While **Background Sync** is on, an **Every Day** automation is not necessary. If you have an **Every Day** automation, it stays in Shortcuts and continues to send changes.

1. In WalletFeed, tap **Settings** (the gear button) at the top of the screen.
2. In the **Sync** section, tap **Automations**.
3. In the **Every Day** section, do the steps for your iPhone.

   These steps are the same as the steps in [Add an After Each Card Tap automation](#add-an-after-each-card-tap-automation), but the parts in the table that follows are different.

| Part | **After Each Card Tap** | **Every Day** |
| --- | --- | --- |
| The text that you copy | `When I tap my Apple Card or Apple Cash card, run Sync New Purchase from WalletFeed without asking.` | `Every day at 9 PM, run Sync Transactions from WalletFeed without asking.` |
| The trigger in Shortcuts | **Transaction**, then your cards | **Time of Day**, then a time |
| The WalletFeed action | **Sync New Purchase** | **Sync Transactions** |
| The last check before you tap **Done** | Your cards | The time |

## Get the Sync Stopped notification

If **Remind If Sync Stops** is on and WalletFeed does not send to all your destinations correctly for 3 days, you get the **Sync Stopped** notification. The notification does not show information about your transactions.

1. In WalletFeed, tap **Settings** (the gear button) at the top of the screen.
2. In the **Sync** section, set **Remind If Sync Stops** to on.
3. If iOS shows a message about notifications, let WalletFeed send notifications.

   If you do not let WalletFeed send notifications, **Remind If Sync Stops** stays off.

4. Tap **Done**.

Each time that WalletFeed sends to all your destinations correctly, the 3-day period starts again. The text of the notification is "WalletFeed hasn't synced in 3 days. Open it to catch up."

## Send changes with Sync Now

**Sync Now** sends the changes to your destinations when you tap it.

1. In WalletFeed, tap **Settings** (the gear button) at the top of the screen.
2. In the **Sync** section, tap **Sync Now**.

   ![WalletFeed Settings, with Initial History set to All and Sync Now with the time 1 minute ago.](app:docs-settings-2)

   While WalletFeed sends the changes, **Sync Now** shows a progress indicator. Then it shows a time, for example "1 minute ago".

3. Tap **Done**.

## Stop Background Sync

If you set **Background Sync** to off, iOS continues to start WalletFeed after a change in Wallet. But WalletFeed then updates only the Spending widget and Recurring Charge Alerts.

1. In WalletFeed, tap **Settings** (the gear button) at the top of the screen.
2. In the **Sync** section, set **Background Sync** to off.
3. Tap **Done**.

While **Background Sync** is off, your destinations receive changes at these times:

- When you open WalletFeed
- When you tap **Sync Now**
- When an automation from **Automations** starts
- While your iPhone charges
- At other times that iOS selects

**Automations** then also shows **Every Day**. Refer to [Add an Every Day automation](#add-an-every-day-automation).

## If something goes wrong

### If a destination does not receive a change after 1 hour

**Background Sync** is off, your iPhone started again, or the destination has a problem.

1. On your iPhone, open WalletFeed.

   While WalletFeed is open, it sends changes in seconds.

2. Tap **Settings** (the gear button) at the top of the screen.
3. In the **Sync** section, if **Background Sync** is off, set it to on.
4. Tap **Sync Now**.
5. Tap **Done**.
6. Tap **Destinations** at the bottom of the screen.

   ![The Destinations screen, where the n8n destination shows Authentication failed.](app:docs-destinations-failure)

7. If a destination shows a problem, for example "Authentication failed", refer to [Troubleshooting](/docs/troubleshooting/).

### If Settings does not show the Sync section

**Settings** shows the **Sync** section only with WalletFeed Pro.

1. In WalletFeed, tap **Settings** (the gear button) at the top of the screen.
2. In the **Subscription** section, tap **WalletFeed Pro**.
3. Select a plan.
4. Tap **Start Free Trial**, **Subscribe** or **Buy Lifetime**.

For the plans, refer to [WalletFeed Pro](/docs/walletfeed-pro/).

### If you get the Sync Stopped notification

In the last 3 days, WalletFeed did not send to all your destinations correctly.

1. On your iPhone, open WalletFeed.
2. Tap **Destinations** at the bottom of the screen.
3. If a destination shows a problem, refer to [Troubleshooting](/docs/troubleshooting/).
4. If no destination shows a problem, tap **Settings** (the gear button) at the top of the screen.
5. In the **Sync** section, tap **Sync Now**.

### If Last Run shows Never

**Last Run** changes only after **Sync New Purchase** starts. An **After Each Card Tap** automation starts it only when you tap your iPhone to make a purchase.

1. After you make a purchase with your iPhone, open WalletFeed.
2. Tap **Settings** (the gear button) at the top of the screen.
3. In the **Sync** section, tap **Automations**.
4. In the **After Each Card Tap** section, if **Last Run** shows **Never**, do the steps in [Add an After Each Card Tap automation](#add-an-after-each-card-tap-automation) again.

> **Note:** On iOS 27, **Set It Up Yourself** and **Describe It Instead** give a different procedure to make the same automation.

### If Remind If Sync Stops does not stay on

iOS does not let WalletFeed send notifications.

1. On your iPhone, open the Settings app.
2. Tap **Notifications** › **WalletFeed**.
3. Set **Allow Notifications** to on.
4. Open WalletFeed.
5. Tap **Settings** (the gear button) at the top of the screen.
6. In the **Sync** section, set **Remind If Sync Stops** to on.
