from django.urls import path
from . import views

urlpatterns = [
    path('', views.mostrar_cartoes, name='mostrar_cartoes'),
]
