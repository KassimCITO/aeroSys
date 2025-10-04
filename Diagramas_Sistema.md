<<<<<<< HEAD
# Diagramas del Sistema de Gestión de Aeropuertos

## Diagrama de Arquitectura del Sistema

```mermaid
graph TB
    A[Usuario] --> B[Navegador Web]
    B --> C[Flask Application]
    C --> D[Base de Datos SQLite]
    C --> E[API Endpoints]
    C --> F[Templates HTML]
    C --> G[Static Files]
    
    E --> H[Autenticación]
    E --> I[CRUD Operations]
    E --> J[Reportes PDF/Excel]
    
    F --> K[Dashboard]
    F --> L[Gestión de Datos]
    F --> M[Configuración]
    
    G --> N[CSS/JS]
    G --> O[Imágenes]
```

## Flujo de Autenticación

```mermaid
sequenceDiagram
    participant U as Usuario
    participant L as Login Page
    participant A as Auth System
    participant D as Dashboard
    
    U->>L: Ingresa credenciales
    L->>A: Valida usuario/contraseña
    A->>A: Verifica rol de usuario
    A->>D: Redirige según rol
    D->>U: Muestra interfaz apropiada
```

## Estructura de la Base de Datos

```mermaid
erDiagram
    USUARIOS {
        int id PK
        string username
        string password_hash
        string rol
        datetime created_at
    }
    
    AERONAVES {
        int aeronave_id PK
        string matricula
        string modelo
        string fabricante
        int capacidad
        string tipo_aeronave
        datetime created_at
    }
    
    PILOTOS {
        int piloto_id PK
        string nombre
        string licencia
        int horas_vuelo
        datetime created_at
    }
    
    VUELOS {
        int vuelo_id PK
        string numero_vuelo
        string origen
        string destino
        datetime fecha_salida
        datetime fecha_llegada
        int aeronave_id FK
        int piloto_id FK
        int copiloto_id FK
        datetime created_at
    }
    
    CONFIRMACIONES {
        int confirmacion_id PK
        int vuelo_id FK
        string estado
        text notas
        datetime created_at
    }
    
    CONFIGURACION_AEROPUERTO {
        int id PK
        string nombre
        string ciudad
        string municipio
        string estado
        string pais
        string codigo_iata
        string codigo_icao
        string director
        string direccion
        string telefono
        string email
        datetime created_at
    }
    
    VUELOS ||--o{ CONFIRMACIONES : "tiene"
    AERONAVES ||--o{ VUELOS : "asignada_a"
    PILOTOS ||--o{ VUELOS : "piloto"
    PILOTOS ||--o{ VUELOS : "copiloto"
```

## Flujo de Gestión de Vuelos

```mermaid
flowchart TD
    A[Inicio] --> B[Seleccionar Vuelo]
    B --> C{¿Acción?}
    C -->|Crear| D[Formulario Nuevo Vuelo]
    C -->|Editar| E[Formulario Editar Vuelo]
    C -->|Confirmar| F[Modal Confirmación]
    C -->|Eliminar| G[Confirmar Eliminación]
    
    D --> H[Validar Datos]
    E --> H
    F --> I[Verificar Permisos]
    G --> J[Eliminar de BD]
    
    H --> K{¿Válido?}
    K -->|Sí| L[Guardar en BD]
    K -->|No| M[Mostrar Errores]
    
    I --> N{¿Autorizado?}
    N -->|Sí| O[Crear Confirmación]
    N -->|No| P[Mostrar Error]
    
    L --> Q[Actualizar Vista]
    O --> Q
    J --> Q
    M --> D
    P --> B
    Q --> R[Fin]
```

## Jerarquía de Roles y Permisos

