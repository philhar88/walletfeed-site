# Send Apple Card transactions to Coda

WalletFeed sends your Apple Card, Apple Cash and Savings transactions from your iPhone to a table in Coda. Coda changed its name to Superhuman Docs. You make the table and an API token in Superhuman Docs, and then you paste the token in WalletFeed.

## Before you start

You must have these items:

- An iPhone with iOS 26 or a newer version. WalletFeed is available only in the US.
- WalletFeed, and an Apple Card, Apple Cash or Savings account that WalletFeed can read.
- [WalletFeed Pro](/docs/walletfeed-pro/), which is necessary for [destinations](/docs/destinations/). It is a subscription with a 1-week free trial, or a one-time Lifetime purchase.
- A Superhuman Docs account. You can make an API token on the Free plan.
- A computer with a web browser, for the steps in Superhuman Docs.

## Step 1: Make a doc and a table in Superhuman Docs

1. On your computer, open [Superhuman Docs](https://docs.superhuman.com/).
2. Get access to your Superhuman Docs account.
3. Click **+ New doc**.

   ![The Superhuman Docs home page, with the New doc button at the top of the sidebar.](https://walletfeed.app/guides/apple-card-to-coda/coda-docs-home.webp)

4. If a message or the **Docs AI** panel opens, close it.
5. If the sidebar with the list of pages is not open, click the sidebar button at the top left.
6. Click the doc name, **Untitled doc**, at the top of the sidebar.

   ![A new doc in Superhuman Docs, with its name, Untitled doc, at the top of the sidebar.](https://walletfeed.app/guides/apple-card-to-coda/coda-new-doc.webp)

7. Type a name for the doc, for example `WalletFeed`.
8. Press **Return**.
9. Click in the page, below **Add page title**. If you do not click in the page, Superhuman Docs adds the text that you type to the doc name.
10. Type `/table`.
11. In the menu, below **Tables**, click **Table**.

    ![The menu that opens when you type /table, with the Table item at the top.](https://walletfeed.app/guides/apple-card-to-coda/coda-insert-table.webp)

12. In the **New table** panel, click **Start blank**.

    ![The New table panel, with Start blank at the top.](https://walletfeed.app/guides/apple-card-to-coda/coda-start-blank.webp)

13. Double-click the table name, **Table**. This selects all of the name.
14. Type `WalletFeed Transactions`. In Step 4, WalletFeed selects the table that has this name.

    ![The table with its new name, WalletFeed Transactions.](https://walletfeed.app/guides/apple-card-to-coda/coda-name-table.webp)

15. Press **Return**.
16. Keep the doc in **My Docs**.
17. Do not use **Share** on the doc.

> **Note:** On the Free plan, a doc that other persons can open has a limit of 1,000 table rows. If the doc has more rows than this limit for 14 days, Superhuman Docs stops all changes to the doc. A doc that only you can open does not have this limit.

## Step 2: Make the columns

WalletFeed writes only to the columns that have the names in this table. Only the **WalletFeed ID** column is necessary. Each name must have the same letters and spaces as in this table, but the letters can be uppercase or lowercase.

| Column name | Column type |
|---|---|
| WalletFeed ID | Text |
| Date | Date |
| Merchant | Text |
| Amount | Number |
| Currency | Text |
| Category | Text |
| Status | Text |
| Pending | Checkbox |
| Account | Text |
| Description | Text |
| Type | Text |
| MCC | Number |
| Foreign Amount | Number |
| Foreign Currency | Text |

A new table has four columns: **Name**, **Column 2**, **Column 3** and **Notes**. You change their names first, and then you add the other 10 columns.

1. Click the column name **Name**. This selects the column.
2. Click **Name** again.
3. Type `WalletFeed ID`.

   ![The first column, with its new name, WalletFeed ID.](https://walletfeed.app/guides/apple-card-to-coda/coda-rename-first-column.webp)

4. Press **Return**.
5. Change the name of **Column 2** to `Date`, as in steps 1 to 4.
6. Put the pointer on **Date**. Superhuman Docs shows the type button (**T**) on the right side of the column name.
7. Click the type button.
8. Click **Column type** › **Date** › **Date**.

   ![The menu of the Date column, with Column type, Date and Date.](https://walletfeed.app/guides/apple-card-to-coda/coda-column-type-date.webp)

9. Change the name of **Column 3** to `Merchant`, as in steps 1 to 4.
10. Change the name of **Notes** to `Amount`, as in steps 1 to 4.
11. Put the pointer on **Amount**.
12. Click the type button.
13. Click **Column type** › **Number** › **Number**. This step is necessary because the **Notes** column has the type **Canvas**.

    ![The menu of the Amount column, with Column type, Number and Number.](https://walletfeed.app/guides/apple-card-to-coda/coda-column-type-number.webp)

14. Put the pointer on the column names. Superhuman Docs shows the **+** button at the right end of the column names.
15. If the table is wider than the window, scroll the table fully to the right.
16. Click **+**.

    ![The plus button at the end of the column names, which adds a column.](https://walletfeed.app/guides/apple-card-to-coda/coda-add-column.webp)

17. In **Pick column type**, click **Text**.

    ![The Pick column type menu, with Text at the top.](https://walletfeed.app/guides/apple-card-to-coda/coda-pick-column-type.webp)

18. Type `Currency`. If you do not type a name, the column has the name **Text**, and WalletFeed does not write to it.

    ![A new column with the name Currency.](https://walletfeed.app/guides/apple-card-to-coda/coda-name-new-column.webp)

19. Press **Return**.
20. For each column from `Category` to `Foreign Currency`, do steps 14 to 19 again, with its name and its column type. For a **Number** column, click **Number** › **Number** in step 17.
21. Put the pointer on the table.
22. Click **Options**.
23. Click **Columns**. The panel shows the 14 columns and their types.

    ![The Columns panel, with all 14 WalletFeed columns and their types.](https://walletfeed.app/guides/apple-card-to-coda/coda-all-columns.webp)

You can delete the three empty rows of the new table. For each empty row, do these steps:

1. Right-click the row.
2. If the menu does not show **Delete row**, scroll to the bottom of the menu.
3. Click **Delete row**.

## Step 3: Make an API token in Superhuman Docs

1. On your computer, open the [Superhuman Docs home page](https://docs.superhuman.com/).
2. Click your name at the bottom of the sidebar.
3. Click **Account settings**.

   ![The account menu, with Account settings.](https://walletfeed.app/guides/apple-card-to-coda/coda-account-menu.webp)

4. In the list on the left side, click **API connections**.

   ![The Account settings page, with API connections in the list on the left side.](https://walletfeed.app/guides/apple-card-to-coda/coda-account-settings.webp)

5. In **API tokens**, click **Generate API token**.

   ![The API tokens section, with the Generate API token button.](https://walletfeed.app/guides/apple-card-to-coda/coda-api-connections.webp)

6. In **Name**, type `WalletFeed`.
7. Click **Permission**. It shows **Read only** until you change it.
8. Click **Read and write**. With a **Read only** token, Superhuman Docs does not accept the transactions from WalletFeed.

   ![The New API token dialog, with Read and write in the Permission list.](https://walletfeed.app/guides/apple-card-to-coda/coda-token-permission.webp)

9. In **Scopes**, keep **Content** and **All** selected. With **Selected content**, WalletFeed cannot find your doc.

   ![The New API token dialog with the name WalletFeed, Read and write in Permission, Content and All in Scopes, and the Generate token button.](https://walletfeed.app/guides/apple-card-to-coda/coda-token-settings.webp)

10. Click **Generate token**.
11. In **API token generated**, click **Copy**. Superhuman Docs shows the token only one time.

    ![The API token generated dialog, with the Copy button.](https://walletfeed.app/guides/apple-card-to-coda/coda-token-created.webp)

12. If you closed the dialog before you clicked **Copy**, do steps 5 to 11 again.

> **Note:** If you use a Mac with the same Apple Account as your iPhone, you can paste the token on the iPhone with [Universal Clipboard](https://support.apple.com/en-us/102430).

> **Note:** On your iPhone, **Open Account Settings** on the Coda screen in WalletFeed opens **Account settings** › **API connections** in Superhuman Docs.

## Step 4: Add Coda in WalletFeed

1. On your iPhone, open WalletFeed.
2. Tap **Destinations**.
3. Tap **+** at the top of the screen.

   ![The empty Destinations screen, with the plus button at the top.](https://walletfeed.app/guides/apple-card-to-coda/walletfeed-destinations-empty-pro.webp)

4. Below **Sheets & Databases**, tap **Coda**. If you do not have WalletFeed Pro, WalletFeed first shows the **WalletFeed Pro** screen.
5. Paste the token in **API Token**.

   ![The Coda screen in WalletFeed, with the API Token field and three steps for Coda.](https://walletfeed.app/guides/apple-card-to-coda/walletfeed-setup-coda.webp)

6. If **Doc** does not show your doc, select your doc in **Doc**.
7. If **Table** does not show **WalletFeed Transactions**, select **WalletFeed Transactions** in **Table**.
8. Tap **Add**.
9. If WalletFeed shows a message in red below the fields, refer to [If there is a problem](#if-there-is-a-problem).
10. Read the **Send Transactions to Coda?** message.

    The message tells you which data the destination will receive, from which accounts and from which date. If you tap **Cancel**, WalletFeed removes the destination.

11. Tap **Send**.

    ![A Superhuman Docs table with six sample transactions in the 14 WalletFeed columns.](https://walletfeed.app/guides/apple-card-to-coda/coda-walletfeed-result.webp)

After some seconds, your table in Superhuman Docs shows your transactions. In **Destinations**, the new destination has the name of your doc after Coda, for example **Coda · WalletFeed**.

## Data in each column

WalletFeed writes these values to the columns:

| Column | Value |
|---|---|
| WalletFeed ID | The ID of the transaction in Wallet. WalletFeed uses it to find the row again. |
| Date | The date of the transaction, in the time zone of your iPhone. |
| Merchant | The merchant name, or the description if Wallet has no merchant name. |
| Amount | The value of the transaction. |
| Currency | The currency code, for example USD. |
| Category | The WalletFeed category, for example Dining or Groceries. |
| Status | The status in Wallet, for example `pending` or `booked`. |
| Pending | A selected checkbox while the charge is pending. |
| Account | The account name, for example Apple Card or Apple Cash. |
| Description | The description from Wallet. |
| Type | The transaction type from Wallet, for example `pointOfSale`. |
| MCC | The merchant category code. A **Number** column shows 5814 as 5,814. |
| Foreign Amount | The value in the currency of the merchant. |
| Foreign Currency | The currency code of the merchant. |

A value in **Amount** or **Foreign Amount** is less than zero for money that goes out of the account. It is more than zero for money that goes into the account. **Foreign Amount** and **Foreign Currency** are empty for a transaction in US dollars.

Your transactions go from your iPhone directly to Superhuman Docs. WalletFeed has no account and no WalletFeed servers. WalletFeed keeps the token in the Keychain on your iPhone. After Superhuman Docs receives your transactions, the terms of Superhuman Docs are applicable to them.

## New and changed transactions

While WalletFeed is open, the table receives changes in seconds. When WalletFeed is not open, iOS starts WalletFeed approximately 1 hour or less after a change in Wallet. If [Background Sync](/docs/background-sync/) is on in **Settings** › **Sync**, WalletFeed then sends the change.

A pending charge has a selected checkbox in **Pending**. When the charge changes from pending to posted, WalletFeed updates the same row.

For a refund or a payment, WalletFeed adds a new row with a value more than zero in **Amount**. For a declined charge, WalletFeed deletes the row. When Wallet removes a transaction, WalletFeed also deletes the row of that transaction.

## Send previous transactions

A new destination also receives previous transactions from the start date in **Settings** › **Sync** › [**Initial History**](/docs/send-history/). **Initial History** is **All** until you change it.

To send history from the screen of the destination, do these steps:

1. In **Destinations**, tap the Coda destination.
2. Tap **Send History**.
3. Tap **30 Days**, **90 Days**, **1 Year** or **All**.

While WalletFeed sends the history, it shows **Sending History**. WalletFeed does not add a second row for a transaction that is in the table.

## Change or remove the destination

In WalletFeed, you change the destination on its screen. To open this screen, you tap the Coda destination in **Destinations**.

To send only some transactions:

1. Set **Filter** to on.
2. Set **Include**, **Minimum**, **Include Pending**, **Accounts**, **Categories** or **Exclude**.

For more information, refer to [Choose what a destination receives](/docs/choose-what-to-send/).

To stop the destination for some time, set **Enabled** to off.

To use a new token:

1. Tap **Replace Token**.
2. Paste the new token.
3. Tap **Replace**. WalletFeed makes sure that the token can read the table and write to it.

To use a column that you make after you add the destination:

1. In Superhuman Docs, give the column a name from the table in Step 2.
2. In WalletFeed, tap **Send Test**. WalletFeed reads the columns again and adds a test row with the merchant WalletFeed.

You can delete the test row in Superhuman Docs.

You can change the name of a column after you add the destination. After the change, WalletFeed writes to the same column.

To remove the destination:

1. Tap **Delete**.
2. Tap **Delete** again. The rows that WalletFeed sent stay in the table.

To stop the token in Superhuman Docs:

1. On your computer, open **Account settings** › **API connections** in Superhuman Docs.
2. On the **WalletFeed** token, click **⋮**.
3. Click **Revoke**.

   ![The token menu, with Revoke.](https://walletfeed.app/guides/apple-card-to-coda/coda-token-revoke-menu.webp)

4. In **Revoke token?**, click **Revoke**. After this step, WalletFeed cannot send transactions to the table.

   ![The Revoke token dialog, with the Revoke button.](https://walletfeed.app/guides/apple-card-to-coda/coda-token-revoke-confirm.webp)

## If there is a problem

### If WalletFeed shows "Authentication failed"

Superhuman Docs does not let the token change your table. For example, the token has **Read only** in **Permission**, or you used **Revoke** on the token.

1. On your computer, open **Account settings** › **API connections** in Superhuman Docs. A **Read only** token shows **Read only - Content** below its name.

   ![A token in the API tokens list with the line Read only - Content.](https://walletfeed.app/guides/apple-card-to-coda/coda-T1-token-read-only.webp)

2. Make a new token with **Read and write**, as in [Step 3](#step-3-make-an-api-token-in-superhuman-docs).
3. On your iPhone, tap the Coda destination in **Destinations**.
4. Tap **Replace Token**.
5. Paste the new token in **API Token**.
6. Tap **Replace**.

### If WalletFeed shows "The token can't reach this doc. Use one without restrictions."

The token has **Selected content** in **Scopes**. With this token, WalletFeed cannot find your docs.

1. In Superhuman Docs, make a new token with **Content** and **All**, as in Step 3.
2. In WalletFeed, if the screen shows **Replace Token**, tap **Replace Token**.
3. Paste the new token in **API Token**.
4. Tap **Add** or **Replace**.

### If WalletFeed shows "Token rejected (HTTP 401). Check it and try again."

The token is not correct, or you used **Revoke** on it.

1. In Superhuman Docs, make a new token, as in Step 3.
2. Click **Copy** to copy the token. The dots in the dialog are not the token.
3. In WalletFeed, if the screen shows **Replace Token**, tap **Replace Token**.
4. Paste the new token in **API Token**.
5. Tap **Add** or **Replace**.

### If WalletFeed shows "No docs yet. Create one with a table, then come back."

WalletFeed cannot find a doc in your Superhuman Docs account.

1. In Superhuman Docs, make the doc and the table, as in Step 1 and Step 2.
2. In WalletFeed, tap the back button.
3. Tap **Coda** again.
4. Paste the token again.
5. Do steps 6 to 11 in [Step 4](#step-4-add-coda-in-walletfeed).

### If WalletFeed shows "This table needs a column named WalletFeed ID."

No column in the table has the name **WalletFeed ID** with the same letters and spaces.

1. In WalletFeed, make sure that **Table** shows **WalletFeed Transactions**.
2. In Superhuman Docs, change the name of the first column to `WalletFeed ID`.
3. In WalletFeed, tap **Add** again.

### If a column stays empty

The column name is not the same as a name in Step 2, or you added the column after you added the destination. WalletFeed also does not write to a column that has a formula.

1. In Superhuman Docs, correct the name of the column.
2. On your iPhone, tap the Coda destination in **Destinations**.
3. Tap **Send Test**. WalletFeed reads the columns again and adds a test row.

### If WalletFeed shows "Server error (503)"

Superhuman Docs did not add or change the rows in approximately 15 seconds. When WalletFeed sends data again, it also sends these rows.

1. To send the rows at this time, tap **Settings** (the gear button) at the top of **Destinations**.
2. Tap **Sync Now**.

### If Amount shows -23.4 and not -23.40

A **Number** column does not show a zero at the end of a value.

1. In Superhuman Docs, put the pointer on **Amount**.
2. Click the type button on the right side of the column name.
3. Click **Column type** › **Number** › **Currency**.

### If Table shows a table that you deleted

Superhuman Docs can keep the table of a deleted page in its list of tables.

1. In WalletFeed, tap **Table**.
2. Tap **WalletFeed Transactions**.
