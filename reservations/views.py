from decimal import Decimal
from django.shortcuts import render, get_object_or_404
from apartments.models import Apartment
from reservations.models import Reservation
from datetime import datetime
from django.contrib.auth.models import User

# Create your views here.

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

    apartment = Apartment.objects.get(id=apartment_id)

    context = {
        'apartment': apartment,
        'date_range': formatted_date_range,
        'email': email,
        'phone': phone,
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