```mermaid
graph TD
    A[Usuario] --> B{¿Autenticado?}
    B -->|No| C[Página de Login]
    B -->|Sí| D{¿Rol?}
    
    D -->|Admin| E[Acceso Completo]
    D -->|Operador| F[Gestión Vuelos/Confirmaciones]
    D -->|Piloto| G[Vista Limitada]
    D -->|Invitado| H[Acceso Mínimo]
    
    E --> I[Dashboard]
    E --> J[Gestión Aeronaves]
    E --> K[Gestión Pilotos]
    E --> L[Gestión Vuelos]
    E --> M[Gestión Confirmaciones]
    E --> N[Gestión Usuarios]
    E --> O[Configuración]
    E --> P[Reportes]
    
    F --> I
    F --> L
    F --> M
    F --> P
    
    G --> I
    G --> Q[Vista Vuelos - Solo Lectura]
    
    H --> I
    H --> R[Vista Limitada]
```

## Flujo de Generación de Reportes

```mermaid
flowchart LR
    A[Seleccionar Tipo Reporte] --> B[Aplicar Filtros]
    B --> C{¿Formato?}
    C -->|PDF| D[Generar PDF]
    C -->|Excel| E[Generar Excel]
    
    D --> F[ReportLab]
    E --> G[OpenPyXL]
    
    F --> H[Archivo PDF]
    G --> I[Archivo Excel]
    
    H --> J[Descargar]
    I --> J
```

## Estructura de Archivos del Proyecto

```mermaid
graph TD
    A[aeroSys/] --> B[app.py]
    A --> C[models.py]
    A --> D[api.py]
    A --> E[reports.py]
    A --> F[config.py]
    A --> G[requirements.txt]
    A --> H[seed.py]
    A --> I[reset_db.py]
    
    A --> J[templates/]
    J --> K[base.html]
    J --> L[dashboard.html]
    J --> M[aeronaves.html]
    J --> N[pilotos.html]
    J --> O[vuelos.html]
    J --> P[confirmaciones.html]
    J --> Q[usuarios.html]
    J --> R[reports.html]
    J --> S[auth/]
    J --> T[config/]
    J --> U[reports/]
    
    A --> V[static/]
    V --> W[css/]
    V --> X[js/]
    V --> Y[images/]
    
    A --> Z[migrations/]
    A --> AA[auth/]
    A --> BB[routes/]
```

## Flujo de Configuración del Aeropuerto

```mermaid
sequenceDiagram
    participant A as Admin
    participant C as Config Page
    participant API as API
    participant DB as Database
    participant F as Footer
    
    A->>C: Accede a Configuración
    C->>API: Carga datos actuales
    API->>DB: Consulta configuración
    DB->>API: Retorna datos
    API->>C: Muestra formulario
    
    A->>C: Modifica datos
    A->>C: Guarda cambios
    C->>API: Envía datos actualizados
    API->>DB: Actualiza configuración
    DB->>API: Confirma actualización
    API->>F: Actualiza footer
    F->>A: Muestra nueva información
```

## Estados de un Vuelo

```mermaid
stateDiagram-v2
    [*] --> Programado
    Programado --> En_Vuelo
    Programado --> Cancelado
    En_Vuelo --> Completado
    En_Vuelo --> Cancelado
    Completado --> [*]
    Cancelado --> [*]
    
    note right of Programado
        Vuelo programado
        pero no iniciado
    end note
    
    note right of En_Vuelo
        Vuelo en progreso
        aeronave en ruta
    end note
    
    note right of Completado
        Vuelo finalizado
        exitosamente
    end note
    
    note right of Cancelado
        Vuelo cancelado
        por cualquier motivo
    end note
```

## Flujo de Confirmación de Vuelos

```mermaid
flowchart TD
    A[Operador Autorizado] --> B[Selecciona Vuelo]
    B --> C[Hace clic en Confirmar]
    C --> D[Modal de Confirmación]
    D --> E[Selecciona Estado]
    E --> F[Agrega Notas Opcionales]
    F --> G[Guarda Confirmación]
    G --> H{¿Éxito?}
    H -->|Sí| I[Actualiza Vista]
    H -->|No| J[Muestra Error]
    I --> K[Fin]
    J --> D
```

