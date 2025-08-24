from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .forms import UserRegistration


# Create your views here.
def register(request):
    if request.method == "POST":
        form = UserRegistration(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, "Your account has been Created")
            return redirect("login")
    else:
        form = UserRegistration()
    return render(request, "accounts/register.html", {"form": form})

@login_required(login_url='login')
def profile(request):
    return render(request, "accounts/profile.html")