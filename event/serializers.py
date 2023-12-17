from rest_framework import serializers
from .models import Event

from django.contrib.auth.models import User 

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')



class EventSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)
    class Meta:
        model = Event
        fields = "__all__"

    def create(self, validated_data):
        return Event.objects.create(**validated_data)
