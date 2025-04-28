# Sistema de Login

Este proyecto fue desarrollado como parte de la actividad de la lección enfocada en la creación de un sistema de autenticación simple utilizando Flask.

## Descripción

Esta aplicación permite a los usuarios iniciar sesión y cerrar sesión de manera sencilla y segura, usando Flask y buenas prácticas de autenticación básica.

## Tecnologías utilizadas

- Python 3
- Flask
- Flask-Login
- Werkzeug
- HTML básico

## Funcionalidades

- Inicio de sesión con validación de usuario y contraseña.
- Cierre de sesión seguro mediante un botón de formulario (método POST).
- Página protegida accesible solo después de autenticar.
- Mensajes Flash para notificar acciones al usuario.

## Cómo ejecutar el proyecto

1. Clona este repositorio.
2. Instala las dependencias necesarias:
3. Ejecuta la aplicación: pip install flask flask-login werkzeug
4. Accede a la aplicación a través del navegador: python app.py


## Rutas de la aplicación

| Método | Ruta      | Descripción                                |
|:-------|:----------|:-------------------------------------------|
| GET    | /login     | Muestra el formulario de inicio de sesión |
| POST   | /login     | Procesa el inicio de sesión               |
| GET    | /protegido | Página protegida para usuarios logueados  |
| POST   | /logout    | Cierra la sesión de forma segura          |

## Autor

Derek J Rosa Sanchez

