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
    
]
