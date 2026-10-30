+++
title = "Siri and Shortcuts"
nav_title = "Siri and Shortcuts"
description = "Use Siri and the Shortcuts app with WalletFeed on your iPhone to open Spending, find transactions and send Apple Card transactions to destinations."
order = 100
related = ["guides/apple-card-shortcuts", "docs/background-sync"]
updated = 2026-10-30
+++

You can use Siri and the Shortcuts app with WalletFeed on your iPhone. Siri can open **Spending** or **Search** in WalletFeed. The WalletFeed actions in Shortcuts can send your Apple Card transactions to your [destinations](/docs/destinations/) or give them to a shortcut.

**Show Spending** and **Search Transactions** operate without WalletFeed Pro. For the actions that send or give your transactions, and for the **Sync Transactions** control, you must have [WalletFeed Pro](/docs/walletfeed-pro/). WalletFeed Pro is a subscription with a 1-week free trial, or a one-time Lifetime purchase.

## WalletFeed actions

WalletFeed gives these actions to Siri and the Shortcuts app:

| Action | Result | WalletFeed Pro |
| --- | --- | --- |
| **Show Spending** | WalletFeed opens **Spending**. | Not necessary |
| **Search Transactions** | WalletFeed opens **Search** with the transactions that you tell Siri to find. | Not necessary |
| **Sync Transactions** | WalletFeed sends new and changed transactions to your destinations. WalletFeed does not open. | Necessary |
| **Sync New Purchase** | WalletFeed sends your last purchase after Wallet records it. WalletFeed does not open. This action is for a **Transaction** automation. | Necessary |
| **Get Recent Card Transactions** | WalletFeed gives your transactions from the last 7 days to the shortcut. You can change the number of days. | Necessary |

## Use Siri with WalletFeed

1. On your iPhone, start Siri.
2. Tell Siri one of these instructions:

| Tell Siri | Result |
| --- | --- |
| "Show my spending in WalletFeed" or "Open my spending in WalletFeed" | WalletFeed opens **Spending**. |
| "Search WalletFeed" or "Find a transaction in WalletFeed" | You hear "What are you looking for?" You tell Siri the transactions to find. Then WalletFeed opens **Search**. |
| "Sync WalletFeed" or "Send my card transactions with WalletFeed" | WalletFeed sends new and changed transactions to your destinations. |
| "Get card transactions from WalletFeed" | Siri receives your transactions from the last 7 days. |

