FROM python:3.10.12-slim

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

EXPOSE 8080

ENV NAME flask

CMD exec gunicorn --bind :8080 app:app