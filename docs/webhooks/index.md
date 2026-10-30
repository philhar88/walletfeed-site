# Webhook format

A Webhook destination sends JSON to your HTTPS URL when transactions change. Your iPhone sends each request directly to the URL. Each request has a [Standard Webhooks](https://www.standardwebhooks.com) signature, so you can use a Standard Webhooks library to examine it.

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

Send Test in WalletFeed sends the same format with `"type": "walletfeed.test"` and one sample transaction. The sample has the ID `00000000-0000-0000-0000-000000000000`. Only the sample has the transaction type `purchase`.

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
- WalletFeed makes `webhook-id` from the contents of `data`. Two requests with the same `data` have the same `webhook-id`, so you can use it to find repeated requests. But when WalletFeed sends changes again, a request can also contain newer changes. Then the request has a different `webhook-id`.

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
