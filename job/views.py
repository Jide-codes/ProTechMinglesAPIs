from django.shortcuts import render

from .models import Job
from .serializers import JobSerializer

from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics

from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from .filters import JobFilter


class JobView(viewsets.ModelViewSet):
    serializer_class = JobSerializer
    queryset = Job.objects.all()
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filterset_fields = ('title', 'location', 'salary', 'type')
    search_fields = ('title', 'location', 'salary', 'type')  
    
    
    def perform_create(self, serializer):
        return serializer.save(creator= self.request.user)
    

    
    
    
    
# class Tagview(APIView):
#     def get(self, request):
#         tags = Tag.objects.all()
#         serializer = TagSerializer(tags, many=True)
#         return Response(serializer.data)
    
#     def post(self, request):
#         serializer = TagSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    