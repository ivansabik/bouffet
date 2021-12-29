# Order Items
Supports registering, viewing, and updating order items.

## View order items

**Request**:

`GET` `/api/v1/order-items/`

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
            "id": "2f6b07af-ebe6-4904-9117-0d4c88e035f2",
            "created_at": "2021-12-29T04:37:41+0000",
            "updated_at": "2021-12-29T04:37:41+0000",
            "notes": "",
            "quantity": 1,
            "selected_option": null,
            "total_amount": 80.0,
            "menu_item": "37e2b0ba-ec39-42e9-b0e6-aa42bd37bb10",
            "children_items": []
        }
    ]
}
```

TODO: Add remaining methods (POST, PUT/PATCH, etc.)
