+++
title = "Send Apple Card transactions to Linear"
nav_title = "Linear"
seo_title = "Apple Card to Linear: an issue for each transaction"
description = "WalletFeed sends your Apple Card transactions from your iPhone to Linear. Each transaction becomes an issue in a Linear team."
group = "Sheets and databases"
order = 60
related = ["docs/choose-what-to-send", "docs/destinations"]
updated = 2026-10-30
+++

WalletFeed sends your Apple Card, Apple Cash and Savings transactions from your iPhone to Linear. In Linear, WalletFeed makes one issue for each transaction. You make a personal API key in Linear, and then you paste the key in WalletFeed.

## Before you start

You must have these items:

- An iPhone with iOS 26 or a newer version. WalletFeed is available only in the US.
- WalletFeed, with access to your [Wallet accounts](/docs/wallet-accounts/).
- [WalletFeed Pro](/docs/walletfeed-pro/), a subscription with a 1-week free trial, or a one-time Lifetime purchase. You must have WalletFeed Pro to send transactions to Linear.
- A Linear account, from [Linear's sign-up page](https://linear.app/signup). You can use the Free plan of Linear.

> **Note:** On Linear's Free plan, a workspace with more than 250 issues cannot get new issues. WalletFeed makes one issue for each transaction. With a filter, WalletFeed sends only some transactions (refer to [Step 3](#step-3-set-a-filter)).

## Your key stays on your iPhone

- WalletFeed keeps the API key in the Keychain on your iPhone. iOS encrypts the Keychain.
- The API key does not go to iCloud Keychain or to your other devices.
- WalletFeed has no account and no servers. No person at WalletFeed can see or get the API key.
- Your iPhone sends the API key only to Linear, in each request to Linear.
- When you delete the destination, WalletFeed deletes the API key from your iPhone. You can also revoke the key in Linear.

## Step 1: Make a personal API key in Linear

With a personal API key, WalletFeed can make issues in your Linear workspace.

1. On your iPhone, open [Linear's Security & Access settings](https://linear.app/settings/account/security).

   > **Note:** On the Linear screen in WalletFeed, **Security & Access** opens the same page.

2. If Linear shows its login page, get access to Linear with your e-mail address or your Google account. Linear does not use passwords.
3. If Linear shows **Verifying it’s you**, tap the **Verify you are human** checkbox.

   ![The Linear page with the heading Verifying it’s you and the Verify you are human checkbox.](web:linear/03-verify-human)

4. If you use your e-mail address, open the e-mail from Linear.
5. Tap the hyperlink in the e-mail, or type the code from the e-mail in Linear.
6. If Linear shows a different page after you get access, open [Linear's Security & Access settings](https://linear.app/settings/account/security) again.
7. On this page, find the API section.
8. In the API section, tap the button for a new personal API key.
9. If Linear shows a field for a name, type `WalletFeed`.
10. Give the key full access, or only **Read** and **Write** access. If you select only **Create issues**, WalletFeed cannot change or archive issues.
11. Optional: Give the key access to only the team that will receive the issues.
12. Tap the button that makes the key.
13. Copy the key. The key starts with `lin_api_`.
14. Keep the Linear page open until you paste the key in WalletFeed.

## Step 2: Add Linear in WalletFeed

1. Open WalletFeed.
2. Optional: If your workspace is on Linear's Free plan, set **Initial History** to **Today**. Then the new destination receives no previous transactions. **Settings** shows the **Sync** section only with WalletFeed Pro.
   1. Tap **Settings** (the gear button) at the top of the screen.
   2. In the **Sync** section, set **Initial History** to **Today**.

      ![WalletFeed Settings with the Sync section and Initial History set to All.](app:docs-settings)

   3. Tap **Done**.
3. Tap **Destinations**.
4. Tap **+** at the top of the screen.

   ![The Destinations screen in WalletFeed with the + button and no destinations.](app:docs-destinations-empty-pro)

5. In **Sheets & Databases**, tap **Linear**. You can also type `Linear` in the search field.
6. If WalletFeed shows the **WalletFeed Pro** screen, get WalletFeed Pro on that screen. Then the **Linear** screen opens.
7. Paste the key in the **API Key** field. WalletFeed keeps the key in the Keychain on your iPhone.

   ![The Linear screen in WalletFeed with the API Key field, three steps and the Security & Access hyperlink.](app:docs-setup-linear)

8. After WalletFeed reads the key, select a team in **Team**. This team receives the issues.
9. Optional: In **Project**, select a project. If you do not select a project, **Project** stays at **None**. A project must be in Linear before WalletFeed can show it.

   Below **Project**, WalletFeed shows "Each transaction becomes an issue to review."

10. Tap **Add**.
11. Read the message **Send Transactions to Linear?** The message gives the fields that Linear receives, the accounts and the start date.
12. Tap **Send**. If you tap **Cancel**, WalletFeed does not add the destination.

Then **Destinations** shows the new destination with the name of the team, for example “Linear · Finance”.

## Step 3: Set a filter

With a [filter](/docs/choose-what-to-send/), WalletFeed sends only some transactions to Linear. If your workspace is on Linear's Free plan, set a filter.

1. In **Destinations**, tap the Linear destination.
2. Set **Filter** to on.

   ![The destination screen for Lunch Money in WalletFeed, with the Filter switch set to off.](app:docs-destination-detail)

3. Optional: Set **Include** to **Purchases**. Then Linear receives no refunds or payments.
4. Optional: In **Minimum**, type an amount, for example `25`. Then Linear receives only transactions of $25 or more.
5. Optional: In **Accounts** or **Categories**, select only the accounts or the categories to send to Linear.
6. Optional: To send previous transactions with this filter, tap **Send History** (refer to [Send previous transactions](#send-previous-transactions)).

## Data that Linear receives

Your transactions go from your iPhone directly to Linear. WalletFeed has no account and no WalletFeed servers. After Linear receives your transactions, the terms of Linear are applicable to them.

WalletFeed puts each issue in the team that you selected. If you selected a project, WalletFeed also puts the issue in that project. If Triage is on for the team, a new issue goes to Triage. If Triage is off, the issue goes to the first Backlog status of the team.

The title of each issue has the amount and the merchant, for example `$6.75 · Blue Bottle Coffee`. The description of the issue is a table with these rows:

| Row in the description | Value from Wallet |
| --- | --- |
| **Date** | The date of the transaction, for example 2026-10-29 |
| **Merchant** | The merchant name, or the description if Wallet has no merchant name |
| **Amount** | Less than zero for a charge, for example -84.12, and more than zero for a refund or a payment |
| **Currency** | The currency code, for example USD |
| **Category** | The WalletFeed category, for example Groceries |
| **Status** | The Wallet status, for example `pending`, or `booked` after the charge posts |
| **Pending** | Yes or No |
| **Account** | The Wallet account, for example Apple Card |
| **Description** | The description from Wallet |
| **Type** | The type of transaction, for example `pointOfSale` or `refund` |
| **MCC** | The merchant category code, for example 5411 |
| **Foreign Amount** and **Foreign Currency** | The amount and the currency of a charge in a different currency |
| **WalletFeed ID** | The transaction ID, in the last row |

WalletFeed does not write a row that has no value. In the description, an amount has no zeros at the end, for example -23.4 for $23.40.

Each issue also has an attachment with the title WalletFeed. WalletFeed uses this attachment and the **WalletFeed ID** row to find the issue again in the team that you selected.

## New and changed transactions

While WalletFeed is open, Linear receives changes in seconds. When WalletFeed is not open, iOS starts WalletFeed approximately 1 hour or less after a change in Wallet. If [Background Sync](/docs/background-sync/) is on in **Settings** › **Sync**, WalletFeed then sends the change.

**Background Sync** is in **Settings** › **Sync**. It stays on until you set it to off. After your iPhone starts again, WalletFeed sends nothing to Linear until you type your iPhone passcode one time.

A pending charge becomes an issue with `· Pending` at the end of the title. When the charge posts, WalletFeed changes the title and the description of the same issue.

A refund and its charge become two different issues. The title of a refund or a payment has + before the amount, for example `+$49.00 · Apple Store`.

If a pending charge becomes a declined charge, or if Wallet removes a transaction, WalletFeed archives the issue. The archived issue stays in Linear.

### Changes that you make in Linear

When a transaction changes, WalletFeed writes the title and the description of its issue again. If you changed them in Linear, WalletFeed replaces your changes. WalletFeed does not change the status or the assignee of the issue.

## Send previous transactions

A new Linear destination also receives previous transactions from the start date in **Settings** › **Sync** › **Initial History**. **Initial History** is **All** until you change it. But a new Linear destination receives a maximum of 30 days of previous transactions.

To send transactions from a longer period, use [Send History](/docs/send-history/):

1. In **Destinations**, tap the Linear destination.
2. If your workspace is on Linear's Free plan, set a filter (refer to [Step 3](#step-3-set-a-filter)). Each previous transaction becomes one issue.
3. Tap **Send History**.
4. Select a period: **30 Days**, **90 Days**, **1 Year** or **All**.
5. Read the message **Send History to Linear?** The message shows “Each transaction can become an issue.”
6. Tap **Send**.

WalletFeed sends the newest transactions first. The destination screen shows the number of transactions that WalletFeed sent. **Send History** also uses the filter.

To stop **Send History**:

1. On the destination screen, tap **Send History**.
2. Tap **Stop Sending**. The issues that WalletFeed sent stay in Linear.

## Change or remove the destination

To change the transactions that go to Linear, change the filter on the destination screen.

The destination screen shows the **Team**, and the **Project** if you selected a project. You cannot change them. To use a different team or a different project:

1. Add Linear again with the new team or the new project (refer to [Step 2](#step-2-add-linear-in-walletfeed)).
2. Delete the previous Linear destination.

To stop the destination temporarily, set **Enabled** to off.

To replace the key, for example after you revoke it in Linear:

1. In Linear, make a new personal API key (refer to [Step 1](#step-1-make-a-personal-api-key-in-linear)).
2. In WalletFeed, tap the Linear destination in **Destinations**.
3. Tap **Replace Key**.
4. Paste the new key in the **API Key** field.
5. Tap **Replace**. Before WalletFeed keeps the new key, it makes sure that the key can get access to the team.

To delete the destination:

1. In WalletFeed, tap the Linear destination in **Destinations**.
2. Tap **Delete**.
3. In the message, tap **Delete**. The issues that WalletFeed sent stay in Linear.
4. Optional: Revoke the key in [Linear's Security & Access settings](https://linear.app/settings/account/security).

## If there is a problem

### If WalletFeed shows “Key rejected”

Linear did not accept the key because the key is not correct, or because a person revoked the key in Linear.

1. In Linear, make a new personal API key (refer to [Step 1](#step-1-make-a-personal-api-key-in-linear)).
2. If WalletFeed shows the message on the Linear screen, paste the new key in the **API Key** field.
3. If WalletFeed shows the message on the destination screen, replace the key (refer to [Change or remove the destination](#change-or-remove-the-destination)).

### If the destination shows “Authentication failed”

Linear did not accept the key, or the key cannot make or change issues in the team.

1. In Linear, make a new personal API key with full access, or with **Read** and **Write** access.
2. In WalletFeed, tap the Linear destination in **Destinations**.
3. Tap **Replace Key**.
4. Paste the new key in the **API Key** field.
5. Tap **Replace**.

### If WalletFeed shows “Give the key Read and Write access to the team”

Linear does not let the key get access to the team.

1. In Linear, make a new personal API key with full access, or with **Read** and **Write** access.
2. If you give the key access to only some teams, include the team that you use with WalletFeed.
3. If WalletFeed shows the message on the Linear screen, paste the new key in the **API Key** field.
4. If WalletFeed shows the message on the destination screen, replace the key (refer to [Change or remove the destination](#change-or-remove-the-destination)).

### If WalletFeed shows “This key can't see any teams”

The key has access to no team in Linear.

1. In Linear, make a new personal API key with access to your team.
2. On the Linear screen in WalletFeed, paste the new key in the **API Key** field.

### If WalletFeed shows “Linear is limiting requests”

Linear has a limit for each user in each hour, and your account is at that limit.

1. Wait for 1 minute.
2. If WalletFeed shows the message on the Linear screen, tap **Try Again**.
3. If WalletFeed shows the message on the destination screen, replace the key again (refer to [Change or remove the destination](#change-or-remove-the-destination)).

### If new transactions do not become issues

On Linear's Free plan, a workspace with more than 250 issues cannot get new issues.

1. To send all your transactions to Linear, change your workspace to a different Linear plan, for example Basic. Basic has no limit on issues.
2. To send only some transactions, set a filter (refer to [Step 3](#step-3-set-a-filter)).

### If one transaction has two issues

If a person removes the **WalletFeed ID** row and the WalletFeed attachment, or moves the issue to a different team, WalletFeed makes a new issue.

1. In Linear, archive or delete the issue that has no **WalletFeed ID** row, or the issue in the different team. WalletFeed continues to change the other issue.
2. Keep the **WalletFeed ID** row and the WalletFeed attachment in each issue.

### If Linear receives changes only when WalletFeed is open

**Background Sync** is off, or your iPhone started again and you did not type its passcode.

1. In WalletFeed, tap **Settings** (the gear button) at the top of the screen.
2. In the **Sync** section, set **Background Sync** to on.
3. Tap **Done**.
4. After your iPhone starts again, type its passcode one time.

### If Linear does not let you make an API key

An admin of your Linear workspace does not let members make API keys. Admins can always make API keys. On the Free plan, all users are admins.

1. Tell an admin of the workspace to change **Member API keys** in **Settings** › **Administration** › **API**.
2. After the admin changes **Member API keys**, make the key (refer to [Step 1](#step-1-make-a-personal-api-key-in-linear)).
