from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Event(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Photo(models.Model):
    url = models.CharField(max_length=200)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for event_id: {self.event_id} @{self.url}"