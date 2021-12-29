# Delivery Couriers
Supports registering, viewing, and updating delivery couriers.

## View delivery couriers

**Request**:

`GET` `/api/v1/delivery-couriers/`

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
            "id": "b50ed36a-8a99-4c90-b084-ce006fea1f73",
            "created_at": "2021-12-29T00:13:17+0000",
            "first_name": "Johnny",
            "last_name": "Ze",
            "phone_number": "+525511111111",
            "updated_at": "2021-12-29T00:13:17+0000"
        }
    ]
}
```

TODO: Add remaining methods (POST, PUT/PATCH, etc.)
