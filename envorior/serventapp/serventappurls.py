from django.urls import path
from .import views
urlpatterns = [
    path('dashboardparent/',views.dashboardparent,name='dashboardparent'),
<<<<<<< HEAD
    path('servent/',views.servent,name='servent'),
    path('post/',views.post,name='post'),
    path('event/',views.event,name='event'),
    path('serventprofile/',views.serventprofile,name='serventprofile'),
    path('notification/',views.notification,name='notification'),
    path('rank/',views.rank,name='rank'),
]
=======
]
>>>>>>> 991c6d5e3b6da6d3b0ccf69dd09e2d45d3bd55ad
