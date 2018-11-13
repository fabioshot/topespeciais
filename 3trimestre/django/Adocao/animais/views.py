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
class Ajuda(TemplateView):
    # Define qual o arquivo HTML vai ser usado para exibir esta página
    template_name = "ajuda.html" # deve estar na pasta templates


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


class PessoaCreate(CreateView):
    model = Pessoa
    success_url = reverse_lazy('index')
    template_name = 'forms.html'
    fields= ['nome', 'email', 'nascimento', 'cidade']


class PessoaUpdate(UpdateView):
    model = Pessoa
    success_url = reverse_lazy('index')
    template_name = 'forms.html'
    fields= ['nome', 'email', 'nascimento', 'cidade']


class PessoaDelete(DeleteView):
    model = Pessoa
    success_url = reverse_lazy('index')
    template_name = 'forms_delete.html'
