from django.shortcuts import render
from django.views import View
from apartments.models import Apartment
from reservations.models import Reservation
from django.http import HttpResponse
from apartments.services import get_available_apartments

# Create your views here.

### Function Based Views ###

def apartments_list(request):
    apartments = Apartment.objects.all()
    return render(request, 'apartments_list.html', { 'apartments' : apartments })

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

###

### Class Based Views ###

class ApartmentList(View):

    def get(self, request):
        apartments = self.get_filtered_apartments(request)
        context = {'apartments': apartments}
        return render(request, 'apartments_list.html', context)

    def get_filtered_apartments(self, request):
        ciudad = request.GET.get('ciudad')
        barrio = request.GET.get('distrito')
        fecha_rango = request.GET.get('fecha_rango')

        fechaSplit = fecha_rango.split("to")
        start_date = fechaSplit[0].replace(" ", "")
        end_date = fechaSplit[1].replace(" ", "")

        apartments = Apartment.objects.all()

        if ciudad:
            apartments = apartments.filter(Ciudad__iexact=ciudad)
        if barrio:
            apartments = apartments.filter(Barrio__iexact=barrio)

        if start_date and end_date:
            apartments = apartments.exclude(
                Reservation__StartDate__lt=end_date, #less than
                Reservation__EndDate__gt=start_date #greater than
            )

        return apartments

