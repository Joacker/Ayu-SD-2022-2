# Python

Para levantar las instancias dentro de la topología
```sh
docker-compose up --build
```

GET
```sh
http://localhost:8000/search?search=
```

Para bajar las instancias del compose
```sh
docker-compose down
```

Borrar cache en contenedores
```sh
docker system prune -a
```

Borrar cache en volumenes
```sh
docker volume rm $(docker volume ls -q)
```