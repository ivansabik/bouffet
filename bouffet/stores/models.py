import pytz
import uuid

from auditlog.registry import auditlog
from config_models.models import ConfigurationModel
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django_enumfield import enum
from phonenumber_field.modelfields import PhoneNumberField

TIMEZONES = tuple(zip(pytz.all_timezones, pytz.all_timezones))


class MenuCategory(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    updated_at = models.DateTimeField(auto_now_add=True)


auditlog.register(MenuCategory)


class MenuItemType(enum.Enum):
    MAIN = 0
    ADDITIONAL = 1
    ORDERWIDE = 2


class MenuItem(models.Model):
    available = models.BooleanField(default=True)
    category = models.ForeignKey(
        MenuCategory, on_delete=models.SET_NULL, blank=True, null=True
    )
    children_items = models.ManyToManyField("self", symmetrical=False, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    image_url = models.URLField(max_length=200, blank=True, null=True)
    is_required = models.BooleanField(blank=True, null=True)
    item_type = enum.EnumField(MenuItemType, default=MenuItemType.MAIN)
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    select_options = models.JSONField(blank=True, null=True)
    updated_at = models.DateTimeField(auto_now_add=True)


auditlog.register(MenuItem)


class OpeningHour(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    day = models.IntegerField(validators=[MaxValueValidator(31), MinValueValidator(1)])
    end_time = models.TimeField()
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    start_time = models.TimeField()
    updated_at = models.DateTimeField(auto_now_add=True)


auditlog.register(OpeningHour)


class Store(models.Model):
    appt_unit_suite_number_floor = models.CharField(
        max_length=10, blank=True, null=True
    )
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    currency = models.CharField(max_length=3)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    logo = models.URLField(max_length=200, blank=True, null=True)
    lat = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    lon = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    menu_items = models.ManyToManyField(MenuItem)
    name = models.CharField(max_length=50)
    opening_hours = models.ManyToManyField(OpeningHour)
    phone_number = PhoneNumberField()
    street_address = models.CharField(max_length=100)
    timezone = models.CharField(
        max_length=50, blank=True, null=True, choices=TIMEZONES, default="UTC"
    )
    updated_at = models.DateTimeField(auto_now_add=True, null=True)
    zip_code = models.CharField(max_length=10)


class StoreOrderingSettings(ConfigurationModel):
    delivery_fee = models.DecimalField(max_digits=6, decimal_places=2)
    delivery_radius_km = models.DecimalField(max_digits=6, decimal_places=2)
    fullfills_delivery = models.BooleanField(default=True)
    fullfills_pickup = models.BooleanField(default=True)


auditlog.register(Store)
