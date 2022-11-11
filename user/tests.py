from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from user.serializers import UserSerializer
from post.serializers import PostSerializer
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from urllib import response
from django.contrib.auth.models import User

# Create your tests here.

class UserTest(APITestCase):
    print("\n")
    def Initiate(self) -> None:
        self.user = User.objects.create_user(
            username='admin',email='',password='admin123123')
        User.objects.create_user(
            username='apurv',password='apurv123123'
        )
        User.objects.create_user(
            username='apurvGarg',password='Gargapurv123123'
        )
        self.client.login(username='admin',password='admin123123')

    def TestFollow(self):
        response = self.client.post('api/follow/2')
        print("User followed Successfully: \n")
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)        
        
    def TestUnfollow(self):
        self.client.post('/api/follow/3')
        response = self.client.post('/api/unfollow/3')
        print("POST : '/api/follow/3'")
        print("User unfollowed Successfully: \n")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED) 

    def TestUnfollowUserDNE(self):
        self.client.post('/api/follow/2')
        response = self.client.post('/api/unfollow/4')
        print("POST : '/api/follow/4'")
        print("User does not exist: \n")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def TestUser(self):
        response = self.client.get('/api/user/')
        print("POSITIVE: User Details: \n")
        self.assertEqual(response.status_code, status.HTTP_200_OK)