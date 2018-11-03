build:
	@docker-compose build

build-test:
	@docker-compose -f docker-compose.test.yml build

up:
	@docker-compose up

up-test:
	@docker-compose -f docker-compose.test.yml up -d
	@docker attach dockering_test

shell-web:
	@docker exec -it dockering_web /bin/sh
