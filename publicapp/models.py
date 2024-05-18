from django.db import models
from generalapp.models import User

# Create your models here.
class Profile(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    contact_no=models.IntegerField()
    full_name=models.CharField(max_length=50)
    dob = models.CharField(max_length=100,blank=True)
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
    postby=models.ForeignKey(Profile,on_delete=models.CASCADE)
    posteddate=models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User,related_name="likes",blank=True)   

class Job(models.Model):
    j_id = models.BigAutoField(primary_key=True)
    skill_required = models.TextField()
    job_description=models.TextField()
    job_type = models.CharField(max_length=200)
    salary = models.IntegerField()
    job_location = models.CharField(max_length=500)
    job_by = models.ForeignKey(Profile,on_delete=models.CASCADE,blank=True,null=True)
    job_post_date = models.DateField()     

class Notification(models.Model):
    n_msg = models.TextField()
    notification_by = models.CharField(max_length=200) 
    notification_to = models.CharField(max_length=200) 
    notification_date = models.DateField()   

class Donation(models.Model):
    d_id=models.AutoField(primary_key=True)
    donation_type=models.CharField(max_length=200)
    description = models.TextField(blank=True)
    donated_by=models.ForeignKey(Profile,on_delete=models.CASCADE,blank=True,null=True)
    product_image = models.ImageField(upload_to='donate_products',blank=True)
    donar_location = models.CharField(max_length=300)
    rewards = models.ManyToManyField(User,related_name="rewards",blank=True)  

class Complain(models.Model):
    c_id=models.AutoField(primary_key=True)
    complain_type=models.CharField(max_length=200)
    description = models.TextField(blank=True)
    complain_by=models.ForeignKey(Profile,on_delete=models.CASCADE,blank=True,null=True)
    complain_image = models.ImageField(upload_to='complain_images',blank=True)
    complain_location = models.CharField(max_length=300)   
    complain_status = models.CharField(max_length=100,default='unsolved')    

class TopEnvorior(models.Model):
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE)  
    reward = models.IntegerField() 