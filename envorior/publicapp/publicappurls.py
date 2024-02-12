<<<<<<< HEAD:envorior/publicapp/publicappurls.py
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
    
]
=======
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
    
]
>>>>>>> dfec71a3c126fad87b8a1f3853527e4c5d2c0fcc:publicapp/publicappurls.py
