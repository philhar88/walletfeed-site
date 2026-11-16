+++
title = "How to ask ChatGPT about your Apple Card transactions"
nav_title = "ChatGPT"
seo_title = "Ask ChatGPT about your Apple Card transactions"
description = "Ask ChatGPT about your Apple Card transactions. WalletFeed keeps a Google Sheet up to date, and ChatGPT reads it with its Google Drive app."
group = "AI chatbots"
order = 20
related = ["guides/ask-ai-about-apple-card-spending", "guides/apple-card-to-google-sheets", "guides/apple-card-to-claude", "docs/background-sync"]
updated = 2026-11-16
+++

To ask ChatGPT about your Apple Card transactions, connect Google Drive in ChatGPT, then ask about the spreadsheet that WalletFeed keeps up to date. WalletFeed reads your Apple Card, Apple Cash and Savings transactions on your iPhone and sends them to Google Sheets.

WalletFeed does not send your transactions to ChatGPT. ChatGPT reads the spreadsheet from your Google Drive when you ask about it.

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

   A very early version of the ChatGPT app can show **Apps** in place of **Plugins**.

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

   Result: ChatGPT tells you the number of rows and the first and the last date in the spreadsheet.

6. In the same chat, ask about your transactions.

## Prompt to start with

Copy this prompt, then paste it in the chat. [The full prompt](/guides/ask-ai-about-apple-card-spending/#prompt-to-start-with) also gives each column.

```
Read the Google Sheets spreadsheet "WalletFeed Transactions" in my Google Drive, tab "Transactions". Each row is one transaction from my Apple Card, Apple Cash or Savings account. In Amount, money out is negative and money in is positive. Spending is the rows with a negative Amount, shown as positive numbers. Payments to my Apple Card and transfers between my accounts are not spending. Use the Date column for periods. Pending is TRUE for a pending transaction. Ignore WalletFeed ID. Show the totals and the rows that you used. First, tell me the number of rows and the first and the last date.
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

The OpenAI help page says that the use of apps can count toward the limits of your ChatGPT plan.

## Privacy

- WalletFeed sends your transactions from your iPhone to Google only. WalletFeed has no account, and no WalletFeed server keeps your transactions or keys.
- With the Google Drive app, ChatGPT can open the files that your Google Account can open, not only the spreadsheet.
- For Free, Go, Plus and Pro users, OpenAI can use data from apps to train its models if **Improve the model for everyone** is on.
- For Business, Enterprise and Edu workspaces, OpenAI does not use data from apps to train models by default.

The OpenAI help pages gave these rules on November 16, 2026. The rules can change.

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

WalletFeed did not update the spreadsheet after the last change in Wallet.

1. On your iPhone, open WalletFeed.

   Result: WalletFeed sends the changes in seconds.

2. Tap **Settings** (the gear button) at the top of the screen.
3. Tap **Sync Now**.
4. In ChatGPT, start a new chat and ask again.

### If the totals are not correct

ChatGPT did not read all the rows, or it used the wrong rows.

1. Tell ChatGPT to list the rows that it used for the total.
2. Compare the rows with the spreadsheet.
3. Ask about a shorter period, for example one month.

## FAQ

### Does WalletFeed send my transactions to ChatGPT?

No. WalletFeed sends your transactions only to the spreadsheet in your Google Drive. ChatGPT reads the spreadsheet when you ask about it.

### Can ChatGPT read my Apple Card without the spreadsheet?

Possibly. ChatGPT has Finances, which connects financial accounts. Users and news reports from July 2026 say that the ChatGPT iPhone app can also connect Apple Card, Apple Cash and Savings from Wallet. On November 16, 2026, the [OpenAI help page for Finances](https://help.openai.com/en/articles/20001222) did not give Apple Card. For the accounts and the plans that Finances supports, refer to that page.

The WalletFeed spreadsheet is for you if you want a spreadsheet that you keep, or if you also use a different chatbot.

### Can ChatGPT change the spreadsheet?

With the permissions for it, the Google Drive app can edit files. Do not let ChatGPT change column A, **WalletFeed ID**, because WalletFeed uses it to find each row again.

### Does ChatGPT get my new transactions?

Yes, when WalletFeed updates the spreadsheet. When WalletFeed is not open, iOS starts WalletFeed approximately 1 hour or less after a change in Wallet. If [Background Sync](/docs/background-sync/) is on, WalletFeed then sends the change.

> **Note:** ChatGPT is a trademark of its owner. WalletFeed has no affiliation with OpenAI, and OpenAI does not endorse WalletFeed.

<!--
Sources, checked 2026-11-16:
- https://help.openai.com/en/articles/10929079 "Google Drive app and setup in ChatGPT" (updated 25 days ago): connect steps (Plugins or Apps, connect, Google sign-in, permissions), availability by plan/location/workspace, Sheets via the Google Drive app, "paste the file's link" troubleshooting.
- https://help.openai.com/en/articles/11487775 "Connected apps in ChatGPT": Settings > Plugins, Install plugin, Connect, @ mention or +, approval before reading, old iOS/Android versions show Apps, training rules for Free/Plus/Go/Pro vs Business/Enterprise/Edu, plan limits.
- https://help.openai.com/en/articles/20001494 "Connecting and managing app accounts in ChatGPT": "ChatGPT needs all requested permissions" > Try again > Select all; disconnect under Settings > Plugins.
- https://help.openai.com/en/articles/20001256 "Plugins in ChatGPT" (updated 18 days ago): Plugins on web, desktop and mobile.
- https://help.openai.com/en/articles/20001222 "Finances in ChatGPT": Plaid and Experian, Free/Go/Plus/Pro in the US; the page does not list Apple Card.
- Not verified: a plan list for the Google Drive app (the help page gives none); exact mobile menu names beyond Settings > Plugins.
-->
