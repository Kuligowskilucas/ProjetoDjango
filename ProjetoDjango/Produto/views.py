from django.shortcuts import render, redirect
from .models import Produto

def home(request):
    produtos = Produto.objects.all()
    return render(request, "produto.html", {"produtos": produtos})

def salvarProduto(request):
    Vdescricao = request.POST.get("descricao")
    Vquantidade = request.POST.get("quantidade")
    VvalorUnitario = request.POST.get("valorUnitario")
    Produto.objects.create(descricao=Vdescricao, quantidade=Vquantidade, valorUnitario=VvalorUnitario)
    produtos = Produto.objects.all()
    return render(request, "produto.html", {"produtos": produtos})

def editarProduto(request, id):
    produtos = Produto.objects.get(id=id)
    return render(request, "updateProduto.html", {"produtos": produtos})

def updateProduto(request, id):
    Vdescricao = request.POST.get("descricao")
    Vquantidade = request.POST.get("quantidade")
    VvalorUnitario = request.POST.get("valorUnitario")
    produtos = Produto.objects.get(id=id)
    produtos.descricao = Vdescricao
    produtos.quantidade = Vquantidade
    produtos.valorUnitario = VvalorUnitario
    produtos.save()
    return redirect(home)

def deleteProduto(request, id):
    produtos = Produto.objects.get(id=id)
    produtos.delete()
    return redirect(home)
