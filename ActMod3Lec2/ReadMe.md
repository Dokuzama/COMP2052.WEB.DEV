# Login con permisos de admin y user

## Descripción
Esta aplicación permite controlar el acceso de usuarios basados en roles: Admin o Usuario. Dependiendo del rol, los usuarios pueden acceder a diferentes rutas protegidas.

## Tecnologías Utilizadas
- Python
- Flask
- Flask-Login
- Flask-Principal
- WTForms
- Visual Studio Code

## ¿Cómo correr el proyecto?
1. Activar el entorno virtual `.venv`.
2. Ejecutar el servidor con:
   ```
   python app.py
   ```
3. Abrir el navegador en:
   ```
   http://127.0.0.1:5000/login
   ```

## Rutas principales
- `/login` — Página de inicio de sesión.
- `/index` — Página principal después de iniciar sesión.
- `/admin` — Área protegida solo para usuarios con rol "admin".
- `/user` — Área protegida para usuarios con rol "user".
- `/logout` — Cerrar sesión.

## Autor
Derek J Rosa Sanchez
