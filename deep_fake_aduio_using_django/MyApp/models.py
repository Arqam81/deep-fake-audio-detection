from django.db import models
from .validators import file_size

# Create your models here.
class Video(models.Model):
      caption=models.CharField(max_length=100)
      video=models.FileField(validators=[file_size])
      def __str__(self):
           return self.caption
     
class Signup(models.Model):
      full_name=models.CharField(max_length=100)
      email=models.EmailField()
      password=models.CharField(max_length=100)
      confirm_password=models.CharField(max_length=100)     