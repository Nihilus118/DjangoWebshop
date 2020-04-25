from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.profil),
    path('auth/', include('django.contrib.auth.urls'))
]
