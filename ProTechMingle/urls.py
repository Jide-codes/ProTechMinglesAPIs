from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-v1/login/', include('rest_framework.urls')),
    path("accounts/", include("userprofiles.urls")),
    path("api-v1/", include("post.urls")),
]
