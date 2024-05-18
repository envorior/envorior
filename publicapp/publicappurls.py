from django.urls import path
from .import views

urlpatterns = [
    path('publichome/',views.publichome,name='publichome'),
    path('uploadpost',views.uploadpost,name='uploadpost'),
    path('like/<int:id>/',views.like_post,name='like'), 
    path('jobs/',views.jobs,name='jobs'),  
    path('uploadjob/',views.uploadjob,name='uploadjob'),
    # path('jobform/',views.jobform,name='jobform'),
    path('apply_job/<int:id>/',views.apply_job,name='apply_job'),
    path('notifications/',views.notifications,name='notifications'),   
    path('donation/',views.donation,name='donation'),
    path('postdonation/',views.postdonation,name='postdonation'),
    path('get_donation/<int:id>/',views.get_donation,name='get_donation'),
    path('rewardondonate/<int:id>/',views.reward_donate,name='rewardondonate'),
    path('changeuserprofile/',views.changeuserprofile,name='changeuserprofile'),
    path('logout/',views.logout,name='logout'),
    path('about/',views.about,name='about'),
    path('complain/',views.complain,name='complain'),   
    path('contact/',views.contact,name='contact'),
    path('followers/',views.followers,name='followers'),   
    path('followings/',views.followings,name='followings'),   
    path('policy/',views.policy,name='policy'),
    path('profile/',views.profile,name='profile'), 
    path('deletepost/<int:id>/',views.deletepost,name='deletepost'), 
    path('deletecomplain/<int:id>/',views.deletecomplain,name='deletecomplain'), 
    path('deletejob/<int:id>/',views.deletejob,name='deletejob'), 
    path('deletedonation/<int:id>/',views.deletedonation,name='deletedonation'), 
    path('scam/',views.scam,name='scam'),
    path('terms/',views.terms,name='terms'),
    path('viewevent/',views.viewevents,name='viewevent'),

    path('follow/<id>/',views.follow,name='follow'),
]

