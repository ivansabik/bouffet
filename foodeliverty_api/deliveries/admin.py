from django.contrib import admin

from .models import DeliveryCourier, DeliveryTrackingPoint

admin.site.register(DeliveryCourier)
admin.site.register(DeliveryTrackingPoint)
