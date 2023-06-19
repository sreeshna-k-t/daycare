from django.urls import path
from . import views


app_name = "daycare_staff"
urlpatterns = [
    # path('',views.home,name="home")
    path('staffhome',views.staffhome,name="staffhome"),
    path('nutritions',views.nutritions,name="nutritions"),
    path('attendance',views.attendance,name="attendance"),
    path('viewprofile',views.viewprofile,name="viewprofile"),
    
]