## Responsive Design - Breakpoints

```mermaid
graph LR
    A[Mobile<br/>320px-768px] --> B[Tablet<br/>768px-1024px]
    B --> C[Desktop<br/>1024px+]
    
    A --> D[Menú Colapsable]
    A --> E[Footer Ajustado]
    A --> F[Botones Grandes]
    
    B --> G[Menú Semi-Expandido]
    B --> H[Layout 2 Columnas]
    
    C --> I[Menú Completo]
    C --> J[Layout 3+ Columnas]
    C --> K[Sidebar Opcional]
```

## Flujo de Instalación

```mermaid
flowchart TD
    A[Descargar Proyecto] --> B[Crear Entorno Virtual]
    B --> C[Activar Entorno Virtual]
    C --> D[Instalar Dependencias]
    D --> E[Configurar Base de Datos]
    E --> F[Poblar Datos de Ejemplo]
    F --> G[Ejecutar Aplicación]
    G --> H[Acceder via Navegador]
    H --> I[Sistema Listo]
    
    D --> J[requirements.txt]
    E --> K[reset_db.py]
    F --> L[seed.py]
    G --> M[python app.py]
    H --> N[http://127.0.0.1:5000]
```

## Arquitectura de Seguridad

```mermaid
graph TB
    A[Cliente] --> B[HTTPS/SSL]
    B --> C[Flask App]
    C --> D[Flask-Login]
    D --> E[Session Management]
    E --> F[Role-Based Access]
    F --> G[API Endpoints]
    G --> H[Database]
    
    I[Password Hashing] --> D
    J[CSRF Protection] --> C
    K[Input Validation] --> G
    L[SQL Injection Prevention] --> H
```

Estos diagramas proporcionan una visión completa de la arquitectura, flujos y funcionalidades del Sistema de Gestión de Aeropuertos, complementando el Manual de Usuario con representaciones visuales claras y detalladas.
=======
# Diagramas del Sistema de Gestión de Aeropuertos

## Diagrama de Arquitectura del Sistema

```mermaid
graph TB
    A[Usuario] --> B[Navegador Web]
    B --> C[Flask Application]
    C --> D[Base de Datos SQLite]
    C --> E[API Endpoints]
    C --> F[Templates HTML]
    C --> G[Static Files]
    
    E --> H[Autenticación]
    E --> I[CRUD Operations]
    E --> J[Reportes PDF/Excel]
    
    F --> K[Dashboard]
    F --> L[Gestión de Datos]
    F --> M[Configuración]
    
    G --> N[CSS/JS]
    G --> O[Imágenes]
```

## Flujo de Autenticación

```mermaid
sequenceDiagram
    participant U as Usuario
    participant L as Login Page
    participant A as Auth System
    participant D as Dashboard
    
    U->>L: Ingresa credenciales
    L->>A: Valida usuario/contraseña
    A->>A: Verifica rol de usuario
    A->>D: Redirige según rol
    D->>U: Muestra interfaz apropiada
```

## Estructura de la Base de Datos

```mermaid
erDiagram
    USUARIOS {
        int id PK
        string username
        string password_hash
        string rol
        datetime created_at
    }
    
    AERONAVES {
        int aeronave_id PK
        string matricula
        string modelo
        string fabricante
        int capacidad
        string tipo_aeronave
        datetime created_at
    }
    
    PILOTOS {
        int piloto_id PK
        string nombre
        string licencia
        int horas_vuelo
        datetime created_at
    }
    
    VUELOS {
        int vuelo_id PK
        string numero_vuelo
        string origen
        string destino
        datetime fecha_salida
        datetime fecha_llegada
        int aeronave_id FK
        int piloto_id FK
        int copiloto_id FK
        datetime created_at
    }
    
    CONFIRMACIONES {
        int confirmacion_id PK
        int vuelo_id FK
        string estado
        text notas
        datetime created_at
    }
    
    CONFIGURACION_AEROPUERTO {
        int id PK
        string nombre
        string ciudad
        string municipio
        string estado
        string pais
        string codigo_iata
        string codigo_icao
        string director
        string direccion
        string telefono
        string email
        datetime created_at
    }
    
    VUELOS ||--o{ CONFIRMACIONES : "tiene"
    AERONAVES ||--o{ VUELOS : "asignada_a"
    PILOTOS ||--o{ VUELOS : "piloto"
    PILOTOS ||--o{ VUELOS : "copiloto"
```

