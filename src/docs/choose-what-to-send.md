+++
title = "Filter the transactions for a destination"
nav_title = "Filters"
seo_title = "Filter your Apple Card transactions for each destination"
description = "A WalletFeed filter selects the Apple Card, Apple Cash and Savings transactions that a destination receives, by account, category, merchant or amount."
order = 130
related = ["docs/destinations", "docs/send-history"]
updated = 2026-10-30
+++

A filter selects the Apple Card, Apple Cash and Savings transactions that a destination receives from WalletFeed. If a destination has no filter, it receives all the transactions of the [Wallet accounts that WalletFeed reads](/docs/wallet-accounts/).

You can set a filter for each destination. For example, you can send your Apple Card transactions to one file and your Apple Cash transactions to a different file. After you add a destination, you set its filter on the screen of the destination.

To add a destination, you must have [WalletFeed Pro](/docs/walletfeed-pro/). WalletFeed Pro is a subscription with a 1-week free trial, or a one-time Lifetime purchase. [Destinations](/docs/destinations/) tells you how to add a destination.

## Set a filter for a destination

1. On your iPhone, open WalletFeed.
2. Tap **Destinations** at the bottom of the screen.

   ![The Destinations screen with four destinations: Lunch Money, Budget 2026, Monthly CSV and n8n.](app:07-destinations)

3. Tap the destination.

   ![The screen of the Lunch Money destination, with the Filter switch in the off position.](app:docs-destination-detail)

4. Set the **Filter** switch to on.

   Below the switch, WalletFeed shows the filter controls: **Include**, **Minimum**, **Include Pending**, **Accounts**, **Categories** and **Exclude**.

A destination receives a transaction only if all the filter controls include it. Until you change a control, the filter includes all transactions.

WalletFeed saves the filter each time that you change a control. When you change the filter, WalletFeed does not remove the transactions that the destination received.

## Send only purchases or only credits

1. On the screen of the destination, tap **Include**.
2. Tap **Purchases** or **Credits**.

   If you tap **Purchases**, the destination receives purchases and fees. If you tap **Credits**, the destination receives credits, for example refunds and payments.

To send all transactions again, select **All** in **Include**.

## Set a minimum amount

1. On the screen of the destination, tap **None** in the **Minimum** row.
2. Type the amount, for example 50.

   The destination receives only transactions of $50 or more.

WalletFeed uses the minimum for purchases and for credits. For example, a destination with a minimum of 50 does not receive a refund of $20.

To remove the minimum, delete the number in the **Minimum** row.

## Send charges only after they post

A pending charge can change before it posts.

1. On the screen of the destination, set the **Include Pending** switch to off.

   The destination receives each charge only after the charge posts.

OFX and QIF files include a charge only after it posts. The **Include Pending** switch does not change this.

## Select the accounts

1. On the screen of the destination, tap **Accounts**.

   The **Accounts** screen shows the Wallet accounts that WalletFeed reads.

2. Tap each account to send its transactions to the destination.

   The **Accounts** screen shows a checkmark on the row of each account that you select.

3. Tap the back button at the top of the screen.

   The **Accounts** row shows the number of accounts that you selected.

To send the transactions of all the accounts again, tap **All** at the top of the **Accounts** screen.

## Select the categories

WalletFeed sets the category of each transaction from its merchant category code (MCC). The categories are **Groceries**, **Dining**, **Transport**, **Fuel**, **Travel**, **Shopping**, **Entertainment**, **Subscriptions**, **Utilities**, **Health**, **Services**, **Cash & Transfers** and **Other**.

1. On the screen of the destination, tap **Categories**.
2. Tap each category to send its transactions to the destination.

   The **Categories** screen shows a checkmark on the row of each category that you select.

3. Tap the back button at the top of the screen.

   The **Categories** row shows the number of categories that you selected.

To send the transactions of all the categories again, tap **All** at the top of the **Categories** screen.

## Send no transactions from some merchants

1. On the screen of the destination, tap **Merchants** in the **Exclude** row.
2. Type the merchant names, with a comma between the names, for example `Uber, Starbucks`.

   The destination does not receive transactions from these merchants.

If the merchant name or the description of a transaction contains one of the names that you typed, the destination does not receive the transaction. You can type part of a name. For example, if you type `uber`, the destination does not receive transactions from Uber or Uber Eats. Uppercase and lowercase letters give the same result.

## Make a filter with Apple Intelligence

With Apple Intelligence, you can make a filter from a sentence. WalletFeed shows the text field for Apple Intelligence only if your iPhone can use Apple Intelligence and Apple Intelligence is active.

