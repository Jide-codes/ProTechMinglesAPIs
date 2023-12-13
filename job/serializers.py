from rest_framework import serializers

from .models import Job


# class TagSerializer(serializers.ModelSerializer):
#     Job_tags = serializers.SlugRelatedField(many=True, read_only=True, slug_field='title')
#     class Meta:
#         model = Tag
#         fields = "__all__"

class JobSerializer(serializers.ModelSerializer):
    creator = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Job
        fields = "__all__"
        
        
