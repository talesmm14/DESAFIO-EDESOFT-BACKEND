import io
import re
import pandas as pd
import boto3

from datetime import datetime
from apps.api.models.usuario import Usuario
from rest_framework.views import APIView
from rest_framework.response import Response

from apps.api.serializers import S3Serializer
from apps.api.serializers.usuario import UsuarioSerializer


class DesafioView(APIView):
    serializer_class = S3Serializer

    def get(self, request):
        usuarios = Usuario.objects.order_by('-create_at')[:10]
        serializer = UsuarioSerializer(usuarios, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            bucket_name = serializer.validated_data.get('bucket_name')
            object_key = serializer.validated_data.get('object_key')
            s3 = boto3.client('s3')
            response = s3.get_object(Bucket=bucket_name, Key=object_key)
            csv_data = response['Body'].read().decode('utf-8')
            data_frame = pd.read_csv(
                io.StringIO(csv_data),
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
                user = Usuario(
                    nome=usuario['nome'],
                    sobrenome=usuario['sobrenome'],
                    profissao=usuario['profissao'],
                    aniversario=usuario['aniversario'],
                    email=usuario['email']
                )
                if len(usuario['cpf_cnpj']) == 11:
                    user.cpf = usuario['cpf_cnpj']
                else:
                    user.cnpj = usuario['cpf_cnpj']
                user.save()
            return Response({'success': True})
        else:
            return Response({'success': False, 'errors': serializer.errors})
