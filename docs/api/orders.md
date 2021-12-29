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
            "id": "d9913197-e6a4-48dd-85d0-9235004322fb",
            "delivery_tracking_points": null,
            "cancel_reason": "",
            "cancelled_at": null,
            "created_at": "2021-12-29T04:38:57+0000",
            "delivery_appt_suite_number": null,
            "delivery_city": "Mexico City",
            "delivery_contact_phone": "+525511111111",
            "delivery_fee": 20.0,
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
            "tip_amount": 5.0,
            "total_order_amount": 85.0,
            "updated_at": "2021-12-29T04:38:57+0000",
            "delivery_courier": "b0500cdd-4df9-4469-b0fb-ea49f9f7c8fd",
            "order_items": [
                "2f6b07af-ebe6-4904-9117-0d4c88e035f2"
            ]
        }
    ]
}
```

TODO: Add remaining methods (POST, PUT/PATCH, etc.)
