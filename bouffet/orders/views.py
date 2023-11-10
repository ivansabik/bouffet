from rest_framework import mixins, viewsets

from .models import Order, OrderItem
from .permissions import IsUserOrReadOnly
from .serializers import (
    OrderItemSerializer,
    OrderSerializer,
)


class OrderViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
):
    """
    Updates and retrieves Orders
    """

    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = (IsUserOrReadOnly,)


class OrderItemViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
):
    """
    Updates and retrieves Orders Items
    """

    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    permission_classes = (IsUserOrReadOnly,)
