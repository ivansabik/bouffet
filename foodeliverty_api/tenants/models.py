import uuid

from django.db import models
from tenant_schemas.models import TenantMixin


class Client(TenantMixin):
    auto_create_schema = True
    created_at = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    on_trial = models.BooleanField()
    paid_until = models.DateField(null=True, blank=True)
    updated_at = models.DateTimeField(auto_now_add=True)
