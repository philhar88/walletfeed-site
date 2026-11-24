+++
title = "Subscriptions and their cost"
nav_title = "Subscriptions"
seo_title = "Subscriptions: Apple Card charges that repeat"
description = "Subscriptions in WalletFeed shows the charges that repeat on your Apple Card, the date of the next charge and the cost for each month and each year."
order = 75
related = ["docs/recurring-charges", "docs/spending", "guides/find-apple-card-subscriptions"]
updated = 2026-11-24
+++

In WalletFeed, **Subscriptions** shows the subscriptions and the other charges that occur again on your Apple Card. It shows the cost of all these charges together for one month and for one year. [WalletFeed Pro](/docs/walletfeed-pro/) is not necessary for **Subscriptions**.

## Open Subscriptions

1. On your iPhone, open WalletFeed.
2. Tap **Spending**.
3. Tap **Subscriptions**.

   The row is above the **Categories** section. If Spending shows the **Accounts** section, the row is below that section.

WalletFeed reads your transactions from Wallet each time that you open the screen. To read them again, swipe down on the screen.

## Totals and categories

**Each Month** and **Each Year** show the cost of all the charges together. Below them, WalletFeed shows "Charges that repeat, from the last 14 months in Wallet."

For **Each Year**, WalletFeed calculates the cost of each charge for one year:

- A **Weekly** charge is 52 times the price of the last charge.
- A **Monthly** charge is 12 times the price of the last charge.
- A **Yearly** charge is the price of the last charge.

**Each Month** is **Each Year** divided by 12.

The **Categories** section shows the cost of each category for one month. At the top of the section, a bar shows each category in a different color. The length of each color shows the part of the cost for that category.

## Charges in the list

The **Charges** section has one row for each charge. The first charge in the list has the largest cost for one year. Each row shows these items:

- An icon for the category of the charge
- The name of the charge
- The word **Weekly**, **Monthly** or **Yearly**
- The date of the next charge, for example "Next Dec 14"
- The price before the last charge, if the price changed, for example "Was $15.49"
- The price of the last charge
- For a **Weekly** or **Monthly** charge, the cost for one year, for example "$185.88 a year".

The list shows each charge that occurs again, not only subscriptions. For example, the list can show a gym, a phone bill or rent on your card.

If WalletFeed finds no charges, the screen shows "No Subscriptions".

## Rules for a charge in the list

WalletFeed reads your transactions from this month and from the 14 months before it. WalletFeed puts the purchases from one merchant in the list in these conditions:

- All the purchases have the same merchant name. For example, “Netflix.com” and “NETFLIX.COM” are the same merchant.
- Each price is not more than 15% above the smallest price.
- For **Weekly**, there are three or more charges. Each of the last two charges is 6 to 8 days after the charge before it.
- For **Monthly**, there are two or more charges. The last charge is 26 to 35 days after the charge before it.
- For **Yearly**, there are two charges. The last charge is 350 to 380 days after the charge before it.
- The next charge is not late.

If one merchant has two subscriptions with different prices, the list shows two charges.

WalletFeed calculates the date of the next charge from the date of the last charge. The next charge is 7 days, one month or one year after the last charge. If the next charge is late, WalletFeed removes the charge from the list. A charge is late after this time:

| Charge | Time after the date of the next charge |
| --- | --- |
| **Weekly** | 4 days |
| **Monthly** | 10 days |
| **Yearly** | 30 days |

These transactions are not in the list:

- Refunds, transfers, bill payments and declined transactions
- Apple Card Monthly Installments (**Spending** shows them in the **Monthly Installments** section)
- Purchases in a different currency.

## Names from Apple Intelligence

For names from Apple Intelligence, you must have an iPhone that can use Apple Intelligence. Apple Intelligence must be active on that iPhone.

With Apple Intelligence, WalletFeed shows a short name, such as Netflix, for a merchant name such as “NETFLIX.COM 866-579”. The row can also show the type of service, for example "Streaming · Monthly · Next Dec 14". When the list has names from Apple Intelligence, WalletFeed shows **Apple Intelligence suggested these names.** below the list.

WalletFeed gets names for only the first 12 charges in the list. If a charge has no name from Apple Intelligence, the row shows the merchant name from Wallet. The rules for the names are the same as in [Recurring Charges](/docs/recurring-charges/#names-from-apple-intelligence).

## Subscriptions and Recurring Charges

The [Recurring Charges](/docs/recurring-charges/) section on Spending and Recurring Charge Alerts read your transactions from this month and from the two months before it. They find only **Monthly** and **Weekly** charges.

The **Subscriptions** screen reads more months. Thus, it also finds **Yearly** charges, and it can show a charge that **Recurring Charges** does not show.

## Privacy

WalletFeed finds the charges on your iPhone each time that you open **Subscriptions**. It does not keep the list, and it does not keep a copy of your transactions.

To give names to the charges, Apple Intelligence gets only the merchant names. Apple Intelligence makes the names on your iPhone. WalletFeed sends nothing to a server.

For more information, refer to the [WalletFeed privacy policy](/privacy/).

## If there is a problem

### If the screen shows "Couldn't Read Wallet"

WalletFeed cannot read your transactions from Wallet.

To make WalletFeed read Wallet again, swipe down on the screen.

### If a subscription is not in the list

WalletFeed shows a **Monthly** charge only after the second charge from the merchant. It shows a **Weekly** charge only after the third charge. For a **Yearly** charge, Wallet must have the charge of this year and the charge of last year.

1. When Wallet shows the next charge from the merchant, open WalletFeed.
2. Tap **Spending**.
3. Tap **Subscriptions**.
4. If the list does not show the charge, refer to [Rules for a charge in the list](#rules-for-a-charge-in-the-list).

If the start date of a Wallet account is after the first charge, WalletFeed cannot read that charge. To change the start date, refer to [Wallet accounts](/docs/wallet-accounts/#change-the-accounts-that-walletfeed-reads).

### If a subscription with a new price is not in the list

After a price change of more than 15%, WalletFeed does not put the new price with the charges before it. The list shows the new price after two charges with that price. For a **Weekly** charge, three charges with the new price are necessary.

### If the list shows a subscription that you stopped

The charge stays in the list until its next charge is late. Refer to [Rules for a charge in the list](#rules-for-a-charge-in-the-list).
