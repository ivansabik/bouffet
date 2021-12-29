import uuid

from auditlog.registry import auditlog
from django.db import models
from django_enumfield import enum
from phonenumber_field.modelfields import PhoneNumberField
from taggit.managers import TaggableManager

from ..stores.models import MenuItem


class Customer(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    custom_labels = TaggableManager(blank=True)
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


class DeliveryCourier(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    custom_labels = TaggableManager(blank=True)
    first_name = models.CharField(max_length=50)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    last_name = models.CharField(max_length=50)
    phone_number = PhoneNumberField()
    updated_at = models.DateTimeField(auto_now_add=True)


auditlog.register(DeliveryCourier)


class Order(models.Model):
    cancel_reason = models.TextField()
    cancelled_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    custom_labels = TaggableManager(blank=True)
    delivery_appt_suite_number = models.CharField(max_length=10)
    delivery_city = models.CharField(max_length=100)
    delivery_contact_phone = PhoneNumberField()
    delivery_courier = models.ForeignKey(DeliveryCourier, on_delete=models.SET_NULL, null=True)
    delivery_fee = models.DecimalField(max_digits=6, decimal_places=2)
    delivery_lat = models.DecimalField(max_digits=9, decimal_places=6)
    delivery_lon = models.DecimalField(max_digits=9, decimal_places=6)
    delivery_notes = models.TextField()
    delivery_street_address = models.CharField(max_length=100)
    delivery_zip_code = models.CharField(max_length=10)
    # device_browser
    # device_ip_address
    # device_os
    fulfilled_at = models.DateTimeField(blank=True, null=True)
    fulfillment_type = enum.EnumField(OrderFulfillmentType)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    menu_items = models.ManyToManyField(MenuItem)
    notes = models.TextField()
    paid_at = models.DateTimeField(blank=True, null=True)
    # payment
    ready_for_fulfillment_at = models.DateTimeField(blank=True, null=True)
    reject_reason = models.TextField()
    rejected_at = models.DateTimeField(blank=True, null=True)
    share_url = models.URLField(max_length=200, blank=True, null=True)
    started_at = models.DateTimeField(blank=True, null=True)
    status = enum.EnumField(OrderStatus, default=OrderStatus.CREATED)
    tip_amount = models.DecimalField(max_digits=6, decimal_places=2)
    total_order_amount = models.DecimalField(max_digits=6, decimal_places=2)
    updated_at = models.DateTimeField(auto_now_add=True)

    @property
    def delivery_tracking_points(self):
        DeliveryTrackingPoint.objects.filter(order=self.id)


auditlog.register(Order)


class DeliveryTrackingPoint(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    lat = models.DecimalField(max_digits=9, decimal_places=6)
    lon = models.DecimalField(max_digits=9, decimal_places=6)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    updated_at = models.DateTimeField(auto_now_add=True)


auditlog.register(DeliveryTrackingPoint)
