# Diagramas del Sistema - Sistema de Gestión de Aeropuertos

## Tabla de Contenidos
1. [Arquitectura General](#arquitectura-general)
2. [Diagrama de Base de Datos](#diagrama-de-base-de-datos)
3. [Diagrama de Flujo de Usuario](#diagrama-de-flujo-de-usuario)
4. [Diagrama de Componentes](#diagrama-de-componentes)
5. [Diagrama de Despliegue](#diagrama-de-despliegue)
6. [Diagrama de Secuencia](#diagrama-de-secuencia)
7. [Diagrama de Casos de Uso](#diagrama-de-casos-de-uso)

## Arquitectura General

```
┌─────────────────────────────────────────────────────────────┐
│                    SISTEMA DE GESTIÓN DE AEROPUERTOS        │
├─────────────────────────────────────────────────────────────┤
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐        │
│  │   CLIENTE   │  │   CLIENTE   │  │   CLIENTE   │  ...   │
│  │  (Navegador)│  │  (Móvil)    │  │  (Tablet)   │        │
│  └─────────────┘  └─────────────┘  └─────────────┘        │
│           │               │               │                │
│           └───────────────┼───────────────┘                │
│                           │                                │
│  ┌─────────────────────────────────────────────────────────┐│
│  │                SERVIDOR WEB (Flask)                     ││
│  │  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐    ││
│  │  │   RUTAS     │  │     API     │  │  REPORTES   │    ││
│  │  │  (Views)    │  │  (REST)     │  │   (PDF/XL)  │    ││
│  │  └─────────────┘  └─────────────┘  └─────────────┘    ││
│  │           │               │               │            ││
│  │  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐    ││
│  │  │ AUTENTICACIÓN│  │   MODELOS   │  │  MIGRACIONES│    ││
│  │  │  (Login)    │  │  (SQLAlchemy)│  │  (Alembic)  │    ││
│  │  └─────────────┘  └─────────────┘  └─────────────┘    ││
│  └─────────────────────────────────────────────────────────┘│
│                           │                                │
│  ┌─────────────────────────────────────────────────────────┐│
│  │                BASE DE DATOS                            ││
│  │  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐    ││
│  │  │   SQLite    │  │    MySQL    │  │ PostgreSQL  │    ││
│  │  │(Desarrollo) │  │(Producción) │  │(Producción) │    ││
│  │  └─────────────┘  └─────────────┘  └─────────────┘    ││
│  └─────────────────────────────────────────────────────────┘│
└─────────────────────────────────────────────────────────────┘
```

## Diagrama de Base de Datos

```
┌─────────────────────────────────────────────────────────────┐
│                    MODELO DE DATOS                          │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌─────────────────┐    ┌─────────────────┐                │
│  │    USUARIOS     │    │   AERONAVES     │                │
│  ├─────────────────┤    ├─────────────────┤                │
│  │ id (PK)         │    │ aeronave_id (PK)│                │
│  │ username        │    │ matricula       │                │
│  │ password_hash   │    │ modelo          │                │
│  │ rol             │    │ fabricante      │                │
│  │ created_at      │    │ capacidad       │                │
│  └─────────────────┘    │ tipo_aeronave   │                │
│                         │ imagen          │                │
│  ┌─────────────────┐    │ created_at      │                │
│  │    PILOTOS      │    └─────────────────┘                │
│  ├─────────────────┤             │                        │
│  │ piloto_id (PK)  │             │                        │
│  │ nombre          │             │                        │
│  │ licencia        │             │                        │
│  │ tipo_licencia   │             │                        │
│  │ horas_vuelo     │             │                        │
│  │ nacionalidad    │             │                        │
│  │ created_at      │             │                        │
│  └─────────────────┘             │                        │
│           │                       │                        │
│           │                       │                        │
│  ┌─────────────────┐    ┌─────────────────┐                │
│  │     VUELOS      │    │  CONFIRMACIONES │                │
│  ├─────────────────┤    ├─────────────────┤                │
│  │ vuelo_id (PK)   │    │ confirmacion_id │                │
│  │ codigo_vuelo    │    │ vuelo_id (FK)   │                │
│  │ origen          │    │ estado          │                │
│  │ destino         │    │ notas           │                │
│  │ fecha_salida    │    │ created_at      │                │
│  │ fecha_llegada   │    └─────────────────┘                │
│  │ aeronave_id (FK)│             │                        │
│  │ piloto_id (FK)  │             │                        │
│  │ copiloto_id (FK)│             │                        │
│  │ estado          │             │                        │
│  │ pasajeros       │◄────── NUEVO                        │
│  │ observaciones   │             │                        │
│  │ aeropuerto_id   │◄────── NUEVO                        │
│  │ created_at      │             │                        │
│  └─────────────────┘             │                        │
│           │                       │                        │
│           └───────────────────────┘                        │
│           │                                                 │
│           │ (FK)                                            │
│           v                                                 │
│  ┌─────────────────┐                                        │
│  │CONFIG_AEROPUERTO│                                        │
│  ├─────────────────┤                                        │
│  │ id (PK)         │                                        │
│  │ nombre          │                                        │
│  │ codigo_iata     │                                        │
│  │ codigo_icao     │                                        │
│  │ director        │                                        │
│  │ direccion       │                                        │
│  │ codigo_postal   │                                        │
│  │ municipio       │                                        │
│  │ ciudad          │                                        │
│  │ estado          │                                        │
│  │ pais            │                                        │
│  │ telefono        │                                        │
│  │ email           │                                        │
│  │ sitio_web       │                                        │
│  │ activo          │◄────── NUEVO                        │
│  │ created_at      │                                        │
│  │ updated_at      │                                        │
│  └─────────────────┘                                        │
└─────────────────────────────────────────────────────────────┘
```

## Diagrama de Flujo de Usuario

```
┌─────────────────┐
│   INICIO        │
└─────────┬───────┘
          │
          v
┌─────────────────┐
│   LOGIN         │
└─────────┬───────┘
          │
          v
┌─────────────────┐    NO    ┌─────────────────┐
│ ¿CREDENCIALES   │ ────────>│   ERROR         │
│   VÁLIDAS?      │          └─────────┬───────┘
└─────────┬───────┘                    │
          │ SÍ                         │
          v                            │
┌─────────────────┐                    │
│   DASHBOARD     │                    │
└─────────┬───────┘                    │
          │                            │
          v                            │
┌─────────────────┐                    │
│   SELECCIONAR   │                    │
│   MÓDULO        │                    │
└─────────┬───────┘                    │
          │                            │
          v                            │
┌─────────────────┐                    │
│   GESTIONAR     │                    │
│   DATOS         │                    │
└─────────┬───────┘                    │
          │                            │
          v                            │
┌─────────────────┐                    │
│   GENERAR       │                    │
│   REPORTES      │                    │
└─────────┬───────┘                    │
          │                            │
          v                            │
┌─────────────────┐                    │
│   LOGOUT        │                    │
└─────────┬───────┘                    │
          │                            │
          └────────────────────────────┘
```

## Diagrama de Componentes

```
┌─────────────────────────────────────────────────────────────┐
│                    COMPONENTES DEL SISTEMA                  │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌─────────────────────────────────────────────────────────┐│
│  │                CAPA DE PRESENTACIÓN                     ││
│  │  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐    ││
│  │  │  TEMPLATES  │  │   STATIC    │  │   FORMS     │    ││
│  │  │  (HTML)     │  │   (CSS/JS)  │  │  (Bootstrap)│    ││
│  │  └─────────────┘  └─────────────┘  └─────────────┘    ││
│  └─────────────────────────────────────────────────────────┘│
│                           │                                │
│  ┌─────────────────────────────────────────────────────────┐│
│  │                CAPA DE CONTROL                          ││
│  │  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐    ││
│  │  │   RUTAS     │  │     API     │  │  REPORTES   │    ││
│  │  │  (Views)    │  │  (REST)     │  │   (PDF/XL)  │    ││
│  │  └─────────────┘  └─────────────┘  └─────────────┘    ││
│  │  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐    ││
│  │  │AUTENTICACIÓN│  │  VALIDACIÓN │  │   FILTROS   │    ││
│  │  │  (Login)    │  │  (Forms)    │  │  Avanzados  │    ││
│  │  └─────────────┘  └─────────────┘  └─────────────┘    ││
│  │  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐    ││
│  │  │MULTI-AIRPORT│  │  STATUSBAR  │  │  PASAJEROS  │    ││
│  │  │  (Gestión)  │  │  (Dinámico) │  │  (Gestión)  │    ││
│  │  └─────────────┘  └─────────────┘  └─────────────┘    ││
│  └─────────────────────────────────────────────────────────┘│
│                           │                                │
│  ┌─────────────────────────────────────────────────────────┐│
│  │                CAPA DE MODELO                           ││
│  │  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐    ││
│  │  │   MODELOS   │  │  MIGRACIONES│  │  RELACIONES │    ││
│  │  │(SQLAlchemy) │  │  (Alembic)  │  │  (Foreign)  │    ││
│  │  └─────────────┘  └─────────────┘  └─────────────┘    ││
│  └─────────────────────────────────────────────────────────┘│
│                           │                                │
│  ┌─────────────────────────────────────────────────────────┐│
│  │                CAPA DE DATOS                            ││
│  │  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐    ││
│  │  │   SQLite    │  │    MySQL    │  │ PostgreSQL  │    ││
│  │  │(Desarrollo) │  │(Producción) │  │(Producción) │    ││
│  │  └─────────────┘  └─────────────┘  └─────────────┘    ││
│  └─────────────────────────────────────────────────────────┘│
└─────────────────────────────────────────────────────────────┘
```

## Diagrama de Despliegue

```
┌─────────────────────────────────────────────────────────────┐
│                    ARQUITECTURA DE DESPLIEGUE               │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌─────────────────────────────────────────────────────────┐│
│  │                    INTERNET                             ││
│  │  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐    ││
│  │  │   USUARIO   │  │   USUARIO   │  │   USUARIO   │    ││
│  │  │  (Admin)    │  │ (Operador)  │  │  (Piloto)   │    ││
│  │  └─────────────┘  └─────────────┘  └─────────────┘    ││
│  └─────────────────────────────────────────────────────────┘│
│                           │                                │
│  ┌─────────────────────────────────────────────────────────┐│
│  │                SERVIDOR WEB                             ││
│  │  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐    ││
│  │  │    NGINX    │  │  GUNICORN   │  │   FLASK     │    ││
│  │  │  (Proxy)    │  │  (WSGI)     │  │  (App)      │    ││
│  │  └─────────────┘  └─────────────┘  └─────────────┘    ││
│  │  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐    ││
│  │  │   SSL/TLS   │  │   STATIC    │  │   UPLOADS   │    ││
│  │  │ (Certificado)│  │  (Files)    │  │  (Images)   │    ││
│  │  └─────────────┘  └─────────────┘  └─────────────┘    ││
│  └─────────────────────────────────────────────────────────┘│
│                           │                                │
│  ┌─────────────────────────────────────────────────────────┐│
│  │                SERVIDOR DE DATOS                        ││
│  │  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐    ││
│  │  │    MySQL    │  │   BACKUP    │  │   MONITOR   │    ││
│  │  │ (Producción)│  │  (Automático)│  │  (Logs)     │    ││
│  │  └─────────────┘  └─────────────┘  └─────────────┘    ││
│  └─────────────────────────────────────────────────────────┘│
└─────────────────────────────────────────────────────────────┘
```

## Diagrama de Secuencia

```
┌─────────────┐  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐
│   USUARIO   │  │   NAVEGADOR │  │   FLASK     │  │   BASE DE   │
│             │  │             │  │   APP       │  │   DATOS     │
└─────────────┘  └─────────────┘  └─────────────┘  └─────────────┘
       │                │                │                │
       │ 1. Login       │                │                │
       ├───────────────>│                │                │
       │                │ 2. POST /login │                │
       │                ├───────────────>│                │
       │                │                │ 3. Query User  │
       │                │                ├───────────────>│
       │                │                │ 4. User Data   │
       │                │                │<───────────────┤
       │                │ 5. Session     │                │
       │                │<───────────────┤                │
       │ 6. Dashboard   │                │                │
       │<───────────────┤                │                │
       │                │                │                │
       │ 7. View Data   │                │                │
       ├───────────────>│                │                │
       │                │ 8. GET /api    │                │
       │                ├───────────────>│                │
       │                │                │ 9. Query Data  │
       │                │                ├───────────────>│
       │                │                │ 10. Data      │
       │                │                │<───────────────┤
       │                │ 11. JSON       │                │
       │                │<───────────────┤                │
       │ 12. Display    │                │                │
       │<───────────────┤                │                │
       │                │                │                │
       │ 13. Create     │                │                │
       ├───────────────>│                │                │
       │                │ 14. POST /api  │                │
       │                ├───────────────>│                │
       │                │                │ 15. Insert    │
       │                │                ├───────────────>│
       │                │                │ 16. Success   │
       │                │                │<───────────────┤
       │                │ 17. Response   │                │
       │                │<───────────────┤                │
       │ 18. Updated    │                │                │
       │<───────────────┤                │                │
```

## Diagrama de Casos de Uso

```
┌─────────────────────────────────────────────────────────────┐
│                    CASOS DE USO                            │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌─────────────────┐    ┌─────────────────┐                │
│  │   ADMINISTRADOR │    │    OPERADOR     │                │
│  │                 │    │                 │                │
│  │ • Gestionar     │    │ • Gestionar     │                │
│  │   usuarios      │    │   vuelos        │                │
│  │ • Configurar    │    │ • Confirmar     │                │
│  │   sistema       │    │   vuelos        │                │
│  │ • Gestionar     │    │ • Agregar       │                │
│  │   aeropuertos   │    │   pasajeros     │                │
│  │ • Activar       │    │ • Ver reportes  │                │
│  │   aeropuerto    │    │   con filtros   │                │
│  │ • Ver reportes  │    │ • Gestionar     │                │
│  │   con filtros   │    │   aeronaves     │                │
│  │ • Gestionar     │    │ • Gestionar     │                │
│  │   aeronaves     │    │   pilotos       │                │
│  │ • Gestionar     │    │                 │                │
│  │   pilotos       │    │                 │                │
│  └─────────────────┘    └─────────────────┘                │
│           │                       │                        │
│           │                       │                        │
│  ┌─────────────────┐    ┌─────────────────┐                │
│  │     PILOTO      │    │    INVITADO     │                │
│  │                 │    │                 │                │
│  │ • Ver vuelos    │    │ • Ver vuelos    │                │
│  │   asignados     │    │   (solo lectura)│                │
│  │ • Ver aeronaves │    │ • Ver aeronaves │                │
│  │ • Ver pilotos   │    │ • Ver pilotos   │                │
│  └─────────────────┘    └─────────────────┘                │
│                                                             │
│  ┌─────────────────────────────────────────────────────────┐│
│  │                SISTEMA                                  ││
│  │                                                         ││
│  │ • Autenticación de usuarios                            ││
│  │ • Autorización de acciones                             ││
│  │ • Validación de datos                                  ││
│  │ • Generación de reportes                               ││
│  │ • Gestión de sesiones                                  ││
│  │ • Logging de actividades                               ││
│  └─────────────────────────────────────────────────────────┘│
└─────────────────────────────────────────────────────────────┘
```

---

## Relaciones y Flujos Principales

### Relación Multi-Aeropuerto
```
┌─────────────────────┐
│ ConfiguracionAeropuerto │
│ (activo = true)     │
└──────────┬──────────┘
           │ 1
           │
           │ N
┌──────────▼──────────┐
│      Vuelos         │
│ (aeropuerto_id FK)  │
└─────────────────────┘
```

### Flujo de Filtros Avanzados
```
Usuario → Selecciona Filtros (Estado, Aeronave, Piloto, Fechas)
          ↓
       Aplicar Filtros
          ↓
       API Request con parámetros
          ↓
       Query a Base de Datos
          ↓
       Resultados Filtrados
          ↓
       Actualización de Tabla
```

### Flujo de Gestión de Pasajeros
```
Usuario → Crear/Editar Vuelo
          ↓
       Ingresar Pasajeros (uno por línea)
          ↓
       Guardar en campo TEXT
          ↓
       Almacenar en BD
          ↓
       Mostrar en Vista/Reportes
```

### Flujo de Cambio de Aeropuerto Activo
```
Admin → Selecciona Aeropuerto
        ↓
     Activar Aeropuerto
        ↓
     Desactivar Anterior
        ↓
     Actualizar StatusBar
        ↓
     Broadcast a Todas las Sesiones
        ↓
     Nuevos Vuelos → Aeropuerto Activo
```

---

## Novedades de la Versión 1.1

### Cambios en el Modelo de Datos
- ✅ **Tabla Vuelos**: Agregados campos `pasajeros` (Text) y `aeropuerto_id` (FK)
- ✅ **Tabla ConfiguracionAeropuerto**: Agregado campo `activo` (Boolean)
- ✅ **Relación**: Vuelos → ConfiguracionAeropuerto (N:1)

### Nuevos Componentes
- ✅ **Filtros Avanzados**: Aeronave y Piloto en gestión de vuelos
- ✅ **StatusBar Dinámico**: Actualización cada 30 segundos
- ✅ **Multi-Aeropuerto**: Gestión y cambio dinámico de aeropuerto activo
- ✅ **Gestión de Pasajeros**: Campo de texto para lista de pasajeros

### Mejoras en la Interfaz
- ✅ **100% Responsive**: Todos los formularios optimizados
- ✅ **Filtros Responsivos**: Diseño de 6 columnas adaptable
- ✅ **Modales**: Creación rápida de aeropuertos
- ✅ **Campos Amplios**: Pasajeros y observaciones con textareas

---

**Versión de los Diagramas:** 1.1  
**Última Actualización:** Octubre 2025  
**Sistema:** Sistema de Gestión de Aeropuertos v1.1