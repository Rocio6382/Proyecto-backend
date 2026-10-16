-- Script de Creación de BD y Permisos para Sistema de Inventario PYME
CREATE DATABASE IF NOT EXISTS pyme_inventario_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

CREATE USER 'pyme_admin'@'%' IDENTIFIED BY 'Pyme_SecurePass_2026!';

GRANT ALL PRIVILEGES ON pyme_inventario_db.* TO 'pyme_admin'@'%';

FLUSH PRIVILEGES;