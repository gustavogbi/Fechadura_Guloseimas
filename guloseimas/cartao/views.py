from django.shortcuts import render
from django.http import HttpResponse
from .models import Cartao

def mostrar_cartoes(request):
  cartoes = Cartao.objects.all()
  response = []
  for cartao in cartoes:
    response.append(cartao)
    response.append("<br>")
    response.append(cartao.saldo)
    response.append("<br>")
  return HttpResponse(response)