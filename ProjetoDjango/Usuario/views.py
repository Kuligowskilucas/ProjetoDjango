from django.shortcuts import render, redirect
from .models import Usuario

# Create your views here.
def home(request):
    usuarios = Usuario.objects.all()
    return render(request, "usuario.html", {"usuarios": usuarios})

def salvar(request):
    Vnome = request.POST.get("nome")
    Vendereco = request.POST.get("endereco")
    Vtelefone = request.POST.get("telefone")
    Vcpf = request.POST.get("cpf")
    Usuario.objects.create(nome=Vnome,endereco=Vendereco,telefone=Vtelefone,cpf=Vcpf)
    usuarios = Usuario.objects.all()
    return render(request, "usuario.html", {"usuarios": usuarios})

def editar(request, id):
    usuario = Usuario.objects.get(id=id)
    return render(request, "update.html", {"usuario": usuario})

def update(request, id):
    Vnome = request.POST.get("nome")
    Vendereco = request.POST.get("endereco")
    Vtelefone = request.POST.get("telefone")
    Vcpf = request.POST.get("cpf")
    usuario = Usuario.objects.get(id=id)
    usuario.nome = Vnome
    usuario.endereco = Vendereco
    usuario.telefone = Vtelefone
    usuario.cpf = Vcpf
    usuario.save()
    return redirect(home)

def delete(request, id):
    usuario = Usuario.objects.get(id=id)
    usuario.delete()
    return redirect(home)