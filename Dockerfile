FROM python:3.10.12-slim

WORKDIR /app

COPY . /app

<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
# Instala as dependências do Flask, se houver
>>>>>>> 42c146b0a8d61d5d6de0034f800d1fd22ddd1a19
>>>>>>> 58bd75726847256564e4cf73b917d85ec2e8ea3a
RUN pip install -r requirements.txt

EXPOSE 8080

<<<<<<< HEAD
CMD exec python3 app.py
=======
<<<<<<< HEAD
ENV NAME flask

CMD exec gunicorn --bind :8080 app:app
=======
# Define o comando para executar o arquivo app.py
CMD ["python", "app.py"]
>>>>>>> 42c146b0a8d61d5d6de0034f800d1fd22ddd1a19
>>>>>>> 58bd75726847256564e4cf73b917d85ec2e8ea3a
