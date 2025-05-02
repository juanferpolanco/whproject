from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
from users.forms import CustomUserCreationForm

# Create your views here.

# def register_view(request):
#     if request.method == "POST":
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect("apartments:list")
#     else:
#         form = UserCreationForm()
#     return render(request, "register.html", { "form" : form})

def register_view(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("apartments:list")
    else:
        form = CustomUserCreationForm()

    return render(request, "register.html", { "form": form })
