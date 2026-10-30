# Send Apple Card transactions to Google Sheets

WalletFeed sends your Apple Card, Apple Cash and Savings transactions from your iPhone to Google Sheets. After you sign in to Google in WalletFeed, WalletFeed makes a spreadsheet in your Google Drive and updates it automatically.

## Before you start

You must have:

- An iPhone with iOS 26 or a newer version. WalletFeed is available only in the US.
- WalletFeed, with access to your Apple Card, Apple Cash or Savings account
- [WalletFeed Pro](/docs/walletfeed-pro/), a subscription with a 1-week free trial, or a one-time Lifetime purchase. WalletFeed Pro is necessary for all destinations.
- A Google Account.

## Step 1: Add Google Sheets in WalletFeed

1. On your iPhone, open WalletFeed.
2. Tap **Destinations**.
3. Tap **+** at the top of the screen.

   ![The empty Destinations screen with the + button at the top.](https://walletfeed.app/guides/apple-card-to-google-sheets/walletfeed-destinations-empty-pro.webp)

4. In **Sheets & Databases**, tap **Google Sheets**.

   ![The Add Destination list with Google Sheets below Sheets & Databases.](https://walletfeed.app/guides/apple-card-to-google-sheets/walletfeed-add-destination.webp)

   If you do not have WalletFeed Pro, the **WalletFeed Pro** screen opens first. Do these steps on that screen:

   1. Select a plan.
   2. Complete the purchase.

   Then the Google Sheets screen opens.

## Step 2: Sign in to Google

1. Tap **Sign In with Google**.

   ![The Google Sheets screen with the Sign In with Google button and the Spreadsheet field.](https://walletfeed.app/guides/apple-card-to-google-sheets/walletfeed-setup-google-sheets.webp)

2. On the Google page, sign in to the Google Account that you want to use.
3. Give WalletFeed access to the files that it makes.

   Then WalletFeed shows **Signed In**.

> **Note:** WalletFeed keeps the sign-in in the Keychain on your iPhone. With this sign-in, WalletFeed can open only the spreadsheets that it makes. Google shows this access with the description "See, edit, create, and delete only the specific Google Drive files you use with this app."

## Step 3: Make the spreadsheet

1. If you want a different name for the spreadsheet, type the name in **Spreadsheet**.

   The name is **WalletFeed Transactions** until you change it.

2. Tap **Add**.

   WalletFeed makes the spreadsheet in your Google Drive. Then WalletFeed shows the message **Send Transactions to Google Sheets?**

   The message tells you the data that Google Sheets receives, the Wallet accounts and the start date.

3. Tap **Send**.

   WalletFeed starts to send your transactions to the spreadsheet.

If you tap **Cancel** in the message, WalletFeed sends nothing and removes the destination. The spreadsheet stays in your Google Drive. It has only the header row.

## Step 4: Open the spreadsheet

1. In **Destinations**, tap the name of your spreadsheet, for example **WalletFeed Transactions**.
2. Tap **Open in Google Sheets**.

   The spreadsheet has one tab, **Transactions**. Row 1 has the headers. Each row below row 1 has one transaction.

On a computer, you can also find the spreadsheet in your Google Drive.

## Columns in the spreadsheet

This table shows the columns that WalletFeed writes, from A to N:

| Column | Header | Contents |
|---|---|---|
| A | **WalletFeed ID** | The ID of the transaction in WalletFeed |
| B | **Date** | The date of the transaction, in your time zone |
| C | **Merchant** | The merchant name. If Wallet has no merchant name, this column has the same data as **Description**. |
| D | **Amount** | Money out of the account is a negative number. Money into the account, for example a refund or a payment, is a positive number. |
| E | **Currency** | The currency code, for example USD |
| F | **Category** | The WalletFeed category, for example Groceries or Dining |
| G | **Status** | The status from Wallet, for example `booked` or `pending` |
| H | **Pending** | A checkbox that shows a check mark while the transaction is pending |
| I | **Account** | The name of the Wallet account, for example Apple Card |
| J | **Description** | The description of the transaction from Wallet |
| K | **Type** | The type of transaction from Wallet, for example `pointOfSale` |
| L | **MCC** | The merchant category code, as a number |
| M | **Foreign Amount** | For a transaction in a different currency, the amount in that currency. It is empty for other transactions. |
| N | **Foreign Currency** | For a transaction in a different currency, the code of that currency. It is empty for other transactions. |

WalletFeed writes numbers in **Amount** and **Foreign Amount**, and dates in **Date**. You can use them in formulas.

Do not change column A. WalletFeed uses the **WalletFeed ID** to find each row again.

WalletFeed writes each row from column A to column N. If you add columns, put them after column N.

You can change the name of the spreadsheet and the name of the **Transactions** tab. WalletFeed does not change the colors or fonts that you set.

Your transactions go from your iPhone directly to Google. WalletFeed has no account and no WalletFeed servers. After Google Sheets receives your transactions, Google's terms are applicable to them.

## New and changed transactions

While WalletFeed is open, the spreadsheet receives changes in seconds. When WalletFeed is closed, iOS starts WalletFeed in approximately 1 hour or less after a change in Wallet.

For changes while WalletFeed is closed, [Background Sync](/docs/background-sync/) in **Settings** › **Sync** must be on. It is on until you set it to off.

WalletFeed adds each new transaction as a new row at the end of the tab. If a purchase is pending, its row has a check mark in **Pending**. When the purchase posts, WalletFeed updates the same row.

WalletFeed removes the rows of declined transactions and of transactions that Wallet removes. A refund is a new row with a positive number in **Amount**.

## Send previous transactions

A new destination also receives previous transactions, from the start date in **Settings** › **Sync** › **Initial History**. **Initial History** is **All** until you change it.

To send transactions from before that start date, or to send them again, use [Send History](/docs/send-history/):

1. In **Destinations**, tap your spreadsheet.
2. Tap **Send History**.
3. Tap **30 Days**, **90 Days**, **1 Year** or **All**.

   While WalletFeed sends the transactions, the screen shows **Sending History**.

If a transaction is in the spreadsheet, WalletFeed updates its row and does not add a second row. To stop before WalletFeed sends all the transactions, tap **Send History** › **Stop Sending**.

## Change or remove the destination

### Send only some transactions

1. In **Destinations**, tap your spreadsheet.
2. Set **Filter** to on.
3. Set the rules that you want, for example **Accounts**, **Categories** or **Minimum**.

   If Apple Intelligence is on, you can also type a rule, for example "Travel over $50, not Uber", and tap **Create Rule**.

### Stop and start the destination

1. In **Destinations**, tap your spreadsheet.
2. Set **Enabled** to off.

To start again, set **Enabled** to on.

### Remove the destination

1. In **Destinations**, tap your spreadsheet.
2. Tap **Delete**.
3. In the message, tap **Delete**.

   WalletFeed sends no more transactions to the spreadsheet. WalletFeed also removes the Google sign-in for the spreadsheet from your iPhone.

The spreadsheet and the transactions in it stay in your Google Drive. When you remove the destination, WalletFeed does not delete the data that it sent.

### Remove WalletFeed's access to your Google Account

To also remove the access that you gave WalletFeed in your Google Account, do these steps:

1. On a computer, open the [linked apps page](https://myaccount.google.com/linkedapps) of your Google Account.
2. Click **Access to your Google Account**.
3. Click WalletFeed.
4. Click **See details**.
5. Click **Remove access**.
6. Click **Confirm**.

## If there is a problem

### If WalletFeed shows "Signed out" or "Authentication failed"

Google does not accept the sign-in that you gave WalletFeed. This occurs if you remove WalletFeed's access on the linked apps page, or if WalletFeed does not use the sign-in for 6 months.

1. In **Destinations**, tap your spreadsheet.
2. Tap **Sign In Again**.
3. Sign in to the Google Account that you used to make the spreadsheet.
4. Give WalletFeed access to the files that it makes.

If you use a different Google Account, WalletFeed shows "This Google account can't open the spreadsheet. Use the one you set it up with."

### If WalletFeed shows "Google rejected the sign-in"

Google did not accept the sign-in when WalletFeed tried to make the spreadsheet.

1. On the **Google Sheets** screen, tap **Use Another Account**.
2. Sign in to your Google Account again.
3. Give WalletFeed access to the files that it makes.
4. Tap **Add**.

### If the spreadsheet does not receive new transactions

When WalletFeed is closed, iOS starts WalletFeed in approximately 1 hour or less after a change in Wallet. This occurs only if **Background Sync** is on.

1. Open WalletFeed.

   While WalletFeed is open, it sends changes in seconds.

2. Tap **Settings** (the gear button) at the top of the screen.
3. Make sure that **Background Sync** is on.
4. Tap **Sync Now**.

### If Destinations shows "Sync Requires Pro"

Your WalletFeed Pro subscription stopped. WalletFeed Pro is necessary for destinations.

1. Tap **Upgrade**.
2. Select a plan.
3. Complete the purchase.

If you have a previous WalletFeed Pro purchase with the same Apple Account, tap **Restore Purchases** on the **WalletFeed Pro** screen.
