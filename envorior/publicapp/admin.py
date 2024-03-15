from django.contrib import admin
from .models import Profile,Post,Job,Notification,Donation,Complain

# Register your models here.
admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(Job)
admin.site.register(Notification)
admin.site.register(Donation)
admin.site.register(Complain)