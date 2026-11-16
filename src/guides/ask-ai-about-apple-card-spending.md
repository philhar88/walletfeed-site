+++
title = "Ask ChatGPT, Claude, Gemini or Grok about your Apple Card spending"
nav_title = "Ask an AI chatbot"
seo_title = "Ask AI about Apple Card spending: ChatGPT, Claude, Gemini"
description = "Ask ChatGPT, Claude, Gemini or Grok about your Apple Card spending. WalletFeed keeps a Google Sheet up to date, and the chatbot reads it from Google Drive."
group = "AI chatbots"
order = 10
related = ["guides/apple-card-to-chatgpt", "guides/apple-card-to-claude", "guides/apple-card-to-gemini", "guides/apple-card-to-grok", "guides/apple-card-to-google-sheets"]
updated = 2026-11-16
+++

To ask ChatGPT, Claude, Gemini or Grok about your Apple Card spending, give the chatbot a Google Sheets spreadsheet of your transactions. WalletFeed keeps the spreadsheet up to date from your iPhone. The chatbot reads the spreadsheet from your Google Drive.

## Apple Card and AI chatbots

A chatbot on the web cannot get your Apple Card transactions with a bank login. Plaid cannot connect to Apple Card with your login, as it does for a bank. [Apple Card and Plaid](/guides/apple-card-plaid/) gives more information.

Your Apple Card, Apple Cash and Savings transactions are in Wallet on your iPhone. An iPhone app can read them with FinanceKit, Apple's software for financial apps, after you give the app access.

Some chatbots have a finance feature that connects to bank accounts through Plaid. For Apple Card in such a feature, refer to the help pages of the chatbot.

## The procedure

WalletFeed reads your transactions from Wallet on your iPhone. Then WalletFeed sends them to a spreadsheet in your Google Drive, and updates the spreadsheet when they change. In the chatbot, you connect your Google Drive and ask about the spreadsheet.

WalletFeed does not send your transactions to the chatbot. The chatbot reads the spreadsheet from Google Drive when you ask about it.

## Chatbots that read a Google Sheets spreadsheet

The help pages of each chatbot gave this information on November 16, 2026.

