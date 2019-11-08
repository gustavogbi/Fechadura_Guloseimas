from django.urls import path
from . import views

app_name="cartao"

urlpatterns = [
    path('cartao/', views.mostrar_cartoes, name='mostrar_cartoes'),
    path('alterar_saldo/', views.alterar_saldo, name='alterar_saldo'),
    path('alterar_saldo2/', views.alterar_saldo2, name='alterar_saldo2'),
    path('cadastrar_cartao/', views.cadastrar_cartao, name='cadastrar_cartao'),
    path('cadastro_cartao/', views.cadastro_cartao, name='cadastro_cartao'),
    path('consultar_saldo/', views.consultar_saldo, name='consultar_saldo'),
    path('consultar_saldo2/', views.consultar_saldo2, name='consultar_saldo2'),
]
