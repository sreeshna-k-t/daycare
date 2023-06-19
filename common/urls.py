from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home, name='home'),
    path('login', views.login, name='login'),
    path('about', views.about, name='about'),
    path('services', views.services, name='services'),
    path('parent_registration', views.parent_registration, name='parentreg'),
    
    









]