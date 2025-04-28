# Formulario de Registro de Usuarios - Flask

Este proyecto fue desarrollado como parte de la actividad de la lección enfocada en el manejo y validación de formularios utilizando Flask y WTForms.

## Descripción

Esta aplicación permite registrar a los usuarios de manera fácil, eficiente y con validaciones básicas, como nombre, correo y contraseña.

## Tecnologías utilizadas

- Python
- Flask
- Visual Studio Code
- HTML
- WTForms

## Instrucciones para ejecutar el proyecto

1. Activar el virtual environment (.venv).
2. Instalar las dependencias necesarias con pip si es necesario (`pip install Flask Flask-WTF email-validator`).
3. Ejecutar la aplicación utilizando:

```bash
python3 app.py

4. Acceder a la applicacion a traves del navegador: http://127.0.0.1:5000/registro

Método | Ruta | Descripción
GET | /registro | Muestra el formulario de registro.
POST | /registro | Procesa el registro del usuario.
