from django.urls import path
from .views import (PostList, PostDetails, CreateComment,CommentList, CommentDetails,LikeUnlike,FollowUnfollow)

urlpatterns = [
    path("post-list/", PostList.as_view(), name="post-list"),
    path("post-details/<int:pk>/", PostDetails.as_view(), name="post-detail"),
    
    
    path("post/<int:pk>/create-comment/", CreateComment.as_view(), name='create_comment'),
    path("post/<int:pk>/comments/", CommentList.as_view(), name="comments"),
    path("post/comment/<int:pk>/", CommentDetails.as_view(), name="comment-details"),
    
    
    path("post/kudos/<int:post_id>/", LikeUnlike.as_view(), name='like_unlike'),  
    path("user/<int:user_id>/follow/", FollowUnfollow.as_view(), name="follow_unfollow" )
]
