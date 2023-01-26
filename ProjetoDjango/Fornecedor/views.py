from django.shortcuts import render, redirect
from .models import Fornecedor
# Create your views here.


def home(request):
    fornecedores = Fornecedor.objects.all()
    return render(request, "fornecedor.html", {"fornecedores": fornecedores})

def salvarFornecedor(request):
    Vnome = request.POST.get("nome")
    Vendereco = request.POST.get("endereco")
    Vtelefone = request.POST.get("telefone")
    Vcnpj = request.POST.get("cnpj")
    Fornecedor.objects.create(nome=Vnome,endereco=Vendereco,telefone=Vtelefone,cnpj=Vcnpj)
    fornecedores = Fornecedor.objects.all()
    return render(request, "fornecedor.html", {"fornecedores": fornecedores})

def editarFornecedor(request, id):
    fornecedores = Fornecedor.objects.get(id=id)
    return render(request, "updateFornecedor.html", {"fornecedores": fornecedores})

def updateFornecedor(request, id):
    Vnome = request.POST.get("nome")
    Vendereco = request.POST.get("endereco")
    Vtelefone = request.POST.get("telefone")
    Vcnpj = request.POST.get("cnpj")
    fornecedores = Fornecedor.objects.get(id=id)
    fornecedores.nome = Vnome
    fornecedores.endereco = Vendereco
    fornecedores.telefone = Vtelefone
    fornecedores.cnpj = Vcnpj
    fornecedores.save()
    return redirect(home)

def deleteFornecedor(request, id):
    fornecedores = Fornecedor.objects.get(id=id)
    fornecedores.delete()
    return redirect(home)