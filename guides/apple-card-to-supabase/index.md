# Send Apple Card transactions to Supabase

WalletFeed sends your Apple Card, Apple Cash and Savings transactions from your iPhone to a Postgres database in your Supabase project. You copy the project URL and the publishable key from Supabase to WalletFeed, and then you paste the SQL from WalletFeed in the Supabase **SQL Editor**.

## Before you start

You must have:

- An iPhone with iOS 26 or a newer version
- WalletFeed, with access to your [Wallet accounts](/docs/wallet-accounts/)
- [WalletFeed Pro](/docs/walletfeed-pro/), a subscription with a 1-week free trial, or a one-time Lifetime purchase
- A Supabase account, or an e-mail address for a new account
- A web browser on a computer or on your iPhone.

WalletFeed is available only in the US.

## Step 1: Make a Supabase project

1. If you have a Supabase project for your transactions, go to [Step 2](#step-2-find-the-project-url-and-the-publishable-key).
2. On your computer, open the [Supabase sign-up page](https://supabase.com/dashboard/sign-up) in a web browser.
3. Type your e-mail address in the **Email** field.
4. Type a password in the **Password** field.
5. Click **Sign up**.

   ![The Supabase sign-up page, with the Sign up button highlighted below the Email and Password fields.](https://walletfeed.app/guides/apple-card-to-supabase/supabase-sign-up.webp)
6. If Supabase sends you an e-mail, open the hyperlink in the e-mail.
7. In the [Supabase dashboard](https://supabase.com/dashboard), make a new project.
8. Complete the form for the new project.
9. Wait until the new database starts.

> **Note:** You can also make the Supabase account with **Continue with GitHub** on the sign-up page.

> **Note:** WalletFeed does not use the database password. From Supabase, WalletFeed uses only the project URL and the publishable key.

## Step 2: Find the project URL and the publishable key

1. In your Supabase project, open the [**Connect** dialog](https://supabase.com/dashboard/project/_?showConnect=true).
2. Find the project URL. The URL starts with `https://` and has `.supabase.co` at the end.
3. If your project has no publishable key, make a publishable key in **Settings** › **API Keys**.
4. Find the publishable key. The key starts with `sb_publishable_`.
5. If Supabase is open on your computer, send the URL and the key to your iPhone (for example, with AirDrop).

> **Note:** WalletFeed does not accept a secret key (a key that starts with `sb_secret_`). With a secret key, Supabase ignores the policies for Row Level Security in your project.

> **Note:** With [Universal Clipboard](https://support.apple.com/en-us/102430), you can copy the URL and the key on a Mac and paste them on your iPhone.

## Step 3: Add Supabase in WalletFeed

1. On your iPhone, open WalletFeed.
2. Tap **Destinations**.
3. Tap **+** at the top of the screen.

   ![The Destinations screen with no destinations, and the + button at the top.](https://walletfeed.app/guides/apple-card-to-supabase/walletfeed-destinations-empty-pro.webp)
4. In the **Sheets & Databases** section, tap **Supabase**.

   ![The Add Destination list, with the Budgeting section, and Google Sheets, Airtable, Notion and Coda in the Sheets & Databases section.](https://walletfeed.app/guides/apple-card-to-supabase/walletfeed-add-destination.webp)
5. If WalletFeed shows the **WalletFeed Pro** screen, get WalletFeed Pro. Then the Supabase form opens.
6. Copy the publishable key.
7. Paste the key in the **Publishable Key** field.

   ![The Supabase form in WalletFeed, with the Publishable Key field, the project URL field, Share SQL and three steps for Supabase.](https://walletfeed.app/guides/apple-card-to-supabase/walletfeed-setup-supabase.webp)
8. Copy the project URL.
9. Paste the URL in the field below the key. The field shows `https://abcd.supabase.co` until you paste the URL.

> **Note:** WalletFeed keeps the key in the Keychain on your iPhone. WalletFeed has no account and no WalletFeed servers.

## Step 4: Make the table in Supabase

The SQL from WalletFeed makes the `walletfeed_transactions` table in your project. Supabase tells you that the publishable key is [safe to show in an app](https://supabase.com/docs/guides/api/api-keys). Thus, the SQL also adds a policy that lets only this WalletFeed destination read the table and write to it. A person with only the publishable key cannot read your transactions.

1. In WalletFeed, tap **Share SQL**. iOS opens a menu with **Copy**.
2. If Supabase is open on your computer, send the SQL to your computer (for example, with AirDrop).
3. If Supabase is open on your iPhone, tap **Copy** in the menu.
4. In your Supabase project, open the **SQL Editor**.
5. Paste the SQL in the editor.
6. Click **Run**.

## Step 5: Start to send transactions

1. On your iPhone, open WalletFeed again.
2. Tap **Add**. WalletFeed reads one row of the table to make sure that the URL, the key and the SQL are correct.
3. If WalletFeed shows an error below **Share SQL**, refer to [If there is a problem](#if-there-is-a-problem).
4. Read the message **Send Transactions to Supabase?** It tells you the data that Supabase will receive and the accounts.
5. Tap **Send**. WalletFeed adds the destination and starts to send your transactions.
6. In Supabase, open the **Table Editor**.
7. Select the `walletfeed_transactions` table. Each transaction is one row.

> **Note:** If **Initial History** is not **All**, the message in step 4 also gives the start date. If you tap **Cancel** in the message, WalletFeed does not add the destination. The Supabase form stays open.

## Columns in the Supabase table

Each transaction is one row in the `public.walletfeed_transactions` table. WalletFeed writes these values:

| Column | Postgres type | Value |
| --- | --- | --- |
| `id` | `text` | The WalletFeed ID of the transaction. This column is the primary key. |
| `date` | `date` | The day of the transaction, in the time zone of your iPhone. |
| `merchant` | `text` | The merchant name, or the description if Wallet has no merchant name. |
| `amount` | `numeric` | The value of the transaction. Purchases and fees have a value less than 0. Payments and refunds have a value more than 0. |
| `currency` | `text` | The currency code, for example `USD`. |
| `category` | `text` | The WalletFeed category, for example Groceries or Travel. |
| `status` | `text` | The status in Wallet, for example `pending`, `authorized` or `booked`. |
| `pending` | `boolean` | `true` when the status is `pending` or `authorized`, and `false` for a different status. |
| `account` | `text` | The account name, for example Apple Card. |
| `description` | `text` | The description of the transaction in Wallet. |
| `type` | `text` | The transaction type in Wallet, for example `pointOfSale` or `refund`. |
| `mcc` | `integer` | The merchant category code. |
| `foreign_amount` | `numeric` | For a purchase in a different currency, the value in that currency, with the same sign as `amount`. |
| `foreign_currency` | `text` | The code of that different currency. |

For a purchase in dollars, `foreign_amount` and `foreign_currency` have no value (`null`). When a transaction changes, WalletFeed updates the row that has the same `id`.

Your transactions go from your iPhone directly to your Supabase project. WalletFeed has no account and no WalletFeed servers. After Supabase receives your transactions, the terms of Supabase are applicable to them.

## New and changed transactions

While WalletFeed is open, Supabase receives changes in seconds. When WalletFeed is not open, iOS starts WalletFeed approximately 1 hour or less after a change in Wallet. If [Background Sync](/docs/background-sync/) is on in **Settings** › **Sync**, WalletFeed then sends the change. **Background Sync** is on until you set it to off.

A pending charge has the value `true` in `pending`. When its status changes to `booked`, WalletFeed updates the same row. WalletFeed deletes the row of a declined or expired charge, and the row of a transaction that Wallet removes.

WalletFeed writes a refund in a new row. The refund has a value more than 0 in `amount`.

## Send previous transactions

A new destination also receives previous transactions from the start date in **Settings** › **Sync** › **Initial History**. **Initial History** is **All** until you change it.

To send transactions from a different start date, use [Send History](/docs/send-history/):

1. In WalletFeed, tap **Destinations**.
2. Tap the Supabase destination. Its name starts with **Supabase ·**.
3. Tap **Send History**.
4. Tap **30 Days**, **90 Days**, **1 Year** or **All**.

Supabase keeps one row for each transaction.

To stop Send History:

1. Tap **Send History**.
2. Tap **Stop Sending**.

## Change or remove the destination

1. In WalletFeed, tap **Destinations**.
2. Tap the Supabase destination.

   ![The screen of a Lunch Money destination, with Name, Enabled, Last Sync, Replace Token, Filter, Send History, Send Test and Delete.](https://walletfeed.app/guides/apple-card-to-supabase/walletfeed-destination-detail.webp)

The screen of a Supabase destination has the same controls. It also has **Project**, **Share SQL** and **Replace Key**, but not **Replace Token**.

To send only some transactions:

1. Set **Filter** to on.
2. Select the transactions with **Accounts**, **Categories**, **Minimum** and the other controls.

[Choose what to send](/docs/choose-what-to-send/) tells you about each control of the filter.

To stop the destination and keep it, set **Enabled** to off.

To use a different publishable key:

1. Tap **Replace Key**.
2. Paste the new key in the **Publishable Key** field.
3. Tap **Replace**. WalletFeed keeps the new key only if WalletFeed can read the table with it.

In the destination, **Share SQL** gives the SQL with the token of this destination. Thus, you can use this SQL in the **SQL Editor** again. This SQL keeps the rows in the table. If the table does not have the `foreign_amount` and `foreign_currency` columns, the SQL adds them.

To remove the destination:

1. Tap **Delete**.
2. Tap **Delete** again.

The rows that WalletFeed sent stay in your Supabase table. You can delete these rows or the table in Supabase.

## If there is a problem

### If you cannot tap Add

WalletFeed lets you tap **Add** only when the form has a key and a correct project URL. If the key is a secret key, you cannot tap **Add**, and WalletFeed shows "Use the publishable key. Secret keys skip the table's policy."

1. Copy the publishable key from the **Connect** dialog again. The key starts with `sb_publishable_`.
2. In WalletFeed, clear the **Publishable Key** field.
3. Paste the key in the **Publishable Key** field.
4. Copy the project URL from the **Connect** dialog again.
5. In WalletFeed, clear the field below the key.
6. Paste the URL in the field below the key.

### If WalletFeed shows "Key rejected. Copy the publishable key again."

Supabase did not accept the key, or the SQL that you used came from a different Supabase form. Each time you open the Supabase form, WalletFeed makes new SQL with a new token.

1. Copy the publishable key from the **Connect** dialog again.
2. In WalletFeed, clear the **Publishable Key** field.
3. Paste the key in the **Publishable Key** field.
4. Tap **Share SQL**.
5. Tap **Copy**, or send the SQL to your computer (for example, with AirDrop).
6. In Supabase, paste the new SQL in the **SQL Editor**.
7. Click **Run**.
8. In WalletFeed, tap **Add**.

### If WalletFeed shows "Table not found. Run the SQL, then try again."

The project has no `walletfeed_transactions` table. For example, you did not click **Run**, or you used the **SQL Editor** of a different project.

1. In Supabase, open the project that has the URL from Step 2.
2. Open the **SQL Editor**.
3. In WalletFeed, tap **Share SQL**.
4. Tap **Copy**, or send the SQL to your computer (for example, with AirDrop).
5. In Supabase, paste the SQL in the **SQL Editor**.
6. Click **Run**.
7. In WalletFeed, tap **Add**.

### If the destination shows "Authentication failed" or "Rejected (HTTP 404)"

Supabase did not accept the key or the token, or the table is not in the project. For example, SQL from a different WalletFeed destination replaced the token in the policy of the table.

1. In WalletFeed, tap **Destinations**.

   ![The Destinations list, with an n8n destination that shows Authentication failed.](https://walletfeed.app/guides/apple-card-to-supabase/walletfeed-destinations-failure.webp)
2. Tap the Supabase destination.
3. Tap **Share SQL**.
4. Tap **Copy**, or send the SQL to your computer (for example, with AirDrop).
5. In Supabase, paste the SQL in the **SQL Editor**.
6. Click **Run**.
7. In WalletFeed, tap **Send Test**.

If **Send Test** shows an error, replace the key:

1. Copy the publishable key from the **Connect** dialog.
2. In WalletFeed, tap **Replace Key**.
3. Paste the key in the **Publishable Key** field.
4. Tap **Replace**.

### If Supabase stopped your project

The Supabase [pricing page](https://supabase.com/pricing) tells you that Free plan projects "are paused after 1 week of inactivity".

1. On your computer, open the [Supabase dashboard](https://supabase.com/dashboard).
2. Select the organization of the project.
3. Select the project.
4. If Supabase stopped the project, click **Resume project**.
5. If Supabase shows a dialog, obey its instructions.
6. In WalletFeed, open the Supabase destination.
7. Tap **Send Test**.

### If no new rows show in the table

WalletFeed sends changes when it is open, or when iOS starts it in the background.

1. Open WalletFeed.
2. Make sure that **Background Sync** is on in **Settings** › **Sync**.
3. Open the Supabase destination.
4. Make sure that the destination shows no error below **Last Sync**.
5. Tap **Send Test**. Supabase receives a test row with the description `WalletFeed test transaction`.
6. In the Supabase **Table Editor**, delete the test row.
