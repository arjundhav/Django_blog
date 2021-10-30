from django.db import models
from django.contrib.auth.models import User as Authuser
from PIL import Image #pillow lib
# Create your models here.


class User(models.Model):

    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password1 = models.CharField(max_length=300)
    password2 = models.CharField(max_length=300)
    mobile = models.CharField(max_length=15, null=True)

    def __str__(self):
        return self.username

class Profile(models.Model):
    user = models.OneToOneField(Authuser, on_delete=models.CASCADE)
    image= models.ImageField(default='default.png',upload_to='profile_pics/')  #pip install pillow
        
    def __str__(self):
        return f'{self.user.username} Profile' 

    def save(self):
        super().save()

        img=Image.open(self.image.path)
        
        if img.height>300 or img.width>300:
            output_size=(300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)



