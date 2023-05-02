from django.db import models
from django.contrib.auth.models import User
# from .models import *

# Create your models here.
class Event(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event_name = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=100)
    image = models.ImageField(upload_to='event_images/', blank=True, null=True)
    likes_count = models.CharField(max_length=100, blank=True, null=True)
    
    def __str__(self):
        return self.event_name

class LikedEvent(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    is_liked = models.BooleanField(default=False)
    def __str__(self):
        return f"{self.user.username} likes {self.event.event_name}"
