from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('designer/', views.designer, name='designer'),
    path('artikel/', views.artikel, name='artikel'),
    path('artikel/detail/<int:artikel>', views.detail, name='detail'),
]
