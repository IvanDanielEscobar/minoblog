# Miniblog en Flask

Este es un proyecto de un miniblog con Flask de Python.
Permite a los usuarios crear, visualizar y comentar posteos.

---

## Requisitos

- Python 3.8+
- MySQL Server (local o remoto)

---

## Configuración del Entorno de Desarrollo

Sigue estos pasos para poner en marcha el proyecto:

1.  **Clona el repositorio:**

    ```bash
    git clone https://github.com/IvanDanielEscobar/minoblog.git
    cd EFI-python
    ```

    (Reemplaza `tu-usuario/miniblog.git` con la URL real de tu repositorio).

2.  **Crea y activa el entorno virtual:**

    ```bash
    # En Linux:
    source .venv/bin/activate
    ```

3.  **Instala las dependencias:**

    ```bash
    pip install Flask Flask-SQLAlchemy Flask-Migrate pymysql
    ```

4.  **Configura la Base de Datos MySQL:**

    - Crea una base de datos llamada `miniblog` en tu servidor MySQL.
      ```sql
      CREATE DATABASE miniblog;
      ```
    - Asegúrate de que tu usuario de MySQL (por ejemplo, `root` con o sin contraseña) tenga permisos para acceder a esta base de datos.
    - Abre `app.py` y verifica que la línea `app.config['SQLALCHEMY_DATABASE_URI']` tenga las credenciales correctas:
      ```python
      app.config['SQLALCHEMY_DATABASE_URI'] = (
          "mysql+pymysql://root:@localhost/miniblog" # Ajustar contraseña o usuario/host
      )
      ```

5.  **Ejecuta las migraciones de la base de datos:**

    - Con el entorno virtual activado y MySQL corriendo.
    - Establece la variable de entorno para Flask:
      ```bash
      # En Linux:
      export FLASK_APP=app.py
      ```
    - Inicializa el repositorio de migraciones (solo la primera vez):
      ```bash
      flask db init
      ```
    - Genera las migraciones para tus modelos (ejecuta esto cada vez que cambies los modelos):
      ```bash
      flask db migrate -m "Initial database setup"
      ```
    - Aplica las migraciones a la base de datos:
      ```bash
      flask db upgrade
      ```

## Ejecutar la Aplicación

```bash
flask run
```
