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
    "count": 2,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": "0236ccaa-819e-481e-967f-01cd9f7d6435",
            "created_at": "2021-12-29T04:04:04+0000",
            "updated_at": "2021-12-29T04:04:04+0000",
            "notes": "",
            "quantity": 1,
            "total_amount": null,
            "menu_item": "7df649a6-0777-406f-90ac-656e1f7744bc",
            "children_items": []
        },
        {
            "id": "225cb929-4fd8-4f48-af91-0ea92d1e8acc",
            "created_at": "2021-12-29T04:04:15+0000",
            "updated_at": "2021-12-29T04:04:15+0000",
            "notes": "",
            "quantity": 1,
            "total_amount": null,
            "menu_item": "ea02ef9d-74b5-47af-91fb-86f9c8628867",
            "children_items": [
                "0236ccaa-819e-481e-967f-01cd9f7d6435"
            ]
        }
    ]
}
```

TODO: Add remaining methods (POST, PUT/PATCH, etc.)
