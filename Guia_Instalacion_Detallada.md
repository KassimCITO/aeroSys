# Guía de Instalación Detallada - Sistema de Gestión de Aeropuertos

## Tabla de Contenidos
1. [Introducción](#introducción)
2. [Requisitos del Sistema](#requisitos-del-sistema)
3. [Instalación en Windows](#instalación-en-windows)
4. [Instalación en Linux](#instalación-en-linux)
5. [Instalación en macOS](#instalación-en-macos)
6. [Configuración de Base de Datos](#configuración-de-base-de-datos)
7. [Configuración de Producción](#configuración-de-producción)
8. [Solución de Problemas](#solución-de-problemas)
9. [Mantenimiento](#mantenimiento)

## Introducción

Esta guía proporciona instrucciones detalladas para instalar y configurar el Sistema de Gestión de Aeropuertos en diferentes sistemas operativos y entornos.

## Requisitos del Sistema

### Requisitos Mínimos
- **Sistema Operativo:** Windows 10, Ubuntu 18.04+, macOS 10.14+
- **Python:** 3.8 o superior
- **RAM:** 4GB mínimo, 8GB recomendado
- **Espacio en Disco:** 2GB libres
- **Navegador:** Chrome 80+, Firefox 75+, Safari 13+, Edge 80+

### Requisitos Recomendados
- **Sistema Operativo:** Windows 11, Ubuntu 20.04+, macOS 12+
- **Python:** 3.9 o superior
- **RAM:** 8GB o más
- **Espacio en Disco:** 5GB libres
- **Procesador:** 4 núcleos o más

## Instalación en Windows

### Paso 1: Instalar Python
1. Descarga Python desde [python.org](https://python.org)
2. Ejecuta el instalador
3. **IMPORTANTE:** Marca "Add Python to PATH"
4. Selecciona "Install Now"
5. Verifica la instalación:
   ```cmd
   python --version
   pip --version
   ```

### Paso 2: Clonar el Repositorio
1. Abre PowerShell o CMD como administrador
2. Navega al directorio deseado
3. Clona el repositorio:
   ```cmd
   git clone https://github.com/KassimCITO/aeroSys.git
   cd aeroSys
   ```

### Paso 3: Instalación Automática
1. Ejecuta el script de instalación:
   ```cmd
   python install.py
   ```
2. Sigue las instrucciones en pantalla
3. El script creará automáticamente:
   - Entorno virtual
   - Instalación de dependencias
   - Base de datos inicial
   - Usuario administrador

### Paso 4: Instalación Manual (Alternativa)
1. Crea el entorno virtual:
   ```cmd
   python -m venv venv
   ```

2. Activa el entorno virtual:
   ```cmd
   venv\Scripts\activate
   ```

3. Instala las dependencias:
   ```cmd
   pip install -r requirements.txt
   ```

4. Configura la base de datos:
   ```cmd
   python -m flask db upgrade
   ```

5. Pobla la base de datos:
   ```cmd
   python seed.py
   ```

### Paso 5: Ejecutar la Aplicación
1. Activa el entorno virtual:
   ```cmd
   venv\Scripts\activate
   ```

2. Ejecuta la aplicación:
   ```cmd
   python app.py
   ```

3. Abre el navegador en `http://localhost:5000`

## Instalación en Linux

### Paso 1: Actualizar el Sistema
```bash
sudo apt update
sudo apt upgrade -y
```

### Paso 2: Instalar Python y Dependencias
```bash
sudo apt install python3 python3-pip python3-venv git -y
```

### Paso 3: Clonar el Repositorio
```bash
git clone https://github.com/KassimCITO/aeroSys.git
cd aeroSys
```

### Paso 4: Instalación Automática
```bash
python3 install.py
```

### Paso 5: Instalación Manual (Alternativa)
1. Crear entorno virtual:
   ```bash
   python3 -m venv venv
   ```

2. Activar entorno virtual:
   ```bash
   source venv/bin/activate
   ```

3. Instalar dependencias:
   ```bash
   pip install -r requirements.txt
   ```

4. Configurar base de datos:
   ```bash
   python -m flask db upgrade
   ```

5. Poblar base de datos:
   ```bash
   python seed.py
   ```

### Paso 6: Ejecutar la Aplicación
```bash
source venv/bin/activate
python app.py
```

## Instalación en macOS

### Paso 1: Instalar Homebrew (si no está instalado)
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

### Paso 2: Instalar Python
```bash
brew install python3
```

### Paso 3: Clonar el Repositorio
```bash
git clone https://github.com/KassimCITO/aeroSys.git
cd aeroSys
```

### Paso 4: Instalación Automática
```bash
python3 install.py
```

### Paso 5: Instalación Manual (Alternativa)
1. Crear entorno virtual:
   ```bash
   python3 -m venv venv
   ```

2. Activar entorno virtual:
   ```bash
   source venv/bin/activate
   ```

3. Instalar dependencias:
   ```bash
   pip install -r requirements.txt
   ```

4. Configurar base de datos:
   ```bash
   python -m flask db upgrade
   ```

5. Poblar base de datos:
   ```bash
   python seed.py
   ```

### Paso 6: Ejecutar la Aplicación
```bash
source venv/bin/activate
python app.py
```

## Configuración de Base de Datos

### SQLite (Desarrollo)
La aplicación usa SQLite por defecto para desarrollo. No requiere configuración adicional.

### MySQL (Producción)
1. Instala MySQL:
   ```bash
   # Ubuntu/Debian
   sudo apt install mysql-server
   
   # CentOS/RHEL
   sudo yum install mysql-server
   
   # macOS
   brew install mysql
   ```

2. Crea la base de datos:
   ```sql
   CREATE DATABASE aeropuertos;
   CREATE USER 'aerosys'@'localhost' IDENTIFIED BY 'password';
   GRANT ALL PRIVILEGES ON aeropuertos.* TO 'aerosys'@'localhost';
   FLUSH PRIVILEGES;
   ```

3. Configura la aplicación:
   ```bash
   cp config.env.example .env
   # Edita .env con la configuración de MySQL
   ```

### PostgreSQL (Producción)
1. Instala PostgreSQL:
   ```bash
   # Ubuntu/Debian
   sudo apt install postgresql postgresql-contrib
   
   # CentOS/RHEL
   sudo yum install postgresql postgresql-server
   
   # macOS
   brew install postgresql
   ```

2. Crea la base de datos:
   ```sql
   CREATE DATABASE aeropuertos;
   CREATE USER aerosys WITH PASSWORD 'password';
   GRANT ALL PRIVILEGES ON DATABASE aeropuertos TO aerosys;
   ```

3. Configura la aplicación:
   ```bash
   cp config.env.example .env
   # Edita .env con la configuración de PostgreSQL
   ```

## Configuración de Producción

### Usando Gunicorn
1. Instala Gunicorn:
   ```bash
   pip install gunicorn
   ```

2. Crea un archivo `wsgi.py`:
   ```python
   from app import app

   if __name__ == "__main__":
       app.run()
   ```

3. Ejecuta con Gunicorn:
   ```bash
   gunicorn -w 4 -b 0.0.0.0:8000 wsgi:app
   ```

### Usando Nginx como Proxy Reverso
1. Instala Nginx:
   ```bash
   # Ubuntu/Debian
   sudo apt install nginx
   
   # CentOS/RHEL
   sudo yum install nginx
   ```

2. Configura Nginx:
   ```nginx
   server {
       listen 80;
       server_name tu-dominio.com;

       location / {
           proxy_pass http://127.0.0.1:8000;
           proxy_set_header Host $host;
           proxy_set_header X-Real-IP $remote_addr;
           proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
           proxy_set_header X-Forwarded-Proto $scheme;
       }
   }
   ```

3. Reinicia Nginx:
   ```bash
   sudo systemctl restart nginx
   ```

### Configuración de HTTPS
1. Instala Certbot:
   ```bash
   sudo apt install certbot python3-certbot-nginx
   ```

2. Obtén certificado SSL:
   ```bash
   sudo certbot --nginx -d tu-dominio.com
   ```

### Configuración de Servicio Systemd
1. Crea el archivo de servicio:
   ```bash
   sudo nano /etc/systemd/system/aerosys.service
   ```

2. Contenido del archivo:
   ```ini
   [Unit]
   Description=AeroSys Web Application
   After=network.target

   [Service]
   User=www-data
   Group=www-data
   WorkingDirectory=/path/to/aeroSys
   Environment="PATH=/path/to/aeroSys/venv/bin"
   ExecStart=/path/to/aeroSys/venv/bin/gunicorn --workers 3 --bind unix:/path/to/aeroSys/aerosys.sock -m 007 wsgi:app
   ExecReload=/bin/kill -s HUP $MAINPID
   Restart=always

   [Install]
   WantedBy=multi-user.target
   ```

3. Habilita y inicia el servicio:
   ```bash
   sudo systemctl enable aerosys
   sudo systemctl start aerosys
   ```

## Solución de Problemas

### Error: "Python no encontrado"
- Verifica que Python esté instalado y en el PATH
- En Windows, reinstala Python marcando "Add to PATH"

### Error: "pip no encontrado"
- Instala pip:
  ```bash
  python -m ensurepip --upgrade
  ```

### Error: "Módulo no encontrado"
- Verifica que el entorno virtual esté activado
- Reinstala las dependencias:
  ```bash
  pip install -r requirements.txt
  ```

### Error: "Base de datos no encontrada"
- Ejecuta las migraciones:
  ```bash
  python -m flask db upgrade
  ```

### Error: "Puerto en uso"
- Cambia el puerto en `app.py`:
  ```python
  app.run(host='0.0.0.0', port=5001, debug=True)
  ```

### Error: "Permisos denegados"
- En Linux/macOS, usa sudo si es necesario
- Verifica permisos del directorio:
  ```bash
  chmod -R 755 /path/to/aeroSys
  ```

## Mantenimiento

### Backup de Base de Datos
1. **SQLite:**
   ```bash
   cp aeropuertos.db backup_aeropuertos_$(date +%Y%m%d).db
   ```

2. **MySQL:**
   ```bash
   mysqldump -u aerosys -p aeropuertos > backup_aeropuertos_$(date +%Y%m%d).sql
   ```

3. **PostgreSQL:**
   ```bash
   pg_dump -U aerosys aeropuertos > backup_aeropuertos_$(date +%Y%m%d).sql
   ```

### Actualización del Sistema
1. Haz backup de la base de datos
2. Descarga la nueva versión:
   ```bash
   git pull origin main
   ```
3. Actualiza las dependencias:
   ```bash
   pip install -r requirements.txt
   ```
4. Ejecuta las migraciones:
   ```bash
   python -m flask db upgrade
   ```

### Monitoreo
- Revisa los logs en `app.log`
- Monitorea el uso de CPU y memoria
- Verifica el espacio en disco regularmente

### Limpieza
- Limpia archivos temporales regularmente
- Elimina logs antiguos
- Optimiza la base de datos periódicamente

---

**Versión de la Guía:** 1.0  
**Última Actualización:** Octubre 2025  
**Sistema:** Sistema de Gestión de Aeropuertos v1.0