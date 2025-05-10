#from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from apartments.models import ApartmentNew
from django.db.models.functions import Lower

### Function Based Views ###

def home(request):
    #return HttpResponse("Home page")
    return render(request, 'home.html')

###

### Class Based Views ###

class Home(View):

    def get(self, request):
        cities = ApartmentNew.objects.order_by(Lower('city')).values_list('city', flat=True).distinct()
        context = {
            'cities': cities
        }
        return render(request, 'home.html', context)
    
###

### Functions API ###

def get_neighborhoods(request):
    city = request.GET.get('city')
    neighborhoods = ApartmentNew.objects.filter(city=city).values_list('neighborhood', flat=True).distinct()
    neighborhoods_list = list(neighborhoods)
    return JsonResponse({'neighborhoods': neighborhoods_list})
    