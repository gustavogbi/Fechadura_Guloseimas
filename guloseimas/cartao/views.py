from django.shortcuts import render
from django.http import HttpResponse
from .models import Cartao
from balas.models import Bala

def consultar_saldo(request):
  return render(request, 'consultar_saldo.html')

def consultar_saldo2(request):
  codigo = request.POST['codigo']
  cartao = Cartao.objects.get(codigo=codigo)
  return HttpResponse("<input value=\"{}\">".format(cartao.saldo))

def alterar_saldo(request):
  return render(request, 'registro.html')

def alterar_saldo2(request):
  codigo = request.POST['codigo']
  saldo = request.POST['saldo']
  response = ""
  try:
    cartao = Cartao.objects.get(codigo=codigo)
    if(float(cartao.saldo) - float(saldo)>=0 and desconto_balas(float(saldo))):
      cartao.saldo = float(cartao.saldo) - float(saldo)
      cartao.save()
      response="<input value=\"sucesso\" id=\"resultado\">"
    else:
      response="<input value=\"falha\" id=\"resultado\">"
  except:
    response += "<input value=\"inexistente\" id=\"resultado\">"
  return HttpResponse(response)

def desconto_balas(preco):
  try:
    bala = Bala.objects.get(preco=preco)
    if (bala.quantidade > 0):
      bala.quantidade -= 1
      bala.save()
      return True
  except:
    pass
  return False
