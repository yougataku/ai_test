APP_CONTAINER_NAME = app
DB_CONTAINER_NAME = db
RUN_APP = docker-compose exec $(APP_CONTAINER_NAME)
RUN_POETRY =  $(RUN_APP) poetry run
RUN_DJANGO = $(RUN_POETRY) python manage.py
RUN_PYTEST = $(RUN_POETRY) pytest

prepare:
	docker-compose up -d --build

up:
	docker-compose up -d

build:
	docker-compose build

down:
	docker-compose down

loaddata:
	$(RUN_DJANGO) loaddata crm.json

makemigrations:
	$(RUN_DJANGO) makemigrations

migrate:
	$(RUN_DJANGO) migrate

show_urls:
	$(RUN_DJANGO) show_urls

shell:
	$(RUN_DJANGO) debugsqlshell

superuser:
	$(RUN_DJANGO) createsuperuser

test:
	$(RUN_PYTEST)

format:
	$(RUN_POETRY) black .
	$(RUN_POETRY) isort .

update:
	$(RUN_APP) poetry update

app:
	docker exec -it $(APP_CONTAINER_NAME) bash

db:
	docker exec -it $(DB_CONTAINER_NAME) bash

zero:
	$(RUN_DJANGO) migrate application zero
