from django.shortcuts import render,redirect
from common.models import *
from daycare_admin.models import *
from .models import *
# from celery import task
from datetime import date
from django.core.mail import send_mail
from .models import ChildRegister
# Create your views here.


def staffhome(request):

    return render(request, "daycare_staff/staffhome.html")


def viewprofile(request):
    view_child = ChildRegister.objects.all()
    print(view_child)
    return render(request, "daycare_staff/viewprofile.html", {"all_child": view_child})


def attendance(request):

    return render(request, "daycare_staff/attendance.html")


def nutritions(request, id):
    if request.method == 'POST':
        print("workint 1")
        cereals = request.POST.getlist('cereals[]')
        proteins = request.POST.getlist('proteins[]')
        fruits = request.POST.getlist('fruits[]')
        dairys = request.POST.getlist('dairy[]')
        notes = request.POST['notes']
        # protein_notes = request.POST['protein_notes']
        # fruit_notes = request.POST['fruit_notes']
        # dairy_notes = request.POST['dairy_notes']
        
        nutrition_check = Nutritions.objects.filter(id=id).first()
        child_fk = ChildRegister.objects.get(id=id)
    

        # Cereal
        all_cereals = []
        cereal_dict = {}
        cereal_nutrition = []
        for cereal in cereals:
            cereal_data = {}
            quantity_key = cereal + '_quantity'
            quantity = request.POST[quantity_key]
            print(cereal, quantity)
            cereal_data["cereal"] = cereal
            cereal_data["quantity"] = quantity
            cereal_nutrition.append(cereal_data)

        cereal_dict["cereal"] = cereal_nutrition
        
        all_cereals.append(cereal_dict)
        
        # Protins
        all_protins = []
        protein_dict = {}
        protein_nutrition = []
        for protein in proteins:
            protein_data = {}
            protin_data = {}
            quantity_key = protein + '_quantity'
            quantity = request.POST[quantity_key]
            print(protein, quantity)
            protin_data["quantity"] = quantity
            protin_data["protein"] = protein
            protein_nutrition.append(protin_data)

        protein_dict["protein"] = protein_nutrition
        # protein_dict["notes"] = protein_notes
        all_protins.append(protein_dict)

        # Fruits
        all_fruits = []
        fruit_dict = {}
        fruit_nutrition = []
        for fruit in fruits:
            fruit_data = {}
            quantity_key = fruit + '_quantity'
            quantity = request.POST[quantity_key]
            print(fruit, quantity)
            fruit_data["quantity"] = quantity
            fruit_data["fruit"] = fruit
            fruit_nutrition.append(fruit_data)
        fruit_dict["fruit"] = fruit_nutrition
        # fruit_dict["notes"] = fruit_notes
        all_fruits.append(fruit_dict)

        # Dairy
        all_dairys = []
        dairy_dict = {}
        dairy_nutrition = []
        for dairy in dairys:
            dairy_data = {}
            quantity_key = dairy + '_quantity'
            quantity = request.POST[quantity_key]
            print(dairy, quantity)
            dairy_data["quantity"] = quantity
            dairy_data["dairy"] = dairy
            dairy_nutrition.append(dairy_data)
        dairy_dict["dairy"] = dairy_nutrition
        # dairy_dict["notes"] = dairy_notes
        all_dairys.append(dairy_dict)

        if nutrition_check:
            Nutritions.objects.filter(id=id).update(cereals=cereal_dict,proteins=protein_dict,fruits=fruit_dict,dairy=dairy_dict,notes=notes)
            return redirect("daycare_staff:viewprofile")
        else:
            nutrition = Nutritions(child_fk=child_fk,cereals=cereal_dict,proteins=protein_dict,fruits=fruit_dict,dairy=dairy_dict,notes=notes)
            nutrition.save()
            return redirect("daycare_staff:viewprofile")
        
    return render(request, "daycare_staff/nutritions.html")

def vaccination():
    # def send_vaccination_alerts():
    # Get the current date
    current_date = date.today()

    # Fetch children whose vaccination is due on the current date
    children = ChildRegister.objects.all()

    for child in children:
        # Calculate the child's age in months
        age_in_months = (current_date.year - child.date_of_birth.year) * 12 + (current_date.month - child.date_of_birth.month)

        # Get the recommended vaccinations for the child's age from the vaccination schedule
        recommended_vaccinations = get_recommended_vaccinations(age_in_months)

        # Send vaccination alerts to parent emails
        if recommended_vaccinations:
            subject = 'Vaccination Alert for {}'.format(child.name)
            message = 'Dear {}, your child {} is due for the following vaccinations: {}. Please make arrangements accordingly.'.format(
                child.parent_name, child.name, ', '.join(recommended_vaccinations))
            from_email = 'your@email.com'
            recipient_list = [child.parent_email]

            send_mail(subject, message, from_email, recipient_list)

# utils.py
def get_recommended_vaccinations(age_in_months):
    # Implement your vaccination schedule logic here to return a list of recommended vaccinations based on the child's age
    # Example: vaccination_schedule = {2: ['Vaccine A'], 6: ['Vaccine B', 'Vaccine C']}
    vaccination_schedule = {
        2: ['Vaccine A'],
        6: ['Vaccine B', 'Vaccine C']
    }
    
    return vaccination_schedule.get(age_in_months, [])

    # return render(request, "daycare_staff/vaccination.html")
