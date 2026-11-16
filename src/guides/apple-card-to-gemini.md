+++
title = "How to ask Gemini about your Apple Card transactions"
nav_title = "Gemini"
seo_title = "Ask Gemini about your Apple Card transactions"
description = "Ask Gemini about your Apple Card transactions. WalletFeed keeps a Google Sheet up to date, and Gemini reads it with the Google Workspace app."
group = "AI chatbots"
order = 40
related = ["guides/ask-ai-about-apple-card-spending", "guides/apple-card-to-google-sheets", "guides/apple-card-to-chatgpt", "docs/background-sync"]
updated = 2026-11-16
+++

To ask Gemini about your Apple Card transactions, connect the Google Workspace app in Gemini, then ask about the spreadsheet that WalletFeed keeps up to date. WalletFeed reads your Apple Card, Apple Cash and Savings transactions on your iPhone and sends them to Google Sheets.

WalletFeed does not send your transactions to Gemini. Gemini reads the spreadsheet from your Google Drive when you ask about it.

## Before you start

You must have these items:

- An iPhone with iOS 26 or a newer version (WalletFeed is available only in the US)
- WalletFeed on your iPhone, with [access to your Wallet accounts](/docs/wallet-accounts/)
- [WalletFeed Pro](/docs/walletfeed-pro/) (a subscription with a 1-week free trial, or a one-time Lifetime purchase)
- A Google Account
- **Keep Activity** on in Gemini. Without it, Gemini cannot connect to Google Workspace.

> **Note:** The Gemini help pages give no plan for the Google Workspace app. A Google AI plan gives higher limits for files. For a work or school account, the Google Workspace administrator must first let Gemini connect to apps.

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

## Step 2: Connect Google Workspace in Gemini

Use the Google Account that has the spreadsheet. On a computer, do these steps:

1. Go to gemini.google.com.
2. On the sidebar, click **Customize**.

   If you do not find **Customize**, click **More** first.

3. At the top, click **Connectors**.
4. Find **Google Workspace**.
5. Click **Add**.
6. Obey the instructions on the screen.

On your iPhone, open the Gemini app, then tap **Menu** › **Customize** › **Connectors**. Then tap **Add** for **Google Workspace**.

## Step 3: Ask Gemini about the spreadsheet

