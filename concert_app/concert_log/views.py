from django.contrib.auth.models import User
from django.contrib.sites import requests
from rest_framework import generics
from rest_framework.response import Response

from concert_app.concert_log.models import UserConcert
from concert_app.concert_log.serializers import UserSerializer, UserConcertSerializer
from concert_app.settings.local import SETLIST_KEY
import requests


# **************************************** USER VIEWS ****************************************#
class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# **************************************** USER CONCERT VIEWS ****************************************#
class UserConcertList(generics.ListCreateAPIView):
    serializer_class = UserConcertSerializer

    def get_queryset(self):
        return UserConcert.objects.filter(user__id=self.kwargs['user_id'])

    def list(self, request, *args, **kwargs):
        request_headers = {'content-type': "application/json", 'x-api-key': SETLIST_KEY}
        api_endpoint = 'https://api.setlist.fm/rest/1.0/search/artists?artistMbid=b10bbbfc-cf9e-42e0-be17-e2c3e1d2600d'

        response = requests.get(api_endpoint, headers=request_headers)
        print(response.text)

        queryset = self.get_queryset()
        serializer = UserConcertSerializer(queryset, many=True)
        return Response(serializer.data)
