import uuid

from auditlog.registry import auditlog
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django_enumfield import enum
from phonenumber_field.modelfields import PhoneNumberField


class Holiday(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    day = models.IntegerField(validators=[MaxValueValidator(31), MinValueValidator(1)])
    holiday_name = models.CharField(max_length=50)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    month = models.IntegerField(validators=[MaxValueValidator(12), MinValueValidator(1)])
    updated_at = models.DateTimeField(auto_now_add=True)


auditlog.register(Holiday)


class MenuCategory(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True, null=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    image_url = models.URLField(max_length=200, blank=True, null=True)
    name = models.CharField(max_length=50)
    updated_at = models.DateTimeField(auto_now_add=True)


auditlog.register(MenuCategory)


class MenuItemType(enum.Enum):
    MAIN = 0
    ADDITIONAL = 1
    ORDERWIDE = 2


class MenuItem(models.Model):
    available = models.BooleanField(default=True)
    category = models.ForeignKey(MenuCategory, on_delete=models.SET_NULL, blank=True, null=True)
    children_items = models.ManyToManyField("self", symmetrical=False, blank=True)
    cost = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True, null=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    image_url = models.URLField(max_length=200, blank=True, null=True)
    item_type = enum.EnumField(MenuItemType, default=MenuItemType.MAIN)
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    select_options = models.JSONField(blank=True, null=True)
    sku = models.CharField(max_length=100, blank=True, null=True)
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
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    currency = models.CharField(max_length=3)
    delivery_fee = models.DecimalField(max_digits=6, decimal_places=2)
    delivery_menu_url = models.URLField(max_length=200, blank=True, null=True)
    delivery_radius_km = models.DecimalField(max_digits=6, decimal_places=2)
    fullfills_delivery = models.BooleanField(default=True)
    fullfills_pickup = models.BooleanField(default=True)
    holidays = models.ManyToManyField(Holiday)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    image_url = models.URLField(max_length=200, blank=True, null=True)
    lat = models.DecimalField(max_digits=9, decimal_places=6)
    lon = models.DecimalField(max_digits=9, decimal_places=6)
    menu_items = models.ManyToManyField(MenuItem)
    name = models.CharField(max_length=20)
    opening_hours = models.ManyToManyField(OpeningHour)
    phone_number = PhoneNumberField()
    street_address = models.CharField(max_length=100)
    street_number = models.IntegerField()
    timezone = models.CharField(max_length=50, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True)
    zip_code = models.CharField(max_length=10)


auditlog.register(Store)
