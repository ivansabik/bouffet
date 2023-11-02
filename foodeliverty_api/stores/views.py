from rest_framework import mixins, viewsets

from .models import Holiday, MenuCategory, MenuItem, OpeningHour, Store
from .permissions import IsUserOrReadOnly
from .serializers import (
    HolidaySerializer,
    MenuCategorySerializer,
    MenuItemSerializer,
    OpeningHourSerializer,
    StoreSerializer,
)


class StoreViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
):
    """
    Updates and retrieves Stores
    """

    queryset = Store.objects.all()
    serializer_class = StoreSerializer
    permission_classes = (IsUserOrReadOnly,)


class HolidayViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
):
    """
    Updates and retrieves Store Holidays
    """

    queryset = Holiday.objects.all()
    serializer_class = HolidaySerializer
    permission_classes = (IsUserOrReadOnly,)


class MenuCategoryViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
):
    """
    Updates and retrieves Menu Categories
    """

    queryset = MenuCategory.objects.all()
    serializer_class = MenuCategorySerializer
    permission_classes = (IsUserOrReadOnly,)


class MenuItemViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
):
    """
    Updates and retrieves Menu Items
    """

    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes = (IsUserOrReadOnly,)


class OpeningHourViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
):
    """
    Updates and retrieves Store Opening Hours
    """

    queryset = OpeningHour.objects.all()
    serializer_class = OpeningHourSerializer
    permission_classes = (IsUserOrReadOnly,)
