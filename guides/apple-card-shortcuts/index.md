# Run a shortcut after each Apple Card purchase

A Shortcuts automation on your iPhone can send your Apple Card purchases to your WalletFeed [destinations](/docs/destinations/) in seconds. The automation starts only when you tap your iPhone to make a purchase with your Apple Card or Apple Cash card.

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
3. If **Settings** does not show **Sync**, get [WalletFeed Pro](/docs/walletfeed-pro/).
4. In the **Sync** section, tap **Automations**.

   ![The WalletFeed Settings screen with Background Sync and Automations in the Sync section.](https://walletfeed.app/guides/apple-card-shortcuts/walletfeed-settings.webp)

   Result: WalletFeed shows **Automations**. **After Each Card Tap** is at the top of the screen.

## Step 2: Make the automation in Shortcuts

iOS does not let apps make automations. Thus, you make the automation one time in the Shortcuts app. In **After Each Card Tap**, WalletFeed shows the steps for your iPhone. These steps are different for iOS 26, iOS 27 and iOS 27 with Apple Intelligence.

Do only the procedure for your iPhone. To find this procedure, look at step 1 in WalletFeed.

### iOS 27 with Apple Intelligence

On iOS 27 with Apple Intelligence, Shortcuts can make a shortcut from text that you give it. WalletFeed gives you the text. In WalletFeed, step 1 is **Copy Description**.

1. In **After Each Card Tap**, tap **Copy Description**.

   ![The Automations screen with Copy Description and its text below After Each Card Tap.](https://walletfeed.app/guides/apple-card-shortcuts/walletfeed-automations.webp)

   Result: WalletFeed copies the text below **Copy Description** and shows **Copied**. The text is "When I tap my Apple Card or Apple Cash card, run Sync New Purchase from WalletFeed without asking."
2. Tap **Open Shortcuts**.

   Result: The Shortcuts app opens.
3. Tap **+**.

   Result: Shortcuts shows a new shortcut. You can type the task that the shortcut must do.
4. Paste the text.
5. Make sure that the shortcut uses your Apple Card or Apple Cash card.
6. Tap the arrow adjacent to the trigger at the top of the shortcut.
7. Make sure that **Confirm Before Run** is off.
8. Tap the information button **ⓘ** › **Privacy**.
9. Make sure that **Allow Running When Locked** is on.
10. Tap **Done**.

If Shortcuts does not let you type the task or does not make the automation, do these steps:

1. Open WalletFeed again.
2. In **After Each Card Tap**, tap **Set It Up Yourself**.
3. Below **Set It Up Yourself**, tap **Open Shortcuts**.
4. Do steps 2 to 11 in [iOS 27 without Apple Intelligence](#ios-27-without-apple-intelligence).

### iOS 27 without Apple Intelligence

On iOS 27, an automation is a trigger at the top of a shortcut. In WalletFeed, step 1 is **Open Shortcuts**, and **Describe It Instead** is below the steps.

1. In **After Each Card Tap**, tap **Open Shortcuts**.

   Result: Shortcuts opens a new shortcut.
2. Tap **Add Action**.
3. Type WalletFeed in the search field.
4. Tap **Sync New Purchase**.
5. In the action list, tap **Automation** › **Transaction**.
6. Select your cards.
7. Tap the arrow adjacent to the trigger at the top of the shortcut.
8. Set **Confirm Before Run** to off.
9. Tap the information button **ⓘ** › **Privacy**.
10. Set **Allow Running When Locked** to on.
11. Tap **Done**.

### iOS 26

On iOS 26, automations have a tab in Shortcuts. Your other devices do not get these automations. In WalletFeed, step 1 is **Open Shortcuts**, and WalletFeed does not show **Describe It Instead**.

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
13. If you use WalletFeed on a different iPhone, do this procedure again on that iPhone.

## Step 3: Make sure that the automation operates

After you tap your iPhone to make a purchase with your Apple Card or Apple Cash card, do these steps:

1. Open WalletFeed.
2. Tap **Settings** (the gear button) at the top of the screen.
3. In the **Sync** section, look at the value adjacent to **Automations**.

   Result: **Automations** shows **On** or **1 of 2**. The table below gives each value.
4. Tap **Automations**.
5. In **After Each Card Tap**, look at **Last Run**.

   Result: **Last Run** shows the time of the last operation of **Sync New Purchase**, for example "2 hr. ago".
6. If **Last Run** shows **Never**, refer to [If Last Run shows Never after a purchase](#if-last-run-shows-never-after-a-purchase).

**Automations** in **Settings** shows if each automation operated in its period. The period is the last 14 days for **After Each Card Tap** and the last 3 days for **Every Day**.

| **Automations** shows | Condition |
| --- | --- |
| **On** | Each automation on the **Automations** screen operated in its period. |
| **1 of 2** | Only one of the two automations operated in its period. |
| **Set Up** | No automation operated in its period, and [Background Sync](/docs/background-sync/) is off or **Sample Data** is on. |
| **Off** | **After Each Card Tap** did not operate in the last 14 days, **Background Sync** is on, and **Sample Data** is off. |

When **Background Sync** is on, the automation is not necessary. Without the automation, iOS starts WalletFeed approximately 1 hour or less after a change in Wallet.

## Time to send each purchase

When you tap your iPhone to make a purchase with your Apple Card or Apple Cash card, the automation starts **Sync New Purchase**. This WalletFeed action operates in the background. It does not open WalletFeed.

At that time, Wallet does not have the purchase. First, WalletFeed sends the changes that your destinations did not receive. Then it waits for Wallet to record the purchase. When Wallet records the purchase, WalletFeed sends the purchase to your destinations.

WalletFeed waits for the purchase until 18 seconds after the action starts. If Wallet records the purchase after that time, WalletFeed sends the purchase when it sends other changes. While WalletFeed is open, it sends each change in seconds. When WalletFeed is not open and **Background Sync** is on, iOS starts WalletFeed approximately 1 hour or less after a change in Wallet. Refer to [Background Sync](/docs/background-sync/).

The automation starts only when you tap your iPhone to make a purchase. Thus, online purchases and posted charges do not start the automation. Your Savings account has no card. As a result, Savings transactions also do not start the automation. WalletFeed sends these changes while WalletFeed is open, or when iOS starts WalletFeed.

The automation does not change the data that WalletFeed sends to your destinations. WalletFeed also uses the filter of each destination. Refer to [filters for destinations](/docs/choose-what-to-send/).

After your iPhone starts again, WalletFeed cannot send to destinations until you type your passcode one time.

When the action stops, it gives a short message. Shortcuts can show the message as a notification.

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

If **Background Sync** is off or **Sample Data** is on, **Automations** also shows **Every Day**. An **Every Day** automation starts **Sync Transactions** at a time that you select. This action sends new transactions and other changes to your destinations, for example online purchases and posted charges.

For **Every Day**, the text that you paste is "Every day at 9 PM, run Sync Transactions from WalletFeed without asking."

To make the automation, do [Step 2](#step-2-make-the-automation-in-shortcuts) with these changes:

- Use the steps below **Every Day** in WalletFeed.
- If you paste the text, make sure that the time in Shortcuts is correct.
- Tap **Sync Transactions**, not **Sync New Purchase**.
- Tap **Time of Day**, not **Transaction**.
- Select a time, not your cards.

If **Background Sync** is on, iOS starts WalletFeed approximately 1 hour or less after a change in Wallet. Thus, WalletFeed does not show **Every Day**. An **Every Day** automation that you made continues to operate.

## Stop or change the automation

iOS does not tell WalletFeed about your automations. To change the cards or the time, open the automation in the Shortcuts app.

To stop the automation, delete it in the Shortcuts app. After you delete it, WalletFeed sends new purchases while WalletFeed is open, or when iOS starts WalletFeed. The transactions that WalletFeed sent stay at each destination.

## Other WalletFeed actions in Shortcuts

WalletFeed has more actions for the Shortcuts app. For example, **Get Recent Card Transactions** gives your transactions from the last 7 days to the subsequent action in a shortcut. You can change the number of days. Refer to [Siri and Shortcuts](/docs/siri-and-shortcuts/).

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

1. If a destination has a filter, make sure that the filter includes the purchase (refer to [filters for destinations](/docs/choose-what-to-send/)).
2. To send the purchase at this time, open WalletFeed.

> **Note:** If you do not open WalletFeed, WalletFeed sends the purchase when iOS starts WalletFeed. When WalletFeed is not open and **Background Sync** is on, iOS starts WalletFeed approximately 1 hour or less after a change in Wallet.

### If the message is "Sync requires WalletFeed Pro."

WalletFeed Pro is not active on this iPhone.

1. Open WalletFeed.
2. Tap **Settings** (the gear button) at the top of the screen.
3. Tap **WalletFeed Pro**.
4. If your Apple Account has a WalletFeed Pro purchase, tap **Restore Purchases**.
5. If you do not have WalletFeed Pro, get it (refer to [WalletFeed Pro](/docs/walletfeed-pro/)).

### If the message is "Open WalletFeed and allow Wallet access."

WalletFeed does not have access to your Wallet accounts.

1. On your iPhone, open the Settings app.
2. Tap **Privacy & Security** › **Wallet** › **WalletFeed**.
3. Select the accounts that WalletFeed can read (refer to [Wallet accounts](/docs/wallet-accounts/)).
4. Open WalletFeed.

### If the message is "Add a destination in WalletFeed first."

WalletFeed has no destination that is on.

1. Open WalletFeed.
2. Tap **Destinations**.
3. If a destination shows **Off**, do these steps:

   1. Tap the destination.
   2. Set **Enabled** to on.

4. If there is no destination, tap **+** to add a destination (refer to [Destinations](/docs/destinations/)).

### If the message includes "needs attention" or "need attention"

WalletFeed cannot send to one or more destinations.

1. Open WalletFeed.
2. Tap **Destinations**.
3. Find the destination with the problem. Below its name, WalletFeed shows the cause, for example "Authentication failed".

   ![The Destinations screen with Authentication failed and a warning symbol for the n8n destination.](https://walletfeed.app/guides/apple-card-shortcuts/walletfeed-destinations-failure.webp)
4. Tap the destination.
5. Do the steps for this cause in [Troubleshooting](/docs/troubleshooting/) or in the guide for the destination.
