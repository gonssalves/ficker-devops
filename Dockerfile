FROM python:3.10.12-slim

WORKDIR /app

COPY . /app

RUN pip install -r requirements

EXPOSE 80

ENV NAME flask

CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]