install:
	poetry install

migrate:
	poetry run python manage.py migrate

run:
	poetry run python manage.py runserver

loaddata:
	poetry run python manage.py loaddata visits/fixtures/workers.json
	poetry run python manage.py loaddata visits/fixtures/retail_points.json
	poetry run python manage.py loaddata visits/fixtures/visits.json