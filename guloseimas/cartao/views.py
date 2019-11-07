from django.shortcuts import render
from django.http import HttpResponse
from .models import Cartao

def alterar_saldo2(request):
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

def mostrar_cartoes(request):
  cartoes = Cartao.objects.all()
  response = ""
  for cartao in cartoes:
    response += cartao.codigo
    response += "<br>"
    response += str(cartao.saldo)
    response += "<br><br>"
  return HttpResponse(response)

def alterar_saldo(request):
  return render(request, 'core/registo.html')

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
