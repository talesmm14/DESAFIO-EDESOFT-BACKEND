from django.db import models
from localflavor.br.models import BRCPFField, BRCNPJField


class Usuario(models.Model):
    nome = models.CharField(verbose_name="Nome", max_length=90)
    sobrenome = models.CharField(verbose_name="Sobrenome", max_length=120)
    email = models.EmailField(verbose_name="Email")
    cnpj = BRCNPJField(verbose_name="CNPJ", null=True, blank=True)
    cpf = BRCPFField(verbose_name="CPF", null=True, blank=True)
    profissao = models.CharField(max_length=40, default=0)
    aniversario = models.DateField()
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.nome} {self.sobrenome}'
