# Bouffet

## API Endpoints

- customers
- menu-categories
- menu-items
- opening-hours
- orders
- order-items
- stores
- users

## Local development

Start the dev server for local development:

```bash
docker-compose up
```

Create a superuser to login to the admin:

```bash
docker-compose run --rm web ./manage.py tenant_command createsuperuser --schema=pizzaurant
```

Create an auth token for this user which you can use to make requests to the API:

```
curl --location 'http://localhost:8000/api-token-auth/' \
--form 'username="admin"' \
--form 'password="admin"'
```

## Models

### orders

- Customer
- OrderStatus
- OrderFulfillmentType
- OrderItem
- Order

### stores

- MenuCategory
- MenuItemType
- MenuItem
- OpeningHour
- Store
