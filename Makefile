ifneq (,$(wildcard ./.env))
include .env
export
ENV_FILE_PARAM = --env-file .env

endif


up:
	docker compose -f docker-compose.yaml up --build --force-recreate --remove-orphans -d
up-staging:
	docker compose -f docker-compose.staging.yml up --build --force-recreate --remove-orphans -d
down: 
	docker compose -f docker-compose.yaml down  -v
down-staging: 
	docker compose -f docker-compose.staging.yml down  -v
show-logs:
	docker compose -f docker-compose.yaml logs -f  
show-logs-staging:
	docker compose -f docker-compose.staging.yml logs -f 
migrate:
	docker compose -f docker-compose.yaml  exec web python3 manage.py migrate 
make-migrations:
	docker compose -f docker-compose.yaml exec web python3 manage.py makemigrations
collectstatic:
	docker compose -f docker-compose.yaml exec web python3 manage.py collectstatic --no-input --clear
runserver:
	python3 manage.py runserver