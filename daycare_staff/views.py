from django.shortcuts import render

# Create your views here.

def staffhome(request):
    
    return render(request,"daycare_staff/staff_home.html")


def nutritions(request):

    return render(request,"nutritions.html")

def attendance(request):

    return render(request,"attendance.html")

def staff(request):

    return render(request,"staff.html")

def staffhome(request):

    return render(request,"staffhome.html")

def viewprofile(request):

    return render(request,"viewprofile.html")



