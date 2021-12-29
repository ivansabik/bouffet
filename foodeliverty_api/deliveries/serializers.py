from rest_framework import serializers
from taggit.serializers import TaggitSerializer, TagListSerializerField

from .models import DeliveryCourier, DeliveryTrackingPoint


class DeliveryCourierSerializer(TaggitSerializer, serializers.ModelSerializer):
    custom_labels = TagListSerializerField()

    class Meta:
        model = DeliveryCourier
        fields = "__all__"


class DeliveryTrackingPointSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryTrackingPoint
        fields = "__all__"
