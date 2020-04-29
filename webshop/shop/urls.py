from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('artikel/', views.artikel, name='artikel'),
    path('detail/<int:artikel>', views.detail, name='detail'),
]
