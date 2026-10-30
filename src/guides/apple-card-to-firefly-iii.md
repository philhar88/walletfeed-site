+++
title = "Send Apple Card transactions to Firefly III"
nav_title = "Firefly III"
seo_title = "Apple Card to Firefly III: send iPhone transactions"
description = "Send Apple Card transactions from your iPhone to Firefly III. Make a personal access token in Firefly III. Then paste the token in WalletFeed."
group = "Budgeting apps"
order = 30
related = ["guides/apple-card-to-sure", "docs/destinations"]
updated = 2026-10-30
+++

WalletFeed sends your Apple Card, Apple Cash and Savings transactions from your iPhone to one account on your Firefly III server. You make a personal access token in Firefly III. Then you paste the token in WalletFeed and type the address of your server.

## Before you start

You must have these items:

- An iPhone with iOS 26 or a newer version. WalletFeed is available only in the US.
- Apple Card, Apple Cash or Savings in Wallet on that iPhone, and WalletFeed with [access to your Wallet accounts](/docs/wallet-accounts/).
- [WalletFeed Pro](/docs/walletfeed-pro/), which is necessary for destinations. WalletFeed Pro is a subscription with a 1-week free trial, or a one-time Lifetime purchase.
- Your Firefly III server, and a user account on it.
- An `https://` address for the server, with a certificate that iOS accepts. Your iPhone must connect to this address from all locations, and not only from your home Wi-Fi.

WalletFeed cannot use an `http://` address. The Firefly III image for Docker uses `http://` on port 8080. To get an `https://` address with a certificate that iOS accepts, you can use one of these:

- Tailscale HTTPS, with a `.ts.net` address
- A reverse proxy with a certificate from Let's Encrypt
- Cloudflare Tunnel.

You can also make a root certificate and install it on your iPhone. If you use a root certificate, you must set the switch for that certificate to on in **Settings** › **General** › **About** › **Certificate Trust Settings**.

WalletFeed sends the time of each transaction as the time on your iPhone. This time has no time zone. Firefly III reads the time in the time zone of the server. If the server time is before the time on your iPhone, a new transaction can have a time after the server time. As a result, Firefly III does not include the transaction in **Current balance** for some hours.

To prevent this problem, you can set `TZ` in the configuration of the server to your time zone. If `TZ` has no value, Firefly III uses UTC.

## Step 1: Make a personal access token in Firefly III

You can do these steps on a computer, or in Safari on your iPhone. With Universal Clipboard, you can copy the token on a Mac and paste it on your iPhone.

> **Caution:** Do not send the token to yourself in a message or an e-mail. The token gives access to all of your Firefly III data.

1. On your computer, get access to your Firefly III account in a web browser.
2. Click the person icon at the top right of the page (the icon has no text).

   ![The Firefly III home page with the highlighted person icon at the top right.](web:firefly-iii/03-user-icon)

3. Click **Remote access and tokens**.

   ![The Firefly III account menu, with the highlighted Remote access and tokens item.](web:firefly-iii/04-user-menu)

4. In the **Personal Access Tokens** section, click **Create new token**.

   ![The Remote access and tokens page, with the highlighted Create new token button in the Personal Access Tokens section.](web:firefly-iii/05-remote-access-page)

   Do not click **Create New Client** in the **OAuth Clients and Applications** section. WalletFeed does not use OAuth clients.

5. In the **Name** field, type `WalletFeed`.
6. Click **Create**.

   ![The Create token dialog, with WalletFeed in the Name field and the highlighted Create button.](web:firefly-iii/06-create-token)

7. Click in the large text box that shows the token.
8. To select all the text in the box, press Command-A on a Mac, or Ctrl-A on a Windows computer.
9. To copy the text, press Command-C on a Mac, or Ctrl-C on a Windows computer.

   ![The Personal Access Token dialog, with the blurred new token in a large text box.](web:firefly-iii/07-token-created)

   > **Note:** Firefly III shows the token only one time. The token is very long, and the dialog has no copy button.

