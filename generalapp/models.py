from django.db import models

# Create your models here.
class User(models.Model):
    email=models.CharField(max_length=200,primary_key=True)
    password=models.CharField(max_length=20)
    user_type=models.CharField(max_length=200,default="general")

class Profile(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    contact_no=models.IntegerField()
    full_name=models.CharField(max_length=50)
    dob = models.CharField(max_length=100)
    city=models.CharField(max_length=200)
    state=models.CharField(max_length=200)
    pin_code=models.CharField(max_length=100)
    followers=models.ManyToManyField(User,related_name='followers',blank=True)
    followings =models.ManyToManyField(User,related_name='followings',blank=True)
    profile_picture = models.ImageField(upload_to='profilepics',blank=True)



