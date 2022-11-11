from django.urls import path, include

from rest_framework.routers import DefaultRouter

from post.views import (
   PostCreateView
)

router = DefaultRouter()
router.register("posts", PostCreateView, basename="post-view")


urlpatterns = [
    path("", include(router.urls)),
]