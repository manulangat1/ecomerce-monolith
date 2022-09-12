
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import translation
# Create your models here.

class User(AbstractUser):
    bio = models.TextField(verbose_name='user bio', null=True, blank=True)

    def __str__(self) -> str:
        return self.email

        
