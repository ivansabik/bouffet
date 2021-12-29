# Customers
Supports registering, viewing, and updating customers.

## View customers

**Request**:

`GET` `/api/v1/customers/`

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
            "id": "c54faf63-7d90-402b-a697-d2fd466b0cd9",
            "custom_labels": [],
            "created_at": "2021-12-29T03:27:32+0000",
            "email": "spoomoni@poyobrands.com",
            "email_verified": false,
            "first_name": "Aquiles",
            "last_name": "Bailo",
            "phone_number": "+525511111112",
            "phone_number_verified": false,
            "updated_at": "2021-12-29T03:27:32+0000"
        }
    ]
}
```

TODO: Add remaining methods (POST, PUT/PATCH, etc.)
