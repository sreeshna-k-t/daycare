from django.urls import path
from . import views


app_name = "daycare_staff"
urlpatterns = [
    # path('',views.home,name="home")
    path('',views.staffhome,name="staffhome"),
    path('viewprofile',views.viewprofile,name='viewprofile'), 
    path('attendance',views.attendance,name='attendance'),
    path('nutritions/<int:id>',views.nutritions,name='nutritions'),
    
    
]