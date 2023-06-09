from django.shortcuts import render

# Create your views here.

def home(request):

    return render(request,"home.html")

def login(request):

    return render(request,"login.html")

def about(request):
    
    return render(request,"about.html")

def services(request):
    
    return render(request,"services.html")

def parent_registration(request):

    return render(request,"parent_registration.html")

def staff_registration(request):

    return render(request,"staff_registration.html")

def report(request):

    return render(request,"report.html")

def nutritions(request):

    return render(request,"nutritions.html")

def attendance(request):

    return render(request,"attendance.html")

def feedback(request):

    return render(request,"feedback.html")

def profile(request):

    return render(request,"profile.html")

def payment(request):

    return render(request,"payment.html")

def admin(request):

    return render(request,"admin.html")