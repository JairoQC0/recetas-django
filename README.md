# Recetas App - Proyecto Django

Este es un proyecto simple en **Django** para gestionar recetas. Puedes crear, editar, eliminar y ver recetas, cada una con su título, descripción, ingredientes, pasos y tiempo de preparación. El proyecto también utiliza **Bootstrap 5** para el diseño.

## 🚀 Instalación

Sigue estos pasos para configurar y ejecutar este proyecto en tu máquina local:

### 1. Clona el repositorio

Primero, clona este repositorio en tu máquina local usando Git:

`git clone https://github.com/JairoQC0/recetas-django`

`cd recetas`

### 2. Crea un entorno virtual


`python -m venv venv` 

### 3. Activa el entorno virtual

-   En Windows:
    

`venv\Scripts\activate` 

-   En macOS/Linux:
    

`source venv/bin/activate` 

### 4. Instala las dependencias

`pip install -r requirements.txt` 

### 5. Aplica migraciones a la base de datos

`python manage.py migrate` 

### 6. Crea un superusuario (opcional)

`python manage.py createsuperuser` 


### 7. Ejecuta el servidor

`python manage.py runserver` 

Visita `http://127.0.0.1:8000/` en tu navegador para usar la app
