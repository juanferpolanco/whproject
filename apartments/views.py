from django.shortcuts import render
from . models import Apartment
from django.http import HttpResponse

# Create your views here.

def apartments_list(request):
    apartments = Apartment.objects.all()
    return render(request, 'apartments_list.html', { 'apartments' : apartments })

# def apartment_detail(request, apartment_id):
#     return HttpResponse(apartment_id)

def apartment_detail(request, apartment_id):
    apartment = Apartment.objects.get(id=apartment_id)
    return render(request, 'apartment_detail.html', { 'apartment' : apartment })
