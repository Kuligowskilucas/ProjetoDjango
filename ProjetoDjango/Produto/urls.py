from django.contrib import admin
from django.urls import path, include
from .views import home, salvarProduto, editarProduto, updateProduto, deleteProduto

urlpatterns = [
    path('', home),
    path('salvar/', salvarProduto, name="salvarProduto"),
    path('editar<int:id>', editarProduto, name="editarProduto"),
    path('update<int:id>', updateProduto, name="updateProduto"),
    path('delete<int:id>', deleteProduto, name="deleteProduto")
]