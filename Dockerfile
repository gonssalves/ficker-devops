FROM python:3.10.12-slim

WORKDIR /app

COPY . /app

# Instala as dependências do Flask, se houver
RUN pip install -r requirements.txt

EXPOSE 8080

CMD exec python3 app.py