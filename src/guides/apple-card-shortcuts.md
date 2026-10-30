+++
title = "Run a shortcut after each Apple Card purchase"
nav_title = "Shortcuts"
seo_title = "Apple Card Shortcuts automation for each purchase"
description = "Make a Shortcuts automation that sends each Apple Card purchase from your iPhone to your WalletFeed destinations in seconds."
group = "Automations"
order = 40
related = ["docs/siri-and-shortcuts", "docs/background-sync"]
updated = 2026-10-30
+++

A Shortcuts automation on your iPhone can send each of your Apple Card purchases to your WalletFeed destinations in seconds. In Shortcuts, it is a **Transaction** automation. It starts when you tap your iPhone to pay with your Apple Card or Apple Cash card.

iOS does not let apps make automations. You make the automation one time in the Shortcuts app. WalletFeed shows the steps.

## Before you start

You must have these items:

- An iPhone with iOS 26 or a newer version
- WalletFeed, with access to your Wallet accounts
- [WalletFeed Pro](/docs/walletfeed-pro/), a subscription with a 1-week free trial, or a one-time Lifetime purchase
- One or more [destinations](/docs/destinations/) in WalletFeed, for example Google Sheets or Lunch Money
- Your Apple Card or Apple Cash card in Wallet on your iPhone
- The Shortcuts app on your iPhone.

WalletFeed is available only in the US. You must have WalletFeed Pro to send transactions to destinations.

## Step 1: Open Automations in WalletFeed

1. On your iPhone, open WalletFeed.
2. Tap **Settings** (the gear button) at the top of the screen.

   Result: WalletFeed shows **Settings**.
3. If **Settings** does not show **Sync**, get WalletFeed Pro. Refer to [WalletFeed Pro](/docs/walletfeed-pro/).
4. Below **Sync**, tap **Automations**.

   ![WalletFeed Settings with Background Sync and Automations below Sync.](app:docs-settings)

   Result: WalletFeed shows **Automations**. **After Each Card Tap** is at the top of the screen.

## Step 2: Make the automation in Shortcuts

In **After Each Card Tap**, WalletFeed shows the steps for your iPhone. The steps for iOS 26, iOS 27 and iOS 27 with Apple Intelligence are different. Do only the procedure that is applicable to your iPhone.

### iOS 27 with Apple Intelligence

On iOS 27 with Apple Intelligence, Shortcuts can make a shortcut from text that you give it. WalletFeed gives you the text. In WalletFeed, step 1 is **Copy Description**.

1. In **After Each Card Tap**, tap **Copy Description**.

   ![The Automations screen with Copy Description and its text below After Each Card Tap.](app:docs-automations)

   Result: WalletFeed copies the text below **Copy Description** and shows **Copied**. The text is "When I tap my Apple Card or Apple Cash card, run Sync New Purchase from WalletFeed without asking."
2. Tap **Open Shortcuts**.

   Result: The Shortcuts app opens.
3. Tap **+**.

   Result: Shortcuts shows a new shortcut. You can type the task that the shortcut must do.
4. Paste the text.
5. Make sure that the shortcut uses your Apple Card or Apple Cash card.
6. Tap the arrow adjacent to the trigger at the top of the shortcut.
7. Make sure that **Confirm Before Run** is off.
8. Tap **Done**.

If Shortcuts does not let you type the task that the shortcut must do, do these steps:

