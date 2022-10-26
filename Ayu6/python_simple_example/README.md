# Python Second version, for beginners
---------------------------------------

Para iniciar la aplicación, es necesario ejecutar los siguientes comandos, sin embargo para que funcionen debemos estar en la raíz de la carpeta:

Comandos:

```
$ docker-compose build --no-cache
$ docker-compose up --force-recreate
```

Una vez levantado el servicio hay que ir al CLI de Kafka y ejecutar el siguiente comando para crear el topic a utilizar:
```sh
docker exec -it kafka bash
```

```
kafka-topics.sh --create --bootstrap-server kafka:9092 --replication-factor 1 --partitions 1 --topic test

```
Una vez inicializado el sistema se podran realizar las consultas al cliente, pero antes es importante acceder a la siguiente dirección, la idea de esto es que el consumer este escuchando las solicitudes realizadas: 

```
http://localhost:5000/
http://localhost:5000/blocked
```
Para poder realizar las consultas se utiliza la siguiente ruta:

```
http://localhost:8000/
http://localhost:8000/login
```
Se puede utilizar postman o el mismo navegador para probar el funcionamiento de la aplicación. En caso de postman se debe realizar una solicitud POST desde el apartado "Body", seleccionando "form-data" a la dirección del login.

---------------------------------------
Observaciones

Para la que se este realizando constantemente la solicitud del "Consumer, se utiliza la siguiente etiqueta HTML la cual nos permite mantener actualizando constantemente la página y mantiendo el estado de espera por el flujo de datos:

```html
<head>
  <meta http-equiv="refresh" content="1">
</head>
```


