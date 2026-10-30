# Send Apple Card transactions to Supabase

WalletFeed sends your Apple Card, Apple Cash and Savings transactions from your iPhone to a Postgres database in your Supabase project. You copy two values from Supabase into WalletFeed, then you paste SQL from WalletFeed into the Supabase **SQL Editor**.

## Before you start

You must have:

- An iPhone with iOS 26 or a newer version
- WalletFeed, with access to your [Wallet accounts](/docs/wallet-accounts/)
- [WalletFeed Pro](/docs/walletfeed-pro/), a subscription with a 1-week free trial, or a one-time Lifetime purchase
- A Supabase account, or an email address for a new account
- A web browser on a computer or on your iPhone.

WalletFeed is available only in the US.

## Step 1: Make a Supabase project

1. If you have a Supabase project for your transactions, go to [Step 2](#step-2-copy-the-project-url-and-the-publishable-key).
2. On your computer, open the [Supabase sign-up page](https://supabase.com/dashboard/sign-up) in a web browser.
3. Type your email address and a password.
4. Click **Sign up**. You can also click **Continue with GitHub**.

   ![The Supabase sign-up page, with the Sign up button highlighted below the Email and Password fields.](https://walletfeed.app/guides/apple-card-to-supabase/supabase-sign-up.webp)
5. If Supabase sends you an email, open the link in that email.
6. In the [Supabase dashboard](https://supabase.com/dashboard), make a new project.
7. Type the details for the project.
8. Wait until the new database starts.

> **Note:** WalletFeed does not use a database password. It uses only the project URL and the publishable key.

## Step 2: Copy the project URL and the publishable key

1. In your Supabase project, open the **Connect** dialog.
2. Copy the project URL. The URL starts with `https://` and ends with `.supabase.co`.
3. If your project has no publishable key, make one in **Settings** › **API Keys**.
4. Copy the publishable key. The key starts with `sb_publishable_`.
5. If Supabase is open on your computer, send the URL and the key to your iPhone, for example with AirDrop.

> **Note:** WalletFeed does not accept a secret key, which starts with `sb_secret_`. With a secret key, Supabase ignores the Row Level Security policies of your project.

## Step 3: Add Supabase in WalletFeed

1. On your iPhone, open WalletFeed.
2. Tap **Destinations**.
3. Tap **+** at the top of the screen.

   ![The Destinations screen with no destinations, and the + button at the top.](https://walletfeed.app/guides/apple-card-to-supabase/walletfeed-destinations-empty-pro.webp)
4. In the **Sheets & Databases** section, tap **Supabase**.

   ![The Add Destination list, with the Budgeting section and the start of the Sheets & Databases section.](https://walletfeed.app/guides/apple-card-to-supabase/walletfeed-add-destination.webp)
5. If WalletFeed shows the **WalletFeed Pro** screen, get WalletFeed Pro. Then the Supabase form opens.
6. Paste the publishable key in **Publishable Key**.

   ![The Supabase form in WalletFeed, with the Publishable Key field, the project URL field, Share SQL and the setup steps.](https://walletfeed.app/guides/apple-card-to-supabase/walletfeed-setup-supabase.webp)
7. Paste the project URL in the field below the key. When this field is empty, it shows `https://abcd.supabase.co`.

> **Note:** WalletFeed keeps the key in the Keychain on your iPhone. WalletFeed has no account and no WalletFeed servers.

## Step 4: Make the table in Supabase

The SQL from WalletFeed makes the table `walletfeed_transactions` in your project. It also adds a policy that lets only this WalletFeed destination read and write the table. Supabase tells you that the publishable key is [safe to show in an app](https://supabase.com/docs/guides/api/api-keys). With this policy, a person who has only the publishable key cannot read your transactions.

1. In WalletFeed, tap **Share SQL**. The share sheet opens.
2. If Supabase is open on your computer, send the SQL to your computer, for example with AirDrop.
3. If Supabase is open on your iPhone, tap **Copy** in the share sheet.
4. In your Supabase project, open the **SQL Editor**.
5. Paste the SQL in the editor.
6. Click **Run**.

## Step 5: Start to send transactions

1. On your iPhone, open WalletFeed again.
2. Tap **Add**. WalletFeed reads one row of the table to make sure that the URL, the key and the SQL are correct.
3. If WalletFeed shows an error below **Share SQL**, refer to [If something goes wrong](#if-something-goes-wrong).
4. Read the message **Send Transactions to Supabase?** It tells you the data that Supabase receives, the accounts, and the start date.
5. Tap **Send**. WalletFeed adds the destination and starts to send your transactions.
6. In Supabase, open the **Table Editor**.
7. Select the table `walletfeed_transactions`. Each transaction is one row.

> **Note:** If you tap **Cancel** in step 4, WalletFeed does not add the destination. The Supabase form stays open.

## Columns in the Supabase table

Each transaction is one row in the table `public.walletfeed_transactions`. WalletFeed writes these values:

| Column | Postgres type | Value |
| --- | --- | --- |
| `id` | `text` | The WalletFeed ID of the transaction. This column is the primary key. |
| `date` | `date` | The day of the transaction, in the time zone of your iPhone. |
| `merchant` | `text` | The merchant name, or the description if Wallet has no merchant name. |
| `amount` | `numeric` | The amount. Purchases and fees are negative numbers. Payments and refunds are positive numbers. |
| `currency` | `text` | The currency code, for example `USD`. |
| `category` | `text` | The WalletFeed category, for example Groceries or Travel. |
| `status` | `text` | The status in Wallet, for example `pending`, `authorized` or `booked`. |
| `pending` | `boolean` | `true` when the status is `pending` or `authorized`, and `false` at other times. |
| `account` | `text` | The account name, for example Apple Card. |
| `description` | `text` | The description of the transaction in Wallet. |
| `type` | `text` | The transaction type in Wallet, for example `pointOfSale` or `refund`. |
| `mcc` | `integer` | The merchant category code. |
| `foreign_amount` | `numeric` | For a purchase in a different currency, the amount in that currency, with the same sign as `amount`. |
| `foreign_currency` | `text` | The code of that different currency. |

For a purchase in dollars, `foreign_amount` and `foreign_currency` are empty (`null`). When a transaction changes, WalletFeed updates its row by `id`. Thus, each transaction has only one row.

Your transactions go from your iPhone directly to your Supabase project. After Supabase receives your transactions, the Supabase terms are applicable to them.

## Sync times and pending charges

While WalletFeed is open, Supabase receives changes in seconds. When WalletFeed is closed, iOS starts WalletFeed in approximately 1 hour or less after a change in Wallet. For this, [Background Sync](/docs/background-sync/) must be on in **Settings** › **Sync**. **Background Sync** is on until you set it to off.

A pending charge has the value `true` in `pending`. When its status changes to `booked`, WalletFeed updates the same row. If a charge becomes declined or expired, or if Wallet removes a transaction, WalletFeed deletes its row. A refund is a different transaction, with a positive number in `amount`.

## Send previous transactions

A new destination also receives previous transactions, from the start date in **Settings** › **Sync** › **Initial History**. **Initial History** is **All** until you change it.

To send transactions from a different period, use [Send History](/docs/send-history/):

1. In WalletFeed, tap **Destinations**.
2. Tap the Supabase destination. Its name starts with **Supabase ·**.
3. Tap **Send History**.
4. Tap **30 Days**, **90 Days**, **1 Year** or **All**.

Supabase keeps one row for each transaction. To stop, tap **Send History**, then tap **Stop Sending**.

## Change or stop the destination

1. In WalletFeed, tap **Destinations**.
2. Tap the Supabase destination.

   ![The screen of a Lunch Money destination, with Name, Enabled, Last Sync, Replace Token, Filter, Send History, Send Test and Delete.](https://walletfeed.app/guides/apple-card-to-supabase/walletfeed-destination-detail.webp)

The screen of a Supabase destination has the same controls. It also has **Project**, **Share SQL** and **Replace Key**, but not **Replace Token**.

To send only some transactions, set **Filter** to on. Then select the transactions with **Accounts**, **Categories**, **Minimum** and the other controls. Refer to [Choose what to send](/docs/choose-what-to-send/).

To stop the destination for a time, set **Enabled** to off.

To use a different publishable key, tap **Replace Key**. Paste the new key, then tap **Replace**. WalletFeed keeps the new key only after it can read the table.

To get the SQL again, tap **Share SQL** in the destination. This SQL has the same token as the destination, so you can use it in the **SQL Editor** again. This SQL keeps the rows. It also adds the columns `foreign_amount` and `foreign_currency` if the table does not have them.

To remove the destination, tap **Delete**, then tap **Delete** again. The rows that WalletFeed sent stay in your Supabase table. To remove them, delete the rows or the table in Supabase.

## If something goes wrong

### If you cannot tap Add

WalletFeed lets you tap **Add** only when the form has a publishable key and a correct project URL. If the key is a secret key, WalletFeed also shows "Use the publishable key. Secret keys skip the table's policy."

1. Copy the publishable key from the **Connect** dialog again. The key starts with `sb_publishable_`.
2. Paste the key in **Publishable Key**.
3. Paste the project URL from the **Connect** dialog again.

### If WalletFeed shows "Key rejected. Copy the publishable key again."

Supabase did not accept the key, or the SQL that you used came from a different Supabase form. Each time you open the Supabase form, WalletFeed makes new SQL with a new token.

1. Copy the publishable key from the **Connect** dialog again.
2. Paste the key in **Publishable Key**.
3. Tap **Share SQL**.
4. Paste the new SQL in the **SQL Editor**.
5. Click **Run**.
6. In WalletFeed, tap **Add**.

### If WalletFeed shows "Table not found. Run the SQL, then try again."

The project has no `walletfeed_transactions` table. For example, you did not click **Run**, or you used the **SQL Editor** of a different project.

1. In Supabase, open the project that has the URL from Step 2.
2. Open the **SQL Editor**.
3. Paste the SQL from **Share SQL**.
4. Click **Run**.
5. In WalletFeed, tap **Add**.

### If the destination shows "Authentication failed" or "Rejected (HTTP 404)"

Supabase did not accept the key or the token, or the table is not in the project. For example, SQL from a different WalletFeed destination replaced the token in the table.

1. In WalletFeed, tap **Destinations**.

   ![The Destinations list, with a destination named n8n that shows Authentication failed.](https://walletfeed.app/guides/apple-card-to-supabase/walletfeed-destinations-failure.webp)
2. Tap the Supabase destination.
3. Tap **Share SQL**.
4. Paste the SQL in the **SQL Editor**.
5. Click **Run**.
6. In WalletFeed, tap **Send Test**.
7. If **Send Test** shows an error, tap **Replace Key**.
8. Paste the publishable key from the **Connect** dialog, then tap **Replace**.

### If Supabase paused your project

The Supabase [pricing page](https://supabase.com/pricing) tells you that Free plan projects "are paused after 1 week of inactivity".

1. Open your project in the [Supabase dashboard](https://supabase.com/dashboard).
2. If the dashboard shows that Supabase paused the project, click the button that starts the project again.
3. In WalletFeed, open the Supabase destination.
4. Tap **Send Test**.

### If no new rows show in the table

WalletFeed sends changes while it is open, or when iOS starts it in the background.

1. Open WalletFeed.
2. Make sure that **Background Sync** is on in **Settings** › **Sync**.
3. Open the Supabase destination.
4. Make sure that the destination shows no error below **Last Sync**.
5. Tap **Send Test**. Supabase receives a test row with the description `WalletFeed test transaction`.
6. In the **Table Editor**, delete the test row.
