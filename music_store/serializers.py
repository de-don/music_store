from rest_framework import serializers
from music_store.models import DefaultUser, ListenerUser, LabelUser


class DefaultUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = DefaultUser
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'balance')


class ListenerUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListenerUser
        exclude = tuple()


class LabelUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = LabelUser
        exclude = tuple()
