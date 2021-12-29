import uuid

from auditlog.registry import auditlog
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from taggit.managers import TaggableManager


class DeliveryCourier(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    custom_labels = TaggableManager(blank=True)
    first_name = models.CharField(max_length=50)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    last_name = models.CharField(max_length=50)
    phone_number = PhoneNumberField()
    updated_at = models.DateTimeField(auto_now_add=True)


auditlog.register(DeliveryCourier)


class DeliveryTrackingPoint(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    lat = models.DecimalField(max_digits=9, decimal_places=6)
    lon = models.DecimalField(max_digits=9, decimal_places=6)
    # order
    updated_at = models.DateTimeField(auto_now_add=True)


auditlog.register(DeliveryTrackingPoint)
