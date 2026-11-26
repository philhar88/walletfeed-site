+++
title = "Budgeting apps that support Apple Card and Apple Cash"
nav_title = "Budget apps for Apple Card"
seo_title = "Budgeting apps with Apple Card support (2026 list)"
description = "The budgeting apps that support Apple Card, Apple Cash and Savings on iPhone, from their help pages, and how WalletFeed sends transactions to other apps."
group = "Budgeting apps"
order = 5
related = ["guides/apple-card-plaid", "guides/export-apple-card-transactions", "guides/apple-card-to-ynab", "docs/destinations", "docs/walletfeed-pro", "guides/apple-card-rocket-money", "guides/apple-card-monarch", "guides/apple-card-copilot"]
updated = 2026-11-26
+++

These budgeting apps support Apple Card on iPhone: YNAB, Monarch, Copilot, PocketGuard, Rocket Money, Quicken Simplifi and Origin. The help pages of YNAB, Monarch, Copilot and PocketGuard also give Apple Cash and Savings. The Origin help pages also give Apple Cash.

Apple Card does not connect to an app with your login, as a bank does. An app can get your Apple Card transactions in three ways:

- The app reads Wallet on your iPhone.
- WalletFeed sends the transactions to the app from your iPhone.
- You import a file into the app.

## Apps that connect to Apple Card, Apple Cash and Savings

On November 26, 2026, the help pages of these apps gave these Wallet accounts. "Not stated" tells you that the help page does not give the account. You start each connection in the app on your iPhone.

