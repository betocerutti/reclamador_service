
## Propuesta
Para cumplir con los requisitos mencionados, propongo utilizar las siguientes tecnologías y enfoques:

Lenguaje de programación: Python 3.9
Framework web: Django rest framework
Base de datos: PostgreSQL
Contenedorización: Docker
Colas de tareas: Celery **(faltó de tiempo)**{: style:"color: red"}
Control de versiones: Git

A continuación, se describe una propuesta general para implementar el servicio con los tres endpoints solicitados, la autenticación de usuarios y los roles:

1. Configuración y Despliegue:
    - Utilizar Docker para contenerizar la aplicación y definir un archivo de Docker Compose para facilitar la configuración y ejecución.
2. Autenticación y Seguridad:
    - Implementar un sistema de autenticación basado en tokens, como JSON Web Tokens (JWT), para asegurar los endpoints y controlar el acceso de los clientes externos.
    - Establecer roles de usuario, como "admin" y "cliente", para diferenciar los permisos de acceso.
3. Endpoints:
    - Crear dos endpoints de recepción de información (POST) para clientes y reclamaciones, que validen y almacenen los datos recibidos en los modelos correspondientes de Django.
    - Implementar un endpoint de envío de información (GET) para obtener los datos de reclamaciones basados en el cliente autenticado.
    - Utilizar la estructura de datos propuesta para recibir y devolver los datos en formato JSON.
4. Integración con Django:
    - Configurar y utilizar Django ORM para interactuar con la base de datos PostgreSQL y definir los modelos "Cliente" y "Reclamación" que se correspondan con los datos recibidos.
5. Colas de tareas:
    - Utilizar Celery para gestionar tareas en segundo plano, como el envío de información adicional en el endpoint correspondiente.
    - Configurar Celery con un broker (como RabbitMQ o Redis) y un backend para almacenar los resultados de las tareas. **(faltó de tiempo)**{: style:"color: red"}
6. Pruebas y Documentación:
    - Realizar pruebas unitarias y de integración para garantizar la calidad del código y la funcionalidad de los endpoints.
    - Documentar la API utilizando herramientas como Swagger o ReDoc, para que los clientes externos puedan entender y utilizar fácilmente los endpoints.**(faltó de tiempo)**{: style:"color: red"}
    - Mantener un control de versiones del código utilizando Git y un repositorio en Github para un seguimiento adecuado de los cambios y la colaboración en el desarrollo.

Esta es solo una propuesta inicial y la implementación exacta puede variar en función del tiempo disponible.

## Requisitos
Docker

## Instalación
```
git clone git@github.com:betocerutti/reclamador_service.git
cd reclamador_service
make up
``` 
Opcionalmente se puede importar la base de datos generada durante el desarrollo con el siguiete comando:
```
make db-restore
```

## Tests
Se han realizado pruebas unitarias y pruebas de integración utilizando el cliente de Django Rest Framework
```
make test
```

Por falta de tiempo las pruebas se han realizado con la clase Token de DRF en lugar de con JWT.
