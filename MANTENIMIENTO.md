# 🔧 Guía de Mantenimiento del Sistema

## 📋 Tareas de Mantenimiento Regular

### Diarias

#### 1. Verificar Logs de Errores
```bash
# Ver últimos errores en la aplicación
tail -f logs/app.log  # Si tienes logging configurado

# O revisar en la consola al ejecutar
python app.py
```

#### 2. Backup de Base de Datos
```bash
# Crear backup diario
cp aeropuertos.db backups/aeropuertos_$(date +%Y%m%d).db

# Mantener solo últimos 7 días
find backups/ -name "aeropuertos_*.db" -mtime +7 -delete
```

### Semanales

#### 1. Limpiar Archivos Temporales
```bash
# Ejecutar script de limpieza
./limpiar_proyecto.sh  # Linux/Mac
limpiar_proyecto.bat   # Windows
```

#### 2. Verificar Espacio en Disco
```bash
# Ver tamaño de la base de datos
du -h aeropuertos.db

# Ver tamaño de uploads
du -sh static/uploads/
```

#### 3. Actualizar Dependencias
```bash
# Activar entorno virtual
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# Ver dependencias desactualizadas
pip list --outdated

# Actualizar (con precaución)
pip install --upgrade <paquete>
```

### Mensuales

#### 1. Optimizar Base de Datos
```bash
# Ejecutar desde Python
python -c "from app import app; from models import db; \
with app.app_context(): db.engine.execute('VACUUM')"
```

#### 2. Revisar Usuarios Inactivos
```python
# Script para listar usuarios sin actividad
from app import app
from models import db, Usuario

with app.app_context():
    usuarios = Usuario.query.all()
    for u in usuarios:
        print(f"{u.username} - Rol: {u.rol} - Creado: {u.created_at}")
```

#### 3. Generar Reporte de Uso
```bash
# Estadísticas de la base de datos
python -c "from app import app; from models import db, Vuelo, Confirmacion; \
with app.app_context(): \
    print(f'Vuelos: {Vuelo.query.count()}'); \
    print(f'Confirmaciones: {Confirmacion.query.count()}')"
```

---

## 🗄️ Gestión de Base de Datos

### Backup Manual
```bash
# Crear backup con timestamp
cp aeropuertos.db aeropuertos_backup_$(date +%Y%m%d_%H%M%S).db
```

### Restaurar Backup
```bash
# Detener la aplicación primero
# Luego restaurar
cp aeropuertos_backup_YYYYMMDD_HHMMSS.db aeropuertos.db
```

### Resetear Base de Datos
```bash
# ADVERTENCIA: Esto eliminará todos los datos
python reset_db.py

# O regenerar con datos de ejemplo
python seed.py
```

### Migraciones
```bash
# Crear nueva migración
flask db migrate -m "Descripción del cambio"

# Aplicar migraciones
flask db upgrade

# Revertir última migración
flask db downgrade
```

---

## 📁 Gestión de Archivos

### Limpiar Uploads Antiguos
```bash
# Eliminar imágenes de aeronaves no usadas
# (Requiere script personalizado)

# Ver archivos en uploads
ls -lh static/uploads/

# Eliminar archivos específicos
rm static/uploads/archivo_viejo.jpg
```

### Verificar Integridad de Archivos
```bash
# Verificar que existen archivos críticos
test -f static/js/vuelos_confirmacion.js && echo "✅ OK" || echo "❌ FALTA"
test -f templates/vuelos.html && echo "✅ OK" || echo "❌ FALTA"
test -f api.py && echo "✅ OK" || echo "❌ FALTA"
```

---

## 🔐 Seguridad

### Cambiar Contraseñas de Usuarios
```python
from app import app
from models import db, Usuario

with app.app_context():
    usuario = Usuario.query.filter_by(username='admin').first()
    usuario.set_password('nueva_contraseña_segura')
    db.session.commit()
    print("Contraseña actualizada")
```

### Rotar SECRET_KEY
```bash
# 1. Generar nueva clave
python -c "import secrets; print(secrets.token_hex(32))"

# 2. Actualizar en .env
# SECRET_KEY=nueva_clave_generada

# 3. Reiniciar aplicación
```

### Revisar Permisos de Archivos
```bash
# Asegurar que .env no sea público
chmod 600 .env

# Verificar permisos de base de datos
chmod 644 aeropuertos.db
```

---

## 🐛 Solución de Problemas Comunes

### Error: "No module named 'flask'"
```bash
# Activar entorno virtual
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# Reinstalar dependencias
pip install -r requirements.txt
```

### Error: "Database is locked"
```bash
# Cerrar todas las conexiones
pkill -f "python app.py"

# Esperar unos segundos
sleep 5

# Reiniciar aplicación
python app.py
```

