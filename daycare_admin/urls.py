from django.urls import path
from . import views


app_name = "daycare_admin"
urlpatterns = [
    path('', views.adminhome, name='admin_home'),
    path('staff_registration', views.staff_registration, name='staffreg'),
    path('report', views.report, name='report'),
    path('viewparent', views.viewparent, name='viewparent'),
    path('viewpayment', views.viewpayment, name='viewpayment'),
    path('viewfeedback', views.viewfeedback, name='viewfeedback'),


]
