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
    "count": 2,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": "52b0cd69-1e55-4be7-abdd-39ca375ac976",
            "created_at": "2021-12-29T04:39:24+0000",
            "lat": 38.8951,
            "lon": -77.0364,
            "updated_at": "2021-12-29T04:39:24+0000",
            "order": "d9913197-e6a4-48dd-85d0-9235004322fb"
        },
        {
            "id": "26acc209-d99a-429b-8530-1cdef5672e0f",
            "created_at": "2021-12-29T04:39:48+0000",
            "lat": 15.23456,
            "lon": -30.6789,
            "updated_at": "2021-12-29T04:39:48+0000",
            "order": "d9913197-e6a4-48dd-85d0-9235004322fb"
        }
    ]
}
```

TODO: Add remaining methods (POST, PUT/PATCH, etc.)
