from django.contrib import admin
from django.urls import path, include
from .views import home, salvar, editar, update, delete

urlpatterns = [
    path('', home),
    path('salvar/', salvar, name="salvarUsuario"),
    path('editar/<int:id>', editar, name="editarUsuario"),
    path('update/<int:id>', update, name="updateUsuario"),
    path('delete/<int:id>', delete, name="deleteUsuario")
]