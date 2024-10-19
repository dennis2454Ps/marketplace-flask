# Marketplace Backend - Flask (Gestión de Productos)

Este es el backend del microservicio de gestión de productos en el marketplace. Está construido con **Flask** (Python) y proporciona las rutas para crear, consultar, actualizar y eliminar productos.

## Requisitos

- **Python 3.7 o superior**
- **pip** (gestor de paquetes de Python)

## Instrucciones para configurar el proyecto

### 1. Clonar el repositorio
### 2. Crear un entorno virtual
python -m venv venv

venv\Scripts\activate

### 3. Instalar las dependencias
pip install -r requirements.txt
### 4. Ejecutar el servidor Flask
python app.py
---------------------------------------------------------
El servidor Flask estará corriendo en http://localhost:5000.

#### 5. Probar las rutas
Puedes probar las siguientes rutas:

GET /productos: Obtener todos los productos.
POST /productos: Crear un nuevo producto.
PUT /productos/<id>: Actualizar un producto existente.
DELETE /productos/<id>: Eliminar un producto
