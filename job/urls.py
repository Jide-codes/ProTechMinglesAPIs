from django.urls import path, include

from .views import JobView

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('jobs', JobView, basename='job')
# router.register('tags', TagView, basename='tags')

urlpatterns = [
    
    path('', include(router.urls)),
    # path('jobs/', JobView.as_view(), name='jobs')
    
]
