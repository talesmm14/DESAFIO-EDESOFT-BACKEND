import re
from datetime import datetime
import io

import boto3
import pandas as pd
from apps.api.models.usuario import Usuario
from config import settings


def read_csv(csv_path):
    try:
        data_frame = pd.read_csv(
            csv_path,
            converters={
                'nome': lambda x: x.capitalize(),
                'sobrenome': lambda x: x.capitalize(),
                'email': lambda x: x.lower(),
                'cpf_cnpj': lambda x: re.sub('[^0-9]', '', x),
                'profissao': str,
                'aniversario': lambda x: datetime.strptime(x, "%d/%m/%Y")
            }
        )

        for _, usuario in data_frame.iterrows():
            if len(usuario['cpf_cnpj']) == 11:
                Usuario.objects.get_or_create(
                    nome=usuario['nome'],
                    sobrenome=usuario['sobrenome'],
                    cpf=usuario['cpf_cnpj'],
                    profissao=usuario['profissao'],
                    aniversario=usuario['aniversario'],
                    defaults={
                        'email': usuario['email']
                    }
                )
        return True
    except Exception as e:
        return e

