from rest_framework import serializers

from django.contrib.auth.models import User
from .models import Community, CommunityPost, CommunityComment


class CommunitySerializer(serializers.ModelSerializer):
    creator = serializers.PrimaryKeyRelatedField(read_only=True)
    members = serializers.PrimaryKeyRelatedField(many=True, queryset=User.objects.all(), required=False)
    class Meta:
        model = Community
        fields = "__all__"

        
        
class CommunityPostSerializer(serializers.ModelSerializer):
    kudos_count = serializers.SerializerMethodField()
    class Meta:
        model = CommunityPost
        fields = "__all__"
        
    
    def get_kudos_count(self, object):
        return object.kudos_count()
        
class CommunityCommentSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(read_only=True)
    post= serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = CommunityComment
        fields = "__all__"
        
        