# Get the totals of a year with Tax Pack

In WalletFeed, **Tax Pack** gives the totals of your Apple Card, Apple Cash and Savings transactions for one year. You can send the totals as files to a tax preparer or an AI assistant. [WalletFeed Pro](/docs/walletfeed-pro/) is not necessary for the totals on the screen. Some plans include the files (refer to [Plans that include the files](#plans-that-include-the-files)).

> **Note:** The totals are sums of the records in Wallet. They are not a tax form. WalletFeed does not give tax advice.

## Find the totals of a year

1. On your iPhone, open WalletFeed.
2. Tap **Settings** (the gear button) at the top of the screen.

   ![The Transactions screen with the gear button at the top.](https://walletfeed.app/docs/tax-pack/walletfeed-transactions.webp)

3. In the **Data** section, tap **Tax Pack**.
4. Tap **Year**.
5. Select a year.

   **Transactions** shows the number of posted transactions in the year. Below it, the screen shows the totals of each Wallet account.

You can also open **Tax Pack** from the **Spending** tab. Tap **Tax Pack** at the end of the [**Accounts**](/docs/spending/#accounts) section.

You can select this year or one of the two years before it. Until April 30, **Tax Pack** opens with last year. After April 30, it opens with this year.

Before the end of a year, the screen shows "The year isn't over. These are the totals so far."

## Totals on the screen

For Apple Card, the screen shows these totals:

| Total | Transactions in the total |
| --- | --- |
| **Purchases** | The purchases on the card. |
| **Refunds** | The refunds from merchants. |
| **Interest charged** | The interest on the card. A refund of interest decreases this total. |
| **Fees** | The fees on the card. A refund of a fee decreases this total. |
| **Payments to the card** | Your payments to the card. A payment that comes back decreases this total. |
| **Other credits** | The credits that are not refunds or payments. The screen shows this total only when it is not zero. |
| **Transfers out** | The transfers from the card. The screen shows this total only when it is not zero. |

For Apple Cash and for Savings, the screen shows these totals:

| Total | Transactions in the total |
| --- | --- |
| **Interest earned** | The interest that the account received. |
| **Money in, without interest** | The other money that came into the account. |
| **Money out** | The money that went out of the account. |
| **Fees** | The fees on the account. The screen shows this total only when it is not zero. |

Each posted transaction is in one total only.

## Save or send the files

1. In **Tax Pack**, select the year in **Year**.
2. Tap **Share Pack**.

   The iOS menu opens with the four files of the pack.

3. Tap **Save to Files**, or select AirDrop, Mail or a different app.

For an AI assistant, tap **Share Summary for AI** at step 2. The iOS menu then opens with only the Markdown file.

The files go only to the app or person that you select. WalletFeed makes the files on your iPhone and does not keep a copy.

## Files in the pack

The name of each file has the year in it. For 2026, the pack has these files:

| File | Contents |
| --- | --- |
| `Tax Pack 2026.pdf` | A summary of one or two pages for a tax preparer. |
| `Tax Pack 2026.md` | The same totals as Markdown text for an AI assistant. Each merchant has one row, with a count and a total. |
| `Tax Pack 2026 Totals.csv` | One row for each total, for a spreadsheet. The columns are Section, Account, Line, Category, Period, Count and Amount. |
| `Tax Pack 2026 Transactions.csv` | One row for each posted transaction of the year. The columns are the same as in [Export CSV](/docs/export-csv/#columns-in-the-file). |

The files have the totals from the screen. They also have this data:

- The balance of Apple Cash and of Savings at the start and at the end of the year, where Wallet has a record. The files give the date of each record. They do not include the balance of Apple Card.
- The purchases minus the refunds, for each category and for each month.
- Each merchant, with the number of its transactions and its total.
- The merchant types that a tax preparer frequently looks for.

WalletFeed finds a merchant type from the merchant category code (MCC) of the merchant. The files have these merchant types:

- Health care and pharmacies
- Charities and religious organizations
- Schools and education
- Child care
- Government, courts and tax payments.

The PDF file gives one total for each merchant type. The list of merchants is in the Markdown file and in the totals file. The Markdown file lists the 250 merchants with the largest totals, and gives one total for the others.

## Plans that include the files

The totals on the screen are free. **Share Pack** and **Share Summary for AI** are in these plans of [WalletFeed Pro](/docs/walletfeed-pro/):

- **Yearly**, but not during its free trial
- **Lifetime**.

With **Monthly**, or during the free trial of **Yearly**, the screen shows **Change Plan**. Without a plan, the screen shows **Upgrade**. Each button opens the **WalletFeed Pro** screen.

[Export CSV](/docs/export-csv/) is free. Its **Last Year** period gives a CSV file of all the transactions of last year.

The text below the button is "Sharing is included with Pro Yearly and Lifetime." Pro Yearly is the **Yearly** plan. During the free trial of **Yearly**, the text gives the date when the trial ends. An example is "Included when your free trial ends on Dec 1, 2026, or now with Lifetime."

## Activate Tax Pack Ready

Tax Pack Ready sends you one notification each January, after the pack of the year before is completed. You can use Tax Pack Ready without WalletFeed Pro. Tax Pack Ready is off until you set it to on.

1. On your iPhone, open WalletFeed.
2. Tap **Settings** (the gear button) at the top of the screen.
3. In the **Notifications** section, set the **Tax Pack Ready** switch to on.
4. If iOS shows a message about notifications, tap **Allow**.

   If you do not let WalletFeed send notifications, the switch stays off.
5. Tap **Done**.

If you set notifications for WalletFeed to off in the iOS Settings app, the switch stays on, but you do not get notifications. For the steps to set them to on again, refer to [If WalletFeed shows "Notifications are off for WalletFeed."](/docs/troubleshooting/#if-walletfeed-shows-notifications-are-off-for-walletfeed).

## The Tax Pack Ready notification

The notification comes at 9:00 on January 3, in the time zone of your iPhone. Thus, most pending charges of December post before the notification comes.

The title of the notification is "Tax Pack Ready". The text gives the year that ended, for example "Your 2026 Tax Pack is in Settings." The notification shows no amount.

If you set the switch to on after 9:00 on January 3, the first notification comes on January 3 of the next year.

For Tax Pack Ready, WalletFeed keeps only the switch. iOS keeps the notification until it comes.

## Stop Tax Pack Ready

1. On your iPhone, open WalletFeed.
2. Tap **Settings** (the gear button) at the top of the screen.
3. In the **Notifications** section, set the **Tax Pack Ready** switch to off.
4. Tap **Done**.

## Limits of the totals

The totals and the files have these limits:

- Only posted transactions are in the totals. The PDF file and the Markdown file give the number of pending transactions that are not in the totals.
- Only transactions in your primary currency (for example, USD) are in the totals. These two files also give the number of transactions in a different currency.
- The date of a transaction, not its posted date, gives the year of the transaction.
- **Interest earned** is the sum of the interest transactions in Wallet. The Form 1099-INT from the bank is the tax record.
- If more than one person uses your Apple Card, the transactions do not show the person who made them.
- Wallet does not identify Daily Cash. Thus, Daily Cash has no total of its own.
- Wallet gives transactions to WalletFeed from the start date that you selected. Thus, the first months of a year can be missing.
- A pack from before the end of the year has the totals up to that day.

The files do not change after WalletFeed makes them. For new transactions, tap **Share Pack** again.

## If there is a problem

### If you cannot tap **Share Pack**

You cannot tap **Share Pack** while WalletFeed reads your transactions, or when the year has no posted transactions.

1. Wait until **Transactions** shows a number.
2. If the number is 0, select a different year in **Year**.

### If the screen shows **Upgrade** or **Change Plan**

Your plan does not include the files.

1. Tap **Upgrade** or **Change Plan**.

   The **WalletFeed Pro** screen opens.

2. Tap **Yearly** or **Lifetime**.
3. Tap the button at the bottom of the screen.
4. Complete the purchase on the App Store screen.

If **Yearly** starts with a free trial, **Tax Pack** shows **Change Plan** until the trial ends. **Lifetime** includes the files from the time of the purchase. For the plans and the prices, refer to [WalletFeed Pro](/docs/walletfeed-pro/#plans-and-prices).

### If the year shows 0 transactions

The year has no posted transactions, or WalletFeed cannot read the transactions of your Wallet accounts.

1. Select a different year in **Year**.
2. If each year shows 0, do the steps in [If each period has 0 transactions](/docs/export-csv/#if-each-period-has-0-transactions).

### If the first months of a year are missing

Wallet gives transactions to WalletFeed from the start date of each account. The transactions before that date are not in the totals.

1. On your iPhone, open the Settings app.
2. Tap **Privacy & Security** › **Wallet** › **WalletFeed**.
3. For each account, select a start date before January 1 of the year.
4. Open WalletFeed.
5. Open **Tax Pack** again.

[Wallet accounts](/docs/wallet-accounts/#change-the-accounts-that-walletfeed-reads) gives all the steps.

### If the totals are different from the tax form of the bank

The totals are sums of the posted transactions that Wallet gives to WalletFeed. The form from the bank, for example Form 1099-INT, is the tax record.

Pending transactions are not in the totals. If the start date of an account is after January 1 of the year, the transactions before that date are also not in the totals.

### If the files have sample transactions

When **Sample Data** is on, WalletFeed shows two months of sample transactions. The totals and the files then have only sample transactions.

1. In WalletFeed, tap **Settings**.
2. In the **Data** section, set **Sample Data** to off.
3. Tap **Tax Pack**.
4. Select the year in **Year**.
5. Tap **Share Pack**.
