# Holidays
Supports registering, viewing, and updating holidays.

## View holidays

**Request**:

`GET` `/api/v1/holidays/`

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
            "id": "00327693-6e8f-4d73-82ac-26f2157851a1",
            "created_at": "2021-12-28T23:29:22+0000",
            "day": 31,
            "holiday_name": "New Year",
            "month": 12,
            "updated_at": "2021-12-28T23:29:22+0000"
        }
    ]
}
```

TODO: Add remaining methods (POST, PUT/PATCH, etc.)
