from rest_framework import serializers

from apps.api.models import Usuario


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'nome', 'sobrenome', 'cpf', 'cnpj', 'email', 'profissao', 'aniversario', 'create_at']
