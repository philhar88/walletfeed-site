+++
title = "Put Apple Card transactions in an app that uses Plaid"
nav_title = "Apps that use Plaid"
seo_title = "Apple Card and Plaid: connect Apple Card to your app"
description = "You can connect your Apple Card to Plaid only in an iPhone app that reads Wallet. For a different app, use an export file from Wallet or WalletFeed."
group = "Budgeting apps"
order = 70
related = ["guides/export-apple-card-transactions", "guides/apple-card-to-ynab", "docs/destinations"]
updated = 2026-10-31
+++

You can connect your Apple Card to Plaid only in an iPhone app that reads your Apple Card transactions from Wallet. If your app cannot connect to Apple Card, you can put your transactions in the app with an export file from Wallet or with WalletFeed.

## Apple Card in Plaid

In its documents for software developers, Plaid gives "Apple Card" as a financial institution. Plaid gets your Apple Card transactions from an iPhone app. The app reads the transactions from Wallet on your iPhone with FinanceKit, Apple's software for financial apps. Then Plaid receives the transactions from the app.

Plaid added FinanceKit to its software kit for iPhone apps in version 6.0.0, on November 14, 2024. On March 12, 2026, Plaid gave the FinanceKit functions of version 6 the status "deprecated". In version 7.0.0, on June 9, 2026, Plaid moved FinanceKit to a new part of the kit, `PlaidFinanceKit`.

An iPhone with iOS 17.4 or a newer version is necessary for FinanceKit.

Thus, a website, a desktop app or an Android app cannot connect your Apple Card to Plaid. An iPhone app can connect your Apple Card only if its developer added this connection.

> **Note:** An Apple Newsroom article from January 7, 2026, tells you that Chase will become the new issuer of your Apple Card. The article gives the time of the change as "approximately 24 months". During the change, you can use your card as usual.

## Apps that read your Apple Card from Wallet

These services connect to your Apple Card in their iPhone apps. Their help pages give the steps:

