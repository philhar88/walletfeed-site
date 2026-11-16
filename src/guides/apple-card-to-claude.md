+++
title = "How to ask Claude about your Apple Card transactions"
nav_title = "Claude"
seo_title = "Ask Claude about your Apple Card transactions"
description = "Ask Claude about your Apple Card transactions. WalletFeed keeps a Google Sheet up to date, and Claude reads it with its Google Drive connector."
group = "AI chatbots"
order = 30
related = ["guides/ask-ai-about-apple-card-spending", "guides/apple-card-to-google-sheets", "guides/apple-card-to-chatgpt", "docs/background-sync"]
updated = 2026-11-16
+++

To ask Claude about your Apple Card transactions, connect Google Drive in Claude, then ask about the spreadsheet that WalletFeed keeps up to date. WalletFeed reads your Apple Card, Apple Cash and Savings transactions on your iPhone and sends them to Google Sheets.

WalletFeed does not send your transactions to Claude. Claude reads the spreadsheet from your Google Drive when you ask about it.

## Before you start

You must have these items:

- An iPhone with iOS 26 or a newer version (WalletFeed is available only in the US)
- WalletFeed on your iPhone, with [access to your Wallet accounts](/docs/wallet-accounts/)
- [WalletFeed Pro](/docs/walletfeed-pro/) (a subscription with a 1-week free trial, or a one-time Lifetime purchase)
- A Google Account
- A Claude account, on a plan of your selection.

> **Note:** The Claude help page says that the Google Drive connector is available for all users on Claude and Claude Desktop. On Team and Enterprise plans, an Owner or a Primary Owner must first add the connector for the organization.

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

## Step 2: Connect Google Drive in Claude

Do these steps on claude.ai or in Claude Desktop. After you connect Google Drive, you can also use it in the Claude app for iPhone.

1. On your computer, open claude.ai or Claude Desktop.
2. Go to **Customize** › **Connectors**.
3. Click the **+** button at the side of **Connectors**.
4. Click **Google Drive**.
5. Click **Connect** or **Install**.
6. On the Google page, get access to the Google Account that has the spreadsheet.
7. Read the permissions on the Google page, then give Claude access.

   Result: Google Drive is in the list of your connectors.

> **Note:** The Claude app for iPhone can also add connectors. The Claude help page gives this function the status "beta".

## Step 3: Ask Claude about the spreadsheet

