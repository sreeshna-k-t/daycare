from django.urls import path
from . import views 
urlpatterns = [
    path('', views.home, name='home'),
    path('login', views.login, name='login'),
    path('about', views.about, name='about'),
    path('services', views.services, name='services'),
    path('parent_registration', views.parent_registration, name='parentreg'),
    path('staff_registration', views.staff_registration, name='staffreg'),
    path('report', views.report, name='report'),
    path('nutritions', views.nutritions, name='nutritions'),
    path('attendance', views.attendance, name='attendance'),
    path('feedback', views.feedback, name='feedback'),
    path('profile', views.profile, name='profile'),
    path('payment', views.payment, name='payment'),
    path('admin', views.admin, name='admin'),









]