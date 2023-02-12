FROM python:3.10.5-slim-buster

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

CMD gunicorn --bind 0.0.0.0:5000 app:app
