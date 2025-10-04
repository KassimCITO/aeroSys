# Manual de Usuario - Sistema de Gestión de Aeropuertos

## Tabla de Contenidos
1. [Introducción](#introducción)
2. [Instalación y Configuración](#instalación-y-configuración)
3. [Acceso al Sistema](#acceso-al-sistema)
4. [Dashboard Principal](#dashboard-principal)
5. [Gestión de Aeronaves](#gestión-de-aeronaves)
6. [Gestión de Pilotos](#gestión-de-pilotos)
7. [Gestión de Vuelos](#gestión-de-vuelos)
8. [Gestión de Confirmaciones](#gestión-de-confirmaciones)
9. [Gestión de Usuarios](#gestión-de-usuarios)
10. [Reportes](#reportes)
11. [Configuración del Sistema](#configuración-del-sistema)
12. [Solución de Problemas](#solución-de-problemas)

## Introducción

El Sistema de Gestión de Aeropuertos es una aplicación web desarrollada en Flask que permite gestionar de manera integral las operaciones de un aeropuerto, incluyendo la administración de aeronaves, pilotos, vuelos, confirmaciones y usuarios.

### Características Principales
- **Dashboard intuitivo** con estadísticas en tiempo real
- **Gestión completa de aeronaves** con imágenes
- **Administración de pilotos** con información detallada
- **Control de vuelos** con asignación de aeronaves y pilotos
- **Sistema de confirmaciones** para seguimiento de vuelos
- **Gestión de usuarios** con diferentes roles
- **Reportes en PDF y Excel**
- **Interfaz responsive** compatible con dispositivos móviles

## Instalación y Configuración

### Requisitos del Sistema
- Python 3.8 o superior
- pip (gestor de paquetes de Python)
- Navegador web moderno

### Instalación Automática
1. Descarga el proyecto desde el repositorio
2. Ejecuta el script de instalación:
   ```bash
   python install.py
   ```
3. Sigue las instrucciones en pantalla
4. El sistema creará automáticamente:
   - Entorno virtual
   - Instalación de dependencias
   - Base de datos inicial
   - Usuario administrador

### Instalación Manual
1. Crea un entorno virtual:
   ```bash
   python -m venv venv
   ```

2. Activa el entorno virtual:
   - Windows: `venv\Scripts\activate`
   - Linux/Mac: `source venv/bin/activate`

3. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

4. Configura la base de datos:
   ```bash
   python -m flask db upgrade
   ```

5. Pobla la base de datos con datos de ejemplo:
   ```bash
   python seed.py
   ```

6. Ejecuta la aplicación:
   ```bash
   python app.py
   ```

## Acceso al Sistema

### Credenciales por Defecto
- **Usuario:** admin
- **Contraseña:** 123456

### Primer Acceso
1. Abre tu navegador web
2. Navega a `http://localhost:5000`
3. Ingresa las credenciales de administrador
4. Cambia la contraseña por defecto en la primera sesión

### Roles de Usuario
- **Administrador:** Acceso completo al sistema
- **Operador:** Gestión de vuelos y confirmaciones
- **Piloto:** Consulta de vuelos asignados
- **Invitado:** Acceso de solo lectura

## Dashboard Principal

El dashboard es la pantalla principal del sistema y muestra:

### Estadísticas Generales
- Total de aeronaves registradas
- Número de pilotos activos
- Vuelos programados
- Confirmaciones pendientes

### Accesos Rápidos
- Botones para acceder a cada módulo
- Enlaces a reportes más utilizados
- Acceso a configuración del sistema

### Información del Sistema
- Estado de la base de datos
- Última actualización
- Usuario conectado

## Gestión de Aeronaves

### Agregar Nueva Aeronave
1. Navega a "Aeronaves" en el menú principal
2. Haz clic en "Agregar Aeronave"
3. Completa el formulario:
   - **Matrícula:** Identificador único de la aeronave
   - **Modelo:** Modelo de la aeronave
   - **Fabricante:** Empresa fabricante
   - **Capacidad:** Número de pasajeros
   - **Tipo:** Comercial, privado, etc.
   - **Imagen:** Foto de la aeronave (opcional)
4. Haz clic en "Guardar"

### Editar Aeronave
1. En la lista de aeronaves, haz clic en el botón "Editar"
2. Modifica los campos necesarios
3. Haz clic en "Actualizar"

### Eliminar Aeronave
1. Haz clic en el botón "Eliminar"
2. Confirma la eliminación
3. La aeronave se eliminará del sistema

### Filtros y Búsqueda
- Filtra por fabricante
- Filtra por tipo de aeronave
- Busca por matrícula o modelo

## Gestión de Pilotos

### Agregar Nuevo Piloto
1. Navega a "Pilotos" en el menú principal
2. Haz clic en "Agregar Piloto"
3. Completa el formulario:
   - **Nombre:** Nombre completo del piloto
   - **Licencia:** Número de licencia
   - **Tipo de Licencia:** ATPL, CPL, PPL, etc.
   - **Horas de Vuelo:** Experiencia del piloto
   - **Nacionalidad:** País de origen
4. Haz clic en "Guardar"

### Editar Piloto
1. En la lista de pilotos, haz clic en "Editar"
2. Modifica la información necesaria
3. Haz clic en "Actualizar"

### Eliminar Piloto
1. Haz clic en el botón "Eliminar"
2. Confirma la eliminación

### Filtros
- Filtra por tipo de licencia
- Filtra por nacionalidad
- Busca por nombre o licencia

## Gestión de Vuelos

### Crear Nuevo Vuelo
1. Navega a "Vuelos" en el menú principal
2. Haz clic en "Agregar Vuelo"
3. Completa el formulario:
   - **Número de Vuelo:** Código único del vuelo
   - **Origen:** Aeropuerto de salida
   - **Destino:** Aeropuerto de llegada
   - **Fecha de Salida:** Fecha y hora de partida
   - **Fecha de Llegada:** Fecha y hora de llegada
   - **Aeronave:** Selecciona la aeronave
   - **Piloto:** Piloto al mando
   - **Copiloto:** Piloto secundario (opcional)
   - **Observaciones:** Notas adicionales
4. Haz clic en "Guardar"

### Editar Vuelo
1. En la lista de vuelos, haz clic en "Editar"
2. Modifica la información necesaria
3. Haz clic en "Actualizar"

### Confirmar Vuelo
1. Haz clic en el botón "Confirmar" junto al vuelo
2. Selecciona el estado:
   - **Confirmado:** Vuelo aprobado
   - **Pendiente:** Esperando confirmación
   - **Cancelado:** Vuelo cancelado
3. Agrega notas si es necesario
4. Haz clic en "Guardar Confirmación"

### Filtros
- Filtra por estado del vuelo
- Filtra por fecha
- Filtra por aeronave o piloto

## Gestión de Confirmaciones

### Ver Confirmaciones
1. Navega a "Confirmaciones" en el menú principal
2. Visualiza todas las confirmaciones de vuelos
3. Filtra por estado o vuelo específico

### Agregar Confirmación
1. Haz clic en "Agregar Confirmación"
2. Selecciona el vuelo
3. Establece el estado
4. Agrega notas si es necesario
5. Haz clic en "Guardar"

### Editar Confirmación
1. Haz clic en "Editar" junto a la confirmación
2. Modifica el estado o las notas
3. Haz clic en "Actualizar"

## Gestión de Usuarios

### Agregar Usuario
1. Navega a "Usuarios" (solo administradores)
2. Haz clic en "Agregar Usuario"
3. Completa el formulario:
   - **Nombre de Usuario:** Identificador único
   - **Contraseña:** Contraseña segura
   - **Rol:** Administrador, Operador, Piloto, Invitado
4. Haz clic en "Guardar"

### Editar Usuario
1. Haz clic en "Editar" junto al usuario
2. Modifica la información necesaria
3. Haz clic en "Actualizar"

### Eliminar Usuario
1. Haz clic en "Eliminar"
2. Confirma la eliminación

## Reportes

### Generar Reportes
1. Navega a "Reportes" en el menú principal
2. Selecciona el tipo de reporte:
   - **Aeronaves:** Lista de aeronaves con filtros
   - **Pilotos:** Información de pilotos
   - **Vuelos:** Detalles de vuelos
   - **Confirmaciones:** Estado de confirmaciones
   - **Dashboard:** Estadísticas generales

### Filtros de Reportes
- Aplica filtros según el tipo de reporte
- Selecciona formato: PDF o Excel
- Haz clic en "Generar Reporte"

### Exportar Reportes
- Los reportes se descargan automáticamente
- Formato PDF para impresión
- Formato Excel para análisis de datos

## Configuración del Sistema

### Configuración del Aeropuerto
1. Navega a "Configuración" en el menú principal
2. Completa la información del aeropuerto:
   - **Nombre:** Nombre oficial del aeropuerto
   - **Códigos:** IATA e ICAO
   - **Dirección:** Ubicación física
   - **Contacto:** Teléfono y email
3. Haz clic en "Guardar"

### Configuración de Usuario
1. Haz clic en tu nombre de usuario
2. Selecciona "Configuración"
3. Modifica tu información personal
4. Cambia tu contraseña si es necesario

## Solución de Problemas

### Problemas Comunes

#### Error de Conexión a Base de Datos
- Verifica que la base de datos esté creada
- Ejecuta: `python -m flask db upgrade`

#### Error de Permisos
- Verifica que el usuario tenga el rol correcto
- Contacta al administrador del sistema

#### Error de Archivos
- Verifica que el directorio `static/uploads` exista
- Verifica permisos de escritura

#### Error de Imágenes
- Verifica que las imágenes estén en formato válido
- Tamaño máximo: 16MB
- Formatos permitidos: JPG, JPEG, PNG, GIF

### Logs del Sistema
- Los logs se guardan en `app.log`
- Revisa los logs para errores específicos
- Contacta al soporte técnico si es necesario

### Contacto de Soporte
- **Email:** soporte@aeropuerto-cit.com
- **Teléfono:** +52 (55) 1234-5678
- **Horario:** Lunes a Viernes, 8:00 AM - 6:00 PM

---

**Versión del Manual:** 1.0  
**Última Actualización:** Octubre 2025  
**Sistema:** Sistema de Gestión de Aeropuertos v1.0