# Generated by Django 2.1 on 2019-05-13 23:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_auto_20190513_1245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='podcastgenre',
            name='parent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='account.PodcastGenre'),
        ),
    ]
