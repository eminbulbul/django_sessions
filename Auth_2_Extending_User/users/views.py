from django.shortcuts import render, redirect, HttpResponse

from django.contrib import messages

from django.contrib.auth import logout, login, authenticate
from .forms import UserForm, UserProfileForm
# Create your views here.


def home(request):
    return render(request, 'users/home.html')


def user_logout(request):
    messages.success(request, 'You logged out!')
    logout(request)
    return redirect('home')


def register(request):
    form_user = UserForm()
    form_profile = UserProfileForm()

    context = {
        "form_user": form_user,
        "form_profile": form_profile,
    }
    return render(request, 'users/register.html', context)
