from rest_framework import serializers

from django.contrib.auth.models import User
from post.models import Post, Comment, UserFollow, Bookmark


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')


class UserFollowSerializer(serializers.ModelSerializer):
    following_count = serializers.SerializerMethodField()
    followers = serializers.SerializerMethodField()
    followers_count = serializers.SerializerMethodField()
    following = UserSerializer(many=True, read_only=True)
    class Meta:
        model = UserFollow
        fields = "__all__"
    
    def get_following_count(self, object):
        return object.total_currentUser_following()

    
    # def get_following_list(self, object):
    #     return object.total_currentUser_followers()
    
    def get_followers_count(self, object):
        return object.total_currentUser_followers()
    
    def get_followers(self, object):
        return object.currentUser_followers_list()
        
     
class BookmarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bookmark
        fields = ['id', 'post', 'added_at']
        
        
class CommentSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    post = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Comment
        fields = "__all__"
        
        
class PostSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    kudos = UserSerializer(many=True, read_only=True)
    total_kudos = serializers.SerializerMethodField()
    total_comments = serializers.SerializerMethodField()
    total_bookmarks = serializers.SerializerMethodField()
    class Meta:
        model = Post
        fields = "__all__"
        
        
    def get_total_kudos(self, object):
        return object.total_kudos()
    
    def get_total_comments(self, object):
        return object.total_comments()
    
    def get_total_bookmarks(self, object):
         return object.total_bookmarks()
    