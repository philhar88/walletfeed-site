# Send Apple Card transactions to Notion

WalletFeed sends your Apple Card, Apple Cash and Savings transactions from your iPhone to a database in Notion. You make a connection in Notion and give it access to a page, and then WalletFeed makes the database on that page.

## Before you start

You must have these items:

- An iPhone with iOS 26 or a newer version. WalletFeed is available only in the US.
- Apple Card, Apple Cash or Savings in Wallet on that iPhone.
- WalletFeed, with [WalletFeed Pro](/docs/walletfeed-pro/). WalletFeed Pro is a subscription with a 1-week free trial, or a one-time Lifetime purchase.
- A Notion account. You must be a Workspace Owner in the workspace that receives your transactions, because only a Workspace Owner can make a connection.
- A computer with a web browser for step 1 and step 2.

## Step 1: Make a connection in Notion

1. On your computer, open [Notion's Developer portal](https://app.notion.com/developers/connections).
2. If Notion shows the **Log in** page, get access to your Notion account.
3. In the **Build** section of the sidebar, click **Internal connections**.
4. Click **Create a new connection**.
5. Type a name for the connection, for example WalletFeed.
6. Select the workspace for your transactions.
7. Save the connection.
8. Open the **Configuration** tab of the connection.
9. In the content capabilities, select **Read content**, **Update content** and **Insert content**.
10. For user capabilities, select **No user information** (WalletFeed does not use user information or comments).

The **Configuration** tab also shows the **API token**. You will copy the token on your iPhone in step 3.

## Step 2: Give the connection access to a page

A new connection cannot open pages in Notion. WalletFeed makes its database on a page that the connection can open.

> **Note:** If you give the connection access to a page, the connection also gets access to all the child pages of that page. If the connection has access only to a new page for WalletFeed, the connection cannot open your other pages.

1. In Notion, make a new page for your transactions, for example Budget.
2. In the Developer portal, open your connection.
3. Click the **Content access** tab.
4. Click **Edit access**.
5. Select the page that you made.
6. Save the change.

You can also give the connection access from the page in Notion:

1. Open the page in Notion.
2. Click **•••** at the top right of the page.
3. If the menu does not show **Connections**, click **More**.
4. Click **Connections**.
5. Click **+ Add connection** or **Add connections**.
6. Type the name of your connection.
7. Select your connection.
8. If Notion shows a message about access to the child pages, accept the access.

## Step 3: Paste the token in WalletFeed

1. On your iPhone, open WalletFeed.
2. Tap **Destinations**.
3. Tap **+** at the top of the screen.

   ![The Destinations screen with no destinations, and the + button at the top.](https://walletfeed.app/guides/apple-card-to-notion/walletfeed-destinations-empty-pro.webp)

4. In **Sheets & Databases**, tap **Notion**.

   ![The Add Destination list, with Notion in the Sheets & Databases section.](https://walletfeed.app/guides/apple-card-to-notion/walletfeed-add-destination.webp)

   If you do not have WalletFeed Pro, WalletFeed shows the **WalletFeed Pro** screen. After you get WalletFeed Pro, WalletFeed shows the Notion screen.

5. Tap **Developer Portal**. Notion's Developer portal opens in your web browser.

   ![The Notion screen in WalletFeed, with the Token field, four steps and the Developer Portal link.](https://walletfeed.app/guides/apple-card-to-notion/walletfeed-setup-notion.webp)

6. If Notion shows the **Log in** page, get access to your Notion account.
7. Tap **Internal connections**.
8. Tap your connection.
9. On the **Configuration** tab, copy the **API token**.
10. Open WalletFeed again.
11. Paste the token in **Token**. WalletFeed shows **Database** and **Page** below **Token**.

WalletFeed keeps the token in the Keychain on your iPhone.

## Step 4: Select the page and add Notion

1. Make sure that **Database** shows **New**.
2. In **Page**, select the page from step 2. WalletFeed shows "Adds a WalletFeed Transactions database to the page."
3. Tap **Add**. WalletFeed makes the **WalletFeed Transactions** database on the page.
4. On the message **Send Transactions to Notion?**, tap **Send**.

   The message tells you the data that Notion will receive, the Wallet accounts and the start date. If you tap **Cancel**, WalletFeed removes the destination and sends nothing. The empty database stays on the page.

WalletFeed starts to send your transactions to the **WalletFeed Transactions** database.

> **Note:** **Database** also shows the databases that the connection can open and that have a text property with the name **WalletFeed ID**. If you select one of these databases, WalletFeed writes to the properties with a name from **WalletFeed Transactions** and a type that can contain the value.

## Properties in the database

WalletFeed makes the **WalletFeed Transactions** database with these properties. Each row is one transaction.

| Property | Type | Value |
| --- | --- | --- |
| **Merchant** | Title | The merchant name. If Wallet has no merchant name, WalletFeed uses the description. |
| **Date** | Date | The day of the transaction, in the time zone of your iPhone. |
| **Amount** | Number, in dollars | Less than zero for money out (for example, a purchase). More than zero for money in (for example, a payment or a refund). |
| **Currency** | Select | The currency code, for example USD. |
| **Category** | Select | The WalletFeed category, for example Groceries or Travel. |
| **Status** | Select | The status of the transaction in Wallet, for example pending or booked. |
| **Pending** | Checkbox | WalletFeed selects this checkbox while the charge is pending. |
| **Account** | Select | The name of the Wallet account, for example Apple Card. |
| **Description** | Text | The description of the transaction in Wallet. |
| **Type** | Select | The transaction type in Wallet. |
| **MCC** | Number | The merchant category code. This number identifies the type of merchant. |
| **Foreign Amount** | Number | The amount in the merchant's currency. It is less than zero when **Amount** is less than zero. It is empty for a purchase in dollars. |
| **Foreign Currency** | Select | The code of that currency. It is empty for a purchase in dollars. |
| **WalletFeed ID** | Text | The ID that WalletFeed uses to find the row again. |

WalletFeed writes only to these properties. You can add other properties to the database, and WalletFeed does not change them. WalletFeed finds each property by its name and each row by its **WalletFeed ID**. Thus, the names of these properties and the **WalletFeed ID** values must stay the same.

Your transactions go from your iPhone directly to Notion. WalletFeed has no account and no WalletFeed servers. After Notion receives your transactions, the terms of Notion are applicable to them.

## New and changed transactions

While WalletFeed is open, Notion receives changes in seconds. When WalletFeed is not open, iOS starts WalletFeed approximately 1 hour or less after a change in Wallet. If [Background Sync](/docs/background-sync/) is on in **Settings** › **Sync**, WalletFeed then sends the change.

WalletFeed sends a pending charge to Notion and selects **Pending**. When Wallet changes the status of the charge to booked, WalletFeed updates **Status** and **Pending** in the same row. A refund is a new row with an **Amount** of more than zero.

If Wallet changes the status of a pending charge to rejected, WalletFeed moves its row to the trash in Notion. WalletFeed also moves a row to the trash when Wallet removes the transaction. In Notion, you can move a row from the trash to the database again.

Notion has a limit on requests. Thus, WalletFeed sends not more than 3 requests each second. As a result, WalletFeed can be slow to send a long history.

## Send previous transactions

A new destination also receives previous transactions from the start date in **Settings** › **Sync** › **Initial History**. **Initial History** is **All** until you change it. To change **Initial History**, do these steps before you add Notion:

1. In WalletFeed, tap **Settings** (the gear button) at the top of the screen.
2. In **Sync**, tap **Initial History**.
3. Select **Today**, **30 Days**, **90 Days**, **1 Year** or **All**.

   ![The Settings screen, with Initial History set to All in the Sync section.](https://walletfeed.app/guides/apple-card-to-notion/walletfeed-settings.webp)

To send more previous transactions to your Notion destination, use [Send History](/docs/send-history/):

1. In **Destinations**, tap the Notion destination.
2. Tap **Send History**.
3. Select **30 Days**, **90 Days**, **1 Year** or **All**.

   ![The destination screen for Lunch Money, with Send History below Filter.](https://walletfeed.app/guides/apple-card-to-notion/walletfeed-destination-detail.webp)

If the database has a row for a transaction, WalletFeed does not add a second row. WalletFeed finds that row by its **WalletFeed ID** and updates it.

While WalletFeed sends the history, the destination screen shows **Sending History** and a progress bar. If you tap **Send History** › **Stop Sending**, WalletFeed stops before it sends all of the history. When WalletFeed completes the history, **History** shows **All sent**, or **Sent from** and the start date.

## Change or remove the destination

To change the destination, tap the Notion destination in **Destinations**. On the destination screen, you can do these tasks:

| Task | On the destination screen |
| --- | --- |
| Stop for a time | Set **Enabled** to off. To start again, set **Enabled** to on. |
| Send only some transactions | Set **Filter** to on. Then set **Include**, **Minimum**, **Include Pending**, **Accounts**, **Categories** or **Exclude**. |
| Use a new token | Tap **Replace Token**. Paste the new token. Tap **Replace**. WalletFeed makes sure that it can read the database with the new token. |
| Make sure that WalletFeed can write to the database | Tap **Send Test**. WalletFeed adds a test row with the merchant "WalletFeed" and the account "Sample Card". |
| Remove the destination | Tap **Delete**. Tap **Delete** again. The rows that WalletFeed sent stay in Notion. |

If Apple Intelligence is active on your iPhone, you can also type a filter rule in words:

1. Set **Filter** to on.
2. In the field below **Filter**, type a rule, for example "Travel over $50, not Uber".
3. Tap the Apple Intelligence icon at the end of the field.

If you remove the destination, the connection in Notion stays. You can disconnect the connection from the page in Notion. Then the connection cannot open the page.

## If there is a problem

### If WalletFeed shows "Token rejected. Copy it again from the Developer portal."

Notion did not accept the token. For example, you did not copy all of the token.

1. On your iPhone, open [Notion's Developer portal](https://app.notion.com/developers/connections).
2. Tap **Internal connections**.
3. Tap your connection.
4. On the **Configuration** tab, copy all of the **API token** again.
5. In WalletFeed, paste the token in **Token**.

### If WalletFeed tells you to give the connection access to a page

The connection has no access to the page or the database. WalletFeed shows "Share a page with your connection, then try again." or "Share the page or database with your connection, then try again."

1. Give the connection access to a page (refer to [step 2](#step-2-give-the-connection-access-to-a-page)).
2. In WalletFeed, tap **Try Again**.

### If WalletFeed shows "Give the connection read, update and insert content capabilities."

The connection does not have the three content capabilities that WalletFeed uses.

1. On your iPhone, open [Notion's Developer portal](https://app.notion.com/developers/connections).
2. Tap **Internal connections**.
3. Tap your connection.
4. On the **Configuration** tab, select **Read content**, **Update content** and **Insert content**.
5. In WalletFeed, tap **Try Again**.

### If WalletFeed shows "Notion is limiting requests. Try again in a minute."

Notion has a limit on requests, and the connection got to this limit.

1. Wait for 1 minute.
2. In WalletFeed, tap **Try Again**.

### If the destination shows "Authentication failed"

Notion rejected the token. For example, a person removed the connection or deselected one of its content capabilities.

1. On your iPhone, open [Notion's Developer portal](https://app.notion.com/developers/connections).
2. Tap **Internal connections**.
3. Tap your connection.

   If you cannot find the connection, make a new connection (refer to [step 1](#step-1-make-a-connection-in-notion)). Then give the new connection access to the page (refer to [step 2](#step-2-give-the-connection-access-to-a-page)).

4. On the **Configuration** tab, make sure that the connection has **Read content**, **Update content** and **Insert content**.
5. Copy the **API token**.
6. In WalletFeed, tap **Destinations**.

   ![The Destinations list, with a destination that shows Authentication failed.](https://walletfeed.app/guides/apple-card-to-notion/walletfeed-destinations-failure.webp)

7. Tap the Notion destination.
8. Tap **Replace Token**.
9. Paste the token in **Token**.
10. Tap **Replace**.

A Notion workspace on the Free plan with more than one member has a limit of 1,000 blocks. Each row in the database is a block. After the workspace gets to this limit, Notion does not accept new rows. Then WalletFeed shows "Authentication failed".

### If the destination shows "Rejected (HTTP 404)"

The connection cannot find the database. For example, a person disconnected the connection from the page.

1. Give the connection access to the page again (refer to [step 2](#step-2-give-the-connection-access-to-a-page)).
2. In WalletFeed, tap **Destinations**.
3. Tap the Notion destination.
4. Tap **Send Test**.
