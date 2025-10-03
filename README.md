# Sistema de Gestión de Aeropuertos 🛫

Un sistema web completo desarrollado en Flask para la gestión integral de operaciones aeroportuarias, incluyendo aeronaves, pilotos, vuelos, confirmaciones y reportes detallados.

## 🚀 Características Principales

- ✅ **Dashboard Interactivo** con estadísticas en tiempo real
- ✅ **Gestión Completa** de aeronaves, pilotos, vuelos y confirmaciones
- ✅ **Sistema de Reportes** en PDF y Excel con filtros avanzados
- ✅ **Configuración del Aeropuerto** personalizable
- ✅ **Gestión de Usuarios** con diferentes roles y permisos
- ✅ **Tema Claro/Oscuro** adaptable
- ✅ **Footer Informativo** siempre visible
- ✅ **Sistema de Confirmación** de vuelos para operadores
- ✅ **Interfaz Responsiva** para todos los dispositivos

## 📋 Requisitos del Sistema

- Python 3.8 o superior
- Navegador web moderno (Chrome, Firefox, Safari, Edge)
- 2GB de RAM mínimo
- 500MB de espacio en disco

## 🛠️ Instalación Rápida

### Opción 1: Instalación Automática (Recomendada)
```bash
# Clonar o descargar el proyecto
git clone [URL_DEL_REPOSITORIO]
cd aeroSys

# Ejecutar instalador automático
python install.py
```

### Opción 2: Instalación Manual
```bash
# 1. Crear entorno virtual
python -m venv venv

# 2. Activar entorno virtual
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. Configurar base de datos
# ⚠️ ADVERTENCIA: Se borrará toda la información existente
python seed.py

# 5. Ejecutar aplicación
python app.py
```

### ⚠️ Generación de Datos de Ejemplo
El comando `python seed.py` crea automáticamente:
- 🛩️ **5 aeronaves** de diferentes tipos
- 👨‍✈️ **5 pilotos** con licencias y horas de vuelo
- ✈️ **5 vuelos** con rutas realistas
- 🎫 **5 confirmaciones** con diferentes estados
- 👥 **5 usuarios** con diferentes roles
- ⚙️ **Configuración** completa del aeropuerto

**⚠️ ADVERTENCIA:** Este proceso **ELIMINA TODA LA INFORMACIÓN EXISTENTE** en la base de datos. Solo use para desarrollo y pruebas.

## 🌐 Acceso al Sistema

1. Abrir navegador en: `http://127.0.0.1:5000`
2. **Credenciales por defecto:**
   - Usuario: `admin`
   - Contraseña: `123456`

## 📚 Documentación Completa

### Manuales de Usuario
- **[Manual de Usuario](Manual_de_Usuario.md)** - Guía completa de uso del sistema
- **[Guía de Instalación Detallada](Guia_Instalacion_Detallada.md)** - Instalación paso a paso para diferentes sistemas operativos
- **[Diagramas del Sistema](Diagramas_Sistema.md)** - Arquitectura y flujos del sistema

### Archivos de Configuración
- **[config.env.example](config.env.example)** - Archivo de configuración de ejemplo
- **[install.py](install.py)** - Instalador automático del sistema

## 🏗️ Arquitectura del Sistema

```
aeroSys/
├── app.py                 # Aplicación principal Flask
├── models.py              # Modelos de base de datos
├── api.py                 # Endpoints de API REST
├── reports.py             # Sistema de reportes
├── config.py              # Configuración de la aplicación
├── requirements.txt       # Dependencias Python
├── seed.py               # Datos de ejemplo
├── install.py            # Instalador automático
├── templates/            # Plantillas HTML
│   ├── base.html         # Plantilla base
│   ├── dashboard.html    # Dashboard principal
│   ├── aeronaves.html    # Gestión de aeronaves
│   ├── pilotos.html      # Gestión de pilotos
│   ├── vuelos.html       # Gestión de vuelos
│   ├── confirmaciones.html # Gestión de confirmaciones
│   └── reports/          # Plantillas de reportes
├── static/               # Archivos estáticos
├── migrations/           # Migraciones de base de datos
└── auth/                 # Sistema de autenticación
```

