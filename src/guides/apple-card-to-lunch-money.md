+++
title = "Send Apple Card transactions to Lunch Money"
nav_title = "Lunch Money"
seo_title = "Apple Card to Lunch Money: send transactions from iPhone"
description = "WalletFeed sends your Apple Card, Apple Cash and Savings transactions from your iPhone to Lunch Money. You paste a Lunch Money access token in WalletFeed."
group = "Budgeting apps"
order = 10
related = ["guides/apple-card-to-pocketsmith", "docs/destinations", "docs/send-history"]
updated = 2026-10-30
+++

WalletFeed sends your Apple Card, Apple Cash and Savings transactions from your iPhone to Lunch Money. You get an access token in Lunch Money, then paste it in WalletFeed.

## Before you start

You must have these items:

- An iPhone with iOS 26 or a newer version. WalletFeed is available only in the US.
- WalletFeed, with access to your Wallet accounts.
- WalletFeed Pro. You must have it to send transactions to Lunch Money. It is a subscription with a 1-week free trial, or a one-time Lifetime purchase. Refer to [WalletFeed Pro](/docs/walletfeed-pro/).
- A Lunch Money budget. Lunch Money has a 30-day free trial, and you can start the trial without a credit card.

## Your access token stays on your iPhone

- WalletFeed keeps the access token in the Keychain on your iPhone. iOS encrypts the Keychain.
- The access token does not go to iCloud Keychain or to your other devices.
- WalletFeed has no account and no servers. No person at WalletFeed can see or get the access token.
- Your iPhone sends the access token only to Lunch Money, in each request to Lunch Money.
- When you delete the destination, WalletFeed deletes the access token from your iPhone. You can also revoke the token in Lunch Money.

## Step 1: Select Lunch Money in WalletFeed

1. On your iPhone, open WalletFeed.
2. Tap **Destinations**.
3. Tap **+** at the top of the screen.

   ![The empty Destinations screen with the + button at the top.](app:docs-destinations-empty-pro)

4. Tap **Lunch Money**, below **Budgeting**.

   ![The Add Destination screen with Lunch Money in the Budgeting list.](app:08-add-destination)

   Result: WalletFeed shows the Lunch Money screen. If you do not have WalletFeed Pro, WalletFeed shows **WalletFeed Pro** first.
5. If WalletFeed shows **WalletFeed Pro**, get WalletFeed Pro. Refer to [WalletFeed Pro](/docs/walletfeed-pro/).

   Result: WalletFeed shows the Lunch Money screen.

## Step 2: Get an access token in Lunch Money

An access token lets WalletFeed send transactions to one Lunch Money budget. The token is for the budget that is open when you get it.

1. On the Lunch Money screen in WalletFeed, tap **Open Developers**.

   ![The Lunch Money screen in WalletFeed with the Access Token field and the Open Developers link.](app:docs-setup-lunch-money)

   Result: Your iPhone shows the Lunch Money Developers page.
2. If Lunch Money shows its login page, get access to Lunch Money with your e-mail address and password.
3. If you have more than one budget, tap the green circle at the top right of the page.

   Result: Lunch Money shows **Switch Accounts**.
4. If Lunch Money shows **Switch Accounts**, select the budget for your transactions.
5. At the top right of the page, type a label for the token (for example, WalletFeed).
6. Tap **Request Access Token**.

   Result: Lunch Money shows the token one time only. If you close the page before you copy the token, you must get a new token.
7. Tap the copy button.

## Step 3: Paste the token in WalletFeed

1. Open WalletFeed again.

   Result: WalletFeed shows the Lunch Money screen.
