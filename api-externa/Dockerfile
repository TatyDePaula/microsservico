# Use a imagem oficial do Python como base
FROM python:3.9-slim

# Defina o diretório de trabalho
WORKDIR /app

# Copie o arquivo requirements.txt para o diretório de trabalho
COPY requirements.txt .

# Instale as dependências
RUN pip install -r requirements.txt

# Copie o arquivo viacep.py para o diretório de trabalho
COPY viacep.py .

# Defina a porta que a API irá usar
EXPOSE 8080

# Defina o comando para executar a API
CMD ["python", "viacep.py"]