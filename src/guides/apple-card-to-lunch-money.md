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

WalletFeed sends your Apple Card, Apple Cash and Savings transactions from your iPhone to Lunch Money. You make an access token in Lunch Money, then you paste the token in WalletFeed.

## Before you start

You must have these items:

- An iPhone with iOS 26 or a newer version. WalletFeed is available only in the US.
- WalletFeed on your iPhone, with access to your Apple Card, Apple Cash or Savings account.
- [WalletFeed Pro](/docs/walletfeed-pro/) (a subscription with a 1-week free trial, or a one-time Lifetime purchase). You must have WalletFeed Pro to send transactions to Lunch Money.
- A Lunch Money account and its password. Lunch Money has a 30-day free trial, and you can start the trial without a payment card. You can make an access token during the trial.

> **Note:** During the free trial, each Lunch Money page shows "Enter your billing information to avoid interruption in service!" This information is not necessary for an access token.

## Your access token stays on your iPhone

- WalletFeed keeps the access token in the Keychain on your iPhone. iOS encrypts the Keychain.
- The access token does not go to iCloud Keychain or to your other devices.
- WalletFeed has no account and no servers. No person at WalletFeed can see or get the access token.
- Your iPhone sends the access token only to Lunch Money, in each request to Lunch Money.
- When you delete the destination, WalletFeed deletes the access token from your iPhone. You can also delete the token in Lunch Money.

## Step 1: Open the Lunch Money form in WalletFeed

1. On your iPhone, open WalletFeed.
2. Tap **Destinations**.
3. Tap **+** at the top of the screen.

   ![The Destinations screen with no destinations, and the + icon at the top.](app:docs-destinations-empty-pro)

4. Below **Budgeting**, tap **Lunch Money**.

   ![The Add Destination screen with Lunch Money in the Budgeting list.](app:08-add-destination)

5. If WalletFeed shows **WalletFeed Pro**, get [WalletFeed Pro](/docs/walletfeed-pro/).

   Result: After you get WalletFeed Pro, WalletFeed shows the Lunch Money form.

## Step 2: Make an access token in Lunch Money

A Lunch Money access token gives access to all of the data in one budget. The token is for the budget that is open when you make the token. With the token, WalletFeed gets the list of your Lunch Money accounts and can make an Apple Card account. WalletFeed also adds, changes and deletes the transactions that it sends.

