from django.urls import path
from .import views

urlpatterns = [  
    
    path('supervisor-dashboard/',views.dashboard,name='supervisordashboard'),
     
    path('supervisor-complain/',views.complain,name='complain'),
    path('supervisor-view-servent/',views.view_servent,name='viewservent'),
    path('supervisor-addservent/',views.addservent,name='addservent'),
    path('supervisor-rank/',views.rank,name='rank'),  
]

