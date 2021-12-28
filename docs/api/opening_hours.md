# Opening Hours
Supports registering, viewing, and updating store open schedules.


## View opening hours

**Request**:

`GET` `/api/v1/opening-hours/`

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
            "id": "2872515a-cb6d-45bf-92d4-7163a3f86e30",
            "created_at": "2021-12-28T23:30:11+0000",
            "day": 1,
            "end_time": "19:00:00",
            "start_time": "10:00:00",
            "updated_at": "2021-12-28T23:30:11+0000"
        }
    ]
}
```

TODO: Add remaining methods (POST, PUT/PATCH, etc.)
