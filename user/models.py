from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

# Create your models here.

class UserFollowing(models.Model):
    currentUser = models.ForeignKey(User,related_name="following",on_delete=models.CASCADE,default = None)
    userFollowing = models.ForeignKey(User,related_name="followers",on_delete=models.CASCADE,default = None)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['currentUser','userFollowing'],name='unique followers')
        ]
    
    def __str__(self):
        return f"{self.currentUser} follows {self.userFollowing}"