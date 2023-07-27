from rest_framework import generics
from .models import *
from .serializers import *

class ListCreateUsersView(generics.ListCreateAPIView):
    queryset= Users.objects.all()
    serializer_class= UsersSerializer



class ListUpdateDeleteUserByID(generics.RetrieveUpdateDestroyAPIView):
    queryset= Users.objects.all()
    serializer_class = UsersSerializer
    lookup_url_kwarg = "user_id"