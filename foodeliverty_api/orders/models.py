import uuid

from auditlog.registry import auditlog
from django.db import models
from django_enumfield import enum
from phonenumber_field.modelfields import PhoneNumberField

from ..stores.models import MenuItem


class Customer(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    email = models.EmailField(max_length=100)
    email_verified = models.BooleanField(default=False)
    first_name = models.CharField(max_length=50)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    last_name = models.CharField(max_length=50)
    phone_number = PhoneNumberField()
    phone_number_verified = models.BooleanField(default=False)
    updated_at = models.DateTimeField(auto_now_add=True)


auditlog.register(Customer)


class OrderStatus(enum.Enum):
    CREATED = 0
    ACCEPTED = 1
    REJECTED = 2
    PAID = 3
    FAILED_PROCESSING_PAYMENT = 4
    STARTED_PREPARING = 5
    COMPLETED_FOR_FULFILLMENT = 6
    FULFILLED = 7
    CANCELLED = 8


class OrderFulfillmentType(enum.Enum):
    PICKUP = 0
    DELIVERY = 1


class OrderItem(models.Model):
    children_items = models.ManyToManyField("self", symmetrical=False, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    updated_at = models.DateTimeField(auto_now_add=True)
    menu_item = models.ForeignKey(MenuItem, on_delete=models.SET_NULL, blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    quantity = models.PositiveIntegerField(default=1)
    selected_option = models.CharField(max_length=50, blank=True, null=True)
    total_amount = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)


auditlog.register(OrderItem)


class Order(models.Model):
    cancel_reason = models.TextField(blank=True, null=True)
    cancelled_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    delivery_appt_suite_number = models.CharField(max_length=10, blank=True, null=True)
    delivery_city = models.CharField(max_length=100)
    delivery_contact_phone = PhoneNumberField()
    delivery_fee = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    delivery_lat = models.DecimalField(max_digits=9, decimal_places=6)
    delivery_lon = models.DecimalField(max_digits=9, decimal_places=6)
    delivery_notes = models.TextField(blank=True, null=True)
    delivery_street_address = models.CharField(max_length=100)
    delivery_zip_code = models.CharField(max_length=10)
    # device_browser
    # device_ip_address
    # device_os
    fulfilled_at = models.DateTimeField(blank=True, null=True)
    fulfillment_type = enum.EnumField(OrderFulfillmentType)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    order_items = models.ManyToManyField(OrderItem)
    paid_at = models.DateTimeField(blank=True, null=True)
    # payment
    ready_for_fulfillment_at = models.DateTimeField(blank=True, null=True)
    reject_reason = models.TextField(blank=True, null=True)
    rejected_at = models.DateTimeField(blank=True, null=True)
    share_url = models.URLField(max_length=200, blank=True, null=True)
    started_at = models.DateTimeField(blank=True, null=True)
    status = enum.EnumField(OrderStatus, default=OrderStatus.CREATED)
    tip_amount = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    total_order_amount = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now_add=True)


auditlog.register(Order)
