from django.db import models
from django.conf import settings
from django.utils import timezone
from cpf_field.models import CPFField
from .validators import validate_cpf

class CPFField(models.CharField):
    default_validators = [validate_cpf]

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('max_length', 14)
        super().__init__(*args, **kwargs)

class Cadastro(models.Model):
    nome = models.CharField(max_length=200, null=False, blank=False)
    data_de_nascimento = models.DateField(blank=False)
    email = models.EmailField(max_length=200, null=False, blank=False, unique=True)
    telefone = models.CharField(max_length=50, null=False, blank=False)
    cpf = CPFField('cpf', unique=True, null=False, blank=False)
    foto = models.ImageField(upload_to='images/')
    data_de_cadastro = models.DateTimeField(default=timezone.now)
    data_de_alteracao = models.DateField(auto_now=True)
    
    def publish(self):
        self.publish_date = timezone.now
        self.save()
        
    def __str__(self):
        return self.nome
    
