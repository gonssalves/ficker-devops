FROM python:3.10.12-slim

# Define o diretório de trabalho
WORKDIR /app

# Copia todos os arquivos do diretório atual para o contêiner
COPY . /app

# Instala as dependências do Flask, se houver
RUN pip install -r requirements.txt

EXPOSE 8080

# Define o comando para executar o arquivo app.py
CMD ["python", "app.py"]
