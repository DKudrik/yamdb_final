FROM python:3.9-slim
WORKDIR /code
COPY . /code
RUN pip install -r requirements.txt
RUN pip install gunicorn
COPY prepare.sh /prepare.sh
RUN chmod +x /prepare.sh
