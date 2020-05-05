from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import ListView
from .models import Artikel, Kaesten, Farben, Warenkorb, Bestellungen
from django.http import Http404


def index(request):
    return render(request, 'index.html')


def warenkorb(request):
    if request.user.is_authenticated:
        # Do something for authenticated users.
        context = {
            'artikel_warenkorb': Warenkorb.objects.filter(kundennummer=request.user)
        }
        return render(request, 'warenkorb.html', context=context)
    else:
        # Do something for anonymous users.
        raise Http404(
            "Sie müssen eingeloggt sein um Ihren Warenkorb zu sehen."
        )


def artikel(request):
    context = {
        'artikel_liste': Artikel.objects.all()
    }
    return render(request, 'artikel.html', context=context)


def detail(request, artikel=1):
    context = {
        'artikel': Artikel.objects.get(artikelnr=artikel)
    }
    return render(request, 'detail.html', context=context)


def impressum(request):
    return render(request, 'impressum.html')


def checkout1(request):
    return render(request, 'checkout1.html')


def checkout2(request):
    return render(request, 'checkout2.html')
