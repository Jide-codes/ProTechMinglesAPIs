from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import *
from rest_framework.response import Response
from rest_framework import status

from .models import *
from .serializers import *


class ListEvent(ListAPIView):
    serializer_class = EventSerializer

    def get_queryset(self):
        return Event.objects.filter(created_by_id=self.request.user.id)


class CreateEvent(CreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class EventsDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = EventSerializer
    lookup_url_kwarg = 'event_id'
    queryset = Event.objects.all()
