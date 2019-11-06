from django.shortcuts import render
from django.http import HttpResponse
from .models import Cartao

def mostrar_cartoes(request):
  codigo = request.POST['codigo']
  saldo = request.POST['saldo']
  cartao = Cartao.objects.get(codigo=codigo)
  response = ""
  if(float(cartao.saldo) - float(saldo)>=0):
    cartao.saldo = float(cartao.saldo) - float(saldo)
    cartao.save()
    response="Sucesso!"
  else:
    response="Saldo Insuficiente"


  return HttpResponse(response)

def bosta(request):

  return render(request, 'core/registo.html')