| App | Apple Card | Apple Cash | Savings | Conditions on the help page |
| --- | --- | --- | --- | --- |
| [YNAB](https://support.ynab.com/en_us/apple-connections-rkShEfrUh) | Yes | Yes | Yes | iOS 17.4 or a newer version. YNAB then shows the transactions in its web app and its Android app. |
| [Monarch](https://help.monarch.com/hc/en-us/articles/24178098173076-Syncing-Your-Apple-Card-Cash-and-Savings) | Yes | Yes | Yes | The newest iOS version, and the Monarch app on an iPhone. |
| [Copilot](https://help.copilot.money/en/articles/9038131-apple-card-apple-cash-and-savings) | Yes | Yes | Yes | iOS 17.4 or a newer version. Copilot then shows the accounts in its Mac app and its iPad app. |
| [PocketGuard](https://pocketguard.com/help/how-to-link-your-apple-card-apple-cash-and-or-savings-with-pocketguard/) | Yes | Yes | Yes | iOS 17.4 or a newer version, and **Background App Refresh** for PocketGuard. |
| [Rocket Money](https://help.rocketmoney.com/en/articles/11504643-important-changes-to-apple-card-integration) | Yes | Not stated | Not stated | iOS 17.4 or a newer version. The connection goes through Plaid. |
| [Quicken Simplifi](https://support.simplifi.quicken.com/en/articles/9859332-how-to-add-your-apple-wallet-accounts) | Yes | Not stated | Not stated | The Quicken Simplifi app on an iPhone. Quicken Simplifi then shows the accounts in its web app. |
| [Origin](https://support.useorigin.com/hc/en-us/articles/34524826040461-How-do-I-remove-my-Apple-Card-or-Apple-Cash-connection) | Yes | Yes | Not stated | The device that made the connection, and **All Available Activity** in the Wallet settings for Origin. |

The Quicken Simplifi page gives "Apple Wallet accounts, including your Apple Card".

Apple gives Wallet transactions to iPhone apps through FinanceKit, its software for financial apps. Apple's [FinanceKit page](https://developer.apple.com/financekit/) for software developers gives these conditions for the US:

- An iPhone with iOS 17.4 or a newer version
- Apple Card, but not for a participant in Apple Card Family
- Apple Cash, but not for a child in Apple Cash Family
- Savings.

[Does Plaid support Apple Card?](/guides/apple-card-plaid/) tells you how these connections operate, and gives the steps for Rocket Money.

## Apps that do not connect to Apple Card

On November 26, 2026, the help pages of these apps gave these statements:

| App | Statement on the help page | Files that the app can import |
| --- | --- | --- |
| [Tiller](https://help.tiller.com/en/articles/432693-tiller-supported-financial-institutions-and-accounts) | "The connection to Apple Card is not supported by our data provider." | A [CSV file](https://help.tiller.com/en/articles/12159768-automatically-import-bank-csvs-into-tiller), in the Tiller Console |
| [EveryDollar](https://everydollar.help.ramseysolutions.com/hc/en-us/articles/360038329931-Bank-Status-Page) | "EveryDollar currently does not support a connection with Apple Card." | [No files](https://everydollar.help.ramseysolutions.com/hc/en-us/articles/360037960692-Importing-Bank-Statements) |

The Tiller page gives a procedure for Apple Card. You add a manual account in the Tiller Console. Then you import a CSV file from Wallet.

## Apps that WalletFeed sends Apple Card to

WalletFeed reads your Apple Card, Apple Cash and Savings transactions from Wallet on your iPhone. With [WalletFeed Pro](/docs/walletfeed-pro/), WalletFeed sends each new or changed transaction to a [destination](/docs/destinations/). Each guide gives the steps:

| Type | Destinations |
| --- | --- |
| Budget apps | [YNAB](/guides/apple-card-to-ynab/), [Lunch Money](/guides/apple-card-to-lunch-money/), [PocketSmith](/guides/apple-card-to-pocketsmith/), [Toshl Finance](/guides/apple-card-to-toshl/), [Firefly III](/guides/apple-card-to-firefly-iii/), [Sure](/guides/apple-card-to-sure/), [Wallet by BudgetBakers](/guides/apple-card-to-budgetbakers/) |
| Accounts software | [QuickBooks Online](/guides/apple-card-to-quickbooks/), [Xero](/guides/apple-card-to-xero/) |
| Spreadsheets | [Google Sheets](/guides/apple-card-to-google-sheets/), [Airtable](/guides/apple-card-to-airtable/), [Notion](/guides/apple-card-to-notion/), [Coda](/guides/apple-card-to-coda/) |
| Automations | [Zapier](/guides/apple-card-to-zapier/), [Make](/guides/apple-card-to-make/), a [webhook](/guides/apple-card-to-webhook/) |

WalletFeed is available only in the US, for an iPhone with iOS 26 or a newer version. WalletFeed has no account, and no WalletFeed server keeps your transactions.

## Apps that import a file

Some apps cannot connect to Apple Card, but they can import a file. WalletFeed writes your transactions to a file in a folder that you select, and updates the file.

| App | File | Guide |
| --- | --- | --- |
| Quicken for Mac | OFX | [Import Apple Card transactions into Quicken](/guides/apple-card-to-quicken/) |
| Quicken for Windows | CSV | [Import Apple Card transactions into Quicken for Windows](/guides/apple-card-to-quicken-for-windows/) |
| Actual Budget | OFX | [Actual Budget](/guides/apple-card-to-actual-budget/) |
| GnuCash | OFX or QIF | [GnuCash](/guides/apple-card-to-gnucash/) |
| Excel or Numbers | CSV | [Excel](/guides/apple-card-to-excel/), [Numbers](/guides/apple-card-to-numbers/) |

Wallet can also make an export file for a statement or a period. [Make an export file of your Apple Card transactions](/guides/export-apple-card-transactions/) gives the steps.

## The summary in Wallet

Wallet shows a summary of your Apple Card transactions for a week, a month or a year. Apple's page [See your Apple Card spending history](https://support.apple.com/en-us/102329) gives the steps.

## If your app is not in these lists

1. In the help pages of your app, find "Apple Card".
2. If the app cannot connect, find the file formats that the app can import.
3. If the app can import a CSV, OFX or QIF file, add that file as a destination in WalletFeed.
