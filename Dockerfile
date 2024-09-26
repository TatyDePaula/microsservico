# Utiliza uma imagem base do Python
FROM python:3.9-slim

# Define o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copia os arquivos de dependências (requirements.txt) para o contêiner
COPY requirements.txt .

# Instala as dependências listadas no requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copia todo o conteúdo da aplicação para o diretório de trabalho
COPY . .

# Define a variável de ambiente para evitar problemas de buffer
ENV PYTHONUNBUFFERED=1

# Expor a porta que o Flask está usando (8000, conforme seu main.py)
EXPOSE 8000

# Comando para rodar a aplicação
CMD ["python", "main.py"]


