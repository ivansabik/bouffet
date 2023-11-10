from rest_framework import serializers

from .models import MenuCategory, MenuItem, OpeningHour, Store


class MenuCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuCategory
        fields = "__all__"


class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = "__all__"


class OpeningHourSerializer(serializers.ModelSerializer):
    class Meta:
        model = OpeningHour
        fields = "__all__"


class StoreSerializer(serializers.ModelSerializer):
    menu_items = MenuItemSerializer(many=True)
    opening_hours = OpeningHourSerializer(many=True)

    class Meta:
        model = Store
        read_only_fields = (
            "created_at",
            "fulfillment_types",
            "id",
            "holidays",
            "menu_items",
            "opening_hours",
            "updated_at",
            "valid_until",
        )
        fields = "__all__"
