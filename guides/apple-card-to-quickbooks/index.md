# Send Apple Card transactions to QuickBooks Online

WalletFeed sends your posted Apple Card, Apple Cash and Savings transactions from your iPhone to a credit card account in QuickBooks Online. You connect WalletFeed to your QuickBooks company, then WalletFeed adds each transaction as an expense or a credit.

You can also upload files from WalletFeed in QuickBooks Online. Refer to [Upload a file instead](#upload-a-file-instead).

## Before you start

You must have these items:

- An iPhone with iOS 26 or a newer version. WalletFeed is available only in the US.
- WalletFeed on your iPhone, with [access to your Apple Card](/docs/wallet-accounts/).
- [WalletFeed Pro](/docs/walletfeed-pro/) (a subscription with a 1-week free trial, or a one-time Lifetime purchase). You must have WalletFeed Pro to send transactions to QuickBooks Online.
- A QuickBooks Online company. Intuit supports apps with Simple Start, Essentials, Plus and Advanced.
- An admin user for that company. Only an admin can connect an app to the company.

> **Note:** QuickBooks Online has no API key. You connect WalletFeed with **Connect to QuickBooks**.

## Your sign-in stays on your iPhone

- WalletFeed keeps your QuickBooks sign-in in the Keychain on your iPhone. iOS encrypts the Keychain.
- Your QuickBooks sign-in does not go to iCloud Keychain or to your other devices.
- WalletFeed has no account, and no WalletFeed server keeps your QuickBooks sign-in. No person at WalletFeed can see or get your QuickBooks sign-in.
- Your iPhone sends your QuickBooks sign-in only to QuickBooks and to the WalletFeed sign-in service (refer to [Step 2](#step-2-connect-walletfeed-to-quickbooks)).
- When you delete the destination, WalletFeed deletes your QuickBooks sign-in from your iPhone. You can also remove WalletFeed from your QuickBooks company.

## Step 1: Open the QuickBooks Online form in WalletFeed

1. On your iPhone, open WalletFeed.
2. Tap **Destinations**.
3. Tap **+** at the top of the screen.

   ![The Destinations screen with no destinations, and the + icon at the top.](https://walletfeed.app/guides/apple-card-to-quickbooks/walletfeed-destinations-empty-pro.webp)

4. In the search field, type `QuickBooks`.
5. Tap **QuickBooks Online**.
6. If WalletFeed shows **WalletFeed Pro**, get [WalletFeed Pro](/docs/walletfeed-pro/).

   Result: After you get WalletFeed Pro, WalletFeed shows the QuickBooks Online form.

## Step 2: Connect WalletFeed to QuickBooks

QuickBooks gives a sign-in to an app only through a server. Thus, for this step, your iPhone uses the WalletFeed sign-in service. The sign-in service completes the sign-in and keeps nothing. Your transactions go from your iPhone directly to QuickBooks.

1. Tap **Connect to QuickBooks**.

   Result: WalletFeed opens the Intuit page.

2. On the Intuit page, get access to your Intuit account with your e-mail address and your password.
3. If the Intuit page shows a list of companies, select the company that receives your transactions.
4. Tap **Connect**.

   Result: WalletFeed shows **Signed In** and **Company**.

With this sign-in, WalletFeed can read and change the accounting data of the company. WalletFeed uses this access to get the name of the company and the list of your accounts. WalletFeed also makes an Apple Card account, and adds, changes and deletes the transactions that it sends.

## Step 3: Select the accounts in WalletFeed

1. In **Company**, make sure that WalletFeed shows the company that you selected.
2. In **Account**, select the credit card account that receives your transactions.

   If QuickBooks has a credit card account with the name Apple Card, WalletFeed selects that account. If QuickBooks has no account with that name, WalletFeed selects **New Apple Card Account**. With **New Apple Card Account**, WalletFeed makes a credit card account with the name Apple Card in QuickBooks.

3. In **Expense Account**, select the account for your transactions, for example **Uncategorized Expense**.

   If QuickBooks has an expense account with the name Uncategorized Expense, WalletFeed selects that account. After WalletFeed adds a transaction, you can change its category in QuickBooks.

4. Tap **Add**.

   Result: WalletFeed shows **Send Transactions to QuickBooks Online?** The message tells you the data that QuickBooks receives, the Wallet accounts and the start date.

5. Tap **Send**.

   Result: WalletFeed starts to send your transactions to QuickBooks. In **Destinations**, the name of the new destination starts with "QuickBooks ·", for example "QuickBooks · Apple Card".

If you tap **Cancel** in the message, WalletFeed sends no transactions and removes the destination. If WalletFeed made the Apple Card account, the account stays in QuickBooks. If you tap **Add** again, WalletFeed uses that account.

## Step 4: Find the transactions in QuickBooks

1. On a computer, open QuickBooks Online in a web browser.
2. Open the chart of accounts.
3. Find the credit card account that you selected in WalletFeed, for example Apple Card.
4. Open the register of the account.

   Result: QuickBooks shows the expenses and the credits from WalletFeed. The **Ref no.** of each transaction starts with `WF`.

## Data that QuickBooks receives

WalletFeed adds each posted transaction to the credit card account that you selected. A purchase is an expense. A refund or a payment to your card is a credit.

| From Wallet | In QuickBooks |
| --- | --- |
| The merchant name, or the description if there is no merchant name | The start of the memo and of the description of the line |
| The description, the card statement text and the amount in a different currency, if they are different from the merchant name | The rest of the memo and of the description of the line |
| The date of the transaction, in the time zone of your iPhone | The date |
| The amount of the transaction | The amount of the one line of the transaction |
| The expense account that you selected in WalletFeed | The category of the line |
| A code from the ID of the transaction in Wallet, with `WF` at the start | The **Ref no.** |

WalletFeed sends no payee, no category from Wallet and no balance. You can add a payee and change the category of each transaction in QuickBooks. After WalletFeed sends a transaction, WalletFeed changes only its date and its amount. WalletFeed keeps all of your changes.

> **Caution:** Do not change or delete the **Ref no.** of a transaction from WalletFeed. WalletFeed uses it to find the transaction again. If you change it, WalletFeed adds the transaction again when the transaction changes in Wallet.

The credit card account also receives the transactions from your other Wallet accounts, for example Apple Cash. Apple Cash and Savings are not credit cards. Thus, set **Filter** to send only your Apple Card transactions (refer to [Send only some transactions](#send-only-some-transactions)).

## New and changed transactions

While WalletFeed is open, QuickBooks receives changes in seconds. When WalletFeed is not open, iOS starts WalletFeed approximately 1 hour or less after a change in Wallet. If [Background Sync](/docs/background-sync/) is on in **Settings** › **Sync**, WalletFeed then sends the change.

QuickBooks receives a charge only after it posts. A pending charge does not go to QuickBooks. When the charge posts, WalletFeed adds it to QuickBooks. A declined charge does not post, thus QuickBooks does not receive it.

If Wallet removes a posted transaction, WalletFeed deletes it in QuickBooks. A refund is a different transaction, as a credit.

A payment to your Apple Card from a bank account is a credit in the Apple Card account. WalletFeed puts the expense account as its category. In QuickBooks, change the category of the credit to the bank account that paid the card. If your bank account in QuickBooks also has the payment, delete one of the two transactions.

If you delete a transaction from WalletFeed in QuickBooks, WalletFeed can add it again. This occurs if the transaction changes in Wallet, or if you send previous transactions again.

## Send previous transactions

A new destination also receives previous transactions from the start date in **Settings** › **Sync** › **Initial History**. **Initial History** is **All** until you change it. If you change **Initial History** before you add QuickBooks Online, the new destination receives transactions from the new start date.

To send previous transactions after you add QuickBooks Online, do these steps:

1. In **Destinations**, tap the QuickBooks destination.
2. Tap **Send History**.
3. Tap **30 Days**, **90 Days**, **1 Year** or **All**.

   Result: WalletFeed shows **Sending History** and the number of transactions that it sent.

4. To stop WalletFeed before it sends all of the transactions, tap **Send History** › **Stop Sending**.

WalletFeed sends 100 previous transactions to QuickBooks, waits 30 seconds, and then sends more transactions.

**Send History** does not add a transaction two times. WalletFeed finds each transaction by its **Ref no.** If the amount or the date is different, WalletFeed changes the transaction that it finds.

For more information, refer to [Send previous transactions](/docs/send-history/).

## Change or remove the destination

You change the QuickBooks destination on its screen in **Destinations**. For more information about this screen, refer to [Destinations](/docs/destinations/).

### Send only some transactions

1. In **Destinations**, tap the QuickBooks destination.
2. Set **Filter** to on.
3. Change **Include**, **Minimum**, **Accounts**, **Categories** or **Exclude**.

   In **Accounts**, you select the Wallet accounts for QuickBooks. With Apple Intelligence, you can also type a rule in words, for example "Travel over $50, not Uber", and tap the Apple Intelligence icon.

For more information, refer to [Filter the transactions for a destination](/docs/choose-what-to-send/).

### Stop the destination for a time

1. In **Destinations**, tap the QuickBooks destination.
2. Set **Enabled** to off.

   Until you set **Enabled** to on again, WalletFeed does not send transactions to QuickBooks.

### Replace the sign-in

If QuickBooks does not accept your sign-in, do these steps:

1. In **Destinations**, tap the QuickBooks destination.
2. Tap **Sign In Again**.
3. On the Intuit page, get access to your Intuit account.
4. If the Intuit page shows a list of companies, select the company of the destination.
5. Tap **Connect**.

   Result: WalletFeed makes sure that the new sign-in can open the company and the account. Then WalletFeed shows **Signed In** with a green checkmark.

QuickBooks lets an app keep a sign-in for a maximum of five years. Before the end of that period, QuickBooks tells you. Then do these steps.

### Remove QuickBooks Online from WalletFeed

1. In **Destinations**, tap the QuickBooks destination.
2. Tap **Delete**.
3. Tap **Delete** again.

   Result: WalletFeed removes the destination and deletes your QuickBooks sign-in from your iPhone. WalletFeed also removes its connection to the company, if no other QuickBooks destination on your iPhone uses that company.

The transactions that WalletFeed sent stay in QuickBooks.

### Remove WalletFeed from your QuickBooks company

1. On a computer, open QuickBooks Online.
2. Open the list of the apps that you connected to the company.
3. Find WalletFeed in the list, then disconnect it.

After you remove WalletFeed in QuickBooks, the QuickBooks destination in WalletFeed shows "Signed out". To send transactions again, [replace the sign-in](#replace-the-sign-in).

## Upload a file instead

You can also put your transactions in QuickBooks Online with a file that you upload. WalletFeed saves your transactions in one OFX file for each month, and you upload each file in QuickBooks Online. QuickBooks gets the changes only when you upload a file again.

> **Note:** For bank transactions from a file, QuickBooks Desktop uses Web Connect. Intuit tells you that Web Connect reads only QBO files. WalletFeed does not write QBO files.

### Files that QuickBooks Online can upload

Intuit gives these rules in [Manually upload transactions into QuickBooks Online](https://quickbooks.intuit.com/learn-support/en-us/help-article/import-transactions/manually-upload-transactions-quickbooks-online/L0rE9OXBz_US_en_US) (updated August 24, 2026):

- QuickBooks Online can upload a list of transactions from a CSV, TXT, QBO, QFX or OFX file.
- The file must be in English and 350 KB or less.
- One upload has 1,000 transactions at most.
- A CSV file must have 3 columns (Date, Description and Amount) or 4 columns (Date, Description, Credit and Debit).

Use the OFX files from WalletFeed. An OFX file has only posted transactions, and each transaction has an ID that stays the same. WalletFeed Pro is necessary for the OFX files.

### Add an OFX file in WalletFeed

1. On your iPhone, open WalletFeed.
2. Tap **Destinations**.
3. Tap **+** at the top of the screen.
4. In the **Destinations** search field, type `OFX`.
5. Tap **OFX File**.
6. Make sure that **Format** is **OFX**.

   ![The Files screen with OFX in Format, Choose… in Folder and WalletFeed in Name.](https://walletfeed.app/guides/apple-card-to-quickbooks/walletfeed-setup-ofx-file.webp)

7. Tap **Folder**.
8. Select a folder in iCloud Drive.
9. Tap **Add**.
10. When WalletFeed shows **Save Transactions to Files?**, tap **Save**.

    Result: WalletFeed writes one file for each month that has posted transactions. For example, the file for October 2026 is `WalletFeed 2026-10.ofx`.

11. Tap the new destination.
12. Set **Filter** to on.
13. In **Accounts**, select your Apple Card account.

    Result: The files then have only your Apple Card transactions.

### Upload a file in QuickBooks Online

Intuit gives these steps in [Manually upload transactions into QuickBooks Online](https://quickbooks.intuit.com/learn-support/en-us/help-article/import-transactions/manually-upload-transactions-quickbooks-online/L0rE9OXBz_US_en_US). The labels are from August 24, 2026.

1. On your computer, open QuickBooks Online in a web browser.
2. Click **All apps** › **Accounting** › **Bank transactions**.
3. If QuickBooks shows a tile for your Apple Card account, click the tile.
4. Click **Link account**.

   If your account in QuickBooks has no connection to online banking, click **Upload from file** or **Or upload transactions manually**. Then go to step 6.

5. Click **Upload from file**.
6. Click **Drag and drop or select files**.
7. In the folder from WalletFeed, select the file for a month, for example `WalletFeed 2026-10.ofx`.
8. Click **Continue**.
9. In **QuickBooks account**, select the credit card account for your Apple Card.
10. Click **Continue**.
11. Select the transactions to upload.
12. Click **Continue**.
13. Click **Yes**.
14. Click **Done**.

After the upload, Intuit tells you to match and categorize the transactions in **Bank transactions**.

> **Caution:** Do not upload files to the account that the QuickBooks Online destination sends to. If you do, QuickBooks can show each transaction two times.

## If there is a problem

To make sure that WalletFeed can send transactions to QuickBooks, do these steps:

1. In **Destinations**, tap the QuickBooks destination.
2. Tap **Send Test**.

   Result: If QuickBooks receives the test transaction, WalletFeed shows a green checkmark.

> **Note:** **Send Test** adds a test expense of $4.20 to the credit card account. The memo of the test expense starts with WalletFeed. If you tap **Send Test** again, WalletFeed does not add a second test expense. You can delete the test expense in QuickBooks.

### If WalletFeed shows "QuickBooks didn't connect a company"

QuickBooks did not give WalletFeed access to a company. WalletFeed then shows "QuickBooks didn't connect a company. Sign in again and choose one."

1. On the QuickBooks Online form, tap **Connect to QuickBooks** or **Use Another Company**.
2. On the Intuit page, select the company.
3. Tap **Connect**.

### If WalletFeed shows "QuickBooks refused access"

QuickBooks does not let WalletFeed open the company. WalletFeed then shows, for example, "QuickBooks refused access to Craig's Design. Sign in again as a company admin." This occurs if your QuickBooks user is not an admin of the company.

1. In QuickBooks, make sure that your user is an admin of the company.
2. In WalletFeed, [replace the sign-in](#replace-the-sign-in).

### If the destination shows "Authentication failed" or "Signed out"

QuickBooks does not accept the sign-in of the destination. This occurs if WalletFeed did not connect to QuickBooks for 100 days, or if a person removed WalletFeed in QuickBooks. The destination then shows "Signed out. Open the destination and tap Sign In Again." or "Authentication failed. Sign in again."

1. Do the steps in [Replace the sign-in](#replace-the-sign-in).

### If WalletFeed shows "This sign-in can't open"

You selected a different company on the Intuit page.

1. Tap **Sign In Again** again.
2. On the Intuit page, select the company of the destination.

### If WalletFeed shows "QuickBooks sign-in isn't available right now"

The WalletFeed sign-in service cannot connect you to QuickBooks at this time. WalletFeed then shows "QuickBooks sign-in isn't available right now. Try again later."

1. Wait some minutes.
2. Tap **Connect to QuickBooks** again.

### If the destination shows that the subscription has ended

The trial or the subscription of the company ended. QuickBooks then lets apps only read the company. WalletFeed shows, for example, "The QuickBooks subscription for Craig's Design has ended. Renew it in QuickBooks."

1. In QuickBooks, renew the subscription of the company.

   Result: WalletFeed then sends the transactions that it did not send.

### If the destination shows "QuickBooks is limiting requests"

QuickBooks lets WalletFeed send a maximum number of requests each minute to a company. WalletFeed then shows "QuickBooks is limiting requests. Sending resumes in a minute."

1. Wait 1 minute.

   Result: WalletFeed can send the transactions again.

### If the destination shows "The closing date in QuickBooks refuses these transactions"

The company has a closing date in QuickBooks, and the transactions are before that date. WalletFeed then shows "The closing date in QuickBooks refuses these transactions. Change it, or stop Send History."

1. If you send previous transactions, tap **Send History** › **Stop Sending**.
2. To add the transactions to QuickBooks, change the closing date in QuickBooks.

### If the destination shows "QuickBooks refused" and a number of transactions

QuickBooks did not accept some transactions, for example because a person made the expense account inactive. QuickBooks added the other transactions. WalletFeed then shows, for example, "QuickBooks refused 2 transactions. Check the destination's accounts in QuickBooks."

1. In QuickBooks, make sure that the credit card account and the expense account of the destination are active.
2. If a person made the expense account inactive, remove the QuickBooks destination in WalletFeed.
3. Add QuickBooks Online again in WalletFeed, and select an active expense account.

### If the destination shows "A transaction changed in QuickBooks during the sync"

A person changed a transaction in QuickBooks while WalletFeed changed it. WalletFeed then shows "A transaction changed in QuickBooks during the sync. Sending resumes at the next sync."

1. Wait until WalletFeed sends transactions again.

   Result: WalletFeed reads the transaction again and sends the change.

### If the destination shows "QuickBooks replaced the Ref no."

QuickBooks put its own number in the **Ref no.** of a new transaction. Without its **Ref no.**, WalletFeed cannot find the transaction again. Thus, WalletFeed deleted the transaction, and it sends no transactions. WalletFeed then shows "QuickBooks replaced the Ref no. that WalletFeed sets. Check the custom transaction numbers setting."

1. In QuickBooks, open the settings of your company.
2. If custom transaction numbers are off, set them to on.
3. In WalletFeed, tap the destination.
4. Tap **Send Test**.

### If the destination shows that the account is in a different currency

The credit card account in QuickBooks has a different currency than your transactions. WalletFeed then shows, for example, "Apple Card in QuickBooks is in CAD, not USD. Add this destination again with a USD account."

1. Remove the QuickBooks destination in WalletFeed.
2. Add QuickBooks Online again, and select a credit card account in USD. You can also select **New Apple Card Account**.

### If WalletFeed shows "QuickBooks has an inactive account named Apple Card"

QuickBooks has an Apple Card account that a person made inactive. WalletFeed cannot make a second account with that name.

1. In QuickBooks, make the Apple Card account active.
2. In WalletFeed, tap **Try Again**.
3. Select the Apple Card account in **Account**.

### If WalletFeed shows "QuickBooks didn't create the account"

QuickBooks did not make the Apple Card account when you tapped **Add**. For example, Simple Start, Essentials and Plus let a company have a maximum of 250 accounts in the chart of accounts. WalletFeed then shows "QuickBooks didn't create the account. Choose an existing account."

1. In **Account**, select a credit card account that you have in QuickBooks.
2. Tap **Add**.

### If QuickBooks shows a transaction two times

You uploaded a file to the account that the QuickBooks Online destination sends to, or you changed a **Ref no.**

1. In QuickBooks, find the transaction with a **Ref no.** that does not start with `WF`.
2. Delete that transaction in QuickBooks.

### If QuickBooks receives transactions only while WalletFeed is open

When **Background Sync** is off, WalletFeed sends transactions only while it is open.

1. Tap the gear icon at the top of **Destinations**.
2. In **Settings** › **Sync**, set **Background Sync** to on.

For more information, refer to [Background Sync](/docs/background-sync/).

### If Destinations shows "Sync Requires Pro"

Your WalletFeed Pro subscription stopped. WalletFeed Pro is necessary for all destinations.

1. Tap **Upgrade**.

   Result: WalletFeed shows the **WalletFeed Pro** screen.

2. If your Apple Account has a WalletFeed Pro purchase, tap **Restore Purchases**.
3. If your Apple Account has no WalletFeed Pro purchase, select a plan.
4. Complete the purchase.