1. In Gemini, start a new chat.
2. Type `@`, then select **Google Drive**.
3. Paste the prompt from [Prompt to start with](#prompt-to-start-with).
4. Send the prompt.
5. In the same chat, ask about your transactions.

The Gemini help page tells you not to paste the URL of a document. Use the name of the spreadsheet, as in the prompt. In each new chat, tell Gemini again to use the spreadsheet in your Google Drive.

You can also add the spreadsheet as a file. In the message box, click **Add files**, then click **Add from Drive**. In the Gemini app for iPhone, tap **Add files**, then tap **Drive**.

> **Note:** In the Gemini app for iPhone, a Google Sheets file from the Files app changes to a PDF file. To keep the rows and the columns, use **Drive**, not **Files**.

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

- `How much did I spend on Dining last month?`
- `Compare my spending in September and October by category.`
- `Show my purchases in a different currency this year.`
- `Make a chart of my spending each month this year.`

## Large spreadsheets

The Gemini help page says that if a file is too large, Gemini can miss details in it. A file can be 100 MB at most.

- Ask about one month or one category at a time.
- Ask Gemini to show the rows that it used, and do a check of the totals.
- In WalletFeed, use **Filter** on the destination to send only some accounts or categories (refer to [Choose what a destination receives](/docs/choose-what-to-send/)).

The help page also says that Google AI Pro and Google AI Ultra give a larger context window and higher limits for files.

## Privacy

- WalletFeed sends your transactions from your iPhone to Google only. WalletFeed has no account, and no WalletFeed server keeps your transactions or keys.
- With Google Workspace in Gemini, Gemini can read the files in your Google Drive, not only the spreadsheet.
- The Gemini help page says that Gemini does not train its models directly on your Drive files.
- The same page says that Google trains its models on the summaries and excerpts of your files that Gemini uses for its answers. For a short file, the summary can be the full file.
- Human reviewers can read some of this data. The page tells you not to connect apps that contain confidential data.

The Gemini help pages gave these rules on November 16, 2026. The rules can change. You can disconnect Google Workspace in **Customize** › **Connectors**. The spreadsheet stays in your Google Drive.

## If there is a problem

### If Gemini cannot connect to Google Workspace

**Keep Activity** is off, or a setting in Gmail stops the connection.

1. In Gemini, make sure that **Keep Activity** is on.
2. In your Gmail settings, set **Smart features in other Google products** to on.
3. Open Gemini again.
4. Connect **Google Workspace** again.

For a work or school account, the Google Workspace administrator must let Gemini connect to apps.

### If Gemini does not find the spreadsheet

Gemini did not use Google Drive for your prompt.

1. Type `@`, then select **Google Drive**.
2. In your prompt, type the name of the spreadsheet, **WalletFeed Transactions**.
3. If Gemini still does not find it, add it with **Add files** › **Add from Drive**.

### If the answers do not include your new transactions

The spreadsheet does not have the new transaction, or Gemini did not read the file again.

1. Open the spreadsheet **WalletFeed Transactions** in Google Sheets. Look for the new transaction.
2. If the transaction is in the spreadsheet, start a new chat in Gemini. Gemini then reads the file again.
3. In the new chat, paste the prompt again, then ask again.
4. If the transaction is not in the spreadsheet, open WalletFeed on your iPhone. WalletFeed sends the new transactions.
5. Look in the spreadsheet again.

## FAQ

### Does WalletFeed send my transactions to Gemini?

No. WalletFeed sends your transactions only to the spreadsheet in your Google Drive. Gemini reads the spreadsheet when you ask about it.

### Do Gemini and WalletFeed have the same access to my Google Drive?

No. Gemini and WalletFeed can use the same Google Account, but they have different access. WalletFeed can open only the spreadsheets that it makes. Gemini can read the files in your Google Drive.

### Does Gemini get my new transactions?

Yes, when WalletFeed updates the spreadsheet. When WalletFeed is not open, iOS decides when WalletFeed runs. Expect the change in about 1 hour or less. If [Background Sync](/docs/background-sync/) is on, WalletFeed then sends the change.

> **Note:** Gemini is a trademark of its owner. WalletFeed has no affiliation with Google, and Google does not endorse WalletFeed.

<!--
Sources, checked 2026-11-16:
- https://support.google.com/gemini/answer/15229592 "Connect the Google Workspace app to Gemini Apps": Keep Activity must be on; "enter @ and select the service"; "Don't paste the URL of a document"; mention the service in every new conversation; work/school admin; Gmail "Smart features in other Google products"; spreadsheets are readable content.
- https://support.google.com/gemini/answer/13695044 "Use & manage Connected Apps in Gemini" (Computer and iPhone & iPad versions): Customize (or More first) > Connectors > Add; iPhone: Menu > Customize > Connectors; disconnect with More options > Disconnect.
- https://support.google.com/gemini/answer/14903178 "Upload & analyze files in Gemini Apps" (Computer and iPhone & iPad versions): Add files > Add from Drive (web), Add files > Drive (iPhone app), Sheets from the Files app convert to PDF, 100 MB per file, large files can miss details, Google AI Pro/Ultra 1M token context.
- https://support.google.com/gemini/answer/16836988 "About personalization with Connected Apps": no direct training on Drive; summaries/excerpts in Gemini Apps activity used to improve Google services with Keep Activity on; human review of a subset.
- Not verified: the exact name "Google Workspace" in the Connectors list on every device (the help pages call it "the Google Workspace app"); a plan requirement (none stated).
-->