2. If WalletFeed shows a different screen, do [Step 1](#step-1-select-lunch-money-in-walletfeed) again.
3. Paste the token in the **Access Token** field.

   Result: WalletFeed connects to Lunch Money and shows **Account**.
4. In **Account**, select the Lunch Money account for your transactions.

   If you select **New Apple Card Account**, WalletFeed makes a credit account with the name Apple Card. Its balance is 0.

   If your budget has an account with the name Apple Card, WalletFeed selects that account. The list then does not show **New Apple Card Account**.

   The list does not show closed accounts or accounts that cannot have transactions.
5. Tap **Add**.

   Result: WalletFeed shows **Send Transactions to Lunch Money?** with a message. The message tells you what Lunch Money receives, from which Wallet accounts and from which date.

   If you tap **Cancel**, WalletFeed removes the new destination and does not send transactions.
6. Tap **Send**.

   Result: WalletFeed starts to send transactions to Lunch Money.

   ![The Destinations screen with Lunch Money and three other destinations.](app:07-destinations)

The Lunch Money **Transactions** page shows the transactions.

## Data that Lunch Money receives

WalletFeed adds each transaction to the Lunch Money account that you selected. The table gives the Lunch Money field for each item.

| WalletFeed sends | Lunch Money field |
| --- | --- |
| Date of the transaction, in your time zone | Date |
| Merchant name, or the description if there is no merchant name | Payee |
| Card statement text | Original payee name |
| Amount | Amount |
| Currency | Currency |
| Transaction ID | External ID |
| Wallet status, transaction type, merchant category code and WalletFeed category | Custom metadata |

A purchase goes to Lunch Money as money out. A payment goes to Lunch Money as money in. WalletFeed uses the external ID to find the transaction again when the transaction changes. Apps that use the Lunch Money API can read the custom metadata.

WalletFeed does not set the Lunch Money category. Lunch Money uses your rules on each new transaction. Thus, a rule can set the category. Lunch Money shows each new transaction as unreviewed.

After WalletFeed adds a transaction, WalletFeed does not change the payee, category, notes, tags or review status. When the date, amount, currency or Wallet status changes in Wallet, WalletFeed makes the same change in Lunch Money.

WalletFeed does not change the balance of the Lunch Money account. To correct the balance, you can change it on the Lunch Money **Accounts** page.

Lunch Money receives transactions from all the Wallet accounts that WalletFeed has access to. WalletFeed sends all of these transactions to the Lunch Money account that you selected. To send transactions from only some Wallet accounts, you can use a filter. Refer to [Send only some transactions](#send-only-some-transactions).

Your transactions go from your iPhone directly to Lunch Money. WalletFeed has no account and no WalletFeed servers. WalletFeed keeps the token in the Keychain on your iPhone. After Lunch Money receives your transactions, the terms of Lunch Money are applicable to them.

## New and changed transactions

While WalletFeed is open, Lunch Money receives changes in seconds. When WalletFeed is not open, iOS starts WalletFeed approximately 1 hour or less after a change in Wallet. If [Background Sync](/docs/background-sync/) is on in **Settings** › **Sync**, WalletFeed then sends the change.

Wallet shows a new charge as pending until the charge posts. Lunch Money does not show transactions in a manual account as pending. Thus, Lunch Money shows a pending charge as a usual transaction. WalletFeed sends the Wallet status in the custom metadata.

When the charge posts, WalletFeed changes the same transaction in Lunch Money. The date does not change. If the posted amount is different, WalletFeed changes the amount. To send charges only after they post, you can set **Include Pending** to off in the filter.

A refund goes to Lunch Money as money in. If Wallet shows a charge as declined or expired, WalletFeed deletes the charge from Lunch Money. WalletFeed also deletes a transaction that Wallet removes. But WalletFeed does not delete a transaction that you divided or put in a group in Lunch Money.

## Send previous transactions

A new destination also receives previous transactions from the start date in **Settings** › **Sync** › **Initial History**. **Initial History** is **All** until you change it. For a different start date, you can change **Initial History** before you add Lunch Money.

To send more previous transactions after you add Lunch Money, use [Send History](/docs/send-history/):

1. In **Destinations**, tap the Lunch Money destination.

   ![The Lunch Money destination in WalletFeed with Replace Token, Filter, Send History, Send Test and Delete.](app:docs-destination-detail)

2. Tap **Send History**.
3. Select **30 Days**, **90 Days**, **1 Year** or **All**.

   Result: WalletFeed shows **Sending History** with the number of transactions that it sent.

WalletFeed sends previous transactions to Lunch Money in groups of 50. It waits 45 seconds between groups. Lunch Money does not receive the same transaction two times.

To stop **Send History**, do these steps:

1. Tap **Send History**.
2. Tap **Stop Sending**.

## Change or remove the destination

### Send only some transactions

1. In **Destinations**, tap the Lunch Money destination.
2. Set **Filter** to on.
3. Set the filter controls (refer to the table).

| Control | Result |
| --- | --- |
| **Include** | WalletFeed sends all transactions, only purchases or only credits. |
| **Minimum** | WalletFeed sends only transactions of this amount or more. |
| **Include Pending** | If **Include Pending** is off, WalletFeed sends charges only after they post. |
| **Accounts** | WalletFeed sends only transactions from the Wallet accounts that you select. |
| **Categories** | WalletFeed sends only transactions in the categories that you select. |
| **Exclude** | WalletFeed does not send transactions from the merchants that you type. You must type a comma between two merchants. |

If Apple Intelligence is active, you can also type a rule in words:

1. In the field that shows "Travel over $50, not Uber", type the rule.
2. Tap the Apple Intelligence icon at the end of the field.

WalletFeed uses the filter only for the transactions that it sends after you set the filter.

### Replace the token

1. Get a new access token for the same budget. Refer to [Step 2](#step-2-get-an-access-token-in-lunch-money).

   If the new token is for a different budget, WalletFeed cannot get access to the account.
2. In **Destinations**, tap the Lunch Money destination.
3. Tap **Replace Token**.
4. Paste the new token in the **Access Token** field.
5. Tap **Replace**.

   Result: WalletFeed shows a green checkmark.

### Stop or delete the destination

To stop the destination for a time, do these steps:

1. In **Destinations**, tap the Lunch Money destination.
2. Set **Enabled** to off.

   Until you set **Enabled** to on again, WalletFeed does not send transactions to Lunch Money.

To delete the destination, do these steps:

1. In **Destinations**, tap the Lunch Money destination.
2. Tap **Delete**.
3. Tap **Delete** again.

The transactions that WalletFeed sent stay in Lunch Money. To make sure that the token cannot get access to your budget, do these steps:

1. On your iPhone, open [the Lunch Money Developers page](https://my.lunchmoney.app/developers).
2. Tap **Revoke** for the WalletFeed token.

## If there is a problem

### If WalletFeed shows "Token rejected" or "Authentication failed"

Lunch Money does not accept the token. This occurs if a person used **Revoke** on the token, or if the pasted text is only a part of the token.

1. Get a new access token. Refer to [Step 2](#step-2-get-an-access-token-in-lunch-money).
2. If WalletFeed shows the Lunch Money screen, paste the new token in the **Access Token** field.
3. If **Destinations** shows the Lunch Money destination, replace the token. Refer to [Replace the token](#replace-the-token).

### If WalletFeed shows "The account is gone from Lunch Money"

Lunch Money does not have the account for this destination, or the token is for a different budget.

1. In **Destinations**, tap the Lunch Money destination.
2. Tap **Delete**.
3. Tap **Delete** again.
4. Do [Step 1](#step-1-select-lunch-money-in-walletfeed), Step 2 and Step 3 again.

### If the transactions go to an incorrect budget

The token is for the budget that was open when you got the token.

1. Delete the Lunch Money destination. Refer to [Stop or delete the destination](#stop-or-delete-the-destination).
2. Do [Step 1](#step-1-select-lunch-money-in-walletfeed), Step 2 and Step 3 again.

The transactions in the incorrect budget stay there. You can delete them in Lunch Money.

### If Lunch Money does not receive new transactions

WalletFeed cannot send transactions to Lunch Money. For example, the destination is off, or **Background Sync** is off.

1. Open WalletFeed. While WalletFeed is open, it sends changes in seconds.
2. If **Destinations** shows **Sync Requires Pro**, tap **Upgrade**.
3. If the Lunch Money destination shows **Off**, set **Enabled** to on in the destination.
4. If **Filter** is on, make sure that the filter includes the new transactions.
5. Tap **Settings** (the gear button) at the top of the screen.
6. Make sure that **Background Sync** is on.
7. Tap **Sync Now**.

After your iPhone starts again, WalletFeed cannot send transactions to destinations until you type your passcode one time.

To make sure that WalletFeed can send transactions to Lunch Money, tap **Send Test** in the destination. If Lunch Money receives the test transaction, WalletFeed shows a green checkmark.

> **Note:** **Send Test** adds a test transaction of $4.20 to the Lunch Money account. The payee of the test transaction is WalletFeed. You can delete the test transaction in Lunch Money.

### If the balance in Lunch Money is not correct

WalletFeed does not change the balance of the Lunch Money account.

1. In Lunch Money, open the **Accounts** page.
2. Change the balance of the account that receives your transactions.

### If WalletFeed shows "Too many requests" or "Rejected (HTTP 429)"

Lunch Money accepts a maximum of 100 requests each minute.

1. Wait. WalletFeed tries again at the time that it shows, or when it starts to send changes again.
