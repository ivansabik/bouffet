# Models

## Store

- city
- country
- created_at
- currency
- custom_labels
- delivery_fee (audited field)
- delivery_menu_url
- delivery_radius_km
- fulfillment_types
- holiday_schedules
- id
- image_url
- lat
- lon
- menu_categories
- name
- open_schedules
- phone_numbers
- street_address
- timezone
- updated_at
- valid_until
- zip_code

## Store Schedule Open

- created_at
- day
- end_time
- id
- start_time
- updated_at

## Store Schedule Holiday

- created_at
- day
- holiday_name
- id
- month
- updated_at

## Menu Item

- category
- price (audited field)
- custom_labels
- description
- id
- image_url
- name
- sku
- stock_status (audited field)

## Menu Category

- id
- name

Two out of the box: Extra (for order-wide items like Bag, Forks, Napkins etc.) and Additional (Cheese, Bacon, Pickles, Onion, etc.)

## Order

- cancel_reason
- cancelled_at
- courier_contact
- created_at
- custom_labels
- delivery_address
- delivery_contact_phone
- delivery_fee
- device_browser
- device_ip_address
- device_os
- extra_items
- fulfilled_at
- fulfillment_type
- id
- items
- notes
- paid_at
- payment
- ready_for_fulfillment_at
- reject_reason
- rejected_at
- share_url
- started_at
- status (audited field)
- tip_amount
- total_order_amount
- updated_at

## Courier Contact

- created_at
- custom_labels
- first_name
- id
- last_name
- phone_number (audited field)
- updated_at

## Customer

- anonymous_id
- created_at
- custom_labels
- email (audited field)
- fb_url
- first_name
- id
- instagram_url
- last_name
- phone_number (audited field)
- delivery_addresses
- updated_at

## Address

- appt_suite_number (audited field)
- city (audited field)
- custom_labels
- customer
- id
- lat (audited field)
- lon (audited field)
- notes (audited field)
- street_address (audited field)
- zip_code (audited field)

## Payment

- amount
- custom_labels
- id
- payment_method
- vendor_response
## Payment Method

- id
- name
- vendor_name

## Payments Ledger

- custom_labels
- id
- created_at
- transaction_type
- amount
- order
- transaction_description
