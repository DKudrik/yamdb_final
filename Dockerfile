FROM python:3.9-slim

WORKDIR /code

COPY . /code

RUN pip install -r requirements.txt && apt-get install -y gunicorn

