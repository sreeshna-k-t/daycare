from django.urls import path
from . import views


app_name = "daycare_admin"
urlpatterns = [
    path('',views.home,name="home")
]