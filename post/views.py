from rest_framework import generics
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets

from django.urls import path
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from .models import Post, Comment, UserFollow, Bookmark
from .serializers import PostSerializer, CommentSerializer, UserFollowSerializer, BookmarkSerializer


class PostList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetails(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = PostSerializer


# THE COMMENTS SECTION
class CreateComment(generics.CreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        pk = self.kwargs.get('pk')
        post = Post.objects.get(pk=pk)
        serializer.save(post=post)


class CommentList(generics.ListAPIView):
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        pk = self.kwargs['pk']
        return Comment.objects.filter(post=pk)


class CommentDetails(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class LikeUnlike(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, post_id):
        user = request.user

        try:
            post = Post.objects.get(pk=post_id)
        except Post.DoesNotExist:
            return Response({"detail": "Post Not Found"}, status=status.HTTP_404_NOT_FOUND)

        if post.kudos.filter(pk=user.pk).exists():
            post.kudos.remove(user)
        else:
            post.kudos.add(user)

        serializer = PostSerializer(post)
        return Response(serializer.data)


class FollowUnfollow(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        try:
            user_to_click = User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return Response({'detail': "User Not Found"}, status=status.HTTP_404_NOT_FOUND)

        user_profile, created = UserFollow.objects.get_or_create(
            user=request.user)

        if user_profile.following.filter(pk=user_to_click.id).exists():
            user_profile.following.remove(user_to_click)

        else:
            user_profile.following.add(user_to_click)

        # fans_count = user_profile.total_user_followers_count()
        # fans_list = user_profile.user_followers_list()

        # response_data = {
        #     "fans_count": fans_count,
        #     "fans_list": fans_list,
        #     "user_profile": user_profile
        # }

        # print("response_data", fans_list)
        serializer = UserFollowSerializer(user_profile)
        print(serializer.data)
        return Response(serializer.data)


class BookmarkListView(generics.ListAPIView):
    queryset = Bookmark.objects.all()
    serializer_class = BookmarkSerializer
    permission_classes = [permissions.IsAuthenticated]


class BookmarkCreateView(generics.CreateAPIView):
    serializer_class = BookmarkSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Bookmark.objects.filter(bookmarked_by=self.request.user)

    def perform_create(self, serializer):
        user = self.request.user
        post = serializer.validated_data['post']
        existing_bookmark = Bookmark.objects.filter(
            bookmarked_by=user, post=post).first()
        print(existing_bookmark)
        if existing_bookmark:
            existing_bookmark.delete()
            response_data = {
                "detail": "Bookmark already exists for this post."}
            return Response(response_data,
                            status=status.HTTP_400_BAD_REQUEST)
        serializer.save(bookmarked_by=user)
        response_data = {"detail": "Bookmark created successfully"}
        return Response(response_data,
                        status=status.HTTP_201_CREATED)
