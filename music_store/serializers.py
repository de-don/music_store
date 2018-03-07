from rest_framework import serializers
from music_store.models import DefaultUser, ListenerUser, LabelUser, TrackLabel


class DefaultUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = DefaultUser
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'balance', 'user_level')


class ListenerUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListenerUser
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'balance', 'preference', 'user_level')


class LabelUserSerializer(serializers.ModelSerializer):
    track_labels = serializers.PrimaryKeyRelatedField(many=True,
                                                      queryset=TrackLabel.objects.all())

    class Meta:
        model = LabelUser
        fields = ('id', 'username', 'first_name', 'last_name',
                  'email', 'balance', 'label_info', 'track_labels', 'user_level')


class TrackLabelSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = TrackLabel
        fields = ('id', 'owner', 'title')