| Chatbot | Connection to Google Drive | Plans | iPhone app |
| --- | --- | --- | --- |
| [ChatGPT](/guides/apple-card-to-chatgpt/) | The **Google Drive** app, in **Settings** › **Plugins** | The help page says that it depends on your plan, your location and your workspace. ChatGPT also has Finances. [Compare Finances and the sheet](/guides/apple-card-to-chatgpt/#chatgpt-finances-or-a-google-sheet-that-you-keep). | Yes |
| [Claude](/guides/apple-card-to-claude/) | The **Google Drive** connector, in **Customize** › **Connectors** | All users. On Team and Enterprise plans, an owner must first add the connector. | Yes |
| [Gemini](/guides/apple-card-to-gemini/) | The **Google Workspace** app, in **Customize** › **Connectors** | The help pages give no plan. **Keep Activity** must be on. | Yes |
| [Grok](/guides/apple-card-to-grok/) | The **Google Drive** connector, at grok.com/connectors | All users. On Business and Enterprise plans, an admin must first add the connector. | Yes |

The page for each chatbot gives the steps.

## Before you start

You must have these items:

- An iPhone with iOS 26 or a newer version (WalletFeed is available only in the US)
- WalletFeed on your iPhone, with [access to your Wallet accounts](/docs/wallet-accounts/)
- [WalletFeed Pro](/docs/walletfeed-pro/) (a subscription with a 1-week free trial, or a one-time Lifetime purchase)
- A Google Account
- An account for the chatbot.

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

## Step 2: Connect Google Drive in the chatbot

Do the steps on the page for your chatbot:

- [ChatGPT](/guides/apple-card-to-chatgpt/)
- [Claude](/guides/apple-card-to-claude/)
- [Gemini](/guides/apple-card-to-gemini/)
- [Grok](/guides/apple-card-to-grok/).

Connect the Google Account that has the spreadsheet.

## Step 3: Ask about the spreadsheet

Start a new chat, then paste the prompt below. After the chatbot reads the spreadsheet, type your prompts in the same chat.

## Prompt to start with

This prompt tells the chatbot where the spreadsheet is, what each column contains, and how to count spending. The rule for spending is the same as in the WalletFeed app. Copy the prompt, then paste it in the chat.

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
- `Show my 10 largest Apple Card purchases this year.`
- `Compare my Groceries spending in each month of this year.`
- `Which merchants did I pay more than 3 times in October?`
- `Show my refunds this year, with the merchant and the date.`
- `How much did I spend in a different currency on my last trip?`

## Large spreadsheets

A chatbot can read only a limited quantity of text at one time. If the spreadsheet has many transactions, it is possible that the chatbot does not read all the rows. Then the totals are not correct.

To get better answers:

- Ask about one month or one category at a time.
- Ask the chatbot to show the rows that it used, and do a check of the totals.
- In WalletFeed, use **Filter** on the destination to send only some accounts or categories (refer to [Choose what a destination receives](/docs/choose-what-to-send/)).
- In WalletFeed, set **Settings** › **Sync** › **Initial History** to **1 Year** before you add the destination.

## Privacy

- WalletFeed sends your transactions from your iPhone to Google only. WalletFeed has no account, and no WalletFeed server keeps your transactions or keys.
- When you connect Google Drive in a chatbot, the provider of the chatbot can read the files in your Google Drive, not only the spreadsheet.
- After the chatbot reads the spreadsheet, the terms and the privacy policy of the provider apply to the data. The page for each chatbot gives the data rules from its help pages.
- To keep the chatbot away from your other files, you can use a different Google Account for the WalletFeed spreadsheet.

To stop the chatbot, disconnect Google Drive in the chatbot. You can also remove the chatbot in your Google Account, on the [third-party connections page](https://myaccount.google.com/connections). The spreadsheet stays in your Google Drive.

## Other procedures

- With **Export CSV**, WalletFeed makes one CSV file of your transactions, without WalletFeed Pro. You can upload the file in the chatbot. The file does not change, so you must make a new file for new transactions. [Export CSV](/docs/export-csv/) gives the steps.
- With [Ask Spending](/docs/ask-spending/), you type text about your transactions in WalletFeed. Apple Intelligence on your iPhone reads your text, and WalletFeed shows a chart and a summary.

## FAQ

### Does WalletFeed send my transactions to the chatbot?

No. WalletFeed sends your transactions only to the spreadsheet in your Google Drive. The chatbot reads the spreadsheet when you ask about it.

### Does the chatbot get my new transactions?

Yes, when WalletFeed updates the spreadsheet. While WalletFeed is open, the spreadsheet receives changes in seconds. When WalletFeed is not open, iOS decides when WalletFeed runs. Expect the change in about 1 hour or less. If [Background Sync](/docs/background-sync/) is on, WalletFeed then sends the change.

### Can the chatbot change the spreadsheet?

Some chatbots can edit files in Google Drive. Do not let a chatbot change column A, **WalletFeed ID**, because WalletFeed uses it to find each row again. To keep your own data, tell the chatbot to put it in a different spreadsheet.

### Is WalletFeed Pro necessary?

Yes, for the spreadsheet. All destinations use WalletFeed Pro. **Export CSV** and **Ask Spending** do not use WalletFeed Pro.

### Are the answers always correct?

No. A chatbot can make mistakes. Do a check of important totals in the spreadsheet or in your Apple Card statement.

> **Note:** ChatGPT, Claude, Gemini and Grok are trademarks of their owners. WalletFeed has no affiliation with these companies, and they do not endorse WalletFeed.

<!--
Sources, checked 2026-11-16:
- ChatGPT: https://help.openai.com/en/articles/10929079 (Google Drive app and setup in ChatGPT), https://help.openai.com/en/articles/11487775 (Connected apps in ChatGPT), https://help.openai.com/en/articles/20001256 (Plugins in ChatGPT), https://help.openai.com/en/articles/20001222 (Finances in ChatGPT: Plaid; page not readable, HTTP 403)
- Claude: https://support.claude.com/en/articles/10166901 (Use Google Workspace connectors), https://support.claude.com/en/articles/11176164 (Use connectors to extend Claude's capabilities), https://support.claude.com/en/articles/18185620 (Personal Finance: Plaid; page not readable, HTTP 403)
- Gemini: https://support.google.com/gemini/answer/15229592 (Connect the Google Workspace app), https://support.google.com/gemini/answer/13695044 (Use & manage Connected Apps), https://support.google.com/gemini/answer/14903178 (Upload & analyze files)
- Grok: https://docs.x.ai/grok/connectors, https://docs.x.ai/grok/connectors/google-drive (last updated 2026-10-10), https://x.ai/news/grok-connectors (2026-05-06: web, iOS and Android)
- WalletFeed: src/guides/apple-card-to-google-sheets.md (columns, steps), docs/writing/guide-style.md
-->