You can delete the token in Lunch Money (refer to [Delete the token in Lunch Money](#delete-the-token-in-lunch-money)). After you delete the token, WalletFeed cannot connect to Lunch Money with it.

To make the token on your iPhone, do these steps:

1. In the Lunch Money form, tap **Open Developers**.

   ![The Lunch Money form in WalletFeed, with the Access Token field and the Open Developers link.](app:docs-setup-lunch-money)

   Result: Your web browser opens Lunch Money.

2. If Lunch Money shows "Welcome back!", get access to your Lunch Money account with your e-mail address and your password.

   ![The Lunch Money login page, with the LOGIN button highlighted.](web:lunch-money/01-login)

   Result: Lunch Money shows **Home**. Lunch Money does not go back to the **Developers** page.

3. If Lunch Money does not show the **Developers** page, tap **☰** › **DEVELOPERS**.

   The menu icon (**☰**) is at the top right of the page. In the menu, **DEVELOPERS** is below **SETTINGS**.

   ![On an iPhone, the Lunch Money menu, with DEVELOPERS highlighted below SETTINGS.](web:lunch-money/14-iphone-menu-developers)

   Result: Lunch Money shows the **Developers** page.

4. Tap the green circle at the top of the page.

   The circle shows the first letter of the name of your budget. It is to the left of **☰**.

   ![On an iPhone, the top of the Lunch Money Developers page, with the green budget circle highlighted.](web:lunch-money/15-iphone-green-circle)

   Result: Lunch Money shows **Switch Accounts**. The open budget has "(Current)" after its name.

5. If you have more than one budget, tap the budget for your transactions.

   Above the list of budgets, Lunch Money shows **Create new budget account**. Do not tap it.

   ![On an iPhone, the Switch Accounts dialog in Lunch Money, with the open budget highlighted.](web:lunch-money/16-iphone-switch-accounts)

6. If you have only one budget, tap **CLOSE**.
7. Scroll to **NEW ACCESS TOKEN**.

   Lunch Money shows **NEW ACCESS TOKEN** below the form "Submit your contribution to Lunch Money". Do not use that form. That form sends a project to Lunch Money and does not make a token.

8. In **Label for access token (optional)**, type `WalletFeed`.

   The label helps you find the WalletFeed token in **ACTIVE ACCESS TOKENS**. It is not necessary to select an item in **What will you use this API key for? (optional)**.

   ![The new access token form in Lunch Money, with the label WalletFeed highlighted.](web:lunch-money/06-token-label)

9. Tap **REQUEST NEW ACCESS TOKEN**.

   ![On an iPhone, the new access token form below the SUBMIT button, with REQUEST NEW ACCESS TOKEN highlighted.](web:lunch-money/17-iphone-request-token)

   Result: Lunch Money shows the token in a box. Above the box, Lunch Money shows "This is your access token. Please save it now as this is the only time it will be shown to you!"

   > **Caution:** Do not tap **GOT IT!** before you tap **Copy**. After you tap **GOT IT!**, Lunch Money cannot show the token again.

10. In the box with the token, tap **Copy**.

    Lunch Money shows **Copy** in small text at the right end of the box.

    ![On an iPhone, the new access token in Lunch Money, with Copy highlighted.](web:lunch-money/18-iphone-token-shown-copy)

    Result: **Copy** changes to **Copied!**.

11. Tap **GOT IT!**.

    ![The Lunch Money token box after you copy the token, with the GOT IT! button highlighted.](web:lunch-money/10-token-copied-got-it)

    Result: Lunch Money closes the box. **ACTIVE ACCESS TOKENS** shows the WalletFeed token.

## Step 3: Paste the token in WalletFeed

1. Open WalletFeed again.
2. If WalletFeed does not show the Lunch Money form, do [Step 1](#step-1-open-the-lunch-money-form-in-walletfeed) again.
3. Touch and hold **Access Token**.
4. Tap **Paste**.

   Result: WalletFeed connects to Lunch Money with the token. Then WalletFeed shows **Account**.

5. In **Account**, select the Lunch Money account for your transactions.

   If your budget has an account with the name Apple Card, WalletFeed selects that account. The list then does not show **New Apple Card Account**.

   If your budget has no account with that name, WalletFeed selects **New Apple Card Account**. With **New Apple Card Account**, WalletFeed makes a credit account with the name Apple Card. Its balance is $0.00.

   The list does not show closed accounts or accounts that cannot have transactions.

6. Tap **Add**.

   Result: WalletFeed shows **Send Transactions to Lunch Money?** The message tells you the data that Lunch Money receives, the Wallet accounts and the start date. If you tap **Cancel**, WalletFeed removes the new destination and does not send transactions.

7. Tap **Send**.

   Result: WalletFeed starts to send your transactions to Lunch Money. In **Destinations**, the name of the new destination starts with "Lunch Money".

   ![The Destinations screen with Lunch Money and three other destinations.](app:07-destinations)

## Data that Lunch Money receives

Lunch Money shows the transactions from WalletFeed on the **TRANSACTIONS** page, below **FINANCES**.

![The Lunch Money Transactions page with six sample transactions from WalletFeed in the Apple Card account.](web:lunch-money/90-walletfeed-result)

WalletFeed adds each transaction to the Lunch Money account that you selected. This account also receives the transactions from your other Wallet accounts, for example Apple Cash. To select the Wallet accounts, refer to [Send only some transactions](#send-only-some-transactions).

| From Wallet | In Lunch Money |
| --- | --- |
| The date of the transaction, in the time zone of your iPhone | **DATE** |
| The merchant name, or the description if there is no merchant name | **PAYEE** |
| The card statement text | Original payee name |
| The amount | **AMOUNT** |
| The currency | Currency |
| The ID of the transaction in Wallet | External ID |
| The Wallet status, the transaction type, the merchant category code and the WalletFeed category | Custom metadata |

Lunch Money shows a purchase with a minus sign, for example -$7.75. It shows a refund in green, for example $49.00. A payment to your card also goes to Lunch Money as money in.

WalletFeed uses the external ID to find the transaction again when the transaction changes. Apps that use the Lunch Money API can read the custom metadata.

WalletFeed does not set the Lunch Money category. Lunch Money uses your rules on each new transaction. Thus, a rule can set the category. Lunch Money shows each new transaction as unreviewed.

After WalletFeed adds a transaction, WalletFeed does not change the payee, category, notes, tags or review status. When the date, amount, currency or Wallet status changes in Wallet, WalletFeed makes the same change in Lunch Money.

If you change the date or the amount of a transaction in Lunch Money, WalletFeed can put the data from Wallet back. This occurs when WalletFeed sends the transaction again, for example with **Send History**.

If WalletFeed makes the Apple Card account, the account starts with a balance of $0.00. When WalletFeed adds or changes a transaction, the balance of the account does not change. But when WalletFeed deletes a transaction, Lunch Money changes the balance by the amount of that transaction. To correct the balance, refer to [If the balance in Lunch Money is not correct](#if-the-balance-in-lunch-money-is-not-correct).

Your transactions go from your iPhone directly to Lunch Money. WalletFeed has no account and no WalletFeed servers. After Lunch Money receives your transactions, the terms of Lunch Money are applicable to them.

## New and changed transactions

While WalletFeed is open, Lunch Money receives changes in seconds. When WalletFeed is not open, iOS starts WalletFeed approximately 1 hour or less after a change in Wallet. If [Background Sync](/docs/background-sync/) is on in **Settings** › **Sync**, WalletFeed then sends the change.

Wallet shows a new charge as pending until the charge posts. Lunch Money does not show a pending status for transactions from WalletFeed. Thus, Lunch Money shows a pending charge as a usual transaction. WalletFeed sends the Wallet status in the custom metadata.

When the charge posts, WalletFeed uses the same transaction in Lunch Money. If the amount or the date changes, WalletFeed changes the transaction in Lunch Money. To send charges only after they post, you can set **Filter** to on and **Include Pending** to off (refer to [Send only some transactions](#send-only-some-transactions)).

Lunch Money receives a refund as a different transaction. If Wallet shows a charge as declined or expired, WalletFeed deletes the charge from Lunch Money. WalletFeed also deletes a transaction that Wallet removes. But WalletFeed does not delete a transaction that you divided or put in a group in Lunch Money.

## Send previous transactions

A new destination also receives previous transactions from the start date in **Settings** › **Sync** › **Initial History**. **Initial History** is **All** until you change it. If you change **Initial History** before you add Lunch Money, the new destination receives transactions from the new start date.

To send previous transactions after you add Lunch Money, do these steps:

1. In **Destinations**, tap the Lunch Money destination.

   ![The Lunch Money destination in WalletFeed with Replace Token, Filter, Send History, Send Test and Delete.](app:docs-destination-detail)

2. Tap **Send History**.
3. Tap **30 Days**, **90 Days**, **1 Year** or **All**.

   Result: WalletFeed shows **Sending History** and the number of transactions that it sent.

4. To stop WalletFeed before it sends all of the transactions, tap **Send History** › **Stop Sending**.

WalletFeed sends previous transactions to Lunch Money in groups of 50. It waits 45 seconds between groups. Lunch Money does not receive the same transaction two times. If you changed the date or the amount of a transaction in Lunch Money, **Send History** puts the data from Wallet back.

For more information, refer to [Send previous transactions](/docs/send-history/).

## Change or remove the destination

You change the Lunch Money destination on its screen in **Destinations**. For more information about this screen, refer to [Destinations](/docs/destinations/).

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

WalletFeed uses the filter only for the transactions that it sends after you set the filter. For more information, refer to [Filter the transactions for a destination](/docs/choose-what-to-send/).

### Stop the destination for a time

1. In **Destinations**, tap the Lunch Money destination.
2. Set **Enabled** to off.

   Until you set **Enabled** to on again, WalletFeed does not send transactions to Lunch Money.

### Replace the token

If you deleted the token in Lunch Money, or if Lunch Money does not accept the token, do these steps:

1. Make a new access token for the same budget (refer to [Step 2](#step-2-make-an-access-token-in-lunch-money)).

   If the new token is for a different budget, WalletFeed cannot get access to the account.

2. Open WalletFeed again.
3. In **Destinations**, tap the Lunch Money destination.
4. Tap **Replace Token**.
5. Touch and hold **Access Token**.
6. Tap **Paste**.
7. Tap **Replace**.

   Result: Before WalletFeed puts the new token in the Keychain, WalletFeed connects to Lunch Money with the token. Then **Replace Token** shows a green checkmark.

### Remove Lunch Money from WalletFeed

1. In **Destinations**, tap the Lunch Money destination.
2. Tap **Delete**.
3. Tap **Delete** again.

   Result: WalletFeed removes the destination and deletes the token from your iPhone. The transactions that WalletFeed sent stay in Lunch Money. Until you delete the token in Lunch Money, Lunch Money accepts the token.

### Delete the token in Lunch Money

1. On your iPhone, open [the Lunch Money Developers page](https://my.lunchmoney.app/developers).
2. If Lunch Money shows "Welcome back!", get access to your Lunch Money account with your e-mail address and your password.
3. If Lunch Money does not show the **Developers** page, tap **☰** › **DEVELOPERS**.
4. In **ACTIVE ACCESS TOKENS**, find the row for WalletFeed.

   Each row shows the label of the token and "Last activity". After WalletFeed uses the token, "Last activity" shows a date and a time.

   ![The list of active access tokens in Lunch Money, with the REVOKE button for WalletFeed highlighted.](web:lunch-money/11-active-token-revoke)

5. In the row for WalletFeed, tap **REVOKE**.

   Result: Lunch Money does not show a message before it deletes the token. Then Lunch Money shows "Successfully revoked token".

   ![On an iPhone, Lunch Money shows the message Successfully revoked token.](web:lunch-money/20-iphone-token-revoked)

After you delete the token, the Lunch Money destination in WalletFeed shows "Authentication failed" when WalletFeed tries to send transactions. To send transactions again, you must make a new token and [replace the token](#replace-the-token) in WalletFeed.

## If there is a problem

To make sure that WalletFeed can send transactions to Lunch Money, do these steps:

1. In **Destinations**, tap the Lunch Money destination.
2. Tap **Send Test**.

   Result: If Lunch Money receives the test transaction, WalletFeed shows a green checkmark.

> **Note:** **Send Test** adds a test transaction of $4.20 to the Lunch Money account. The payee of the test transaction is WalletFeed. If you tap **Send Test** again, WalletFeed does not add a second test transaction. You can delete the test transaction in Lunch Money.

### If WalletFeed shows "Token rejected (HTTP 401)"

Lunch Money does not accept the token, for example because you copied only a part of the token. WalletFeed then shows "Token rejected (HTTP 401). Request a new one in Lunch Money."

1. Make a new access token in Lunch Money (refer to [Step 2](#step-2-make-an-access-token-in-lunch-money)).
2. Open WalletFeed again.
3. Touch and hold **Access Token**.
4. Tap **Paste**.

### If the destination shows "Authentication failed"

Lunch Money does not accept the token of the destination, for example because a person deleted the token in Lunch Money.

1. Make a new access token in Lunch Money (refer to [Step 2](#step-2-make-an-access-token-in-lunch-money)).
2. Replace the token in WalletFeed (refer to [Replace the token](#replace-the-token)).

### If you did not copy the token

Lunch Money shows a token only one time.

1. In Lunch Money, open the **Developers** page again (refer to [Step 2](#step-2-make-an-access-token-in-lunch-money)).
2. In the row for the token that you did not copy, tap **REVOKE**.
3. Make a new access token (refer to [Step 2](#step-2-make-an-access-token-in-lunch-money)).

### If WalletFeed shows "The account is gone from Lunch Money" or "Rejected (HTTP 400)"

Lunch Money does not have the account for this destination, or the token is for a different budget. If you tap **Replace Token**, WalletFeed shows "The account is gone from Lunch Money. Add this destination again."

1. Remove the destination (refer to [Remove Lunch Money from WalletFeed](#remove-lunch-money-from-walletfeed)).
2. Add Lunch Money again (refer to [Step 1](#step-1-open-the-lunch-money-form-in-walletfeed)).

### If the transactions go to an incorrect budget

The token is for the budget that was open when you made the token.

1. Remove the destination (refer to [Remove Lunch Money from WalletFeed](#remove-lunch-money-from-walletfeed)).
2. Do [Step 1](#step-1-open-the-lunch-money-form-in-walletfeed), Step 2 and Step 3 again.

   In Step 2, tap the correct budget in **Switch Accounts** before you make the token.

The transactions in the incorrect budget stay there. You can delete them in Lunch Money.

### If Lunch Money does not receive new transactions

WalletFeed cannot send transactions to Lunch Money. For example, the destination is off, or **Background Sync** is off.

1. Open WalletFeed. While WalletFeed is open, it sends changes in seconds.
2. If **Destinations** shows **Sync Requires Pro**, tap **Upgrade**.
3. If the Lunch Money destination shows **Off**, set **Enabled** to on in the destination.
4. If **Filter** is on, make sure that the filter includes the new transactions.
5. Tap the gear icon at the top of **Destinations**.
6. Make sure that **Background Sync** is on.
7. Tap **Sync Now**.

After your iPhone starts again, WalletFeed cannot send transactions to destinations until you type your passcode one time.

### If the balance in Lunch Money is not correct

When WalletFeed deletes a transaction, Lunch Money changes the balance of the account. WalletFeed does not know the balance of your card.

1. On a computer, open [Lunch Money](https://my.lunchmoney.app) in a web browser.
2. Click **SETUP** at the top of the page.

   Result: Lunch Money shows **Accounts**.

3. Click the account that receives your transactions, for example **Apple Card**.

   ![The Lunch Money Accounts page, with the Apple Card credit account highlighted.](web:lunch-money/13-accounts-apple-card)

   Result: Lunch Money shows **Edit Account**.

4. In **CURRENT BALANCE**, type the correct balance.
5. Click **SAVE CHANGES**.

### If WalletFeed shows "Too many requests" or "Rejected (HTTP 429)"

Lunch Money accepts a maximum of 100 requests each minute.

1. Wait until WalletFeed tries again.

   Result: WalletFeed tries again at the time that it shows, or when it starts to send changes again.
