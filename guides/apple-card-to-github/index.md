# Send Apple Card transactions to GitHub

WalletFeed writes your Apple Card, Apple Cash and Savings transactions from your iPhone to a private GitHub repository. Each month has one file, in Beancount, hledger or Ledger, or CSV format. WalletFeed updates the file of the month with new and changed transactions, a maximum of one time each day until you change **Send**. You connect GitHub with **Sign In with GitHub**, or with a token that you make in GitHub.

## Before you start

You must have these items:

- An iPhone with iOS 26 or a newer version
- WalletFeed, with [access to your Wallet accounts](/docs/wallet-accounts/)
- [WalletFeed Pro](/docs/walletfeed-pro/) (a subscription with a 1-week free trial, or a one-time Lifetime purchase)
- A GitHub account with a verified email address
- A private repository in GitHub with one or more files, for example a README file. You can use the repository of your ledger.

WalletFeed is available only in the US. WalletFeed writes only to private repositories. It does not write to a public repository or to an internal repository of an enterprise.

## Step 1: Open the GitHub form in WalletFeed

1. On your iPhone, open WalletFeed.
2. Tap **Destinations**.
3. Tap **+** at the top of the screen.

   ![The Destinations screen with no destinations, and the + icon at the top.](https://walletfeed.app/guides/apple-card-to-github/walletfeed-destinations-empty-pro.webp)

4. In the search field, type `GitHub`.
5. Tap **GitHub**.
6. If WalletFeed shows **WalletFeed Pro**, get [WalletFeed Pro](/docs/walletfeed-pro/).

   Result: After you get WalletFeed Pro, WalletFeed shows the GitHub form.

## Step 2: Connect WalletFeed to GitHub

GitHub gives a sign-in to an app only through a server. Thus, for this step, your iPhone uses the WalletFeed sign-in service. The sign-in service completes the sign-in and keeps nothing. Your transactions go from your iPhone directly to GitHub.

With **Sign In with GitHub**, these conditions apply:

- WalletFeed gets access only to the repositories that you select. In these repositories, WalletFeed can read and write contents, pull requests and issues.
- WalletFeed keeps the sign-in in the Keychain on your iPhone. The sign-in does not go to iCloud Keychain or to your other devices.
- The sign-in has no expiration date for you to monitor. When the sign-in expires, WalletFeed gets a new sign-in from GitHub.
- You can remove WalletFeed in GitHub (refer to [Remove WalletFeed in GitHub](#remove-walletfeed-in-github)).

To use a token, refer to [Use a token instead](#use-a-token-instead).

1. On the GitHub form in WalletFeed, tap **Sign In with GitHub**.
2. If iOS shows "“WalletFeed” Wants to Use “github.com” to Sign In", tap **Continue**.
3. If GitHub shows its sign-in page, type your GitHub email address and password.
4. On the GitHub page, give approval to WalletFeed.

   Result: WalletFeed shows **Signed In**. Until WalletFeed has a repository, it also shows "WalletFeed reaches no private repository yet. Tap Choose Repositories."

5. Tap **Choose Repositories**.
6. On the GitHub page, select **Only select repositories**.
7. Select your repository.
8. Tap **Install**.

   Result: WalletFeed shows **Repository** and **Branch**.

## Step 3: Select the repository and add GitHub

1. If **Repository** does not show your repository, select it in **Repository**.
2. In **Branch**, select the branch for the files.

   WalletFeed starts with the default branch of the repository.

3. In **Format**, select **Beancount**, **hledger or Ledger** or **CSV**.
4. If you keep files in a different folder, change **Path**.

   For example, `transactions/{yyyy}/{yyyy}-{mm}.beancount` gives `transactions/2026/2026-10.beancount` for October 2026. **Path** must contain `{yyyy}` and `{mm}`.

5. To use a different commit message, type the message in **Commit Message**.

   If **Commit Message** is empty, the message is like "Add Apple Card transactions for October 2026". You can use `{yyyy}`, `{mm}` and `{month}` in the message.

6. In **Send**, select **Each Transaction**, **Hourly**, **Daily** or **Monthly**.

   WalletFeed starts with **Daily**. For more information, refer to [Options for Send](#options-for-send).

7. If you selected **Monthly**, select **Commit**, **Pull Request** or **Commit and Issue** in **Each Month**.

   For more information, refer to [Each month in GitHub](#each-month-in-github).

8. For Beancount or hledger, change the account names in **Accounts** if your ledger uses different names.

   For more information, refer to [The accounts in each file](#the-accounts-in-each-file).

9. Tap **Add**.

   Result: WalletFeed makes sure that it can write to the repository. WalletFeed does not change the repository for this.

10. When WalletFeed shows **Send Transactions to GitHub?**, tap **Send**.

    If you tap **Cancel**, WalletFeed removes the new destination.

If **Send** is not **Monthly**, the **Send Transactions to GitHub?** message tells you that the repository receives "one file a month, kept up to date". With **Monthly**, it tells you that the repository receives "one file 5 days after each month ends". The message also tells you the data in each file and the accounts. It gives the start date, or "including earlier ones" if **Initial History** is **All**.

In **Destinations**, the destination has the name **GitHub · your-name/your-repository**.

## Step 4: Add the accounts to your ledger

The files from WalletFeed do not open the accounts.

For Beancount, your ledger must open each account one time. Add an `open` line for each account in your main file, for example:

```beancount
2020-01-01 open Liabilities:AppleCard
2020-01-01 open Assets:AppleCash
2020-01-01 open Assets:AppleSavings
2020-01-01 open Expenses:Uncategorized
2020-01-01 open Income:Uncategorized
2020-01-01 open Assets:Transfers
```

Then add an `include` line with a pattern for the month files, for example `include "transactions/**/*.beancount"`.

For hledger, add an `include` line with a pattern for the month files, for example `include transactions/**/*.journal`. If you use strict mode, also add an `account` line for each account, for example `account liabilities:apple card`.

For Ledger, add an `include` line for each month file, for example `include transactions/2026/2026-10.journal`. Ledger does not accept a pattern in an `include` line.

If an account name has `{category}`, open the account for each WalletFeed category. For example, `Expenses:{category}` gives `Expenses:Dining`, `Expenses:Groceries` and `Expenses:Other`.

> **Caution:** The pattern `transactions/**/*.beancount` also includes the test file from **Send Test** if you merge it. Refer to [Send a test](#send-a-test).

## Step 5: Find the files in GitHub

1. On a computer, open your repository in GitHub.
2. Open the folder of the files, for example `transactions/2026`.

   Result: The folder has one file for each month, for example `2026-11.beancount` for November 2026.

If **Send** is not **Monthly**, WalletFeed writes the files after you add the destination. It writes one file for each month from the start date, and this month is one of them. Then WalletFeed updates the file of a month when the month has a new or changed transaction (refer to [Options for Send](#options-for-send)).

With **Monthly**, WalletFeed writes the files for the previous months after you add the destination. It writes the file for each subsequent month 5 days after the month ends.

If a month has no transactions for the destination, WalletFeed does not write a file for that month.

## Use a token instead

You can also connect WalletFeed to GitHub with a personal access token. A token has an expiration date, and you replace the token before that date (refer to [Replace the token](#replace-the-token)).

The GitHub documentation tells you that personal access tokens are "intended to access GitHub resources on behalf of yourself". For long-lived integrations, GitHub recommends a GitHub App. **Sign In with GitHub** uses the GitHub App of WalletFeed (refer to [Step 2](#step-2-connect-walletfeed-to-github)).

- With the token, WalletFeed reads your private repositories and their branches. In the repository that you select, WalletFeed writes the month files. It also opens pull requests or issues, if you select them.
- WalletFeed also makes branches that start with `walletfeed/`, for example for **Send Test**.
- You can delete the token in GitHub (refer to [Delete the token in GitHub](#delete-the-token-in-github)).

> **Note:** If the repository is in an organization, the organization can make approval necessary for your token. Until an owner of the organization gives approval, the token gets access only to public repositories.

### Your token stays on your iPhone

- WalletFeed keeps the personal access token in the Keychain on your iPhone. iOS encrypts the Keychain.
- The personal access token does not go to iCloud Keychain or to your other devices.
- WalletFeed has no account, and no WalletFeed server keeps the personal access token. No person at WalletFeed can see or get the personal access token.
- Your iPhone sends the personal access token only to GitHub, in each request to GitHub.
- When you delete the destination, WalletFeed deletes the personal access token from your iPhone. You can also delete the token in GitHub.

### Make a personal access token in GitHub

1. Open the GitHub form in WalletFeed (refer to [Step 1](#step-1-open-the-github-form-in-walletfeed)).
2. Tap **Use a Token Instead**.
3. In **Send**, select **Each Transaction**, **Hourly**, **Daily** or **Monthly**.
4. If you selected **Monthly**, select **Commit**, **Pull Request** or **Commit and Issue** in **Each Month**.

   Do steps 3 and 4 first, because the token gets the permissions for this selection.

5. At the end of the GitHub form, tap **Create Token**.

   Result: GitHub opens the page for a new fine-grained token. The page has the name WalletFeed, an expiration of 366 days and the permission **Contents**. For **Pull Request**, it also has the permission **Pull requests**. For **Commit and Issue**, it also has the permission **Issues**.

6. If GitHub shows **Sign in**, type your GitHub email address and password.
7. If the repository is in an organization, select the organization in **Resource owner**.
8. In **Repository access**, select **Only select repositories**.
9. Select your repository.
10. Tap **Generate token**.
11. Copy the token.

    The token starts with `github_pat_`.

### Paste the token in WalletFeed

1. In WalletFeed, paste the token in **Personal Access Token**.

   Result: WalletFeed shows **Repository** and **Branch**. **Repository** shows the private repository with the most recent change.

2. Do the steps in [Step 3](#step-3-select-the-repository-and-add-github).

To show **Sign In with GitHub** again before you tap **Add**, tap **Sign In with GitHub Instead**.

## Options for Send

**Send** sets the time that GitHub gets the transactions:

| **Send** | What GitHub gets |
| --- | --- |
| **Each Transaction** | A commit on the branch each time that WalletFeed sends a change to the file of a month. |
| **Hourly** | A maximum of one commit each hour for the file of a month. |
| **Daily** | A maximum of one commit each day for the file of a month. |
| **Monthly** | The file of a month one time, 5 days after the month ends. **Each Month** sets how GitHub gets the file. |

A new destination starts with **Daily**. A destination from before WalletFeed 1.3 keeps **Monthly**. You can change **Send** after you add the destination (refer to [Change Send](#change-send)).

With **Each Transaction**, **Hourly** and **Daily**, each commit updates the file of the month. With **Each Transaction**, one purchase is usually two commits: one when Wallet shows the purchase, and one when the purchase posts. For fewer commits, use **Hourly** or **Daily**.

With **Hourly** and **Daily**, WalletFeed holds a change that comes before the hour or the day ends. WalletFeed sends the change the first time that it sends changes after the hour or the day ends. Thus, the file can get a change one hour or one day after the change in Wallet. The file gets all the changes.

> **Caution:** With **Each Transaction**, **Hourly** or **Daily**, do not change or delete the file of a month before the month ends. If you change or delete the file, WalletFeed stops its updates of that month. The file then does not get the remaining transactions of the month.

When WalletFeed stops the updates of a month, the destination shows "November 2026 changed in the repository, so WalletFeed stopped updating it." one time. If you change the files, for example to add tags or balance assertions, do one of these:

- Make your changes after the month ends.
- Keep your changes in a different file.
- Set **Send** to **Monthly**.

With **Each Transaction**, **Hourly** and **Daily**, these conditions also apply:

- If **Commit Message** is empty, the first commit of a month has a message like "Add Apple Card transactions for November 2026". Each subsequent commit has a message like "Update Apple Card transactions for November 2026".
- Each commit can start the workflows of your repository for a push. To stop these workflows, put `[skip ci]` in **Commit Message**.
- GitHub refuses a commit to a branch that has protection. For this branch, set **Send** to **Monthly**. Then select **Pull Request** in **Each Month**.

## Each month in GitHub

With **Send** set to **Monthly**, **Each Month** has three options:

| Option | What GitHub gets 5 days after the month ends | Token permissions |
| --- | --- | --- |
| **Commit** | A commit with the file of the month, on the branch | **Contents** |
| **Pull Request** | A branch with the file of the month, and a pull request to your branch, for example "Apple Card transactions, October 2026" | **Contents** and **Pull requests** |
| **Commit and Issue** | The commit, then an issue with the same title, a hyperlink to the commit and the text of the file | **Contents** and **Issues** |

With **Sign In with GitHub**, WalletFeed has the permissions for the three options. WalletFeed shows **Each Month** only while **Send** is **Monthly**.

If your branch has protection or if a workflow examines each pull request, use **Pull Request**. The names of the branches from WalletFeed start with `walletfeed/`.

GitHub does not send you an email for a pull request or an issue that your token opens. To get these emails, select the option for your own updates in the notification settings of GitHub.

If you change **Each Month** on the screen of the destination, the change applies to the next months. If the token does not have the permission for the new option, add the permission to the token in GitHub.

### Find the month in GitHub

With **Monthly**, WalletFeed writes the file for a month only one time. It writes the file 5 days after the end of the month. During these 5 days, most pending charges from the end of the month post.

1. Wait until the 6th day of the next month.
2. On your iPhone, open WalletFeed.

   Result: WalletFeed writes the file for the month that ended. For example, on November 6, 2026, it writes `transactions/2026/2026-10.beancount`.

3. On a computer, open your repository in GitHub.

   With **Commit**, the file is on the branch. With **Pull Request**, a pull request has the file. With **Commit and Issue**, an issue has a hyperlink to the file.

WalletFeed also writes the file on that day or after it when one of these occurs:

- WalletFeed gets a change from Wallet with [Background Sync](/docs/background-sync/).
- An [automation](/docs/siri-and-shortcuts/#send-transactions-with-an-automation) starts.
- iOS starts WalletFeed while your iPhone is on a charger.

## The accounts in each file

Each transaction has two postings. The first posting is the Wallet account. The second posting is one of these accounts:

| Transaction | Account |
| --- | --- |
| A transfer or a payment, in the two directions | **Transfers** |
| A refund | **Money Out** |
| A different purchase, fee or charge | **Money Out** |
| A different credit, for example Daily Cash or interest | **Money In** |

The two sides of a transfer between two Wallet accounts go to **Transfers**, and they cancel. When you add the payment from your bank to your ledger, use the same **Transfers** account. If **Transfers** has a balance, one side of a transfer is not in your ledger.

An Apple Cash payment to a person or from a person can also go to **Transfers**. This payment has only one side in Wallet, so it stays in **Transfers**. Move it to the correct account in your ledger.

These are the account names at the start:

| Row | Beancount | hledger or Ledger |
| --- | --- | --- |
| **Apple Card** | `Liabilities:AppleCard` | `liabilities:apple card` |
| **Apple Cash** | `Assets:AppleCash` | `assets:apple cash` |
| **Savings** | `Assets:AppleSavings` | `assets:apple savings` |
| **Money Out** | `Expenses:Uncategorized` | `expenses:unknown` |
| **Money In** | `Income:Uncategorized` | `income:unknown` |
| **Transfers** | `Assets:Transfers` | `assets:transfers` |

For hledger or Ledger, **Currency** sets how dollars show: `USD` or `$`. Use the same symbol as your journal. hledger counts `$` and `USD` as two different commodities.

## Data that GitHub receives

The collaborators of the repository and its GitHub Actions workflows can read the files that WalletFeed writes. Git keeps each version of a file in the history of the repository. A pull request or an issue from WalletFeed shows the number of transactions and the total of the month. An issue also shows the file. GitHub can send these to the people who watch the repository in an email.

Each file contains the transactions of one month from the Wallet accounts for the destination. A Beancount or hledger file starts with a comment line, for example `; Apple Card transactions, October 2026, from WalletFeed`. The transactions are in date sequence.

| From Wallet | In the file |
| --- | --- |
| Date | The date of the transaction on your iPhone, for example `2026-10-28` |
| Status | `*` for a posted transaction, `!` for a pending charge |
| Merchant | The payee. If Wallet has no merchant name, the payee is the description. |
| Description | In Beancount, the narration, if it is different from the payee |
| Amount and currency | The two postings. Purchases have a minus sign on the Wallet account. |
| Category | `category:`, if the category is not **Other** |
| Card statement text | `statement:`, if it is different from the payee |
| Amount in a different currency | `foreign:`, for example `6.20 EUR` |
| Merchant category code | `mcc:`, for example `"5812"` in Beancount and `5812` in hledger |
| Posted date | If the transaction posted on a different day: in Beancount `posted:`, and in hledger the date of the Wallet account posting, for example `; [2026-10-05]` |
| WalletFeed ID | `walletfeed-id:` |

In hledger and Ledger, the Wallet account shows a transaction on the day that it posted. The expense shows it on the day of the transaction.

A CSV file has the columns of a WalletFeed CSV file, with the newest transaction first. For the columns, refer to [CSV files](/guides/apple-card-to-csv/).

With **Monthly**, WalletFeed does not change a file after it writes the file. Thus, you can change the accounts, add tags and add balance assertions in the file. With the other options of **Send**, read the caution in [Options for Send](#options-for-send) before you change a file.

## New and changed transactions

WalletFeed puts each transaction in the file for the month of the transaction date. A pending charge has the flag `!`, and a posted transaction has the flag `*`.

If a file for the month is in the repository before WalletFeed writes it, WalletFeed does not change that file. The destination then shows "October 2026 was already in the repository, so WalletFeed left it." A file that WalletFeed wrote before for that month does not cause this message.

### Changes with Each Transaction, Hourly or Daily

WalletFeed updates the file of a month, with one commit, when one of these occurs:

- Wallet adds a transaction to the month, which can be a previous month.
- A pending charge posts.
- The amount of a transaction changes.
- A pending charge becomes a declined charge, or Wallet removes a transaction. WalletFeed then removes the transaction from the file.

With **Each Transaction**, GitHub gets the commit at these times:

- While WalletFeed is open, GitHub gets the commit in seconds.
- When WalletFeed is not open, iOS starts WalletFeed approximately 1 hour or less after a change in Wallet. If [Background Sync](/docs/background-sync/) is on in **Settings** › **Sync**, WalletFeed then makes the commit.

With **Hourly** and **Daily**, WalletFeed holds the change if the file got a commit in the same hour or on the same day. Refer to [Options for Send](#options-for-send).

If a change in Wallet does not change the text of the file, WalletFeed makes no commit.

WalletFeed updates a file only while the repository has the file that WalletFeed wrote. If a person or a workflow changes or deletes the file, WalletFeed stops its updates of that month. Refer to the caution in [Options for Send](#options-for-send).

### Changes with Monthly

WalletFeed writes each file only one time. Thus, the file does not get changes after that time.

Compare the transactions that have the flag `!` with your statement, and make these changes in your ledger:

- If the amount of a pending charge changes when the charge posts, change the amount.
- If a pending charge becomes a declined charge after WalletFeed writes the file, delete the charge.
- If Wallet removes a transaction after WalletFeed writes the file, delete the transaction.
- If Wallet adds a transaction to a month after WalletFeed writes the file, add the transaction.

## Send previous transactions

A new GitHub destination also receives previous transactions from the start date in **Settings** › **Sync** › **Initial History**. **Initial History** is **All** until you change it. WalletFeed moves the start date to the first day of its month. Thus, each file has all the transactions of its month.

If you added previous months to your ledger by hand, set the start in **Initial History** after the last of these months. Do this before you add the destination.

WalletFeed writes the files for the previous months after you add the destination, one month at a time, with 10 seconds between the months. If **Send** is not **Monthly**, it also writes the file for this month.

With **Monthly** and **Pull Request**, all the previous months go in one pull request, for example "Transactions before October 2026". With **Monthly** and **Commit and Issue**, the previous months get no issues.

Each previous month is one commit. If your repository has a workflow for each push, add `[skip ci]` to **Commit Message** before you add the destination.

To get files for the previous months that have no file in the repository, use [Send History](/docs/send-history/):

1. In WalletFeed, tap **Destinations**.
2. Tap the GitHub destination.
3. Tap **Send History**.
4. Tap **30 Days**, **90 Days**, **1 Year** or **All**.

WalletFeed then writes a file for each previous month in the period, if the repository has no file for that month.

To write a month again with new account names, do these steps:

1. In GitHub, delete the file for the month.
2. In WalletFeed, delete the destination.
3. Add the destination again, with the new account names.

## Send a test

**Send Test** writes a file with a test purchase to the branch `walletfeed/…/test`, not to your branch.

1. In WalletFeed, tap **Destinations**.
2. Tap the GitHub destination.
3. Tap **Send Test**.

   Result: The test branch gets the file `walletfeed-test.beancount` (or `.journal` or `.csv`), in the folder of the month files. With **Pull Request**, GitHub shows the pull request "WalletFeed test". With **Commit and Issue**, GitHub shows the issue "WalletFeed test".

4. If GitHub shows the pull request "WalletFeed test", close it. Do not merge it.
5. After the test, delete the test branch in GitHub.

## Change or remove the destination

### Change Send

1. In **Destinations**, tap the destination.
2. In **Send**, select **Each Transaction**, **Hourly**, **Daily** or **Monthly**.

After you change **Send** from **Monthly** to a different option, WalletFeed writes the file of a month at the next change to that month. WalletFeed does not update a file that it wrote with **Monthly**.

After you select **Monthly**, WalletFeed updates the file of this month one more time, 5 days after the month ends. It does this only if you did not change the file. With **Pull Request**, the file on your branch stays as it is.

### Send only some transactions

1. In **Destinations**, tap the destination.
2. Set **Filter** to on.
3. Set **Include**, **Minimum**, **Accounts**, **Categories** or **Exclude**.

WalletFeed uses the new [filter](/docs/choose-what-to-send/) for the files that it writes after the change. The filter of a GitHub destination always includes pending charges, so that each charge gets into a file.

### Change the commit message or the accounts

1. In **Destinations**, tap the destination.
2. Change **Each Month**, **Commit Message**, the names in **Accounts** or **Currency**.

If **Send** is not **Monthly**, the change applies from the next commit. After you change an account name or **Currency**, the next commit to a month writes the full file of that month again.

With **Monthly**, the change applies to the months that WalletFeed did not write.

To use a different repository, branch, format or path, delete the destination and add it again.

### Stop the destination for a time

1. In **Destinations**, tap the destination.
2. Set **Enabled** to off.

When you set **Enabled** to on again, WalletFeed writes the changes from that time. With **Monthly**, it writes the files for the months that ended during that time.

### Change the repositories of WalletFeed

If you used **Sign In with GitHub**, the screen of the destination shows **Choose Repositories**.

1. In **Destinations**, tap the destination.
2. Tap **Choose Repositories**.
3. On the GitHub page, select the repositories for WalletFeed.

A destination writes to one repository only. To write to a different repository, delete the destination and add it again.

### Replace the sign-in

If you used **Sign In with GitHub**, the screen of the destination shows **Sign In Again**.

1. In **Destinations**, tap the destination.
2. Tap **Sign In Again**.
3. On the GitHub page, get access to the GitHub account of the destination.

WalletFeed keeps the new sign-in only if the sign-in can write to the repository of the destination.

### Make a new token for the destination

1. On a computer, open GitHub.
2. Click your profile picture.
3. Click **Settings**.
4. Click **Developer settings** › **Personal access tokens** › **Fine-grained tokens**.
5. Click **Generate new token**.
6. In **Token name**, type `WalletFeed`.
7. In **Repository access**, select **Only select repositories**. Then select the repository of the destination.
8. In **Permissions**, set **Contents** to **Read and write**.
9. If **Send** is **Monthly** and **Each Month** is **Pull Request**, set **Pull requests** to **Read and write**.
10. If **Send** is **Monthly** and **Each Month** is **Commit and Issue**, set **Issues** to **Read and write**.
11. Click **Generate token**.
12. Copy the token.

### Replace the token

If you used a token, do these steps before the token expires. The screen of the destination shows the date in **Token Expires**, if GitHub gives it. When 14 days or less remain, the destination shows "Your GitHub token expires on November 5, 2027. Replace the token." (with the date of your token).

1. Make a new token (refer to [Make a new token for the destination](#make-a-new-token-for-the-destination)).
2. In WalletFeed, tap **Destinations**.
3. Tap the destination.
4. Tap **Replace Token**.
5. Paste the new token.
6. Tap **Replace**.

   WalletFeed keeps the new token only if the token can write to the repository of the destination.

### Remove GitHub from WalletFeed

1. In **Destinations**, tap the destination.
2. Tap **Delete**.
3. Tap **Delete** again.

   The files, pull requests and issues stay in GitHub.

If you used **Sign In with GitHub**, WalletFeed also deletes the sign-in from your iPhone. In GitHub, WalletFeed stays in **Installed GitHub Apps** until you remove it (refer to [Remove WalletFeed in GitHub](#remove-walletfeed-in-github)).

### Remove WalletFeed in GitHub

If you used **Sign In with GitHub**, do these steps to remove the access of WalletFeed to your repositories:

1. On a computer, open GitHub.
2. Click your profile picture.
3. Click **Settings**.
4. Click **Applications**.
5. In **Installed GitHub Apps**, remove WalletFeed.
6. In **Authorized GitHub Apps**, remove WalletFeed.

After you remove WalletFeed, WalletFeed cannot write to GitHub with the sign-in.

### Delete the token in GitHub

1. On a computer, open GitHub.
2. Click your profile picture.
3. Click **Settings**.
4. Click **Developer settings** › **Personal access tokens** › **Fine-grained tokens**.
5. Click the WalletFeed token.
6. Click **Delete**.

After you delete the token, WalletFeed cannot write to GitHub with it.

## If there is a problem

First, use **Send Test** (refer to [Send a test](#send-a-test)). If the test branch gets the test file, WalletFeed can write to the repository.

In the GitHub form, WalletFeed examines the token again when the token changes. To make WalletFeed examine the same token again, delete the token in **Personal Access Token**, then paste it again.

### If WalletFeed shows "WalletFeed reaches no private repository yet"

You used **Sign In with GitHub**, and WalletFeed has no private repository where your account can write.

1. Tap **Choose Repositories**.
2. On the GitHub page, select **Only select repositories**.
3. Select your private repository.
4. Tap **Install**.

### If the destination shows "Signed out. Open the destination and tap Sign In Again."

GitHub stopped the sign-in. This occurs, for example, if the destination sent nothing to GitHub for 6 months.

1. In **Destinations**, tap the destination.
2. Tap **Sign In Again**.
3. On the GitHub page, get access to the GitHub account of the destination.

### If the destination shows "The repository is gone, or WalletFeed can't reach it"

You used **Sign In with GitHub**. The repository is not in GitHub, or it is not one of the repositories of WalletFeed.

1. In **Destinations**, tap the destination.
2. Tap **Choose Repositories**.
3. On the GitHub page, select the repository of the destination.

### If WalletFeed shows "Token rejected (HTTP 401)"

The token is not correct, or GitHub deleted it.

1. Make a new token (refer to [Make a personal access token in GitHub](#make-a-personal-access-token-in-github)).
2. Paste the new token in **Personal Access Token**.

### If WalletFeed shows "The token reaches no private repository"

The token has no access to a private repository, or the organization did not give approval for the token.

1. On a computer, open the token in GitHub.
2. In **Repository access**, add your repository.
3. If the repository is in an organization, ask an owner of the organization for approval.
4. In WalletFeed, delete the token in **Personal Access Token**, then paste it again.

### If WalletFeed shows "This repository is empty"

GitHub cannot add a branch to a repository that has no files.

1. In GitHub, add a README file to the repository.
2. In WalletFeed, delete the token in **Personal Access Token**, then paste it again.

### If WalletFeed shows "The token can't write files"

The token does not have the permission **Contents** with **Read and write**.

1. On a computer, open the token in GitHub.
2. In **Permissions**, set **Contents** to **Read and write**.
3. Click **Update**.
4. In WalletFeed, tap **Add** again. If you added the destination before, WalletFeed tries again after some time.

### If WalletFeed shows "The token can't open pull requests" or "The token can't open issues"

The token does not have the permission for **Pull Request** or **Commit and Issue**.

1. On a computer, open the token in GitHub.
2. In **Permissions**, set **Pull requests** or **Issues** to **Read and write**.
3. Click **Update**.
4. In WalletFeed, tap **Add** again. If you added the destination before, WalletFeed tries again after some time.

### If WalletFeed shows "The token can't write to private repositories"

The token is a classic token without the `repo` scope.

1. Make a fine-grained token (refer to [Make a personal access token in GitHub](#make-a-personal-access-token-in-github)).
2. Paste the new token in WalletFeed.

### If WalletFeed shows "GitHub refused the request"

GitHub did not accept the request for a different cause, for example a limit of your organization.

If you used a token, do these steps:

1. On a computer, open the token in GitHub.
2. Make sure that the token has access to the repository and has the permissions in [Each month in GitHub](#each-month-in-github).

If you used **Sign In with GitHub**, the message is "GitHub refused the request. Check your access to the repository in GitHub." Do this step:

1. In GitHub, make sure that your account can write to the repository.

### If WalletFeed shows "Another destination writes to this path"

A different GitHub destination writes to the same path in the same repository and branch.

1. Change **Path**, for example to `cash/{yyyy}/{yyyy}-{mm}.beancount`.

### If WalletFeed shows "Include {yyyy} and {mm}"

**Path** does not have `{yyyy}` and `{mm}`.

1. Change **Path**, for example to `transactions/{yyyy}/{yyyy}-{mm}.beancount`.

### If WalletFeed shows "WalletFeed can't write to this path"

GitHub or Git does not accept a file at the path. For example, the path starts with `/`, has `..` or `.git`, or starts with `.github/`.

1. Change **Path**, for example to `transactions/{yyyy}/{yyyy}-{mm}.beancount`.

### If WalletFeed shows "Shorten the path"

**Path** has more than 400 characters, or a folder name or the file name has more than 255 characters.

1. Change **Path** to a shorter path.

### If WalletFeed shows "Remove < > : | ? * and quotation marks from the path"

Git for Windows cannot use these characters in a file name.

1. Remove the characters from **Path**.

### If WalletFeed shows "Don't end a folder or file name with a space or a dot"

Git for Windows cannot use a folder name or a file name that ends with a space or a dot.

1. Remove the space or the dot from **Path**.

### If WalletFeed shows "Name every account"

A row in **Accounts** is empty.

1. Type an account name in each row of **Accounts**.

### If WalletFeed shows "Use {category} only in Money Out and Money In"

`{category}` is in **Apple Card**, **Apple Cash**, **Savings** or **Transfers**. WalletFeed puts the category only in **Money Out** and **Money In**.

1. Remove `{category}` from that row.

### If WalletFeed shows "Start with Assets, Liabilities, Equity, Income or Expenses"

A Beancount account name must start with one of these five words.

1. Change the account name, for example to `Expenses:Food`.

### If WalletFeed shows "Use letters, numbers and dashes. Start each part with a capital"

Beancount does not accept the account name. Each part between two colons must start with a capital letter or a number, and must not have spaces.

1. Change the account name, for example to `Expenses:FoodCourt`.

### If WalletFeed shows "Use single spaces, no semicolons, and don't start with ( or ["

hledger and Ledger do not accept the account name. The name has two spaces together, a semicolon, a tab or an empty part, or it starts with `(` or `[`.

1. Change the account name, for example to `expenses:food court`.

### If the GitHub form shows "main is protected"

Your branch has protection, or a rule of the repository accepts changes only in a pull request. If **Send** is not **Monthly**, the message is "main is protected. Set Send to Monthly, then choose Pull Request." With **Monthly**, the message is "main is protected, so GitHub may refuse commits. Choose Pull Request."

1. If **Send** is not **Monthly**, set **Send** to **Monthly**.
2. In **Each Month**, select **Pull Request**.

### If the GitHub form shows "main has rules that may refuse WalletFeed's commits"

A ruleset of the repository can refuse the file or the commit, for example its extension or its message.

1. In GitHub, open the rulesets of the repository.
2. Make sure that the rules accept the path and the commit message from WalletFeed.

### If the Each Month footer shows "GitHub's rules refuse new branches here"

A ruleset of the repository does not let WalletFeed make branches. **Pull Request** and **Send Test** make branches.

1. In **Each Month**, select **Commit**, or change the ruleset in GitHub to accept branches that start with `walletfeed/`.

### If the destination shows "GitHub refused the commit to main"

Your branch has protection, or a rule of the repository accepts changes only in a pull request. If **Send** is not **Monthly**, the message is "GitHub refused the commit to main. Set Send to Monthly, then choose Pull Request." With **Monthly**, the message is "GitHub refused the commit to main. Choose Pull Request under Each Month."

1. In **Destinations**, tap the destination.
2. If **Send** is not **Monthly**, set **Send** to **Monthly**.
3. In **Each Month**, select **Pull Request**.

### If the destination shows "A rule on main refused WalletFeed's commit"

A ruleset of the repository does not accept the file or the commit, for example its extension or its message.

1. In GitHub, open the rulesets of the repository.
2. Change the rule, or change **Commit Message** in WalletFeed.

### If the destination shows "A rule in your-name/your-repository refused WalletFeed's branch"

A ruleset of the repository does not let WalletFeed make branches. **Pull Request**, the previous months with **Pull Request**, and **Send Test** make branches.

1. In GitHub, open the rulesets of the repository.
2. Change the ruleset to accept branches that start with `walletfeed/`, or select **Commit** in **Each Month**.

### If the destination shows "Issues are off"

The repository does not have issues.

1. In GitHub, open the settings of the repository.
2. In **Features**, select **Issues**.

### If the destination shows that the repository is public or internal

WalletFeed writes only to private repositories.

1. In GitHub, make the repository private.

### If the destination shows that GitHub archived the repository

GitHub does not accept changes to an archived repository.

1. In GitHub, unarchive the repository.

### If the destination shows that the branch is gone

The branch of the destination is not in the repository.

1. Delete the destination.
2. Add the destination again, and select a branch.

### If the destination shows "The repository is gone, or the token can't reach it"

You used a token. GitHub deleted the repository, or the token has no access to it.

1. In GitHub, add the repository to the token in **Repository access**.
2. If the token has access, replace the token (refer to [Replace the token](#replace-the-token)).

### If the destination shows "The token expired" or "Your GitHub token expires"

The token is at the end of its expiration period, or it is near the end.

1. Make a new token (refer to [Make a new token for the destination](#make-a-new-token-for-the-destination)).
2. Replace the token (refer to [Replace the token](#replace-the-token)).

### If the destination shows "Authorize the token for your organization's single sign-on"

The organization uses single sign-on, and the token does not have authorization for it.

1. In GitHub, authorize the token for the organization. For the steps, refer to [GitHub's instructions for single sign-on](https://docs.github.com/en/authentication/authenticating-with-saml-single-sign-on/authorizing-a-personal-access-token-for-use-with-saml-single-sign-on).

### If the destination shows "GitHub's rate limit is reached"

GitHub accepts a limited number of requests in a period. WalletFeed sends the month again after some time.

1. Wait one hour, then open WalletFeed.

### If the destination shows "Rejected (HTTP 409)"

A different change to the same file or branch occurred at the same time. WalletFeed sends the month again after some time.

1. Wait some minutes, then open WalletFeed.

### If the destination shows "Authentication failed"

GitHub does not accept the token.

1. Replace the token (refer to [Replace the token](#replace-the-token)).

### If the destination shows "November 2026 changed in the repository"

With **Each Transaction**, **Hourly** or **Daily**, a person or a workflow changed or deleted the file of the month in the repository. WalletFeed stopped its updates of that month. The full message is "November 2026 changed in the repository, so WalletFeed stopped updating it." If the message has a number of months, for example "3 months changed in the repository, so WalletFeed stopped updating them.", it is the same for each of these months.

1. To keep your file, add the subsequent transactions of that month to the file by hand.
2. To get the file from WalletFeed again, delete the file in GitHub. Then delete the destination, and add it again.

To prevent this message, read the caution in [Options for Send](#options-for-send).

### If the destination shows "October 2026 was already in the repository"

The repository has a file at the path of the month, and WalletFeed did not change it. If the message has a number of months, for example "3 months were already in the repository", it is the same for each of these months.

1. If you made the file for the month, do nothing.
2. To get the file from WalletFeed for a month before the start of the destination, delete the file in GitHub. Then use **Send History** (refer to [Send previous transactions](#send-previous-transactions)).
3. To get the file from WalletFeed for a month after the start of the destination, delete the file in GitHub. Then delete the destination, and add it again.

### If Destinations shows "Sync Requires Pro"

You do not have WalletFeed Pro at this time. WalletFeed keeps the destination but does not write the files.

1. In **Destinations**, tap **Upgrade**.
2. If you got WalletFeed Pro before, tap **Restore Purchases**.
3. To get WalletFeed Pro for the first time, select a plan.

[Download WalletFeed on the App Store](https://apps.apple.com/app/apple-store/id6827429675?pt=125538749&ct=site&mt=8&ppid=67f05d46-993f-4df0-bf41-381c261854dd)
