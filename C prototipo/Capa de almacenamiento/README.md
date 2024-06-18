# Proyecto Integrador 1 - Capa de Almacenamiento

Este proyecto es parte de la materia "Proyecto Integrador 1" de la carrera "Técnico Superior en Telecomunicaciones" del ISPC. El objetivo de este proyecto es proporcionar una plantilla general de desarrollo para los alumnos, enfocada en la implementación de la capa de almacenamiento dentro de una estructura IoT de 7 capas. 

## Docente

Cristian Gonzalo Vera  
[GitHub](https://github.com/Gona79)

## Descripción General del Proyecto

El proyecto se divide en varias capas, cada una encargada de una función específica dentro de la arquitectura IoT:

1. **Capa de Percepción**: Encargada de la recolección de datos a través de sensores y dispositivos.
2. **Capa de Conectividad**: Transmisión de datos desde los dispositivos al sistema central.
3. **Capa de Preprocesamiento/Edge**: Procesamiento inicial de datos cerca de la fuente.
4. **Capa de Almacenamiento**: Almacenamiento seguro y accesible de datos.
5. **Capa de Procesamiento en la Nube**: Procesamiento avanzado y análisis de datos.
6. **Capa de Aplicación (Análisis)**: Proporciona una API RESTful para la interacción y análisis de datos.
7. **Capa de Presentación**: Diseño de interfaces de usuario para la visualización y gestión de datos.

## Stack Tecnológico Utilizado

- **Capa de Percepción**:
  - Dispositivo: ESP32-WROOM
  - Sensores y Actuadores
  - IDE: Visual Studio Code (VSCode)
  - Framework: Platformio, Arduino

- **Capa de Almacenamiento**:
  - IDE: Visual Studio Code (VSCode)
  - Bases de Datos: MySQL, MongoDB
  - Contenedores: Docker

- **Capa de Análisis (Aplicación)**:
  - IDE: Visual Studio Code (VSCode)
  - Lenguaje: Python
  - Framework: Flask para RESTful API

## Capa de Almacenamiento

Esta capa es responsable de almacenar los datos de manera segura y eficiente. Utiliza MySQL y MongoDB como sistemas de gestión de bases de datos, y Docker para su despliegue.

### Estructura del Proyecto de la Capa de Almacenamiento
    
``` plaintext

.vscode
docker
└── images
├── mongo_4.4.tar
├── mysql_8.0.tar
└── mongo
├── Dockerfile
├── mongo.conf
└── mysql
├── Dockerfile
├── mysql.conf
├── docker-compose.yml
├── README.md
src
└── mongo
├── init_db.py
├── queries.py
└── mysql
├── init_db.sql
├── queries.sql
├── app.py
├── README.md
tests
.gitignore
.dockerignore
LICENSE
README.md
```
### Descripción de Carpetas y Archivos

- **.vscode/**: Contiene configuraciones específicas para el editor Visual Studio Code.
- **docker/**: 
  - **images/**: Carpeta que contiene las imágenes Docker descargadas (`mongo_4.4.tar` y `mysql_8.0.tar`).
  - **mongo/**: 
    - **Dockerfile**: Define cómo construir la imagen Docker para MongoDB.
    - **mongo.conf**: Archivo de configuración para MongoDB.
  - **mysql/**:
    - **Dockerfile**: Define cómo construir la imagen Docker para MySQL.
    - **mysql.conf**: Archivo de configuración para MySQL.
  - **docker-compose.yml**: Define y gestiona múltiples contenedores Docker para MySQL y MongoDB.
  - **README.md**: Documentación específica para la configuración de Docker.
- **src/**:
  - **mongo/**:
    - **init_db.py**: Script para inicializar la base de datos MongoDB.
    - **queries.py**: Funciones para realizar operaciones en MongoDB.
  - **mysql/**:
    - **init_db.sql**: Script SQL para inicializar la base de datos MySQL.
    - **queries.sql**: Consultas SQL para operaciones en MySQL.
  - **app.py**: Archivo principal de la aplicación que integra las bases de datos y proporciona una API RESTful.
  - **README.md**: Documentación específica para el código fuente.
- **tests/**: Contiene pruebas automatizadas para el código fuente.
- **.gitignore**: Especifica los archivos y directorios que deben ser ignorados por Git.
- **.dockerignore**: Especifica los archivos y directorios que deben ser ignorados por Docker.
- **LICENSE**: Define los términos bajo los cuales el código del proyecto puede ser utilizado, modificado y distribuido.
- **README.md**: Documentación principal del proyecto.

### Integración de la Capa de Almacenamiento con la Capa de Análisis

La capa de almacenamiento se integra con la capa de análisis mediante una API RESTful, que proporciona endpoints para realizar operaciones CRUD (Create, Read, Update, Delete) sobre las bases de datos. La API RESTful se desarrolla utilizando Python y Flask, y se define en el archivo `app.py` en la carpeta `src`.

#### Ejemplo de Endpoints CRUD

**Para MySQL**:

```python
@app.route('/mysql/create', methods=['POST'])
def create_mysql():
    data = request.json
    cursor = mysql_conn.cursor()
    query = "INSERT INTO my_table (column1, column2) VALUES (%s, %s)"
    cursor.execute(query, (data['value1'], data['value2']))
    mysql_conn.commit()
    return jsonify({'status': 'success'})
```

**Para MongoDB:**
    
```python
@app.route('/mongo/create', methods=['POST'])
def create_mongo():
    data = request.json
    mongo_db.my_collection.insert_one(data)
    return jsonify({'status': 'success'})
```

## Despliegue
Para desplegar la capa de almacenamiento, sigue estos pasos:  

- Descargar las imágenes Docker:  

```bash
docker load -i docker/images/mysql_8.0.tar
docker load -i docker/images/mongo_4.4.tar
```
- Construir las imágenes personalizadas:  
    
```bash
docker build -t custom_mysql:1.0 -f docker/mysql/Dockerfile .
docker build -t custom_mongo:1.0 -f docker/mongo/Dockerfile .
``` 

- Iniciar los contenedores Docker:  
    
```bash
docker-compose up -d
```

### Pruebas  

Para ejecutar las pruebas, asegúrate de tener configurados los archivos de prueba en la carpeta tests. Las pruebas deben verificar la correcta interacción con las bases de datos y la API RESTful.  

### Conclusión  
Esta plantilla proporciona una base sólida para que los alumnos desarrollen sus proyectos IoT, enfocándose en la integración de la capa de almacenamiento con la capa de análisis a través de una API RESTful. Cada componente está diseñado para ser modular y escalable, facilitando el desarrollo y la implementación de aplicaciones IoT complejas.
 
