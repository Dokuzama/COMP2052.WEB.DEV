# Proyecto de Usuarios - API Flask

Este proyecto fue desarrollado como parte del curso COMP2052.WEB DEV SERV-SIDE&MICROSER BKE.

##  Descripción

La aplicación es una API REST construida con Flask que permite:

- Crear nuevos usuarios.
- Consultar información general del sistema.
- Listar los usuarios almacenados en memoria.

---

## Tecnologías utilizadas

- Python 3
- Flask
- JSON
- Visual Studio Code

---

## Cómo correr la aplicación

1. Activar la máquina virtual.
2. Ejecutar el siguiente comando:

```bash
python app.py

3. Acceder a las rutas desde el navegador o usando curl o Postman.

Método | Ruta | Descripción
GET | /info | Devuelve información general del sistema
POST | /crear_usuario | Crea un usuario con nombre y correo
GET | /usuarios | Lista todos los usuarios creados