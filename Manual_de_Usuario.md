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
9. [Sistema de Reportes](#sistema-de-reportes)
10. [Configuración del Aeropuerto](#configuración-del-aeropuerto)
11. [Gestión de Usuarios](#gestión-de-usuarios)
12. [Solución de Problemas](#solución-de-problemas)

---

## Introducción

El **Sistema de Gestión de Aeropuertos** es una aplicación web desarrollada en Flask que permite la administración completa de operaciones aeroportuarias. El sistema incluye gestión de aeronaves, pilotos, vuelos, confirmaciones y reportes detallados.

### Características Principales
- ✅ **Dashboard interactivo** con estadísticas en tiempo real
- ✅ **Gestión completa de aeronaves** (matrícula, modelo, fabricante, capacidad)
- ✅ **Administración de pilotos** con licencias y horas de vuelo
- ✅ **Control de vuelos** con rutas, horarios y estados
- ✅ **Sistema de confirmaciones** para operadores autorizados
- ✅ **Reportes en PDF y Excel** con filtros avanzados
- ✅ **Configuración del aeropuerto** personalizable
- ✅ **Gestión de usuarios** con diferentes roles
- ✅ **Tema claro/oscuro** adaptable
- ✅ **Footer informativo** siempre visible

---

## Instalación y Configuración

### Requisitos del Sistema
- Python 3.8 o superior
- Navegador web moderno (Chrome, Firefox, Safari, Edge)
- 2GB de RAM mínimo
- 500MB de espacio en disco

### Paso 1: Descargar el Proyecto
```bash
# Clonar o descargar el proyecto
git clone [URL_DEL_REPOSITORIO]
cd aeroSys
```

### Paso 2: Crear Entorno Virtual
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python -m venv venv
source venv/bin/activate
```

### Paso 3: Instalar Dependencias
```bash
pip install -r requirements.txt
```

### Paso 4: Configurar Base de Datos
```bash
# Poblar la base de datos con datos de ejemplo
python seed.py
```

### Paso 5: Ejecutar la Aplicación
```bash
python app.py
```

### Paso 6: Acceder al Sistema
Abrir el navegador y navegar a: `http://127.0.0.1:5000`

---

## Acceso al Sistema

### Pantalla de Login
![Pantalla de Login](https://via.placeholder.com/800x400/007bff/ffffff?text=Pantalla+de+Login)

**Credenciales por defecto:**
- **Usuario:** `admin`
- **Contraseña:** `123456`

### Proceso de Inicio de Sesión
1. Ingrese su nombre de usuario
2. Ingrese su contraseña
3. Haga clic en "Iniciar Sesión"
4. Será redirigido al Dashboard principal

### Roles de Usuario
- **Administrador:** Acceso completo a todas las funcionalidades
- **Operador:** Puede gestionar vuelos y confirmaciones
- **Piloto:** Acceso limitado (solo lectura)
- **Invitado:** Acceso muy limitado

---

## Dashboard Principal

### Vista General
![Dashboard Principal](https://via.placeholder.com/1200x600/28a745/ffffff?text=Dashboard+Principal)

El Dashboard es la pantalla principal que muestra:
- **Estadísticas en tiempo real** de aeronaves, pilotos, vuelos y confirmaciones
- **Accesos rápidos** a todas las secciones del sistema
- **Enlaces a reportes** en PDF y Excel
- **Información del aeropuerto** en el footer fijo

### Tarjetas de Estadísticas
Cada tarjeta muestra:
- **Número total** de registros
- **Icono representativo** de la sección
- **Enlace directo** para ver detalles

### Acciones Rápidas
- **Gestionar Aeronaves:** Acceso directo a la gestión de aeronaves
- **Gestionar Pilotos:** Acceso directo a la gestión de pilotos
- **Gestionar Vuelos:** Acceso directo a la gestión de vuelos
- **Gestionar Confirmaciones:** Acceso directo a las confirmaciones

### Sección de Reportes
- **Reporte General:** Estadísticas completas del sistema
- **Reporte Aeronaves:** Listado detallado de aeronaves
- **Reporte Pilotos:** Información de pilotos
- **Reporte Vuelos:** Detalles de vuelos
- **Reporte Confirmaciones:** Estado de confirmaciones

---

## Gestión de Aeronaves

### Vista Principal
![Gestión de Aeronaves](https://via.placeholder.com/1200x600/17a2b8/ffffff?text=Gestión+de+Aeronaves)

### Agregar Nueva Aeronave
1. Haga clic en el botón **"Nueva Aeronave"**
2. Complete el formulario:
   - **Matrícula:** Identificador único de la aeronave
   - **Modelo:** Modelo de la aeronave
   - **Fabricante:** Empresa fabricante
   - **Capacidad:** Número de pasajeros
   - **Tipo de Aeronave:** Categoría (Comercial, Privada, etc.)
3. Haga clic en **"Guardar"**

### Editar Aeronave
1. Localice la aeronave en la tabla
2. Haga clic en el botón **"Editar"** (ícono de lápiz)
3. Modifique los campos necesarios
4. Haga clic en **"Guardar"**

### Eliminar Aeronave
1. Localice la aeronave en la tabla
2. Haga clic en el botón **"Eliminar"** (ícono de papelera)
3. Confirme la eliminación en el diálogo

### Filtros y Búsqueda
- **Filtro por Fabricante:** Seleccione un fabricante específico
- **Filtro por Tipo:** Filtre por tipo de aeronave
- **Exportar PDF/Excel:** Genere reportes de las aeronaves filtradas

---

## Gestión de Pilotos

### Vista Principal
![Gestión de Pilotos](https://via.placeholder.com/1200x600/ffc107/000000?text=Gestión+de+Pilotos)

### Agregar Nuevo Piloto
1. Haga clic en el botón **"Nuevo Piloto"**
2. Complete el formulario:
   - **Nombre:** Nombre completo del piloto
   - **Licencia:** Número de licencia de vuelo
   - **Horas de Vuelo:** Total de horas acumuladas
3. Haga clic en **"Guardar"**

### Editar Piloto
1. Localice el piloto en la tabla
2. Haga clic en el botón **"Editar"**
3. Modifique los campos necesarios
4. Haga clic en **"Guardar"**

### Eliminar Piloto
1. Localice el piloto en la tabla
2. Haga clic en el botón **"Eliminar"**
3. Confirme la eliminación

### Filtros Disponibles
- **Filtro por Tipo de Licencia:** (Funcionalidad futura)
- **Filtro por Nacionalidad:** (Funcionalidad futura)
- **Exportar Reportes:** PDF y Excel

---

## Gestión de Vuelos

### Vista Principal
![Gestión de Vuelos](https://via.placeholder.com/1200x600/6f42c1/ffffff?text=Gestión+de+Vuelos)

### Agregar Nuevo Vuelo
1. Haga clic en el botón **"Nuevo Vuelo"**
2. Complete el formulario:
   - **Número de Vuelo:** Código único del vuelo
   - **Aeronave:** Seleccione de la lista desplegable
   - **Origen:** Aeropuerto de salida
   - **Destino:** Aeropuerto de llegada
   - **Fecha y Hora de Salida:** Programación de salida
   - **Fecha y Hora de Llegada:** Programación de llegada
   - **Piloto:** Seleccione piloto principal
   - **Copiloto:** Seleccione copiloto (opcional)
   - **Estado actual del vuelo:** Programado, En Vuelo, Completado, Cancelado
3. Haga clic en **"Guardar"**

### Editar Vuelo
1. Localice el vuelo en la tabla
2. Haga clic en el botón **"Editar"**
3. Modifique los campos necesarios
4. Haga clic en **"Guardar"**

### Confirmar Vuelo (Solo Operadores Autorizados)
1. Localice el vuelo en la tabla
2. Haga clic en el botón **"Confirmar"** (ícono de check verde)
3. Complete el modal de confirmación:
   - **Estado de Confirmación:** Confirmado, Pendiente, Cancelado
   - **Notas Adicionales:** Observaciones opcionales
4. Haga clic en **"Guardar Confirmación"**

### Filtros de Vuelos
- **Estado:** Filtre por estado del vuelo
- **Fecha Desde/Hasta:** Rango de fechas
- **Exportar PDF/Excel:** Genere reportes filtrados

---

## Gestión de Confirmaciones

### Vista Principal
![Gestión de Confirmaciones](https://via.placeholder.com/1200x600/dc3545/ffffff?text=Gestión+de+Confirmaciones)

### Agregar Nueva Confirmación
1. Haga clic en el botón **"Nueva Confirmación"**
2. Complete el formulario:
   - **Vuelo:** Seleccione de la lista desplegable
   - **Estado:** Estado de la confirmación
   - **Notas:** Observaciones adicionales
3. Haga clic en **"Guardar"**

### Editar Confirmación
1. Localice la confirmación en la tabla
2. Haga clic en el botón **"Editar"**
3. Modifique los campos necesarios
4. Haga clic en **"Guardar"**

### Filtros de Confirmaciones
- **Estado:** Filtre por estado de confirmación
- **Vuelo:** Filtre por vuelo específico
- **Exportar Reportes:** PDF y Excel

---

## Sistema de Reportes

### Acceso a Reportes
![Sistema de Reportes](https://via.placeholder.com/1200x600/20c997/ffffff?text=Sistema+de+Reportes)

### Tipos de Reportes Disponibles

#### 1. Reporte General (Dashboard)
- **Descripción:** Estadísticas completas del sistema
- **Incluye:** Totales de aeronaves, pilotos, vuelos y confirmaciones
- **Formato:** PDF y Excel

#### 2. Reporte de Aeronaves
- **Descripción:** Listado detallado de todas las aeronaves
- **Filtros:** Fabricante, tipo de aeronave
- **Incluye:** Matrícula, modelo, fabricante, capacidad, tipo

#### 3. Reporte de Pilotos
- **Descripción:** Información completa de pilotos
- **Filtros:** Tipo de licencia, nacionalidad
- **Incluye:** Nombre, licencia, horas de vuelo

#### 4. Reporte de Vuelos
- **Descripción:** Detalles de todos los vuelos
- **Filtros:** Estado, rango de fechas
- **Incluye:** Número, ruta, fechas, aeronave, piloto

#### 5. Reporte de Confirmaciones
- **Descripción:** Estado de confirmaciones
- **Filtros:** Estado, vuelo específico
- **Incluye:** Vuelo, estado, notas

### Generar Reportes
1. Navegue a la sección **"Reportes"**
2. Seleccione el tipo de reporte deseado
3. Aplique filtros si es necesario
4. Elija el formato (PDF o Excel)
5. Haga clic en **"Generar"**

---

## Configuración del Aeropuerto

### Acceso a Configuración
![Configuración del Aeropuerto](https://via.placeholder.com/1200x600/6c757d/ffffff?text=Configuración+del+Aeropuerto)

**Nota:** Solo disponible para usuarios con rol de Administrador.

### Información Básica
- **Nombre del Aeropuerto:** Nombre oficial
- **Código IATA:** Código de 3 letras
- **Código ICAO:** Código de 4 letras
- **Director:** Nombre del director

### Información de Ubicación
- **Dirección:** Dirección completa
- **Código Postal:** Código postal
- **Municipio:** Municipio
- **Ciudad:** Ciudad
- **Estado:** Estado o provincia
- **País:** País (por defecto: México)

### Información de Contacto
- **Teléfono:** Número de teléfono
- **Email:** Correo electrónico
- **Sitio Web:** URL del sitio web

### Guardar Configuración
1. Complete todos los campos necesarios
2. Haga clic en **"Guardar Configuración"**
3. Los cambios se reflejarán inmediatamente en el footer

---

## Gestión de Usuarios

### Vista Principal
![Gestión de Usuarios](https://via.placeholder.com/1200x600/fd7e14/ffffff?text=Gestión+de+Usuarios)

**Nota:** Solo disponible para usuarios con rol de Administrador.

### Agregar Nuevo Usuario
1. Haga clic en el botón **"Nuevo Usuario"**
2. Complete el formulario:
   - **Nombre de Usuario:** Identificador único
   - **Contraseña:** Contraseña segura
   - **Rol:** Seleccione el rol apropiado
3. Haga clic en **"Guardar"**

### Roles Disponibles
- **Administrador:** Acceso completo
- **Operador:** Gestión de vuelos y confirmaciones
- **Piloto:** Acceso limitado
- **Invitado:** Acceso mínimo

### Editar Usuario
1. Localice el usuario en la tabla
2. Haga clic en el botón **"Editar"**
3. Modifique los campos necesarios
4. Haga clic en **"Guardar"**

---

## Características Adicionales

### Tema Claro/Oscuro
![Selector de Tema](https://via.placeholder.com/400x200/343a40/ffffff?text=Selector+de+Tema)

- **Ubicación:** Esquina superior derecha
- **Funcionalidad:** Cambia entre tema claro y oscuro
- **Persistencia:** La preferencia se guarda automáticamente

### Footer Informativo
![Footer Informativo](https://via.placeholder.com/1200x100/212529/ffffff?text=Footer+Informativo)

- **Ubicación:** Parte inferior fija de la pantalla
- **Información:** Nombre del aeropuerto, ciudad, municipio, estado y país
- **Actualización:** Se actualiza automáticamente con la configuración

### Navegación Responsiva
- **Menú colapsable** en dispositivos móviles
- **Iconos intuitivos** para mejor usabilidad
- **Accesos rápidos** desde el dashboard

---

## Generación de Datos de Ejemplo

### ⚠️ ADVERTENCIA IMPORTANTE
**ANTES DE CONTINUAR, TENGA EN CUENTA QUE:**
- 🚨 **SE BORRARÁ TODA LA INFORMACIÓN EXISTENTE** en las tablas de la base de datos
- 🚨 **NO SE PUEDE DESHACER** esta operación
- 🚨 **HAGA UN BACKUP** de sus datos importantes antes de proceder
- 🚨 **SOLO PARA DESARROLLO Y PRUEBAS** - NO usar en producción con datos reales

### ¿Cuándo Usar Datos de Ejemplo?
- ✅ **Primera instalación** del sistema
- ✅ **Pruebas y desarrollo** local
- ✅ **Demostraciones** del sistema
- ✅ **Aprendizaje** de las funcionalidades
- ❌ **NO usar** si ya tiene datos importantes capturados
- ❌ **NO usar** en ambiente de producción

### Generar Datos de Ejemplo

#### Método 1: Desde la Línea de Comandos
```bash
# 1. Navegar al directorio del proyecto
cd aeroSys

# 2. Activar entorno virtual
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# 3. Ejecutar el script de datos de ejemplo
python seed.py
```

#### Método 2: Usando el Instalador Automático
```bash
# El instalador automático incluye la generación de datos
python install.py
```

### ¿Qué Datos se Generan?
El script `seed.py` crea automáticamente:

#### 🛩️ **5 Aeronaves de Ejemplo**
- Airbus A320-200 (XA-ABC) - 180 pasajeros
- Boeing 737-800 (XA-DEF) - 160 pasajeros  
- Cessna C208B (XA-GHI) - 12 pasajeros
- Airbus A330-300 (XA-JKL) - 300 pasajeros
- Boeing 787-9 (XA-MNO) - 290 pasajeros

#### 👨‍✈️ **5 Pilotos de Ejemplo**
- Carlos Ramírez González (LIC-001) - 8,500 horas
- María López Hernández (LIC-002) - 4,200 horas
- Roberto Silva Martínez (LIC-003) - 12,000 horas
- Ana García Torres (LIC-004) - 6,800 horas
- Miguel Ángel Cruz (LIC-005) - 9,500 horas

#### ✈️ **5 Vuelos de Ejemplo**
- AMX101: Ciudad de México → Guadalajara
- VIV202: Monterrey → Cancún
- AER303: Tijuana → Ciudad de México
- INT404: Ciudad de México → Madrid (Internacional)
- DOM505: Guadalajara → Tijuana

#### 🎫 **5 Confirmaciones de Ejemplo**
- Estados variados: Confirmado, Pendiente, Cancelado
- Notas descriptivas para cada confirmación

#### 👥 **5 Usuarios de Ejemplo**
- **admin** (Administrador) - Contraseña: 123456
- **operador1** (Operador) - Contraseña: 123456
- **piloto1** (Piloto) - Contraseña: 123456
- **invitado1** (Invitado) - Contraseña: 123456
- **supervisor** (Administrador) - Contraseña: 123456

#### ⚙️ **Configuración del Aeropuerto**
- Información completa del aeropuerto
- Datos de contacto y ubicación
- Configuración para el footer informativo

### Salida del Script
Al ejecutar `python seed.py`, verá algo como:

```
🗑️  Eliminando tablas existentes...
🏗️  Creando nuevas tablas...
✈️  Creando configuración del aeropuerto...
🛩️  Creando aeronaves...
👨‍✈️  Creando pilotos...
✈️  Creando vuelos...
🎫 Creando confirmaciones...
👥 Creando usuarios...

==================================================
✅ SEED COMPLETADO EXITOSAMENTE
==================================================
📊 Resumen de datos creados:
   🛩️  Aeronaves: 5
   👨‍✈️  Pilotos: 5
   ✈️  Vuelos: 5
   🎫 Confirmaciones: 5
   👥 Usuarios: 5
   ⚙️  Configuración: 1

🔑 Credenciales de acceso:
   Usuario: admin
   Contraseña: 123456

🌐 Acceder en: http://127.0.0.1:5000
==================================================
```

### Restaurar Datos Después de Generar Ejemplos
Si desea volver a sus datos originales:

1. **Restaurar desde backup** (si tiene uno)
2. **Reconfigurar manualmente** todos los datos
3. **Importar desde archivo** (funcionalidad futura)

## Solución de Problemas

### Problemas Comunes

#### 1. Error de Conexión a la Base de Datos
**Síntoma:** Error al iniciar la aplicación
**Solución:**
```bash
# Verificar que la base de datos existe
python reset_db.py
python seed.py
```

#### 2. No se Puede Iniciar Sesión
**Síntoma:** Credenciales no funcionan
**Solución:**
- Verificar usuario: `admin`
- Verificar contraseña: `123456`
- Crear nuevo usuario desde la línea de comandos

#### 3. Error al Generar Reportes
**Síntoma:** Los reportes no se descargan
**Solución:**
- Verificar que las dependencias estén instaladas
- Revisar los permisos de escritura
- Verificar la conexión a internet

#### 4. Footer No Muestra Información
**Síntoma:** Footer muestra "Cargando..."
**Solución:**
- Configurar la información del aeropuerto
- Verificar la conexión a la API
- Recargar la página

#### 5. Error al Ejecutar seed.py
**Síntoma:** Error al generar datos de ejemplo
**Solución:**
```bash
# Verificar que el entorno virtual está activado
# Debe mostrar (venv) al inicio de la línea de comandos

# Reinstalar dependencias si es necesario
pip install -r requirements.txt

# Ejecutar nuevamente
python seed.py
```

### Comandos de Diagnóstico

#### Verificar Estado de la Aplicación
```bash
python -c "from app import app; print('Aplicación OK')"
```

#### Verificar Base de Datos
```bash
python -c "from models import db; print('Base de datos OK')"
```

#### Reinstalar Dependencias
```bash
pip uninstall -r requirements.txt -y
pip install -r requirements.txt
```

### Logs y Debugging
- Los logs se muestran en la consola donde se ejecuta la aplicación
- Para debugging, ejecutar con `debug=True` en `app.py`
- Revisar el navegador (F12) para errores de JavaScript

---

## Contacto y Soporte

### Información de Contacto
- **Desarrollador:** Equipo de Desarrollo
- **Email:** soporte@aeropuerto.com
- **Teléfono:** +52 (55) 1234-5678

### Recursos Adicionales
- **Documentación técnica:** Ver archivo `README.md`
- **Código fuente:** Disponible en el repositorio
- **Actualizaciones:** Consultar el changelog

---

## Changelog

### Versión 1.0.0
- ✅ Dashboard interactivo
- ✅ Gestión completa de aeronaves, pilotos, vuelos y confirmaciones
- ✅ Sistema de reportes en PDF y Excel
- ✅ Configuración del aeropuerto
- ✅ Gestión de usuarios con roles
- ✅ Tema claro/oscuro
- ✅ Footer informativo fijo
- ✅ Sistema de confirmación de vuelos
- ✅ Filtros avanzados en reportes

---

**© 2024 Sistema de Gestión de Aeropuertos. Todos los derechos reservados.**
