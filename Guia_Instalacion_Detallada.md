<<<<<<< HEAD
# Guía de Instalación Detallada - Sistema de Gestión de Aeropuertos

## Tabla de Contenidos
1. [Instalación en Windows](#instalación-en-windows)
2. [Instalación en Linux/Ubuntu](#instalación-en-linuxubuntu)
3. [Instalación en macOS](#instalación-en-macos)
4. [Instalación en Docker](#instalación-en-docker)
5. [Configuración de Base de Datos](#configuración-de-base-de-datos)
6. [Configuración de Producción](#configuración-de-producción)
7. [Solución de Problemas](#solución-de-problemas)

---

## Instalación en Windows

### Requisitos Previos
- Windows 10 o superior
- Python 3.8+ (descargar desde [python.org](https://python.org))
- Git (opcional, para clonar repositorio)

### Paso 1: Verificar Python
```cmd
python --version
# Debe mostrar Python 3.8 o superior
```

Si no tienes Python instalado:
1. Descarga Python desde [python.org](https://python.org)
2. **IMPORTANTE:** Marca la casilla "Add Python to PATH" durante la instalación
3. Reinicia la terminal/CMD

### Paso 2: Descargar el Proyecto
```cmd
# Opción 1: Clonar con Git
git clone [URL_DEL_REPOSITORIO]
cd aeroSys

# Opción 2: Descargar ZIP y extraer
# Descargar el archivo ZIP del repositorio
# Extraer en una carpeta (ej: C:\aeroSys)
cd C:\aeroSys
```

### Paso 3: Crear Entorno Virtual
```cmd
# Crear entorno virtual
python -m venv venv

# Activar entorno virtual
venv\Scripts\activate

# Verificar que está activado (debe mostrar (venv) al inicio)
```

### Paso 4: Instalar Dependencias
```cmd
# Actualizar pip
python -m pip install --upgrade pip

# Instalar dependencias
pip install -r requirements.txt
```

### Paso 5: Configurar Base de Datos

#### ⚠️ ADVERTENCIA IMPORTANTE
**ANTES DE CONTINUAR:**
- 🚨 **SE BORRARÁ TODA LA INFORMACIÓN EXISTENTE** en las tablas
- 🚨 **NO SE PUEDE DESHACER** esta operación
- 🚨 **HAGA UN BACKUP** de sus datos importantes antes de proceder
- 🚨 **SOLO PARA DESARROLLO Y PRUEBAS** - NO usar en producción

#### Opción A: Poblar con Datos de Ejemplo (Recomendado para principiantes)
```cmd
# Generar datos de ejemplo completos
python seed.py
```

**¿Qué se crea?**
- 5 aeronaves de diferentes tipos
- 5 pilotos con licencias y horas de vuelo
- 5 vuelos con rutas realistas
- 5 confirmaciones con diferentes estados
- 5 usuarios con diferentes roles
- Configuración completa del aeropuerto

#### Opción B: Base de Datos Vacía
```cmd
# Solo crear las tablas sin datos
python reset_db.py
```

#### Opción C: Crear Solo Usuario Admin
```cmd
# Crear solo el usuario administrador
python -c "from app import app; from models import db, Usuario; app.app_context().push(); db.create_all(); admin = Usuario(username='admin', rol='admin') if not Usuario.query.filter_by(username='admin').first() else None; admin.set_password('123456') if admin else None; db.session.add(admin) if admin else None; db.session.commit() if admin else None; print('Usuario admin creado') if admin else print('Usuario admin ya existe')"
```

### Paso 6: Ejecutar Aplicación
```cmd
python app.py
```

### Paso 7: Acceder al Sistema
Abrir navegador y ir a: `http://127.0.0.1:5000`

**Credenciales por defecto:**
- Usuario: `admin`
- Contraseña: `123456`

---

## Instalación en Linux/Ubuntu

### Requisitos Previos
```bash
# Actualizar sistema
sudo apt update && sudo apt upgrade -y

# Instalar Python y pip
sudo apt install python3 python3-pip python3-venv -y

# Instalar Git (opcional)
sudo apt install git -y
```

### Paso 1: Verificar Python
```bash
python3 --version
# Debe mostrar Python 3.8 o superior
```

### Paso 2: Descargar el Proyecto
```bash
# Opción 1: Clonar con Git
git clone [URL_DEL_REPOSITORIO]
cd aeroSys

# Opción 2: Descargar y extraer
wget [URL_DEL_ZIP]
unzip aeroSys.zip
cd aeroSys
```

### Paso 3: Crear Entorno Virtual
```bash
# Crear entorno virtual
python3 -m venv venv

# Activar entorno virtual
source venv/bin/activate

# Verificar que está activado (debe mostrar (venv) al inicio)
```

### Paso 4: Instalar Dependencias
```bash
# Actualizar pip
python -m pip install --upgrade pip

# Instalar dependencias
pip install -r requirements.txt
```

### Paso 5: Configurar Base de Datos

#### ⚠️ ADVERTENCIA IMPORTANTE
**ANTES DE CONTINUAR:**
- 🚨 **SE BORRARÁ TODA LA INFORMACIÓN EXISTENTE** en las tablas
- 🚨 **NO SE PUEDE DESHACER** esta operación
- 🚨 **HAGA UN BACKUP** de sus datos importantes antes de proceder
- 🚨 **SOLO PARA DESARROLLO Y PRUEBAS** - NO usar en producción

#### Opción A: Poblar con Datos de Ejemplo (Recomendado para principiantes)
```bash
# Generar datos de ejemplo completos
python seed.py
```

**¿Qué se crea?**
- 5 aeronaves de diferentes tipos
- 5 pilotos con licencias y horas de vuelo
- 5 vuelos con rutas realistas
- 5 confirmaciones con diferentes estados
- 5 usuarios con diferentes roles
- Configuración completa del aeropuerto

#### Opción B: Base de Datos Vacía
```bash
# Solo crear las tablas sin datos
python reset_db.py
```

#### Opción C: Crear Solo Usuario Admin
```bash
# Crear solo el usuario administrador
python3 -c "
from app import app
from models import db, Usuario
with app.app_context():
    db.create_all()
    if not Usuario.query.filter_by(username='admin').first():
        admin = Usuario(username='admin', rol='admin')
        admin.set_password('123456')
        db.session.add(admin)
        db.session.commit()
        print('Usuario admin creado')
    else:
        print('Usuario admin ya existe')
"
```

### Paso 6: Ejecutar Aplicación
```bash
python app.py
```

### Paso 7: Acceder al Sistema
Abrir navegador y ir a: `http://127.0.0.1:5000`

---

## Instalación en macOS

### Requisitos Previos
- macOS 10.14 o superior
- Xcode Command Line Tools
- Homebrew (recomendado)

### Paso 1: Instalar Homebrew (si no lo tienes)
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

### Paso 2: Instalar Python
```bash
# Instalar Python
brew install python

# Verificar instalación
python3 --version
```

### Paso 3: Descargar el Proyecto
```bash
# Opción 1: Clonar con Git
git clone [URL_DEL_REPOSITORIO]
cd aeroSys

# Opción 2: Descargar y extraer
curl -L [URL_DEL_ZIP] -o aeroSys.zip
unzip aeroSys.zip
cd aeroSys
```

### Paso 4: Crear Entorno Virtual
```bash
# Crear entorno virtual
python3 -m venv venv

# Activar entorno virtual
source venv/bin/activate
```

### Paso 5: Instalar Dependencias
```bash
# Actualizar pip
python -m pip install --upgrade pip

# Instalar dependencias
pip install -r requirements.txt
```

### Paso 6: Configurar Base de Datos
```bash
python seed.py
```

### Paso 7: Ejecutar Aplicación
```bash
python app.py
```

---

## Instalación en Docker

### Requisitos Previos
- Docker instalado
- Docker Compose (opcional)

### Paso 1: Crear Dockerfile
```dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", "app.py"]
```

### Paso 2: Crear docker-compose.yml
```yaml
version: '3.8'

services:
  aerosys:
    build: .
    ports:
      - "5000:5000"
    volumes:
      - ./data:/app/data
    environment:
      - FLASK_ENV=production
```

### Paso 3: Construir y Ejecutar
```bash
# Construir imagen
docker build -t aerosys .

# Ejecutar contenedor
docker run -p 5000:5000 aerosys

# O usar docker-compose
docker-compose up -d
```

---

## Configuración de Base de Datos

### SQLite (Por Defecto)
```python
# En config.py
SQLALCHEMY_DATABASE_URI = 'sqlite:///aeropuertos.db'
```

### MySQL (Producción)
```python
# En config.py
SQLALCHEMY_DATABASE_URI = 'mysql://usuario:contraseña@localhost/aeropuertos'
```

### PostgreSQL (Producción)
```python
# En config.py
SQLALCHEMY_DATABASE_URI = 'postgresql://usuario:contraseña@localhost/aeropuertos'
```

### Configurar Base de Datos Externa
1. Instalar driver de base de datos:
```bash
# Para MySQL
pip install PyMySQL

# Para PostgreSQL
pip install psycopg2-binary
```

2. Actualizar `config.py` con la URI correcta
3. Ejecutar migraciones:
```bash
python reset_db.py
python seed.py
```

---

## Configuración de Producción

### Variables de Entorno
Crear archivo `.env`:
```env
FLASK_ENV=production
SECRET_KEY=tu_clave_secreta_muy_larga_y_segura
DATABASE_URL=mysql://usuario:contraseña@localhost/aeropuertos
```

### Configuración de Servidor Web (Nginx + Gunicorn)

#### Instalar Gunicorn
```bash
pip install gunicorn
```

#### Crear archivo wsgi.py
```python
from app import app

if __name__ == "__main__":
    app.run()
```

#### Ejecutar con Gunicorn
```bash
gunicorn -w 4 -b 0.0.0.0:5000 wsgi:app
```

#### Configuración Nginx
```nginx
server {
    listen 80;
    server_name tu-dominio.com;

    location / {
        proxy_pass http://127.0.0.1:5000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

### Configuración SSL (HTTPS)
```bash
# Instalar certificado SSL (Let's Encrypt)
sudo apt install certbot python3-certbot-nginx
sudo certbot --nginx -d tu-dominio.com
```

---

## Generación de Datos de Ejemplo

### ⚠️ ADVERTENCIA CRÍTICA
**LEA ESTO ANTES DE CONTINUAR:**
- 🚨 **SE ELIMINARÁ TODA LA INFORMACIÓN EXISTENTE** en la base de datos
- 🚨 **ESTA OPERACIÓN NO SE PUEDE DESHACER**
- 🚨 **HAGA BACKUP DE SUS DATOS IMPORTANTES** antes de proceder
- 🚨 **SOLO PARA DESARROLLO Y PRUEBAS** - NUNCA en producción

### ¿Cuándo Usar Datos de Ejemplo?
- ✅ **Primera instalación** del sistema
- ✅ **Ambiente de desarrollo** local
- ✅ **Demostraciones** y pruebas
- ✅ **Aprendizaje** de funcionalidades
- ❌ **NO usar** si ya tiene datos importantes
- ❌ **NO usar** en ambiente de producción

### Métodos para Generar Datos

#### Método 1: Script Completo (Recomendado)
```bash
# Generar todos los datos de ejemplo
python seed.py
```

**Datos que se crean:**
- 🛩️ **5 Aeronaves:** Airbus A320, Boeing 737, Cessna, A330, B787
- 👨‍✈️ **5 Pilotos:** Con nombres realistas y horas de vuelo
- ✈️ **5 Vuelos:** Rutas nacionales e internacionales
- 🎫 **5 Confirmaciones:** Estados variados (Confirmado, Pendiente, Cancelado)
- 👥 **5 Usuarios:** Diferentes roles (admin, operador, piloto, invitado)
- ⚙️ **Configuración:** Datos completos del aeropuerto

#### Método 2: Solo Usuario Admin
```bash
# Crear solo el usuario administrador
python -c "
from app import app
from models import db, Usuario
with app.app_context():
    db.create_all()
    if not Usuario.query.filter_by(username='admin').first():
        admin = Usuario(username='admin', rol='admin')
        admin.set_password('123456')
        db.session.add(admin)
        db.session.commit()
        print('✅ Usuario admin creado')
    else:
        print('ℹ️  Usuario admin ya existe')
"
```

#### Método 3: Base de Datos Vacía
```bash
# Solo crear las tablas sin datos
python reset_db.py
```

### Salida Esperada del Script
Al ejecutar `python seed.py`, verá:

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

### Credenciales de Usuario Generadas
- **admin** (Administrador) - Contraseña: 123456
- **operador1** (Operador) - Contraseña: 123456
- **piloto1** (Piloto) - Contraseña: 123456
- **invitado1** (Invitado) - Contraseña: 123456
- **supervisor** (Administrador) - Contraseña: 123456

### Restaurar Datos Originales
Si necesita volver a sus datos originales:

1. **Restaurar desde backup** (si tiene uno)
2. **Reconfigurar manualmente** todos los datos
3. **Contactar soporte** para asistencia

## Solución de Problemas

### Error: "python no se reconoce como comando"
**Solución Windows:**
1. Reinstalar Python marcando "Add to PATH"
2. O agregar manualmente al PATH:
   - Buscar "Variables de entorno" en Windows
   - Agregar `C:\Python39` y `C:\Python39\Scripts` al PATH

**Solución Linux/macOS:**
```bash
# Usar python3 en lugar de python
python3 --version
python3 -m venv venv
```

### Error: "pip no se reconoce como comando"
```bash
# Windows
python -m pip install --upgrade pip

# Linux/macOS
python3 -m pip install --upgrade pip
```

### Error: "ModuleNotFoundError"
```bash
# Verificar que el entorno virtual está activado
# Debe mostrar (venv) al inicio de la línea de comandos

# Reinstalar dependencias
pip install -r requirements.txt
```

### Error: "Permission denied" en Linux/macOS
```bash
# Dar permisos de ejecución
chmod +x app.py

# O ejecutar con python3
python3 app.py
```

### Error de Base de Datos
```bash
# Eliminar base de datos corrupta
rm aeropuertos.db

# Recrear base de datos
python reset_db.py
python seed.py
```

### Puerto 5000 ya en uso
```bash
# Encontrar proceso que usa el puerto
# Windows
netstat -ano | findstr :5000

# Linux/macOS
lsof -i :5000

# Matar proceso
# Windows
taskkill /PID [PID_NUMBER] /F

# Linux/macOS
kill -9 [PID_NUMBER]

# O cambiar puerto en app.py
app.run(host='0.0.0.0', port=5001, debug=True)
```

### Error de Memoria en Dispositivos Pequeños
```bash
# Reducir workers de Gunicorn
gunicorn -w 1 -b 0.0.0.0:5000 wsgi:app

# O usar modo desarrollo
python app.py
```

### Problemas de Red/Firewall
```bash
# Verificar que el puerto está abierto
# Windows
netsh advfirewall firewall add rule name="Flask App" dir=in action=allow protocol=TCP localport=5000

# Linux
sudo ufw allow 5000
```

---

## Comandos Útiles

### Desarrollo
```bash
# Ejecutar en modo desarrollo
python app.py

# Ejecutar con debug
export FLASK_DEBUG=1
python app.py
```

### Base de Datos
```bash
# Resetear base de datos
python reset_db.py

# Poblar con datos de ejemplo
python seed.py

# Crear migración
flask db migrate -m "Descripción del cambio"

# Aplicar migración
flask db upgrade
```

### Producción
```bash
# Ejecutar con Gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 wsgi:app

# Ejecutar en background
nohup gunicorn -w 4 -b 0.0.0.0:5000 wsgi:app &

# Ver logs
tail -f nohup.out
```

### Mantenimiento
```bash
# Backup de base de datos
cp aeropuertos.db backup_$(date +%Y%m%d).db

# Limpiar logs
rm -f nohup.out

# Actualizar dependencias
pip install --upgrade -r requirements.txt
```

---

## Checklist de Instalación

### Pre-instalación
- [ ] Python 3.8+ instalado
- [ ] Git instalado (opcional)
- [ ] Terminal/CMD funcionando
- [ ] Conexión a internet

### Instalación
- [ ] Proyecto descargado
- [ ] Entorno virtual creado
- [ ] Entorno virtual activado
- [ ] Dependencias instaladas
- [ ] Base de datos configurada
- [ ] Datos de ejemplo cargados

### Verificación
- [ ] Aplicación ejecutándose
- [ ] Navegador accede a http://127.0.0.1:5000
- [ ] Login funciona (admin/123456)
- [ ] Dashboard se muestra correctamente
- [ ] Footer muestra información del aeropuerto

### Producción
- [ ] Variables de entorno configuradas
- [ ] Base de datos externa configurada
- [ ] Servidor web configurado
- [ ] SSL configurado
- [ ] Backup automático configurado
- [ ] Monitoreo configurado

---

**¡Instalación completada exitosamente!** 🎉

El Sistema de Gestión de Aeropuertos está listo para usar. Consulta el [Manual de Usuario](Manual_de_Usuario.md) para aprender a usar todas las funcionalidades.
=======
# Guía de Instalación Detallada - Sistema de Gestión de Aeropuertos

## Tabla de Contenidos
1. [Instalación en Windows](#instalación-en-windows)
2. [Instalación en Linux/Ubuntu](#instalación-en-linuxubuntu)
3. [Instalación en macOS](#instalación-en-macos)
4. [Instalación en Docker](#instalación-en-docker)
5. [Configuración de Base de Datos](#configuración-de-base-de-datos)
6. [Configuración de Producción](#configuración-de-producción)
7. [Solución de Problemas](#solución-de-problemas)

---

## Instalación en Windows

### Requisitos Previos
- Windows 10 o superior
- Python 3.8+ (descargar desde [python.org](https://python.org))
- Git (opcional, para clonar repositorio)

### Paso 1: Verificar Python
```cmd
python --version
# Debe mostrar Python 3.8 o superior
```

Si no tienes Python instalado:
1. Descarga Python desde [python.org](https://python.org)
2. **IMPORTANTE:** Marca la casilla "Add Python to PATH" durante la instalación
3. Reinicia la terminal/CMD

### Paso 2: Descargar el Proyecto
```cmd
# Opción 1: Clonar con Git
git clone [URL_DEL_REPOSITORIO]
cd aeroSys

# Opción 2: Descargar ZIP y extraer
# Descargar el archivo ZIP del repositorio
# Extraer en una carpeta (ej: C:\aeroSys)
cd C:\aeroSys
```

### Paso 3: Crear Entorno Virtual
```cmd
# Crear entorno virtual
python -m venv venv

# Activar entorno virtual
venv\Scripts\activate

# Verificar que está activado (debe mostrar (venv) al inicio)
```

### Paso 4: Instalar Dependencias
```cmd
# Actualizar pip
python -m pip install --upgrade pip

# Instalar dependencias
pip install -r requirements.txt
```

### Paso 5: Configurar Base de Datos

#### ⚠️ ADVERTENCIA IMPORTANTE
**ANTES DE CONTINUAR:**
- 🚨 **SE BORRARÁ TODA LA INFORMACIÓN EXISTENTE** en las tablas
- 🚨 **NO SE PUEDE DESHACER** esta operación
- 🚨 **HAGA UN BACKUP** de sus datos importantes antes de proceder
- 🚨 **SOLO PARA DESARROLLO Y PRUEBAS** - NO usar en producción

#### Opción A: Poblar con Datos de Ejemplo (Recomendado para principiantes)
```cmd
# Generar datos de ejemplo completos
python seed.py
```

**¿Qué se crea?**
- 5 aeronaves de diferentes tipos
- 5 pilotos con licencias y horas de vuelo
- 5 vuelos con rutas realistas
- 5 confirmaciones con diferentes estados
- 5 usuarios con diferentes roles
- Configuración completa del aeropuerto

#### Opción B: Base de Datos Vacía
```cmd
# Solo crear las tablas sin datos
python reset_db.py
```

#### Opción C: Crear Solo Usuario Admin
```cmd
# Crear solo el usuario administrador
python -c "from app import app; from models import db, Usuario; app.app_context().push(); db.create_all(); admin = Usuario(username='admin', rol='admin') if not Usuario.query.filter_by(username='admin').first() else None; admin.set_password('123456') if admin else None; db.session.add(admin) if admin else None; db.session.commit() if admin else None; print('Usuario admin creado') if admin else print('Usuario admin ya existe')"
```

### Paso 6: Ejecutar Aplicación
```cmd
python app.py
```

### Paso 7: Acceder al Sistema
Abrir navegador y ir a: `http://127.0.0.1:5000`

**Credenciales por defecto:**
- Usuario: `admin`
- Contraseña: `123456`

---

## Instalación en Linux/Ubuntu

### Requisitos Previos
```bash
# Actualizar sistema
sudo apt update && sudo apt upgrade -y

# Instalar Python y pip
sudo apt install python3 python3-pip python3-venv -y

# Instalar Git (opcional)
sudo apt install git -y
```

### Paso 1: Verificar Python
```bash
python3 --version
# Debe mostrar Python 3.8 o superior
```

### Paso 2: Descargar el Proyecto
```bash
# Opción 1: Clonar con Git
git clone [URL_DEL_REPOSITORIO]
cd aeroSys

# Opción 2: Descargar y extraer
wget [URL_DEL_ZIP]
unzip aeroSys.zip
cd aeroSys
```

### Paso 3: Crear Entorno Virtual
```bash
# Crear entorno virtual
python3 -m venv venv

# Activar entorno virtual
source venv/bin/activate

# Verificar que está activado (debe mostrar (venv) al inicio)
```

### Paso 4: Instalar Dependencias
```bash
# Actualizar pip
python -m pip install --upgrade pip

# Instalar dependencias
pip install -r requirements.txt
```

### Paso 5: Configurar Base de Datos

#### ⚠️ ADVERTENCIA IMPORTANTE
**ANTES DE CONTINUAR:**
- 🚨 **SE BORRARÁ TODA LA INFORMACIÓN EXISTENTE** en las tablas
- 🚨 **NO SE PUEDE DESHACER** esta operación
- 🚨 **HAGA UN BACKUP** de sus datos importantes antes de proceder
- 🚨 **SOLO PARA DESARROLLO Y PRUEBAS** - NO usar en producción

#### Opción A: Poblar con Datos de Ejemplo (Recomendado para principiantes)
```bash
# Generar datos de ejemplo completos
python seed.py
```

**¿Qué se crea?**
- 5 aeronaves de diferentes tipos
- 5 pilotos con licencias y horas de vuelo
- 5 vuelos con rutas realistas
- 5 confirmaciones con diferentes estados
- 5 usuarios con diferentes roles
- Configuración completa del aeropuerto

#### Opción B: Base de Datos Vacía
```bash
# Solo crear las tablas sin datos
python reset_db.py
```

#### Opción C: Crear Solo Usuario Admin
```bash
# Crear solo el usuario administrador
python3 -c "
from app import app
from models import db, Usuario
with app.app_context():
    db.create_all()
    if not Usuario.query.filter_by(username='admin').first():
        admin = Usuario(username='admin', rol='admin')
        admin.set_password('123456')
        db.session.add(admin)
        db.session.commit()
        print('Usuario admin creado')
    else:
        print('Usuario admin ya existe')
"
```

### Paso 6: Ejecutar Aplicación
```bash
python app.py
```

### Paso 7: Acceder al Sistema
Abrir navegador y ir a: `http://127.0.0.1:5000`

---

## Instalación en macOS

### Requisitos Previos
- macOS 10.14 o superior
- Xcode Command Line Tools
- Homebrew (recomendado)

### Paso 1: Instalar Homebrew (si no lo tienes)
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

### Paso 2: Instalar Python
```bash
# Instalar Python
brew install python

# Verificar instalación
python3 --version
```

### Paso 3: Descargar el Proyecto
```bash
# Opción 1: Clonar con Git
git clone [URL_DEL_REPOSITORIO]
cd aeroSys

# Opción 2: Descargar y extraer
curl -L [URL_DEL_ZIP] -o aeroSys.zip
unzip aeroSys.zip
cd aeroSys
```

### Paso 4: Crear Entorno Virtual
```bash
# Crear entorno virtual
python3 -m venv venv

# Activar entorno virtual
source venv/bin/activate
```

### Paso 5: Instalar Dependencias
```bash
# Actualizar pip
python -m pip install --upgrade pip

# Instalar dependencias
pip install -r requirements.txt
```

### Paso 6: Configurar Base de Datos
```bash
python seed.py
```

### Paso 7: Ejecutar Aplicación
```bash
python app.py
```

---

## Instalación en Docker

### Requisitos Previos
- Docker instalado
- Docker Compose (opcional)

### Paso 1: Crear Dockerfile
```dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", "app.py"]
```

### Paso 2: Crear docker-compose.yml
```yaml
version: '3.8'

services:
  aerosys:
    build: .
    ports:
      - "5000:5000"
    volumes:
      - ./data:/app/data
    environment:
      - FLASK_ENV=production
```

### Paso 3: Construir y Ejecutar
```bash
# Construir imagen
docker build -t aerosys .

# Ejecutar contenedor
docker run -p 5000:5000 aerosys

# O usar docker-compose
docker-compose up -d
```

---

## Configuración de Base de Datos

### SQLite (Por Defecto)
```python
# En config.py
SQLALCHEMY_DATABASE_URI = 'sqlite:///aeropuertos.db'
```

### MySQL (Producción)
```python
# En config.py
SQLALCHEMY_DATABASE_URI = 'mysql://usuario:contraseña@localhost/aeropuertos'
```

### PostgreSQL (Producción)
```python
# En config.py
SQLALCHEMY_DATABASE_URI = 'postgresql://usuario:contraseña@localhost/aeropuertos'
```

### Configurar Base de Datos Externa
1. Instalar driver de base de datos:
```bash
# Para MySQL
pip install PyMySQL

# Para PostgreSQL
pip install psycopg2-binary
```

2. Actualizar `config.py` con la URI correcta
3. Ejecutar migraciones:
```bash
python reset_db.py
python seed.py
```

---

## Configuración de Producción

### Variables de Entorno
Crear archivo `.env`:
```env
FLASK_ENV=production
SECRET_KEY=tu_clave_secreta_muy_larga_y_segura
DATABASE_URL=mysql://usuario:contraseña@localhost/aeropuertos
```

### Configuración de Servidor Web (Nginx + Gunicorn)

#### Instalar Gunicorn
```bash
pip install gunicorn
```

#### Crear archivo wsgi.py
```python
from app import app

if __name__ == "__main__":
    app.run()
```

#### Ejecutar con Gunicorn
```bash
gunicorn -w 4 -b 0.0.0.0:5000 wsgi:app
```

#### Configuración Nginx
```nginx
server {
    listen 80;
    server_name tu-dominio.com;

    location / {
        proxy_pass http://127.0.0.1:5000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

### Configuración SSL (HTTPS)
```bash
# Instalar certificado SSL (Let's Encrypt)
sudo apt install certbot python3-certbot-nginx
sudo certbot --nginx -d tu-dominio.com
```

---

## Generación de Datos de Ejemplo

### ⚠️ ADVERTENCIA CRÍTICA
**LEA ESTO ANTES DE CONTINUAR:**
- 🚨 **SE ELIMINARÁ TODA LA INFORMACIÓN EXISTENTE** en la base de datos
- 🚨 **ESTA OPERACIÓN NO SE PUEDE DESHACER**
- 🚨 **HAGA BACKUP DE SUS DATOS IMPORTANTES** antes de proceder
- 🚨 **SOLO PARA DESARROLLO Y PRUEBAS** - NUNCA en producción

### ¿Cuándo Usar Datos de Ejemplo?
- ✅ **Primera instalación** del sistema
- ✅ **Ambiente de desarrollo** local
- ✅ **Demostraciones** y pruebas
- ✅ **Aprendizaje** de funcionalidades
- ❌ **NO usar** si ya tiene datos importantes
- ❌ **NO usar** en ambiente de producción

### Métodos para Generar Datos

#### Método 1: Script Completo (Recomendado)
```bash
# Generar todos los datos de ejemplo
python seed.py
```

**Datos que se crean:**
- 🛩️ **5 Aeronaves:** Airbus A320, Boeing 737, Cessna, A330, B787
- 👨‍✈️ **5 Pilotos:** Con nombres realistas y horas de vuelo
- ✈️ **5 Vuelos:** Rutas nacionales e internacionales
- 🎫 **5 Confirmaciones:** Estados variados (Confirmado, Pendiente, Cancelado)
- 👥 **5 Usuarios:** Diferentes roles (admin, operador, piloto, invitado)
- ⚙️ **Configuración:** Datos completos del aeropuerto

#### Método 2: Solo Usuario Admin
```bash
# Crear solo el usuario administrador
python -c "
from app import app
from models import db, Usuario
with app.app_context():
    db.create_all()
    if not Usuario.query.filter_by(username='admin').first():
        admin = Usuario(username='admin', rol='admin')
        admin.set_password('123456')
        db.session.add(admin)
        db.session.commit()
        print('✅ Usuario admin creado')
    else:
        print('ℹ️  Usuario admin ya existe')
"
```

#### Método 3: Base de Datos Vacía
```bash
# Solo crear las tablas sin datos
python reset_db.py
```

### Salida Esperada del Script
Al ejecutar `python seed.py`, verá:

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

### Credenciales de Usuario Generadas
- **admin** (Administrador) - Contraseña: 123456
- **operador1** (Operador) - Contraseña: 123456
- **piloto1** (Piloto) - Contraseña: 123456
- **invitado1** (Invitado) - Contraseña: 123456
- **supervisor** (Administrador) - Contraseña: 123456

### Restaurar Datos Originales
Si necesita volver a sus datos originales:

1. **Restaurar desde backup** (si tiene uno)
2. **Reconfigurar manualmente** todos los datos
3. **Contactar soporte** para asistencia

## Solución de Problemas

### Error: "python no se reconoce como comando"
**Solución Windows:**
1. Reinstalar Python marcando "Add to PATH"
2. O agregar manualmente al PATH:
   - Buscar "Variables de entorno" en Windows
   - Agregar `C:\Python39` y `C:\Python39\Scripts` al PATH

**Solución Linux/macOS:**
```bash
# Usar python3 en lugar de python
python3 --version
python3 -m venv venv
```

### Error: "pip no se reconoce como comando"
```bash
# Windows
python -m pip install --upgrade pip

# Linux/macOS
python3 -m pip install --upgrade pip
```

### Error: "ModuleNotFoundError"
```bash
# Verificar que el entorno virtual está activado
# Debe mostrar (venv) al inicio de la línea de comandos

# Reinstalar dependencias
pip install -r requirements.txt
```

### Error: "Permission denied" en Linux/macOS
```bash
# Dar permisos de ejecución
chmod +x app.py

# O ejecutar con python3
python3 app.py
```

### Error de Base de Datos
```bash
# Eliminar base de datos corrupta
rm aeropuertos.db

# Recrear base de datos
python reset_db.py
python seed.py
```

### Puerto 5000 ya en uso
```bash
# Encontrar proceso que usa el puerto
# Windows
netstat -ano | findstr :5000

# Linux/macOS
lsof -i :5000

# Matar proceso
# Windows
taskkill /PID [PID_NUMBER] /F

# Linux/macOS
kill -9 [PID_NUMBER]

# O cambiar puerto en app.py
app.run(host='0.0.0.0', port=5001, debug=True)
```

### Error de Memoria en Dispositivos Pequeños
```bash
# Reducir workers de Gunicorn
gunicorn -w 1 -b 0.0.0.0:5000 wsgi:app

# O usar modo desarrollo
python app.py
```

### Problemas de Red/Firewall
```bash
# Verificar que el puerto está abierto
# Windows
netsh advfirewall firewall add rule name="Flask App" dir=in action=allow protocol=TCP localport=5000

# Linux
sudo ufw allow 5000
```

---

## Comandos Útiles

### Desarrollo
```bash
# Ejecutar en modo desarrollo
python app.py

# Ejecutar con debug
export FLASK_DEBUG=1
python app.py
```

### Base de Datos
```bash
# Resetear base de datos
python reset_db.py

# Poblar con datos de ejemplo
python seed.py

# Crear migración
flask db migrate -m "Descripción del cambio"

# Aplicar migración
flask db upgrade
```

### Producción
```bash
# Ejecutar con Gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 wsgi:app

# Ejecutar en background
nohup gunicorn -w 4 -b 0.0.0.0:5000 wsgi:app &

# Ver logs
tail -f nohup.out
```

### Mantenimiento
```bash
# Backup de base de datos
cp aeropuertos.db backup_$(date +%Y%m%d).db

# Limpiar logs
rm -f nohup.out

# Actualizar dependencias
pip install --upgrade -r requirements.txt
```

---

## Checklist de Instalación

### Pre-instalación
- [ ] Python 3.8+ instalado
- [ ] Git instalado (opcional)
- [ ] Terminal/CMD funcionando
- [ ] Conexión a internet

### Instalación
- [ ] Proyecto descargado
- [ ] Entorno virtual creado
- [ ] Entorno virtual activado
- [ ] Dependencias instaladas
- [ ] Base de datos configurada
- [ ] Datos de ejemplo cargados

### Verificación
- [ ] Aplicación ejecutándose
- [ ] Navegador accede a http://127.0.0.1:5000
- [ ] Login funciona (admin/123456)
- [ ] Dashboard se muestra correctamente
- [ ] Footer muestra información del aeropuerto

### Producción
- [ ] Variables de entorno configuradas
- [ ] Base de datos externa configurada
- [ ] Servidor web configurado
- [ ] SSL configurado
- [ ] Backup automático configurado
- [ ] Monitoreo configurado

---

**¡Instalación completada exitosamente!** 🎉

El Sistema de Gestión de Aeropuertos está listo para usar. Consulta el [Manual de Usuario](Manual_de_Usuario.md) para aprender a usar todas las funcionalidades.
>>>>>>> 348e468 (Actualización de archivos y carpetas)
