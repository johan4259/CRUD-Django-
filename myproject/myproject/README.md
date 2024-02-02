# Mi API REST de Gestión de Clientes, Facturas y Productos

## Introducción
Esta API REST ha sido desarrollada utilizando Django y Django REST Framework. Permite realizar operaciones CRUD (Crear, Leer, Actualizar, Eliminar) en entidades como Clientes, Facturas y Productos. Además, incluye funcionalidades como autenticación basada en JSON Web Tokens (JWT), importación y exportación de datos de clientes en formato CSV, y ejecución de consultas SQL directas para ciertas operaciones.

## Configuración del Entorno

### Requisitos Previos
- Python 3.8+
- Django 3.2+
- Django REST Framework
- Otros paquetes especificados en `requirements.txt`

### Instalación y Configuración
1. Clona el repositorio de GitHub:
2. Instala las dependencias:
3. Configura la base de datos (PostgreSQL recomendada) en `settings.py`. 
4. Realiza las migraciones para crear las tablas en la base de datos:

## Ejecución

Para iniciar el servidor de desarrollo de Django:

La API estará disponible en `http://localhost:8000/`.

## Autenticación

La API usa JWT para la autenticación. Los tokens deben enviarse en el encabezado de autorización de las solicitudes HTTP.

### Registro de Usuarios

- **URL**: `/register/`
- **Método**: `POST`
- **Cuerpo de la solicitud**: `{"username": "usuario", "password": "contraseña"}`
- **Respuesta exitosa**: Código 201, devuelve token de acceso y actualización.

### Obtener Token de Acceso

- **URL**: `/token/`
- **Método**: `POST`
- **Cuerpo de la solicitud**: `{"username": "usuario", "password": "contraseña"}`
- **Respuesta exitosa**: Código 200, devuelve token de acceso y actualización.

## Endpoints

### Clientes

#### Obtener Clientes
- **URL**: `/clients/`
- **Método**: `GET`

#### Crear Cliente
- **URL**: `/clients/`
- **Método**: `POST`

### Productos

#### Obtener Productos
- **URL**: `/products/`
- **Método**: `GET`

#### Crear Producto
- **URL**: `/products/`
- **Método**: `POST`

### Facturas

#### Obtener Facturas
- **URL**: `/bills/`
- **Método**: `GET`

#### Crear Factura
- **URL**: `/bills/`
- **Método**: `POST`

### Importación/Exportación de CSV

#### Exportar Clientes a CSV
- **URL**: `/clients/csv_export/`
- **Método**: `GET`

#### Importar Clientes desde CSV
- **URL**: `/clients/csv_import/`
- **Método**: `POST`

## Manejo de Errores

Descripción de cómo la API maneja y reporta errores comunes, incluyendo códigos de estado y mensajes de error.

## Pruebas

Instrucciones sobre cómo ejecutar pruebas unitarias o de integración, si están disponibles.

## Contribuir

Si estás interesado en contribuir a este proyecto, por favor lee las siguientes instrucciones.

## Contacto

Nota: Asegúrate de revisar y personalizar cada sección de este esquema para que refleje con precisión los detalles y características de tu API.
