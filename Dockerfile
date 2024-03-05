FROM python:3.10.12-slim

# Define o diretório de trabalho
WORKDIR /app

# Copia todos os arquivos do diretório atual para o contêiner
COPY . /app

<<<<<<< HEAD
=======
# Instala as dependências do Flask, se houver
>>>>>>> 42c146b0a8d61d5d6de0034f800d1fd22ddd1a19
RUN pip install -r requirements.txt

EXPOSE 8080

<<<<<<< HEAD
ENV NAME flask

CMD exec gunicorn --bind :8080 app:app
=======
# Define o comando para executar o arquivo app.py
CMD ["python", "app.py"]
>>>>>>> 42c146b0a8d61d5d6de0034f800d1fd22ddd1a19
