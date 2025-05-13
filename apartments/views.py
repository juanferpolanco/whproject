from django.db import connection
from django.shortcuts import get_object_or_404, render
from django.views import View
from django.db.models import Prefetch
from apartments.models import Apartment, ApartmentNew, ApartmentPicture
from reservations.models import ReservationNew
# from django.http import HttpResponse
from apartments.services import get_available_apartments

# Create your views here.

### Function Based Views ###

def apartments_list(request):
    apartments = Apartment.objects.all()
    return render(request, 'apartments_list.html', { 'apartments' : apartments })

def apartment_detail(request, apartment_id):
    # apartment = Apartment.objects.get(id=apartment_id)
    # apartment = ApartmentNew.objects.get(id=apartment_id)
    # return render(request, 'apartment_detail.html', { 'apartment' : apartment })
    apartment = get_object_or_404(ApartmentNew, id=apartment_id)
    pictures = list(apartment.pictures.order_by('id')[:3])  # force evaluate

    photo1 = pictures[0].url if len(pictures) > 0 else None
    photo2 = pictures[1].url if len(pictures) > 1 else None
    photo3 = pictures[2].url if len(pictures) > 2 else None

    context = {
        'apartment': apartment,
        'photo1': photo1,
        'photo2': photo2,
        'photo3': photo3
    }

    reponse = render(request, 'apartment_detail.html', context)

    print(len(connection.queries))
    return reponse
    # return render(request, 'apartment_detail.html', context)

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
        reponse = render(request, 'apartments_list.html', context)

        print(len(connection.queries))
        return reponse

    def get_filtered_apartments(self, request):
        ciudad = request.GET.get('ciudad')
        barrio = request.GET.get('distrito')
        fecha_rango = request.GET.get('fecha_rango')
        adultos = request.GET.get('adultos')
        ninos = request.GET.get('ninos')

        apartments = ApartmentNew.objects.prefetch_related(
            Prefetch('pictures', queryset=ApartmentPicture.objects.order_by('id')),
            Prefetch('reservations_new', queryset=ReservationNew.objects.all())
        ).filter(active=True)
        # ).all()

        if ciudad and ciudad != 'All Cities':
            apartments = apartments.filter(city__iexact=ciudad)
        if barrio:
            apartments = apartments.filter(neighborhood__iexact=barrio)
        if adultos or ninos:
            apartments = apartments.filter(accommodates__gte=int(adultos)+int(ninos))

        if fecha_rango:
            start_date, end_date = [d.strip() for d in fecha_rango.split('to')]
            apartments = apartments.exclude(
                reservations_new__start_date__lt=end_date,
                reservations_new__end_date__gt=start_date
            )

        return apartments[:20]

