# Send Apple Card transactions to Supabase

WalletFeed sends your Apple Card, Apple Cash and Savings transactions from your iPhone to a Postgres database in your Supabase project. You copy the project URL and the publishable key to WalletFeed. Then you paste the SQL from WalletFeed in the Supabase **SQL Editor**.

## Before you start

You must have these items:

- An iPhone with iOS 26 or a newer version. WalletFeed is available only in the US.
- WalletFeed, with access to your [Wallet accounts](/docs/wallet-accounts/).
- [WalletFeed Pro](/docs/walletfeed-pro/) (a subscription with a 1-week free trial, or a one-time Lifetime purchase). You must have WalletFeed Pro to send transactions to Supabase.
- A Supabase account, or an e-mail address for a new account. You can use the Free plan of Supabase.
- A web browser on a computer. In this guide, you use the Supabase **SQL Editor** on the computer.

> **Note:** The Supabase [pricing page](https://supabase.com/pricing) tells you that Free plan projects "are paused after 1 week of inactivity". [If Supabase stopped your project](#if-supabase-stopped-your-project) tells you how to start the project again.

## Your key stays on your iPhone

- WalletFeed keeps the publishable key in the Keychain on your iPhone. iOS encrypts the Keychain.
- The publishable key does not go to iCloud Keychain or to your other devices.
- WalletFeed has no account and no servers. No person at WalletFeed can see or get the publishable key.
- Your iPhone sends the publishable key only to your Supabase project, in each request to your Supabase project.
- When you delete the destination, WalletFeed deletes the publishable key from your iPhone. You can also delete the key in Supabase.

## Step 1: Make a Supabase project

A Supabase project has its own Postgres database. If you have a project for your transactions, go to [Step 2](#step-2-open-the-supabase-form-in-walletfeed).

1. On your computer, open the [Supabase sign-up page](https://supabase.com/dashboard/sign-up) in a web browser.
2. Type your e-mail address in **Email**.
3. Type a password in **Password**.
4. Click **Sign up**.

   ![The Supabase sign-up page, with the highlighted Sign up button below the Email and Password fields.](https://walletfeed.app/guides/apple-card-to-supabase/supabase-sign-up.webp)

5. If Supabase shows an hCaptcha image check, obey the instructions in the check.
6. If Supabase sends you an e-mail, open the hyperlink in the e-mail.
7. If Supabase shows "Sign in to your account", get access to your Supabase account with your e-mail address and your password.

   ![The Supabase sign-in page, with the highlighted Sign in button below the Email and Password fields.](https://walletfeed.app/guides/apple-card-to-supabase/supabase-sign-in.webp)

8. On the "Your organizations" page, click **New organization**.

   A new Supabase account has no organization. An organization contains your projects.

   ![The Supabase organizations page with no organizations, and the highlighted New organization button.](https://walletfeed.app/guides/apple-card-to-supabase/supabase-organizations.webp)

9. In **Name**, replace the text with a name for the organization, for example `WalletFeed`.
10. In **Type**, select a type, for example **Personal**.
11. In **Plan**, select a plan, for example **Free - $0/month**.
12. Click **Create organization**.

    ![The "Create a new organization" form, with the name WalletFeed Docs, the Personal type, the Free plan and the highlighted Create organization button.](https://walletfeed.app/guides/apple-card-to-supabase/supabase-new-organization.webp)

    Result: Supabase shows "Create a new project".

13. In **Project name**, replace the text with a name for the project, for example `WalletFeed`.
14. Click **Generate a password**.

    Supabase puts a password in **Database password**. WalletFeed does not use the database password.

15. In **Region**, select a region, for example **West US (Oregon)**.
16. In **Security**, make sure that **Enable Data API** has a checkmark.

    WalletFeed sends your transactions to the Data API of the project.

17. Click **Create new project**.

    ![The "Create a new project" form, with a checkmark for Enable Data API and the highlighted Create new project button.](https://walletfeed.app/guides/apple-card-to-supabase/supabase-new-project.webp)

18. Wait until the project page shows **Healthy** below **STATUS**.

> **Note:** On the sign-up page, you can also make the account with **Continue with GitHub**, **Continue with ChatGPT** or **Continue with SSO**.

## Step 2: Open the Supabase form in WalletFeed

1. On your iPhone, open WalletFeed.
2. Tap **Destinations**.
3. Tap **+** at the top of the screen.

   ![The Destinations screen with no destinations, and the + button at the top.](https://walletfeed.app/guides/apple-card-to-supabase/walletfeed-destinations-empty-pro.webp)

4. In the search field, type `Supabase`.

   ![The Add Destination screen, with the Destinations search field above the list of destinations.](https://walletfeed.app/guides/apple-card-to-supabase/walletfeed-add-destination.webp)

5. Tap **Supabase**.
6. If WalletFeed shows **WalletFeed Pro**, get [WalletFeed Pro](/docs/walletfeed-pro/).

   Result: After you get WalletFeed Pro, WalletFeed shows the Supabase form.

   ![The Supabase form in WalletFeed, with the Publishable Key field, the URL field, Share SQL and the Supabase Dashboard link.](https://walletfeed.app/guides/apple-card-to-supabase/walletfeed-setup-supabase.webp)

7. Keep the Supabase form open until you tap **Add** in [Step 5](#step-5-add-the-destination-in-walletfeed).

   You can use a different app while the form is open. Each time that you open the Supabase form, WalletFeed makes new SQL with a new token for the table. If you close the form, do Step 2, Step 3 and Step 4 again.

## Step 3: Copy the publishable key and the project URL

Do these steps on your iPhone. To copy the key and the URL on a Mac, refer to [Copy the key and the URL on a Mac](#copy-the-key-and-the-url-on-a-mac).

1. In the Supabase form, tap **Supabase Dashboard**.

   Result: Your web browser opens Supabase.

2. If Supabase shows "Sign in to your account", get access to your Supabase account with your e-mail address and your password.
3. If Supabase does not show "Select a project to continue", tap **Supabase Dashboard** in WalletFeed again.
4. In "Select a project to continue", tap your project.

   ![Supabase on an iPhone, with the page "Select a project to continue" and the highlighted WalletFeed Docs project.](https://walletfeed.app/guides/apple-card-to-supabase/supabase-iphone-select-project.webp)

5. In "Connect to your project", tap **Server**.

   ![The "Connect to your project" panel on an iPhone, with the highlighted Server button.](https://walletfeed.app/guides/apple-card-to-supabase/supabase-iphone-connect.webp)

6. Scroll to `.env`.
7. Tap the copy button in the `SUPABASE_PUBLISHABLE_KEY=` row.

   The publishable key starts with `sb_publishable_`. Do not copy the `SUPABASE_SECRET_KEY=` row. WalletFeed does not accept a secret key.

   ![The .env rows in the Connect panel on an iPhone, with the highlighted copy button for the publishable key.](https://walletfeed.app/guides/apple-card-to-supabase/supabase-iphone-connect-key.webp)

8. Open WalletFeed again.
9. Touch and hold **Publishable Key**.
10. Tap **Paste**.
11. Open the Supabase page in your web browser again.
12. Tap the copy button in the `SUPABASE_URL=` row.
13. Open WalletFeed again.
14. Touch and hold the field that shows `https://abcd.supabase.co`.
15. Tap **Paste**.

### Copy the key and the URL on a Mac

If your Mac uses the same Apple Account as your iPhone, you can copy on the Mac and paste on the iPhone with [Universal Clipboard](https://support.apple.com/en-us/102430).

1. On your Mac, open your project in the [Supabase dashboard](https://supabase.com/dashboard).
2. Click **Copy**, to the right of the project URL.
3. Click **Publishable key**.

   ![The Copy menu on the project page, with the highlighted Project URL and Publishable key items.](https://walletfeed.app/guides/apple-card-to-supabase/supabase-copy-menu.webp)

4. On your iPhone, touch and hold **Publishable Key** in the Supabase form.
5. Tap **Paste**.
6. On your Mac, click **Copy** again.
7. Click **Project URL**.
8. On your iPhone, touch and hold the field that shows `https://abcd.supabase.co`.
9. Tap **Paste**.

> **Note:** **Connect** at the top of the project page opens the same panel as on the iPhone. On **Framework**, the key and the URL are in one block of text. On **Server**, each row has a copy button.

## Step 4: Make the table in Supabase

The SQL from WalletFeed makes the `walletfeed_transactions` table in your project. On the **API Keys** page, Supabase shows "Publishable keys can be safely shared publicly". Thus, the SQL also adds a policy to the table. The policy lets WalletFeed read and change the table only with the token of this destination. A person with only the project URL and the publishable key cannot read your transactions.

1. On your iPhone, in the Supabase form, tap **Share SQL**.

   Result: iOS opens a menu with **Copy**.

2. Send the SQL to your computer, for example with AirDrop.

   If your computer is a Mac with Universal Clipboard, you can tap **Copy**.

3. On your computer, open your project in the [Supabase dashboard](https://supabase.com/dashboard).
4. In the bar on the left, click the **SQL Editor** icon.

   The icons in this bar have no names on the page. When you put the pointer on an icon, Supabase shows its name.

   ![The empty SQL Editor, with the highlighted SQL Editor icon in the bar on the left.](https://walletfeed.app/guides/apple-card-to-supabase/supabase-sql-editor.webp)

5. If Supabase shows "Snippets no longer save automatically", click **Understood**.

   ![The Supabase message "Snippets no longer save automatically", with the Understood button.](https://walletfeed.app/guides/apple-card-to-supabase/supabase-sql-editor-notice.webp)

6. Paste the SQL in the editor.

   The editor shows 28 lines of SQL. Do not change the SQL.

7. Click **Run**.

   ![The SQL Editor with the WalletFeed SQL, and the highlighted Run button.](https://walletfeed.app/guides/apple-card-to-supabase/supabase-sql-run.webp)

   Result: Supabase shows "Potential issue detected". Supabase shows this message because the SQL removes all access to the table first. Then the SQL gives access only to this destination. The SQL does not delete the table or its rows.

8. Click **Run query**.

   ![The Supabase message "Potential issue detected", with the highlighted Run query button.](https://walletfeed.app/guides/apple-card-to-supabase/supabase-destructive-warning.webp)

9. Make sure that the result is "Success. No rows returned".

   ![The SQL Editor with the result "Success. No rows returned", and the highlighted Table Editor icon in the bar on the left.](https://walletfeed.app/guides/apple-card-to-supabase/supabase-sql-success.webp)

> **Note:** It is not necessary to save the SQL in Supabase. In the destination, **Share SQL** gives you the same SQL again.

## Step 5: Add the destination in WalletFeed

1. On your iPhone, open WalletFeed again.
2. In the Supabase form, tap **Add**.

   Result: WalletFeed tries to read the table with the project URL and the publishable key.

3. If WalletFeed shows a message in red below **Share SQL**, refer to [If there is a problem](#if-there-is-a-problem).
4. In **Send Transactions to Supabase?**, tap **Send**.

   The message tells you the data that Supabase receives and the Wallet accounts. If **Initial History** is not **All**, the message also gives the start date. If you tap **Cancel**, WalletFeed does not add the destination. The Supabase form stays open.

   Result: WalletFeed starts to send your transactions to Supabase. In **Destinations**, the name of the new destination has two parts, for example "Supabase · abcd". The second part is from the project URL.

## Step 6: Find the transactions in Supabase

1. On your computer, open your project in the [Supabase dashboard](https://supabase.com/dashboard).
2. In the bar on the left, click the **Table Editor** icon.
3. Click `walletfeed_transactions`.

   ![The Table Editor, with the highlighted walletfeed_transactions table in the list.](https://walletfeed.app/guides/apple-card-to-supabase/supabase-table-list.webp)

   Result: The Table Editor shows one row for each transaction. For the columns, refer to [Columns in the Supabase table](#columns-in-the-supabase-table).

## Columns in the Supabase table

Each transaction is one row in the `public.walletfeed_transactions` table.

![The walletfeed_transactions table in the Supabase Table Editor, with six rows from WalletFeed.](https://walletfeed.app/guides/apple-card-to-supabase/supabase-walletfeed-result.webp)

WalletFeed puts these values in the columns:

| Column | Postgres type | Value |
| --- | --- | --- |
| `id` | `text` | The WalletFeed ID of the transaction. This column is the primary key. |
| `date` | `date` | The day of the transaction, in the time zone of your iPhone. |
| `merchant` | `text` | The merchant name, or the description if Wallet has no merchant name. |
| `amount` | `numeric` | The amount of the transaction. A purchase or a fee is less than 0. A payment or a refund is more than 0. |
| `currency` | `text` | The currency code, for example `USD`. |
| `category` | `text` | The WalletFeed category, for example Groceries or Travel. |
| `status` | `text` | The status in Wallet, for example `pending`, `authorized` or `booked`. |
| `pending` | `boolean` | `true` when the status is `pending` or `authorized`, and `false` for a different status. |
| `account` | `text` | The name of the Wallet account, for example Apple Card. |
| `description` | `text` | The description of the transaction in Wallet. |
| `type` | `text` | The transaction type in Wallet, for example `pointOfSale` or `refund`. |
| `mcc` | `integer` | The merchant category code. |
| `foreign_amount` | `numeric` | For a purchase in a different currency, the amount in that currency, with the same sign as `amount`. |
| `foreign_currency` | `text` | The code of that different currency. |

For a purchase in US dollars, `foreign_amount` and `foreign_currency` have no value (`null`). When a transaction changes, WalletFeed updates the row that has the same `id`. If you change a value in a WalletFeed column, WalletFeed replaces your change when the transaction changes again.

> **Caution:** Do not change the `id` of a row. WalletFeed uses the `id` to find the row. If the `id` changes, WalletFeed adds a new row when the transaction changes in Wallet.

Your transactions go from your iPhone directly to your Supabase project. WalletFeed has no account and no WalletFeed servers. After Supabase receives your transactions, the terms of Supabase are applicable to them.

## New and changed transactions

While WalletFeed is open, Supabase receives changes in seconds. When WalletFeed is not open, iOS starts WalletFeed approximately 1 hour or less after a change in Wallet. If [Background Sync](/docs/background-sync/) is on in **Settings** › **Sync**, WalletFeed then sends the change. **Background Sync** is on until you set it to off.

A pending charge has the value `true` in `pending`. When its status changes to `booked`, WalletFeed updates the same row. WalletFeed deletes the row of a declined or expired charge. WalletFeed also deletes the row of a transaction that Wallet removes.

A refund is a new row. Its `amount` is more than 0.

## Send previous transactions

A new destination also receives previous transactions from the start date in **Settings** › **Sync** › **Initial History**. **Initial History** is **All** until you change it.

To send previous transactions after you add Supabase, do these steps:

1. In **Destinations**, tap the Supabase destination.
2. Tap **Send History**.
3. Tap **30 Days**, **90 Days**, **1 Year** or **All**.
4. To stop WalletFeed before it sends all of the transactions, tap **Send History** › **Stop Sending**.

**Send History** does not make copies of rows. WalletFeed updates the row that has the same `id`. If you deleted a row in Supabase, **Send History** adds the row again.

For more information, refer to [Send previous transactions](/docs/send-history/).

## Change or remove the destination

You change the Supabase destination on its screen in **Destinations**.

1. In WalletFeed, tap **Destinations**.
2. Tap the Supabase destination.

   ![The screen of a Lunch Money destination, with Name, Enabled, Last Sync, Replace Token, Filter, Send History, Send Test and Delete.](https://walletfeed.app/guides/apple-card-to-supabase/walletfeed-destination-detail.webp)

The screen of a Supabase destination has the same items. In place of **Replace Token**, it has **Project**, **Share SQL** and **Replace Key**.

### Send only some transactions

1. In **Destinations**, tap the Supabase destination.
2. Set **Filter** to on.
3. Change **Include**, **Minimum**, **Include Pending**, **Accounts**, **Categories** or **Exclude**.

For more information, refer to [Filter the transactions for a destination](/docs/choose-what-to-send/).

### Stop the destination for a time

1. In **Destinations**, tap the Supabase destination.
2. Set **Enabled** to off.

   Until you set **Enabled** to on again, WalletFeed does not send transactions to Supabase.

### Replace the key

If you deleted the publishable key in Supabase, or if Supabase does not accept the key, do these steps:

1. If the project has no publishable key, make a key (refer to [If the project has no publishable key](#if-the-project-has-no-publishable-key)).
2. On your iPhone, open the [Supabase dashboard](https://supabase.com/dashboard/project/_?showConnect=true).
3. Copy the publishable key with steps 2 thru 7 of [Step 3](#step-3-copy-the-publishable-key-and-the-project-url).
4. Open WalletFeed again.
5. In **Destinations**, tap the Supabase destination.
6. Tap **Replace Key**.
7. Touch and hold **Publishable Key**.
8. Tap **Paste**.
9. Tap **Replace**.

   Result: Before WalletFeed puts the new key in the Keychain, WalletFeed reads the table with the key. Then **Replace Key** shows a green checkmark.

### Use the SQL of the destination again

In the destination, **Share SQL** gives the SQL with the token of this destination. This SQL keeps the rows in the table. If the table does not have the `foreign_amount` and `foreign_currency` columns, the SQL adds them.

1. In **Destinations**, tap the Supabase destination.
2. Tap **Share SQL**.
3. Send the SQL to your computer, for example with AirDrop.
4. On your computer, open the **SQL Editor** of your project.
5. Paste the SQL in the editor.
6. Click **Run**.
7. Click **Run query**.
8. In WalletFeed, tap **Send Test**.

### Remove Supabase from WalletFeed

1. In **Destinations**, tap the Supabase destination.
2. Tap **Delete**.
3. Tap **Delete** again.

   Result: WalletFeed removes the destination and deletes the key from your iPhone. The rows that WalletFeed sent stay in your Supabase table. You can delete these rows or the table in Supabase.

### Delete the key in Supabase

After you delete the key, Supabase does not accept the key from WalletFeed. Supabase also does not accept the key from a different app that uses it.

1. On your computer, open your project in the [Supabase dashboard](https://supabase.com/dashboard).
2. In the bar on the left, click the **Project Settings** icon.
3. Click **API Keys**.
4. In the row of the publishable key, click **⋮**.
5. Click **Delete API key**.

   ![The menu of the default publishable key, with the highlighted Delete API key item.](https://walletfeed.app/guides/apple-card-to-supabase/supabase-delete-publishable-key.webp)

6. In the dialog, type the name of the key, for example `default`.
7. Click **Yes, irreversibly delete this API key**.

   Result: Supabase shows "Successfully deleted publishable key". The WalletFeed destination then shows "Authentication failed".

## If there is a problem

To make sure that WalletFeed can send transactions to Supabase, do these steps:

1. In **Destinations**, tap the Supabase destination.
2. Tap **Send Test**.

   Result: If Supabase receives the test row, WalletFeed shows a green checkmark.

> **Note:** **Send Test** adds a test row with the description `WalletFeed test transaction` to the table. If you tap **Send Test** again, WalletFeed does not add a second test row. You can delete the test row in the **Table Editor**.

### If you cannot tap Add

WalletFeed lets you tap **Add** only when the form has a key and a project URL. If the key is a secret key, you cannot tap **Add**, and WalletFeed shows "Use the publishable key. Secret keys skip the table's policy."

1. Copy the publishable key again (refer to [Step 3](#step-3-copy-the-publishable-key-and-the-project-url)). The key starts with `sb_publishable_`.
2. In WalletFeed, clear the **Publishable Key** field.
3. Paste the key in the **Publishable Key** field.
4. Make sure that the field below the key contains the project URL.

### If WalletFeed shows "Key rejected. Copy the publishable key again."

Supabase did not accept the key. For example, you copied only a part of the key, or a person deleted the key in Supabase.

1. Copy the publishable key again (refer to [Step 3](#step-3-copy-the-publishable-key-and-the-project-url)).
2. In WalletFeed, clear the **Publishable Key** field.
3. Paste the key in the **Publishable Key** field.
4. Tap **Add**.

If the project has no publishable key, refer to [If the project has no publishable key](#if-the-project-has-no-publishable-key).

### If WalletFeed shows "Table not found. Run the SQL, then try again."

The project has no `walletfeed_transactions` table. For example, you did not click **Run query**, or you pasted the SQL in a different project.

1. On your computer, open the project that has the URL from Step 3.
2. Open the **SQL Editor**.
3. In WalletFeed, tap **Share SQL**.
4. Send the SQL to your computer, for example with AirDrop.
5. On your computer, paste the SQL in the **SQL Editor**.
6. Click **Run**.
7. Click **Run query**.
8. In WalletFeed, tap **Add**.

### If WalletFeed shows "Couldn't connect"

WalletFeed cannot connect to the project URL in the form.

1. Make sure that your iPhone has an internet connection.
2. Copy the project URL again (refer to [Step 3](#step-3-copy-the-publishable-key-and-the-project-url)).
3. In WalletFeed, clear the field below the key.
4. Paste the URL in this field.
5. Tap **Add**.

### If the project has no publishable key

A new project has a publishable key with the name `default`. If a person deleted this key, Supabase shows "No publishable keys created yet" on the **API Keys** page.

1. On your computer, open your project in the [Supabase dashboard](https://supabase.com/dashboard).
2. In the bar on the left, click the **Project Settings** icon.
3. Click **API Keys**.

   ![The Project Settings page in Supabase, with the highlighted settings icon and API Keys item.](https://walletfeed.app/guides/apple-card-to-supabase/supabase-project-settings.webp)

4. Click **New publishable key**.
5. Obey the instructions in Supabase.
6. Copy the new key, as in [Step 3](#step-3-copy-the-publishable-key-and-the-project-url).

   On a Mac, you can also click the copy button in the row of the key. The **API Keys** page does not show the project URL.

   ![The API Keys page, with the highlighted copy button of the default publishable key above the secret keys.](https://walletfeed.app/guides/apple-card-to-supabase/supabase-api-keys.webp)

### If the destination shows "Authentication failed"

Supabase did not accept the key or the token of the destination. For example, a person deleted the key in Supabase, or SQL from a different Supabase form or destination replaced the token in the policy.

1. In WalletFeed, tap **Destinations**.

   ![The Destinations list, with an n8n destination that shows Authentication failed.](https://walletfeed.app/guides/apple-card-to-supabase/walletfeed-destinations-failure.webp)

2. Use the SQL of the Supabase destination again (refer to [Use the SQL of the destination again](#use-the-sql-of-the-destination-again)).
3. If **Send Test** shows an error, replace the key (refer to [Replace the key](#replace-the-key)).

> **Note:** When you tap **Add**, WalletFeed does not make sure that the token in the policy is correct. If the token is not correct, the destination shows "Authentication failed" after WalletFeed tries to send the first transactions.

### If the destination shows "Rejected (HTTP 404)"

The project has no `walletfeed_transactions` table. For example, a person deleted the table in Supabase.

1. Use the SQL of the Supabase destination again (refer to [Use the SQL of the destination again](#use-the-sql-of-the-destination-again)).

### If Supabase stopped your project

The Supabase [pricing page](https://supabase.com/pricing) tells you that Free plan projects "are paused after 1 week of inactivity".

1. On your computer, open your project in the [Supabase dashboard](https://supabase.com/dashboard).
2. If Supabase stopped the project, obey the instructions on the project page to start the project again.
3. On your iPhone, tap the Supabase destination in **Destinations**.
4. Tap **Send Test**.

### If no new rows show in the table

WalletFeed sends changes when it is open, or when iOS starts it in the background.

1. On your iPhone, open WalletFeed.
2. Tap the gear icon at the top of **Destinations**.
3. In **Settings** › **Sync**, make sure that **Background Sync** is on.
4. In **Destinations**, tap the Supabase destination.
5. Make sure that the destination shows no error below **Last Sync**.
6. Make sure that **Filter** is off, or that the filter includes the transactions.
7. Tap **Send Test**.
