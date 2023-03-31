SHELL = /bin/bash

python = venv/bin/python
manage := $(python) manage.py

ip = 0
port = 8000

migrate:
	$(manage) makemigrations && $(manage) migrate

run:
	$(manage) runserver $(ip):$(port)

runque:
	$(manage) runque

superuser:
	$(manage) createsuperuser

check:
	$(manage) check

migrations:
	$(manage) makemigrations

test:
	$(manage) test

shell:
	$(manage) shell

app:
	django-admin startapp $(name)

build:
	docker-compose -f confs/docker/docker-compose.yml up --build -d
