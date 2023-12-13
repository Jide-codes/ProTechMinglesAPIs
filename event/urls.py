from django.urls import path
from .views import *

urlpatterns = [
    path('', CreateEvent.as_view(), name='add_event'),
    path('event_list/', ListEvent.as_view(), name='event_list'),
    path('event_detail/<int:event_id>/', EventsDetailView.as_view(),),
]
