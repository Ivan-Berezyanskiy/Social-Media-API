from rest_framework import serializers

from post.models import Post, Hashtag


class HashtagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hashtag
        fields = "__all__"


class PostSerializer(serializers.ModelSerializer):
    hashtags = HashtagSerializer(
        many=True,
        read_only=True,
    )

    class Meta:
        model = Post
        fields = (
            "id",
            "title",
            "content",
            "user",
            "hashtags",
        )
        read_only_fields = (
            "id",
            "title",
            "content",
            "user",
            "hashtags",
        )


class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"
        read_only_fields = ("id", "user")
