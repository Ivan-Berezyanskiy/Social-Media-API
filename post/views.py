from rest_framework import viewsets, mixins

from post.models import Post, Hashtag
from post.serializers import (
    PostSerializer,
    PostCreateSerializer,
    HashtagSerializer,
)


class HashtagViewSet(
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    viewsets.GenericViewSet,
):
    serializer_class = HashtagSerializer
    queryset = Hashtag.objects.all()


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_serializer_class(self):
        if self.action in ("create", "put", "patch"):
            return PostCreateSerializer
        return PostSerializer

    def get_queryset(self):
        queryset = Post.objects.all()
        hashtags = self.request.query_params.get("hashtags")
        if hashtags:
            queryset = queryset.filter(hashtags__in=hashtags)
        return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
