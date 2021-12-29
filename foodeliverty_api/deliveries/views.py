from rest_framework import mixins, viewsets

from .models import DeliveryCourier, DeliveryTrackingPoint
from .permissions import IsUserOrReadOnly
from .serializers import DeliveryCourierSerializer, DeliveryTrackingPointSerializer


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
