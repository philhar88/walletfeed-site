# Choose what a destination receives

A filter selects which of your Apple Card, Apple Cash and Savings transactions a destination receives from WalletFeed. Without a filter, a destination receives all the transactions from the Wallet accounts that you share with WalletFeed.

Each destination has its own filter. For example, you can send your Apple Card transactions to one file and your Apple Cash transactions to a different file.

You set the filter on the screen of the destination, after you add the destination. To add a destination, you must have [WalletFeed Pro](/docs/walletfeed-pro/). WalletFeed Pro is a subscription with a 1-week free trial, or a one-time Lifetime purchase. Refer to [Destinations](/docs/destinations/).

## Set a filter for a destination

1. On your iPhone, open WalletFeed.
2. Tap **Destinations** at the bottom of the screen.

   ![The Destinations screen with four destinations: Lunch Money, Budget 2026, Monthly CSV and n8n.](https://walletfeed.app/docs/choose-what-to-send/walletfeed-destinations.webp)

3. Tap the destination.

   ![The Lunch Money destination screen, with the Filter switch set to off.](https://walletfeed.app/docs/choose-what-to-send/walletfeed-destination-detail.webp)

4. Set the **Filter** switch to on.

   The filter controls show below the switch: **Include**, **Minimum**, **Include Pending**, **Accounts**, **Categories** and **Exclude**.

Until you change a control, the filter includes all transactions. WalletFeed saves each change when you make it.

A destination receives a transaction only if all the filter controls include it. When you change the filter, WalletFeed does not remove the transactions that it sent before.

## Send only purchases or only credits

1. On the screen of the destination, tap **Include**.
2. Tap **Purchases** or **Credits**.

   With **Purchases**, the destination receives purchases and fees. With **Credits**, it receives credits, such as refunds and payments.

To send all transactions again, select **All** in **Include**.

## Set a minimum amount

1. On the screen of the destination, tap **None** in the **Minimum** row.
2. Type the amount, for example 50.

   The destination receives only transactions of $50 or more.

The minimum is also for credits. Thus, a destination with a minimum of 50 does not receive a refund of $20. To remove the minimum, delete the number.

## Send charges only after they post

A pending charge can change before it posts. To send each charge only after it posts, set the **Include Pending** switch to off on the screen of the destination.

OFX and QIF files include a charge only after it posts, also when **Include Pending** is on.

## Select the accounts

1. On the screen of the destination, tap **Accounts**.

   **Accounts** opens with the Wallet accounts that you share with WalletFeed.

2. Tap each account that the destination receives.

   **Accounts** shows a check mark on the row of each account that you select.

3. Tap the back button at the top of the screen.

   The **Accounts** row shows the number of accounts that you selected.

To send all the accounts again, tap **All** at the top of the **Accounts** screen.

## Select the categories

WalletFeed sets the category of each transaction from its merchant category code (MCC). The categories are **Groceries**, **Dining**, **Transport**, **Fuel**, **Travel**, **Shopping**, **Entertainment**, **Subscriptions**, **Utilities**, **Health**, **Services**, **Cash & Transfers** and **Other**.

1. On the screen of the destination, tap **Categories**.
2. Tap each category that the destination receives.

   **Categories** shows a check mark on the row of each category that you select.

3. Tap the back button at the top of the screen.

   The **Categories** row shows the number of categories that you selected.

To send all the categories again, tap **All** at the top of the **Categories** screen.

## Send no transactions from some merchants

1. On the screen of the destination, tap **Merchants** in the **Exclude** row.
2. Type the merchants, with a comma between them, for example `Uber, Starbucks`.

   The destination does not receive transactions from these merchants.

The destination does not receive a transaction if its merchant name or description contains one of the names. Part of a name is sufficient. For example, with `uber`, the destination receives no transactions from Uber or Uber Eats. Uppercase and lowercase letters give the same result.

## Make a filter with Apple Intelligence

With Apple Intelligence, you can type the filter as a sentence. WalletFeed shows the text field for Apple Intelligence only on an iPhone that can use Apple Intelligence, with Apple Intelligence on.

1. On the screen of the destination, tap the text field below **Filter**.

   Until you type, the field shows the example "Travel over $50, not Uber".

2. Type a sentence about the transactions to send, for example `Dining over $20, not Starbucks`.
3. Tap the Apple Intelligence symbol at the end of the field.

   Apple Intelligence sets the filter controls from your sentence.

4. Examine the controls below the field.
5. If the value of a control is not correct, change it.

Your sentence replaces the values of all the controls, but not **Accounts**. Apple Intelligence uses an amount or a merchant only if your sentence contains it.

Apple Intelligence operates on your iPhone. It gets only your sentence, and not your transactions.

## Send previous transactions with the filter

To send previous transactions with the filter, use [Send History](/docs/send-history/).

1. On the screen of the destination, tap **Send History**.
2. Select **30 Days**, **90 Days**, **1 Year** or **All**.
3. If WalletFeed shows a message, tap **Send**.

   The destination receives the transactions from that period that agree with the filter.

## Filter the history of a new destination

A new destination has no filter. Before it receives transactions, WalletFeed shows a message. The message tells what the destination receives, from which accounts and from when. Because the destination has no filter, the message names all the Wallet accounts that you share.

When you tap **Send**, the destination starts to receive transactions from the date in **Initial History**. **Initial History** is **All** until you change it. If **Send** is **Each Transaction** for Zapier, Make or Linear, the date is a maximum of 30 days before today.

To send only the transactions from today before you set the filter, do these steps:

1. In **Destinations**, tap **Settings** at the top of the screen.
2. In **Sync**, tap **Initial History**.

   ![WalletFeed Settings with Initial History set to All in the Sync section.](https://walletfeed.app/docs/choose-what-to-send/walletfeed-settings.webp)

3. Tap **Today**.
4. Tap **Done**.
5. Add the destination. Refer to [Destinations](/docs/destinations/).
6. In the message from WalletFeed, tap **Send** (**Save** for Files).
7. Set the filter. Refer to [Set a filter for a destination](#set-a-filter-for-a-destination).
8. Tap **Send History**.
9. Select **30 Days**, **90 Days**, **1 Year** or **All**.
10. If WalletFeed shows a message, tap **Send**.

    The destination receives the previous transactions that agree with the filter.

**Initial History** stays at **Today** for the destinations that you add after this.

## Remove the filter

To remove the filter, set the **Filter** switch to off on the screen of the destination. WalletFeed removes the values of all the filter controls, and the destination receives all transactions again. If you set **Filter** to on again, you must set each control again.

## If something goes wrong

### If WalletFeed shows "Couldn't create a rule. Try describing it another way."

Apple Intelligence cannot make a filter from your sentence.

1. Write the sentence in a different way.
2. Tap the Apple Intelligence symbol again.
3. If the message shows again, change the controls below the field.

### If the text field for Apple Intelligence does not show

Your iPhone cannot use Apple Intelligence, or Apple Intelligence is off. You can set the filter without Apple Intelligence.

1. Make sure that your iPhone can use Apple Intelligence, and that Apple Intelligence is on.
2. Open the screen of the destination again.

### If a destination does not receive a transaction

One or more filter controls do not include the transaction. If the charge is pending and **Include Pending** is off, the destination receives the charge after it posts.

1. In **Destinations**, tap the destination.
2. Examine the filter controls, for example **Minimum** and **Accounts**.
3. Change the control that does not include the transaction.
4. Tap **Send History**.
5. Select a period that includes the date of the transaction.
6. If WalletFeed shows a message, tap **Send**.

If the filter includes the transaction, find the cause in the guide for the destination. Refer to [Guides](/guides/).

### If a destination has transactions that the filter does not include

WalletFeed sent these transactions before you set the filter. A filter change does not remove them.

1. Open the service or the file that receives the transactions, for example your spreadsheet or budget app.
2. Remove the transactions that the filter does not include.
