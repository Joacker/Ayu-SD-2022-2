# Python

Para levantar las instancias dentro de la topología
```sh
docker-compose up --build
```

Luego de haber levantado la topología debemos de conectarnos al contenedor de kafka para habilitar el topic
```sh
docker exec -it kafka bash
```
Creamos el Topic
```sh
kafka-topics.sh --create --bootstrap-server kafka:9092 --replication-factor 1 --partitions 1 --topic test
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