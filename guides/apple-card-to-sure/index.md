# Send Apple Card transactions to Sure

WalletFeed sends your Apple Card, Apple Cash and Savings transactions from your iPhone to Sure, the self-hosted budget app that is a fork of Maybe Finance. You add a card account and make an API key in Sure. Then you paste the key into WalletFeed.

## Before you start

You must have these items:

- An iPhone with iOS 26 or a newer version. WalletFeed is available only in the US.
- Apple Card, Apple Cash or Savings in Wallet on that iPhone.
- WalletFeed with [WalletFeed Pro](/docs/walletfeed-pro/), a subscription with a 1-week free trial, or a one-time Lifetime purchase.
- A Sure server and an account on that server. Sure is open source, and you can get it without a purchase.
- An `https://` address for the Sure server. [Step 1](#step-1-get-an-https-address-for-your-sure-server) gives the conditions for this address.
- A computer with a web browser. You use it to add the card account and to make the key in Sure.

## Step 1: Get an HTTPS address for your Sure server

WalletFeed connects only to an address that starts with `https://`. [Background Sync](/docs/background-sync/) also sends transactions when your iPhone can be away from your home network. Thus, your iPhone must connect to the address from all locations.

If you install Sure with Docker and do not change its configuration, Sure uses an `http://` address on port 3000. WalletFeed cannot use this address.

1. If the address of your Sure server starts with `http://`, use a tunnel service to make an `https://` address. Tailscale and Cloudflare Tunnel are examples of tunnel services.
2. If a tunnel service gives Sure its `https://` address, set `RAILS_ASSUME_SSL: "true"` in the Sure configuration. For more information, refer to the HTTPS section of [the Docker instructions for Sure](https://github.com/we-promise/sure/blob/main/docs/hosting/docker.md).
3. Disconnect your iPhone from your home Wi-Fi.
4. On your iPhone, open the `https://` address of your Sure server in Safari.
5. Make sure that Sure opens.

## Step 2: Add a card account in Sure

WalletFeed writes the transactions into one account in Sure. The Sure API cannot make accounts. Thus, you must add the account in Sure first.

1. On your computer, open your Sure server in a web browser.
2. If a **What's new** dialog opens, click **Got it**.
3. On **Home** › **Dashboard**, click **Add account** or **New**.

   ![The Sure dashboard with no accounts and the Add account button highlighted.](https://walletfeed.app/guides/apple-card-to-sure/sure-home-add-account.webp)

4. Click **Credit Card**.

   ![The Sure dialog that shows the account types, with Credit Card highlighted.](https://walletfeed.app/guides/apple-card-to-sure/sure-choose-credit-card.webp)

5. Click **Enter account balance**.

   ![The Sure dialog that shows the methods to add the card, with Enter account balance highlighted.](https://walletfeed.app/guides/apple-card-to-sure/sure-enter-account-balance.webp)

6. In **Account name**, type `Apple Card`.
7. In **Balance on date:**, type `0`, or type the card balance on the **Opening balance date**.
8. Click **Create Account**.

   ![The credit card form in Sure with the name Apple Card, and with the Create Account button highlighted.](https://walletfeed.app/guides/apple-card-to-sure/sure-credit-card-details.webp)

> **Note:** Sure shows a credit card on the **Debts** tab of the account list. The **Assets** tab does not show it.

> **Note:** Sure calculates the card balance from the balance in **Balance on date:** and from the transactions that it receives. The balance in Sure agrees with Wallet only if the balance in **Balance on date:** is correct.

## Step 3: Make a Read/Write API key in Sure

WalletFeed uses the key to read your Sure accounts and to write transactions. With Universal Clipboard, you can copy the key on a Mac and paste it on your iPhone. Do not send the key to yourself in a message or an email.

1. On your computer, open your Sure server in a web browser.
2. At the bottom of the left bar, click the circular button that shows the first letters of your name.

   ![The Sure account page with the circular button at the bottom of the left bar highlighted.](https://walletfeed.app/guides/apple-card-to-sure/sure-open-account-menu.webp)

3. Click **Settings**.

   ![The Sure account menu, with Settings highlighted.](https://walletfeed.app/guides/apple-card-to-sure/sure-account-menu-settings.webp)

4. In the Settings list, scroll down to the **ADVANCED** group.
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

    ![The Sure page that shows the new key one time, with the Copy API Key button highlighted.](https://walletfeed.app/guides/apple-card-to-sure/sure-key-created-copy.webp)

> **Note:** Sure shows the key on this page only. The `curl` example on the same page also contains the key, but WalletFeed cannot use the full `curl` line.

> **Note:** Sure does not select a permission for you. WalletFeed does not accept a **Read Only** key.

To make the key on your iPhone, do these steps:

1. In WalletFeed, do steps 1 to 6 of [Step 4](#step-4-add-sure-in-walletfeed).
2. Tap **Open API Keys**. WalletFeed opens the **API Keys** page of your Sure server.
3. If Sure shows its sign-in page, sign in.
4. If Sure then shows its dashboard, tap **Open API Keys** in WalletFeed again.
5. On the **API Keys** page, do steps 6 to 10 of the first procedure in Step 3.

## Step 4: Add Sure in WalletFeed

1. On your iPhone, open WalletFeed.
2. Tap **Destinations**.
3. Tap **+**.

   ![The empty Destinations screen with the + button at the top.](https://walletfeed.app/guides/apple-card-to-sure/walletfeed-destinations-empty-pro.webp)

4. In **Budgeting**, tap **Sure**. If you do not have WalletFeed Pro, WalletFeed first shows the WalletFeed Pro screen.

   ![The Add Destination list, with Sure and the text Self-hosted in the Budgeting group.](https://walletfeed.app/guides/apple-card-to-sure/walletfeed-add-destination.webp)

5. In the field that shows `https://sure.example.com`, type the `https://` address of your Sure server.
6. If WalletFeed shows **Use an API Key Instead**, tap it.

   In Sure v0.7.6, WalletFeed does not connect with **Sign In with Sure**. For more information, refer to [If Sure opens the dashboard after you sign in](#if-sure-opens-the-dashboard-after-you-sign-in).

7. In **API Key**, paste the key. WalletFeed connects to Sure and shows **Account**.

   ![The Sure setup screen in WalletFeed with the server field, the API Key field and three steps.](https://walletfeed.app/guides/apple-card-to-sure/walletfeed-setup-sure.webp)

8. In **Account**, select your card account. If an account has Apple Card in its name, WalletFeed selects that account for you.
9. Tap **Add**.
10. In the **Send Transactions to Sure?** message, tap **Send**. The message tells you the data that Sure receives, the Wallet accounts and the start date.
11. On your computer, click **Transactions** in Sure. Sure shows the transactions from WalletFeed in the list.

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

Sure shows a purchase with a minus sign, for example -$6.75. It shows a refund in green without a minus sign. The **Debt balance** of the card increases with each purchase.

WalletFeed sends the transactions from your iPhone directly to your Sure server. WalletFeed has no account and no WalletFeed servers. The server address and the key stay in the Keychain on your iPhone.

## New and changed transactions

While WalletFeed is open, Sure receives changes in seconds. When WalletFeed is closed, iOS starts WalletFeed in approximately 1 hour or less after a change in Wallet. Then WalletFeed sends the change. For this, [Background Sync](/docs/background-sync/) must be on in **Settings** › **Sync**.

WalletFeed sends a pending charge to Sure as a usual transaction. When Wallet shows the charge as posted, WalletFeed changes the date and the amount in Sure to agree with Wallet. The name, category, merchant, tags and notes that you set in Sure stay the same.

If Wallet removes a pending charge, for example a declined charge, WalletFeed deletes the transaction from Sure. WalletFeed deletes only transactions from the last 90 days.

If WalletFeed sends a transaction again, Sure does not make a second copy. Sure keeps one transaction for each Wallet transaction.

## Send previous transactions

A new destination also receives previous transactions, from the start date in **Settings** › **Sync** › **Initial History**. **Initial History** is **All** until you change it.

You can also send previous transactions with [Send History](/docs/send-history/):

1. In WalletFeed, tap **Destinations**.
2. Tap the Sure destination, for example **Sure · Apple Card**.
3. Tap **Send History**.
4. Tap **30 Days**, **90 Days**, **1 Year** or **All**.

WalletFeed shows **Sending History** with the number of transactions that it sent. To stop, tap **Send History** › **Stop Sending**.

## Change or remove the destination

To open the Sure destination, do these steps:

1. In WalletFeed, tap **Destinations**.
2. Tap the Sure destination.

For more information, refer to [Destinations](/docs/destinations/).

### Send only some transactions

1. Set **Filter** to on.
2. Use **Include**, **Minimum**, **Include Pending**, **Accounts**, **Categories** and **Exclude** to select the transactions.

To send only Apple Card transactions to this destination, select Apple Card in **Accounts**. To send Apple Cash to a different Sure account, add Sure again. In **Account**, select that account.

For more information, refer to [Choose what a destination receives](/docs/choose-what-to-send/).

### Replace the key

> **Note:** Sure does not accept two active keys with the same name. While the previous key is active, the new key must have a different name. If you click **Revoke** for the previous key first, you can use the same name.

1. Make a new Read/Write key in Sure, as in [Step 3](#step-3-make-a-read-write-api-key-in-sure).
2. In the Sure destination, tap **Replace Key**.
3. In **API Key**, paste the new key.
4. Tap **Replace**.

WalletFeed keeps the new key only if the key lets WalletFeed read the card account and write transactions into it.

### Stop or remove the destination

To stop the destination temporarily, set **Enabled** to off.

To remove the destination, do these steps:

1. In the Sure destination, tap **Delete**.
2. In the **Delete Sure · Apple Card?** message, tap **Delete**.
3. On your computer, open **Settings** › **API Keys** in Sure.
4. Click **Revoke** for the WalletFeed key.

   ![The API Keys list in Sure, with the Revoke button for the WalletFeed key highlighted.](https://walletfeed.app/guides/apple-card-to-sure/sure-revoke-key.webp)

5. Click **Confirm**.

   ![The Sure dialog about the WalletFeed key, with Confirm highlighted.](https://walletfeed.app/guides/apple-card-to-sure/sure-revoke-confirm.webp)

The transactions that WalletFeed sent stay in Sure. If you remove the destination, WalletFeed does not delete them.

## If there is a problem

### If Sure opens the dashboard after you sign in

You tapped **Sign In with Sure**. In Sure v0.7.6, Sure opens its dashboard after you sign in, and WalletFeed does not connect. The dashboard starts with "Welcome back" and your name.

1. Close the Sure page.
2. Tap **Use an API Key Instead**.
3. Make a key, as in [Step 3](#step-3-make-a-read-write-api-key-in-sure).
4. Do steps 7 to 11 of [Step 4](#step-4-add-sure-in-walletfeed).

### If WalletFeed does not show Account or Open API Keys

The address starts with `http://`. WalletFeed connects only to `https://` addresses, and it shows no message for an `http://` address.

1. Get an `https://` address for your Sure server, as in [Step 1](#step-1-get-an-https-address-for-your-sure-server).
2. In WalletFeed, type the `https://` address.

### If WalletFeed shows "This server doesn't support sign-in"

WalletFeed shows "This server doesn't support sign-in. Use an API key." when it cannot find Sign In with Sure at the address. Then WalletFeed opens the API key form.

1. Make sure that the address is the same address that you use to open Sure in a web browser.
2. If the address is correct, paste the key in **API Key**, as in [Step 4](#step-4-add-sure-in-walletfeed).

### If WalletFeed shows "Sure signs in at"

WalletFeed shows "Sure signs in at", then a different address, when Sure gives a different address for Sign In with Sure. Sure gets this address from `APP_URL` in its configuration. An API key does not use this address.

1. Tap **Use an API Key Instead**.
2. Paste the key in **API Key**, as in [Step 4](#step-4-add-sure-in-walletfeed).

### If WalletFeed shows "Create an account in Sure"

When Sure has no account that WalletFeed can write into, WalletFeed shows "Create an account in Sure for your card, then try again."

1. Add a card account in Sure, as in [Step 2](#step-2-add-a-card-account-in-sure).
2. In WalletFeed, delete the key in **API Key**.
3. Paste the key in **API Key** again.
4. Make sure that WalletFeed shows **Account**.

### If WalletFeed shows "This key is Read Only"

WalletFeed shows "This key is Read Only. Create a Read/Write key." when you paste a **Read Only** key. WalletFeed must have a Read/Write key to write transactions into Sure.

1. On your computer, open **Settings** › **API Keys** in Sure.
2. Click **Revoke** for the key.
3. Click **Confirm**.
4. Make a new Read/Write key, as in [Step 3](#step-3-make-a-read-write-api-key-in-sure).
5. In WalletFeed, paste the new key in **API Key**.

### If WalletFeed shows "Key rejected (HTTP 401)"

When Sure does not accept the key, WalletFeed shows "Key rejected (HTTP 401). Check it, or create a new one in Sure." The key is not correct or expired, or you clicked **Revoke** for it in Sure.

1. Make sure that you copied the key with **Copy API Key**, and not the `curl` line.
2. If you copied the `curl` line, do the steps in [If you closed the key page before you copied the key](#if-you-closed-the-key-page-before-you-copied-the-key).
3. If you copied the key with **Copy API Key**, make a new Read/Write key in Sure, as in [Step 3](#step-3-make-a-read-write-api-key-in-sure).
4. In WalletFeed, paste the new key in **API Key**.

### If Destinations shows "Authentication failed" for Sure

Sure does not accept the key when WalletFeed sends transactions. For example, you clicked **Revoke** for the key in Sure.

1. In WalletFeed, tap **Destinations**.

   ![The Destinations screen, where one destination shows Authentication failed.](https://walletfeed.app/guides/apple-card-to-sure/walletfeed-destinations-failure.webp)

2. Tap the Sure destination.
3. Replace the key, as in [Replace the key](#replace-the-key).

### If WalletFeed shows "Can't connect" or "Couldn't connect"

WalletFeed cannot connect to your Sure server. The server is off, or your iPhone can connect to it only on your home network.

1. Make sure that your Sure server operates.
2. Disconnect your iPhone from your home Wi-Fi.
3. On your iPhone, open the `https://` address of your Sure server in Safari.
4. If Sure does not open, get an `https://` address for all locations, as in [Step 1](#step-1-get-an-https-address-for-your-sure-server).
5. If you added Sure in WalletFeed, tap **Send Test** in the Sure destination.

The test writes a transaction of $4.20 with the name WalletFeed into the card account in Sure. You can delete it in Sure after the test.

### If WalletFeed shows "No Sure API at this address"

WalletFeed shows "No Sure API at this address, or the account is gone." when the address is not correct. WalletFeed also shows this message if you deleted the card account in Sure.

1. Make sure that the address is the same address that you use to open Sure in a web browser.
2. If you deleted the card account in Sure, add a new card account, as in [Step 2](#step-2-add-a-card-account-in-sure).
3. If you added a new card account, add Sure again in WalletFeed, as in [Step 4](#step-4-add-sure-in-walletfeed).

### If you closed the key page before you copied the key

Sure shows a key one time only. Sure also does not accept two active keys with the same name.

1. On your computer, open **Settings** › **API Keys** in Sure.
2. Click **Revoke** for the WalletFeed key.
3. Click **Confirm**.
4. Make a new key, as in [Step 3](#step-3-make-a-read-write-api-key-in-sure).
5. In WalletFeed, paste the new key in **API Key**.

### If the card balance in Sure is not correct

Sure calculates the balance from the balance in **Balance on date:** and from the transactions. After many transactions in a short time, Sure can show a balance without the last transaction.

1. In Sure, open the card account.
2. On the right side of the account name, click the icon with two circular arrows.

   ![The Apple Card account in Sure, with the icon that has two circular arrows highlighted.](https://walletfeed.app/guides/apple-card-to-sure/sure-refresh-account-balance.webp)
