FROM python:3.9-slim

WORKDIR /code

COPY . /code

RUN pip install -r requirements.txt && pip install -y gunicorn

