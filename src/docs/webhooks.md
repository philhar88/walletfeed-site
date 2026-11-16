+++
title = "Webhook format"
nav_title = "Webhook format"
description = "The JSON events that a WalletFeed webhook sends, the switch for each event type, and how to examine the Standard Webhooks signature."
order = 900
related = ["guides/apple-card-to-webhook", "docs/destinations", "docs/choose-what-to-send"]
updated = 2026-11-16
+++

A Webhook destination sends one JSON event to your HTTPS URL for each change in Wallet. In WalletFeed, a switch for each event type controls which events go to the URL. Your iPhone sends each request directly to the URL. Each request has a [Standard Webhooks](https://www.standardwebhooks.com) signature, so you can use a Standard Webhooks library to examine it.

This page is for format version 2, which WalletFeed 1.2 sends. Each body has `"version": 2`.

## Switches

A Webhook destination has two sections of switches. Each switch sends one event type. WalletFeed does not send an event type if its switch is off.

| Section | Switch | Event type | When you add the destination |
| --- | --- | --- | --- |
| **Transactions** | **New** | `transaction.created` | On |
| **Transactions** | **Changed** | `transaction.updated` | On |
| **Transactions** | **Removed** | `transaction.deleted` | On |
| **Transactions** | **History** | `transaction.backfilled` | On |
| **Accounts** | **Balances** | `balance.updated` | Off |
| **Accounts** | **Account Details** | `account.updated` | Off |
| **Accounts** | **Added** | `account.added` | Off |
| **Accounts** | **Removed** | `account.removed` | Off |

- For a full copy of your transactions, set **New**, **Changed** and **Removed** to on.
- When you set **Balances** or **Account Details** to on, WalletFeed sends the data of each account at that time. The other switches send only the changes that occur after you set them to on.
- One switch does not change a different switch.
- You cannot add a Webhook destination with all switches off. If you set all switches to off in the destination, WalletFeed sends nothing until you set a switch to on again.
- **Balances**, **Account Details**, **Added** and **Removed** under **Accounts** use only **Accounts** of the filter. The other parts of the filter and the start date do not apply to them.

To change the switches, open WalletFeed, tap **Destinations**, then tap the Webhook destination.

## Request

- A `POST` request to the URL of the destination, with `Content-Type: application/json` and `User-Agent: WalletFeed-Webhooks/2`.
- One event in each request.
- The `webhook-id`, `webhook-timestamp` and `webhook-signature` headers. The ID is `evt_` and 32 hexadecimal characters, the same as the `id` in the body. The timestamp is the Unix time in seconds. To examine the signature, refer to [Signature](#signature).
- A `WalletFeed-Event` header with the event type, for example `transaction.created`. The signature does not include this header. After you examine the signature, use the `type` in the body.
- An `Authorization` header, if you typed a value in **Authorization** in WalletFeed. WalletFeed sends the value exactly as you typed it, for example `Bearer`, a space and a token.

## Body

Each body has the same six fields. `data` is different for each event type.

```
{
  "id": "evt_3f9a0c7e1b2d4a5f8e6c9b0a1d2e3f4a",
  "type": "transaction.created",
  "version": 2,
  "timestamp": "2026-11-16T17:41:20.512Z",
  "livemode": true,
  "data": {}
}
```

| Field | Value |
| --- | --- |
| `id` | `evt_` and 32 hexadecimal characters. It is the same as `webhook-id`. Use it to find events that you received before. |
| `type` | The event type. Each type has one format for `data`. |
| `version` | `2`. |
| `timestamp` | The date and time when your iPhone made the event, in UTC with milliseconds. |
| `livemode` | `false` for **Send Test** and for **Sample Data**. `true` for data from Wallet. |
| `data` | The object of the event. Refer to the sections for each event type. |

These rules apply to all events:

- Each field in the tables is always in `data`. If Wallet has no value for a field, the value is `null`. If an object such as `credit` or `booked` is `null`, its fields are not in `data`.
- The names of the fields use snake case, for example `account_id`.
- An amount is a JSON number in the currency of the account, for example `-6.75`. WalletFeed writes the exact amount from Wallet, without the zeros at the end. Thus $8,000.00 is `8000`. Compare amounts as numbers, not as text.
- An amount is positive for money that goes to you or that you have. It is negative for money that goes from you or that you owe. A purchase is `-6.75`, and a refund is `6.75`. Savings with $5,012.48 is `5012.48`, and an Apple Card balance of $1,243.18 is `-1243.18`.
- `direction` is the FinanceKit credit or debit indicator, `credit` or `debit`. It always agrees with the sign. An amount of zero has `credit`.
- A date and time is in UTC, in ISO 8601, for example `2026-11-16T15:02:11Z`. A calendar day, such as a due date, is `YYYY-MM-DD` with no time.
- An ID from Wallet is a UUID in capital letters. It does not change when the object changes.
- Each event type can get new fields in version 2. Some values can also get new values: the transaction `type`, `category`, `wallet_status`, `reason`, `source` and `trigger`. Ignore a field or a value that you do not know.
- WalletFeed can add new event types in version 2, each with a new switch that is off. A status code from 200 to 299 is correct for an event type that you do not use.

## `transaction.created` and `transaction.updated`

`transaction.created` is a transaction that Wallet has for the first time. `transaction.updated` is a change to a transaction, for example when a pending charge posts. The two types have the same `data`, one transaction:

```
{
  "id": "evt_a2315d2ca67d6bb3120751a1466c8bfa",
  "type": "transaction.updated",
  "version": 2,
  "timestamp": "2026-11-16T17:41:20.512Z",
  "livemode": true,
  "data": {
    "id": "8B3F0C2E-6D7A-4E8F-9C1B-2A4D5E6F7A8B",
    "account_id": "4F1E2D3C-5B6A-4798-8A9B-0C1D2E3F4A5B",
    "account_name": "Apple Card",
    "account_type": "liability",
    "amount": -6.75,
    "direction": "debit",
    "currency": "USD",
    "status": "posted",
    "wallet_status": "booked",
    "type": "pointOfSale",
    "description": "Blue Bottle Coffee",
    "original_description": "BLUE BOTTLE COFFEE OAKLAND CA",
    "merchant_name": "Blue Bottle Coffee",
    "merchant_category_code": "5814",
    "category": "dining",
    "transacted_at": "2026-11-16T15:02:11Z",
    "posted_at": "2026-11-17T08:00:00Z",
    "foreign_amount": null,
    "foreign_currency": null,
    "exchange_rate": null
  }
}
```

When Wallet first has a charge, it is often pending:

```
{
  "id": "evt_cd0452538e320e8554053afb13548af6",
  "type": "transaction.created",
  "version": 2,
  "timestamp": "2026-11-16T17:41:20.512Z",
  "livemode": true,
  "data": {
    "id": "8B3F0C2E-6D7A-4E8F-9C1B-2A4D5E6F7A8B",
    "account_id": "4F1E2D3C-5B6A-4798-8A9B-0C1D2E3F4A5B",
    "account_name": "Apple Card",
    "account_type": "liability",
    "amount": -6.75,
    "direction": "debit",
    "currency": "USD",
    "status": "pending",
    "wallet_status": "pending",
    "type": "pointOfSale",
    "description": "Blue Bottle Coffee",
    "original_description": "BLUE BOTTLE COFFEE OAKLAND CA",
    "merchant_name": "Blue Bottle Coffee",
    "merchant_category_code": "5814",
    "category": "dining",
    "transacted_at": "2026-11-16T15:02:11Z",
    "posted_at": null,
    "foreign_amount": null,
    "foreign_currency": null,
    "exchange_rate": null
  }
}
```

| Field | Value |
| --- | --- |
| `id` | The Wallet transaction ID. It stays the same when the charge posts. Upsert on this ID. |
| `account_id`, `account_name` | The ID and name of the Wallet account, for example Apple Card. |
| `account_type` | `liability` (Apple Card) or `asset` (Apple Cash, Savings). |
| `amount` | The amount, with the sign. Purchases, fees and money that you send are negative. Refunds, card payments and deposits are positive. |
| `direction` | `debit` or `credit`. |
| `currency` | ISO 4217, for example `USD`. |
| `status` | `pending` or `posted`. `pending` is the Wallet status `authorized`, `pending` or `memo`. `posted` is `booked`. |
| `wallet_status` | The Wallet status: `authorized`, `pending`, `memo` or `booked`. A declined or expired charge comes as `transaction.deleted`. |
| `type` | The [FinanceKit transaction type](https://developer.apple.com/documentation/financekit/transactiontype): `adjustment`, `atm`, `billPayment`, `check`, `deposit`, `directDebit`, `directDeposit`, `dividend`, `fee`, `interest`, `loan`, `pointOfSale`, `refund`, `standingOrder`, `transfer`, `unknown` or `withdrawal`. |
| `description`, `original_description` | The clean description from Wallet, and the description from the card network. |
| `merchant_name` | The merchant name, if Wallet has it. |
| `merchant_category_code` | The four-digit MCC from the card network, as text, for example `"0742"`. |
| `category` | The WalletFeed category from the MCC: `groceries`, `dining`, `transport`, `fuel`, `travel`, `shopping`, `entertainment`, `subscriptions`, `utilities`, `health`, `services`, `cash` or `other`. |
| `transacted_at` | The date and time of the transaction. |
| `posted_at` | The date and time when the charge posted, if Wallet gives it. |
| `foreign_amount`, `foreign_currency` | For a purchase in a different currency, the amount in that currency, with the same sign as `amount`, and its ISO 4217 code. |
| `exchange_rate` | The exchange rate from Wallet, for a purchase in a different currency. |

Upsert the two types in the same way. `transaction.updated` can have an ID that you did not receive. For example, the filter, the start date or the **New** switch can stop the first version of a transaction.

## `transaction.deleted`

```
{
  "id": "evt_7d75d06ee48b157a8b8ba40508fb8bdc",
  "type": "transaction.deleted",
  "version": 2,
  "timestamp": "2026-11-16T17:41:20.512Z",
  "livemode": true,
  "data": {
    "id": "8B3F0C2E-6D7A-4E8F-9C1B-2A4D5E6F7A8B",
    "account_id": "4F1E2D3C-5B6A-4798-8A9B-0C1D2E3F4A5B",
    "reason": "rejected"
  }
}
```

| Field | Value |
| --- | --- |
| `id` | The ID of the transaction to delete. If you do not have a transaction with that ID, do nothing. |
| `account_id` | The ID of the Wallet account. |
| `reason` | `rejected`: Wallet declined the charge or it expired. `removed`: Wallet deleted the transaction. |

If Wallet gives a posted charge a new ID, the previous ID comes with `"reason": "removed"`. The new ID comes as `transaction.created`.

## `transaction.backfilled`

`transaction.backfilled` sends a page of transactions, with a maximum of 100 in each page.

```
{
  "id": "evt_99b5ba7fed7d89a8c02fc135bf273601",
  "type": "transaction.backfilled",
  "version": 2,
  "timestamp": "2026-11-16T17:41:20.512Z",
  "livemode": true,
  "data": {
    "source": "history",
    "run": "2D6C1B8E-0F4A-4E3B-9C2D-7A1B0C9D8E7F",
    "account_id": null,
    "has_more": false,
    "transactions": [
      {
        "id": "1C2D3E4F-5A6B-4C7D-8E9F-0A1B2C3D4E5F",
        "account_id": "4F1E2D3C-5B6A-4798-8A9B-0C1D2E3F4A5B",
        "account_name": "Apple Card",
        "account_type": "liability",
        "amount": -214.6,
        "direction": "debit",
        "currency": "USD",
        "status": "posted",
        "wallet_status": "booked",
        "type": "pointOfSale",
        "description": "Delta",
        "original_description": "DELTA AIR LINES",
        "merchant_name": "Delta",
        "merchant_category_code": "3058",
        "category": "travel",
        "transacted_at": "2026-03-02T19:20:44Z",
        "posted_at": "2026-03-03T08:00:00Z",
        "foreign_amount": -198,
        "foreign_currency": "EUR",
        "exchange_rate": 1.0838
      }
    ]
  }
}
```

| Field | Value |
| --- | --- |
| `source` | `history`: transactions from **Initial History** or **Send History**. `catch_up`: more than 25 changes at one time, refer to [Delivery](#delivery). |
| `run` | A UUID for one history, or for one group of `catch_up` pages. A new **Send History** has a new `run`. |
| `account_id` | `null`. |
| `has_more` | `false` on the last page of the `run`. The last page of a history can have no transactions. |
| `transactions` | From 0 to 100 transactions, with the same fields as `transaction.updated`. History is newest first. |

Upsert each transaction on `id`, the same as `transaction.updated`. History has no deletions and no declined charges.

## `balance.updated`

`balance.updated` sends the balance of one account. When a balance changes, WalletFeed sends a `balance.updated` for each account of the destination.

```
{
  "id": "evt_f61181c09d3af3779d3c23bf801dcc5b",
  "type": "balance.updated",
  "version": 2,
  "timestamp": "2026-11-16T17:41:20.512Z",
  "livemode": true,
  "data": {
    "account_id": "4F1E2D3C-5B6A-4798-8A9B-0C1D2E3F4A5B",
    "account_name": "Apple Card",
    "account_type": "liability",
    "currency": "USD",
    "booked": {
      "amount": -1243.18,
      "direction": "debit",
      "as_of": "2026-11-16T08:00:00Z"
    },
    "available": {
      "amount": 6750.07,
      "direction": "credit",
      "as_of": "2026-11-16T17:41:20Z"
    },
    "credit": {
      "limit": 8000,
      "available_credit": 6750.07,
      "minimum_payment": 35,
      "payment_due_date": "2026-12-31",
      "overdue_amount": null
    },
    "trigger": "change",
    "snapshot": {
      "id": "B67B656F-F03D-89D6-91E1-7D386CBF7D31",
      "index": 1,
      "count": 2
    }
  }
}
```

| Field | Value |
| --- | --- |
| `account_id`, `account_name`, `account_type`, `currency` | The same as in `transaction.updated`. Upsert the balance on `account_id`. |
| `booked` | The latest balance from the posted transactions. |
| `available` | The latest available figure from Wallet. For Apple Cash and Savings, it is the balance with pending transactions. For Apple Card, it is the available credit. |
| `amount` | The figure from Wallet, with the sign of its indicator. In `booked`, an Apple Card balance that you owe is negative. Savings is positive. |
| `direction` | The [FinanceKit credit or debit indicator](https://developer.apple.com/documentation/financekit/balance/creditdebitindicator) of the figure, as Wallet gives it. |
| `as_of` | The date and time when Wallet calculated that balance. `booked` and `available` can have different times. |
| `credit` | The credit details of Apple Card, the same as in `account.updated`. `null` for Apple Cash and Savings, and for a card with no credit details. |
| `credit.available_credit` | The credit that you can use on Apple Card, `0` or more: the `available` amount without the sign. Without `available`, `credit.limit` minus the `booked` balance. |
| `trigger` | `change`: a balance changed. `snapshot`: all balances, at the first send, when you set **Balances** to on, and after **Send History**. |
| `snapshot` | The group of `balance.updated` events that WalletFeed sent at the same time: `id`, `index` (from 1) and `count`. |

- For the Apple Card balance that Wallet shows, with pending transactions, subtract `credit.available_credit` from `credit.limit`. In the example, 8000 minus 6750.07 is 1249.93. `booked` is the balance of the posted transactions.
- The sign of the Apple Card `available` amount agrees with the indicator from Wallet. Apple does not document this indicator. Use `credit.available_credit`, which is always `0` or more.
- If `booked` or `available` is `null`, keep the balance that you have.
- Apply a figure only if its `as_of` is the same as or newer than the `as_of` that you have. Apply `booked` and `available` separately.
- After you have all the events of a `snapshot` `id` (`count` events), you can remove the accounts that were not in it.
- WalletFeed sends balances also when no transaction changed, for example when Savings interest posts.
- A balance can include transactions that you did not receive yet. Do not calculate a balance from transactions.

## `account.updated` and `account.added`

`account.updated` sends the details of one account when Wallet tells WalletFeed that the account changed. The `account.added` event sends the same details for an account that is new in the destination. This occurs when you give WalletFeed access to the account in Wallet. It also occurs when you add the account to **Accounts** of the filter.

```
{
  "id": "evt_fb94176bfdfa147629e7e83966109053",
  "type": "account.updated",
  "version": 2,
  "timestamp": "2026-11-16T17:41:20.512Z",
  "livemode": true,
  "data": {
    "id": "4F1E2D3C-5B6A-4798-8A9B-0C1D2E3F4A5B",
    "name": "Apple Card",
    "description": "Apple Card",
    "institution_name": "Apple",
    "account_type": "liability",
    "currency": "USD",
    "opening_date": "2023-04-02",
    "credit": {
      "limit": 8000,
      "available_credit": null,
      "minimum_payment": 35,
      "payment_due_date": "2026-12-31",
      "overdue_amount": null
    },
    "trigger": "change",
    "snapshot": null
  }
}
```

| Field | Value |
| --- | --- |
| `id` | The Wallet account ID, the same as `account_id` in other events. Upsert on this ID. |
| `name`, `description` | The name and the description of the account in Wallet. |
| `institution_name` | The bank of the account. |
| `account_type`, `currency` | The same as in `transaction.updated`. |
| `opening_date` | The day when the account opened, `YYYY-MM-DD`. |
| `credit` | The credit details of Apple Card. `null` for Apple Cash and Savings, and for a card with no credit details. |
| `credit.limit` | The credit limit. |
| `credit.available_credit` | Always `null` in an account event. For the available credit, set **Balances** to on and use `balance.updated`. |
| `credit.minimum_payment` | The minimum payment for the next due date. |
| `credit.payment_due_date` | The due date of the next payment, `YYYY-MM-DD`. |
| `credit.overdue_amount` | The amount that is overdue. `null` or `0` tells you that no amount is overdue. |
| `trigger` | `change`, or `snapshot` when WalletFeed sends all accounts on purpose: when you set **Account Details** to on, and after **Send History**. `account.added` always has `change`. |
| `snapshot` | For `snapshot`, the same as in `balance.updated`. `null` for `change`. |

`account.updated` does not tell you which field changed. To find a new due date, compare `credit.payment_due_date` with the due date that you have. WalletFeed does not keep a copy of the details.

An account event does not contain a balance. For balances, set **Balances** to on.

This is an `account.added` for Savings:

```
{
  "id": "evt_743166131f13a232932915bcdc63170d",
  "type": "account.added",
  "version": 2,
  "timestamp": "2026-11-16T17:41:20.512Z",
  "livemode": true,
  "data": {
    "id": "7C3B2A19-0F8E-4D7C-9B6A-5F4E3D2C1B0A",
    "name": "Savings",
    "description": "Savings",
    "institution_name": "Apple",
    "account_type": "asset",
    "currency": "USD",
    "opening_date": null,
    "credit": null,
    "trigger": "change",
    "snapshot": null
  }
}
```

## `account.removed`

`account.removed` tells you that WalletFeed does not send more events for an account.

```
{
  "id": "evt_0ccdfdb62f4ec5848c0c1d1b1e2ac18d",
  "type": "account.removed",
  "version": 2,
  "timestamp": "2026-11-16T17:41:20.512Z",
  "livemode": true,
  "data": {
    "id": "9A2B7C4D-1E3F-4A5B-8C7D-6E5F4A3B2C1D",
    "name": null,
    "reason": "wallet"
  }
}
```

| Field | Value |
| --- | --- |
| `id` | The Wallet account ID. |
| `name` | The name of the account if `reason` is `filter`. `null` if `reason` is `wallet`, because WalletFeed does not keep names. |
| `reason` | `wallet`: the account is not in Wallet, or WalletFeed has no access to it. `filter`: you removed it from **Accounts** of the filter. |

WalletFeed does not send `transaction.deleted` for the transactions of a removed account. You can keep them or delete them.

## Delivery

- A status code from 200 to 299 tells WalletFeed that you received the event.
- If WalletFeed gets 429 or a status code from 500 to 599, it sends the event again 3 times, after approximately 1, 2 and 4 seconds. Each try has a new `webhook-timestamp` and a new signature, with the same `webhook-id` and body.
- If WalletFeed cannot connect, or gets a different status code or no response in 30 seconds, it keeps the change. It sends the event again the next time that it sends data.
- If WalletFeed sends an event again with the same data from the same place in Wallet, the event has the same `id`. The body `timestamp` can be newer. A changed object gets a new `id`.
- If Wallet has more changes before the next send, WalletFeed can send events that you received before with a new `id`. Upsert on the ID of the object, so that a repeated event does not cause a problem.
- Each snapshot has a new `snapshot` `id` and new event IDs. This is also true after **Send History** when no data changed in Wallet. Thus, if you remove your data and keep the IDs that you received, you get all accounts again.
- After an error, WalletFeed can send again the events that you accepted before the error, with the same `id`.
- WalletFeed sends one event at a time to a destination. It stops at the first event that your server does not accept, and sends that event again at the next send.
- Transactions, accounts and balances stop separately. If your server does not accept a transaction event, account and balance events still go.
- Thus a status code that is not correct for one event stops the events of that kind after it. Answer with a status code from 200 to 299 for each event that you do not use, or set its switch to off.
- If WalletFeed gets 410 when it sends data, it stops the destination. Then **Enabled** is off in the destination.
- For history, WalletFeed waits between tries, from 1 minute to 1 day. It obeys `Retry-After` in a 429 or 503 response.
- When WalletFeed is open, it sends a change in seconds. When WalletFeed is not open, iOS starts WalletFeed approximately 1 hour or less after a change in Wallet.

If one send has 25 changed transactions or less, each goes as `transaction.created` or `transaction.updated`. If it has more than 25, for example after the iPhone was off for a long time, they go as `transaction.backfilled` pages with `"source": "catch_up"`. If **History** is off, they go as `transaction.created` and `transaction.updated` events. Deleted transactions always go as `transaction.deleted` events.

In one send, the order is `account.added`, then the transaction events, then `account.updated`, then `balance.updated`, then `account.removed`. Do not use the order of events across types. A balance can come before the transactions that it includes.

## Rules for your server

1. Examine the signature with the raw body, before you parse the JSON.
2. Save the event, for example in a table with `id` as the key.
3. Answer with a status code from 200 to 299 in 30 seconds. Do this only after you save the event. WalletFeed has no copy of an event that you accepted, so it cannot send it again.
4. If you have an event with the same `id`, do not apply it again. Answer with a status code from 200 to 299.
5. Upsert each object on its ID: `id` for transactions and accounts, `account_id` for balances.
6. Apply a balance figure only if its `as_of` is the same as or newer than your `as_of`.
7. If `livemode` is `false`, do not write the event to your real data.

This Node example uses the `standardwebhooks` package:

```
// Examine, save, then answer. WalletFeed cannot send an event again after you accept it.
let evt;
try {
  evt = new Webhook(process.env.WALLETFEED_SECRET).verify(rawBody, req.headers);
} catch { return res.status(400).end(); }
if (!evt.livemode) return res.status(200).end();
await db.transaction(async (tx) => {
  if (!(await tx.markSeen(evt.id))) return;
  switch (evt.type) {
    case "balance.updated":        await upsertBalance(tx, evt.data); break;
    case "account.added":
    case "account.updated":        await upsertAccount(tx, evt.data); break;
    case "account.removed":        await markRemoved(tx, evt.data.id); break;
    case "transaction.created":
    case "transaction.updated":    await upsertTxn(tx, evt.data); break;
    case "transaction.backfilled": for (const t of evt.data.transactions) await upsertTxn(tx, t); break;
    case "transaction.deleted":    await deleteTxn(tx, evt.data.id); break;
    default: break;
  }
});
res.status(200).end();
```

## Signature

To get the signing secret, tap **Share Signing Secret** in WalletFeed. It is on the Webhook screen when you add the destination, and in the destination. The secret is `whsec_` and base64 text. With a Standard Webhooks library:

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

Use the raw body exactly as you received it. Do the check before you parse the JSON. Use a tolerance of 5 minutes for the timestamp, not 0.

## Receive events in n8n

n8n has no Standard Webhooks node. This workflow examines the signature in a Code node.

1. Add a **Webhook** node with **HTTP Method** `POST`.
2. In the node options, set **Raw Body** to on, and set **Respond** to **When Last Node Finishes**.
3. Add a **Code** node after the **Webhook** node.
4. Paste the code below in the **Code** node. Then replace `PASTE_YOUR_SIGNING_SECRET` with your signing secret.
5. Add a **Switch** node on `{{ $json.type }}`, with one output for each event type that you use.

```
const crypto = require("crypto");
const secret = "PASTE_YOUR_SIGNING_SECRET";
const headers = $input.first().json.headers;
const raw = (await this.helpers.getBinaryDataBuffer(0, "data")).toString("utf8");
const key = Buffer.from(secret.replace("whsec_", ""), "base64");
const signed = `${headers["webhook-id"]}.${headers["webhook-timestamp"]}.${raw}`;
const expected = crypto.createHmac("sha256", key).update(signed).digest("base64");
const ok = headers["webhook-signature"].split(" ").some((s) => s === `v1,${expected}`);
const age = Math.abs(Date.now() / 1000 - Number(headers["webhook-timestamp"]));
if (!ok || age > 300) throw new Error("Bad signature");
return [{ json: JSON.parse(raw) }];
```

If the signature is not correct, n8n answers 500, and WalletFeed sends the event again. Make sure that the secret in the code is correct.

> **Note:** A self-hosted n8n can stop the `crypto` module. Then set `NODE_FUNCTION_ALLOW_BUILTIN=crypto` in the n8n environment.

For an alert when the due date changes, set **Account Details** to on. Then keep `credit.payment_due_date` for each account in an n8n Data Table. Send the alert only if the new date is different from the date in the table. Keep the workflow short, so that n8n answers in 30 seconds.

## Send Test

**Send Test** sends one event with sample data and `"livemode": false`. If two or more switches are on, **Send Test** shows a menu. The menu has one item for each switch that is on: **New Transaction**, **Changed Transaction**, **Removed Transaction**, **History**, **Balance**, **Account Details**, **Added Account** and **Removed Account**. Each tap sends one request.

- The sample account is `00000000-0000-0000-0000-000000000001`, "Sample Card", a liability in USD.
- The sample transaction is `00000000-0000-0000-0000-000000000000`, "WalletFeed test transaction", `-4.2`, with the type `pointOfSale`. It is pending in `transaction.created`, and posted in `transaction.updated` and `transaction.backfilled`.
- The sample balance has `booked` `-42`, `available` `953.8` and `credit.available_credit` `953.8`, with `"trigger": "snapshot"` and a `snapshot` of 1 event. The sample card balance is `1000` minus `953.8`, which is `46.2`.
- The sample account details have a limit of `1000`, a minimum payment of `25` and a due date 12 days after the test.
- Each test has a new `id`, so your server does not find it as a repeated event.
- If **Send Test** gets 410, WalletFeed shows the error and does not stop the destination.

## Changes from the earlier format

WalletFeed 1.2 sends format version 2 only. Format version 1 had `User-Agent: WalletFeed-Webhooks/1` and no `version` in the body. If your server uses format version 1, change it before you update WalletFeed.

- `transactions.changed` is gone. Each change is now one event with its own type: `transaction.created`, `transaction.updated` or `transaction.deleted`. History is `transaction.backfilled`.
- `data.upserted` (a list of transactions) and `data.deletedIDs` are gone. Each transaction is now its own event, and `data` has the transaction. A deleted transaction is a `transaction.deleted` event, and `data.id` is its ID.
- Each request has one event. It does not have a list of transactions, except `transaction.backfilled`.
- The body has `id`, `type`, `version`, `timestamp` and `livemode`, and `data` has the object. `webhook-id` starts with `evt_`, not `msg_`.
- The names of the fields use snake case, for example `account_id`, not `accountID`.
- An amount has a sign, and `direction` agrees with it. In format version 1, an amount was always positive.
- Each field is always in `data`, with `null` if Wallet has no value. In format version 1, a field with no value was not in the body.
- `merchant_category_code` is text with four digits. `exchange_rate` is new.
- A Webhook destination that you added before WalletFeed 1.2 has **New**, **Changed**, **Removed** and **History** on after the update. The switches under **Accounts** are off.
- `walletfeed.test` is gone. **Send Test** sends the event type that you select, with `"livemode": false`.
