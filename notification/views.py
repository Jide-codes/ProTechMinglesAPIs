from django.shortcuts import render

from rest_framework import generics
from rest_framework import permissions
from rest_framework.response import Response
from .models import Notification
from .serializers import NotificatonSerializer

class NotificationView(generics.ListAPIView):
    serializer_class = NotificatonSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        user = self.request.user
        return Notification.objects.filter(user=user)
    
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        total_notifications = queryset.count()
        
        data = {
            'total_notifications': total_notifications,
            'notifications': serializer.data
        }
        
        return Response(data)