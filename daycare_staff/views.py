from django.shortcuts import render
from common.models import *
from daycare_admin.models import *
# Create your views here.

def staffhome(request):
    
    return render(request,"daycare_staff/staffhome.html")

def viewprofile(request):
    view_child = ChildRegister.objects.all()
    print(view_child)
    return render(request,"daycare_staff/viewprofile.html",{"all_child":view_child})


    
def attendance(request):

    return render(request,"daycare_staff/attendance.html")



def nutritions(request):

    return render(request,"daycare_staff/nutritions.html")







