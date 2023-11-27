from django.db import models

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