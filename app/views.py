from datetime import date
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
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)

        funcionario = context['object']
        idade = self.calcular_idade(funcionario.data_nascimento)
        funcionario.nascimento_idade = f"{funcionario.data_nascimento.strftime('%d/%m/%Y')} - {idade} anos"
        
        return context

    def calcular_idade(self, data_nascimento):
        hoje = date.today()
        idade = hoje.year - data_nascimento.year
        if hoje.month < data_nascimento.month or (hoje.month == data_nascimento.month and hoje.day < data_nascimento.day):
            idade -= 1
        return idade

class FuncionarioDeleteView(DeleteView):
    model = Funcionario
    template_name = "remover_funcionario.html"
    context_object_name = "fun"
    success_url = reverse_lazy("lista_funcionarios")
