# How to ask ChatGPT about your Apple Card transactions

To ask ChatGPT about your Apple Card transactions, connect Google Drive in ChatGPT, then ask about the spreadsheet that WalletFeed keeps up to date. WalletFeed reads your Apple Card, Apple Cash and Savings transactions on your iPhone and sends them to Google Sheets.

WalletFeed does not send your transactions to ChatGPT. ChatGPT reads the spreadsheet from your Google Drive when you ask about it.

## ChatGPT Finances or a Google Sheet that you keep

ChatGPT has its own feature for money, called Finances. You can also give ChatGPT a Google Sheet that WalletFeed keeps up to date. This section gives the facts that we can confirm for each one. Then it says when the sheet is the better fit.

### Facts about Finances

- Finances shows your spending, bills, subscriptions, net worth, investments and credit score in one place. You can ask about them in chat.
- You connect financial accounts through Plaid. Credit report data comes through Experian.
- A news report on the rollout of October 2, 2026 gives Free, Go, Plus and Pro plans, in the US, on the web, iOS and Android. The help page has the current list.

For the accounts that Finances can connect, refer to the [OpenAI help page for Finances](https://help.openai.com/en/articles/20001222).

### Reports from users and news sites

A news item of July 17, 2026 says that the ChatGPT app can connect Apple Card and Savings. A user report of October 20, 2026 says that you must use the ChatGPT iPhone app for this. These are reports, not statements from OpenAI. If you use the iPhone app, you can look for the option in Finances.

### Reasons to use the WalletFeed sheet

Use the WalletFeed sheet in these cases:

- You want a spreadsheet that you keep and can edit.
- You also use Claude, Gemini or Grok, and you want the same data in each one.
- You want to select which accounts and transactions the sheet gets.
- Finances is not available on your plan or in your workspace.

> **Note:** This page does not say that the sheet is more private than Finances. In each case, the terms of the service that holds your transactions apply.

The rest of this page gives the procedure for the Google Sheet.

## Before you start

You must have these items:

- An iPhone with iOS 26 or a newer version (WalletFeed is available only in the US)
- WalletFeed on your iPhone, with [access to your Wallet accounts](/docs/wallet-accounts/)
- [WalletFeed Pro](/docs/walletfeed-pro/) (a subscription with a 1-week free trial, or a one-time Lifetime purchase)
- A Google Account
- A ChatGPT account.

> **Note:** The OpenAI help page says that the Google Drive app depends on your ChatGPT plan, your location, your workspace settings and the Google Workspace policies. In a workspace, an administrator can make the app unavailable.

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

## Step 2: Connect Google Drive in ChatGPT

You can do these steps on chatgpt.com, in the ChatGPT desktop app or in the ChatGPT app for iPhone.

1. In ChatGPT, open **Settings** › **Plugins**.

   An earlier version of the ChatGPT app can show **Apps** in place of **Plugins**.

2. Select **Google Drive**.
3. If ChatGPT shows **Install plugin**, select it.
4. If ChatGPT shows **Connect**, select it.
5. On the Google page, get access to the Google Account that has the spreadsheet.
6. Read the permissions on the Google page, then give ChatGPT access.

   Result: ChatGPT shows Google Drive as connected.

If ChatGPT shows **ChatGPT needs all requested permissions**, select **Try again**. Then, on the Google page, select **Select all**.

## Step 3: Ask ChatGPT about the spreadsheet

1. In ChatGPT, start a new chat.
2. Type `@`, then select **Google Drive**.

   You can also select **+** in the message box, then select Google Drive.

3. Paste the prompt from [Prompt to start with](#prompt-to-start-with).
4. Send the prompt.
5. If ChatGPT asks for approval to read the file, do a check of the request, then approve it.
6. In the same chat, ask about your transactions.

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
- `Show my 10 largest Apple Card purchases this year.`
- `Make a table of my spending by category for each month this year.`
- `Do I have two charges from the same merchant on the same day?`

## Large spreadsheets

If the spreadsheet has many transactions, it is possible that ChatGPT does not read all the rows. Then the totals are not correct.

- Ask about one month or one category at a time.
- Ask ChatGPT to show the rows that it used, and do a check of the totals.
- In WalletFeed, use **Filter** on the destination to send only some accounts or categories (refer to [Choose what a destination receives](/docs/choose-what-to-send/)).

For the limits of your ChatGPT plan, refer to the [OpenAI help page for connected apps](https://help.openai.com/en/articles/11487775).

## Privacy

- WalletFeed sends your transactions from your iPhone to Google only. WalletFeed has no account, and no WalletFeed server keeps your transactions or keys.
- With the Google Drive app, ChatGPT can open the files that your Google Account can open, not only the spreadsheet.
- For the rules on the use of your data to train models, refer to the [OpenAI help page for connected apps](https://help.openai.com/en/articles/11487775). The rules can depend on your plan and your settings.

To stop ChatGPT, do these steps:

1. In ChatGPT, open **Settings** › **Plugins**.
2. Select **Google Drive**.
3. Open the more options menu (•••) of your Google Account.
4. Select **Disconnect**.

The spreadsheet stays in your Google Drive.

## If there is a problem

### If Google Drive is not in Plugins

The Google Drive app is not available for your plan, your location or your workspace.

1. If you use a ChatGPT workspace, ask your administrator to make the Google Drive app available.
2. Read the [OpenAI help page for the Google Drive app](https://help.openai.com/en/articles/10929079).

### If ChatGPT finds the file but does not read the rows

ChatGPT found the name of the file, but it did not get the contents.

1. On a computer, open the spreadsheet in Google Sheets.
2. Copy the URL from the address bar of the browser.
3. In ChatGPT, start a new chat with Google Drive.
4. Paste the URL, then tell ChatGPT to read that file through Google Drive.

### If the answers do not include your new transactions

The spreadsheet does not have the new transaction, or ChatGPT did not read the file again.

1. Open the spreadsheet **WalletFeed Transactions** in Google Sheets. Look for the new transaction.
2. If the transaction is in the spreadsheet, start a new chat in ChatGPT. ChatGPT then reads the file again.
3. In the new chat, paste the prompt again, then ask again.
4. If the transaction is not in the spreadsheet, open WalletFeed on your iPhone. WalletFeed sends the new transactions.
5. Look in the spreadsheet again.

### If the totals are not correct

ChatGPT did not read all the rows, or it used the wrong rows.

1. Tell ChatGPT to list the rows that it used for the total.
2. Compare the rows with the spreadsheet.
3. Ask about a shorter period, for example one month.

## FAQ

### Does WalletFeed send my transactions to ChatGPT?

No. WalletFeed sends your transactions only to the spreadsheet in your Google Drive. ChatGPT reads the spreadsheet when you ask about it.

### Can ChatGPT read my Apple Card without the spreadsheet?

Possibly. ChatGPT has Finances. [ChatGPT Finances or a Google Sheet that you keep](#chatgpt-finances-or-a-google-sheet-that-you-keep) gives what OpenAI documents and what users report.

### Can ChatGPT change the spreadsheet?

With the permissions for it, the Google Drive app can edit files. Do not let ChatGPT change column A, **WalletFeed ID**, because WalletFeed uses it to find each row again.

### Does ChatGPT get my new transactions?

Yes, when WalletFeed updates the spreadsheet. When WalletFeed is not open, iOS decides when WalletFeed runs. Expect the change in about 1 hour or less. If [Background Sync](/docs/background-sync/) is on, WalletFeed then sends the change.

> **Note:** ChatGPT is a trademark of its owner. WalletFeed has no affiliation with OpenAI, and OpenAI does not endorse WalletFeed.

[Download WalletFeed on the App Store](https://apps.apple.com/app/apple-store/id6827429675?pt=125538749&ct=site&mt=8&ppid=8cf35fa5-e377-4e63-a21f-63da47703d25)
