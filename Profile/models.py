from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    profile_pic = models.ImageField(upload_to='images', default='images\profile\default.png', blank=True)
    vk = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return str(self.user)