# Generated by Django 3.1.4 on 2021-01-05 09:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0006_auto_20210105_1411'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='videos',
            name='duration',
        ),
        migrations.RemoveField(
            model_name='videos',
            name='frame_rate',
        ),
        migrations.RemoveField(
            model_name='videos',
            name='thumbnail',
        ),
    ]