1. On the screen of the destination, set the **Filter** switch to on.
2. Tap the text field below **Filter**.

   Until you type, the field shows the example "Travel over $50, not Uber".

3. Type a sentence about the transactions to send to the destination, for example `Dining over $20, not Starbucks`.
4. Tap the Apple Intelligence icon at the end of the field.

   Apple Intelligence sets the filter controls from your sentence.

5. Examine the controls below the field.
6. If the value of a control is not correct, change the value.

When Apple Intelligence sets the controls, it does not keep the values that you set previously. But the accounts that you selected do not change. The **Minimum** and **Exclude** controls get only the amounts and merchant names that are in your sentence.

Apple Intelligence makes the filter on your iPhone from your sentence. It does not get your transactions.

## Send previous transactions with the filter

With [Send History](/docs/send-history/), you can send previous transactions to the destination.

1. On the screen of the destination, tap **Send History**.
2. Tap **30 Days**, **90 Days**, **1 Year** or **All**.
3. If WalletFeed shows a message, tap **Send**.

   The destination receives the transactions from that period that the filter includes.

## Filter the history of a new destination

Before a new destination receives transactions, WalletFeed shows a message. The message tells you the accounts and the start date of the transactions that the destination will receive. A new destination has no filter. Thus, the message shows all the Wallet accounts that WalletFeed reads.

When you tap **Send** (**Save** for a Files destination), the destination starts to receive transactions from the start date in **Initial History**. Until you change **Initial History**, it is **All**. A new Zapier, Make or Linear destination receives a maximum of 30 days of previous transactions.

To set the filter before a new destination receives previous transactions, set **Initial History** to **Today** before you add the destination.

1. In WalletFeed, tap **Destinations** at the bottom of the screen.
2. Tap **Settings** (the gear button) at the top of the screen.
3. In the **Sync** section, tap **Initial History**.

   ![The Settings screen, with All in the Initial History row of the Sync section.](app:docs-settings)

4. Tap **Today**.
5. Tap **Done**.
6. Add the destination. Refer to [Destinations](/docs/destinations/).
7. In the message from WalletFeed, tap **Send** (**Save** for a Files destination).
8. Set the filter. Refer to [Set a filter for a destination](#set-a-filter-for-a-destination).
9. Tap **Send History**.
10. Tap **30 Days**, **90 Days**, **1 Year** or **All**.
11. If WalletFeed shows a message, tap **Send**.

    The destination receives the previous transactions that the filter includes.

**Initial History** stays at **Today** for the destinations that you add after this procedure.

## Remove the filter

1. On the screen of the destination, set the **Filter** switch to off.

   The destination receives all transactions again. WalletFeed removes the values of all the filter controls.

If you set the **Filter** switch to on again, you must set each control again.

To send the previous transactions that the filter did not include, use [Send History](/docs/send-history/).

## If there is a problem

### If WalletFeed shows "Couldn't create a rule. Try describing it another way."

Apple Intelligence cannot make a filter from your sentence.

1. Change the sentence in the text field.
2. Tap the Apple Intelligence icon again.
3. If WalletFeed shows the message again, set the controls below the field yourself.

### If WalletFeed does not show the text field for Apple Intelligence

The **Filter** switch is off, your iPhone cannot use Apple Intelligence, or Apple Intelligence is not active. You can set the filter without Apple Intelligence.

1. On the screen of the destination, set the **Filter** switch to on.
2. If WalletFeed does not show the field, make sure that your iPhone model is on the list in [Get started with the next generation of Apple Intelligence](https://support.apple.com/en-us/121115).
3. Open the Settings app.
4. Tap **Apple Intelligence & Siri**.
5. Activate Apple Intelligence.
6. Open WalletFeed again.
7. In **Destinations**, tap the destination.

### If a destination does not receive a transaction

One or more filter controls do not include the transaction. If the transaction is a pending charge and the **Include Pending** switch is off, the destination receives the charge after it posts.

1. In **Destinations**, tap the destination.
2. Examine the filter controls, for example **Minimum** and **Accounts**.
3. Change the control that does not include the transaction.
4. Tap **Send History**.
5. Tap a period that includes the date of the transaction.
6. If WalletFeed shows a message, tap **Send**.

If the filter includes the transaction, find the cause in the guide for the destination. Refer to [Destination types](/docs/destinations/#destination-types).

### If a destination has transactions that the filter does not include

WalletFeed sent these transactions before you set the filter. When you change the filter, WalletFeed does not remove them.

1. Open the service or the file that receives the transactions, for example your spreadsheet or your budget app.
2. Remove the transactions that the filter does not include.
