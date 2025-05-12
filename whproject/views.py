#from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from apartments.models import ApartmentNew, ApartmentCity, ApartmentNeighborhood
from django.db.models.functions import Lower

### Function Based Views ###

def home(request):
    #return HttpResponse("Home page")
    return render(request, 'home.html')

###

### Class Based Views ###

class Home(View):

    def get(self, request):
        # cities = ApartmentNew.objects.order_by(Lower('city')).values_list('city', flat=True).distinct()
        cities = ApartmentCity.objects.order_by('name')
        context = {
            'cities': cities
        }
        return render(request, 'home.html', context)
    
###

### Functions API ###

# def get_neighborhoods(request):
#     city = request.GET.get('city')
#     neighborhoods = ApartmentNew.objects.filter(city=city).values_list('neighborhood', flat=True).distinct()
#     neighborhoods_list = list(neighborhoods)
#     return JsonResponse({'neighborhoods': neighborhoods_list})
def get_neighborhoods(request):
    city_id = request.GET.get('city_id')
    if not city_id:
        return JsonResponse({'neighborhoods': []})
    
    neighborhoods = ApartmentNeighborhood.objects.filter(city_id=city_id).values_list('name', flat=True).distinct()
    return JsonResponse({'neighborhoods': list(neighborhoods)})
    