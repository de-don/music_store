from music_store.models import ListenerUser
from music_store.serializers import ListenerUserSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class ListenerList(APIView):
    """
    List all listeners, or create a new.
    """

    def get(self, request, format=None):
        lus = ListenerUser.objects.all()
        serializer = ListenerUserSerializer(lus, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ListenerUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ListenerDetail(APIView):
    """
    Retrieve, update or delete a code snippet.
    """

    def get_object(self, pk):
        try:
            return ListenerUser.objects.get(pk=pk)
        except ListenerUser.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        lu = self.get_object(pk)
        serializer = ListenerUserSerializer(lu)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        lu = self.get_object(pk)
        serializer = ListenerUserSerializer(lu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        lu = self.get_object(pk)
        lu.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
