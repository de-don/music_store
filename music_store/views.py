from music_store.models import ListenerUser
from music_store.serializers import ListenerUserSerializer
from rest_framework import generics


class ListenerList(generics.ListCreateAPIView):
    """
    List all listeners, or create a new.
    """
    queryset = ListenerUser.objects.all()
    serializer_class = ListenerUserSerializer


class ListenerDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a code snippet.
    """
    queryset = ListenerUser.objects.all()
    serializer_class = ListenerUserSerializer
