# Generated by Django 2.1 on 2019-05-13 12:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20190513_0143'),
    ]

    operations = [
        migrations.AddField(
            model_name='podcastgenre',
            name='subgenres',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='account.PodcastGenre'),
        ),
    ]
