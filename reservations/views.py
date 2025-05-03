from django.shortcuts import render
# from . models import Apartment
# from django.http import HttpResponse

# Create your views here.

def reservation_detail(request):
    # apartments = Apartment.objects.all()
    return render(request, 'reservation_detail.html')
