from rest_framework import mixins, viewsets

from .models import Customer, DeliveryCourier, DeliveryTrackingPoint, Order
from .permissions import IsUserOrReadOnly
from .serializers import CustomerSerializer, DeliveryCourierSerializer, DeliveryTrackingPointSerializer, OrderSerializer


class CustomerViewSet(
    mixins.CreateModelMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet
):
    """
    Updates and retrieves Customers
    """

    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = (IsUserOrReadOnly,)


class DeliveryCourierViewSet(
    mixins.CreateModelMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet
):
    """
    Updates and retrieves Delivery Courier Contacts
    """

    queryset = DeliveryCourier.objects.all()
    serializer_class = DeliveryCourierSerializer
    permission_classes = (IsUserOrReadOnly,)


class DeliveryTrackingPointViewSet(
    mixins.CreateModelMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet
):
    """
    Updates and retrieves Delivery Tracking Points
    """

    queryset = DeliveryTrackingPoint.objects.all()
    serializer_class = DeliveryTrackingPointSerializer
    permission_classes = (IsUserOrReadOnly,)


class OrderViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    Updates and retrieves Orders
    """

    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = (IsUserOrReadOnly,)
