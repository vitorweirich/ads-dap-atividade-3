from django.shortcuts import render
from django.views.generic import (
    CreateView, ListView, UpdateView, DetailView, DeleteView
)
from django.urls import reverse_lazy
from .models import Funcionario

# Create your views here.

class FuncionarioCreateView(CreateView):
    model = Funcionario
    fields = "__all__"
    template_name = "form_funcionario.html"
    success_url = "lista_funcionarios"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['botao_texto'] = "Cadastrar"
        return context

class FuncionarioUpdateView(UpdateView):
    model = Funcionario
    fields = ("nome", "data_nascimento", "email", "profissao")
    template_name = "form_funcionario.html"
    success_url = reverse_lazy("lista_funcionarios")
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['botao_texto'] = "Salvar"
        return context

class FuncionarioListView(ListView):
    model = Funcionario
    template_name = "lista_funcionarios.html"
    ordering = ['nome']

class FuncionarioDetailView(DetailView):
    model = Funcionario
    template_name = "lista_funcionario.html"
    context_object_name = "fun"

class FuncionarioDeleteView(DeleteView):
    model = Funcionario
    template_name = "remover_funcionario.html"
    context_object_name = "fun"
    success_url = reverse_lazy("lista_funcionarios")
