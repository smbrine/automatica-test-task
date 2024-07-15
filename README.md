# automatica-test-task

# Postgres
Skip this part if you already have a running postgres instance.
1. Set any Postgres credentials in [.env](./.env)
2. Run docker on your computer
3. Create a postgres instance with either of these
* `docker compose --env-file .env up`
* `docker run --env-file .env postgres:16.2-bullseye`

# Installation
1. Upgrade pip: 
    ```sh
    python -m pip install --upgrade pip
    ```
2. Install Poetry (package manager):
    ```sh
    python -m pip install poetry
    ```
3. Create venv and install project dependencies:
    ```sh
    poetry install
    ```
4. Ensure the correct Postgres credentials are set in the [.env](./.env) file. Example:
```
POSTGRES_HOST=localhost
POSTGRES_USERNAME=username
POSTGRES_PASSWORD=password
PGADMIN_DEFAULT_EMAIL=admin@pgadmin.com
PGADMIN_DEFAULT_PASSWORD=password
```
5. Apply migrations and run the Django server:
    ```sh
    poetry run python manage.py migrate
    poetry run python manage.py runserver
    ```

# Test data
Load test data by running these commands consecutively:
1. ```sh
    poetry run python manage.py loaddata visits/fixtures/workers.json
    ```
2. ```sh
    poetry run python manage.py loaddata visits/fixtures/retail_points.json
    ```
3. ```sh
    poetry run python manage.py loaddata visits/fixtures/visits.json
    ```

# Env vars
* Hostname for Postgres DB: `POSTGRES_HOST`
* Username for Postgres DB: `POSTGRES_USERNAME`
* Password for Postgres DB: `POSTGRES_PASSWORD`
* PGAdmin email: `PGADMIN_DEFAULT_EMAIL`
* PGAdmin password: `PGADMIN_DEFAULT_PASSWORD`

# Methods
* Returns retail points related to the worker:
    ```sh
    curl -X GET -H "Authorization: Phone +79999999999" http://localhost:8000/api/retail-points/
    ```

* Adds a new visit to a retail point by a worker:
    ```sh
    curl -X POST -H "Authorization: Phone +79999999999" -H "Content-Type: application/json" -d '{"retail_point_id": "b4ea36ee-845d-4a65-9e65-1294f2e8c305", "latitude": 37.7749, "longitude": -122.4194}' http://localhost:8000/api/visits/
    ```
