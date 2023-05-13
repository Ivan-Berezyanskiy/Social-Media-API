from django.urls import include, path
from rest_framework import routers

from post.views import HashtagViewSet, PostViewSet

post_router = routers.DefaultRouter()
post_router.register("posts", PostViewSet)
hashtag_router = routers.DefaultRouter()
hashtag_router.register("hashtags", HashtagViewSet)

urlpatterns = [
    path("", include(post_router.urls)),
    path("hashtag/", include(hashtag_router.urls)),
]

app_name = "post"
