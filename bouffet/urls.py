from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path, re_path, reverse_lazy
from django.views.generic.base import RedirectView
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter

from .orders.views import (
    OrderItemViewSet,
    OrderViewSet,
)
from .stores.views import (
    MenuCategoryViewSet,
    MenuItemViewSet,
    OpeningHourViewSet,
    StoreViewSet,
)
from .users.views import UserCreateViewSet, UserViewSet

router = DefaultRouter()
router.register(r"menu-categories", MenuCategoryViewSet)
router.register(r"menu-items", MenuItemViewSet)
router.register(r"opening-hours", OpeningHourViewSet)
router.register(r"orders", OrderViewSet)
router.register(r"order-items", OrderItemViewSet)
router.register(r"stores", StoreViewSet)
router.register(r"users", UserCreateViewSet)
router.register(r"users", UserViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/", include(router.urls)),
    path("api-token-auth/", views.obtain_auth_token),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    # the 'api-root' from django rest-frameworks default router
    # http://www.django-rest-framework.org/api-guide/routers/#defaultrouter
    re_path(r"^$", RedirectView.as_view(url=reverse_lazy("api-root"), permanent=False)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
