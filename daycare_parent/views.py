from django.shortcuts import render, redirect
from django.conf import settings
from .models import *
from daycare_admin.models import *
import datetime
from daycare_staff.models import *
from django.views.generic.base import TemplateView
import stripe
# Create your views here.


def parenthome(request):
    parent = ParentRegister.objects.get(id=request.session['user_id'])

    return render(request, "daycare_parent/parenthome.html", {"parent": parent})


def payment(request):

    return render(request, "daycare_parent/payment.html")
def charge(request):
    if request.method == 'POST':
        stripe.api_key = settings.STRIPE_SECRET_KEY

        try:
            intent = stripe.PaymentIntent.create(
                amount=1099,
                currency='inr',
                payment_method_types=['card'],
            )
        except stripe.error.StripeError as e:
            # Handle error here
            return render(request, 'daycare_parent/error.html', {'message': 'Your card has been declined.'})
    return render(request, "daycare_parent/charge.html")

class ViewPayment(TemplateView):
    template_name = 'daycare_parent/payment.html'

    def get_context_data(self, **kwargs): #new
        context = super().get_context_data(**kwargs)
        context['key'] = settings.STRIPE_PUBLISHABLE_KEY
        return context


def profile(request):
    parent_fk = request.session['user_id']
    all_child = ChildRegister.objects.filter(parent_fk=parent_fk)

    return render(request, "daycare_parent/profile.html", {"all_child": all_child})


def edit_child(request, id):
    child = ChildRegister.objects.get(id=id)
    if request.method == 'POST':
        name = request.POST['childname']
        dob = request.POST['childdob']
        gender = request.POST['childgender']
        height = request.POST['childheight']
        weight = request.POST['childweight']
        medical = request.POST['childmedical']
        dieatry = request.POST['childdieatry']
        pickup = request.POST['childpickup']
        preferences = request.POST['childpreferences']
        ChildRegister.objects.filter(id=id).update(
            name=name,
            # dateofbirth=dob,
            height=height,
            weight=weight,
            gender=gender,
            medical_information=medical,
            dieatry_preferences=dieatry,
            pickup_list=pickup,
            parental_preferences=preferences
        )
        return redirect("daycare_parent:profile")
    return render(request, "daycare_parent/edit_child.html", {"child": child})


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
    user_id = request.session['user_id']
    child = ChildRegister.objects.filter(parent_fk=user_id)
    print(child)
    all_child = []
    for i in child:
        nutritions = Nutritions.objects.get(child_fk=i.id)
        all_child.append(nutritions)
    print(all_child)
    return render(request, "daycare_parent/viewnutritions.html", {"all_child":all_child})


def logout(request):

    del request.session['user_id']
    request.session.flush()
    return redirect('home')
