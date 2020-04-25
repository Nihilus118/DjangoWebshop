from django.db import models
from django.contrib.auth.models import User


class Kaesten(models.Model):
    beschreibung = models.CharField(max_length=150)
    groesse = models.CharField(max_length=50)
    verfuegbar = models.BooleanField(default=True)

    def __str__(self):
        return self.beschreibung


class Farben(models.Model):
    name = models.CharField(max_length=30)
    verfuegbar = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Artikel(models.Model):
    artikelnr = models.IntegerField(primary_key=True, auto_created=True)
    artikelname = models.CharField(max_length=50)
    preis = models.FloatField()
    menge = models.IntegerField()
    groesse_kasten = models.ForeignKey(
        Kaesten,
        default=1,
        on_delete=models.DO_NOTHING
    )
    farbe_kasten = models.ForeignKey(
        Farben,
        default=1,
        on_delete=models.DO_NOTHING
    )

    def __str__(self):
        return self.artikelname


class Zahlarten(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Bestellungen(models.Model):
    bestellnummer = models.IntegerField(primary_key=True, auto_created=True)
    kundennummer = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    bestelldatum = models.DateTimeField(auto_now_add=True)
    stadt = models.CharField(max_length=30)
    strasse = models.CharField(max_length=50)
    hausnummer = models.CharField(max_length=5)
    bezahlt = models.BooleanField(default=True)
    zahlart = models.ForeignKey(
        Zahlarten,
        default=1,
        on_delete=models.DO_NOTHING
    )
    zahldatum = models.DateTimeField()
    kasten = models.ForeignKey(Kaesten, on_delete=models.DO_NOTHING)
    farbe = models.ForeignKey(Farben, on_delete=models.DO_NOTHING)

    def __str__(self):
        return str(self.bestellnummer)
