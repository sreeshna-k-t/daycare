from django.shortcuts import render,redirect
from common.models import *
from daycare_admin.models import *
from .models import *
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
        cereal_notes = request.POST['cereal_notes']
        protein_notes = request.POST['protein_notes']
        fruit_notes = request.POST['fruit_notes']
        dairy_notes = request.POST['dairy_notes']
        
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
        cereal_dict["notes"] = cereal_notes
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
        protein_dict["notes"] = protein_notes
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
        fruit_dict["notes"] = fruit_notes
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
        dairy_dict["notes"] = dairy_notes
        all_dairys.append(dairy_dict)

        if nutrition_check:
            Nutritions.objects.filter(id=id).update(cereals=cereal_dict,proteins=protein_dict,fruits=fruit_dict,dairy=dairy_dict)
            return redirect("daycare_staff:viewprofile")
        else:
            nutrition = Nutritions(child_fk=child_fk,cereals=cereal_dict,proteins=protein_dict,fruits=fruit_dict,dairy=dairy_dict)
            nutrition.save()
            return redirect("daycare_staff:viewprofile")
        
    return render(request, "daycare_staff/nutritions.html")
