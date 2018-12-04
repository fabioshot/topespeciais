# Uma classe simples para exibir uma página simples
from django.views.generic import TemplateView
# Serve para páginas que só tem HTML e talvez alguma consulta
# para listar coisas do banco


#importar modelos
from .models import *


#importar metodos views para inserir, alterar. exluir
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Trabalhar com view de lista
from django.views.generic.list import ListView

#importar funçao para gerar os endereços de nossas URLs inteiras
from django.urls import reverse_lazy


# Página inicial
class Index(TemplateView):
    # Define qual o arquivo HTML vai ser usado para exibir esta página
    template_name = "index.html" # deve estar na pasta templates


# Página de ajuda
class Sobre(TemplateView):
    # Define qual o arquivo HTML vai ser usado para exibir esta página
    template_name = "sobre.html" # deve estar na pasta templates

class Menu(TemplateView):
    template_name = "menu.html"


class CidadeCreate(CreateView):
    model = Cidade
    success_url = reverse_lazy('index')
    template_name = 'forms.html'
    fields= ['nome', 'estado']


class CidadeDelete(DeleteView):
    model = Cidade
    success_url = reverse_lazy('index')
    template_name = 'forms_delete.html'


class CidadeUpdate(UpdateView):
    model = Cidade
    success_url = reverse_lazy('index')
    template_name = 'forms.html'
    fields= ['nome', 'estado']


class CidadeList(ListView):
    model = Cidade
    template_name = 'cidade_list.html'



class TipoCreate(CreateView):
    model = Tipo
    success_url = reverse_lazy('index')
    template_name = 'forms.html'
    fields= ['descricao']



class TipoDelete(DeleteView):
    model = Tipo
    success_url = reverse_lazy('index')
    template_name = 'forms_delete.html'


class TipoUpdate(UpdateView):
    model = Tipo
    success_url = reverse_lazy('index')
    template_name = 'forms.html'
    fields= ['descricao']


class AnimaisCreate(CreateView):
    model = Animais
    success_url = reverse_lazy('index')
    template_name = 'forms.html'
    fields= ['doador', 'email', 'telefone', 'nascimento', 'cidade', 'tipo', 'raca', 'apelido', 'vacinas']


class AnimaisUpdate(UpdateView):
    model = Animais
    success_url = reverse_lazy('index')
    template_name = 'forms.html'
    fields= ['doador', 'email', 'telefone', 'nascimento', 'cidade', 'tipo', 'raca', 'apelido', 'vacinas']


class AnimaisDelete(DeleteView):
    model = Animais
    success_url = reverse_lazy('index')
    template_name = 'forms_delete.html'


class AnimaisList(ListView):
    model = Animais
    template_name = 'animais_list.html'
