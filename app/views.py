from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from .models import Cadastro


class CadastroList(ListView):
    model = Cadastro
    queryset = Cadastro.objects.all()
    
class CadastroCreate(CreateView):
    model = Cadastro
    fields = '__all__'
    success_url = reverse_lazy('app:cadastro_list')


class CadastroUpdate(UpdateView):
    model = Cadastro
    fields = 'nome', 'data_de_nacimento', 'email', 'telefone', 'foto'
    success_url = reverse_lazy('app:cadastro_list')

class CadastroDetail(DetailView):
    queryset = Cadastro.objects.all()

class CadastroDelete(DeleteView):
    queryset = Cadastro.objects.all()
    success_url = reverse_lazy('app:cadastro_list')