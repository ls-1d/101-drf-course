# Install dependencies
install:
	# Install dependencies from requirements.txt
	pip install -r requirements.txt

# Run Django migrations
migrations:
	python manage.py makemigrations

migrate:
	python manage.py migrate

# Start Django development server
runserver:
	python manage.py runserver

superuser:
	python manage.py createsuperuser

# Run PostgreSQL Docker container
run_postgres:
	# Run PostgreSQL Docker container using a default password and database name
	docker run --name drf_postgres -e POSTGRES_PASSWORD=drf_password -e POSTGRES_DB=drf_db -p 5432:5432 -d postgres

# Stop the PostgreSQL Docker container
stop_postgres:
	docker stop drf_postgres
	docker rm drf_postgres