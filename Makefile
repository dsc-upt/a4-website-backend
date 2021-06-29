BASE_DIR := src
RUN := poetry run
MANAGE_PY := $(RUN) $(BASE_DIR)/manage.py

run:
	poetry run src/manage.py runserver

# run this command every time when you modified a model
migrations:
	poetry run src/manage.py makemigrations

# run this command every time when you make a git pull and after you ran above command
migrate:
	poetry run src/manage.py migrate

superuser:
	poetry run src/manage.py createsuperuser
