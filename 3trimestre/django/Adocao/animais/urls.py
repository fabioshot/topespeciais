from django.urls import path

# importa tudo que tem no views.py do app "animais"
from .views import *
# . indica para o python buscar o views dentro deste diretório
# * indica para importar tudo de lá

urlpatterns = [
    #   ( endereço, método da view, nome da url )
    path('', Index.as_view(), name="index" ),
    path('sobre/', Sobre.as_view(), name="sobre"),
    path('menu/', Menu.as_view(), name="menu"),

    path('inserir/cidade/', CidadeCreate.as_view(), name = 'inserir-cidade'),
    path('editar/cidade/<int:pk>/', CidadeUpdate.as_view(), name = 'editar-cidade'),
    path('excluir/cidade/<int:pk>/', CidadeDelete.as_view(), name = 'excluir-cidade'),
    
    path('inserir/tipo', TipoCreate.as_view(), name = 'inserir-tipo'),
    path('editar/tipo/<int:pk>/', TipoUpdate.as_view(), name = 'editar-tipo'),
    path('excluir/tipo/<int:pk>/', TipoDelete.as_view(), name = 'excluir-tipo'),

    path('inserir/animais', AnimaisCreate.as_view(), name = 'inserir-animais'),
    path('editar/animais/<int:pk>/', AnimaisUpdate.as_view(), name = 'editar-animais'),
    path('excluir/animais/<int:pk>/', AnimaisDelete.as_view(), name = 'excluir-animais'),
    path('listar/listartodos/', AnimaisList.as_view(), name="listar-animais"),

]
