+++
title = "How to ask Grok about your Apple Card transactions"
nav_title = "Grok"
seo_title = "Ask Grok about your Apple Card transactions"
description = "Ask Grok about your Apple Card transactions. WalletFeed keeps a Google Sheet up to date, and Grok reads it with its Google Drive connector."
group = "AI chatbots"
order = 50
related = ["guides/ask-ai-about-apple-card-spending", "guides/apple-card-to-google-sheets", "guides/apple-card-to-claude", "docs/background-sync"]
updated = 2026-11-16
+++

To ask Grok about your Apple Card transactions, connect Google Drive in Grok, then ask about the spreadsheet that WalletFeed keeps up to date. WalletFeed reads your Apple Card, Apple Cash and Savings transactions on your iPhone and sends them to Google Sheets.

WalletFeed does not send your transactions to Grok. Grok reads the spreadsheet from your Google Drive when you ask about it.

## Before you start

You must have these items:

- An iPhone with iOS 26 or a newer version (WalletFeed is available only in the US)
- WalletFeed on your iPhone, with [access to your Wallet accounts](/docs/wallet-accounts/)
- [WalletFeed Pro](/docs/walletfeed-pro/) (a subscription with a 1-week free trial, or a one-time Lifetime purchase)
- A Google Account
- A Grok account.

> **Note:** The Grok documents say that connectors are available to all Grok users. On Grok Business and Enterprise plans, a team admin must first add the connector for the organization.

## Step 1: Make the spreadsheet in WalletFeed

1. On your iPhone, open WalletFeed.
2. Tap **Destinations** at the bottom of the screen.
3. Tap **+** at the top of the screen.
4. In **Sheets & Databases**, tap **Google Sheets**.
5. Tap **Sign In with Google**, then give WalletFeed access on the Google page.
6. Tap **Add** at the top of the screen.
7. In the message **Send Transactions to Google Sheets?**, tap **Send**.

   Result: WalletFeed makes the spreadsheet **WalletFeed Transactions** in your Google Drive and sends your transactions to it.

[Send Apple Card transactions to Google Sheets](/guides/apple-card-to-google-sheets/) gives all the steps and the columns.

## Step 2: Connect Google Drive in Grok

On a computer, do these steps:

