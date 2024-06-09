run_app: 
	docker compose -f './docker-compose-prod.yml' --env-file ./.env up -d --build --remove-orphans

stop_app:
	docker compose -f './docker-compose-prod.yml' --env-file ./.env down

upload_file:
	curl -X POST -F "file=@$(file)" http://localhost:8000/api/upload/

tests: _testUp 

stop_tests: _testDown

_start_app:
	ENV_FILE_PATH='/.env' python manage.py startapp invoices

_testUp:
	docker compose --env-file ./.env  build 
	docker compose --env-file ./.env run test 

_testDown:
	docker compose --env-file ./.env down

_initTestDb:
	#TODO: crear un csv de test

_sleep5:
	sleep 5