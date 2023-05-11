from django.contrib.auth import get_user_model

from django.db import models


class Hashtag(models.Model):
    name = models.CharField(max_length=60)

    class Meta:
        ordering = ["name"]


class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    user = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, related_name="posts"
    )
    hashtags = models.ManyToManyField(Hashtag)
