from django.urls import path
from .import views
urlpatterns = [

    
    path('supervisor-complain/',views.complain,name='complain'),
    path('supervisor-event/',views.event,name='event'),
    path('supervisor-dashboard/',views.dashboard,name='dashboard'),
    path('supervisor-notification/',views.notification,name='notification'),
    path('supervisor-addservent/',views.addservent,name='addservent'),
    path('supervisor-rank/',views.rank,name='rank'),
  
]

