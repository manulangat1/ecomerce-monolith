from django.urls import path 
from . import views
urlpatterns = [ 
    path('register/', views.RegisterAPI.as_view(), name="registration_api"),
    path('login/', views.LoginAPI.as_view(), name="login_api"),
    path('me/', views.UserAPI.as_view(), name="get_logged_in_user_api"),
]