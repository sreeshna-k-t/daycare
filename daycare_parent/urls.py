from django.urls import path
from . import views


app_name = "daycare_parent"
urlpatterns = [
    # path('',views.home,name="home")
    path('', views.parenthome, name='parenthome'),
    path('feedback', views.feedback, name='feedback'),
    path('profile', views.profile, name='profile'),
    path('payment', views.payment, name='payment'),
    path('viewnutritions', views.viewnutritions, name='viewnutritions'),
    path('viewreport', views.viewreport, name='viewreport'),
    path('viewattendance', views.viewattendance, name='viewattendance'),

]