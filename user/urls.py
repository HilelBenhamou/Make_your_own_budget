from django.urls import path
from user import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register', views.register, name='register'),
    path('my_profile', views.my_profile, name='my_profile'),


]