from django.urls import path, include
from .views import (PostList,PostDetails,CreateComment,CommentList, 
                               CommentDetails,LikeUnlike,FollowUnfollow,
                               BookmarkListView, BookmarkCreateView)
from rest_framework.routers import DefaultRouter

# router = DefaultRouter()
# router.register('posts', PostViewSet, basename='post')

urlpatterns = [
    # path('', include(router.urls)),
    
    path("posts/", PostList.as_view(), name="post-list"),
    path("post-details/<int:pk>/", PostDetails.as_view(), name="post-detail"),
    
    
    path("post/<int:post_id>/create-comment/", CreateComment.as_view(), name='create_comment'),
    path("post/<int:pk>/comments/", CommentList.as_view(), name="comments"),
    path("post/comment/<int:pk>/", CommentDetails.as_view(), name="comment-details"),
    
    
    path("post/kudos/<int:post_id>/", LikeUnlike.as_view(), name='like_unlike'),  
    path("user/<int:user_id>/follow/", FollowUnfollow.as_view(), name="follow_unfollow" ),
    
     path('bookmarks/', BookmarkListView.as_view(), name='bookmark-list'),
    path('post/bookmark/', BookmarkCreateView.as_view(), name='bookmark-create'),
    # path('bookmark/<int:post_id>/delete', BookmarkDeleteView.as_view(), name='bookmark-delete'),
]
