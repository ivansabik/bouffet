import uuid

from auditlog.registry import auditlog
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from phonenumber_field.modelfields import PhoneNumberField
from rest_framework.authtoken.models import Token


class User(AbstractUser, models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    email = models.EmailField(max_length=100)
    first_name = models.CharField(max_length=50)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    last_name = models.CharField(max_length=50)
    phone_number = PhoneNumberField()
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username

auditlog.register(User)

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