1. Go to [grok.com/connectors](https://grok.com/connectors).
2. Click **New Connector**.
3. Select **Google Drive**.
4. On the Google page, get access to the Google Account that has the spreadsheet.
5. Read the permissions, then click **Allow**.

   Result: Google Drive is in the list of your connectors.

In the Grok app for iPhone, go to **Settings** › **Connectors**, then connect Google Drive.

## Step 3: Ask Grok about the spreadsheet

1. In Grok, start a new chat.
2. Paste the prompt from [Prompt to start with](#prompt-to-start-with).
3. Send the prompt.
4. In the same chat, ask about your transactions.

## Prompt to start with

Copy this prompt, then paste it in the chat. It gives the columns and the rule for spending. The rule is the same as in the WalletFeed app.

```
Read the Google Sheets spreadsheet "WalletFeed Transactions" in my Google Drive. Use the tab "Transactions". Row 1 has the column names. Each row below row 1 is one transaction from my Apple Card, Apple Cash or Savings account.

The columns are:
- WalletFeed ID: an ID that the WalletFeed app uses. Ignore it.
- Date: the date of the transaction.
- Merchant: the name of the merchant.
- Amount: money out of the account is a negative number. Money into the account is a positive number.
- Currency: the currency code, for example USD. Amount is in this currency.
- Category: the category, for example Groceries or Dining.
- Status: the status from Apple Wallet, for example booked or pending.
- Pending: TRUE (a checkmark) when the transaction is pending.
- Account: the account, for example Apple Card, Apple Cash or Savings.
- Description: the description of the transaction from Apple Wallet.
- Type: the type of the transaction from Apple Wallet, for example pointOfSale, refund, transfer or billPayment.
- MCC: the merchant category code.
- Foreign Amount and Foreign Currency: for a purchase in a different currency, the amount and the currency code in that currency. Empty for other transactions.

To find the spending of one row, use only the columns Type and Amount, in this order. Do not use Category, Merchant or Description for this.
1. If Type is exactly transfer or billPayment, the spending of the row is 0. This is true even when Amount is negative.
2. Otherwise, if Amount is negative, the spending of the row is Amount without the minus sign.
3. Otherwise, if Type is exactly refund, the spending of the row is minus Amount. A refund makes the total smaller.
4. Otherwise, the spending of the row is 0.

The total spending of a group of rows is the sum of the spending of each row.
- Include the rows where Pending is TRUE, unless I ask you to leave out pending transactions.
- Use the Date column for periods, for example a month or a year.
- Do not add amounts in different currencies. Give one total for each currency.
- Show the totals, and list the rows that you used for each total.
- If you cannot read all the rows, tell me the first and the last date that you read.

First, tell me the number of rows and the first and the last date in the spreadsheet.
```

Then ask about your transactions, for example:

- `How much did I spend on Transport last month?`
- `Show my 10 most frequent merchants this year, with the total for each.`
- `Show my refunds this year, with the merchant and the date.`
- `Compare my spending in each week of October.`

## Large spreadsheets

If the spreadsheet has many transactions, it is possible that Grok does not read all the rows. Then the totals are not correct. The Grok documents give no limit for the size of a file.

- Ask about one month or one category at a time.
- Ask Grok to show the rows that it used, and do a check of the totals.
- In WalletFeed, use **Filter** on the destination to send only some accounts or categories (refer to [Choose what a destination receives](/docs/choose-what-to-send/)).

## Privacy

- WalletFeed sends your transactions from your iPhone to Google only. WalletFeed has no account, and no WalletFeed server keeps your transactions or keys.
- The Google Drive connector asks for access to read the files in your Google Drive, not only the spreadsheet. It can also ask for access to edit files.
- The Grok documents say that the company that makes Grok does not use your Google Drive data to train its models.
- The documents also say that Grok reads your files when you ask about them, and does not keep them on its servers.

The Grok documents gave these rules on November 16, 2026. The rules can change.

To stop Grok, do these steps:

1. Go to [grok.com/connectors](https://grok.com/connectors).
2. Find **Google Drive** in the list of your connectors.
3. Click **Disconnect**.

You can also remove Grok on the [third-party connections page](https://myaccount.google.com/permissions) of your Google Account. The spreadsheet stays in your Google Drive.

## If there is a problem

### If Google Drive is not in the list of connectors

On Grok Business or Enterprise, the team admin did not add the connector.

1. Ask your team admin to add the Google Drive connector.
2. After the admin adds it, do the steps in [Step 2](#step-2-connect-google-drive-in-grok) again.

### If Grok does not find the spreadsheet

Grok did not use the Google Drive connector for your prompt.

1. Go to [grok.com/connectors](https://grok.com/connectors).
2. Make sure that **Google Drive** is in the list of your connectors.
3. In your prompt, type "in my Google Drive" and the name of the spreadsheet, **WalletFeed Transactions**.

### If the answers do not include your new transactions

The spreadsheet does not have the new transaction, or Grok did not read the file again.

1. Open the spreadsheet **WalletFeed Transactions** in Google Sheets. Look for the new transaction.
2. If the transaction is in the spreadsheet, start a new chat in Grok. Grok then reads the file again.
3. In the new chat, paste the prompt again, then ask again.
4. If the transaction is not in the spreadsheet, open WalletFeed on your iPhone. WalletFeed sends the new transactions.
5. Look in the spreadsheet again.

## FAQ

### Does WalletFeed send my transactions to Grok?

No. WalletFeed sends your transactions only to the spreadsheet in your Google Drive. Grok reads the spreadsheet when you ask about it.

### Can Grok change the spreadsheet?

The Google Drive connector can make and edit files, if you give it that access. Do not let Grok change column A, **WalletFeed ID**, because WalletFeed uses it to find each row again.

### Does Grok get my new transactions?

Yes, when WalletFeed updates the spreadsheet. When WalletFeed is not open, iOS decides when WalletFeed runs. Expect the change in about 1 hour or less. If [Background Sync](/docs/background-sync/) is on, WalletFeed then sends the change.

> **Note:** Grok is a trademark of its owner. WalletFeed has no affiliation with SpaceXSI (formerly xAI), the company that makes Grok, and SpaceXSI does not endorse WalletFeed.

<!--
Sources, checked 2026-11-16:
- https://docs.x.ai/grok/connectors "Connectors": available to all Grok users; Business/Enterprise admin provisions connectors; Google Drive connector covers "Google Drive files, Docs, Sheets, and Slides"; grok.com/connectors > New Connector > OAuth.
- https://docs.x.ai/grok/connectors/google-drive "Google Drive Connector" (last updated October 10, 2026): search and read Sheets; scopes drive.metadata.readonly, drive.readonly, drive (optional write), userinfo.email; New Connector > Google Drive > sign in > Allow; no training on Drive data; files not stored; Disconnect at grok.com/connectors; revoke at myaccount.google.com/permissions.
- https://x.ai/news/grok-connectors (May 6, 2026): connectors on Grok web, iOS and Android; iOS and Android: Settings > Connectors; web: + > Connectors > + Add connector.
- Not verified: the exact names of the iPhone screens after Settings > Connectors; a file size limit (none stated). The docs name the company SpaceXSI (docs.x.ai/grok/connectors, 2026-11-16); xAI was renamed after the SpaceX acquisition.
-->
