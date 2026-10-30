# Send Apple Card transactions to Firefly III

WalletFeed sends your Apple Card, Apple Cash and Savings transactions from your iPhone to one account on your Firefly III server. You make a personal access token in Firefly III. Then you paste the token and the address of your server into WalletFeed.

## Before you start

- An iPhone with iOS 26 or a newer version. WalletFeed is available only in the US.
- Apple Card, Apple Cash or Savings in Wallet on that iPhone, and WalletFeed with [access to your Wallet accounts](/docs/wallet-accounts/).
- [WalletFeed Pro](/docs/walletfeed-pro/), which is necessary for destinations. WalletFeed Pro is a subscription with a 1-week free trial, or a one-time Lifetime purchase.
- Your Firefly III server, and a user account on it.
- An `https://` address for the server, with a certificate that iOS accepts. Your iPhone must connect to this address from all locations, not only on your home Wi-Fi.
- Your time zone in `TZ` on the server.

WalletFeed cannot use an `http://` address. The Firefly III image for Docker uses `http://` on port 8080. To get an `https://` address with a certificate that iOS accepts, you can use one of these:

- Tailscale HTTPS, with an address that ends in `.ts.net`
- A reverse proxy with a certificate from Let's Encrypt
- Cloudflare Tunnel

You can also make a root certificate and install it on your iPhone. Then, in **Settings** › **General** › **About** › **Certificate Trust Settings**, set the switch for that certificate to on.

WalletFeed sends the time of each transaction as the time on your iPhone, without a time zone. If the server uses a different time zone, a new transaction can have a time after the time on the server. Then Firefly III does not include the transaction in **Current balance** for some hours. If `TZ` has no value, Firefly III uses UTC.

## Step 1: Make a personal access token in Firefly III

You can do these steps on a computer, or in Safari on your iPhone. With Universal Clipboard, you can copy the token on a Mac and paste it on your iPhone. Do not send the token to yourself in a message or an email.

