# Does Plaid support Apple Card? How to connect, and the apps that connect

Plaid supports Apple Card only in iPhone apps that added the connection. To connect your Apple Card to Plaid, you add the card in one of these apps on your iPhone. Plaid cannot connect to Apple Card with your login, as it does for a bank. Thus, a website, a desktop app or an Android app cannot connect your Apple Card through Plaid. Most budgeting apps use the connection with your login.

If your app cannot connect, WalletFeed can send the transactions. WalletFeed reads your Apple Card, Apple Cash and Savings transactions on your iPhone. Then it sends each new or changed transaction to your app, spreadsheet, server or webhook, also when WalletFeed is not open.

## Connect Apple Card to Plaid in an iPhone app

You start the connection in an iPhone app that uses Plaid. The app must have the Apple Card connection. For example, on September 22, 2026, the [Rocket Money help center](https://help.rocketmoney.com/en/articles/11504643-important-changes-to-apple-card-integration) gave these steps for the Rocket Money app:

1. Make sure that your iPhone has iOS 17.4 or a newer version.
2. Update the Rocket Money app to the newest version.
3. Open Rocket Money on your iPhone.
4. Start the connection of a new account.
5. In the institution search, select **Apple**.

   Result: Rocket Money shows the Plaid screens.

6. On your iPhone, open **Settings** › **Apps** › **Rocket Money** › **Wallet**.
7. Select **All Available Activity** for each Wallet account that you send through Plaid.
8. In Rocket Money, complete the Plaid screens.

   Result: After Plaid processes your data, Rocket Money shows your Apple Card transactions. The **Linked Accounts** page shows the new connection.

If Rocket Money has your Apple Card transactions from CSV files, Rocket Money shows a message to update the connection. The transactions from the CSV files stay in Rocket Money.

If you remove the access to a Wallet account in **Settings**, Rocket Money cannot get the transactions of that account through Plaid.

For a different app, refer to the help pages of that app.

## Apps that read your Apple Card from Wallet

On November 26, 2026, the help pages of these services gave a connection to Apple Card in their iPhone apps. The help pages give the steps:

| App | Wallet accounts on the help page | Connection |
| --- | --- | --- |
| [Rocket Money](https://help.rocketmoney.com/en/articles/11504643-important-changes-to-apple-card-integration) | Apple Card | Through Plaid, in the Rocket Money app for iPhone |
| [YNAB](https://support.ynab.com/en_us/apple-connections-rkShEfrUh) | Apple Card, Apple Cash and Savings | In the YNAB app for iPhone |
| [Monarch](https://help.monarch.com/hc/en-us/articles/24178098173076-Syncing-Your-Apple-Card-Cash-and-Savings) | Apple Card, Apple Cash and Savings | In the Monarch app for iPhone |
| [Copilot](https://help.copilot.money/en/articles/9038131-apple-card-apple-cash-and-savings) | Apple Card, Apple Cash and Savings | In the Copilot app for iPhone |
| [PocketGuard](https://pocketguard.com/help/how-to-link-your-apple-card-apple-cash-and-or-savings-with-pocketguard/) | Apple Card, Apple Cash and Savings | In the PocketGuard app for iPhone |
| [Quicken Simplifi](https://support.simplifi.quicken.com/en/articles/9859332-how-to-add-your-apple-wallet-accounts) | Apple Card | In the Quicken Simplifi app for iPhone |
| [Origin](https://support.useorigin.com/hc/en-us/articles/35772490810637-Apple-card-account-disconnected-or-missing-transactions-Here-s-how-to-fix-it) | Apple Card and Apple Cash | In the Origin app on your iPhone |

The Rocket Money page gives Plaid for this connection. The other pages do not give Plaid.

After the iPhone app connects, some services also show your transactions on other devices. For example, YNAB shows them in its web app and in its Android app. Quicken Simplifi shows the accounts in its web app. The transactions come from the iPhone that made the connection. The [YNAB guide](/guides/apple-card-to-ynab/) gives the steps for YNAB.

## Apps that do not connect to Apple Card

On November 26, 2026, the help pages of these services gave these statements:

| App | Statement on the help page |
| --- | --- |
| [Tiller](https://help.tiller.com/en/articles/432693-tiller-supported-financial-institutions-and-accounts) | "The connection to Apple Card is not supported by our data provider." |
| [EveryDollar](https://everydollar.help.ramseysolutions.com/hc/en-us/articles/360038329931-Bank-Status-Page) | "EveryDollar currently does not support a connection with Apple Card." |

[Budgeting apps that support Apple Card and Apple Cash](/guides/apple-card-budget-apps/) gives the files that these apps can import.

## Plaid, FinanceKit and Wallet

In its documents for software developers, Plaid gives "Apple Card" as a financial institution. Plaid gets your Apple Card transactions from an iPhone app. The app reads the transactions from Wallet on your iPhone with FinanceKit, Apple's software for financial apps. Then Plaid receives the transactions from the app.

Apple's [FinanceKit page](https://developer.apple.com/financekit/) for software developers gives these conditions for the US:

- An iPhone with iOS 17.4 or a newer version
- Apple Card, but not for a participant in Apple Card Family
- Apple Cash, but not for a child in Apple Cash Family
- Savings.

With FinanceKit, you select the accounts and the period that an app can read.

[Plaid's list of changes](https://plaid.com/docs/changelog/) gives FinanceKit in version 6.0.0 of its software kit for iPhone apps, on November 14, 2024. On March 12, 2026, Plaid gave the FinanceKit functions of version 6 the status "deprecated". In [version 7.0.0](https://github.com/plaid/plaid-link-ios/releases/tag/7.0.0), on June 9, 2026, Plaid moved FinanceKit to a new part of the kit, `PlaidFinanceKit`.

Thus, a website, a desktop app or an Android app cannot connect your Apple Card to Plaid. An iPhone app can connect your Apple Card only if its developer added this connection.

> **Note:** An Apple Newsroom article from January 7, 2026, tells you that Chase will become the new issuer of your Apple Card. The article gives the time of the change as "approximately 24 months". During the change, you can use your card as usual.

## Apple Cash and Savings

Plaid's documents give a financial institution for Apple Card. The Rocket Money and Quicken Simplifi help pages give only Apple Card. The help pages of YNAB, Monarch, Copilot and PocketGuard give Apple Card, Apple Cash and Savings. The Origin help pages give Apple Card and Apple Cash.

For your Apple Cash or Savings account, refer to the help pages of your app.

## A Plaid-like feed for Apple Card

This table compares a Plaid connection with WalletFeed.

| You get | A bank connection through Plaid | WalletFeed |
| --- | --- | --- |
| Each transaction with its own ID | Yes | Yes |
| A pending charge that changes when it posts | Yes | Yes, usually with the same ID |
| New transactions when you do not use the app | Yes | Yes, approximately 1 hour or less after a change, with [Background Sync](/docs/background-sync/) |
| The balance of each account | Yes | With **Balances** on a [webhook](/docs/webhooks/#balance-updated) |
| Where your transactions go | To Plaid, then to the app | From your iPhone directly to your destination |
| Your own server | With the Plaid API, after you sign up as a developer | With a [signed webhook](/guides/apple-card-to-webhook/), [AWS](/guides/apple-card-to-aws/) or [Supabase](/guides/apple-card-to-supabase/) |
| Apple Card | Only in iPhone apps that added it | Yes, and Apple Cash and Savings |

For software developers, [Send Apple Card transactions to your app or server](/guides/apple-card-api/) gives the JSON fields and the other destinations for your own code.

[Send your transactions with WalletFeed](#send-your-transactions-with-walletfeed) gives the steps.

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

WalletFeed has no account, and no WalletFeed server keeps your transactions or keys. Your transactions go from your iPhone directly to the folder or the service that you select.

Some of the destinations are:

- Budget apps, for example [YNAB](/guides/apple-card-to-ynab/), [Lunch Money](/guides/apple-card-to-lunch-money/), [PocketSmith](/guides/apple-card-to-pocketsmith/), [Toshl Finance](/guides/apple-card-to-toshl/), [Firefly III](/guides/apple-card-to-firefly-iii/) or [Sure](/guides/apple-card-to-sure/)
- Spreadsheets and databases, for example [Google Sheets](/guides/apple-card-to-google-sheets/), [Airtable](/guides/apple-card-to-airtable/), [Notion](/guides/apple-card-to-notion/) or [Coda](/guides/apple-card-to-coda/)
- [CSV](/guides/apple-card-to-csv/), [OFX](/guides/apple-card-to-ofx/) or [QIF](/guides/apple-card-to-qif/) files for an app that imports files, for example [Quicken](/guides/apple-card-to-quicken/), [Actual Budget](/guides/apple-card-to-actual-budget/), [GnuCash](/guides/apple-card-to-gnucash/) or [QuickBooks Online](/guides/apple-card-to-quickbooks/)
- Automations, for example [Zapier](/guides/apple-card-to-zapier/), [Make](/guides/apple-card-to-make/) or a [webhook](/guides/apple-card-to-webhook/).

To add a destination:

1. On your iPhone, open WalletFeed.
2. Tap **Destinations**.
3. Tap **+** at the top of the screen.

   ![The Destinations screen with no destinations and the + button at the top.](https://walletfeed.app/guides/apple-card-plaid/walletfeed-destinations-empty-pro.webp)

4. In the **Destinations** search field, type the name of the destination, for example `Lunch Money` or `OFX`.

   ![The Add Destination screen with the Destinations search field above the Budgeting list.](https://walletfeed.app/guides/apple-card-plaid/walletfeed-add-destination.webp)

5. Tap the destination.

   If you do not have WalletFeed Pro, the **WalletFeed Pro** screen opens. After you get WalletFeed Pro, the form for the destination opens.

6. Do the steps in the guide for the destination.

## Plaid and Apple Card in short

### Does Plaid support Apple Card?

Only in an iPhone app that added the connection. [Plaid, FinanceKit and Wallet](#plaid-financekit-and-wallet) tells you how the connection operates.

### Can I add Apple Card to Plaid without an app?

No. You start the connection in an iPhone app that has the Apple Card connection. [Connect Apple Card to Plaid in an iPhone app](#connect-apple-card-to-plaid-in-an-iphone-app) gives the steps.

### Does Plaid support Apple Cash or the Apple Savings account?

Plaid's documents give only Apple Card. [Apple Cash and Savings](#apple-cash-and-savings) gives the apps that connect to these accounts.

### Can I connect Apple Card to Plaid on the web or on Android?

No. The connection reads Wallet on your iPhone. Some services then show the transactions on your other devices.

### Does Plaid support Apple Pay?

Apple Pay is not an account. Apple Pay uses a card, for example your Apple Card, and the transactions are in the account of that card.

### Can ChatGPT connect to Apple Card through Plaid?

ChatGPT connects financial accounts through Plaid. On November 26, 2026, the [OpenAI help page for Finances](https://help.openai.com/en/articles/20001222-finances-in-chatgpt) did not give Apple Card. [Connect your Apple Card to ChatGPT with a Google Sheet](/guides/apple-card-to-chatgpt/) gives a different procedure.

### Can my budgeting app connect to Apple Card?

[Budgeting apps that support Apple Card and Apple Cash](/guides/apple-card-budget-apps/) gives the apps that connect, and the apps that WalletFeed sends to.

## If there is a problem

### If your app does not find Apple Card

The app cannot connect to Apple Card on this device, or this version of the app cannot connect. FinanceKit also does not give the Apple Card transactions of a participant in Apple Card Family ([FinanceKit page](https://developer.apple.com/financekit/)).

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

[Download WalletFeed on the App Store](https://apps.apple.com/app/apple-store/id6827429675?pt=125538749&ct=site&mt=8&ppid=67f05d46-993f-4df0-bf41-381c261854dd)
