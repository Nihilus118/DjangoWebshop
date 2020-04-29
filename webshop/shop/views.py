from django.shortcuts import render, redirect
from django.views.generic import ListView
from .models import Artikel


def index(request):
    return render(request, 'index.html')


def detail(request, artikel=1):
    context = {
        'artikelnr': artikel
    }
    return render(request, 'detail.html', context=context)


def artikel(request):
    context = {
        'artikel_liste': Artikel.objects.all()
    }
    return render(request, 'artikel.html', context=context)