When you tell Siri "Sync WalletFeed", WalletFeed does not open. After WalletFeed sends the transactions, Siri gives a message, for example "Changes sent: 3." Refer to [Messages from WalletFeed actions](#messages-from-walletfeed-actions).

## Find transactions with Siri

1. On your iPhone, start Siri.
2. Tell Siri "Search WalletFeed".

   You hear "What are you looking for?"

3. Tell Siri the transactions to find, for example "dining over $50 last month".

   **Search** opens in WalletFeed and shows your instruction in the search field.

   ![The Search screen with the filters Groceries, Over $50.00 and Last 30 days, and 4 transactions with a total of $277.57.](app:04-search)

With Apple Intelligence, WalletFeed reads your instruction on your iPhone. Then **Search** shows the transactions and their total. Search with Apple Intelligence operates only on an iPhone that can use Apple Intelligence, and only when Apple Intelligence is active.

Without Apple Intelligence, **Search** shows the results that you get when you type your instruction in the search field. For more information, refer to [Search](/docs/search/).

## The **Sync Transactions** control

WalletFeed has a control with the name **Sync Transactions**. You can add it to Control Center, the Lock Screen or the Action button. The control shows **Sync**.

When you use the control, WalletFeed opens. With WalletFeed Pro, WalletFeed then sends new and changed transactions to your destinations. While WalletFeed is open, your destinations receive changes in seconds.

## Use your transactions in a shortcut

**Get Recent Card Transactions** gives your transactions to the subsequent action in a shortcut. For example, a shortcut can send them to Notes or Mail.

1. On your iPhone, open the Shortcuts app.
2. To make a new shortcut, tap **+**.
3. To change a shortcut that you have, tap **•••** on the shortcut.
4. Tap **Search Actions**.
5. Type WalletFeed in the search field.
6. Tap **Get Recent Card Transactions**.

   The action shows "Get card transactions from the last 7 days".

7. To change the number of days, tap **7**.
8. Type the number of days.
9. Add the actions that use the transactions.

The action gives the transactions of the [Wallet accounts](/docs/wallet-accounts/) that you select for WalletFeed. WalletFeed reads them from Wallet when the action operates. WalletFeed does not keep a copy.

The action gives this information for each transaction:

| Name in Shortcuts | Data |
| --- | --- |
| **Merchant** | The name of the merchant. If Wallet has no merchant name, **Merchant** has the description of the transaction. |
| **Amount** | The value of the transaction, with its currency. This value is more than zero for debits and for credits. |
| **Date** | The date of the transaction. |
| **Category** | The WalletFeed category, for example **Groceries** or **Dining**. |
| **Status** | The status of the transaction in Wallet, for example `pending`, `authorized`, `booked` (posted) or `rejected` (declined). |
| **Credit** | **Credit** shows if the transaction is a credit, for example a refund or a payment. |

## Send transactions with an automation

An automation in the Shortcuts app can send your transactions while WalletFeed is not open. iOS does not let apps make automations. Thus, you make the automation in Shortcuts, with the steps that WalletFeed shows.

If you do not have WalletFeed Pro, **Settings** does not show the **Sync** section. Refer to [WalletFeed Pro](/docs/walletfeed-pro/).

1. On your iPhone, open WalletFeed.
2. Tap **Settings** (the gear button) at the top of the screen.
3. In the **Sync** section, tap **Automations**.

   ![The WalletFeed Settings screen with Background Sync and Automations in the Sync section.](app:docs-settings)

4. Do the steps in the **After Each Card Tap** section.

   ![The Automations screen with Last Run, Copy Description and Open Shortcuts in the After Each Card Tap section.](app:docs-automations)

5. If the screen also shows **Every Day**, do the steps in the **Every Day** section.

The steps on the screen are different on iOS 26 and iOS 27. On iOS 27, when Apple Intelligence is active, step 1 is **Copy Description**. You paste the copied text in Shortcuts. Then you make sure that the automation is correct.

On iOS 27, a different procedure is below the steps. It is in **Set It Up Yourself** when Apple Intelligence is active, or in **Describe It Instead** when Apple Intelligence is not active. For the steps of each procedure, refer to [Run a shortcut after each Apple Card purchase](/guides/apple-card-shortcuts/).

The **Automations** screen can show these automations:

| Automation | WalletFeed action | Result |
| --- | --- | --- |
| **After Each Card Tap** | **Sync New Purchase**, in a **Transaction** automation | WalletFeed sends each purchase some seconds after you make it with your iPhone. |
| **Every Day** | **Sync Transactions**, in a **Time of Day** automation | WalletFeed sends the changes that **After Each Card Tap** does not send, for example purchases on the internet and posted charges. |

The **Automations** screen shows **Every Day** only if **Background Sync** is off or **Sample Data** is on. When **Background Sync** is on and WalletFeed is not open, iOS starts WalletFeed approximately 1 hour or less after a change in Wallet. Thus, an **After Each Card Tap** automation is not necessary, but you can make one. Refer to [Background Sync](/docs/background-sync/).

If you made an **Every Day** automation, it continues to operate when the **Automations** screen does not show **Every Day**.

After **Sync New Purchase** starts, it waits a maximum of 18 seconds for Wallet to record the purchase. If Wallet records the purchase after this time, WalletFeed sends the purchase when it sends changes again.

### **Last Run** and the **Automations** value

On the **Automations** screen, the section of each automation starts with **Last Run**. **Last Run** shows the last time that the action operated, for example "2 hr. ago". If the action did not operate, **Last Run** shows **Never**. For **Every Day**, **Last Run** also changes when you use **Sync Transactions** with Siri or in a different shortcut.

The **Automations** value in **Settings** shows if each automation operated in its period. The period of **After Each Card Tap** is the last 14 days, and the period of **Every Day** is the last 3 days. The value is one of these:

| Value | Condition |
| --- | --- |
| **On** | Each automation on the **Automations** screen operated in its period. |
| **1 of 2** | One of the two automations operated in its period. |
| **Set Up** | No automation operated in its period, and **Background Sync** is off or **Sample Data** is on. |
| **Off** | **Background Sync** is on, **Sample Data** is off, and **After Each Card Tap** did not operate in its period. |

iOS does not tell WalletFeed about your automations. You change or delete an automation in the Shortcuts app.

## Messages from WalletFeed actions

When **Sync Transactions** or **Sync New Purchase** stops, the action gives a message. Siri shows or speaks the message. In an automation, Shortcuts can show the message as a notification. The message is one of these:

| Message | Condition |
| --- | --- |
| "Changes sent: 3." | WalletFeed sent 3 changes. The number is the total for all your destinations. |
| "Nothing new to send." | **Sync Transactions** did not find a new change. |
| "Nothing new yet." | **Sync New Purchase** did not find a new change. |
| "Changes sent: 3. One destination needs attention." | WalletFeed cannot send to one destination. If more destinations have this problem, the message gives the number of destinations. |
| "Sync requires WalletFeed Pro." | WalletFeed Pro is not active on this iPhone. |
| "Open WalletFeed and allow Wallet access." | WalletFeed cannot read your Wallet accounts. |
| "Add a destination in WalletFeed first." | WalletFeed has no destination that is on. |

Without WalletFeed Pro, **Get Recent Card Transactions** shows "This action requires WalletFeed Pro."

## Your data in Siri and Shortcuts

When you use **Show Spending** or **Search Transactions** with Siri, Siri opens WalletFeed. Siri does not receive your transactions or the totals on **Spending**. For **Search Transactions**, Siri receives only your instruction.

**Get Recent Card Transactions** gives your transactions to the shortcut or to Siri. The subsequent actions in the shortcut can send the transactions to different apps.

On your iPhone, WalletFeed records the last time that **Sync Transactions** operated and the last time that **Sync New Purchase** operated. WalletFeed uses these times to show **Last Run** on the **Automations** screen and the **Automations** value in **Settings**.

## If there is a problem

### If **Last Run** shows **Never**

The automation did not start the WalletFeed action on this iPhone.

1. On your iPhone, open the Shortcuts app.
2. Tap **Automation**.

   On iOS 27, the Shortcuts app shows the shortcuts that have an automation trigger.

3. Find the automation.
4. If you cannot find the automation, do the steps in [Send transactions with an automation](#send-transactions-with-an-automation) again.
5. Open the automation.
6. Make sure that the automation starts **Sync New Purchase** or **Sync Transactions**.
7. On iOS 26, make sure that the automation uses **Run Immediately**.
8. On iOS 27, tap the arrow adjacent to the trigger at the top of the shortcut.
9. On iOS 27, make sure that **Confirm Before Run** is off.
10. On iOS 27, tap the information button **ⓘ** › **Privacy**.
11. On iOS 27, make sure that **Allow Running When Locked** is on.

### If the message is "Sync requires WalletFeed Pro."

WalletFeed Pro is not active on this iPhone. When **Get Recent Card Transactions** shows "This action requires WalletFeed Pro.", the cause is the same.

1. Open WalletFeed.
2. Tap **Settings** (the gear button) at the top of the screen.
3. In the **Subscription** section, tap the **WalletFeed Pro** row that shows **Upgrade**.
4. If you have a plan, tap **Restore Purchases** below the plans.
5. If you do not have a plan, get WalletFeed Pro. Refer to [Get WalletFeed Pro](/docs/walletfeed-pro/#get-walletfeed-pro).

### If the message is "Open WalletFeed and allow Wallet access."

WalletFeed cannot read your Wallet accounts.

1. Open WalletFeed.
2. Tap **Transactions**.
3. If WalletFeed shows **No Cards**, do the steps in [Select the accounts from WalletFeed](/docs/wallet-accounts/#select-the-accounts-from-walletfeed).
4. If WalletFeed shows **Wallet Access Off**, do the steps in [If WalletFeed shows Wallet Access Off](/docs/wallet-accounts/#if-walletfeed-shows-wallet-access-off).

### If the message is "Add a destination in WalletFeed first."

WalletFeed has no destination that is on.

1. Open WalletFeed.
2. Tap **Destinations**.
3. If there is no destination, do the steps in [Add a destination](/docs/destinations/#add-a-destination).
4. If a destination shows **Off**, tap the destination.
5. Set **Enabled** to on.

### If the message is "Changes sent: 3. One destination needs attention."

WalletFeed cannot send to one or more destinations.

1. Open WalletFeed.
2. Tap **Destinations**.
3. Find the destination that shows a message below its name, for example "Authentication failed".

   ![The Destinations screen with the message Authentication failed and a warning symbol for the n8n destination.](app:docs-destinations-failure)

4. Find the message in [If there is a problem](/docs/destinations/#if-there-is-a-problem) on the Destinations page.
5. Do the steps for that message.
