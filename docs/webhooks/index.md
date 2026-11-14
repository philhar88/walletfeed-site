# Webhook format

A Webhook destination sends JSON to your HTTPS URL when transactions change. If Send Balances is on, it also sends the balances of the accounts when they change. Your iPhone sends each request directly to the URL. Each request has a [Standard Webhooks](https://www.standardwebhooks.com) signature, so you can use a Standard Webhooks library to examine it.

## Request

- A `POST` request to the URL of the destination, with `Content-Type: application/json` and `User-Agent: WalletFeed-Webhooks/1`.
- The `webhook-id`, `webhook-timestamp` and `webhook-signature` headers. The ID is `msg_` and 32 hexadecimal characters. The timestamp is the Unix time in seconds. To examine the signature, refer to [Signature](https://walletfeed.app/docs/webhooks/#verify).
- An `Authorization` header, if you typed a value in Authorization in WalletFeed. WalletFeed sends the value exactly as you typed it, for example `Bearer`, a space and a token.
- A maximum of 100 transactions, or 100 IDs to delete, in each request.
- A status code from 200 to 299 tells WalletFeed that you received the request. If WalletFeed cannot connect, or gets a different status code or no response in 30 seconds, it keeps the changes. It sends them again each time that it sends data, until you accept them.
- For history, WalletFeed waits between tries, from 1 minute to 1 day. It obeys `Retry-After` in a 429 or 503 response.

## Body

```
{
  "type": "transactions.changed",
  "timestamp": "2026-10-27T17:41:21Z",
  "data": {
    "upserted": [
      {
        "id": "8B3F0C2E-6D7A-4E8F-9C1B-2A4D5E6F7A8B",
        "accountID": "4F1E2D3C-…",
        "accountName": "Apple Card",
        "accountType": "liability",
        "date": "2026-10-27T15:02:11Z",
        "amount": 6.75,
        "currencyCode": "USD",
        "direction": "debit",
        "description": "Blue Bottle Coffee",
        "originalDescription": "BLUE BOTTLE COFFEE OAKLAND CA",
        "merchantName": "Blue Bottle Coffee",
        "merchantCategoryCode": 5814,
        "category": "dining",
        "status": "pending",
        "type": "pointOfSale"
      }
    ],
    "deletedIDs": []
  }
}
```

The top-level `type` is `transactions.changed`, also for history. `timestamp` is the date and time when WalletFeed sent the request, the same as `webhook-timestamp`.

Send Test in WalletFeed sends the same format with `"type": "walletfeed.test"` and one sample transaction. The sample has the ID `00000000-0000-0000-0000-000000000000`. Only the sample has the transaction type `purchase`. If Send Balances is on, `data` also has `balances`, with one sample balance for the account `sample-account`. Send Test always sends one request.

WalletFeed sends deletions in a different request from new and changed transactions. Thus, in each request, one of the two lists is empty. A deletion has only the ID:

```
{
  "type": "transactions.changed",
  "timestamp": "2026-10-28T09:12:40Z",
  "data": {
    "upserted": [],
    "deletedIDs": ["8B3F0C2E-6D7A-4E8F-9C1B-2A4D5E6F7A8B"]
  }
}
```

## Changes

- Upsert each transaction on `id`. WalletFeed sends a transaction again when it changes. For example, a pending charge comes again with the same `id` when it posts. Then its `status` changes from `pending` or `authorized` to `booked`, and `amount` is the posted amount.
- Delete the transactions that have their IDs in `deletedIDs`. The IDs come from declined and expired charges, and from transactions that Wallet removed. If Wallet gives a posted charge a new ID, the previous ID comes in `deletedIDs`.
- `deletedIDs` can also contain IDs that you did not receive. This occurs for a charge that Wallet declined before WalletFeed sent it. It also occurs for a transaction that the filter or start date of the destination did not include. If you do not have a transaction with that ID, do nothing.
- WalletFeed sends the history of the destination (previous transactions) in `transactions.changed` requests too, newest first. History has no deletions and no declined charges. Upsert on `id` for history too, because Send History can send a transaction again.
- WalletFeed can send the same changes two times or more. After an error, it can also send again the requests that you accepted before the error.
- WalletFeed makes `webhook-id` from the place of the changes in the Wallet history and the contents of `data`. When WalletFeed sends a request again, the request has the same `webhook-id`, so you can use it to find repeated requests. But when WalletFeed sends changes again, a request can also contain newer changes. Then the request has a different `webhook-id`.

## Fields

| Field | Value |
| --- | --- |
| `id` | The Wallet transaction ID (a UUID). It stays the same when the transaction changes. |
| `accountID`, `accountName` | The ID and name of the Wallet account, for example Apple Card. |
| `accountType` | `liability` (Apple Card) or `asset` (Apple Cash, Savings). |
| `date`, `postedDate` | ISO 8601 in UTC. A transaction has `postedDate` after the charge posts, if Wallet gives the date. |
| `amount` | A positive number. `direction` gives the sign. |
| `direction` | `debit` (purchases, fees) or `credit` (refunds, payments, deposits). |
| `currencyCode` | ISO 4217, for example `USD`. A purchase in a different currency also has `foreignAmount` and `foreignCurrencyCode`. |
| `description`, `originalDescription` | The clean description from Wallet, and the description from the card network. |
| `merchantName`, `merchantCategoryCode` | Only if Wallet has them. The category code is the MCC from the card network. |
| `category` | The WalletFeed category from the MCC (`other` without an MCC): `groceries`, `dining`, `transport`, `fuel`, `travel`, `shopping`, `entertainment`, `subscriptions`, `utilities`, `health`, `services`, `cash` or `other`. |
| `status` | The Wallet status: `authorized`, `pending`, `booked` or `memo`. WalletFeed sends a declined or expired charge (`rejected`) as a deletion. |
| `type` | The [FinanceKit transaction type](https://developer.apple.com/documentation/financekit/transactiontype): `adjustment`, `atm`, `billPayment`, `check`, `deposit`, `directDebit`, `directDeposit`, `dividend`, `fee`, `interest`, `loan`, `pointOfSale`, `refund`, `standingOrder`, `transfer`, `unknown` or `withdrawal`. Send Test uses `purchase`. |

If Wallet has no value for a field, the transaction does not include that field.

## Balances

Send Balances is off when you add a Webhook destination. You can set it to on when you add the destination, or after you add it, in the destination. Then WalletFeed also sends `balances.changed` requests:

```
{
  "type": "balances.changed",
  "timestamp": "2026-11-14T16:05:00Z",
  "data": {
    "balances": [
      {
        "accountID": "9A2B7C4D-…",
        "accountName": "Savings",
        "accountType": "asset",
        "currencyCode": "USD",
        "booked": {
          "amount": 5012.48,
          "asOfDate": "2026-11-14T08:00:00Z",
          "direction": "credit"
        },
        "available": {
          "amount": 5012.48,
          "asOfDate": "2026-11-14T08:00:00Z",
          "direction": "credit"
        }
      }
    ]
  }
}
```

- Upsert each balance on `accountID`. Each request has the latest balance of each account that the destination sends: Apple Card, Apple Cash and Savings, or only the accounts in Accounts of the filter. The other parts of the filter and the start date do not apply to balances.
- WalletFeed sends all the balances the first time that it sends data, when you set Send Balances to on, and after Send History. Then it sends all the balances again each time that a balance changes.
- WalletFeed sends the balances after the transactions that it sends at the same time, also if your server did not accept the transactions. A balance can include transactions that you did not receive yet.
- When WalletFeed is not open, iOS starts WalletFeed approximately 1 hour or less after a balance changes. If no balance changes, WalletFeed does not send balances.
- When WalletFeed sends the same balances again, the request has the same `webhook-id`. A 410 response stops the destination, as for transactions.

| Field | Value |
| --- | --- |
| `accountID`, `accountName` | The ID and name of the Wallet account, the same as in transactions. |
| `accountType` | `liability` (Apple Card) or `asset` (Apple Cash, Savings). |
| `currencyCode` | ISO 4217, for example `USD`. |
| `booked` | The balance from the posted transactions. Only if Wallet gives it. |
| `available` | The balance that also includes the pending transactions. Only if Wallet gives it. |
| `amount` | A positive number. `direction` gives the sign. |
| `direction` | The [FinanceKit credit or debit indicator](https://developer.apple.com/documentation/financekit/balance/creditdebitindicator) of the balance: `credit` or `debit`. A zero balance is `credit`. |
| `asOfDate` | The date and time when Wallet calculated the balance, in ISO 8601 and UTC. `booked` and `available` can have different times. |

For an asset, `credit` is a positive balance and `debit` is a negative balance. For a liability, `debit` is a balance that you owe and `credit` is a balance in your favor.

If Wallet has no value for `booked` or `available`, the balance does not include that field.

## Signature

To get the signing secret, tap Share Signing Secret in WalletFeed. It is on the Webhook screen when you add the destination, and in the destination. The secret is `whsec_` and base64 text. With a Standard Webhooks library:

```
// Node: npm install standardwebhooks
import { Webhook } from "standardwebhooks";
const payload = new Webhook(process.env.WALLETFEED_SECRET).verify(rawBody, request.headers);
```

```
# Python: pip install standardwebhooks
from standardwebhooks.webhooks import Webhook
payload = Webhook(os.environ["WALLETFEED_SECRET"]).verify(raw_body, request.headers)
```

Without a library:

1. Decode the base64 text after `whsec_`. The result is the key.
2. Calculate the HMAC-SHA256 of `{webhook-id}.{webhook-timestamp}.{raw body}` with the key.
3. Encode the result in base64.
4. Compare it with the text after `v1,` in `webhook-signature`. Use a constant-time comparison.
5. Do not accept the request if `webhook-timestamp` is more than 5 minutes before or after the current time.

Use the raw body exactly as you received it. Do the check before you parse the JSON.
