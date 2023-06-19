from django.shortcuts import render
from common.models import *

# Create your views here.


def adminhome(request):
    
    return render(request,"daycare_admin/admin_home.html")

def staff_registration(request):

    return render(request,"daycare_admin/staff_registration.html")

def report(request):

    return render(request,"daycare_admin/report.html")

def viewparent(request):
    all_parents = ParentRegister.objects.all()
    

    return render(request,"daycare_admin/viewparent.html",{"all_parents":all_parents})

def viewpayment(request):

    return render(request,"daycare_admin/viewpayment.html")

def viewfeedback(request):

    return render(request,"daycare_admin/viewfeedback.html")




