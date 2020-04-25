from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('detail/<int:artikel>', views.detail, name='detail'),
]
