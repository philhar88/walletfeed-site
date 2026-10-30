# Send Apple Card transactions to Sure

WalletFeed sends your Apple Card, Apple Cash and Savings transactions from your iPhone to Sure. Sure is a self-hosted budget app that is a fork of Maybe Finance. You add a card account and make an API key in Sure. Then you paste the key in WalletFeed.

## Before you start

You must have these items:

- An iPhone with iOS 26 or a newer version. WalletFeed is available only in the US.
- Apple Card, Apple Cash or Savings in Wallet on that iPhone.
- WalletFeed with [WalletFeed Pro](/docs/walletfeed-pro/), a subscription with a 1-week free trial, or a one-time Lifetime purchase.
- A Sure server and an account on that server. Sure is open source, and you can get it without a purchase.
- An `https://` address for the Sure server. [Step 1](#step-1-get-an-https-address-for-your-sure-server) gives the conditions for this address.
- A computer with a web browser. You use it to add the card account and to make the key in Sure.

## Step 1: Get an HTTPS address for your Sure server

WalletFeed connects only to an address that starts with `https://`. With [Background Sync](/docs/background-sync/), WalletFeed also sends transactions when your iPhone is not on your home network. Thus, your iPhone must connect to the address from all locations.

If you install Sure with Docker and do not change its configuration, Sure uses an `http://` address on port 3000. WalletFeed cannot use this address. A tunnel service, for example Tailscale or Cloudflare Tunnel, can give Sure an `https://` address.

1. If the address of your Sure server starts with `http://`, make an `https://` address with a tunnel service.
2. If a tunnel service gives Sure its `https://` address, set `RAILS_ASSUME_SSL: "true"` in the Sure configuration.

   The HTTPS section of [the Docker instructions for Sure](https://github.com/we-promise/sure/blob/main/docs/hosting/docker.md) gives more information.

3. Disconnect your iPhone from your home Wi-Fi.
4. On your iPhone, open the `https://` address of your Sure server in Safari.
5. Make sure that Sure opens.

## Step 2: Add a card account in Sure

WalletFeed writes the transactions to one account in Sure. The Sure API cannot make accounts. Thus, you must add the account in Sure first.

1. On your computer, open your Sure server in a web browser.
2. If a **What's new** dialog opens, click **Got it**.
3. On **Home** › **Dashboard**, click **Add account** or **New**.

   ![The Sure dashboard with no accounts and the Add account button highlighted.](https://walletfeed.app/guides/apple-card-to-sure/sure-home-add-account.webp)

4. Click **Credit Card**.

   ![The Sure dialog that shows the account types, with Credit Card highlighted.](https://walletfeed.app/guides/apple-card-to-sure/sure-choose-credit-card.webp)

5. Click **Enter account balance**.

   ![The Sure dialog that shows the procedures to add the card, with Enter account balance highlighted.](https://walletfeed.app/guides/apple-card-to-sure/sure-enter-account-balance.webp)

6. In **Account name**, type `Apple Card`.
7. In **Balance on date:**, type `0`, or type the card balance on the **Opening balance date**.
8. Click **Create Account**.

   ![The credit card form in Sure with the name Apple Card, and with the Create Account button highlighted.](https://walletfeed.app/guides/apple-card-to-sure/sure-credit-card-details.webp)

> **Note:** Sure shows a credit card on the **Debts** tab of the account list. The **Assets** tab does not show it.

> **Note:** Sure calculates the card balance from the balance in **Balance on date:** and from the transactions that Sure receives. The balance in Sure is the same as the balance in Wallet only if the balance in **Balance on date:** is correct. Sure sets the **Opening balance date** to 2 years before the day that you add the account.

## Step 3: Make a Read/Write API key in Sure

WalletFeed uses the key to read your Sure accounts and to write transactions. With [Universal Clipboard](https://support.apple.com/en-us/102430), you can copy the key on a Mac and paste it on your iPhone.

> **Caution:** Do not send the key to yourself in a message or an e-mail. With the key, a different person can read your Sure accounts and write transactions.

1. On your computer, open your Sure server in a web browser.
2. At the bottom of the left bar, click the button that shows the first letters of your name.

   ![The Sure account page with the button at the bottom of the left bar highlighted.](https://walletfeed.app/guides/apple-card-to-sure/sure-open-account-menu.webp)

3. Click **Settings**.

   ![The Sure account menu, with Settings highlighted.](https://walletfeed.app/guides/apple-card-to-sure/sure-account-menu-settings.webp)

4. In the **Settings** list, scroll to the **ADVANCED** group.
5. Click **API Keys**.

   ![The Sure Settings list with API Keys highlighted in the ADVANCED group.](https://walletfeed.app/guides/apple-card-to-sure/sure-settings-api-keys.webp)

6. Click **New API Key**.

   ![The API Keys page in Sure, with no keys and the New API Key button highlighted.](https://walletfeed.app/guides/apple-card-to-sure/sure-api-keys-empty.webp)

7. In **API Key Name**, type `WalletFeed`.
8. In **Permissions**, click **Read/Write**.

   ![The page for a new key in Sure with the name WalletFeed, and with the Read/Write permission highlighted.](https://walletfeed.app/guides/apple-card-to-sure/sure-create-key-read-write.webp)

9. Click **Save API Key**.

   ![The page for a new key in Sure, with the Save API Key button highlighted.](https://walletfeed.app/guides/apple-card-to-sure/sure-save-api-key.webp)

10. Click **Copy API Key**.

    ![The API Key Created Successfully page in Sure, with the Copy API Key button highlighted.](https://walletfeed.app/guides/apple-card-to-sure/sure-key-created-copy.webp)

> **Note:** Sure shows the key on this page only. The `curl` example on the same page also contains the key, but WalletFeed cannot use the `curl` example.

> **Note:** Sure does not select a permission for you. With a **Read Only** key, Sure does not accept the transactions from WalletFeed.

To make the key on your iPhone, do these steps:

1. In WalletFeed, do steps 1 to 5 of [Step 4](#step-4-add-sure-in-walletfeed).
2. Tap **Open API Keys**. Your web browser opens the **API Keys** page of your Sure server.
3. If Sure shows its sign-in page, get access to your Sure account.
4. If Sure then shows its dashboard, tap **Open API Keys** in WalletFeed again.
5. On the **API Keys** page, do steps 6 to 10 of the first procedure in Step 3.
6. Open WalletFeed again.
7. Do steps 6 to 10 of Step 4.

## Step 4: Add Sure in WalletFeed

1. On your iPhone, open WalletFeed.
2. Tap **Destinations**.
3. Tap **+** at the top of the screen.

   ![The empty Destinations screen with the + button at the top.](https://walletfeed.app/guides/apple-card-to-sure/walletfeed-destinations-empty-pro.webp)

4. In **Budgeting**, tap **Sure**. If you do not have WalletFeed Pro, WalletFeed first shows the WalletFeed Pro screen.

   ![The Add Destination list, with Sure and the text Self-hosted in the Budgeting group.](https://walletfeed.app/guides/apple-card-to-sure/walletfeed-add-destination.webp)

5. In the field that shows `https://sure.example.com`, type the `https://` address of your Sure server.

   ![The WalletFeed screen for Sure with the server field, the API Key field and three steps.](https://walletfeed.app/guides/apple-card-to-sure/walletfeed-setup-sure.webp)

6. In **API Key**, paste the key. WalletFeed connects to Sure and shows **Account**.
7. In **Account**, select your card account.

   If an account has Apple Card in its name, WalletFeed selects that account for you. If no account has Apple Card in its name, WalletFeed selects a credit card account.

8. Tap **Add**.
9. In the **Send Transactions to Sure?** message, tap **Send**.

   The message tells you the data that Sure will receive, the Wallet accounts and the start date.

10. On your computer, click **Transactions** in Sure. Sure shows the transactions from WalletFeed in the list.

    ![The Sure Transactions page with seven sample transactions from WalletFeed in the Apple Card account.](https://walletfeed.app/guides/apple-card-to-sure/sure-walletfeed-result.webp)

## Data that Sure receives

WalletFeed sends these fields for each transaction to the Sure account that you selected:

| From Wallet | In Sure |
| --- | --- |
| The date of the transaction, in your time zone | Date |
| The merchant name, or the description if there is no merchant name | Name |
| The amount | Amount. A purchase is an expense, and a refund or other credit is income. |
| The currency | Currency |
| The ID of the transaction in Wallet | An ID that WalletFeed uses to change the transaction |

WalletFeed does not send categories. Sure shows new transactions as **Uncategorized** until you give them a category.

Sure shows a purchase with a minus sign, for example -$6.75, and a refund in green without a minus sign. The **Debt balance** of the card increases with each purchase.

WalletFeed has no account and no WalletFeed servers. Thus, your iPhone sends the transactions directly to your Sure server. The server address and the key stay in the Keychain on your iPhone.

## New and changed transactions

While WalletFeed is open, Sure receives changes in seconds. When WalletFeed is not open, iOS starts WalletFeed approximately 1 hour or less after a change in Wallet. If [Background Sync](/docs/background-sync/) is on in **Settings** › **Sync**, WalletFeed then sends the change.

WalletFeed sends a pending charge to Sure. Sure does not show that the charge is pending. When Wallet shows the charge as posted, the date or the amount can change. Then WalletFeed makes the same change in Sure. WalletFeed does not change the name, category, merchant, tags and notes that you set in Sure.

If Wallet removes a pending charge, for example a declined charge, WalletFeed deletes the transaction from Sure. WalletFeed deletes only transactions from the last 90 days.

If WalletFeed sends a transaction again, Sure does not make a second copy. Sure keeps one transaction for each Wallet transaction.

## Send previous transactions

A new destination also receives previous transactions from the start date in **Settings** › **Sync** › **Initial History**. **Initial History** is **All** until you change it.

You can also send previous transactions with [Send History](/docs/send-history/):

1. In WalletFeed, tap **Destinations**.
2. Tap the Sure destination, for example **Sure · Apple Card**.
3. Tap **Send History**.
4. Tap **30 Days**, **90 Days**, **1 Year** or **All**. WalletFeed shows **Sending History** with the number of transactions that it sent.

To stop Send History before WalletFeed sends all of the transactions, tap **Send History** › **Stop Sending**.

## Change or remove the destination

To open the Sure destination, do these steps:

1. In WalletFeed, tap **Destinations**.
2. Tap the Sure destination.

For more information, refer to [Destinations](/docs/destinations/).

### Send only some transactions

1. Set **Filter** to on.
2. Select the transactions with **Include**, **Minimum**, **Include Pending**, **Accounts**, **Categories** and **Exclude**.

To send only Apple Card transactions to this destination, select Apple Card in **Accounts**.

For more information, refer to [Choose what a destination receives](/docs/choose-what-to-send/).

### Replace the key

1. Make a new Read/Write key in Sure, as in [Step 3](#step-3-make-a-read-write-api-key-in-sure). While the previous key is active, the new key must have a different name, for example `WalletFeed 2`.
2. In the Sure destination, tap **Replace Key**.
3. In **API Key**, paste the new key.
4. Tap **Replace**.

WalletFeed keeps the new key only if the key can read the card account and write transactions.

### Stop or remove the destination

To stop the destination but not remove it, set **Enabled** to off.

To remove the destination, do these steps:

1. In the Sure destination, tap **Delete**.
2. In the **Delete Sure · Apple Card?** message, tap **Delete**.
3. On your computer, open **Settings** › **API Keys** in Sure.
4. Click **Revoke** for the WalletFeed key.

   ![The API Keys list in Sure, with the Revoke button for the WalletFeed key highlighted.](https://walletfeed.app/guides/apple-card-to-sure/sure-revoke-key.webp)

5. Click **Confirm**.

   ![The Sure dialog about the WalletFeed key, with Confirm highlighted.](https://walletfeed.app/guides/apple-card-to-sure/sure-revoke-confirm.webp)

If you remove the destination, the transactions that WalletFeed sent stay in Sure.

## If there is a problem

### If WalletFeed does not show Account or Open API Keys

The address starts with `http://`. WalletFeed connects only to `https://` addresses, and it shows no message for an `http://` address.

1. Get an `https://` address for your Sure server, as in [Step 1](#step-1-get-an-https-address-for-your-sure-server).
2. In WalletFeed, type the `https://` address.

### If WalletFeed shows "Create an account in Sure"

When Sure has no accounts, WalletFeed shows "Create an account in Sure for your card, then try again."

1. Add a card account in Sure, as in [Step 2](#step-2-add-a-card-account-in-sure).
2. In WalletFeed, delete the key in **API Key**.
3. Paste the key in **API Key** again.
4. Make sure that WalletFeed shows **Account**.

### If WalletFeed shows "Key rejected (HTTP 401)"

When Sure does not accept the key, WalletFeed shows "Key rejected (HTTP 401). Use a Read/Write key." The key is incorrect or expired, or you clicked **Revoke** for the key in Sure.

1. Make sure that you copied the key with **Copy API Key**, and not the `curl` example.
2. If you copied the `curl` example, do the steps in [If you closed the key page before you copied the key](#if-you-closed-the-key-page-before-you-copied-the-key).
3. If you copied the key with **Copy API Key**, make a new Read/Write key in Sure, as in [Step 3](#step-3-make-a-read-write-api-key-in-sure). While the previous key is active, the new key must have a different name, for example `WalletFeed 2`.
4. In WalletFeed, paste the new key in **API Key**.

### If Destinations shows "Authentication failed" for Sure

Sure does not accept the key when WalletFeed sends transactions. For example, this occurs if the key is **Read Only**, or if you clicked **Revoke** for the key in Sure.

1. In WalletFeed, tap **Destinations**.

   ![The Destinations screen, where one destination shows Authentication failed.](https://walletfeed.app/guides/apple-card-to-sure/walletfeed-destinations-failure.webp)

2. Tap the Sure destination.
3. Replace the key, as in [Replace the key](#replace-the-key).

### If WalletFeed shows "Can't connect" or "Couldn't connect"

WalletFeed cannot connect to your Sure server. The server does not operate, or your iPhone can connect to it only on your home network.

1. Make sure that your Sure server operates.
2. Disconnect your iPhone from your home Wi-Fi.
3. On your iPhone, open the `https://` address of your Sure server in Safari.
4. If Sure does not open, get an `https://` address for all locations, as in [Step 1](#step-1-get-an-https-address-for-your-sure-server).
5. If you added Sure in WalletFeed, tap **Send Test** in the Sure destination.

The test writes a transaction of $4.20 with the name WalletFeed to the card account in Sure. You can delete the test transaction in Sure.

### If WalletFeed shows "No Sure API at this address"

When the address is not correct, WalletFeed shows "No Sure API at this address, or the account is gone." If you deleted the card account, WalletFeed also shows this message when you replace the key.

1. Make sure that the address is the same address that you use to open Sure in a web browser.
2. If you deleted the card account in Sure, add a new card account, as in [Step 2](#step-2-add-a-card-account-in-sure).
3. If you added a new card account, add Sure again in WalletFeed, as in [Step 4](#step-4-add-sure-in-walletfeed).

### If you closed the key page before you copied the key

Sure shows a key one time only. Sure also does not accept two active keys with the same name.

1. On your computer, open **Settings** › **API Keys** in Sure.
2. Click **Revoke** for the WalletFeed key.
3. Click **Confirm**.
4. Make a new Read/Write key in Sure, as in [Step 3](#step-3-make-a-read-write-api-key-in-sure).
5. In WalletFeed, paste the new key in **API Key**.

### If the card balance in Sure is not correct

Sure calculates the balance from the balance in **Balance on date:** and from the transactions. If Sure receives many transactions in a short time, Sure can show a balance without the last transaction.

1. In Sure, open the card account.
2. On the right side of the account name, click the icon with two arrows in a circle. Sure calculates the card balance again.

   ![The Apple Card account in Sure, with the icon of two arrows in a circle highlighted.](https://walletfeed.app/guides/apple-card-to-sure/sure-refresh-account-balance.webp)
