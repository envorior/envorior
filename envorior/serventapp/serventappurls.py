from django.urls import path
from .import views
urlpatterns = [
    path('servent-dashboard/',views.serventparent,name='serventparent'),
    path('servent/',views.servent,name='servent'),
    path('servent-post/',views.post,name='post'),
    path('servent-event/',views.event,name='event'),
    path('servent-serventprofile/',views.serventprofile,name='serventprofile'),
    path('servent-notification/',views.notification,name='notification'),
    path('servent-rank/',views.rank,name='rank'),
]

