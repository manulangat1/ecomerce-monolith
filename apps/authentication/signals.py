from asyncio.log import logger
from django.dispatch import receiver 
from django.db.models.signals import post_save 
from django.contrib.auth import get_user_model
import logging
from apps.authentication.models import Profile
from monolithEcommerce.settings.base import AUTH_USER_MODEL
from django.dispatch import receiver
from .models import User


logger = logging.getLogger(__name__)

@receiver(post_save,sender=AUTH_USER_MODEL)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        logger.info(f" {instance}'s profiile created")

@receiver(post_save, sender=AUTH_USER_MODEL)
def save_user_profile(sender, instance, created, **kwargs):
    instance.profile.save()
    logger.info(f" {instance}'s profiile created")


