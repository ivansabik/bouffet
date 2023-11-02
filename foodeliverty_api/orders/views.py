from rest_framework import mixins, viewsets

from .models import Customer, Order, OrderItem
from .permissions import IsUserOrReadOnly
from .serializers import (
    CustomerSerializer,
    OrderItemSerializer,
    OrderSerializer,
)


class CustomerViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
):
    """
    Updates and retrieves Customers
    """

    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = (IsUserOrReadOnly,)


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
