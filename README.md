# foodeliverty

The REST API for foodeliverty.

Foodeliverty is an opinionated ordering and delivery app with first-class support for Machine Learning and Analytics.

Foodeliverty focuses on providing core services for orders and delivery operations and management, while relying on third-party integrations for doing other things.

Foodeliverty can be accesed via:
- Web App (for Admin, Delivery Courier and Customers)
- Mobile Native App (only for Delivery Courier and Customers)

See the [docs](./docs) section for development instructions.
# Prerequisites

- [Docker](https://docs.docker.com/docker-for-mac/install/)  

# Submodules and features

- Orders
  - Phone orders
- Delivery
- CMS
  - Create or update menu on Facebook page 
- Events (as in real-time event streaming and processing)

# Third-party integrations

## Cloud Phones

- CloudTalk
- Ring Central
- DialPad

## Auth

- Facebook
- Google
- Instagram

## Sales promotions

- Voucherify

## Payments

- Stripe
- PayPal

## Push Notifications

- OneSignal

#### Customer Verification

- Email (SMTP, Sendgrid)
- Phone Number (Twilio)

## Support and Live Chat

- Embed script (supports tawk.to, Zoho SalesIQ, elfsight and more free-tier)

## Outgoing Events

- HTTP Webhooks
- Custom Code (via AWS Lambda)

# Machine learning features

- Suggest items in the menu
- Predict time to complete order
- Predict sales
- Schedule delivery routes
- Transcribe and search through phone orders
