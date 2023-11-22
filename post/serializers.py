from rest_framework import serializers

from django.contrib.auth.models import User
from post.models import Post, Comment, UserFollow



class UserFollowSerializer(serializers.ModelSerializer):
    following_count = serializers.SerializerMethodField()
#     # following_list = serializers.SerializerMethodField()
    followers_count = serializers.SerializerMethodField()
    followers_list = serializers.SerializerMethodField()
    class Meta:
        model = UserFollow
        fields = "__all__"
    
    def get_following_count(self, object):
        return object.total_currentUser_following()

    
#     # def get_following_list(self, object):
#     #     return object.user_following_list()
    
    def get_followers_count(self, object):
        return object.total_currentUser_followers()
    
    def get_followers_list(self, object):
        return object.currentUser_followers_list()
        
        
class UserSerializer(serializers.ModelSerializer):
    following = UserFollowSerializer(many=True)
    class Meta:
        model = User
        fields = "__all__"
     

     
# class BookmarkSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Bookmark
#         fields = "__all__"
        
        
class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        exclude = ('post',)
        # fields = "__all__"
        
        
class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    # bookmarks = BookmarkSerializer(many=True, read_only=True)
    kudos_count = serializers.SerializerMethodField()
    class Meta:
        model = Post
        exclude = ('kudos',)
        # fields = "__all__"
        
        
    def get_kudos_count(self, object):
        return object.total_kudos()
    
    # def get_bookmark_count(self, object):
    #     return object.total_bookmarks()
    