from django.urls import path
from . import views

app_name="cartao"

urlpatterns = [
    path('cartao/', views.mostrar_cartoes, name='mostrar_cartoes'),
    path('bosta/', views.bosta, name='bosta'),
    path('cadastrar_cartao/', views.cadastrar_cartao, name='cadastrar_cartao'),
    path('cadastro_cartao/', views.cadastro_cartao, name='cadastro_cartao')
]
