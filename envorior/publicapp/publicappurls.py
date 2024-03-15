from django.urls import path
from .import views

urlpatterns = [
    path('about/',views.about,name='about'),
    path('complain/',views.complain,name='complain'),   
    path('contact/',views.contact,name='contact'),
    path('donation/',views.donation,name='donation'),
    path('followers/',views.followers,name='followers'),   
    path('followings/',views.followings,name='followings'),   
    path('jobs/',views.jobs,name='jobs'),
    path('notifications/',views.notifications,name='notifications'),   
    path('policy/',views.policy,name='policy'),
    path('post/',views.post,name='post'),
    path('postjob/',views.postjob,name='postjob'),
    path('postdonation/',views.postdonation,name='postdonation'),
    path('profile/',views.profile,name='profile'),   
    path('publichome/',views.publichome,name='publichome'),
    path('scam/',views.scam,name='scam'),
    path('terms/',views.terms,name='terms'),

    path('like/<int:id>/',views.like_post,name='like'), 
    path('uploadpost/',views.uploadpost,name='uploadpost'),
    path('uploadjob/',views.uploadjob,name='uploadjob'),
    path('apply_job/<int:id>/',views.apply_job,name='apply_job'),
]