10. Click **Close**.

## Step 2: Add Firefly III in WalletFeed

1. On your iPhone, open WalletFeed.
2. Tap **Destinations**.
3. Tap **+** at the top of the screen.

   ![The Destinations screen in WalletFeed with no destinations, and the + button at the top.](app:docs-destinations-empty-pro)

4. In the **Budgeting** section, tap **Firefly III**.

   If you do not have WalletFeed Pro, WalletFeed first shows the **WalletFeed Pro** screen. After you get WalletFeed Pro, WalletFeed shows the Firefly III screen.

5. Paste the token in the **Personal Access Token** field.

   ![The Firefly III screen in WalletFeed, with the Personal Access Token field, the server address field and three steps.](app:docs-setup-firefly-iii)

   > **Note:** The page that **Firefly III Docs** opens gives the path **Options** › **Profile** › **OAuth**. Firefly III 6.7.9 does not have this path. Step 1 on this page gives the path for Firefly III 6.7.9.

6. In the field that shows `https://firefly.example.com`, type the address that you use to open Firefly III in a web browser.

   After you type the address, WalletFeed makes sure that the token and the address are correct. If they are correct, WalletFeed shows **Account**. If they are not correct, WalletFeed shows an error message (refer to [If there is a problem](#if-there-is-a-problem)). WalletFeed removes a `/`, `/api` or `/api/v1` at the end of the address.

7. If you made an account for your card in Firefly III, select that account in **Account**.

   **Account** shows the active asset accounts and liabilities in Firefly III. If one of these accounts has the name Apple Card, WalletFeed selects it, and **New Apple Card** is not in the list.

   If Firefly III has no account with the name Apple Card, WalletFeed selects **New Apple Card**. With **New Apple Card**, WalletFeed makes an asset account with the name Apple Card in Firefly III. This account has the role **Credit card** and the currency US dollars.

8. Tap **Add**.
9. When WalletFeed shows **Send Transactions to Firefly III?**, tap **Send**.

   The message tells you which data Firefly III receives, from which Wallet accounts and from which date. If you tap **Cancel**, WalletFeed removes the destination and does not send data. If WalletFeed made the Apple Card account, this account stays in Firefly III.

WalletFeed adds **Firefly III · Apple Card** to **Destinations** and starts to send your transactions. WalletFeed keeps the token in the Keychain on your iPhone.

## Step 3: Find your transactions in Firefly III

1. On your computer, in the Firefly III sidebar, click **Accounts**.
2. Click **Asset accounts**.

   ![The Firefly III sidebar, with Accounts open and the highlighted Asset accounts item.](web:firefly-iii/09-accounts-menu)

3. Click **Apple Card** (the account with the role **Credit card**).

   ![The Asset accounts list, with the highlighted Apple Card account and its Credit card role.](web:firefly-iii/12-apple-card-account)

4. Look at the **Transactions** section on the **Apple Card** page.

   ![The Transactions section of the Apple Card account in Firefly III, with six transactions from WalletFeed and their amounts, dates, merchants and categories.](web:firefly-iii/90-walletfeed-result)

## Data that Firefly III receives

WalletFeed puts all of your transactions in one Firefly III account. These transactions come from each Wallet account that WalletFeed has access to. This table shows the Firefly III field for each Wallet field.

| Wallet | Firefly III |
| --- | --- |
| A purchase | A withdrawal from your account to an expense account |
| A refund or a different credit | A deposit to your account from a revenue account |
| Merchant | The name of the expense account or revenue account. If Wallet has no merchant, WalletFeed uses the description. |
| Amount | **Amount**, with two decimals |
| Date | **Date**, with the time on your iPhone |
| Posted date | Book date |
| Description | **Description**. If Wallet has no description, WalletFeed uses the merchant. |
| Category, but not Other | **Category**. If the category is new, Firefly III adds it. |
| Amount in a foreign currency | Foreign amount and foreign currency |
| Card statement text, merchant category code and foreign amount | **Notes** |
| The WalletFeed ID of the transaction | **External ID** |
| No Wallet field | The `walletfeed` tag. A pending charge also has the `pending` tag. |

![A withdrawal in Firefly III, with its category, external ID, notes, and the walletfeed and pending tags.](web:firefly-iii/14-result-transaction-detail)

WalletFeed sets the category and the notes only when it adds a transaction. When WalletFeed updates a transaction, it changes only the amounts, the dates and the `pending` tag. Your changes to the description, the category, the notes and your tags stay.

Firefly III receives a payment to your card as a deposit from a revenue account. In Firefly III, you can change this deposit to a transfer. A rule can also make this change, because Firefly III uses your rules on each new transaction.

If Firefly III does not have the foreign currency, WalletFeed sends the transaction again without the foreign amount. The notes also show the foreign amount.

Your transactions go from your iPhone directly to your Firefly III server. WalletFeed has no account and no WalletFeed servers.

## New and changed transactions

While WalletFeed is open, Firefly III receives changes in seconds. When WalletFeed is not open, iOS starts WalletFeed approximately 1 hour or less after a change in Wallet. If [Background Sync](/docs/background-sync/) is on in **Settings** › **Sync**, WalletFeed then sends the change.

WalletFeed sends a pending charge to Firefly III with the `pending` tag. When Wallet shows the charge as posted, WalletFeed updates the same transaction and removes the `pending` tag. If Wallet shows a charge as declined or expired, WalletFeed deletes the transaction in Firefly III.

> **Caution:** If you add splits to a WalletFeed transaction in Firefly III, WalletFeed does not update that transaction. Thus, the amounts, the dates and the `pending` tag do not change when Wallet changes the charge. If Wallet shows the charge as declined or expired, WalletFeed deletes the transaction and its splits.

If Firefly III does not accept a change, WalletFeed tries to send that change again when it subsequently sends changes.

## Send previous transactions

A new destination also receives previous transactions from the start date in **Settings** › **Sync** › **Initial History**. **Initial History** is **All** until you change it. To change it, do these steps before you add Firefly III:

1. In WalletFeed, tap **Settings** (the gear button) at the top of the screen.
2. In the **Sync** section, tap **Initial History**.

   ![In the Sync section of the Settings screen, Initial History shows All.](app:docs-settings)

3. Select **Today**, **30 Days**, **90 Days**, **1 Year** or **All**.

To send more previous transactions to your Firefly III destination, use [Send History](/docs/send-history/):

1. In **Destinations**, tap your Firefly III destination (for example, **Firefly III · Apple Card**).
2. Tap **Send History**.
3. Select **30 Days**, **90 Days**, **1 Year** or **All**.

WalletFeed does not add a transaction two times. Before WalletFeed adds a transaction, it makes sure that the **External ID** of the transaction is not in Firefly III.

If you delete a transaction in Firefly III, **Send History** does not add it again. If Wallet subsequently changes the amount of that transaction, WalletFeed adds the transaction again.

While WalletFeed sends the transactions, the destination shows **Sending History** and a progress bar.

To stop Send History, tap **Send History** › **Stop Sending**.

## Change or remove the destination

In **Destinations**, tap your Firefly III destination. Then use this table:

| Change | On the destination screen |
| --- | --- |
| Stop the destination for a time | Set **Enabled** to off. |
| Send only some transactions | Set **Filter** to on. Then set **Include**, **Minimum**, **Include Pending**, **Accounts**, **Categories** or **Exclude**. |
| Send transactions from only one Wallet account (for example, Apple Card) | Set **Filter** to on. Then select the account in **Accounts**. |
| Use a new token | Tap **Replace Token**. Paste the new token. Then tap **Replace**. WalletFeed makes sure that Firefly III accepts the token. |
| Make sure that WalletFeed can send | Tap **Send Test**. Firefly III receives a test withdrawal of $4.20 with the merchant WalletFeed. You can delete this withdrawal in Firefly III. |
| Remove the destination | Tap **Delete**. Then tap **Delete** again. The transactions that WalletFeed sent stay in Firefly III. |

For more information about the filter, refer to [Choose what a destination receives](/docs/choose-what-to-send/).

### Replace the token after one year

You can use a personal access token for one year. In Firefly III, **Expires at** shows the last date that you can use the token.

![The Personal Access Tokens list, with the WalletFeed token and its Expires at date.](web:firefly-iii/08-token-list)

1. Make a new token (refer to [step 1](#step-1-make-a-personal-access-token-in-firefly-iii)).
2. In WalletFeed, on the destination screen, tap **Replace Token**.
3. Paste the new token.
4. Tap **Replace**.

### Delete the token in Firefly III

When you remove the destination, the token stays in Firefly III. To delete the token, do these steps:

1. In Firefly III, click the person icon.
2. Click **Remote access and tokens**.
3. In the **WalletFeed** row of **Personal Access Tokens**, click **Delete**.

   ![The Personal Access Tokens list, with the highlighted Delete button for the WalletFeed token.](web:firefly-iii/15-delete-token)

When you click **Delete**, Firefly III deletes the token and does not show a message first. The row stays on the page until you load the page again.

## If there is a problem

### If WalletFeed shows "Use your server's HTTPS address."

The address does not use `https://`. For example, it starts with `http://`.

1. If your server has no `https://` address, get an `https://` address for it (refer to [Before you start](#before-you-start)).
2. Type the `https://` address of your server.

### If WalletFeed shows "iOS doesn't trust your server's certificate."

iOS does not accept the certificate of your server. WalletFeed shows this message for a self-signed certificate.

1. Give your server a certificate that iOS accepts (refer to [Before you start](#before-you-start)).

### If WalletFeed shows "Can't reach your server."

Your iPhone cannot connect to the address. WalletFeed cannot use `localhost` or an address on your home network (for example, `192.168.1.20`).

1. Use an `https://` address that your iPhone can connect to from all locations.

### If WalletFeed shows "No Firefly III API at this address."

The address is not the address of your Firefly III server.

1. Type the address that you use to open Firefly III in a web browser.

### If WalletFeed shows "Token rejected (HTTP 401)"

Firefly III does not accept the token. Possible causes are a deleted token, an expired token or a token that you did not copy fully. The message can also show 403.

1. Make a new token (refer to [step 1](#step-1-make-a-personal-access-token-in-firefly-iii)).
2. Make sure that you copied all of the token.
3. Paste the new token in the **Personal Access Token** field.

### If you closed the token dialog before you copied the token

Firefly III shows a token only one time.

1. In **Personal Access Tokens**, click **Delete** in the row of the token that you did not copy.
2. Make a new token (refer to [step 1](#step-1-make-a-personal-access-token-in-firefly-iii)).

### If the destination shows "Authentication failed"

Firefly III does not accept the token. Possible causes are an expired token or a token that you deleted in Firefly III.

1. Make a new token (refer to [step 1](#step-1-make-a-personal-access-token-in-firefly-iii)).
2. In WalletFeed, on the destination screen, tap **Replace Token**.
3. Paste the new token.
4. Tap **Replace**.

### If the destination shows "Can't connect"

Your iPhone cannot connect to the server. This can occur when your iPhone is not on your home Wi-Fi. WalletFeed tries to connect again when it subsequently sends changes.

1. Make sure that your iPhone can open the `https://` address of the server from all locations.

### If a new transaction is not in Current balance

The server time is before the time on your iPhone. As a result, the transaction has a time after the server time.

1. Set `TZ` in the configuration of the server to your time zone.
