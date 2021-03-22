# Generated by Django 3.1.4 on 2021-01-04 18:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('videos', '0004_auto_20210104_2358'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='videos',
            name='watchlist_users',
        ),
        migrations.CreateModel(
            name='watchlist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('video', models.ManyToManyField(blank=True, default=None, related_name='video', to='videos.videos')),
            ],
        ),
    ]
