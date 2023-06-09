from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, "daycare_admin/admin_home.html")