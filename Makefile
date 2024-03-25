.PHONY: runserver
runserver:
	poetry run python manage.py runserver

.PHONY: migrate
migrate:
	poetry run python manage.py migrate

.PHONY: migrations
migrations:
	poetry run python manage.py makemigrations

.PHONY: superuser
superuser:
	poetry run python manage.py createsuperuser

.PHONY: update_db
update_db: migrations migrate ;
