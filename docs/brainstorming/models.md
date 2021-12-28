# Models

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
