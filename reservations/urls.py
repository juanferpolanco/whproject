from django.contrib import admin
from django.urls import path
from . import views

app_name = 'reservations'

urlpatterns = [
    path('detail/', views.reservation_detail, name='detail'),
    # path('<int:apartment_id>', views.apartment_detail, name='detail')
]