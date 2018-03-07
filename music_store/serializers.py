from rest_framework import serializers
from music_store.models import DefaultUser, ListenerUser


class ListenerUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListenerUser
        fields = ('id', 'email', 'name', 'is_active', 'created')