### Error: "Template not found"
```bash
# Verificar estructura de directorios
ls -la templates/

# Reinstalar si es necesario
python install.py
```

### Error: "Static file not found"
```bash
# Verificar archivos JavaScript
ls -la static/js/

# Verificar que vuelos_confirmacion.js existe
test -f static/js/vuelos_confirmacion.js && echo "Existe" || echo "No existe"
```

### Modal no se abre al crear vuelo
```javascript
// Verificar en consola del navegador (F12)
// Buscar errores JavaScript

// Verificar que el script está cargado
console.log(typeof crearConfirmacionAutomatica);
// Debe mostrar: "function"
```

### Confirmación no se actualiza
```bash
# Verificar logs del servidor
# Buscar errores 403 (permisos) o 404 (ruta no encontrada)

# Verificar que el endpoint existe
curl -X GET http://localhost:5000/api/confirmaciones/1
```

---

## 📊 Monitoreo

### Verificar Estado del Sistema
```bash
# Ver procesos de Python
ps aux | grep python

# Ver uso de memoria
free -h

# Ver espacio en disco
df -h
```

### Logs de Acceso
```bash
# Si usas un servidor web (nginx, apache)
tail -f /var/log/nginx/access.log

# O revisar logs de Flask
# (Configurar logging en app.py)
```

### Métricas de Rendimiento
```python
# Script para medir tiempo de respuesta
import time
from app import app

with app.test_client() as client:
    start = time.time()
    response = client.get('/api/vuelos')
    end = time.time()
    print(f"Tiempo de respuesta: {end - start:.3f}s")
```

---

## 🔄 Actualizaciones

### Actualizar el Sistema
```bash
# 1. Hacer backup
cp aeropuertos.db aeropuertos_backup.db

# 2. Activar entorno virtual
source venv/bin/activate

# 3. Actualizar código (si usas Git)
git pull origin main

# 4. Actualizar dependencias
pip install -r requirements.txt --upgrade

# 5. Aplicar migraciones
flask db upgrade

# 6. Reiniciar aplicación
python app.py
```

### Verificar Versión
```python
# Agregar en app.py
VERSION = "1.1.0"

# Mostrar en dashboard o logs
print(f"Sistema versión {VERSION}")
```

---

## 📝 Checklist de Mantenimiento

### Diario
- [ ] Verificar que la aplicación está corriendo
- [ ] Revisar logs de errores
- [ ] Backup de base de datos

### Semanal
- [ ] Limpiar archivos temporales
- [ ] Verificar espacio en disco
- [ ] Revisar uploads innecesarios

### Mensual
- [ ] Optimizar base de datos
- [ ] Actualizar dependencias
- [ ] Revisar usuarios inactivos
- [ ] Generar reporte de uso

### Trimestral
- [ ] Cambiar contraseñas de admin
- [ ] Rotar SECRET_KEY
- [ ] Auditoría de seguridad
- [ ] Revisar y actualizar documentación

---

## 🚨 Plan de Contingencia

### Si la aplicación no inicia
1. Verificar que el entorno virtual está activado
2. Verificar que todas las dependencias están instaladas
3. Revisar logs de error
4. Verificar que la base de datos existe
5. Verificar permisos de archivos

### Si hay pérdida de datos
1. Detener la aplicación inmediatamente
2. Restaurar desde el backup más reciente
3. Verificar integridad de datos
4. Reiniciar aplicación
5. Documentar el incidente

### Si hay problemas de rendimiento
1. Verificar uso de CPU y memoria
2. Optimizar base de datos (VACUUM)
3. Limpiar archivos temporales
4. Reiniciar aplicación
5. Considerar migrar a servidor más potente

---

## 📞 Contactos de Soporte

### Recursos
- **Documentación**: Manual_de_Usuario.md
- **Cambios**: CHANGELOG.md
- **Instalación**: install.py
- **Datos de prueba**: seed.py

### Comandos Rápidos
```bash
# Reiniciar desde cero
python install.py

# Regenerar datos de prueba
python seed.py

# Limpiar proyecto
./limpiar_proyecto.sh
```

---

## ✅ Buenas Prácticas

1. **Siempre hacer backup antes de cambios importantes**
2. **Probar en entorno de desarrollo primero**
3. **Documentar todos los cambios**
4. **Mantener dependencias actualizadas**
5. **Revisar logs regularmente**
6. **Usar control de versiones (Git)**
7. **Mantener .env seguro y privado**
8. **No subir datos sensibles al repositorio**

---

**Última actualización**: 10 de Octubre de 2025  
**Versión del documento**: 1.0
