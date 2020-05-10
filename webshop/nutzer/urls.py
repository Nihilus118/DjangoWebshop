from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.profil, name='profil'),
    path('auth/', include('django.contrib.auth.urls')),
    path('auth/registrieren/', views.registrieren, name="registrieren")
]