## Flujo de Gestión de Vuelos

```mermaid
flowchart TD
    A[Inicio] --> B[Seleccionar Vuelo]
    B --> C{¿Acción?}
    C -->|Crear| D[Formulario Nuevo Vuelo]
    C -->|Editar| E[Formulario Editar Vuelo]
    C -->|Confirmar| F[Modal Confirmación]
    C -->|Eliminar| G[Confirmar Eliminación]
    
    D --> H[Validar Datos]
    E --> H
    F --> I[Verificar Permisos]
    G --> J[Eliminar de BD]
    
    H --> K{¿Válido?}
    K -->|Sí| L[Guardar en BD]
    K -->|No| M[Mostrar Errores]
    
    I --> N{¿Autorizado?}
    N -->|Sí| O[Crear Confirmación]
    N -->|No| P[Mostrar Error]
    
    L --> Q[Actualizar Vista]
    O --> Q
    J --> Q
    M --> D
    P --> B
    Q --> R[Fin]
```

## Jerarquía de Roles y Permisos

```mermaid
graph TD
    A[Usuario] --> B{¿Autenticado?}
    B -->|No| C[Página de Login]
    B -->|Sí| D{¿Rol?}
    
    D -->|Admin| E[Acceso Completo]
    D -->|Operador| F[Gestión Vuelos/Confirmaciones]
    D -->|Piloto| G[Vista Limitada]
    D -->|Invitado| H[Acceso Mínimo]
    
    E --> I[Dashboard]
    E --> J[Gestión Aeronaves]
    E --> K[Gestión Pilotos]
    E --> L[Gestión Vuelos]
    E --> M[Gestión Confirmaciones]
    E --> N[Gestión Usuarios]
    E --> O[Configuración]
    E --> P[Reportes]
    
    F --> I
    F --> L
    F --> M
    F --> P
    
    G --> I
    G --> Q[Vista Vuelos - Solo Lectura]
    
    H --> I
    H --> R[Vista Limitada]
```

## Flujo de Generación de Reportes

```mermaid
flowchart LR
    A[Seleccionar Tipo Reporte] --> B[Aplicar Filtros]
    B --> C{¿Formato?}
    C -->|PDF| D[Generar PDF]
    C -->|Excel| E[Generar Excel]
    
    D --> F[ReportLab]
    E --> G[OpenPyXL]
    
    F --> H[Archivo PDF]
    G --> I[Archivo Excel]
    
    H --> J[Descargar]
    I --> J
```

## Estructura de Archivos del Proyecto

```mermaid
graph TD
    A[aeroSys/] --> B[app.py]
    A --> C[models.py]
    A --> D[api.py]
    A --> E[reports.py]
    A --> F[config.py]
    A --> G[requirements.txt]
    A --> H[seed.py]
    A --> I[reset_db.py]
    
    A --> J[templates/]
    J --> K[base.html]
    J --> L[dashboard.html]
    J --> M[aeronaves.html]
    J --> N[pilotos.html]
    J --> O[vuelos.html]
    J --> P[confirmaciones.html]
    J --> Q[usuarios.html]
    J --> R[reports.html]
    J --> S[auth/]
    J --> T[config/]
    J --> U[reports/]
    
    A --> V[static/]
    V --> W[css/]
    V --> X[js/]
    V --> Y[images/]
    
    A --> Z[migrations/]
    A --> AA[auth/]
    A --> BB[routes/]
```

