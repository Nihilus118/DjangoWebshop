from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('warenkorb/', views.warenkorb, name='warenkorb'),
    path('impressum/', views.impressum, name='impressum'),
    path('artikel/', views.artikel, name='artikel'),
    path('artikel/detail/<int:artikel>', views.detail, name='detail'),
    path('checkout1/', views.checkout1, name='co1'),
    path('checkout2/', views.checkout2, name='co2'),
]
