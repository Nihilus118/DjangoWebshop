from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from .forms import RegistrationForm


# Create your views here.

def profil(request):
    return render(request, 'profil.html')


def registrieren(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(
                username=username,
                password=password
            )
            login(request, user)
            return redirect(profil)
    else:
        form = RegistrationForm()

    context = {
        'form': form
    }

    return render(request, 'registration/registrieren.html', context)
