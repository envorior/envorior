from django.db import models
<<<<<<< HEAD
from django.contrib.auth.models import AbstractBaseUser

# Create your models here.
class User(models.Model):
    email=models.CharField(max_length=200,primary_key=True)
    password=models.CharField(max_length=20)
    user_type=models.CharField(max_length=200,default="general")

class Profile(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    contact_no=models.IntegerField()
    full_name=models.CharField(max_length=50)
    dob = models.CharField(max_length=100)
    city=models.CharField(max_length=200)
    state=models.CharField(max_length=200)
    pin_code=models.CharField(max_length=100)
    followers=models.ManyToManyField(User,related_name='followers',blank=True)
    followings =models.ManyToManyField(User,related_name='followings',blank=True)
    profile_picture = models.ImageField(upload_to='profilepics',blank=True)
    reward = models.IntegerField(default=0)



=======

# Create your models here.
class Registration(models.Model):
    email=models.CharField(max_length=50,primary_key=True)
    contactno=models.IntegerField()
    fname=models.CharField(max_length=20)
    lname=models.CharField(max_length=30)
    gender=models.CharField(max_length=10)
    dob=models.DateField(max_length=50)
    country=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    city=models.CharField(max_length=50)
    pin=models.IntegerField()

class Login(models.Model):
    email=models.CharField(max_length=50)
    password=models.CharField(max_length=20)
>>>>>>> 1c239607f22fe8c0decd8b5d29d10a429c48233f
