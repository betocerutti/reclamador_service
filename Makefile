DB_CONTAINER_NAME=postgres
WEB_CONTAINER_NAME=reclamador
DATABASE_NAME=reclamador

run:
	@echo "Running containers..."
	@sudo docker compose up

test:
	@echo "Running tests..."
	@sudo docker exec -it $(WEB_CONTAINER_NAME) python manage.py test

stop:
	@echo "Stopping containers..."
	@sudo docker compose down

build:
	@echo "Building containers..."
	@sudo docker compose up build

db-dump:
	@echo "Dumping database..."
	@sudo docker exec -it $(DB_CONTAINER_NAME) pg_dump -U postgres $(DATABASE_NAME) > db/$(DATABASE_NAME)_dump.sql

db-restore:
	@echo "Restoring database..."
	# stop web container
	@sudo docker stop $(WEB_CONTAINER_NAME)
	@sudo docker exec -it $(DB_CONTAINER_NAME) psql -U postgres $(DATABASE_NAME) < db/$(DATABASE_NAME)_dump.sql
	# start web container
	@sudo docker start $(WEB_CONTAINER_NAME)

app-migrations:
	@echo "Running migrations..."
	@sudo docker exec -it $(WEB_CONTAINER_NAME) python manage.py makemigrations 
	@sudo docker exec -it $(WEB_CONTAINER_NAME) python manage.py migrate

app-createsuperuser:
	@echo "Creating superuser..."
	@sudo docker exec -it $(WEB_CONTAINER_NAME) python manage.py createsuperuser

app-clean-pycache:
	@echo "Cleaning pycache..."
	@sudo find . -name "*.pyc" -exec rm -rf {} \;
	@sudo find . -name "__pycache__" -exec rm -rf {} \;

docker-clean:
	@echo "Cleaning docker..."
	@sudo docker system prune -a
