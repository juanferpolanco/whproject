from django.shortcuts import render
from apartments.models import Apartment
from django.http import HttpResponse
from apartments.services import get_available_apartments

# Create your views here.

def apartments_list(request):
    apartments = Apartment.objects.all()
    return render(request, 'apartments_list.html', { 'apartments' : apartments })

# def apartment_detail(request, apartment_id):
#     return HttpResponse(apartment_id)

def apartment_detail(request, apartment_id):
    apartment = Apartment.objects.get(id=apartment_id)
    return render(request, 'apartment_detail.html', { 'apartment' : apartment })

def available_apartments_list(request):
    ciudad = request.GET.get('ciudad')
    distrito = request.GET.get('distrito')
    fecha_rango = request.GET.get('fecha_rango')
    adultos = request.GET.get('adultos')
    ninos = request.GET.get('ninos')
    mascotas = request.GET.get('mascotas')
    
    fechaSplit = fecha_rango.split("to")
    start_date = fechaSplit[0].replace(" ", "")
    end_date = fechaSplit[1].replace(" ", "")

    #print(start_date, end_date)

    apartments = get_available_apartments(start_date, end_date, ciudad, distrito)
    
    return render(request, 'apartments_list.html', {'apartments': apartments})
