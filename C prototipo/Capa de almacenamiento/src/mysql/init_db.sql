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