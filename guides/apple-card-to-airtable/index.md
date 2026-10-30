# Send Apple Card transactions to Airtable

WalletFeed sends your Apple Card, Apple Cash and Savings transactions from your iPhone to a table in Airtable. You make a personal access token in Airtable. Then you paste the token in WalletFeed.

## Before you start

You must have these items:

- An iPhone with iOS 26 or a newer version. WalletFeed is available only in the US.
- WalletFeed, with access to your Wallet accounts. Refer to [First steps with WalletFeed](/docs/get-started/).
- [WalletFeed Pro](/docs/walletfeed-pro/). Destinations are part of WalletFeed Pro. WalletFeed Pro is a subscription with a 1-week free trial, or a one-time Lifetime purchase.
- An Airtable account. You can make an account at [airtable.com](https://airtable.com/signup).
- A web browser for the Airtable steps. The screenshots show Airtable on a computer.

> **Note:** A new Airtable account starts with a 14-day trial of the Team plan. On the Airtable Free plan, the maximum number of records in a base is 1,000. For each workspace on this plan, the maximum number of API calls is 1,000 each month.

## Step 1: Make a base in Airtable

A base is an Airtable database. If you have a base for your transactions, go to [Step 2](#step-2-make-a-personal-access-token-in-airtable).

1. On your computer, get access to your [Airtable](https://airtable.com) account.
2. On **Home**, click **+ Create** at the bottom of the sidebar.

   ![The Airtable Home page with the Create button at the bottom of the sidebar.](https://walletfeed.app/guides/apple-card-to-airtable/airtable-home-create.webp)

3. Click **Build an app on your own**.

   ![The dialog "How do you want to start?" with the highlighted card "Build an app on your own".](https://walletfeed.app/guides/apple-card-to-airtable/airtable-build-on-your-own.webp)

   Airtable opens a new base with the name **Untitled Base**. In this dialog, Airtable uses "app" for a base. On the base and in the token form, Airtable uses "base".
4. If Airtable shows a message with a **Skip** or **Dismiss** button, click the button.
5. Click **Untitled Base**, at the top of the page.

   ![A new Airtable base with the highlighted name Untitled Base at the top.](https://walletfeed.app/guides/apple-card-to-airtable/airtable-new-base.webp)

6. In the **Base name** box, delete **Untitled Base**.
7. Type a name for the base, for example `WalletFeed`.

   ![The Airtable base panel with WalletFeed Docs as the new base name.](https://walletfeed.app/guides/apple-card-to-airtable/airtable-rename-base.webp)

8. Press **Return** or **Enter**.
9. Click outside the panel.

> **Note:** A new base can show an Omni panel on the left side. The **«** button closes the Omni panel.

> **Note:** The new base also has a table with the name **Table 1**. WalletFeed does not change this table.

## Step 2: Make a personal access token in Airtable

1. On your computer, open [Airtable](https://airtable.com).
2. On **Home**, click your account picture in the top-right corner.
3. Click **Builder hub**.

   ![The Airtable account menu with the highlighted Builder hub item.](https://walletfeed.app/guides/apple-card-to-airtable/airtable-account-menu.webp)

   Airtable opens **Builder hub** in a new browser tab, on the **Personal access tokens** page.
4. Click **Create token**.

   ![The Personal access tokens page with the highlighted Create token button.](https://walletfeed.app/guides/apple-card-to-airtable/airtable-personal-access-tokens.webp)

5. In **Name**, type `WalletFeed`.

   ![The new token form with WalletFeed in the Name box.](https://walletfeed.app/guides/apple-card-to-airtable/airtable-token-name.webp)

   Airtable shows this name in the revision history of the records that WalletFeed writes. The form also tells you not to give the token to third-party apps. Refer to [The Airtable text about third-party apps](#the-airtable-text-about-third-party-apps).
6. Below **Scopes**, click **+ Add a scope**.
7. In **Find a scope**, type `data.records`.
8. Select `data.records:read` and `data.records:write`.

   ![The scope list for data.records with the selected read and write scopes.](https://walletfeed.app/guides/apple-card-to-airtable/airtable-scopes-records.webp)

9. In **Find a scope**, replace the text with `schema.bases`.
10. Select `schema.bases:read` and `schema.bases:write`.

    ![The scope list for schema.bases with the selected read and write scopes.](https://walletfeed.app/guides/apple-card-to-airtable/airtable-scopes-schema.webp)

11. To close the list, press **Esc**.
12. Make sure that the form shows the four scopes below **Scopes**.
13. Below **Access**, click **+ Add a base**.

    ![The token form with the four scopes and the highlighted Add a base link.](https://walletfeed.app/guides/apple-card-to-airtable/airtable-scopes-added.webp)

14. Click your base, below the name of its workspace.

    ![The base list with the highlighted WalletFeed Docs base.](https://walletfeed.app/guides/apple-card-to-airtable/airtable-add-base.webp)

    The token has access only to this base. If you click **All current and future bases in this workspace**, the token gets access to all the bases in the workspace.
15. Click **Create token**.

    ![The completed token form with the highlighted Create token button.](https://walletfeed.app/guides/apple-card-to-airtable/airtable-create-token.webp)

16. In the **Your token has been created** dialog, click the clipboard button on the right side of the token.

    ![The dialog "Your token has been created" with the highlighted clipboard button.](https://walletfeed.app/guides/apple-card-to-airtable/airtable-token-created.webp)

    Airtable shows the token only one time. You cannot click **Done** until you copy the token.
17. Click **Done**.
18. Until you paste the token in [Step 3](#step-3-add-airtable-in-walletfeed), do not copy different text.

> **Note:** If you use a Mac with the same Apple Account as your iPhone, you can paste the token on the iPhone with [Universal Clipboard](https://support.apple.com/en-us/102430).

### The Airtable text about third-party apps

In the token form and in the token dialog, Airtable shows the text "Only use this token for your own development. Don't share it with third-party services and applications." WalletFeed is a third-party app. These items give information about the token in WalletFeed:

- WalletFeed keeps the token in the Keychain on your iPhone. The token does not go to iCloud Keychain.
- WalletFeed sends the token only in requests to the Airtable API. WalletFeed has no account and no WalletFeed servers. Your transactions go from your iPhone directly to Airtable.
- The token has access only to the base or the workspace that you added in [Step 2](#step-2-make-a-personal-access-token-in-airtable). The token can do only the tasks that its four scopes let it do.
- If you delete the token in Airtable, WalletFeed has no access to your base. Refer to [Change or remove the destination](#change-or-remove-the-destination).

## Step 3: Add Airtable in WalletFeed

1. On your iPhone, open WalletFeed.
2. Tap **Destinations**.
3. Tap **+** at the top of the screen.

   ![The empty Destinations screen with the + button at the top.](https://walletfeed.app/guides/apple-card-to-airtable/walletfeed-destinations-empty-pro.webp)

4. Tap **Airtable**, in **Sheets & Databases**.

   ![The Add Destination list with Airtable in the Sheets & Databases group.](https://walletfeed.app/guides/apple-card-to-airtable/walletfeed-add-destination.webp)

   If you do not have WalletFeed Pro, WalletFeed shows the **WalletFeed Pro** screen first.
5. Tap **Personal Access Token**.

   ![The Airtable screen in WalletFeed with the Personal Access Token field and the steps for Airtable.](https://walletfeed.app/guides/apple-card-to-airtable/walletfeed-setup-airtable.webp)

6. Paste the token.

   The form then shows **Base** and **Table**. **Base** shows the bases that the token can change.
7. In **Base**, select your base.
8. Do not change **Table**.

   **Table** shows **New Table**, and the form shows "Adds a WalletFeed Transactions table to the base." If the base has a **WalletFeed Transactions** table from a previous destination, **Table** shows that table.
9. Tap **Add**.

   The message **Send Transactions to Airtable?** gives the data that Airtable will receive, the accounts and the start date.
10. Tap **Send**.

    If you tap **Cancel**, WalletFeed sends nothing and removes the destination.

The new destination is in **Destinations**. Its name has two parts, for example **Airtable · WalletFeed**. The second part is the name of your base. WalletFeed starts to send your transactions.

## Step 4: Look at your transactions in Airtable

1. On your computer, open your base in Airtable.
2. Click the **WalletFeed Transactions** tab.

   ![The WalletFeed Transactions table in Airtable with six sample transactions.](https://walletfeed.app/guides/apple-card-to-airtable/airtable-walletfeed-result.webp)

3. Move the pointer to the row of a transaction.
4. In the row, click the expand icon.

   ![The record of one transaction with its fields and a checkmark in the Pending box.](https://walletfeed.app/guides/apple-card-to-airtable/airtable-result-record.webp)

   Airtable shows all the fields of the transaction.

To add a test record, do these steps on your iPhone:

1. In WalletFeed, tap **Destinations**.
2. Tap your Airtable destination.
3. Tap **Send Test**.

   The table gets a test record with WalletFeed in **Merchant** and -4.20 in **Amount**. You can delete this record in Airtable.

## Fields in Airtable

Each transaction is one record in the **WalletFeed Transactions** table. WalletFeed makes these fields:

| Airtable field | Data |
| --- | --- |
| **WalletFeed ID** | The ID of the transaction in Wallet. WalletFeed uses it to find and change the same record. |
| **Date** | The date of the transaction in your time zone, for example 2026-10-30. |
| **Merchant** | The name of the merchant. If Wallet has no merchant name, this field contains the description. |
| **Amount** | A number with two decimal places. A purchase or a fee is less than zero, and a refund or a payment is more than zero. |
| **Currency** | The currency code, for example `USD`. |
| **Category** | The WalletFeed category, for example Groceries or Fuel. |
| **Status** | The status in Wallet, for example `pending` or `booked`. |
| **Pending** | A checkbox. WalletFeed selects it while the status is `pending` or `authorized`. |
| **Account** | The name of the Wallet account, for example Apple Card. |
| **Description** | The description from Wallet. |
| **Type** | The type of transaction in Wallet, for example `pointOfSale` or `refund`. |
| **MCC** | The merchant category code, as a number. If Wallet has no code, this field is empty. |
| **Foreign Amount** | The value in the currency of the merchant, with the same sign as **Amount**. This field is empty for a purchase in US dollars. |
| **Foreign Currency** | The currency code of the merchant. This field is empty for a purchase in US dollars. |

WalletFeed does not change the fields that you add to the table. If you change a WalletFeed field in a record, WalletFeed replaces your change when that transaction changes again.

When you add Airtable in WalletFeed, you can select a different table in **Table**. The list in **Table** shows only the tables that have a field with the name **WalletFeed ID**. WalletFeed writes only to the WalletFeed fields that the table has. If you add a WalletFeed field to the table, WalletFeed writes to it after you tap **Send Test**.

## New and changed transactions

WalletFeed sends each change in Wallet to Airtable:

- While WalletFeed is open, Airtable receives changes in seconds.
- When WalletFeed is not open, iOS starts WalletFeed approximately 1 hour or less after a change in Wallet. If [Background Sync](/docs/background-sync/) is on in **Settings** › **Sync**, WalletFeed then sends the change. **Background Sync** is on until you set it to off.
- When your iPhone starts again, WalletFeed cannot send changes until you type your iPhone passcode.

When a transaction changes in Wallet, WalletFeed changes the table:

- WalletFeed adds a pending charge as a record and selects the **Pending** checkbox. When the status of the charge changes to `booked`, WalletFeed changes the same record and clears the checkbox.
- A refund is a new record, and its **Amount** is more than zero.
- If the status of a pending charge changes to `rejected`, WalletFeed removes the record of the charge. Wallet gives this status to a declined or expired charge.
- If Wallet removes a transaction, WalletFeed also removes its record.

## Send previous transactions

A new destination also receives previous transactions from the start date in **Settings** › **Sync** › **Initial History**. **Initial History** is **All** until you change it.

To send previous transactions after you add the destination, do these steps:

1. In WalletFeed, tap **Destinations**.
2. Tap your Airtable destination.
3. Tap **Send History**.
4. Select **30 Days**, **90 Days**, **1 Year** or **All**.

To stop WalletFeed while it sends these transactions, tap **Send History** › **Stop Sending**. For more information, refer to [Send previous transactions](/docs/send-history/).

On the Airtable Free plan, you can decrease the number of records in the base. To do this, set **Initial History** to a shorter period before you add Airtable.

## Change or remove the destination

To open the destination, tap **Destinations** in WalletFeed. Then tap your Airtable destination. On the destination screen, you can make these changes:

- To send only some transactions, set **Filter** to on. You can set **Include**, **Minimum**, **Include Pending**, **Accounts**, **Categories** and **Exclude**. Refer to [Choose what a destination receives](/docs/choose-what-to-send/).
- To stop the destination for a period, set **Enabled** to off.
- To use a new token, tap **Replace Token**. Paste the new token. Then tap **Replace**. WalletFeed keeps the new token only if the new token lets WalletFeed read the table.
- To remove the destination, tap **Delete**. Then tap **Delete** again. WalletFeed removes the destination and its token from your iPhone.

If you remove the destination, the records that WalletFeed sent stay in Airtable. The terms of Airtable are applicable to these records.

To delete the token in Airtable, do these steps on your computer:

1. On **Home** in Airtable, click your account picture in the top-right corner.
2. Click **Builder hub**.

   Airtable opens the **Personal access tokens** page.
3. In the row of the token, click **…**.

   ![The token list with the WalletFeed token and its highlighted menu button.](https://walletfeed.app/guides/apple-card-to-airtable/airtable-token-list.webp)

4. Click **Delete token**.

   ![The token menu with the highlighted Delete token item.](https://walletfeed.app/guides/apple-card-to-airtable/airtable-token-menu.webp)

5. Click **Delete**.

   ![The dialog "Are you sure you want to delete this token?" with the highlighted Delete button.](https://walletfeed.app/guides/apple-card-to-airtable/airtable-delete-token.webp)

   After this step, Airtable does not accept the token from WalletFeed.

## If there is a problem

### If you cannot click Done in the token dialog

Airtable does not let you click **Done** until you copy the token.

1. Click the clipboard button on the right side of the token.
2. Click **Done**.

### If you closed the token dialog before you copied the token

Airtable shows a token only one time. The **Token ID** in the token list is not the token.

1. Delete the token that you cannot use, with the procedure in [Change or remove the destination](#change-or-remove-the-destination).
2. Make a new token with the procedure in [Step 2](#step-2-make-a-personal-access-token-in-airtable).

### If WalletFeed shows "Token rejected (HTTP 401). Check it and try again."

Airtable did not accept the token.

1. Make sure that you pasted the full token from the **Your token has been created** dialog.
2. If you do not have the full token, make a new token with the procedure in [Step 2](#step-2-make-a-personal-access-token-in-airtable).
3. In WalletFeed, delete the text in **Personal Access Token**.
4. Paste the token.

### If WalletFeed shows "The token has no base you can edit. Add one to the token."

The token has no base, or you cannot change the bases that the token has.

1. In Airtable, make a new token with the procedure in [Step 2](#step-2-make-a-personal-access-token-in-airtable).
2. In WalletFeed, delete the text in **Personal Access Token**.
3. Paste the new token.

### If WalletFeed shows "The token can't reach this base. Add the base and every scope to it."

The token does not have the base or one of the four scopes. If you tap **Add** without the Creator permission for the base, WalletFeed can also show this message. WalletFeed can add the **WalletFeed Transactions** table only if you have this permission.

1. If you do not have the Creator permission for the base, make a base with the procedure in [Step 1](#step-1-make-a-base-in-airtable).
2. In Airtable, make a new token with the procedure in [Step 2](#step-2-make-a-personal-access-token-in-airtable).
3. In WalletFeed, delete the text in **Personal Access Token**.
4. Paste the new token.

### If WalletFeed shows "Airtable is limiting requests. Try again in 30 seconds."

Airtable accepts not more than five requests each second for one base. If a base gets more than five requests in one second, Airtable rejects requests for 30 seconds.

1. After 30 seconds, do the last step again in WalletFeed.

### If Destinations shows "Authentication failed"

Airtable does not accept the token. This occurs if you deleted the token, or if the token does not have the base or a scope.

![The Destinations list with Authentication failed below the name of a destination.](https://walletfeed.app/guides/apple-card-to-airtable/walletfeed-destinations-failure.webp)

1. In Airtable, make a new token with the procedure in [Step 2](#step-2-make-a-personal-access-token-in-airtable).
2. In WalletFeed, tap the destination.
3. Tap **Replace Token**.
4. Paste the new token.
5. Tap **Replace**.

### If some transactions are not in the table

The cause can be a filter or the start date in **Initial History**.

1. In WalletFeed, tap **Destinations**.
2. Tap your Airtable destination.
3. Make sure that **Filter** is off, or that the filter includes these transactions.
4. To send previous transactions, tap **Send History**.
5. Select a period.
