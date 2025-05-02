from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def register_view(request):
    form = UserCreationForm()
    return render(request, "register.html", { "form" : form})
