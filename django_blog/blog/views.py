from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .forms import UserRegistration,UserUpdateForm,ProfileUpdateForm
from .models import Profile


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


def prof(request):
    return render(request, "accounts/profile.html")
def profile(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        print(f" user : {u_form.errors}, profile : {p_form.errors}")
        if u_form.is_valid() and p_form.is_valid():
            print("checked")
            u_form.save()
            p_form.save()
            return redirect('login')
    else:
        print("not checked")
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    return render(request, "accounts/profiles.html", {'u_form': u_form, 'p_form':p_form})

def betterRegister(request):
        if request.method == "POST":
            form = UserRegistration(request.POST)
            if form.is_valid():
                user = form.save()
                messages.success(request, "Your account has been Created")
                return redirect("login")
        else:
            form = UserRegistration()
        return render(request, "accounts/register.html", {"form": form})


