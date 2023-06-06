from django.db import models
from django.contrib.auth.models import User

# Create your models here.


# class Photo(models.Model):
#     url = models.CharField(max_length=200)
#     event = models.ForeignKey(Event, on_delete=models.CASCADE)

#     def __str__(self):
#         return f"Photo for owl_id: {self.owl_id} @{self.url}"
    

from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(null=True, blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics', null=True, blank=True)
    
    def __str__(self):
        return f'{self.user.username} Profile'
class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'Comment {self.id} by {self.user.username}'

# class Photo(models.Model):
#     url = models.CharField(max_length=200)
#     event = models.ForeignKey(Event, on_delete=models.CASCADE)

#     def __str__(self):
#         return f"Photo for event_id: {self.event_id} @{self.url}"
