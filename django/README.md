# Desafio EDESOFT BackEnd Com Django

## Como rodar o projeto
- Primeira coisa a se fazer e criar e preencher o arquivo .env, para facilitar copie o arquivo .env.example
- Depois instale o [docker](https://www.docker.com/) em sua máquina.
- Execute o comando `docker compose up -d`
- Entre em [0.0.0.0:8000/api/desafio](0.0.0.0:8000/api/desafio)

## Preenchendo formulario

O arquivo bucket esta localizado na aws S3, seu bucket_name e `teste-edesoft-csv` e o object_key `teste.csv`

Realize uma solicitação `POST`, a api ira cadastrar todos os dados presentes na planilha e retornar os últimos 10 cadastrados em formato JSON
