from rest_framework import generics
from .models import *
from .serializers import *

class ListCreateUsersView(generics.ListCreateAPIView):
    queryset= 'aqui vai o model importado.objects.all()'
    serializer_class= 'serializerUser'


class ListUpdateDeleteUserByID(generics.RetrieveUpdateDestroyAPIView):
    queryset= 'Users.objects.all()'
    serializer_class = 'UsersSerializers'
    lookup_url_kwarg = "users_id"