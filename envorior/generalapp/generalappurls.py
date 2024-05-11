from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('registation/',views.registration, name='registration'),
    path('forget_password/',views.forget_password, name='forgetpassword'),
    path('get_otp/',views.get_otp, name='get_otp'),
    path('verify_otp/',views.verify_otp, name='verify_otp'),
    path('change_password/',views.change_password, name='change_password'),
]