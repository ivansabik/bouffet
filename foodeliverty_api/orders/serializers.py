from rest_framework import serializers
from taggit.serializers import TaggitSerializer, TagListSerializerField

from .models import Customer, DeliveryCourier, DeliveryTrackingPoint, Order, OrderItem


class CustomerSerializer(TaggitSerializer, serializers.ModelSerializer):
    custom_labels = TagListSerializerField()

    class Meta:
        model = Customer
        fields = "__all__"


class DeliveryCourierSerializer(TaggitSerializer, serializers.ModelSerializer):
    custom_labels = TagListSerializerField()

    class Meta:
        model = DeliveryCourier
        fields = "__all__"


class DeliveryTrackingPointSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryTrackingPoint
        fields = "__all__"


class OrderSerializer(serializers.ModelSerializer):
    custom_labels = TagListSerializerField()
    delivery_tracking_points = DeliveryTrackingPointSerializer(many=True)

    class Meta:
        model = Order
        fields = "__all__"


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = "__all__"
