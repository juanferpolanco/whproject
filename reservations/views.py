from decimal import Decimal
from django.shortcuts import render, get_object_or_404, redirect
from apartments.models import Apartment, ApartmentNew
from reservations.models import Reservation, ReservationNew
from datetime import datetime
from django.contrib.auth.models import User
from django.views import View
from django.contrib.auth import authenticate, login

# Create your views here.

### Function Based Views ###

# def reservation_detail(request):
#     # apartments = Apartment.objects.all()
#     return render(request, '')

# def reservation_detail(request):
#     if request.method == 'GET':
#         apartment_id = request.GET.get('apartment_id')
#         date_range = request.GET.get('date_range')
#         email = request.GET.get('email')
#         phone = request.GET.get('phone')

#     print(date_range)
#     apartment = Apartment.objects.get(id=apartment_id)

#     context = {
#         'apartment': apartment,
#         'date_range': date_range,
#         'email': email,
#         'phone': phone,
#     }

#     return render(request, 'reservation_detail.html', context)

def reservation_detail(request):
    date_range = request.GET.get('date_range')  # expected format: "YYYY-MM-DD to YYYY-MM-DD"
    formatted_date_range = ""

    if date_range:
        try:
            start_str, end_str = date_range.split(' to ')
            start_date = datetime.strptime(start_str.strip(), '%Y-%m-%d')
            end_date = datetime.strptime(end_str.strip(), '%Y-%m-%d')

            if start_date.month == end_date.month:
                formatted_date_range = f"{start_date.day} - {end_date.day} {end_date.strftime('%b')}"
            else:
                formatted_date_range = f"{start_date.day} {start_date.strftime('%b')} - {end_date.day} {end_date.strftime('%b')}"
        except Exception as e:
            formatted_date_range = date_range  

    apartment_id = request.GET.get('apartment_id')
    email = request.GET.get('email')
    phone = request.GET.get('phone')

    # apartment = Apartment.objects.get(id=apartment_id)
    apartment = ApartmentNew.objects.get(id=apartment_id)
    first_picture_url = apartment.first_picture

    context = {
        'apartment': apartment,
        'date_range': formatted_date_range,
        'email': email,
        'phone': phone,
        'first_picture': first_picture_url
    }

    return render(request, 'reservation_detail.html', context)

def create_reservation(request):
    if request.method == 'GET':
        apartment_id = request.GET.get('apartment_id')
        # user_id = request.GET.get('user_id') 
        user_id = 1
        date_range = request.GET.get('date_range')
        total_price = 10.23

        if apartment_id and user_id and date_range and total_price:
            try:
                apartment = get_object_or_404(Apartment, id=apartment_id)
                user = get_object_or_404(User, id=user_id)

                start_str, end_str = date_range.split(' to ')
                start_date = datetime.strptime(start_str.strip(), '%Y-%m-%d').date()
                end_date = datetime.strptime(end_str.strip(), '%Y-%m-%d').date()

                reservation = Reservation(
                    Apartment=apartment,
                    User=user,
                    StartDate=start_date,
                    EndDate=end_date,
                    TotalPrice=Decimal(total_price)
                )
                reservation.save()

                return render(request, 'home.html')

            except Exception as e:
                return render(request, 'home.html')

    return render(request, 'home.html')

###

### Class Based Views ###

class ReservationView(View):
    errors = None
    def get(self, request):
        apartment_id = request.GET.get('apartment_id')
        date_range = request.GET.get('date_range')

        apartment = get_object_or_404(ApartmentNew, id=apartment_id)
        first_picture_url = apartment.first_picture

        context = {
            'apartment': apartment,
            'date_range': date_range,
            'first_picture': first_picture_url,
            'errors' : self.errors
        }

        return render(request, 'reservation_detail.html', context)

    def post(self, request):
        apartment_id = request.POST.get('apartment_id')
        date_range = request.POST.get('date_range')
        total_price = request.POST.get('total_price')

        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        nationality = request.POST.get('nationality')
        country_code = request.POST.get('country_code')
        phone = request.POST.get('phone')
        birthdate = request.POST.get('birthdate')

        if not request.user.is_authenticated:
            if not User.objects.filter(username=email).exists():
                user = User.objects.create_user(username=email, email=email, password=password)
                user.first_name = full_name
                user.save()
            else:
                user = User.objects.get(username=email)

            authenticated_user = authenticate(request, username=email, password=password)
            if authenticated_user:
                login(request, authenticated_user)
        else:
            user = request.user

        try:
            apartment = get_object_or_404(ApartmentNew, id=apartment_id)

            start_str, end_str = date_range.split(' to ')
            start_date = datetime.strptime(start_str.strip(), '%Y-%m-%d').date()
            end_date = datetime.strptime(end_str.strip(), '%Y-%m-%d').date()

            ReservationNew.objects.create(
                apartment=apartment,
                user=user,
                start_date=start_date,
                end_date=end_date,
                total_price=Decimal(total_price),
                full_name=full_name,
                nationality=nationality,
                country_code=country_code,
                phone=phone,
                birthdate=birthdate
            )

            return redirect('home')

        except Exception as e:
            print("Error al guardar la reserva:", e)

            self.errors = str(e)

            return self.get(request)
            