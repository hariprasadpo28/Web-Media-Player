from django.db import models
from django.contrib.auth.models import User
# Create your models here.

def upload_directory_path(instance, filename):
    return 'uploads/{0}/{1}'.format(instance.user_name.id ,filename)

def thumbnails(instance, filename):
    return 'uploads/{0}/thumbnails/{1}'.format(instance.user_name.id, filename)

class videos(models.Model):
    name = models.CharField(max_length=30)
    datafile = models.FileField(upload_to=upload_directory_path)
    upload_date = models.DateTimeField(auto_now_add = True)
    private = models.BooleanField(default = True)
    liked = models.ManyToManyField(User, default= None, blank = True, related_name='liked')
    user_name = models.ForeignKey(User,to_field="username", on_delete = models.CASCADE, related_name='user')
    
    #thumbnail = models.ImageField(upload_to=thumbnails, default = None, blank=True)
    #duration = models.CharField(max_length=50 ,default="0:0")
    #frame_rate = models.CharField(max_length=20, default="0")

    #watchlist_users = models.ManyToManyField(User, default=None, blank=True, related_name='watchlist')

    @property
    def num_likes(self):
        return self.liked.all().count()

CHOICES = (
    ('Like', 'Like'),
    ('Unlike', 'Unlike'),
)
class like(models.Model):
    video = models.ForeignKey(videos, on_delete = models.CASCADE)
    user_name = models.ForeignKey(User, to_field="username", on_delete = models.CASCADE)
    value = models.CharField(choices= CHOICES, default='Like', max_length=15)

    def __str__(self):
        return str(self.video)

class watchlist(models.Model):
    video = models.ManyToManyField(videos, default= None, blank = True, related_name='video')
    user_name = models.OneToOneField(User, on_delete = models.CASCADE)