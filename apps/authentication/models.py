
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import translation

#local imports 
from apps.common.models import TimeStampedModel
# Create your models here.

class User(AbstractUser):
    bio = models.TextField(verbose_name='user bio', null=True, blank=True)

    def __str__(self) -> str:
        return self.email


class Profile(TimeStampedModel):
    user = models.OneToOneField(User, related_name="profile", on_delete=models.CASCADE)
    city = models.CharField(verbose_name='City', max_length=255, null=True, blank=True)
    state = models.CharField(verbose_name='state', max_length=255, null=True, blank=True)
    country = models.CharField(verbose_name='country', max_length=255, null=True, blank=True)
    address = models.CharField(verbose_name='City', max_length=255, null=True, blank=True)

    def __str__(self) -> str:
        return self.user.username