+++
title = "Send Apple Card transactions to Notion"
nav_title = "Notion"
seo_title = "Apple Card to Notion: send transactions to a database"
description = "Send your Apple Card, Apple Cash and Savings transactions from your iPhone to a Notion database with WalletFeed, for a budget in Notion."
group = "Sheets and databases"
order = 30
related = ["guides/apple-card-to-airtable", "docs/destinations"]
updated = 2026-10-30
+++

WalletFeed sends your Apple Card, Apple Cash and Savings transactions from your iPhone to a database in Notion. You make a connection in Notion and share a page with it. WalletFeed then makes a database on that page and adds one row for each transaction. You can use this database for a budget in Notion.

## Before you start

- An iPhone with iOS 26 or a newer version. WalletFeed is available only in the US.
- Apple Card, Apple Cash or Savings in Wallet on that iPhone.
- WalletFeed, with [WalletFeed Pro](/docs/walletfeed-pro/). WalletFeed Pro is a subscription with a 1-week free trial, or a one-time Lifetime purchase.
- A Notion account. You must be a Workspace Owner in the workspace that receives your transactions, because only a Workspace Owner can make a connection.
- A computer with a web browser, for step 1 and step 2.

## Step 1: Make a connection in Notion

1. On your computer, open [Notion's Developer portal](https://app.notion.com/developers/connections).
2. Sign in to Notion.
3. In the **Build** section of the sidebar, click **Internal connections**.
4. Click **Create a new connection**.
5. Type a name for the connection, for example WalletFeed.
6. Select the workspace for your transactions.
7. Save the connection.
8. Open the **Configuration** tab of the connection.
9. In the content capabilities, select **Read content**, **Update content** and **Insert content**.
10. For user capabilities, select **No user information**. WalletFeed does not use user information or comments.

The **Configuration** tab also shows the **API token**. You copy the token on your iPhone in step 3.

## Step 2: Share a page with the connection

A new connection cannot open pages in Notion. WalletFeed makes its database on a page that you share with the connection.

> **Note:** When you share a page, the connection also gets access to all the child pages of that page. If you share a new page for WalletFeed, the connection cannot open your other pages.

1. In Notion, make a new page for your transactions, for example Budget.
2. In the Developer portal, open your connection.
3. Click the **Content access** tab.
4. Click **Edit access**.
5. Select the page that you made.
6. Save the change.

You can also share the page from Notion:

1. Open the page in Notion.
2. Click **•••** at the top right of the page.
3. Find **Connections** in the menu. If you cannot find it, click **More**.
4. Click **+ Add connection** or **Add connections**.
5. Type the name of your connection.
6. Select your connection.
7. If Notion shows a message about access to the child pages, accept the access.

## Step 3: Paste the token in WalletFeed

1. On your iPhone, open WalletFeed.
2. Tap **Destinations**.
3. Tap **+** at the top of the screen.

   ![The Destinations screen with no destinations, and the + button at the top.](app:docs-destinations-empty-pro)

4. In **Sheets & Databases**, tap **Notion**.

   ![The Add Destination list, with Notion in the Sheets & Databases section.](app:08-add-destination)

   If you do not have WalletFeed Pro, WalletFeed first shows the **WalletFeed Pro** screen. After you get WalletFeed Pro, WalletFeed shows the Notion screen.

5. Tap **Developer Portal**. Notion's Developer portal opens in your web browser.

   ![The Notion screen in WalletFeed, with the Token field, four steps and the Developer Portal link.](app:docs-setup-notion)

6. If Notion shows its sign-in page, sign in.
7. Tap **Internal connections**.
8. Tap your connection.
9. On the **Configuration** tab, copy the **API token**.
10. Open WalletFeed again.
11. Paste the token in **Token**. WalletFeed shows **Database** and **Page** below **Token**.

WalletFeed keeps the token in the Keychain on your iPhone.

## Step 4: Select the page and add Notion

1. Make sure that **Database** shows **New**.
2. In **Page**, select the page that you shared in step 2. WalletFeed shows "Adds a WalletFeed Transactions database to the page."
3. Tap **Add**. WalletFeed makes the **WalletFeed Transactions** database on the page.
4. On the message **Send Transactions to Notion?**, tap **Send**.

   The message tells you which data Notion receives, from which Wallet accounts and from which date. If you tap **Cancel**, WalletFeed removes the destination and sends nothing. The empty database stays on the page.

WalletFeed starts to send your transactions to the **WalletFeed Transactions** database.

> **Note:** **Database** also shows the databases that the connection can open and that have a text property with the name **WalletFeed ID**. If you select one of these databases, WalletFeed writes to it. WalletFeed fills each property that has the same name as a property in the next section.

## Properties in the database

WalletFeed makes the **WalletFeed Transactions** database with these properties. Each row is one transaction.

| Property | Type | Value |
| --- | --- | --- |
| **Merchant** | Title | The merchant name. If Wallet has no merchant name, the description. |
| **Date** | Date | The day of the transaction, in the time zone of your iPhone. |
| **Amount** | Number, in dollars | Less than zero for money out, for example a purchase. More than zero for money in, for example a payment or a refund. |
| **Currency** | Select | The currency code, for example USD. |
| **Category** | Select | The WalletFeed category, for example Groceries or Dining. |
| **Status** | Select | The status of the transaction in Wallet, for example pending or booked. |
| **Pending** | Checkbox | Selected while the charge is pending. |
| **Account** | Select | The name of the Wallet account, for example Apple Card. |
| **Description** | Text | The description of the transaction in Wallet. |
| **Type** | Select | The type of transaction in Wallet. |
| **MCC** | Number | The merchant category code. This number identifies the type of business. |
| **Foreign Amount** | Number | The amount in the currency of the merchant. It is less than zero for money out. It is empty for a purchase in dollars. |
| **Foreign Currency** | Select | The code of that currency. It is empty for a purchase in dollars. |
| **WalletFeed ID** | Text | The ID that WalletFeed uses to find the row again. |

WalletFeed writes only to these properties. You can add other properties to the database, and WalletFeed does not change them. WalletFeed finds each property by its name, and each row by its **WalletFeed ID**. Thus, these names and values must stay the same.

Your transactions go from your iPhone directly to Notion. WalletFeed has no account and no WalletFeed servers. After Notion receives your transactions, the terms of Notion are applicable to them.

## Sync times and changes

While WalletFeed is open, Notion receives changes in seconds. When WalletFeed is closed, iOS starts WalletFeed in approximately 1 hour or less after a change in Wallet. For this, [Background Sync](/docs/background-sync/) must be on in **Settings** › **Sync**.

A pending charge goes to Notion with **Pending** selected. When the charge posts, WalletFeed changes **Status** and **Pending** in the same row. A refund is a new row, with an **Amount** that is more than zero.

If a pending charge does not post, WalletFeed moves its row to the trash in Notion. WalletFeed also moves a row to the trash when Wallet removes the transaction. You can restore a row from the trash.

Notion has a limit on requests. Thus, WalletFeed sends not more than three requests each second, and a long history can be slow.

## Send previous transactions

A new destination also receives previous transactions, from the start date in **Settings** › **Sync** › **Initial History**. **Initial History** is **All** until you change it. To change it, do these steps before you add Notion:

1. In WalletFeed, tap **Settings** (the gear button) at the top of the screen.
2. In **Sync**, tap **Initial History**.
3. Select **Today**, **30 Days**, **90 Days**, **1 Year** or **All**.

   ![Settings, with Initial History set to All in the Sync section.](app:docs-settings)

To send more previous transactions to a Notion destination that you have, use [Send History](/docs/send-history/):

1. In **Destinations**, tap your Notion destination. Its name starts with Notion.
2. Tap **Send History**.
3. Select **30 Days**, **90 Days**, **1 Year** or **All**.

   ![A destination screen, here for Lunch Money, with Send History below Filter.](app:docs-destination-detail)

Rows that are already in the database do not show two times. WalletFeed finds them by **WalletFeed ID** and changes them. While WalletFeed sends the history, the destination shows **Sending History** and a progress bar. You can stop it with **Send History** › **Stop Sending**. When WalletFeed has sent all of the history, **History** shows **All sent**, or **Sent from** and the start date.

## Change or remove the destination

To change the destination, tap it in **Destinations**. On the destination screen, you can do these tasks:

| Task | On the destination screen |
| --- | --- |
| Stop for a time | Set **Enabled** to off. To start again, set **Enabled** to on. |
| Send only some transactions | Set **Filter** to on. Then set **Include**, **Minimum**, **Include Pending**, **Accounts**, **Categories** or **Exclude**. |
| Use a new token | Tap **Replace Token**. Paste the token. Tap **Replace**. WalletFeed makes sure that the token can read the database. |
| Make sure that WalletFeed can write | Tap **Send Test**. WalletFeed adds a sample row, with the merchant WalletFeed and the account Sample Card. |
| Remove the destination | Tap **Delete**. Tap **Delete** again. The rows that WalletFeed sent stay in Notion. |

If your iPhone can use Apple Intelligence and Apple Intelligence is on, you can also type a filter rule in words:

1. Set **Filter** to on.
2. In the field below **Filter**, type a rule, for example "Travel over $50, not Uber".
3. Tap **Create Rule**, the button with the Apple Intelligence symbol.

The connection in Notion stays after you remove the destination. To stop its access to your pages, disconnect the connection from the page in Notion.

## If something goes wrong

### If WalletFeed shows "Token rejected. Copy it again from the Developer portal."

Notion did not accept the token. For example, you did not copy all of the token.

1. On your iPhone, open [Notion's Developer portal](https://app.notion.com/developers/connections).
2. Open your connection.
3. On the **Configuration** tab, copy all of the **API token** again.
4. In WalletFeed, paste the token in **Token**.

### If WalletFeed tells you to share a page

The connection has no access to the page or the database. WalletFeed shows "Share a page with your connection, then try again." or "Share the page or database with your connection, then try again."

1. Share a page with the connection, as in [step 2](#step-2-share-a-page-with-the-connection).
2. In WalletFeed, tap **Try Again**.

### If WalletFeed shows "Give the connection read, update and insert content capabilities."

The connection does not have the three content capabilities that WalletFeed uses.

1. In the Developer portal, open your connection.
2. Open the **Configuration** tab.
3. Select **Read content**, **Update content** and **Insert content**.
4. In WalletFeed, tap **Try Again**.

### If WalletFeed shows "Notion is limiting requests. Try again in a minute."

Notion received too many requests from the connection in a short time.

1. Wait for one minute.
2. Tap **Try Again**.

### If the destination shows "Authentication failed"

Notion rejected the token. For example, a person removed the connection, or deselected one of its content capabilities.

1. On your iPhone, open [Notion's Developer portal](https://app.notion.com/developers/connections).
2. Open your connection.

   If you cannot find the connection, make a new one as in step 1. Then share the page with it as in step 2.

3. On the **Configuration** tab, make sure that the connection has **Read content**, **Update content** and **Insert content**.
4. Copy the **API token**.
5. In WalletFeed, tap **Destinations**.

   ![The Destinations list, where a destination with a problem shows Authentication failed.](app:docs-destinations-failure)

6. Tap your Notion destination.
7. Tap **Replace Token**.
8. Paste the token in **Token**.
9. Tap **Replace**.

On the Free plan of Notion, a workspace can get to its block limit. Then Notion can reject new rows, and WalletFeed shows "Authentication failed".

### If the destination shows "Rejected (HTTP 404)"

The connection cannot find the database. For example, a person disconnected the connection from the page.

1. Share the page with the connection again, as in [step 2](#step-2-share-a-page-with-the-connection).
2. In WalletFeed, open your Notion destination.
3. Tap **Send Test**.
