from django.db import models
from django.contrib.auth.models import User

#Create your models here.
class Profile(models.Model)
    gender_choices = [
        ('male', "male")
        ('female', "female")
        ('other', "Don't want to disclose")
    ]
     first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    picture = models.ImageField(upload_to='profile/')
    gender_choices