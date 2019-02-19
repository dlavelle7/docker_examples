Docker Compose with Elasticsearch
=================================
Example of a simple web application with a "country search" feature, powered by
Elasticsearch search engine.

Stack
-----
* Alpine
* Python 3.6
* Django
* Elasticsearch
* Kibana

Instructions
------------
Build the application containers:
```
docker compose build
```

Run the application containers:
```
docker compose up
```

Run the application containers in "dev"; mode which mounts the web app source
code to the container, uses the Django devserver and allows for interative
breakpoints:
```
docker-compose -f docker-compose.yml -f docker-compose.dev.yml up --build
docker attach web
```

Kibana
------
Run the application containers with a Kibana container:
```
docker-compose -f docker-compose.yml -f docker-compose.kibana.yml up --build
```

Once the application containers have been brought up, you can view the
Elasticsearch data store via the Kibana UI by opening this
url: `http://localhost:5601`.
