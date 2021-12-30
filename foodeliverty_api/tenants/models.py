from django.db import models
from tenant_schemas.models import TenantMixin


class Client(TenantMixin):
    created_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100)
    on_trial = models.BooleanField()
    paid_until = models.DateField(null=True, blank=True)
    updated_at = models.DateTimeField(auto_now_add=True)