| App | Wallet accounts on the help page | Connection |
| --- | --- | --- |
| [Rocket Money](https://help.rocketmoney.com/en/articles/11504643-important-changes-to-apple-card-integration) | Apple Card | Through Plaid, in the Rocket Money app for iPhone |
| [YNAB](https://support.ynab.com/en_us/apple-connections-rkShEfrUh) | Apple Card, Apple Cash and Savings | In the YNAB app for iPhone |
| [Monarch](https://help.monarch.com/hc/en-us/articles/24178098173076-Syncing-Your-Apple-Card-Cash-and-Savings) | Apple Card, Apple Cash and Savings | In the Monarch app for iPhone |
| [Copilot](https://help.copilot.money/en/articles/9038131-apple-card-apple-cash-and-savings) | Apple Card, Apple Cash and Savings | In the Copilot app for iPhone |

On September 22, 2026, the Rocket Money help center gave these conditions for the connection through Plaid:

- An iPhone with iOS 17.4 or a newer version
- The newest version of the Rocket Money app
- **All Available Activity** for each Wallet account that you send through Plaid, in **Settings** › **Apps** › **Rocket Money** › **Wallet**.

After the iPhone app connects, some services also show your transactions on other devices. For example, YNAB shows them in its web app and in its Android app. The transactions come from the iPhone that made the connection. The [YNAB guide](/guides/apple-card-to-ynab/) gives the steps for YNAB.

## Apple Cash and Savings

Plaid's documents give a financial institution for Apple Card. The Rocket Money help page gives only Apple Card. The help pages of YNAB, Monarch and Copilot give Apple Card, Apple Cash and Savings.

For your Apple Cash or Savings account, refer to the help pages of your app.

## Use an export file from Wallet

In Wallet, **Export Transactions** makes a file with the transactions of a monthly statement, or of a period between two dates. If your app can import files, you can then import the file into the app. The file does not change after Wallet makes it.

[Make an export file of your Apple Card transactions](/guides/export-apple-card-transactions/) gives the steps.

## Send your transactions with WalletFeed

WalletFeed reads your Apple Card, Apple Cash and Savings transactions from Wallet on your iPhone. With WalletFeed Pro, WalletFeed sends the transactions to a [destination](/docs/destinations/). When your transactions change, WalletFeed updates the destination.

You must have these items:

- An iPhone with iOS 26 or a newer version
- WalletFeed, with [access to your Wallet accounts](/docs/wallet-accounts/)
- [WalletFeed Pro](/docs/walletfeed-pro/), a subscription with a 1-week free trial, or a one-time Lifetime purchase.

WalletFeed is available only in the US. WalletFeed Pro is not necessary for [Export CSV](/docs/export-csv/), which makes one CSV file of your transactions.

WalletFeed has no account and no WalletFeed servers. Your transactions go from your iPhone directly to the folder or the service that you select.

Some of the destinations are:

- Budget apps, for example [Lunch Money](/guides/apple-card-to-lunch-money/), [PocketSmith](/guides/apple-card-to-pocketsmith/), [Toshl Finance](/guides/apple-card-to-toshl/), [Firefly III](/guides/apple-card-to-firefly-iii/) or [Sure](/guides/apple-card-to-sure/)
- Spreadsheets and databases, for example [Google Sheets](/guides/apple-card-to-google-sheets/), [Airtable](/guides/apple-card-to-airtable/), [Notion](/guides/apple-card-to-notion/) or [Coda](/guides/apple-card-to-coda/)
- [CSV](/guides/apple-card-to-csv/), [OFX](/guides/apple-card-to-ofx/) or [QIF](/guides/apple-card-to-qif/) files for an app that imports files, for example [YNAB](/guides/apple-card-to-ynab/), [Quicken](/guides/apple-card-to-quicken/), [Actual Budget](/guides/apple-card-to-actual-budget/), [GnuCash](/guides/apple-card-to-gnucash/) or [QuickBooks Online](/guides/apple-card-to-quickbooks/)
- Automations, for example [Zapier](/guides/apple-card-to-zapier/), [Make](/guides/apple-card-to-make/) or a [webhook](/guides/apple-card-to-webhook/).

To add a destination:

1. On your iPhone, open WalletFeed.
2. Tap **Destinations**.
3. Tap **+** at the top of the screen.

   ![The Destinations screen with no destinations and the + button at the top.](app:docs-destinations-empty-pro)

4. In the **Destinations** search field, type the name of the destination, for example `Lunch Money` or `OFX`.

   ![The Add Destination screen with the Destinations search field above the Budgeting list.](app:08-add-destination)

5. Tap the destination.

   If you do not have WalletFeed Pro, the **WalletFeed Pro** screen opens. After you get WalletFeed Pro, the form for the destination opens.

6. Do the steps in the guide for the destination.

## If there is a problem

### If your app does not find Apple Card

The app cannot connect to Apple Card on this device, or this version of the app cannot connect. FinanceKit also does not give the Apple Card transactions of a participant in Apple Card Family.

1. Open the app on your iPhone.
2. Make sure that your iPhone has iOS 17.4 or a newer version.
3. Update the app to the newest version.
4. Find Apple Card again in the app.
5. If the app does not find Apple Card, refer to the help pages of the app.
6. If the app cannot connect to Apple Card, use [an export file from Wallet](#use-an-export-file-from-wallet) or [WalletFeed](#send-your-transactions-with-walletfeed).

### If WalletFeed has no destination for your app

It is possible that your app can import a CSV, OFX or QIF file from WalletFeed.

1. In the help pages of your app, find the file formats that the app can import.
2. If the app can import a CSV file, use **Export CSV** or a **CSV File** destination.
3. If the app can import an OFX or a QIF file, add an **OFX File** or a **QIF File** destination.
