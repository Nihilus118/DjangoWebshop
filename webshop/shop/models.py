from django.db import models

# Create your models here.


class Artikel(models.Model):
    artikelnr = models.IntegerField(primary_key=True, auto_created=True)
    artikelname = models.CharField(max_length=50)
    preis = models.FloatField()
    menge = models.IntegerField()