1. In Claude, start a new chat.
2. Click **+** in the lower left of the chat.
3. Put the pointer on **Connectors**.
4. Make sure that the switch for **Google Drive** is on.
5. Paste the prompt from [Prompt to start with](#prompt-to-start-with).
6. Send the prompt.
7. If Claude asks for your approval, do a check of the request, then approve it.
8. In the same chat, ask about your transactions.

If Claude does not find the spreadsheet, paste the URL of the spreadsheet in the chat. To get the URL, open the spreadsheet in Google Sheets on a computer, then copy the URL from the address bar.

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

- `How much did I spend on Groceries each month this year?`
- `Which subscriptions do I pay each month, and what is the total?`
- `Show my Apple Card purchases over $100 in October.`
- `Make a table of my spending by category for last month.`

## Large spreadsheets

The Claude help page says that the files in a chat must fit in the context window of the chat. If the spreadsheet has many transactions, Claude cannot read all the rows at one time. Then the totals are not correct.

- Ask about one month or one category at a time.
- Ask Claude to show the rows that it used, and do a check of the totals.
- In WalletFeed, use **Filter** on the destination to send only some accounts or categories (refer to [Choose what a destination receives](/docs/choose-what-to-send/)).

## Privacy

- WalletFeed sends your transactions from your iPhone to Google only. WalletFeed has no account, and no WalletFeed server keeps your transactions or keys.
- With the Google Drive connector, Claude can open the files that your Google Account can open, not only the spreadsheet.
- Claude keeps the data that it reads with the chat, on Anthropic servers. When you delete the chat, you delete that data.
- The Claude help page says that Anthropic does not train its models on data from the Google Drive connector.
- On Free, Pro, Max and Ultra plans, you can let Anthropic use your chats to train its models. Then Anthropic can use text that you paste from the spreadsheet, and answers from Claude that contain data from it.

The Claude help pages gave these rules on November 16, 2026. The rules can change.

To stop Claude, go to **Customize** › **Connectors**, then disconnect **Google Drive**. The spreadsheet stays in your Google Drive.

## If there is a problem

### If Google Drive is not in Connectors

On a Team or Enterprise plan, the owner of your organization did not add the connector.

1. Ask an Owner or a Primary Owner of your organization to add Google Drive in **Organization settings** › **Connectors**.
2. After the owner adds it, do the steps in [Step 2](#step-2-connect-google-drive-in-claude) again.

### If Claude shows "Please try again. You may need to reconnect with your Google Drive account"

Claude cannot use your Google sign-in.

1. Go to **Customize** › **Connectors**.
2. Disconnect **Google Drive**.
3. Connect **Google Drive** again.

### If Claude shows "Access blocked: your institution's admin needs to review Claude for Google Drive"

Your Google Account is part of an organization, and its Google Workspace administrator did not approve Claude.

1. Ask the Google Workspace administrator to make Claude a trusted app.
2. Connect **Google Drive** again.

### If the answers do not include your new transactions

The spreadsheet does not have the new transaction, or Claude did not read the file again.

1. Open the spreadsheet **WalletFeed Transactions** in Google Sheets. Look for the new transaction.
2. If the transaction is in the spreadsheet, start a new chat in Claude. Claude then reads the file again.
3. In the new chat, paste the prompt again, then ask again.
4. If the transaction is not in the spreadsheet, open WalletFeed on your iPhone. WalletFeed sends the new transactions.
5. Look in the spreadsheet again.

## FAQ

### Does WalletFeed send my transactions to Claude?

No. WalletFeed sends your transactions only to the spreadsheet in your Google Drive. Claude reads the spreadsheet when you ask about it.

### Can Claude read my Apple Card without the spreadsheet?

Claude has Personal Finance, which connects bank accounts through Plaid. On November 16, 2026, the [Claude help page for Personal Finance](https://support.claude.com/en/articles/18185620) did not give Apple Card. For the accounts that Personal Finance can connect, refer to that page.

### Can Claude change the spreadsheet?

The Google Drive connector can read, move and delete files, or give them to other people, and Claude asks for your approval first. A separate Google Sheets connector can edit a spreadsheet. To use it, click **+** in the chat, put the pointer on **Connectors**, then set **Google Sheets** to on. Do not let Claude change column A, **WalletFeed ID**, because WalletFeed uses it to find each row again.

### Does Claude get my new transactions?

Yes, when WalletFeed updates the spreadsheet. When WalletFeed is not open, iOS decides when WalletFeed runs. Expect the change in about 1 hour or less. If [Background Sync](/docs/background-sync/) is on, WalletFeed then sends the change.

> **Note:** Claude is a trademark of its owner. WalletFeed has no affiliation with Anthropic, and Anthropic does not endorse WalletFeed.

<!--
Sources, checked 2026-11-16:
- https://support.claude.com/en/articles/10166901 "Use Google Workspace connectors" (updated this week): available for all users on Claude and Claude Desktop; Team/Enterprise Owner or Primary Owner must enable; Drive reads Sheets; files must fit in the context window; + > Connectors toggles; data stored with the chat on Anthropic servers; no training on connector data, with the consumer copy/paste caveat; reconnect error text; "Access blocked" admin text; separate Google Sheets connector edits files.
- https://support.claude.com/en/articles/11176164 "Use connectors to extend Claude's capabilities" (updated over a week ago): Customize > Connectors, + next to Connectors, Connect or Install; connectors on iOS/Android, installing on mobile in beta; a connector set up on web or desktop is available in the mobile app; Organization settings > Connectors.
- https://support.claude.com/en/articles/18185620 "Use Personal Finance in Claude": Plaid, beta on Pro/Max/Ultra in the US; the page does not list Apple Card.
- Not verified: the exact label of the Google Drive tile and the Connect button text in the directory (the help page says "Connect" or "Install"); the step to add a Drive spreadsheet with "Add from Google Drive" (the help page describes it for documents), so the page uses the prompt or the URL instead.
-->
