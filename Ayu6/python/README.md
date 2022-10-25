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


Para acceder a las rutas aplicar lo siguiente:
```sh
curl --location --request POST http://localhost:3000/login \
--header 'Content-Type: application/json' \
--data-raw '{
    "user":"user",
    "pass":"password"
}'
```

Response
```js
// En caso de colocar una contraseña incorrecta
{
    "error":"Wrong password"
}
// En caso de colocar correctamente los datos
{
    "success":True
}
```
Ahora bien, se debe de crear una cuenta:
```sh
curl --location --request POST 'localhost:3000/register' \
--header 'Content-Type: application/json' \
--data-raw '{
    "user":"test",
    "pass":"test1234"
}'
```
Aunque no es del todo necesario, al momento de hacer logins de igual forma bloquea al usuario en específico.
