# Generated by Django 2.1 on 2019-05-13 12:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_podcastgenre_subgenres'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='podcastgenre',
            name='subgenres',
        ),
        migrations.AddField(
            model_name='podcastgenre',
            name='parent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sub_genre', to='account.PodcastGenre'),
        ),
    ]
