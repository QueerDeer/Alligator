from django.contrib.auth.models import User
from django.db import models


class Podcast(models.Model):
    url = models.URLField()


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name=u"Пользователь")
    avatar = models.FileField(verbose_name=u"Аватар", null=True, blank=True)
    subscribes = models.ManyToManyField(Podcast)