from django.urls import path
from .views import *

urlpatterns = [
    path('event_list/', EventView.as_view(), name='event_list'),
    path('', EventView.as_view(), name='add_event'),
]
