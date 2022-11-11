from django.urls import path, include

from rest_framework.routers import DefaultRouter
from post.views import AllPostView

from user.views import (
   UserFollowingView,
   UnfollowView,
   ProfileView,
)

router = DefaultRouter()
router.register("all_posts", AllPostView, basename="all-post-view")

router.register("user", ProfileView, basename="user-profile-view")

urlpatterns = [
    path("", include(router.urls)),
]