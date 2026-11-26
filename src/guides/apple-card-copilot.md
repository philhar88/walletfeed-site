+++
title = "Add Apple Card to Copilot Money"
nav_title = "Copilot Money"
seo_title = "Add Apple Card to Copilot Money: steps and limits"
description = "You can add Apple Card to Copilot Money only in its iPhone app, on iOS 17.4 or newer. The limits, and what to do if Apple Card does not sync with Copilot."
group = "Budgeting apps"
order = 88
related = ["guides/apple-card-plaid", "guides/apple-card-budget-apps", "guides/apple-card-monarch", "guides/apple-card-rocket-money", "guides/export-apple-card-transactions"]
updated = 2026-11-26
+++

Copilot Money connects to your Apple Card, Apple Cash and Savings accounts in its app for iPhone. An iPhone with iOS 17.4 or a newer version is necessary. After you connect on your iPhone, the Copilot apps for Mac and iPad also show the accounts.

The facts on this page come from the Copilot help center page [Apple Card, Apple Cash, and Savings](https://help.copilot.money/en/articles/9038131-apple-card-apple-cash-and-savings). The page has the date March 20, 2026.

## Before you start

You must have these items:

- An iPhone with iOS 17.4 or a newer version
- The newest version of the Copilot app on that iPhone
- An Apple Card, Apple Cash or Savings account of which you are the primary account holder.

> **Note:** Copilot tells you that only the primary account holder can connect these accounts.

## Add your Apple Card in Copilot

The Copilot help page does not give the name of each button. It gives these steps:

1. Update your iPhone to iOS 17.4 or a newer version.
2. Update the Copilot app on your iPhone to the newest version.
3. On your iPhone, open Copilot.
4. Add a new Apple Card connection.
5. Do the steps that Copilot shows.

You cannot add the connection in the Copilot app for Mac. On the date of the help page, a known bug also prevented the connection on an iPad.

## If Copilot has a manual account for your Apple Card

A manual account is an account to which you added the transactions yourself.

### Apple Card

Do not delete the manual account. When you add the new Apple Card connection, Copilot gives you the option to merge the manual account with the connected account. This option is only for Apple Card.

### Apple Cash and Savings

The connection also brings your earlier transactions. Thus, Copilot gives you two options for the manual account:

- Delete the manual account, and use the connected account.
- Set the manual account to **CLOSED**. Copilot then keeps the earlier transactions of the manual account, and the connected account gets the new transactions.

If the manual account and the connected account show the same transaction, change the date from which Wallet gives your transactions to Copilot:

1. On your iPhone, open **Settings** › **Privacy & Security** › **Wallet** › **Copilot** › **Activity**.
2. Select **Starting Today** or **Starting 30 Days Ago**.

## Limits of the connection

Copilot gives these limits:

- You can add the connection only in the Copilot app on an iPhone.
- Copilot reads the data from Wallet in its app for iPhone. Thus, the Mac and iPad apps get new transactions only after you open Copilot on your iPhone.
- Only the primary account holder can connect an account.
- If you are an authorized user of the account of a different person, you get updates only after that person opens Copilot on their iPhone.
- Apple gives Copilot the "total balance" of your Apple Card. This balance does not include pending transactions. It includes monthly installments that are not paid.
- Apple does not give Copilot the names of Savings transactions. Thus, Copilot shows one of these names for each transaction: Savings Interest Earned, Apple Card Daily Cash, Savings Deposit, Savings Withdrawal, or Savings.

### Files

Copilot does not import transaction files. The Copilot help center article [Investment Account Limitations](https://help.copilot.money/en/articles/10262766-investment-account-limitations), with the date April 14, 2026, has this sentence: "We are not able to support importing transactions via CSV or XLS at this time."

## If Apple Card does not connect or get updates in Copilot

### If you cannot connect your account

1. Make sure that you use the Copilot app on an iPhone, not on a Mac or an iPad.
2. Make sure that your iPhone has iOS 17.4 or a newer version.
3. Make sure that you are the primary account holder.

### If Copilot does not show new transactions

1. Open Copilot on your iPhone.
2. Look for the new transactions in Copilot on your Mac or iPad.
3. If you are an authorized user, tell the primary account holder to open Copilot on their iPhone.

### If the Apple Card balance is not correct

The "total balance" from Apple does not include pending transactions, and it includes monthly installments that are not paid. Thus, the balance in Copilot can be different from the balance in Wallet.

1. If you have no pending transactions and no monthly installments, open the chat in the Copilot app.
2. Make a screenshot of the balance in Copilot.
3. Make a screenshot of the correct balance in Wallet.
4. Remove your personal data and your full account numbers from each screenshot.
5. Send the two screenshots to Copilot in the chat.

### If a Savings transaction has a general name

1. In Copilot, tap the transaction.
2. Tap the name.
3. Tap **Edit**.
4. Type a new name.
5. Tap **Save**.

## Keep a copy of your transactions in a file or a spreadsheet

WalletFeed is a different app for iPhone. It reads your Apple Card, Apple Cash and Savings transactions from Wallet on your iPhone. WalletFeed does not send transactions to Copilot. If you also want your transactions in a file or a spreadsheet, WalletFeed can make one:

- [Export CSV](/docs/export-csv/) makes one CSV file of a period that you select. WalletFeed Pro is not necessary for this file.
- A [CSV file destination](/guides/apple-card-to-csv/) writes a CSV file in a folder that you select. WalletFeed updates the file when your transactions change.
- A [Google Sheets destination](/guides/apple-card-to-google-sheets/) makes a spreadsheet in your Google Drive. WalletFeed updates the spreadsheet when your transactions change.

[WalletFeed Pro](/docs/walletfeed-pro/) is necessary for a destination. WalletFeed Pro is a subscription with a 1-week free trial, or a one-time Lifetime purchase.

WalletFeed is available only in the US, for an iPhone with iOS 26 or a newer version. WalletFeed has no account, and no WalletFeed server keeps your transactions.
