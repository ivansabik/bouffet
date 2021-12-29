# Orders
Supports registering, viewing, and updating orders.

## View orders

**Request**:

`GET` `/api/v1/orders/`

Parameters:

*Note:*

- **[Authorization Protected](authentication.md)**

**Response**:

Content-Type application/json
HTTP 200 OK

```json
{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": "497dae06-66e3-486f-9c55-8594f08cfb1b",
            "custom_labels": [],
            "delivery_tracking_points": null,
            "cancel_reason": "",
            "cancelled_at": null,
            "created_at": "2021-12-29T03:35:34+0000",
            "delivery_appt_suite_number": null,
            "delivery_city": "Mexico City",
            "delivery_contact_phone": "+525511111111",
            "delivery_fee": null,
            "delivery_lat": 38.8951,
            "delivery_lon": -77.0364,
            "delivery_notes": "",
            "delivery_street_address": "Avenida Constitucion 123",
            "delivery_zip_code": "01210",
            "fulfilled_at": null,
            "fulfillment_type": 0,
            "paid_at": null,
            "ready_for_fulfillment_at": null,
            "reject_reason": "",
            "rejected_at": null,
            "share_url": null,
            "started_at": null,
            "status": 0,
            "tip_amount": null,
            "total_order_amount": null,
            "updated_at": "2021-12-29T03:35:34+0000",
            "delivery_courier": null,
            "order_items": []
        }
    ]
}
```

TODO: Add remaining methods (POST, PUT/PATCH, etc.)
