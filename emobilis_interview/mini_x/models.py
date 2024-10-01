from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    content = models.CharField(max_length=280)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='liked_posts', blank=True)

    def __str__(self):
        return f'{self.author.username}: {self.content[:50]}'

