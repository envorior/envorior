from django.urls import path
from .import views
urlpatterns = [

    path('servent/',views.servent,name='servent'),
    path('servent-complain/',views.complain,name='complain'),
    path('servent-event/',views.event,name='event'),
    path('servent-dashboard/',views.dashboard,name='dashboard'),
    path('servent-notification/',views.notification,name='notification'),
    path('servent-post/',views.post,name='post'),
    path('servent-rank/',views.rank,name='rank'),
    path('servent-serventprofile/',views.serventprofile,name='serventprofile'),
]

