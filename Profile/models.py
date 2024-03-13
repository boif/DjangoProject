from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
<<<<<<< HEAD
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    profile_pic = models.ImageField(upload_to='images', default='images\profile\default.png', blank=True)
    vk = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return str(self.user)
=======
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=255, blank=True,null=True)
    image = models.ImageField(upload_to='media/',blank=True, null=True)
    surname = models.CharField(max_length=255, blank=True,null=True)
    bio = models.TextField(blank=True,null=True)
    age = models.IntegerField(null=True)
    friends = models.ManyToManyField('self', symmetrical=True, blank=True)
        
    def __str__(self):
        return f"{self.user.username}'s Profile"
    
    def save(self):
        super().save()
        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
            


>>>>>>> profile
