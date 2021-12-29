from django.contrib import admin

from .models import Customer, DeliveryCourier, DeliveryTrackingPoint, Order, OrderItem

admin.site.register(Customer)
admin.site.register(DeliveryCourier)
admin.site.register(DeliveryTrackingPoint)
admin.site.register(Order)
admin.site.register(OrderItem)
