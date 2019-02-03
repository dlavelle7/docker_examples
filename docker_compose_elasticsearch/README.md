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

Run the application containers with a pdb interactive breakpoint:
```
docker-compose -f docker-compose.yml -f docker-compose.pdb.yml up --build
docker attach web
```

Kibana
------
Once the application containers have been brought up, you can view the
Elasticsearch data store via the Kibana UI by opening this
url: `http://localhost:5601`.
