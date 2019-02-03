Docker Compose Full Stack
=========================
Example of a full stack web application using docker-compose.

Stack
-----
* Alpine
* Postgres
* Nginx
* Gunicorn
* Redis
* Django (REST framework)

Instructions
------------

Build application containers:
```
docker compose build
```

Run application containers:
```
docker compose up
```

Drop a shell into the running web application container:
```
docker exec -it dockering_web /bin/sh
```

Build unit test containers:
```
docker-compose -f docker-compose.test.yml build
```

Run unit test containers (attach for interactive breakpoint):
```
docker-compose -f docker-compose.test.yml up
docker attach dockering_test
```
