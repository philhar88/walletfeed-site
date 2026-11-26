+++
title = "Link Apple Card to Rocket Money"
nav_title = "Rocket Money"
seo_title = "Link Apple Card to Rocket Money: steps and checks"
description = "Rocket Money can link to Apple Card in its iPhone app, on iOS 17.4 or newer. The steps to link it, and what to look at if Apple Card does not connect."
group = "Budgeting apps"
order = 84
related = ["guides/apple-card-plaid", "guides/apple-card-budget-apps", "guides/apple-card-monarch", "guides/apple-card-copilot", "guides/find-apple-card-subscriptions"]
updated = 2026-11-26
+++

Rocket Money connects to your Apple Card in its app for iPhone, through Plaid. An iPhone with iOS 17.4 or a newer version is necessary. After you connect, Rocket Money gets your Apple Card transactions, and a statement file each month is not necessary.

The steps on this page come from the Rocket Money help center article [Important changes to Apple Card integration](https://help.rocketmoney.com/en/articles/11504643-important-changes-to-apple-card-integration). The article has the date September 22, 2026.

## Before you start

You must have these items:

- An iPhone with iOS 17.4 or a newer version
- The newest version of the Rocket Money app
- Your Apple Card in Wallet on that iPhone.

## Connect your Apple Card in Rocket Money

1. On your iPhone, update Rocket Money to the newest version.
2. Open Rocket Money.
3. If Rocket Money has your Apple Card from statement files, update the connection when Rocket Money tells you.

   Rocket Money shows this message on the dashboard and on the **Linked Accounts** page.

4. If Rocket Money does not have your Apple Card, add a new account.
5. In the institution search, select **Apple**.

   Result: The Plaid steps start.

6. Do the steps that Plaid shows.

   In these steps, you give Rocket Money access to your Wallet accounts.

7. On your iPhone, open **Settings** › **Apps** › **Rocket Money** › **Wallet**.
8. Make sure that each account that you want in Rocket Money shows **All Available Activity**.

After you complete the Plaid steps, Plaid processes your data. Then Rocket Money shows your Apple Card transactions. The **Linked Accounts** page shows the new connection.

## The earlier upload of statement files

Before this connection, you gave Rocket Money a CSV file of each monthly statement. The article gives these facts about the change:

- With the connection through Plaid, a CSV file each month is not necessary.
- The transactions from your CSV files stay in Rocket Money.
- The connection gets the transactions that came after your last CSV file.

For an iPhone with iOS 17.3 or an earlier version, Rocket Money has a second article, [Adding your Apple Card statements](https://help.rocketmoney.com/en/articles/4470451-adding-your-apple-card-statements). This article also has the date September 22, 2026. It gives the procedure for statement files.

### Add a statement file on iOS 17.3 or an earlier version

1. In Rocket Money on your iPhone, tap the Settings icon in the upper left corner.
2. Tap **Linked Accounts**.
3. Tap **Add institution**.
4. In the search field, type `Apple Card`.

   Rocket Money shows a video of the subsequent steps.

5. Open Wallet.
6. Tap the balance of your Apple Card.
7. Scroll down to the statements.
8. Tap the statement that you want in Rocket Money.
9. Tap **Export Transactions**.
10. Tap **Comma Separated Values (CSV)**.
11. Tap the **Share** icon in the top right corner.
12. Tap **Rocket Money**.

    If the list does not show Rocket Money, scroll the list. Then tap **More**.

Result: Rocket Money opens and shows your Apple Card transactions.

The article gives these limits for statement files:

- You can add a statement file only from an iPhone. The procedure is not available on the Rocket Money website.
- You must do the procedure again each month for the new statement.
- Rocket Money does not show the balance of your Apple Card.
- The procedure is for Apple Card only. It is not available for Apple Savings.

## Apple Cash and Savings

The article about the connection gives only Apple Card by name. It also refers to "an additional Apple finance account", but it does not give the name of that account.

For an account of this type, the article tells you to add the account in **Settings** before you connect in Rocket Money.

## If Apple Card does not connect to Rocket Money

Rocket Money gets your Apple Card data directly from your iPhone. Thus, the settings on your iPhone change the data that Rocket Money shows. If you remove the access to an account in **Settings**, Rocket Money cannot process the transactions of that account through Plaid.

1. Make sure that your iPhone has iOS 17.4 or a newer version.
2. Update Rocket Money to the newest version.
3. On your iPhone, open **Settings** › **Apps** › **Rocket Money** › **Wallet**.
4. Make sure that each account that you want in Rocket Money shows **All Available Activity**.
5. If Rocket Money does not show your transactions after these steps, refer to the [Rocket Money help center](https://help.rocketmoney.com/en/).

If your iPhone has iOS 17.3 or an earlier version, Rocket Money cannot connect to your Apple Card. [Add a statement file](#add-a-statement-file-on-ios-173-or-an-earlier-version) gives the procedure for that iPhone.

## Keep a copy of your transactions in a file or a spreadsheet

WalletFeed is a different app for iPhone. It reads your Apple Card, Apple Cash and Savings transactions from Wallet on your iPhone. WalletFeed does not send transactions to Rocket Money. If you also want your transactions in a file or a spreadsheet, WalletFeed can make one:

- [Export CSV](/docs/export-csv/) makes one CSV file of a period that you select. WalletFeed Pro is not necessary for this file.
- A [CSV file destination](/guides/apple-card-to-csv/) writes a CSV file in a folder that you select. WalletFeed updates the file when your transactions change.
- A [Google Sheets destination](/guides/apple-card-to-google-sheets/) makes a spreadsheet in your Google Drive. WalletFeed updates the spreadsheet when your transactions change.

[WalletFeed Pro](/docs/walletfeed-pro/) is necessary for a destination. WalletFeed Pro is a subscription with a 1-week free trial, or a one-time Lifetime purchase.

WalletFeed is available only in the US, for an iPhone with iOS 26 or a newer version. WalletFeed has no account, and no WalletFeed server keeps your transactions.
