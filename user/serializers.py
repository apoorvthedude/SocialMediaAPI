from .models import UserFollowing,User
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','email']

class UserFollowingSerializer(serializers.ModelSerializer):
    currentUser = serializers.CurrentUserDefault()

    class Meta:
        model = UserFollowing
        fields = ['id','userFollowing']
    
    def create(self, validated_data):
        request = self.context.get('request',None)
        userFollowing = self.validated_data['userFollowing']
        if request.user!=UserFollowing:
            UserFollowing.objects.create(currentUser = request.user,userFollowing = userFollowing)

        return UserFollowing(**validated_data)

class UnFollowSerializer(serializers.ModelSerializer):
    currentUser = serializers.CurrentUserDefault()
    class Meta:
        model = UserFollowing
        fields = ['id','userFollowing']

    def create(self, validated_data):
        userFollowing = self.validated_data['userFollowing']
        request = self.context.get('request',None)
        obj = UserFollowing.objects.get(currentUser = request.user,userFollowing = userFollowing)
        obj.delete()
        return UserFollowing(**validated_data)

class CustomJwtSerializer(TokenObtainPairSerializer):

    def validate(self, attrs):
        credentials = {
            'username': '',
            'password': attrs.get("password")
        }
        user_obj = User.objects.filter(email=attrs.get("username")).first() or User.objects.filter(username = attrs.get("username")).first()
        if user_obj:
            credentials['username'] = user_obj.username

        return super().validate(credentials)

class ProfileSerializer(serializers.Serializer):
    following = serializers.SerializerMethodField()
    followers = serializers.SerializerMethodField()
    username = serializers.SerializerMethodField()
    class Meta:
        model = UserFollowing
        fields = ['username','followers','following']

    def get_username(self,obj):
        user = User.objects.get(username = obj.username)
        username = user.username

    def get_followers(self,obj):
        follower = UserFollowing.objects.filter(followingUser = obj)
        return len(follower)
        
    def get_following(self,obj):
        following = UserFollowing.objects.filter(currUser = obj)
        return len(following)