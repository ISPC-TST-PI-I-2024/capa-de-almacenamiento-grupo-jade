# Capa de Almacenamiento - MySQL

Este documento proporciona una guía detallada sobre el uso de MySQL como parte de la capa de almacenamiento en proyectos IoT. La estructura presentada aquí es parte del Proyecto Integrador 1 de la "Técnicatura Superior en Telecomunicaciones" del ISPC.

## Tabla de Contenidos

- [Capa de Almacenamiento - MySQL](#capa-de-almacenamiento---mysql)
  - [Tabla de Contenidos](#tabla-de-contenidos)
  - [Descripción General](#descripción-general)
  - [Estructura del Proyecto](#estructura-del-proyecto)
  - [Modelo de Datos Relacional](#modelo-de-datos-relacional)
    - [Diagrama del Modelo de Datos](#diagrama-del-modelo-de-datos)
  - [Detalles de las Tablas](#detalles-de-las-tablas)
    - [Tabla `Usuarios`](#tabla-usuarios)
    - [Tabla `Dispositivos`](#tabla-dispositivos)
    - [Tabla `Datos_Dispositivos`](#tabla-datos_dispositivos)
    - [Tabla `Seguridad`](#tabla-seguridad)
    - [Tabla `Proyectos`](#tabla-proyectos)
    - [Tabla `Configuraciones`](#tabla-configuraciones)
  - [Script de Inicialización](#script-de-inicialización)
  - [Consultas SQL](#consultas-sql)
  - [Seguridad y Usuarios](#seguridad-y-usuarios)
  - [Integración con la Capa de Análisis](#integración-con-la-capa-de-análisis)
  - [Endpoints](#endpoints)
  - [Ejemplos de Endpoints CRUD](#ejemplos-de-endpoints-crud)
  - [Conclusión](#conclusión)

## Descripción General

La capa de almacenamiento en este proyecto utiliza MySQL para gestionar y almacenar datos provenientes de dispositivos IoT. Este documento describe la estructura del modelo de datos relacional, los scripts de inicialización, las consultas SQL, y cómo estos elementos se integran con la capa de análisis a través de una API RESTful.

## Estructura del Proyecto

```plaintext
src
└── mysql
├── init_db.sql
├── queries.sql
├── README.md
```

## Modelo de Datos Relacional

El modelo de datos está diseñado para ser aplicable a cualquier proyecto IoT presentado. Incluye tablas para usuarios, dispositivos, datos de dispositivos, seguridad, proyectos y configuraciones.

### Diagrama del Modelo de Datos

![Diagrama ER](/Capa%20de%20almacenamiento/src/mysql/diagram.png)

## Detalles de las Tablas

### Tabla `Usuarios`

| Columna        | Tipo         | Descripción                          |
| -------------- | ------------ | ------------------------------------ |
| id_usuario     | INT          | Identificador único del usuario      |
| nombre         | VARCHAR(100) | Nombre del usuario                   |
| email          | VARCHAR(100) | Correo electrónico del usuario       |
| rol            | VARCHAR(50)  | Rol del usuario (admin, usuario)     |
| password_hash  | VARCHAR(255) | Hash de la contraseña                |
| fecha_creacion | TIMESTAMP    | Fecha de creación del registro       |

### Tabla `Dispositivos`

| Columna        | Tipo         | Descripción                          |
| -------------- | ------------ | ------------------------------------ |
| id_dispositivo | INT          | Identificador único del dispositivo  |
| nombre         | VARCHAR(100) | Nombre del dispositivo               |
| tipo           | VARCHAR(50)  | Tipo de dispositivo (sensor, actuador) |
| ubicacion      | VARCHAR(100) | Ubicación física del dispositivo     |
| id_usuario     | INT          | Relación con el usuario propietario  |

### Tabla `Datos_Dispositivos`

| Columna         | Tipo         | Descripción                          |
| --------------- | ------------ | ------------------------------------ |
| id_dato         | INT          | Identificador único del dato         |
| id_dispositivo  | INT          | Relación con el dispositivo          |
| fecha_recoleccion | TIMESTAMP  | Fecha y hora de recolección de datos |
| valor           | FLOAT        | Valor del dato recolectado           |
| unidad          | VARCHAR(20)  | Unidad de medida del dato            |

### Tabla `Seguridad`

| Columna           | Tipo         | Descripción                          |
| ----------------- | ------------ | ------------------------------------ |
| id_seguridad      | INT          | Identificador único                  |
| id_usuario        | INT          | Relación con el usuario              |
| id_dispositivo    | INT          | Relación con el dispositivo          |
| permisos          | VARCHAR(50)  | Permisos otorgados (lectura, escritura) |
| fecha_asignacion  | TIMESTAMP    | Fecha de asignación de permisos      |

### Tabla `Proyectos`

| Columna         | Tipo         | Descripción                          |
| --------------- | ------------ | ------------------------------------ |
| id_proyecto     | INT          | Identificador único del proyecto     |
| nombre          | VARCHAR(100) | Nombre del proyecto                  |
| descripcion     | TEXT         | Descripción detallada del proyecto   |
| id_usuario      | INT          | Relación con el usuario propietario  |
| fecha_inicio    | DATE         | Fecha de inicio del proyecto         |
| fecha_fin       | DATE         | Fecha de finalización del proyecto   |

### Tabla `Configuraciones`

| Columna           | Tipo         | Descripción                          |
| ----------------- | ------------ | ------------------------------------ |
| id_configuracion  | INT          | Identificador único de la configuración |
| id_dispositivo    | INT          | Relación con el dispositivo          |
| parametro         | VARCHAR(50)  | Nombre del parámetro                 |
| valor             | VARCHAR(100) | Valor del parámetro                  |
| fecha_asignacion  | TIMESTAMP    | Fecha de asignación de la configuración |

## Script de Inicialización

El archivo `init_db.sql` contiene el script SQL para inicializar la base de datos y crear las tablas descritas.

```sql
-- Crear base de datos
CREATE DATABASE IF NOT EXISTS iot_project;
USE iot_project;

-- Crear tabla Usuarios
CREATE TABLE IF NOT EXISTS Usuarios (
    id_usuario INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    rol VARCHAR(50) NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Crear tabla Dispositivos
CREATE TABLE IF NOT EXISTS Dispositivos (
    id_dispositivo INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    tipo VARCHAR(50) NOT NULL,
    ubicacion VARCHAR(100),
    id_usuario INT,
    FOREIGN KEY (id_usuario) REFERENCES Usuarios(id_usuario)
);

-- Crear tabla Datos_Dispositivos
CREATE TABLE IF NOT EXISTS Datos_Dispositivos (
    id_dato INT AUTO_INCREMENT PRIMARY KEY,
    id_dispositivo INT,
    fecha_recoleccion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    valor FLOAT,
    unidad VARCHAR(20),
    FOREIGN KEY (id_dispositivo) REFERENCES Dispositivos(id_dispositivo)
);

-- Crear tabla Seguridad
CREATE TABLE IF NOT EXISTS Seguridad (
    id_seguridad INT AUTO_INCREMENT PRIMARY KEY,
    id_usuario INT,
    id_dispositivo INT,
    permisos VARCHAR(50),
    fecha_asignacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (id_usuario) REFERENCES Usuarios(id_usuario),
    FOREIGN KEY (id_dispositivo) REFERENCES Dispositivos(id_dispositivo)
);

-- Crear tabla Proyectos
CREATE TABLE IF NOT EXISTS Proyectos (
    id_proyecto INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    descripcion TEXT,
    id_usuario INT,
    fecha_inicio DATE,
    fecha_fin DATE,
    FOREIGN KEY (id_usuario) REFERENCES Usuarios(id_usuario)
);

-- Crear tabla Configuraciones
CREATE TABLE IF NOT EXISTS Configuraciones (
    id_configuracion INT AUTO_INCREMENT PRIMARY KEY,
    id_dispositivo INT,
    parametro VARCHAR(50),
    valor VARCHAR(100),
    fecha_asignacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (id_dispositivo) REFERENCES Dispositivos(id_dispositivo)
);
```

## Consultas SQL  
El archivo queries.sql contiene ejemplos de consultas SQL para realizar operaciones CRUD (Create, Read, Update, Delete).  

**Ejemplos de Consultas**  

- Insertar un nuevo usuario:

``` sql
INSERT INTO Usuarios (nombre, email, rol, password_hash) VALUES ('Juan Pérez', 'juan@example.com', 'usuario', 'hashed_password');
```
- Seleccionar todos los dispositivos:  
```sql
SELECT * FROM Dispositivos;  
```  

- Actualizar la ubicación de un dispositivo:  
``` sql
UPDATE Dispositivos SET ubicacion = 'Laboratorio 1' WHERE id_dispositivo = 1;
```  

- Eliminar un proyecto:  
``` sql
DELETE FROM Proyectos WHERE id_proyecto = 1;  
```  

## Seguridad y Usuarios  
La tabla Seguridad gestiona los permisos y las relaciones entre usuarios y dispositivos, asegurando que solo los usuarios autorizados puedan acceder o modificar los datos de los dispositivos.  

## Integración con la Capa de Análisis
La capa de almacenamiento se integra con la capa de análisis mediante una API RESTful que proporciona endpoints para realizar operaciones CRUD sobre las bases de datos. Esta API se desarrolla utilizando Python y Flask, y se define en el archivo app.py en la carpeta src.  

## Endpoints  
Los endpoints son puntos de acceso específicos a una API, estos permiten a los usuarios interactuar con el sistema mediante direcciones URL que se utilizan para realizar operaciones sobre los datos.  

**GET /datos**  
Mediante el método HTTP GET se obtiene una lista de todos los datos. Este método no requiere parámetros adicionales en la URL.

**POST /datos**  
Mediante el método HTTP POST se crear un nuevo dato. El mismo requiere especificar (en formato JSON, o XML) en el cuerpo de la solicitud con los detalles del nuevo dato.
  
**PUT /datos/{id}**  
Mediante el método HTTP PUT se actualiza la información de un dato específico. El mismo equiere un parámetro en la URL ({id}) que identifica el dato a actualizar, asi como especificar (en formato JSON, o XML) en el cuerpo de la solicitud los nuevos valores.  
  
**DELETE /datos/{id}**  
Mediante eL método HTTP DELETE se elimina un dato específico. El mismo requiere un parámetro en la URL ({id}) que identifica el dato a eliminar.

En resumen, los endpoints son las direcciones específicas a las que se puede enviar solicitudes HTTP (GET, POST, PUT, DELETE, etc.) para realizar operaciones CRUD.  
  
## Ejemplos de Endpoints CRUD  

- Obtener un dato:

``` python
    @app.route('/mysql/read', methods=['GET'])
    def read_mysql():
        cursor = mysql_conn.cursor()
        query = "SELECT * FROM Datos_Dispositivos"
        cursor.execute(query)
        result = cursor.fetchall()
        return jsonify(result)
```  
- Crear un nuevo dato:  
``` python
    @app.route('/mysql/create', methods=['POST'])
    def create_mysql():
        data = request.json
        cursor = mysql_conn.cursor()
        query = "INSERT INTO Datos_Dispositivos (id_dispositivo, fecha_recoleccion, valor, unidad) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, (data['id_dispositivo'], data['fecha_recoleccion'], data['valor'], data['unidad']))
        mysql_conn.commit()
        return jsonify({'status': 'success'})
```  
- Actualizar un dato:  
``` python
   @app.route('/mysql/update/<int:id_dispositivo>', methods=['PUT'])
    def update_mysql(id_dispositivo):
        data = request.json
        cursor = mysql_conn.cursor()
        query = "UPDATE Datos_Dispositivos SET fecha_recoleccion = %s, valor = %s, unidad = %s WHERE id_dispositivo = %s"
        cursor.execute(query, (data['fecha_recoleccion'], data['valor'], data['unidad'], id_dispositivo))
        mysql_conn.commit()
        if cursor.rowcount == 0:
            return jsonify({'error': 'Dispositivo no encontrado'}), 404
        return jsonify({'status': 'success'})
```  
 - Eliminar un dato:
``` python
    @app.route('/mysql/delete/<int:id_dispositivo>', methods=['DELETE'])
    def delete_mysql(id_dispositivo):
        cursor = mysql_conn.cursor()
        query = "DELETE FROM Datos_Dispositivos WHERE id_dispositivo = %s"
        cursor.execute(query, (id_dispositivo,))
        mysql_conn.commit()
        if cursor.rowcount == 0:
            return jsonify({'error': 'Dispositivo no encontrado'}), 404
        return jsonify({'status': 'success'})
```  
## Conclusión  
Este documento proporciona una guía completa para la implementación y uso de MySQL en la capa de almacenamiento de proyectos IoT. Con un modelo de datos relacional bien definido y scripts claros para inicialización y consultas, este recurso facilita el desarrollo y la integración de la capa de almacenamiento con otras capas del sistema IoT.