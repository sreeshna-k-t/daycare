from django.shortcuts import render
from common.models import *
from daycare_parent.models import * 
from .models import * 
from  daycare_admin.models import *
from django.core.mail import send_mail
from django.conf import settings
import stripe


# Create your views here.
from django.views.generic.base import TemplateView

stripe.api_key = settings.STRIPE_SECRET_KEY


def adminhome(request):
    
    return render(request,"daycare_admin/admin_home.html")

def staff_registration(request):
    msg = ""
    if request.method == "POST":
        staffname = request.POST["staff_name"]
        staffaddress = request.POST["staff_address"]
        staffemail = request.POST["staff_email_id"]
        staffdob = request.POST["staff_dob"]
        staffgender = request.POST["staff_gender"]
        staffqualification =request.POST["staff_qualification"]
        staffphone = request.POST["staff_mobile_no"]
        staffusername = request.POST["staff_username"]
        staffpassword = request.POST["staff_password"]
        staff_exist = StaffRegistration.objects.filter(staff_email_id=staffemail)
        username_exist = StaffRegistration.objects.filter(staff_username=staffusername)
        if staff_exist:
            msg = "Email already exist"
        elif username_exist:
            msg = "Username already exist"

        else:
        
            staffreg = StaffRegistration(staff_name=staffname,staff_address=staffaddress,
                                        staff_email_id=staffemail,staff_dob=staffdob,staff_gender=staffgender,staff_qualification=staffqualification,
                                        staff_mobile_no=staffphone,
                                        staff_username=staffusername,staff_password=staffpassword)
            subject = "Calicut University Daycare Staff Registration"
            message = f"Hi {staffname}, \n\nYour Daycare login credentials is, \n\nUsername : {staffusername} \nPassword : {staffpassword} \n\nRegards \nDaycare Team"
            email_from = settings.EMAIL_HOST_USER
            email_to = [staffemail]
            send_mail(subject, message, email_from, email_to)
            staffreg.save()
            msg = "Staff Registration Successful"
        return render(request,"daycare_admin/staff_registration.html", {"message":msg})

    return render(request,"daycare_admin/staff_registration.html")
    

def report(request):
    
    if request.method == "POST":
        child_name = request.POST["child_name"]
        parent_email_id = request.POST["parent_email_id"]
        description = request.POST["description"]
        current_status = request.POST["current_status"]
        report_date = request.POST["report_date"]
        parent_fk = ParentRegister.objects.filter(email_id=parent_email_id).first()
        print(parent_fk)
        if parent_fk is not None:
            report = IncidentReport(parent_fk=parent_fk,child_name=child_name, parent_email_id=parent_email_id, description=description, current_status=current_status,incident_date=report_date )
            report.save()
            message = "Report Sent!"
        else:
            message = "Please enter registered email address of the parent "
        return render(request,"daycare_admin/report.html",{'message':message})
    return render(request,"daycare_admin/report.html")

def viewparent(request):
    all_parents = ParentRegister.objects.all()
    

    return render(request,"daycare_admin/viewparent.html",{"all_parents":all_parents})

def viewchild(request, id):
    view_child = ChildRegister.objects.filter(parent_fk=id)
    print(view_child)
    return render(request,"daycare_admin/viewchild.html",{"all_child":view_child})

def viewpayment(request):

    return render(request,"daycare_admin/viewpayment.html")

def viewfeedback(request):
    all_feedback = ParentFeedback.objects.all()


    return render(request,"daycare_admin/viewfeedback.html",{"all_feedback":all_feedback})


def charge(request): #new
    if request.method == 'POST':
        charge = stripe.Charge.create(
            amount=500,
            currency='inr',
            description='Payment Gateway',
            source=request.POST['stripeToken']
        )
        return render(request,'charge.html')