1. In WalletFeed, tap **Set It Up Yourself**.
2. Below **Set It Up Yourself**, tap **Open Shortcuts**.
3. Do steps 2 to 11 in [iOS 27 without Apple Intelligence](#ios-27-without-apple-intelligence).

### iOS 27 without Apple Intelligence

On iOS 27, an automation is a trigger at the top of a shortcut. In WalletFeed, step 1 is **Open Shortcuts**, and **Describe It Instead** is below the steps.

1. In **After Each Card Tap**, tap **Open Shortcuts**.

   Result: Shortcuts opens a new shortcut.
2. Tap **Add Action**.
3. Type WalletFeed in the search field.
4. Tap **Sync New Purchase**.
5. In the action list, tap **Automation** › **Transaction**.
6. Select your cards.
7. Tap the arrow adjacent to the trigger.
8. Set **Confirm Before Run** to off.
9. Tap the information button **ⓘ** › **Privacy**.
10. Set **Allow Running When Locked** to on.
11. Tap **Done**.

### iOS 26

On iOS 26, automations have a tab in Shortcuts. Your other devices do not get these automations. In WalletFeed, step 1 is **Open Shortcuts**.

1. In **After Each Card Tap**, tap **Open Shortcuts**.

   Result: The Shortcuts app opens.
2. Tap **Automation**.
3. If you have no automations, tap **New Automation**.
4. If you have one or more automations, tap **+**.
5. Tap **Transaction**.
6. Select your cards.
7. Select **Run Immediately**.
8. Tap **Next**.
9. Tap **New Blank Automation** › **Add Action**.
10. Type WalletFeed in the search field.
11. Tap **Sync New Purchase**.
12. Tap **Done**.
13. If you use WalletFeed on a different iPhone, do this procedure on that iPhone also.

## Step 3: Make sure that the automation operates

After you tap your iPhone to pay with your Apple Card or Apple Cash card, do these steps:

1. Open WalletFeed.
2. Tap **Settings** (the gear button) at the top of the screen.
3. Below **Sync**, look at the value adjacent to **Automations**.

   Result: **Automations** shows **On** or **1 of 2**. The table that follows gives each value.
4. Tap **Automations**.
5. In **After Each Card Tap**, look at **Last Run**.

   Result: **Last Run** shows the time of the last operation of **Sync New Purchase**, for example "2 hr. ago".
6. If **Last Run** shows **Never**, refer to [If Last Run shows Never after a purchase](#if-last-run-shows-never-after-a-purchase).

**Automations** in **Settings** shows if each automation operated in its period. The period of **After Each Card Tap** is the last 14 days. The period of **Every Day** is the last 3 days. This table gives the values of **Automations**.

| **Automations** shows | Condition |
| --- | --- |
| **On** | Each automation on the **Automations** screen operated in its period. |
| **1 of 2** | Only one of the two automations operated in its period. |
| **Set Up** | No automation operated in its period, and **Background Sync** is off or **Sample Data** is on. |
| **Off** | **After Each Card Tap** did not operate in the last 14 days, **Background Sync** is on, and **Sample Data** is off. |

When **Background Sync** is on, the automation is optional. Without the automation, iOS starts WalletFeed in approximately 1 hour or less after a change in Wallet.

## Time to send each purchase

When you tap your iPhone to pay with your Apple Card or Apple Cash card, the automation starts **Sync New Purchase**. This WalletFeed action operates in the background. It does not open WalletFeed.

At that time, Wallet does not have the purchase. First, WalletFeed sends the changes that it did not send previously. Then it waits for Wallet to record the purchase. When Wallet records the purchase, WalletFeed sends the purchase to your destinations.

WalletFeed waits for the purchase until 18 seconds after the action starts. If Wallet records the purchase after that time, WalletFeed sends it at the next sync. While WalletFeed is open, it sends each change in seconds. When WalletFeed is closed and **Background Sync** is on, iOS starts WalletFeed in approximately 1 hour or less after a change in Wallet. Refer to [Background Sync](/docs/background-sync/).

The automation starts only when you tap your iPhone to pay. WalletFeed sends other changes at the next sync, for example online purchases and posted charges. Your Savings account has no card. Thus, the automation does not start for Savings transactions.

The automation does not change the data that WalletFeed sends to your destinations. WalletFeed also uses the filter of each destination. Refer to [filters for destinations](/docs/choose-what-to-send/).

After your iPhone starts again, WalletFeed cannot send to destinations until you type your passcode one time.

When the action stops, it gives a short message. Shortcuts can show the message as a notification. This table gives the messages.

| Message | Condition |
| --- | --- |
| "Changes sent: 2." | WalletFeed sent 2 changes. The number is the total for all your destinations. |
| "Nothing new yet." | WalletFeed did not find a new change to send. |
| "Changes sent: 1. One destination needs attention." | WalletFeed cannot send to one destination. If two or more destinations have a problem, the message gives the number of these destinations. |
| "Sync requires WalletFeed Pro." | WalletFeed Pro is not active on this iPhone. |
| "Open WalletFeed and allow Wallet access." | WalletFeed does not have access to your Wallet accounts. |
| "Add a destination in WalletFeed first." | WalletFeed has no destination that is on. |

To correct a problem, refer to [If there is a problem](#if-there-is-a-problem).

## Send other changes each day

If **Background Sync** is off, **Automations** also shows **Every Day**. An **Every Day** automation starts **Sync Transactions** at a time that you select. This action sends new and changed transactions to your destinations, for example online purchases and posted charges.

For **Every Day**, the text to paste is "Every day at 9 PM, run Sync Transactions from WalletFeed without asking."

To make the automation, do [Step 2](#step-2-make-the-automation-in-shortcuts) with these changes:

- Use the steps below **Every Day** in WalletFeed.
- If you paste the text, make sure that the time in Shortcuts is correct.
- Tap **Sync Transactions**, not **Sync New Purchase**.
- Tap **Time of Day**, not **Transaction**.
- Select a time, not your cards.

If **Background Sync** is on, iOS starts WalletFeed in approximately 1 hour or less after a change in Wallet. Thus, WalletFeed does not show **Every Day**. An **Every Day** automation that you made previously continues to operate.

## Stop or change the automation

iOS does not tell WalletFeed about your automations. To change the cards or the time, open the automation in the Shortcuts app.

To stop the automation, delete it in the Shortcuts app. After you delete it, WalletFeed sends new purchases at the next sync. The transactions that WalletFeed sent stay at each destination.

## Other WalletFeed actions in Shortcuts

WalletFeed has more actions for the Shortcuts app. For example, **Get Recent Card Transactions** gives your transactions from the last 7 days to the next action in a shortcut. You can change the number of days. Refer to [Siri and Shortcuts](/docs/siri-and-shortcuts/).

## If there is a problem

### If Last Run shows Never after a purchase

The automation did not start, or it did not start the WalletFeed action.

1. Open the Shortcuts app.
2. If you cannot find the automation, do [Step 2](#step-2-make-the-automation-in-shortcuts) again.
3. Make sure that the automation uses your Apple Card or Apple Cash card.
4. Make sure that the automation starts **Sync New Purchase**.
5. On iOS 26, make sure that the automation uses **Run Immediately**.
6. On iOS 27, make sure that **Confirm Before Run** is off.
7. On iOS 27, make sure that **Allow Running When Locked** is on.

### If the message is "Nothing new yet."

WalletFeed did not send the purchase before the action stopped. For example, Wallet recorded the purchase more than 18 seconds after the action started.

1. If the destination has a filter, make sure that the filter includes the purchase.
2. To send the purchase at this time, open WalletFeed.
3. If you do not open WalletFeed, wait for the next sync.

> **Note:** When WalletFeed is closed and **Background Sync** is on, the next sync occurs in approximately 1 hour or less after a change in Wallet.

### If the message is "Sync requires WalletFeed Pro."

WalletFeed Pro is not active on this iPhone.

1. Open WalletFeed.
2. Tap **Settings** (the gear button) at the top of the screen.
3. Tap **WalletFeed Pro**.
4. If you got WalletFeed Pro previously, tap **Restore Purchases**.
5. If you do not have WalletFeed Pro, get it. Refer to [WalletFeed Pro](/docs/walletfeed-pro/).

### If the message is "Open WalletFeed and allow Wallet access."

WalletFeed does not have access to your Wallet accounts.

1. On your iPhone, open the Settings app.
2. Tap **Privacy & Security** › **Wallet** › **WalletFeed**.
3. Select the accounts that WalletFeed can read. Refer to [Wallet accounts](/docs/wallet-accounts/).
4. Open WalletFeed.

### If the message is "Add a destination in WalletFeed first."

WalletFeed has no destination that is on.

1. Open WalletFeed.
2. Tap **Destinations**.
3. If a destination shows **Off**, do these steps:

   1. Tap the destination.
   2. Set **Enabled** to on.

4. If there is no destination, tap **+** to add a destination. Refer to [Destinations](/docs/destinations/).

### If the message includes "One destination needs attention."

WalletFeed cannot send to one or more destinations.

1. Open WalletFeed.
2. Tap **Destinations**.
3. Find the destination with the problem. Below its name, WalletFeed shows the cause, for example "Authentication failed".

   ![The Destinations screen with Authentication failed and a warning symbol for the n8n destination.](app:docs-destinations-failure)
4. Tap the destination.
5. In the guide for that destination, do the steps for this cause. Refer to [Guides](/guides/).
