# Apple Card budget template for Google Sheets

The WalletFeed budget template for Google Sheets shows your Apple Card spending for each category and each month, and your budget for each category. You copy two tabs from the template into the spreadsheet that WalletFeed makes.

## Before you start

You must have these items:

- An iPhone with iOS 26 or a newer version. WalletFeed is available only in the US.
- WalletFeed, with a Google Sheets destination (refer to [Send Apple Card transactions to Google Sheets](/guides/apple-card-to-google-sheets/)).
- [WalletFeed Pro](/docs/walletfeed-pro/), because WalletFeed Pro is necessary for destinations. WalletFeed Pro is a subscription with a 1-week free trial, or a one-time Lifetime purchase.
- A computer with a web browser, and access to the Google Account that has your WalletFeed spreadsheet.

Without WalletFeed Pro, you can use the template with a CSV file (refer to [Use the template with a CSV file](#use-the-template-with-a-csv-file)).

## Step 1: Make a copy of the template

1. On your computer, open the [WalletFeed budget template](https://docs.google.com/spreadsheets/d/PUBLIC-TEMPLATE-ID/copy).
2. Click **Make a copy**.

   Result: Google Sheets opens the copy in your Google Drive. The name of the copy is **Copy of WalletFeed Budget Template**.

## Step 2: Copy the tabs to your WalletFeed spreadsheet

The tabs read the tab with the name **Transactions**. If you changed the name of the **Transactions** tab in your WalletFeed spreadsheet, give the tab the name **Transactions** again before you copy the tabs.

1. In the copy of the template, right-click the **Spending** tab at the bottom of the screen.
2. Click **Copy to**.
3. Click **Existing spreadsheet**.
4. Select your WalletFeed spreadsheet, for example **WalletFeed Transactions**.
5. Click **Select**.

   Result: Google Sheets adds the tab to your WalletFeed spreadsheet. The name of the tab is **Copy of Spending**.

6. Do steps 1 to 5 again for the **Budget** tab.

Do not copy the **Transactions** tab of the template. WalletFeed writes only to the **Transactions** tab that it made.

After you copy the tabs, you can change the names of all the tabs. Google Sheets then changes the formulas to use the new names.

## Step 3: Type your budget

1. On your computer, open your WalletFeed spreadsheet in Google Drive.
2. Click the **Copy of Budget** tab.
3. In column B, type a budget for each category, for example `400` for **Groceries**.

   Result: **Spent**, **Left** and **Used** show the data for the month in cell B1. Cell B1 shows this month.

4. For a different month, type a date in that month in cell B1, for example `2026-10-01`.

When WalletFeed sends new or changed transactions, the **Spending** and **Budget** tabs change too.

## Tabs in the template

| Tab | Contents |
| --- | --- |
| **Spending** | The money out in each category, for each month |
| **Budget** | Your budget and the money out in each category, for one month |
| **Transactions** | The header row that WalletFeed writes, and two sample rows |

On the **Spending** tab, the newest month is in column B. The tab shows the 24 newest months. The **Total** row has the total for each month.

On the **Budget** tab, cell B1 has the month. The **Spent** column shows the money out in that month. The **Left** column shows **Budget** minus **Spent**, in red when it is less than zero. The **Used** column shows **Spent** as a percentage of **Budget**.

You use the **Transactions** tab of the template only with a CSV file.

The two tabs find the money out in the same way. They add each **Amount** of less than zero. Then they subtract the **Amount** of each row with the **Type** `refund`. Other money into an account, for example a payment to your Apple Card, does not change the totals.

A transfer out of Apple Cash or Savings is also money out. It is in the row of its category, for example **Cash & Transfers** or **Other**.

The formulas find each column by its header in row 1 of the **Transactions** tab. Thus, the totals stay correct when WalletFeed adds a column at the end of the tab. You can also add columns after column N.

## Use the template with a CSV file

Without WalletFeed Pro, you can use [Export CSV](/docs/export-csv/) to make a CSV file. Then you put the file in the **Transactions** tab of your copy of the template. The CSV file has the same column headers as the spreadsheet that WalletFeed makes, in a different sequence. Thus, the tabs show the same totals.

1. On your iPhone, make a CSV file with **Export CSV** (refer to [Make a CSV file with Export CSV](/docs/export-csv/)).
2. Save the file in iCloud Drive.
3. On your computer, open your copy of the template.
4. Click the **Transactions** tab.
5. Click **File** › **Import**.
6. Click **Upload**.
7. Select the CSV file.
8. In **Import location**, select **Replace current sheet**.
9. Click **Import data**.

   Result: The **Transactions** tab shows the transactions from the CSV file. The **Spending** and **Budget** tabs show the totals.

The CSV file does not change after WalletFeed makes it. For new transactions, make a new file and do the steps again.

## If there is a problem

### If a tab shows #REF!

When you copied the tab, your WalletFeed spreadsheet had no tab with the name **Transactions**.

1. In your WalletFeed spreadsheet, right-click the **Copy of Spending** tab.
2. Click **Delete**.
3. Do steps 1 and 2 again for the **Copy of Budget** tab.
4. Give the tab with your transactions the name **Transactions** again.
5. Do the steps in [Step 2](#step-2-copy-the-tabs-to-your-walletfeed-spreadsheet) again.
