from django.contrib import admin
from django.urls import path, include
from.views import home, salvarFornecedor, editarFornecedor, updateFornecedor, deleteFornecedor

urlpatterns = [
    path('', home),
    path('salvar/', salvarFornecedor, name="salvarFornecedor"),
    path('editar/<int:id>', editarFornecedor, name="editarFornecedor"),
    path('update/<int:id>', updateFornecedor, name="updateFornecedor"),
    path('delete<int:id>', deleteFornecedor, name="deleteFornecedor")
]
