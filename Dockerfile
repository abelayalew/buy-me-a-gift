FROM python:3.10.7
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /code


ADD ./requirements.txt /code/requirements.txt
RUN pip install -r requirements.txt

RUN apt-get update -y && apt-get install nginx -y

ADD . /code

RUN cp ./nginx.conf /etc/nginx/sites-enabled/default
RUN service nginx restart
