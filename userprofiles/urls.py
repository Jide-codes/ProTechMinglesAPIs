from django.urls import path
from .views import *

urlpatterns = [
    # 首页
    path("", TestApi.as_view(), name="test"),
    path("signup/", SignUpView.as_view(), name="signup"),
    path('users/', UserList.as_view()),
    path('profile/', ProfileView.as_view()),
]
