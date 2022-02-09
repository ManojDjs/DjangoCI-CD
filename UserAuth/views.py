from .serializers import UserDetailSerializer, UserRegSerializer
from rest_framework import generics
from .models import User


class User_detail(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer


class User_Edit(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegSerializer
    lookup_field = 'pk'
