from django.shortcuts import render

# Create your views here.

def parenthome(request):

    return render(request,"daycare_parent/parenthome.html")

def payment(request):

    return render(request,"daycare_parent/payment.html")

def profile(request):

    return render(request,"daycare_parent/profile.html")

def feedback(request):

    return render(request,"daycare_parent/feedback.html")

def viewreport(request):

    return render(request,"daycare_parent/viewreport.html")

def viewattendance(request):

    return render(request,"daycare_parent/attendance.html")

def viewnutritions(request):

    return render(request,"daycare_parent/viewnutritions.html")






     

