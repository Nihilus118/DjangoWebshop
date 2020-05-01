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
    zahlvorgang = models.IntegerField(default=0)
    zahlart = models.ForeignKey(
        Zahlarten,
        default=1,
        on_delete=models.DO_NOTHING
    )

    def __str__(self):
        return str(self.bestellnummer)


class Bestelldetails(models.Model):
    bestellnummer = models.ForeignKey(
        Bestellungen,
        on_delete=models.DO_NOTHING
    )
    artikel = models.ForeignKey(
        Artikel,
        on_delete=models.DO_NOTHING
    )
    menge = models.IntegerField()
    einzelpreis = models.FloatField()

    def __str__(self):
        return str(self.artikel + " " + self.menge)


class Warenkorb(models.Model):
    kundennummer = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    artikel = models.ForeignKey(
        Artikel,
        on_delete=models.DO_NOTHING
    )
    menge = models.IntegerField()

    def __str__(self):
        return str(self.kundennummer) + " - " + self.artikel.artikelname + " x " + str(self.menge)
