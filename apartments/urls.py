from django.contrib import admin
from django.urls import path
from . import views

app_name = 'apartments'

urlpatterns = [
    path('', views.apartments_list, name="list"),
    # path('<slug:apartment_name>', views.apartment_detail, name="detail")
    path('<int:apartment_id>', views.apartment_detail, name="detail")
]
