# Generated by Django 4.1.7 on 2023-03-20 15:06

from django.db import migrations, models
import localflavor.br.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=90, verbose_name='Nome')),
                ('sobrenome', models.CharField(max_length=120, verbose_name='Sobrenome')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('cnpj', localflavor.br.models.BRCNPJField(blank=True, max_length=18, null=True, verbose_name='CNPJ')),
                ('cpf', localflavor.br.models.BRCPFField(blank=True, max_length=14, null=True, verbose_name='CPF')),
                ('profissao', models.CharField(default=0, max_length=40)),
                ('aniversario', models.DateField()),
                ('create_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]