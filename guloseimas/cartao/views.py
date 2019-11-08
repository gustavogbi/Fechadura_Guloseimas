from django.shortcuts import render
from django.http import HttpResponse
from .models import Cartao
from balas.models import Bala
from django.core.mail import send_mail

def consultar_saldo(request):
  return render(request, 'consultar_saldo.html')

def consultar_saldo2(request):
  codigo = request.POST['codigo']
  cartao = Cartao.objects.get(codigo=codigo)
  return HttpResponse("<input value=\"{}\">".format(cartao.saldo))

def alterar_saldo(request):
  return render(request, 'registro.html')

def alterar_saldo2(request):
  nome = request.POST['bala']
  bala = Bala.objects.get(nome=nome)
  codigo = request.POST['codigo']
  response = ""
  try:
    cartao = Cartao.objects.get(codigo=codigo)
    if(float(cartao.saldo) - float(bala.preco) >= 0 and bala.quantidade > 0):
      bala.quantidade -= 1
      bala.save()
      cartao.saldo = float(cartao.saldo) - float(bala.preco)
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




