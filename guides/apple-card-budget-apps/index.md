# Budget apps that work with Apple Card

Apple Card does not connect to a budget app with your login, as a bank does. An app can get your Apple Card transactions in three ways:

- The app reads Wallet on your iPhone.
- WalletFeed sends the transactions to the app from your iPhone.
- You import a file into the app.

## Apps that read Apple Card on your iPhone

These services connect to your Apple Card in their iPhone apps. Their help pages give the steps:

| App | Wallet accounts on the help page |
| --- | --- |
| [YNAB](https://support.ynab.com/en_us/apple-connections-rkShEfrUh) | Apple Card, Apple Cash and Savings |
| [Monarch](https://help.monarch.com/hc/en-us/articles/24178098173076-Syncing-Your-Apple-Card-Cash-and-Savings) | Apple Card, Apple Cash and Savings |
| [Copilot](https://help.copilot.money/en/articles/9038131-apple-card-apple-cash-and-savings) | Apple Card, Apple Cash and Savings |
| [Rocket Money](https://help.rocketmoney.com/en/articles/11504643-important-changes-to-apple-card-integration) | Apple Card |

An iPhone with iOS 17.4 or a newer version is necessary. [Does Plaid support Apple Card?](/guides/apple-card-plaid/) tells you how these connections operate.

## Apps that WalletFeed sends Apple Card to

WalletFeed reads your Apple Card, Apple Cash and Savings transactions from Wallet on your iPhone. With [WalletFeed Pro](/docs/walletfeed-pro/), WalletFeed sends each new or changed transaction to a [destination](/docs/destinations/). Each guide gives the steps:

| Type | Destinations |
| --- | --- |
| Budget apps | [YNAB](/guides/apple-card-to-ynab/), [Lunch Money](/guides/apple-card-to-lunch-money/), [PocketSmith](/guides/apple-card-to-pocketsmith/), [Toshl Finance](/guides/apple-card-to-toshl/), [Firefly III](/guides/apple-card-to-firefly-iii/), [Sure](/guides/apple-card-to-sure/) |
| Accounts software | [QuickBooks Online](/guides/apple-card-to-quickbooks/) |
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

## If your app is not in these lists

1. In the help pages of your app, find "Apple Card".
2. If the app cannot connect, find the file formats that the app can import.
3. If the app can import a CSV, OFX or QIF file, add that file as a destination in WalletFeed.

[Download WalletFeed on the App Store](https://apps.apple.com/app/apple-store/id6827429675?pt=125538749&ct=site&mt=8)
