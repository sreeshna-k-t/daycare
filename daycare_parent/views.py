from django.shortcuts import render,redirect
from .models import *
from daycare_parent .models import *

# Create your views here.

def parenthome(request):

    return render(request,"daycare_parent/parenthome.html")

def payment(request):

    return render(request,"daycare_parent/payment.html")

def profile(request):

    return render(request,"daycare_parent/profile.html")

def feedback(request):
    
    if request.method == "POST":
        feed_name = request.POST["feed_name"]
        feed_no = request.POST["feed_no"]
        feed_email = request.POST["feed_email"]
        feed_feedback = request.POST["feed_feedback"]
        feed_date = request.POST["feed_date"]
        user_id = request.session["user_id"]
        parent_fk = ParentRegister.objects.get(id=user_id)
        feedback = ParentFeedback(parent_fk=parent_fk,feed_name=feed_name,feed_no=feed_no,feed_email=feed_email,feed_feedback=feed_feedback,feed_date=feed_date)
        feedback.save()
        message = "Thank you for submitting feedback!"
        return render(request,"daycare_parent/feedback.html",{"message":message})
    return render(request,"daycare_parent/feedback.html")

def viewreport(request):
    reports = IncidentReport.objects.all()

    return render(request,"daycare_parent/viewreport.html",{"reports":reports})

def viewattendance(request):

    return render(request,"daycare_parent/viewattendance.html")

def viewnutritions(request):

    return render(request,"daycare_parent/viewnutritions.html")






     

