from django.shortcuts import render,redirect
from . models import *
from django.http.response import JsonResponse

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
        name = request.POST['regname']
        address = request.POST['regaddress']
        email = request.POST['regemail']
        occupation = request.POST['regoccupation']
        mobileno = request.POST['regnumber']
        username = request.POST['regusername']
        password = request.POST['regpassword']
        userexist = ParentRegister.objects.filter(
            username=username, email_id=email)
        if userexist:
            message = 'Email or Username already exist'
            
        else:
            register = ParentRegister(name=name, address=address, email_id=email,
                                      occupation=occupation, phone_no=mobileno, username=username, password=password)
            register.save()
            print("saved")
           

    return render(request, "parent_registration.html",{'message':message })