## Flujo de Configuración del Aeropuerto

```mermaid
sequenceDiagram
    participant A as Admin
    participant C as Config Page
    participant API as API
    participant DB as Database
    participant F as Footer
    
    A->>C: Accede a Configuración
    C->>API: Carga datos actuales
    API->>DB: Consulta configuración
    DB->>API: Retorna datos
    API->>C: Muestra formulario
    
    A->>C: Modifica datos
    A->>C: Guarda cambios
    C->>API: Envía datos actualizados
    API->>DB: Actualiza configuración
    DB->>API: Confirma actualización
    API->>F: Actualiza footer
    F->>A: Muestra nueva información
```

## Estados de un Vuelo

```mermaid
stateDiagram-v2
    [*] --> Programado
    Programado --> En_Vuelo
    Programado --> Cancelado
    En_Vuelo --> Completado
    En_Vuelo --> Cancelado
    Completado --> [*]
    Cancelado --> [*]
    
    note right of Programado
        Vuelo programado
        pero no iniciado
    end note
    
    note right of En_Vuelo
        Vuelo en progreso
        aeronave en ruta
    end note
    
    note right of Completado
        Vuelo finalizado
        exitosamente
    end note
    
    note right of Cancelado
        Vuelo cancelado
        por cualquier motivo
    end note
```

## Flujo de Confirmación de Vuelos

```mermaid
flowchart TD
    A[Operador Autorizado] --> B[Selecciona Vuelo]
    B --> C[Hace clic en Confirmar]
    C --> D[Modal de Confirmación]
    D --> E[Selecciona Estado]
    E --> F[Agrega Notas Opcionales]
    F --> G[Guarda Confirmación]
    G --> H{¿Éxito?}
    H -->|Sí| I[Actualiza Vista]
    H -->|No| J[Muestra Error]
    I --> K[Fin]
    J --> D
```

## Responsive Design - Breakpoints

```mermaid
graph LR
    A[Mobile<br/>320px-768px] --> B[Tablet<br/>768px-1024px]
    B --> C[Desktop<br/>1024px+]
    
    A --> D[Menú Colapsable]
    A --> E[Footer Ajustado]
    A --> F[Botones Grandes]
    
    B --> G[Menú Semi-Expandido]
    B --> H[Layout 2 Columnas]
    
    C --> I[Menú Completo]
    C --> J[Layout 3+ Columnas]
    C --> K[Sidebar Opcional]
```

## Flujo de Instalación

```mermaid
flowchart TD
    A[Descargar Proyecto] --> B[Crear Entorno Virtual]
    B --> C[Activar Entorno Virtual]
    C --> D[Instalar Dependencias]
    D --> E[Configurar Base de Datos]
    E --> F[Poblar Datos de Ejemplo]
    F --> G[Ejecutar Aplicación]
    G --> H[Acceder via Navegador]
    H --> I[Sistema Listo]
    
    D --> J[requirements.txt]
    E --> K[reset_db.py]
    F --> L[seed.py]
    G --> M[python app.py]
    H --> N[http://127.0.0.1:5000]
```

## Arquitectura de Seguridad

```mermaid
graph TB
    A[Cliente] --> B[HTTPS/SSL]
    B --> C[Flask App]
    C --> D[Flask-Login]
    D --> E[Session Management]
    E --> F[Role-Based Access]
    F --> G[API Endpoints]
    G --> H[Database]
    
    I[Password Hashing] --> D
    J[CSRF Protection] --> C
    K[Input Validation] --> G
    L[SQL Injection Prevention] --> H
```

Estos diagramas proporcionan una visión completa de la arquitectura, flujos y funcionalidades del Sistema de Gestión de Aeropuertos, complementando el Manual de Usuario con representaciones visuales claras y detalladas.
>>>>>>> 348e468 (Actualización de archivos y carpetas)
