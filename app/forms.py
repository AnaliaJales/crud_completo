from django import forms
from django.forms import ModelForm
from app.models import Cadastro
from cpf_field.models import Cadastro
from .models import *

class CadastroForm(forms.ModelForm):
    class Meta:
        model = Cadastro
        fields = ('__all__')
       