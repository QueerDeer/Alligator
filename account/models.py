from django.contrib.auth.models import User
from django.db import models


class PodcastGenre(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=256)
    is_active = models.BooleanField(default=False)
    parent = models.ForeignKey('self', null=True, related_name='children', on_delete=models.CASCADE)

    @property
    def is_top_level(self):
        return bool(self.parent)


class Podcast(models.Model):
    id = models.IntegerField(primary_key=True)
    feed_url = models.URLField(default=None)
    primary_genre = models.OneToOneField(PodcastGenre, on_delete=models.CASCADE)
    genres = models.ManyToManyField(PodcastGenre, related_name='genres')
    art_url_30 = models.URLField(default=None)
    art_url_60 = models.URLField(default=None)
    art_url_100 = models.URLField(default=None)
    art_url_600 = models.URLField(default=None)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name=u"Пользователь")
    avatar = models.FileField(verbose_name=u"Аватар", null=True, blank=True)
    subscribes = models.ManyToManyField(Podcast)
