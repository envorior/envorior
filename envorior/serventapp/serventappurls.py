from django.urls import path
from .import views
urlpatterns = [
    path('dashboardparent/',views.dashboardparent,name='dashboardparent'),
    path('servent/',views.servent,name='servent'),
    path('post/',views.post,name='post'),
    path('event/',views.event,name='event'),
    path('serventprofile/',views.serventprofile,name='serventprofile'),
    path('notification/',views.notification,name='notification'),
    path('rank/',views.rank,name='rank'),
]
