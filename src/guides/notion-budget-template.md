+++
title = "Apple Card budget template for Notion"
nav_title = "Notion template"
description = "A Notion template with a WalletFeed Transactions database and views of your Apple Card spending by month and by category. WalletFeed sends the rows."
group = "Sheets and databases"
order = 35
related = ["guides/apple-card-to-notion", "docs/destinations"]
updated = 2026-11-11
+++

The WalletFeed budget template for Notion shows your Apple Card spending by month and by category. You copy the template page to your Notion workspace. Then WalletFeed sends your transactions to the database on that page.

## Before you start

You must have these items:

- An iPhone with iOS 26 or a newer version. WalletFeed is available only in the US.
- Apple Card, Apple Cash or Savings in Wallet on that iPhone.
- WalletFeed, with [WalletFeed Pro](/docs/walletfeed-pro/). WalletFeed Pro is a subscription with a 1-week free trial, or a one-time Lifetime purchase.
- A Notion account.

> **Note:** A Notion workspace on the Free plan with more than one member has a limit of 1,000 blocks. Each row in the database is one block.

## Step 1: Copy the template to your workspace

1. In a web browser, open the [WalletFeed budget template](https://upbeat-judo-c67.notion.site/WalletFeed-Budget-Template-4155382d8124819d92f4f6b263c4f4a3).
2. At the top right of the page, click the Duplicate icon (two squares).
3. If Notion shows **Log in to your Notion account**, get access to your Notion account.
4. If you have more than one workspace, select the workspace for your transactions.

   Result: Notion adds the **WalletFeed Budget Template** page to your workspace. The page has the **WalletFeed Transactions** database.

5. In the database, right-click **Sample: coffee shop**.
6. Click **Delete**.
7. Do steps 5 and 6 again for **Sample: grocery store**.

## Step 2: Connect WalletFeed to the page

1. On your iPhone, open WalletFeed.
2. Tap **Destinations**.
3. Tap **+** at the top of the screen.
4. In **Sheets & Databases**, tap **Notion**.

   If you do not have WalletFeed Pro, WalletFeed shows the **WalletFeed Pro** screen.

5. Tap **Sign In with Notion**.
6. If Notion shows **Log in to your Notion account**, get access to your Notion account.
7. If you have more than one workspace, select the workspace at the top right of the Notion page.
8. Tap **Select pages**.
9. Tap **Private**, or the teamspace that has the template page.
10. Select **WalletFeed Budget Template**.
11. Tap **Allow access**.

    Result: The Notion screen in WalletFeed shows **Signed In**. Then WalletFeed shows **Database** and **Page**.

For more information about the sign-in, refer to [Send Apple Card transactions to Notion](/guides/apple-card-to-notion/).

## Step 3: Add the database in WalletFeed

1. Make sure that **Database** shows **WalletFeed Transactions**.

   WalletFeed selects the **WalletFeed Transactions** database on the page that you selected. If you select **New**, WalletFeed makes a second database.

2. Tap **Add**.
3. On the message **Send Transactions to Notion?**, tap **Send**.

   Result: WalletFeed starts to send your transactions to the **WalletFeed Transactions** database.

A new destination also receives previous transactions, from the start date in **Settings** › **Sync** › **Initial History**. To send more, refer to [Send History](/docs/send-history/).

## Views in the template

| View | Rows |
| --- | --- |
| **All** | All the transactions, with the newest first |
| **By month** | Money out and refunds, in a group for each month |
| **By category** | Money out and refunds, in a group for each category |

In **By month** and **By category**, each group shows the **Sum** of **Amount**. These views show a row if its **Amount** is less than zero, or if its **Type** is `refund`. Thus, the sum is the money out, less refunds. The sum is less than zero, because money out is less than zero.

Other money into an account, for example a payment to your Apple Card, shows only in **All**.

The database has the same properties as the database that WalletFeed makes. For the list of properties, refer to [Properties in the database](/guides/apple-card-to-notion/#properties-in-the-database).

> **Caution:** Do not change the names of the properties or the **WalletFeed ID** values. WalletFeed finds each property by its name and each row by its **WalletFeed ID**.

You can add properties and views to the database. WalletFeed does not change them.

## If there is a problem

### If **Database** shows **New**

WalletFeed found no **WalletFeed Transactions** database on the pages that you selected. For example, you selected a different page on the Notion page.

1. On the Notion screen in WalletFeed, tap **Use Another Workspace**.
2. Tap **Select pages**.
3. Select **WalletFeed Budget Template**.
4. Tap **Allow access**.
