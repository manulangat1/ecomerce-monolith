from django.urls import path 
from . import views
urlpatterns = [ 
    path('auth/register/', views.RegisterAPI.as_view(), name="registration_api"),
    path('auth/login/', views.LoginAPI.as_view(), name="login_api"),
    path('auth/me/', views.UserAPI.as_view(), name="get_logged_in_user_api"),
]