## 👥 Roles de Usuario

- **Administrador:** Acceso completo a todas las funcionalidades
- **Operador:** Gestión de vuelos y confirmaciones
- **Piloto:** Acceso limitado (solo lectura)
- **Invitado:** Acceso muy limitado

## 🔧 Funcionalidades por Módulo

### Dashboard
- Estadísticas en tiempo real
- Accesos rápidos a todas las secciones
- Enlaces a reportes
- Información del aeropuerto en footer fijo

### Gestión de Aeronaves
- CRUD completo de aeronaves
- Filtros por fabricante y tipo
- Exportación a PDF/Excel
- Validación de matrículas únicas

### Gestión de Pilotos
- CRUD completo de pilotos
- Control de licencias y horas de vuelo
- Filtros avanzados
- Reportes detallados

### Gestión de Vuelos
- CRUD completo de vuelos
- Asignación de aeronaves y pilotos
- Estados de vuelo (Programado, En Vuelo, Completado, Cancelado)
- Sistema de confirmación para operadores
- Filtros por estado y fechas

### Sistema de Confirmaciones
- Confirmación de vuelos por operadores autorizados
- Estados de confirmación (Confirmado, Pendiente, Cancelado)
- Notas adicionales
- Control de permisos por rol

### Sistema de Reportes
- Reportes en PDF y Excel
- Filtros avanzados por módulo
- Estadísticas generales
- Exportación personalizada

### Configuración del Aeropuerto
- Información básica del aeropuerto
- Datos de ubicación
- Información de contacto
- Actualización en tiempo real del footer

## 🚀 Despliegue en Producción

### Variables de Entorno
```env
FLASK_ENV=production
SECRET_KEY=tu_clave_secreta_muy_larga_y_segura
DATABASE_URL=mysql://usuario:contraseña@localhost/aeropuertos
```

### Con Docker
```bash
# Construir imagen
docker build -t aerosys .

# Ejecutar contenedor
docker run -p 5000:5000 aerosys
```

### Con Gunicorn + Nginx
```bash
# Instalar Gunicorn
pip install gunicorn

# Ejecutar aplicación
gunicorn -w 4 -b 0.0.0.0:5000 wsgi:app
```

## 🐛 Solución de Problemas

### Error: "python no se reconoce como comando"
- **Windows:** Reinstalar Python marcando "Add to PATH"
- **Linux/Mac:** Usar `python3` en lugar de `python`

### Error: "ModuleNotFoundError"
- Verificar que el entorno virtual está activado
- Reinstalar dependencias: `pip install -r requirements.txt`

### Puerto 5000 ya en uso
- Cambiar puerto en `app.py`: `app.run(port=5001)`
- O matar proceso que usa el puerto

### Error de Base de Datos
```bash
# Resetear base de datos
python reset_db.py
python seed.py
```

## 📞 Soporte

- **Documentación:** Consulta los manuales incluidos
- **Issues:** Reporta problemas en el repositorio
- **Email:** soporte@aeropuerto.com

## 📄 Licencia

© 2024 Sistema de Gestión de Aeropuertos. Todos los derechos reservados.

## 🔄 Changelog

### Versión 1.0.0
- ✅ Dashboard interactivo con estadísticas
- ✅ Gestión completa de aeronaves, pilotos, vuelos y confirmaciones
- ✅ Sistema de reportes en PDF y Excel
- ✅ Configuración del aeropuerto personalizable
- ✅ Gestión de usuarios con roles
- ✅ Tema claro/oscuro
- ✅ Footer informativo fijo
- ✅ Sistema de confirmación de vuelos
- ✅ Filtros avanzados en reportes
- ✅ Instalador automático
- ✅ Documentación completa

---

**¡Bienvenido al Sistema de Gestión de Aeropuertos!** 🛫✨
