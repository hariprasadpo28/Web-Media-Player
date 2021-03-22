# Generated by Django 3.1.4 on 2021-01-05 08:41

from django.db import migrations, models
import videos.models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0005_auto_20210105_0027'),
    ]

    operations = [
        migrations.AddField(
            model_name='videos',
            name='duration',
            field=models.CharField(default='0:0', max_length=50),
        ),
        migrations.AddField(
            model_name='videos',
            name='frame_rate',
            field=models.CharField(default='0', max_length=20),
        ),
        migrations.AddField(
            model_name='videos',
            name='thumbnail',
            field=models.ImageField(blank=True, default=None, upload_to=videos.models.thumbnails),
        ),
    ]