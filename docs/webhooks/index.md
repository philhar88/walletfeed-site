# Webhook format

A Webhook destination posts JSON to your HTTPS URL whenever transactions change. Requests come straight from your iPhone and are signed with [Standard Webhooks](https://www.standardwebhooks.com), so any Standard Webhooks library can verify them.

## Request

- `POST` to the URL you entered, with `Content-Type: application/json` and `User-Agent: WalletFeed-Webhooks/1`.
- `webhook-id`, `webhook-timestamp` and `webhook-signature` headers (see [Verify](https://walletfeed.app/docs/webhooks/#verify)).
- Your `Authorization` value, if you set one in WalletFeed.
- Up to 100 transactions per request. Any 2xx response counts as delivered; anything else is retried on the next sync.

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
        "type": "purchase"
      }
    ],
    "deletedIDs": []
  }
}
```

Send Test in WalletFeed posts the same shape with `"type": "walletfeed.test"` and one sample transaction.

## Handling changes

- Upsert on `id`. A pending charge (`status` `pending` or `authorized`) arrives again under the same `id` when it posts (`booked`), with its final amount.
- Delete the transactions listed in `deletedIDs`: declined and expired charges, and transactions removed from Wallet.
- Earlier transactions, sent as the destination's history, arrive the same way in `transactions.changed` requests, newest first, so upserting on `id` covers them too.
- To drop repeated deliveries, deduplicate on `webhook-id`. It's derived from the request's contents, so a retried request carries the same ID.

## Fields

| Field | Value |
| --- | --- |
| `id` | Wallet's transaction ID. Stable across updates. |
| `accountID`, `accountName` | The Wallet account, such as Apple Card. |
| `accountType` | `liability` (Apple Card) or `asset` (Apple Cash, Savings). |
| `date`, `postedDate` | ISO 8601. `postedDate` appears once the charge posts, when Wallet provides it. |
| `amount` | A positive number; `direction` gives the sign. |
| `direction` | `debit` (purchases, fees) or `credit` (refunds, payments, deposits). |
| `currencyCode` | ISO 4217, such as `USD`. `foreignAmount` and `foreignCurrencyCode` appear for purchases in another currency. |
| `description`, `originalDescription` | Wallet's cleaned-up description, and the raw one from the network. |
| `merchantName`, `merchantCategoryCode` | When Wallet knows them. The category code is the card network's MCC. |
| `category` | WalletFeed's category from the MCC: `groceries`, `dining`, `transport`, `fuel`, `travel`, `shopping`, `entertainment`, `subscriptions`, `utilities`, `health`, `services`, `cash` or `other`. |
| `status` | Wallet's status: `authorized`, `pending`, `booked` or `memo`. |
| `type` | Wallet's transaction type, such as `purchase`, `refund`, `payment` or `transfer`. |

Fields without a value are left out.

## Verify

Get the signing secret from Share Signing Secret in WalletFeed, on the setup screen or the destination's screen. It's `whsec_` followed by base64. With a Standard Webhooks library:

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

Or by hand:

1. Base64-decode the secret after `whsec_`.
2. Compute HMAC-SHA256 of `{webhook-id}.{webhook-timestamp}.{raw body}` with it, and base64-encode the result.
3. Compare it, in constant time, with the value after `v1,` in `webhook-signature`.
4. Reject timestamps more than five minutes from now.

Verify the raw body exactly as received, before parsing it.
