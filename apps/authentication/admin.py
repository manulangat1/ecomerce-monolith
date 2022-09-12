from django.contrib import admin
from apps.authentication.models import User, Profile
# Register your models here.

admin.site.register(User)
admin.site.register(Profile)

