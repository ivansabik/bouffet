from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path, re_path, reverse_lazy
from django.views.generic.base import RedirectView
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter

from .deliveries.views import DeliveryCourierViewSet, DeliveryTrackingPointViewSet
from .stores.views import HolidayViewSet, MenuCategoryViewSet, MenuItemViewSet, OpeningHourViewSet, StoreViewSet
from .users.views import UserCreateViewSet, UserViewSet

router = DefaultRouter()
router.register(r"delivery-couriers", DeliveryCourierViewSet)
router.register(r"delivery-tracking-points", DeliveryTrackingPointViewSet)
router.register(r"holidays", HolidayViewSet)
router.register(r"menu-categories", MenuCategoryViewSet)
router.register(r"menu-items", MenuItemViewSet)
router.register(r"opening-hours", OpeningHourViewSet)
router.register(r"stores", StoreViewSet)
router.register(r"users", UserViewSet)
router.register(r"users", UserCreateViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/", include(router.urls)),
    path("api-token-auth/", views.obtain_auth_token),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    # the 'api-root' from django rest-frameworks default router
    # http://www.django-rest-framework.org/api-guide/routers/#defaultrouter
    re_path(r"^$", RedirectView.as_view(url=reverse_lazy("api-root"), permanent=False)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
