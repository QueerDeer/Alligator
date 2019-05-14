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

    class Meta:
        db_table = 'podcast_genres'
        verbose_name = 'Podcast Genre'
        verbose_name_plural = 'Podcast Genres'


# class Podcast(models.Model):
#     id = models.IntegerField(primary_key=True)
#     author_id = models.IntegerField()
#     author = models.CharField(max_length=256)
#     title = models.CharField(max_length=256)
#     description = models.TextField()
#     feed_url = models.URLField(default=None)
#     primary_genre = models.OneToOneField(PodcastGenre, on_delete=models.CASCADE)
#     genres = models.ManyToManyField(PodcastGenre, related_name='genres')
#     image_url = models.URLField(default=None)
#
#     class Meta:
#         db_table = 'podcasts'
#         verbose_name = 'Podcast'
#         verbose_name_plural = 'Podcasts'

class Podcast(models.Model):
    title = models.CharField(max_length=256, default=None)
    description = models.TextField(default=None)
    feed_url = models.URLField(default=None)
    image_url = models.URLField(default=None)

    class Meta:
        db_table = 'podcasts'
        verbose_name = 'Podcast'
        verbose_name_plural = 'Podcasts'


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name=u"Пользователь")
    # avatar = models.FileField(verbose_name=u"Аватар", default='static/images/default_avatar.jpg')
    subscribes = models.ManyToManyField(Podcast, default=None)

    class Meta:
        db_table = 'profiles'
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'
