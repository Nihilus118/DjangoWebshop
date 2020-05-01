from django.contrib import admin
from .models import Kaesten, Farben, Artikel, Bestellungen, Bestelldetails, Zahlarten, Warenkorb

admin.site.register(Kaesten)
admin.site.register(Farben)
admin.site.register(Zahlarten)
admin.site.register(Artikel)
admin.site.register(Bestellungen)
admin.site.register(Bestelldetails)
admin.site.register(Warenkorb)
