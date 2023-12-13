from django.urls import path
from .views import *

from rest_framework.authtoken.views import obtain_auth_token
urlpatterns = [
    path("", TestApi.as_view(), name  = "test"),
    path("signup", SignUpView.as_view(), name = "signup"),
    path("login/", obtain_auth_token, name="login"),
    path("logout/", LogOutView.as_view(), name="logout")
]