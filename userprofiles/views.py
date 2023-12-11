from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.permissions import *
from rest_framework.generics import GenericAPIView, ListAPIView, ListCreateAPIView
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.parsers import FormParser, MultiPartParser

from .serializers import *
from .models import *


class TestApi(GenericAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication, SessionAuthentication]

    def get(self, request, *args, **kwargs):
        print(request.user)
        return Response({
            "detail": "User is authenticted!"
        })


class SignUpView(GenericAPIView):
    def post(self, request):

        if request.data["password"] != request.data["confirm_password"]:
            return Response({
                "error": "Password and confirm password does not match"},
                status=status.HTTP_400_BAD_REQUEST)
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():

            user = serializer.save()
            token = Token.objects.get(user=user)
            return Response({'token': token.key}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserList(ListAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ProfileView(ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    parser_classes = (MultiPartParser, FormParser)

    def create(self, request, *args, **kwargs):
        user = request.data['user']
        picture = request.data['picture'] or None
        bio = request.data['bio'] or None
        user_profile = Profile.objects.filter(user=user)
        if user_profile:
            user_profile.update(picture=picture, bio=bio)
            return Response('Profile UPDATED successfully', status=status.HTTP_200_OK)
        Profile.objects.create(user_id=user, picture=picture, bio=bio)

        return Response('Profile created successfully', status=status.HTTP_200_OK)
