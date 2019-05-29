# Generated by Django 2.1 on 2019-05-29 14:19

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
                ('id', models.UUIDField(primary_key=True, serialize=False)),
                ('author', models.CharField(default=None, max_length=256)),
                ('title', models.CharField(default=None, max_length=256)),
                ('description', models.TextField(default=None)),
                ('feed_url', models.URLField(default=None)),
                ('image_url', models.URLField(default=None)),
            ],
            options={
                'verbose_name_plural': 'Podcasts',
                'db_table': 'account_podcasts',
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
                'db_table': 'account_podcast_genres',
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
                'db_table': 'account_profiles',
                'verbose_name': 'Profile',
            },
        ),
        migrations.AddField(
            model_name='podcast',
            name='genres',
            field=models.ManyToManyField(null=True, related_name='genres', to='account.PodcastGenre'),
        ),
        migrations.AddField(
            model_name='podcast',
            name='primary_genre',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to='account.PodcastGenre'),
        ),
    ]
