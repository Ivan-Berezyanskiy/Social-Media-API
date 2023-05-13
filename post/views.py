from rest_framework import viewsets, mixins

from post.models import Post, Hashtag
from post.serializers import (
    PostSerializer,
    PostCreateSerializer,
    HashtagSerializer, PostDetailSerializer,
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
        if self.action == "retrieve":
            return PostDetailSerializer
        return PostSerializer

    def get_queryset(self):
        queryset = Post.objects.prefetch_related("hashtags")
        title = self.request.query_params.get("title")
        hashtags = self.request.query_params.get("hashtags")
        if hashtags:
            queryset = queryset.filter(hashtags__in=hashtags)
        if title:
            queryset = queryset.filter(title__icontains=title)
        return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
