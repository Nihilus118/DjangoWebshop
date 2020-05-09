from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import ListView
from .models import Artikel, Kaesten, Farben, Warenkorb, Bestellungen, Warenkorb, Bestelldetails
from django.db.models import Sum
from django.http import Http404
from django.http.response import JsonResponse
import json


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
        'artikel': Artikel.objects.get(artikelnummer=artikel)
    }
    return render(request, 'detail.html', context=context)


def impressum(request):
    return render(request, 'impressum.html')


def checkout1(request):
    if request.user.is_authenticated:
        artikel_list = Warenkorb.objects.filter(kundennummer=request.user)

        # Gesamtpreis des Warenkorbs
        warenkorb_gesamt = 0
        for pos in artikel_list:
            warenkorb_gesamt += pos.artikel.preis * pos.menge

        context = {
            'artikel_warenkorb': artikel_list,
            'gesamtpreis_warenkorb': warenkorb_gesamt
        }
        return render(request, 'checkout1.html', context=context)
    else:
        # Do something for anonymous users.
        raise Http404(
            "Sie müssen eingeloggt sein um diese Seite zu sehen."
        )


def checkout2(request):
    if request.user.is_authenticated:
        # Daten aus Request laden
        body = json.loads(request.body)
        print('BODY', body)

        # Bestellung in System
        best = Bestellungen.objects.create(
            kundennummer=request.user,
            # TODO: Werte von PP aus body
            ort="Aus Body",
            plz="Aus Body",
            strasseHausnummer="Aus Body",
            adresszusatz="Aus Body",
            zahlvorgang="PAYPAL-Process ID"
        )

        # Artikel aus Warenkorb
        artikel_list = Warenkorb.objects.filter(kundennummer=request.user)

        # Bestellpositionen in System
        for pos in artikel_list:
            Bestelldetails.objects.create(
                bestellnummer=best.bestellnummer,
                artikel=pos["artikelnummer"],
                menge=pos["menge"],
                einzelpreis=pos["Artikel"]["preis"]
            )

        # Warenkorb leeren
        artikel_list = Warenkorb.objects.filter(
            kundennummer=request.user).delete()

        return JsonResponse('Bezahlvorgang erfolgreich!', safe=False)
    else:
        # Do something for anonymous users.
        raise Http404(
            "Sie müssen eingeloggt sein um diese Seite zu sehen."
        )
