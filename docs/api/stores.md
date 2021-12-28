# Stores
Supports registering, viewing, and updating stores.


## View stores

**Request**:

`GET` `/stores/`

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
            "id": "87a6f496-57c1-4eca-af84-47ca2966617a",
            "custom_labels": [],
            "holidays": [
                {
                    "id": "00327693-6e8f-4d73-82ac-26f2157851a1",
                    "created_at": "2021-12-28T23:29:22+0000",
                    "day": 31,
                    "holiday_name": "New Year",
                    "month": 12,
                    "updated_at": "2021-12-28T23:29:22+0000"
                }
            ],
            "menu_items": [
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
            ],
            "opening_hours": [
                {
                    "id": "2872515a-cb6d-45bf-92d4-7163a3f86e30",
                    "created_at": "2021-12-28T23:30:11+0000",
                    "day": 1,
                    "end_time": "19:00:00",
                    "start_time": "10:00:00",
                    "updated_at": "2021-12-28T23:30:11+0000"
                }
            ],
            "city": "Mexico City",
            "country": "Mexico",
            "created_at": "2021-12-28T23:32:21+0000",
            "currency": "MXN",
            "delivery_fee": 65.0,
            "delivery_menu_url": null,
            "delivery_radius_km": 5.0,
            "fullfills_delivery": true,
            "fullfills_pickup": true,
            "image_url": null,
            "lat": 19.432608,
            "lon": -99.133209,
            "name": "Kebab Oso",
            "phone_number": "+525511111111",
            "street_address": "Avenida Constitucion",
            "street_number": 123,
            "timezone": null,
            "updated_at": "2021-12-28T23:32:21+0000",
            "zip_code": "01210"
        }
    ]
}
```

TODO: Add remaining methods (POST, PUT/PATCH, etc.)
