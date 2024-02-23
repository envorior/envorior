from django.urls import path
from .import views

urlpatterns = [
    path('publichome/',views.publichome,name='publichome'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('donation/',views.donation,name='donation'),
    path('jobs/',views.jobs,name='jobs'),
    path('policy/',views.policy,name='policy'),
    path('scam/',views.scam,name='scam'),
    path('terms/',views.terms,name='terms'),
    path('profile/',views.profile,name='profile'),   
    path('complain/',views.complain,name='complain'),   
    path('followers/',views.followers,name='followers'),   
    path('followings/',views.followings,name='followings'),   
    path('notifications/',views.notifications,name='notifications'),   
]

