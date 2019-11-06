from django.shortcuts import render
from django.http import HttpResponse
from .models import Cartao

def mostrar_cartoes(request):
  cartoes = Cartao.objects.all()
  response = ""
  for cartao in cartoes:
    cartao.saldo = 10.00
    cartao.save()
    response += cartao.codigo
    response += "<br>"
    response += str(cartao.saldo)
    response += "<br>"
  return HttpResponse(response)

