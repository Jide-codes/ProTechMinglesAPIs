from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.permissions import *
from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView
from django.contrib.auth.models import User
from .serializers import *
from rest_framework import status

# Create your views here.

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
                "error":"Password and confirm password does not match"},
                status=status.HTTP_400_BAD_REQUEST)
        serializer = UserSerializer(data=request.data)
        
        if serializer.is_valid():
            
            user = serializer.save()
            token = Token.objects.get(user=user)
            return Response({'token': token.key}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LogOutView(APIView):
    def post(self, request):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)