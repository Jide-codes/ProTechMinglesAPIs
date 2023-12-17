from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend

from .models import Event
from .serializers import  EventSerializer


# class ListEvent(ListAPIView):
#     serializer_class = EventSerializer

#     def get_queryset(self):
#         return Event.objects.filter(created_by_id=self.request.user.id)


# class CreateEvent(CreateAPIView):
#     queryset = Event.objects.all()
#     serializer_class = EventSerializer


# class EventsDetailView(RetrieveUpdateDestroyAPIView):
#     serializer_class = EventSerializer
#     lookup_url_kwarg = 'event_id'
#     queryset = Event.objects.all()

class EventView(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filterset_fields = ('title', 'type', 'location')
    search_fields = ('title', 'type', 'location')
    
    
    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

# class ListEventType(ListAPIView):
#     queryset = EventType.objects.all()
#     serializer_class = EventTypeSerializer