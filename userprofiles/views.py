from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.permissions import *
from rest_framework import generics 
from rest_framework.views import APIView
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework import permissions
from rest_framework.exceptions import PermissionDenied
from rest_framework_simplejwt.tokens import RefreshToken



from .serializers import *
from .models import *


class TestApi(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication, SessionAuthentication]

    def get(self, request, *args, **kwargs):
        print(request.user)
        return Response({
            "detail": "User is authenticated!"
        })


class SignUpView(generics.GenericAPIView):
    def post(self, request):
         
        serializer = UserSerializer(data=request.data)
        
        data = {}
        
        if serializer.is_valid():
            account = serializer.save()
            profile=Profile.objects.create(user=account)
            WorkExperience.objects.create(profile=profile)
            Education.objects.create(profile=profile)
            
            data['response'] = "Registration Successful !"
            data['username'] = account.username
            data['email'] = account.email
        
        else:
            data = serializer.errors
            
        return Response(data)


        # if request.data["password"] != request.data["confirm_password"]:
        #     return Response({
        #         "error": "Password and confirm password does not match"},
        #         status=status.HTTP_400_BAD_REQUEST)
        # serializer = UserSerializer(data=request.data)

        # if serializer.is_valid():

        #     user = serializer.save()
        #     # token = Token.objects.get(user=user)
        #     refresh = RefreshToken.for_user(user=user)
        #     token =  {
        #                     'refresh': str(refresh),
        #                     'access': str(refresh.access_token),
        #                 }

        #     # profile=Profile.objects.create(user=user)
        #     # WorkExperience.objects.create(profile=profile)
        #     # Education.objects.create(profile=profile)
        #     # return Response(refresh, status=status.HTTP_201_CREATED)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LogOutView(APIView):
    def post(self, request):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)



class ProfilesView(generics.RetrieveUpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    
    
    def perform_update(self,  serializer):
        pk = self.kwargs['pk']
        profile = Profile.objects.get(id=pk)
        
        if profile.user != self.request.user:
           raise  PermissionDenied("You don't have permission to update this profile")
       
        serializer.save()
    
    
    
class WorkExperienceView(generics.RetrieveUpdateAPIView):
    queryset = WorkExperience.objects.all()
    serializer_class = WorkExperienceSerializer
    
    
    def perform_update(self,  serializer):
        pk = self.kwargs['pk']
        work_profile = WorkExperience.objects.get(id=pk)
        
        if work_profile.profile.user != self.request.user:
           raise  PermissionDenied("You don't have permission to update this profile")
       
        serializer.save()
        
        
class EducationView(generics.RetrieveUpdateAPIView):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer
    
    
    def perform_update(self,  serializer):
        pk = self.kwargs['pk']
        education_profile = WorkExperience.objects.get(id=pk)
        
        if education_profile.profile.user != self.request.user:
           raise  PermissionDenied("You don't have permission to update this profile")
       
        serializer.save()