1. On your computer, sign in to Firefly III in a web browser.
2. Click the person icon at the top right of the page. The icon has no text.

   ![The Firefly III home page with the person icon at the top right highlighted.](https://walletfeed.app/guides/apple-card-to-firefly-iii/firefly-iii-user-icon.webp)

3. Click **Remote access and tokens**.

   ![The Firefly III account menu, with Remote access and tokens highlighted.](https://walletfeed.app/guides/apple-card-to-firefly-iii/firefly-iii-user-menu.webp)

4. In the **Personal Access Tokens** section, click **Create new token**.

   ![The Remote access and tokens page, with the Create new token button in the Personal Access Tokens section highlighted.](https://walletfeed.app/guides/apple-card-to-firefly-iii/firefly-iii-remote-access-page.webp)

   Do not click **Create New Client** in the **OAuth Clients and Applications** section. WalletFeed does not use OAuth clients.

5. In **Name**, type `WalletFeed`.
6. Click **Create**.

   ![The Create token dialog, with WalletFeed in the Name field and the Create button highlighted.](https://walletfeed.app/guides/apple-card-to-firefly-iii/firefly-iii-create-token.webp)

7. Click in the large box that shows the token.
8. To select all the text in the box, press Command-A on a Mac, or Ctrl-A on Windows.
9. Copy the text.

   ![The Personal Access Token dialog with the new token, blurred here, in a large text box.](https://walletfeed.app/guides/apple-card-to-firefly-iii/firefly-iii-token-created.webp)

   > **Note:** Firefly III shows the token only one time. The token is very long, and the dialog has no copy button.

10. Click **Close**.

The token gives full access to your Firefly III data. WalletFeed keeps the token in the Keychain on your iPhone.

## Step 2: Add Firefly III in WalletFeed

1. On your iPhone, open WalletFeed.
2. Tap **Destinations**.
3. Tap **+** at the top of the screen.

   ![The Destinations screen in WalletFeed with no destinations, and the + button at the top.](https://walletfeed.app/guides/apple-card-to-firefly-iii/walletfeed-destinations-empty-pro.webp)

4. In the **Budgeting** section, tap **Firefly III**.

   If you do not have WalletFeed Pro, WalletFeed first shows the **WalletFeed Pro** screen. After you get WalletFeed Pro, WalletFeed shows the Firefly III screen.

5. Paste the token into **Personal Access Token**.

   ![The Firefly III screen in WalletFeed, with the Personal Access Token field, the server address field and three steps.](https://walletfeed.app/guides/apple-card-to-firefly-iii/walletfeed-setup-firefly-iii.webp)

   > **Note:** The steps on this screen and the **Firefly III Docs** link give the path **Options** › **Profile** › **OAuth**. Firefly III 6.7.9 does not have this path. Step 1 on this page gives the path for Firefly III 6.7.9.

6. In the field that shows `https://firefly.example.com`, type the address of your server.

   Use the address that you use to open Firefly III in a browser. WalletFeed removes a `/` or `/api/v1` at the end. Then WalletFeed makes sure that the token and the address are correct, and shows **Account**.

7. Make sure that **Account** shows **New Apple Card**.

   With **New Apple Card**, WalletFeed makes an asset account with the name Apple Card in Firefly III. Its role is **Credit card**, and its currency is US dollars.

   If you made an account for your card in Firefly III, select that account. The list shows the active asset accounts and liabilities in Firefly III. If Firefly III has an account with the name Apple Card, WalletFeed selects it, and **New Apple Card** is not in the list.

8. Tap **Add**.
9. When WalletFeed shows **Send Transactions to Firefly III?**, tap **Send**.

   The message tells you which data Firefly III receives, from which Wallet accounts and from which date. If you tap **Cancel**, WalletFeed removes the destination and sends nothing.

WalletFeed adds **Firefly III · Apple Card** to **Destinations**, and starts to send your transactions.

## Step 3: Find your transactions in Firefly III

1. On your computer, in the Firefly III sidebar, click **Accounts**.
2. Click **Asset accounts**.

   ![The Firefly III sidebar, with Accounts open and Asset accounts highlighted.](https://walletfeed.app/guides/apple-card-to-firefly-iii/firefly-iii-accounts-menu.webp)

3. Click **Apple Card**. Its role is **Credit card**.

   ![The Asset accounts list, with the Apple Card credit card account highlighted.](https://walletfeed.app/guides/apple-card-to-firefly-iii/firefly-iii-apple-card-account.webp)

4. Look at the **Transactions** section on the **Apple Card** page.

   ![The Apple Card account in Firefly III, with six card transactions and their amounts, dates, merchants and categories.](https://walletfeed.app/guides/apple-card-to-firefly-iii/firefly-iii-result-transactions.webp)

## Data that Firefly III receives

WalletFeed puts the transactions from all the Wallet accounts that you share into the one Firefly III account. This table shows the Firefly III field for each Wallet field.

| Wallet | Firefly III |
| --- | --- |
| A purchase | A withdrawal from your account to an expense account |
| A refund or a different credit | A deposit into your account from a revenue account |
| Merchant | The name of the expense account or revenue account. If Wallet has no merchant, WalletFeed uses the description. |
| Amount | **Amount**, with two decimals |
| Date | **Date**, in the time of your iPhone |
| Posted date | Book date |
| Description | **Description**. If Wallet has no description, WalletFeed uses the merchant. |
| Category, but not Other | **Category**. Firefly III adds the category if it is new. |
| Amount in a foreign currency | Foreign amount and foreign currency |
| Card statement text, merchant category code and foreign amount | **Notes** |
| The WalletFeed ID of the transaction | **External ID** |
| No Wallet field | The `walletfeed` tag. A pending charge also has the `pending` tag. |

![A Firefly III transaction from WalletFeed, with its category, external ID, notes, and the walletfeed and pending tags.](https://walletfeed.app/guides/apple-card-to-firefly-iii/firefly-iii-result-transaction-detail.webp)

WalletFeed sets the category and the notes only when it adds a transaction. When it updates a transaction, it changes only the amounts, the dates and the `pending` tag. Your changes to the description, the category, the notes and your tags stay.

Firefly III applies your rules to each new transaction. Firefly III receives a payment to your card as a deposit from a revenue account. You can change it to a transfer in Firefly III, or with a rule.

If Firefly III does not have the foreign currency, WalletFeed sends the transaction again without the foreign amount. The notes also show the foreign amount.

Your transactions go from your iPhone directly to your Firefly III server. WalletFeed has no account and no WalletFeed servers.

## Sync times and changes

While WalletFeed is open, Firefly III receives changes in seconds. When WalletFeed is closed, iOS starts WalletFeed in approximately 1 hour or less after a change in Wallet. For this, [Background Sync](/docs/background-sync/) must be on in **Settings** › **Sync**.

A pending charge goes to Firefly III with the `pending` tag. When Wallet shows the charge as posted, WalletFeed updates the same transaction and removes the `pending` tag. If a transaction has more than one split in Firefly III, WalletFeed does not change it.

If Wallet shows a charge as declined or expired, WalletFeed deletes the transaction in Firefly III.

If Firefly III does not accept a change, WalletFeed tries to send it again the next time that it syncs.

## Send previous transactions

A new destination also receives previous transactions, from the start date in **Settings** › **Sync** › **Initial History**. **Initial History** is **All** until you change it. To change it, do these steps before you add Firefly III:

1. In WalletFeed, tap **Settings** (the gear button) at the top of the screen.
2. In **Sync**, tap **Initial History**, then select **Today**, **30 Days**, **90 Days**, **1 Year** or **All**.

   ![Settings, with Initial History set to All in the Sync section.](https://walletfeed.app/guides/apple-card-to-firefly-iii/walletfeed-settings.webp)

To send more previous transactions to your Firefly III destination, use [Send History](/docs/send-history/):

1. In **Destinations**, tap your Firefly III destination, such as **Firefly III · Apple Card**.
2. Tap **Send History**, then select **30 Days**, **90 Days**, **1 Year** or **All**.

WalletFeed does not add a transaction two times. Before it adds a transaction, it looks for the **External ID** in Firefly III. While WalletFeed sends, the destination shows **Sending History** and the progress. To stop, tap **Send History** › **Stop Sending**.

## Change or remove the destination

In **Destinations**, tap your Firefly III destination. Then use this table:

| Change | On the destination screen |
| --- | --- |
| Stop the destination for a time | Set **Enabled** to off. |
| Send only some transactions | Set **Filter** to on. Then set **Include**, **Minimum**, **Include Pending**, **Accounts**, **Categories** or **Exclude**. |
| Send only one Wallet account, such as Apple Card | Set **Filter** to on, then select the account in **Accounts**. |
| Use a new token | Tap **Replace Token**, paste the token, then tap **Replace**. WalletFeed makes sure that Firefly III accepts the token. |
| Make sure that WalletFeed can send | Tap **Send Test**. Firefly III receives a test withdrawal of $4.20, with the merchant WalletFeed. You can delete it in Firefly III. |
| Remove the destination | Tap **Delete**, then tap **Delete** again. The transactions that WalletFeed sent stay in Firefly III. |

For more information about the filter, refer to [Choose what a destination receives](/docs/choose-what-to-send/).

### Replace the token after one year

You can use a personal access token for one year. In Firefly III, **Expires at** shows the last date of the token.

![The Personal Access Tokens list with one token named WalletFeed and its Expires at date.](https://walletfeed.app/guides/apple-card-to-firefly-iii/firefly-iii-token-list.webp)

1. Make a new token, as in [step 1](#step-1-make-a-personal-access-token-in-firefly-iii).
2. In WalletFeed, on the destination screen, tap **Replace Token**.
3. Paste the new token, then tap **Replace**.

### Delete the token in Firefly III

When you remove the destination, the token stays in Firefly III. To delete the token:

1. In Firefly III, click the person icon, then click **Remote access and tokens**.
2. In the **WalletFeed** row of **Personal Access Tokens**, click **Delete**.

   ![The Personal Access Tokens list, with the Delete button for the WalletFeed token highlighted.](https://walletfeed.app/guides/apple-card-to-firefly-iii/firefly-iii-delete-token.webp)

Firefly III deletes the token when you click **Delete**, and does not show a message first. The row stays on the page until you load the page again.

## If there is a problem

### If WalletFeed shows "Use your server's HTTPS address."

The address does not start with `https://`.

1. Type the `https://` address of your server. If your server has no `https://` address, refer to [Before you start](#before-you-start).

### If WalletFeed shows "iOS doesn't trust your server's certificate."

iOS does not accept the certificate of your server. A self-signed certificate gives this message.

1. Give your server a certificate that iOS accepts, as in [Before you start](#before-you-start).

### If WalletFeed shows "Can't reach your server."

Your iPhone cannot connect to the address. WalletFeed cannot use `localhost`, or an address on your home network such as `192.168.1.20`.

1. Use an `https://` address that your iPhone can connect to from all locations.

### If WalletFeed shows "No Firefly III API at this address."

The address does not go to Firefly III.

1. Type the address that you use to open Firefly III in a browser.

### If WalletFeed shows "Token rejected (HTTP 401)"

Firefly III does not accept the token. You did not copy all of the token, you deleted the token, or the token is expired. The number can also be 403.

1. Make a new token, as in [step 1](#step-1-make-a-personal-access-token-in-firefly-iii).
2. Make sure that you copy all the text in the token box.
3. Paste the new token into **Personal Access Token**.

### If you closed the token dialog before you copied the token

Firefly III shows a token only one time.

1. In **Personal Access Tokens**, click **Delete** in the row of that token.
2. Make a new token, as in [step 1](#step-1-make-a-personal-access-token-in-firefly-iii).

### If the destination shows "Authentication failed"

Firefly III does not accept the token now. The token can be expired, or you deleted it in Firefly III.

1. Make a new token, as in [step 1](#step-1-make-a-personal-access-token-in-firefly-iii).
2. In WalletFeed, on the destination screen, tap **Replace Token**.
3. Paste the new token, then tap **Replace**.

### If the destination shows "Can't connect"

Your iPhone cannot connect to the server, for example when you are not on your home Wi-Fi. WalletFeed tries again the next time that it syncs.

1. Make sure that your iPhone can open the `https://` address of the server from all locations.

### If a new transaction is not in Current balance

The server uses a different time zone from your iPhone. The transaction has a time after the time on the server.

1. Set `TZ` on the server to your time zone.
