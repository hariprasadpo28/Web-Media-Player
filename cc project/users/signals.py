from django.db.models.signals import post_save
from django.dispatch import receiver
from videos.models import watchlist
from django.contrib.auth.models import User


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        watchlist.objects.create(user_name=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.watchlist.save()