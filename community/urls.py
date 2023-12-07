from django.urls import path, include
from .views import (CreateCommunityView, CreateCommunityPostView,  
                               ListCommunitiesView,JoinCommunityView, LeaveCommunityView,
                               CommunityDetailView, ListCommunityPost, DeleteCommunityPostView,
                               CreateCommentView, ListCommentView, UpdateCommentView,
                               DeleteCommentView, LikeUnlike)



urlpatterns = [
    path('create_community/', CreateCommunityView.as_view(), name='create-community'),
    path('communities/', ListCommunitiesView.as_view(), name='communities'),
    path('community_detail/<int:pk>/', CommunityDetailView.as_view(), name='community-detail'),
    
    # JOIN AND LEAVE COMMUNITY
    path('join_community/<int:community_id>/', JoinCommunityView.as_view(), name='join-community'),
    path('leave_community/<int:community_id>/', LeaveCommunityView.as_view(), name='leave-community'),
    
    # COMMUNITY POST
    path("community/<int:community_id>/create-post/", CreateCommunityPostView.as_view(), name="create-community-post"),
    path("community/<int:community_id>/posts/", ListCommunityPost.as_view(), name='community-posts'),
    path("community_post/<int:post_id>/delete/", DeleteCommunityPostView.as_view(), name="delete-community-post"),
    
    #  COMMUNITY POST COMMENTS
    path('community_post/<int:post_id>/create-comment/', CreateCommentView.as_view(), name='create-communitypost-comment'),
    path('community_post/<int:post_id>/comments/', ListCommentView.as_view(), name='community-post-comments'),
    path('community_comment/<int:pk>/update/', UpdateCommentView.as_view(), name='update-community-comment'),
    path('community_comment/<int:pk>/delete/', DeleteCommentView.as_view(), name='delete-community-comment'),
    
    # LIKE POST
    path('community/<int:post_id>/like-unlike/', LikeUnlike.as_view(), name='like_unlike'),
    
       
]

