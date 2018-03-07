from music_store.models import ListenerUser, LabelUser, TrackLabel
from music_store.serializers import (ListenerUserSerializer,
                                     LabelUserSerializer, TrackLabelSerializer)
from rest_framework import generics
from rest_framework import permissions

from .permissions import IsOwnerOrReadOnly, IsLabelUserOrReadOnly

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'listeners': reverse('listeners-list', request=request, format=format),
        'labelusers': reverse('labelusers-list', request=request, format=format),
        'track_labels': reverse('track_labels-list', request=request, format=format)
    })

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
