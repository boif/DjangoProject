from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(blank=True)
    content = models.FileField(upload_to='PostContent', blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()

    def __str__(self):
        return f"{self.author.username} - {self.date.strftime('%Y-%m-%d %H:%M:%S')}"