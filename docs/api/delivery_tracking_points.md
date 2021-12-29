# Delivery Tracking Points
Supports registering, viewing, and updating delivery tracking points.


## View delivery tracking points

**Request**:

`GET` `/api/v1/delivery-tracking-points/`

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
            "id": "f0269c70-8341-4f43-85e6-2641911ebb6d",
            "created_at": "2021-12-29T00:18:06+0000",
            "lat": 38.8951,
            "lon": 77.0364,
            "order": "e2412ff6-2ee0-4066-a441-63c6989aa902",
            "updated_at": "2021-12-29T00:18:06+0000"
        }
    ]
}
```

TODO: Add remaining methods (POST, PUT/PATCH, etc.)
