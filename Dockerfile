# Use a imagem compatível com o Railway
FROM railwayapp/python:3.11

# Defina o diretório de trabalho
WORKDIR /app

# Copie o arquivo requirements.txt para o diretório de trabalho
COPY requirements.txt requirements.txt

# Instale as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copie todo o projeto para o diretório de trabalho
COPY . /app
