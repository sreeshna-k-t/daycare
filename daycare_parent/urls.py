from django.urls import path
from . import views


app_name = "daycare_parent"
urlpatterns = [
    # path('',views.home,name="home")
    path('', views.parenthome, name='parenthome'),
    path('feedback', views.feedback, name='feedback'),
    path('profile', views.profile, name='profile'),
    path('edit/<int:id>', views.edit_child, name='edit_child'),
    # path('payment', views.payment, name='payment'),
    path('viewnutritions', views.viewnutritions, name='viewnutritions'),
    path('viewreport', views.viewreport, name='viewreport'),
    path('viewattendance', views.viewattendance, name='viewattendance'),
    path('payment', views.ViewPayment.as_view(), name='payment'),
    path('charge', views.charge, name='charge'),
    path('logout', views.logout, name="logout"),

]