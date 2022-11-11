from django.shortcuts import render
from user.serializers import UserFollowingSerializer,UnFollowSerializer, UserSerializer, ProfileSerializer
from .models import UserFollowing
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404
from rest_framework import serializers, viewsets

# Create your views here.
class UserView(viewsets.ModelViewSet):
    http_method_names: ['get']
    serializer_class = UserSerializer
    queryset = User.objects.all()

class ProfileView(viewsets.ModelViewSet):
    serializer_class = ProfileSerializer
    def get_queryset(self):
        user = self.request.user
        queryset = User.objects.filter(id=user.id)
        return queryset()

class UserFollowingView(generics.CreateAPIView):
    serializer_class = UserFollowingSerializer
    queryset = UserFollowing.objects.all()

    def get_serializer(self, *args, **kwargs):
        serializer_class = self.get_serializer_class()
        kwargs['context'] = self.get_serializer_class()

        if 'pk' in self.kwargs:
            mod_data = self.request.data.copy()
            mod_data['userFollowing'] = self.kwargs.get('pk')
            mod_data['currentUser'] = self.request.user.id
            kwargs["data"] = mod_data
            return serializer_class(*args, **kwargs)

        return serializer_class(*args,**kwargs)

class UnfollowView(generics.CreateAPIView):
    serializer_class = UnFollowSerializer
    queryset = UserFollowing.objects.all()

    def get_serializer(self, *args, **kwargs):
        serializer_class = self.get_serializer_class()
        kwargs['context'] = self.get_serializer_context()

        if 'pk' in self.kwargs:
            mod_data = self.request.data.copy()
            mod_data['userFollowing'] = self.kwargs.get('pk')
            mod_data['currentUser'] = self.request.user.id
            kwargs['data'] = mod_data
            return serializer_class(*args, **kwargs)

        #if not found then return
        return serializer_class(*args,**kwargs)
