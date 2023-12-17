from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include("userprofiles.urls")),
    path('api-v1/', include("post.urls")),
    path('api-v1/', include('community.urls')),
    path('api-v1/', include('job.urls')),
    path('api-v1/', include("notification.urls")),
    path('api-v1/', include("event.urls"))
]
