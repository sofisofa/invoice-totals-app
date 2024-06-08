run_app: prodUp

upload_file:
	curl -X POST -F "file=@$(file)" http://localhost:8000/api/upload/

prodUp:
	docker compose -f './docker-compose-prod.yml' --env-file ./.env up -d --build

prodDown:
	docker compose -f './docker-compose-prod.yml' --env-file ./.env down

tests: _testUp _sleep2 _initTestDb _coverage _testDown

_start_app:
	ENV_FILE_PATH='/.env' python manage.py startapp invoices

_testUp:
	docker compose --env-file ./.env.test up -d --build

_testDown:
	docker compose --env-file ./.env.test down

_initTestDb:
	#TODO: crear un db de test

_coverage:
	coverage run -m pytest
	coverage report -m
	coverage erase

_sleep2:
	sleep 2