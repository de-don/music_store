from music_store.models import DefaultUser, ListenerUser, LabelUser
from music_store.serializers import *
from rest_framework import generics


class DefaultUserList(generics.ListCreateAPIView):
    """
    List all listeners, or create a new.
    """
    queryset = DefaultUser.objects.all()
    serializer_class = DefaultUserSerializer


class DefaultUserDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a listeners.
    """
    queryset = DefaultUser.objects.all()
    serializer_class = DefaultUserSerializer
