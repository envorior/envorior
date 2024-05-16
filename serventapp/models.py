from django.db import models
from publicapp.models import Profile

# Create your models here.

class Event(models.Model):
    e_id=models.AutoField(primary_key=True)
    department=models.ForeignKey(Profile,on_delete=models.CASCADE,blank=True,null=True)
    image = models.ImageField(upload_to='event_news',blank=True)
    description = models.CharField(max_length=300) 
    date = models.CharField(max_length=50)  
