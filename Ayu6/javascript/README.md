# Javascript version, for beginners
---------------------------------------
**Finalmente para ejecutar el SW se recomienda usar el siguiente comando**

 ```bash
docker-compose up --build
```

Ruta tipo post para ingresar usuarios del producer al consumer (1):

```url
http://localhost:3000/login [post]
```

Añadiendo también el siguiente json

```json
{
	"username":"pablo",
	"password":"123"
}
```

```url
http://localhost:8000/blocked [get]
```

Al ejecutar esta ruta en el cliente postman o insomnia retornará la lista de usuarios bloqueados bajo las condiciones entregadas por el enunciado. Un ejemplo más práctico es el siguiente:

```json
[
    "pablo"
]
```
En caso de que el consumer no logre conectarse con el producer, se recomienda efectuar la siguiente ruta asociado al directorio root:

```url
http://localhost:8000/
```

Luego de esto se puede efectuar el inicio de sesión con la ruta post ya mencionada anteriormente (1). 

![github small](https://elestanteliterario.com/wp-content/uploads/2018/12/franz-kafka.jpg)
