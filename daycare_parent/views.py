from django.shortcuts import render, redirect
from .models import *
from daycare_admin.models import *
import datetime

# Create your views here.


def parenthome(request):
    parent = ParentRegister.objects.get(id=request.session['user_id'])

    return render(request, "daycare_parent/parenthome.html", {"parent": parent})


def payment(request):

    return render(request, "daycare_parent/payment.html")


def profile(request):

    return render(request, "daycare_parent/profile.html")


def feedback(request):

    if request.method == "POST":
        feed_description = request.POST["feed_description"]
        user_id = request.session["user_id"]
        parent_fk = ParentRegister.objects.get(id=user_id)
        feed_date = datetime.datetime.now()
        feedback = ParentFeedback(
            parent_fk=parent_fk, feed_description=feed_description, feed_date=feed_date)
        feedback.save()
        message = "Thank you for submitting feedback!"
        return render(request, "daycare_parent/feedback.html", {"message": message})
    return render(request, "daycare_parent/feedback.html")


def viewreport(request):

    parent_id = request.session['user_id']

    reports = IncidentReport.objects.filter(parent_fk=parent_id)

    return render(request, "daycare_parent/viewreport.html", {"reports": reports})


def viewattendance(request):

    return render(request, "daycare_parent/viewattendance.html")


def viewnutritions(request):

    return render(request, "daycare_parent/viewnutritions.html")


def logout(request):

    del request.session['user_id']
    request.session.flush()
    return redirect('home')
