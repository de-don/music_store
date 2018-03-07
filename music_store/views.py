from music_store.models import DefaultUser, ListenerUser, LabelUser, TrackLabel
from music_store.serializers import (DefaultUserSerializer, ListenerUserSerializer,
                                     LabelUserSerializer, TrackLabelSerializer)
from rest_framework import generics
from rest_framework import permissions

from .permissions import IsOwnerOrReadOnly, IsLabelUserOrReadOnly


class DefaultUserList(generics.ListCreateAPIView):
    queryset = DefaultUser.objects.all()
    serializer_class = DefaultUserSerializer


class DefaultUserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = DefaultUser.objects.all()
    serializer_class = DefaultUserSerializer


class ListenerUserList(generics.ListCreateAPIView):
    queryset = ListenerUser.objects.all()
    serializer_class = ListenerUserSerializer


class ListenerUserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ListenerUser.objects.all()
    serializer_class = ListenerUserSerializer


class LabelUserList(generics.ListCreateAPIView):
    queryset = LabelUser.objects.all()
    serializer_class = LabelUserSerializer


class LabelUserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = LabelUser.objects.all()
    serializer_class = LabelUserSerializer


class TrackLabelList(generics.ListCreateAPIView):
    queryset = TrackLabel.objects.all()
    serializer_class = TrackLabelSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsLabelUserOrReadOnly)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class TrackLabelDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = TrackLabel.objects.all()
    serializer_class = TrackLabelSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly, IsLabelUserOrReadOnly)
