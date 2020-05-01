from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('warenkorb/', views.warenkorb, name='warenkorb'),
    path('artikel/', views.artikel, name='artikel'),
    path('artikel/detail/<int:artikel>', views.detail, name='detail'),
]
