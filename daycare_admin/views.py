from django.shortcuts import render
from common.models import *
from daycare_parent.models import * 
from .models import *


# Create your views here.


def adminhome(request):
    
    return render(request,"daycare_admin/admin_home.html")

def staff_registration(request):

    return render(request,"daycare_admin/staff_registration.html")

def report(request):
    
    if request.method == "POST":
        child_name = request.POST["child_name"]
        parent_email_id = request.POST["parent_email_id"]
        description = request.POST["description"]
        current_status = request.POST["current_status"]
        reported_by = request.POST["reported_by"]
        report_date = request.POST["report_date"]
        report = IncidentReport(child_name=child_name, parent_email_id=parent_email_id, description=description, current_status=current_status, reported_by=reported_by, incident_date=report_date )
        report.save()
        message = "Report Sent!"
        return render(request,"daycare_admin/report.html",{'message':message})
    return render(request,"daycare_admin/report.html")

def viewparent(request):
    all_parents = ParentRegister.objects.all()
    

    return render(request,"daycare_admin/viewparent.html",{"all_parents":all_parents})

def viewpayment(request):

    return render(request,"daycare_admin/viewpayment.html")

def viewfeedback(request):
    all_feedback = ParentFeedback.objects.all()


    return render(request,"daycare_admin/viewfeedback.html",{"all_feedback":all_feedback})




