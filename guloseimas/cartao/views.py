from django.shortcuts import render
from django.http import HttpResponse
from .models import Cartao
from balas.models import Bala

def consultar_saldo(request):
  return render(request, 'consultar_saldo.html')

def consultar_saldo2(request):
  return HttpResponse("<input value=\"sucesso\">")

def alterar_saldo(request):
  return render(request, 'core/registo.html')

def alterar_saldo2(request):
  codigo = request.POST['codigo']
  saldo = request.POST['saldo']
  response = ""
  try:
    cartao = Cartao.objects.get(codigo=codigo)
    if(float(cartao.saldo) - float(saldo)>=0 and desconto_balas(float(saldo))):
      cartao.saldo = float(cartao.saldo) - float(saldo)
      cartao.save()
      response="<input value=\"sucesso\">"
    else:
      response="<input value=\"falha\">"
  except:
    response += "<input value=\"inexistente\">"
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

def mostrar_cartoes(request):
  cartoes = Cartao.objects.all()
  response = ""
  for cartao in cartoes:
    response += cartao.codigo
    response += "<br>"
    response += str(cartao.saldo)
    response += "<br><br>"
  return HttpResponse(response)

def cadastro_cartao(request):
  codigo = request.POST['codigo']
  try:
    cartao = Cartao.objects.get(codigo=codigo)
    return HttpResponse("Cartão já cadastrado")
  except:
    cartao = Cartao(codigo=codigo, saldo=0)
    cartao.save()
    return HttpResponse("Sucesso!")

def cadastrar_cartao(request):
  return render(request, 'cadastrar_cartao.html')
