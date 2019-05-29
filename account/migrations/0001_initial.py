# Generated by Django 2.1 on 2019-05-29 11:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Podcast',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default=None, max_length=256)),
                ('description', models.TextField(default=None)),
                ('feed_url', models.URLField(default=None)),
                ('image_url', models.URLField(default=None)),
            ],
            options={
                'verbose_name_plural': 'Podcasts',
                'db_table': 'podcasts',
                'verbose_name': 'Podcast',
            },
        ),
        migrations.CreateModel(
            name='PodcastGenre',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=256)),
                ('is_active', models.BooleanField(default=False)),
                ('parent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='account.PodcastGenre')),
            ],
            options={
                'verbose_name_plural': 'Podcast Genres',
                'db_table': 'podcast_genres',
                'verbose_name': 'Podcast Genre',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subscribes', models.ManyToManyField(default=None, to='account.Podcast')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name_plural': 'Profiles',
                'db_table': 'profiles',
                'verbose_name': 'Profile',
            },
        ),
    ]
