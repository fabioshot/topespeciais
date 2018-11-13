from django.urls import path

# importa tudo que tem no views.py do app "animais"
from .views import *
# . indica para o python buscar o views dentro deste diretório
# * indica para importar tudo de lá

urlpatterns = [
    #   ( endereço, método da view, nome da url )
    path('', Index.as_view(), name="index" ),
    path('ajuda/', Ajuda.as_view(), name="ajuda"),

    path('inserir/cidade/', CidadeCreate.as_view(), name = 'inserir-cidade'),
    path('editar/cidade/<int:pk>/', CidadeUpdate.as_view(), name = 'editar-cidade'),
    path('excluir/cidade/<int:pk>/', CidadeDelete.as_view(), name = 'excluir-cidade'),
    path('listar/cidades/', CidadeList.as_view(), name="listar-cidade"),

    path('inserir/pessoa', PessoaCreate.as_view(), name = 'inserir-pessoa'),
    path('editar/pessoa/<int:pk>/', PessoaUpdate.as_view(), name = 'editar-pessoa'),
    path('excluir/pessoa/<int:pk>/', PessoaDelete.as_view(), name = 'excluir-pessoa'),
]
