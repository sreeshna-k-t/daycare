from django.shortcuts import render,redirect
from . models import *
from django.http.response import JsonResponse
import json
from datetime import datetime

# Create your views here.


def home(request):

    return render(request, "home.html")


def login(request):
    msg = ''
    if request.method == 'POST':
        username = request.POST['log_username']
        password = request.POST['log_password']

        user_exist = ParentRegister.objects.filter(
            username=username, password=password).exists()
        
        if user_exist:
            user_detail = ParentRegister.objects.get(
                username=username, password=password)
            request.session['user_id'] = user_detail.id
            print("working1")
            return redirect("daycare_parent:parenthome")
        else:
            print("working2")
            msg = 'invalid username or password'
            return render(request, 'login.html', {'err_msg': msg, })
    return render(request, 'login.html', {'err_msg': msg, })
    


def about(request):

    return render(request, "about.html")


def services(request):

    return render(request, "services.html")



def parent_registration(request):
    message = ""
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        address = request.POST.get('address')
        email = request.POST.get('email_id')
        occupation = request.POST.get('occupation')
        mobileno = request.POST.get('phone_no')
        username = request.POST.get('username')
        gender = request.POST.get('gender')
        password = request.POST.get('password')
        child_details = request.POST.get('child_details[]')
        child_data = json.loads(child_details)
        userexist = ParentRegister.objects.filter(
            username=username, email_id=email)
        if userexist:
            message = 'Email or Username already exist'
            
        else:
            register = ParentRegister(name=first_name,last_name=last_name, address=address, email_id=email,
                                      occupation=occupation, phone_no=mobileno, username=username,gender=gender, password=password)
            register.save()
            parent_fk = ParentRegister.objects.get(username=username,password=password)
            print("working1")
            for child in child_data:
                dob = datetime.strptime(child['dateofbirth'], '%Y-%m-%d').date()
                print(dob)
                child_register = ChildRegister(parent_fk=parent_fk,name=child['name'],dateofbirth=dob,height=int(child['height']),weight=int(child['weight']),gender=child['gender'],medical_information=child['medical_information'],dieatry_preferences=child['dieatry'],pickup_list=child['pickup_list'],parental_preferences=child['parental_preferences'])
                child_register.save()
                print("child saved")
                
            print("saved")
            return redirect("child_registration")
           

    return render(request, "parent_registration.html",{'message':message })

def child_registration(request):
    return render(request, "child_register.html")