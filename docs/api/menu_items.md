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
    "count": 2,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": "b9f52ec2-4cde-4686-879c-4ff96429a156",
            "available": true,
            "cost": null,
            "created_at": "2021-12-29T04:35:10+0000",
            "description": "",
            "image_url": null,
            "item_type": 1,
            "name": "Extra cheese",
            "price": 15.0,
            "select_options": null,
            "sku": null,
            "updated_at": "2021-12-29T04:35:10+0000",
            "category": null,
            "children_items": []
        },
        {
            "id": "37e2b0ba-ec39-42e9-b0e6-aa42bd37bb10",
            "available": true,
            "cost": null,
            "created_at": "2021-12-29T04:35:19+0000",
            "description": "",
            "image_url": null,
            "item_type": 0,
            "name": "Mac And Cheese",
            "price": 80.0,
            "select_options": null,
            "sku": null,
            "updated_at": "2021-12-29T04:35:19+0000",
            "category": "221d46f2-7d25-41f4-a8aa-0dfe789445eb",
            "children_items": [
                "b9f52ec2-4cde-4686-879c-4ff96429a156"
            ]
        }
    ]
}
```

TODO: Add remaining methods (POST, PUT/PATCH, etc.)
