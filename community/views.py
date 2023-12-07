from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User

from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.exceptions import PermissionDenied

from .models import Community,CommunityPost, CommunityComment
from .serializers import CommunitySerializer, CommunityPostSerializer, CommunityCommentSerializer 


class CreateCommunityView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def post(self, request):
        serializer = CommunitySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(creator=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ListCommunitiesView(generics.ListAPIView):
    queryset = Community.objects.all()
    serializer_class = CommunitySerializer


class CommunityDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Community.objects.all()
    serializer_class = CommunitySerializer


class JoinCommunityView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def post(self, request, *args, **kwargs):
        community_id = kwargs.get('community_id')
        community = get_object_or_404(Community, pk=community_id)
        user = request.user
        
        if not community.members.filter(id=user.id).exists():
            community.members.add(user)
            return Response({'detail': 'Successfully joined the community.'}, status=status.HTTP_200_OK)
        
        serializer = CommunitySerializer(community)
        return Response(serializer.data, status=status.HTTP_200_OK)
   
    
class LeaveCommunityView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def post(self, request, *args, **kwargs):
        community_id = kwargs.get('community_id')
        community = get_object_or_404(Community, pk=community_id)
        user = request.user
        
        if community.members.filter(id=user.id).exists():
            community.members.remove(user)
            return Response({'detail': 'Successfully left the community.'}, status=status.HTTP_200_OK)
        
        serializer = CommunitySerializer(community)
        return Response( serializer.data, status=status.HTTP_200_OK)
            
            
"""This section is everything about Community Post"""    
        
class CreateCommunityPostView(APIView):
    """This class makes sure a post is created under a particular only if the user 
    creating the post is in the community"""
    
    permission_classes = [permissions.IsAuthenticated]
    
    def post(self, request, community_id):
        user = request.user
        community = get_object_or_404(Community, pk=community_id)
        
        if not community.members.filter(id=user.id).exists():
            return Response({ 'detail': 'User is not a member of the community'}, status=status.HTTP_403_FORBIDDEN)   
        post_data = {'community':community_id, 'author':user.id, 'body':request.data.get('body')}
        serializer = CommunityPostSerializer(data=post_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
class ListCommunityPost(generics.ListAPIView):
    serializer_class = CommunityPostSerializer
    
    def get_queryset(self):
        community_id = self.kwargs['community_id']
        return CommunityPost.objects.filter(community=community_id)
    
    
    

class DeleteCommunityPostView(APIView):
    """This class makes sure a post created under a particular community is deleted by only 
    the author of the post in the community"""
    
    permission_classes = [permissions.IsAuthenticated]
    
    def delete(self, request, post_id):
        user = request.user
        post = get_object_or_404(CommunityPost, pk=post_id)
        
        if user != post.author:
            return Response({'detail': 'You do not have permission to delete this post'})
        post.delete()
        return Response({'detail':'Post deleted successfully.'}, status=status.HTTP_204_NO_CONTENT)


"""This section is everything about Community Post Comments"""    

class CreateCommentView(generics.CreateAPIView):
    serializer_class = CommunityCommentSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def perform_create(self, serializer):
        user = self.request.user
        post_id = self.kwargs['post_id']
        post = get_object_or_404(CommunityPost, pk=post_id)
        community = post.community
        
        if not community.members.filter(id=user.id).exists():
            raise PermissionError("User is not a member of the community")
        serializer.save(author=user, post=post)


class ListCommentView(generics.ListAPIView):
    serializer_class = CommunityCommentSerializer
    
    def get_queryset(self):
        post_id = self.kwargs['post_id']
        return CommunityComment.objects.filter(post=post_id)


class UpdateCommentView(generics.UpdateAPIView):
    serializer_class = CommunityCommentSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        user = self.request.user
        comment_id = self.kwargs['pk']
        return CommunityComment.objects.filter(pk=comment_id)
    
    def perform_update(self, serializer):
        comment = self.get_object()
        
        if self.request.user != comment.author:
            raise PermissionDenied('You do not have permission to update this comment.')
        serializer.save()

class DeleteCommentView(generics.DestroyAPIView):
    serializer_class = CommunityCommentSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        comment_id = self.kwargs['pk']
        return CommunityComment.objects.filter(pk=comment_id)
    
    def perform_destroy(self, instance):
        if self.request.user != instance.author:
            raise PermissionDenied('You do not have permission to delete this comment.')
        instance.delete()
        
        
        
class LikeUnlike(APIView):
    
    def post(self, request, post_id):
        user = request.user
        post = get_object_or_404(CommunityPost, pk=post_id)

        if not post.community.members.filter(id=user.id).exists():
            return Response({'detail': 'User is not a member of the commumity'})
        
        if post.kudos.filter(pk=user.pk).exists():
            post.kudos.remove(user)
        else:
            post.kudos.add(user)

        serializer = CommunityPostSerializer(post)
        return Response(serializer.data)
    

        