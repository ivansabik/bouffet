# Menu Item
Supports registering, viewing, and updating menu items.


## View meny categories

**Request**:

`GET` `/api/v1/menu-items/`

Parameters:

*Note:*

- All parameters are optional

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
            "id": "97b37633-4f6e-493b-b9b8-32829e93b5a6",
            "available": true,
            "cost": 100.0,
            "created_at": "2021-12-28T23:30:47+0000",
            "description": "Test item",
            "image_url": null,
            "item_type": 0,
            "name": "Test item",
            "price": 150.0,
            "sku": "TEST",
            "updated_at": "2021-12-28T23:30:47+0000",
            "category": "939d2e58-628d-47fe-876b-886f7c8e0e1a"
        }
    ]
}
```

TODO: Add remaining methods (POST, PUT/PATCH, etc.)
