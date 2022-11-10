from django.shortcuts import render, HttpResponse
from datetime import datetime
from sample.models import contact
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request, "index.html")

def employee_details(request):
    return render(request, "employee_details.html")

def contact_us(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        abc = contact(name=name, email=email, phone=phone, date=datetime.today())
        abc.save()
        messages.success(request, 'Your Detailes has been submitted!')
    return render(request, "contact_us.html")


def accepted(request):
    return render(request, "accepted.html")

def rejected(request):
    return render(request, "rejected.html")

