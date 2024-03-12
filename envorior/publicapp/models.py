from django.db import models
from generalapp.models import User

# Create your models here.
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

class Post(models.Model):
    pid=models.AutoField(primary_key=True)
    postcaption=models.TextField()
    postimage=models.ImageField(upload_to='posts',blank=True)
    postby=models.CharField(max_length=200)
    posteddate=models.CharField(max_length=30)
    reward = models.IntegerField()
    

class Job(models.Model):
    j_id = models.BigAutoField(primary_key=True)
    skill_required = models.TextField()
    job_description=models.TextField()
    job_type = models.CharField(max_length=200)
    salary = models.IntegerField()
    job_location = models.CharField(max_length=500)
    job_by = models.CharField(max_length=500)
    job_post_date = models.DateField()

class Notification(models.Model):
    n_msg = models.TextField()
    notification_by = models.CharField(max_length=200) 
    notification_to = models.CharField(max_length=200) 
    notification_date = models.DateField()
