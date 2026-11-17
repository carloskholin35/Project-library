# Biblioteca personal

Aplicación web sencilla para llevar un registro de los libros que leo. Es un proyecto personal que hago fuera de clase para practicar el desarrollo backend con Python y SQL.

> Proyecto de aprendizaje, ahora mismo pausado.

## Tecnologías

- Python 3 y Flask
- SQLite, con las consultas SQL escritas a mano usando el módulo `sqlite3` de Python
- Plantillas Jinja2, HTML y CSS

## Qué hace ahora mismo

- Añadir, ver, editar y borrar libros (CRUD).
- Cada libro tiene autor, géneros, año de publicación y portada (opcional).
- Los autores se guardan en su propia tabla: si el autor ya existe se reutiliza, y si no, se crea.
- Comprobaciones al crear y al borrar, con mensajes para el usuario.
- Consultas con parámetros (`?`) para evitar inyección SQL.

## Base de datos

El esquema evoluciona con migraciones numeradas en `migrations/` (libros, autores, géneros, usuarios, lecturas y "me gusta"). Las tablas de usuarios y lecturas están creadas, pero no se usan desde la interfaz.

## Cómo ejecutarlo

En Windows (PowerShell):

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt

# Crear la base de datos aplicando las migraciones en orden
Get-ChildItem migrations\*.py | ForEach-Object { python $_.FullName }
python seeds\001_seed_genres.py

flask run
```

Después, abre http://127.0.0.1:5000.

## Ideas pendientes

- Registrar lecturas por usuario (fecha, valoración).
- Mejorar la validación de autores para evitar duplicados por erratas.
- Mejorar el diseño de la interfaz.
