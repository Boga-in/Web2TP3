# PROGRAMACION WEB II
# TRABAJO PRACTICO N°3

[Informe realizado](InformeTP3.pdf)

# Proyecto: Blog

*El objetivo de este trabajo práctico es que las/os estudiantes desarrollen un proyecto llamado Blog y una aplicación denominada post utilizando Django y el patrón de diseño MVT. 
*Se espera que implementen funcionalidades esenciales para la gestión de publicaciones (post) en un blog, trabajando con vistas, plantillas y modelos, así como la
integración con GitHub y el uso de un entorno virtual. 
*En forma adicional se busca que los estudiantes puedan implementar un middleware personalizado y que habiliten y utilicen el middleware de autenticación que provee Django


# Requisitos

- Python 3.11.0rc1
- Django 4.2

# Instalación

1. **Clonar el repositorio**:
    ```bash
    git clone git@github.com:Boga-in/Web2TP3.git
    ```
2. **Desplazarnos al repositorio creado**:
    ```bash
    cd Web2TP3
    ```
3. **Crear un entorno virtual**:
    ```bash
    virtualenv env
    ```
4. **Activar el entorno virtual**:
    ```bash
    source venv/bin/activate 
    ```
5. **Instalar los requirimientos**:
    ```bash
    pip install -r requirements.txt
    ```
6. **Aplicar las migraciones**:
    ```bash
    python manage.py migrate
    ```

7. **Inicia el servidor**:
    ```bash
    python manage.py runserver
    ```

## Desarrollo

<h3> Planificación del Proyecto:</h3>
<li>Definición de requisitos y funcionalidades la aplicacion de post</li>
<li>Diseño del archivo models</li>

<h3> Configuración del Entorno:</h3>
<li>Instalación de Django y configuración del entorno virtual.</li>
<li>Creación de un repositorio en GitHub.</li>

<h3>Desarrollo de Modelos:</h3>
<li>Implementación del modelo Post para almacenar información sobre los posteos.</li>
<li>Creación de migraciones y aplicación de las mismas para crear las tablas en la base de datos.</li>

<h3>Desarrollo de Vistas:</h3>
<li>Implementación de la creación, visualización y eliminación de posteos.</li>
<li>Manejo de Sesion con implementacion del modelo de User de Django.</li>

<h3>Desarrollo de Plantillas:</h3>
<li>Creación de plantillas HTML utilizando Django Template Language</li>
<li>Implementación de formularios para la creación y edicion de posteos</li>

<h3>Pruebas:</h3>
<li>Pruebas manuales para asegurar que todas funcione correctamente.</li>
<li>Corrección de errores y optimización del código.</li>
