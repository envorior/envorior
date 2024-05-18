from django.urls import path
from .import views
urlpatterns = [
    path('servent-dashboard/',views.dashboard,name='dashboard'),
    path('servent-complain/',views.complain,name='complain'),
    path('solvecomplain/<int:id>/',views.solve_complain,name='solvecomplain'), 
    path('servent-rank/',views.rank,name='rank'),


    path('servent/',views.servent,name='servent'),
    
    path('servent-event/',views.event,name='event'),
    path('your_event/',views.your_event,name='your_event'),
    path('delete_event/<int:id>/',views.delete_event,name='delete_event'),
    path('servent-post/',views.post,name='post'),
    path('servent-serventprofile/',views.serventprofile,name='serventprofile'),

    
]

