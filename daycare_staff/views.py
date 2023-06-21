from django.shortcuts import render

# Create your views here.

def staffhome(request):
    
    return render(request,"daycare_staff/staffhome.html")

def viewprofile(request):

    return render(request,"daycare_staff/viewprofile.html")

def attendance(request):

    return render(request,"daycare_staff/attendance.html")



def nutritions(request):

    return render(request,"daycare_staff/nutritions.html")







