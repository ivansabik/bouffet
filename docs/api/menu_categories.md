# Menu Category
Supports registering, viewing, and updating menu categories.


## View menu categories

**Request**:

`GET` `/api/v1/menu-categories/`

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
            "id": "939d2e58-628d-47fe-876b-886f7c8e0e1a",
            "created_at": "2021-12-28T23:29:45+0000",
            "description": "Appetizers",
            "image_url": null,
            "name": "Appetizers",
            "updated_at": "2021-12-28T23:29:45+0000"
        },
        {
            "id": "8c378e78-184e-4aab-840a-5bc2e84240b2",
            "created_at": "2021-12-28T23:29:56+0000",
            "description": "Soups",
            "image_url": null,
            "name": "Soups",
            "updated_at": "2021-12-28T23:29:56+0000"
        }
    ]
}
```

TODO: Add remaining methods (POST, PUT/PATCH, etc.)
