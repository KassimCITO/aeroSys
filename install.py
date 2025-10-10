#!/usr/bin/env python3
"""
Script de instalación automática para el Sistema de Gestión de Aeropuertos
Ejecutar: python install.py
"""

import os
import sys
import subprocess
import platform
import shutil
from pathlib import Path

def print_banner():
    """Muestra el banner de instalación"""
    print("=" * 60)
    print("  SISTEMA DE GESTIÓN DE AEROPUERTOS - INSTALADOR")
    print("=" * 60)
    print()

def check_python_version():
    """Verifica la versión de Python"""
    print("🔍 Verificando versión de Python...")
    version = sys.version_info
    if version.major < 3 or (version.major == 3 and version.minor < 8):
        print("❌ Error: Se requiere Python 3.8 o superior")
        print(f"   Versión actual: {version.major}.{version.minor}.{version.micro}")
        print("   Descarga Python desde: https://python.org")
        return False
    print(f"✅ Python {version.major}.{version.minor}.{version.micro} detectado")
    return True

def check_pip():
    """Verifica que pip esté disponible"""
    print("🔍 Verificando pip...")
    try:
        import pip
        print("✅ pip disponible")
        return True
    except ImportError:
        print("❌ Error: pip no está disponible")
        print("   Instala pip: https://pip.pypa.io/en/stable/installation/")
        return False

def create_virtual_environment():
    """Crea el entorno virtual"""
    print("🔧 Creando entorno virtual...")
    venv_path = Path("venv")
    
    if venv_path.exists():
        print("⚠️  El entorno virtual ya existe")
        response = input("¿Deseas recrearlo? (s/N): ").lower()
        if response == 's':
            shutil.rmtree(venv_path)
        else:
            print("✅ Usando entorno virtual existente")
            return True
    
    try:
        subprocess.run([sys.executable, "-m", "venv", "venv"], check=True)
        print("✅ Entorno virtual creado exitosamente")
        return True
    except subprocess.CalledProcessError:
        print("❌ Error al crear entorno virtual")
        return False

def get_activation_command():
    """Retorna el comando de activación según el SO"""
    system = platform.system().lower()
    if system == "windows":
        return "venv\\Scripts\\activate"
    else:
        return "source venv/bin/activate"

def get_python_executable():
    """Retorna la ruta del ejecutable de Python en el entorno virtual"""
    system = platform.system().lower()
    if system == "windows":
        return "venv\\Scripts\\python.exe"
    else:
        return "venv/bin/python"

def install_dependencies():
    """Instala las dependencias"""
    print("📦 Instalando dependencias...")
    python_exe = get_python_executable()
    
    try:
        # Actualizar pip
        print("   Actualizando pip...")
        subprocess.run([python_exe, "-m", "pip", "install", "--upgrade", "pip"], 
                      check=True, capture_output=True)
        
        # Instalar dependencias
        print("   Instalando dependencias del proyecto...")
        subprocess.run([python_exe, "-m", "pip", "install", "-r", "requirements.txt"], 
                      check=True, capture_output=True)
        
        print("✅ Dependencias instaladas exitosamente")
        return True
    except subprocess.CalledProcessError as e:
        print("❌ Error al instalar dependencias")
        print(f"   Error: {e}")
        return False

def verify_project_structure():
    """Verifica que la estructura del proyecto sea correcta"""
    print("🔍 Verificando estructura del proyecto...")
    
    required_dirs = ['templates', 'static', 'static/js', 'static/css', 'auth', 'routes']
    required_files = [
        'app.py', 'api.py', 'models.py', 'config.py', 'reports.py',
        'static/js/vuelos_confirmacion.js'
    ]
    
    missing_items = []
    
    # Verificar directorios
    for directory in required_dirs:
        if not Path(directory).exists():
            missing_items.append(f"Directorio: {directory}")
    
    # Verificar archivos
    for file in required_files:
        if not Path(file).exists():
            missing_items.append(f"Archivo: {file}")
    
    if missing_items:
        print("⚠️  Advertencia: Faltan algunos archivos/directorios:")
        for item in missing_items:
            print(f"   - {item}")
        print("   El sistema puede no funcionar correctamente")
        return False
    
    print("✅ Estructura del proyecto verificada")
    return True

def setup_database():
    """Configura la base de datos"""
    print("🗄️  Configurando base de datos...")
    print("⚠️  ADVERTENCIA: Se eliminará toda la información existente")
    
    # Preguntar al usuario si desea continuar
    response = input("¿Desea continuar con la generación de datos de ejemplo? (s/N): ").lower()
    if response != 's':
        print("ℹ️  Saltando generación de datos de ejemplo")
        print("   Puede ejecutar 'python seed.py' más tarde si lo desea")
        return True
    
    python_exe = get_python_executable()
    
    try:
        # Crear y poblar base de datos
        subprocess.run([python_exe, "seed.py"], check=True, capture_output=True)
        print("✅ Base de datos configurada exitosamente")
        print("   Se crearon 5 registros por tabla con datos de ejemplo")
        print("   ✓ Aeronaves, Pilotos, Vuelos")
        print("   ✓ Confirmaciones (automáticas)")
        print("   ✓ Usuarios con diferentes roles")
        return True
    except subprocess.CalledProcessError as e:
        print("❌ Error al configurar base de datos")
        print(f"   Error: {e}")
        return False

def create_start_script():
    """Crea script de inicio"""
    system = platform.system().lower()
    
    if system == "windows":
        script_content = """@echo off
echo Iniciando Sistema de Gestión de Aeropuertos...
call venv\\Scripts\\activate
python app.py
pause
"""
        with open("start.bat", "w") as f:
            f.write(script_content)
    else:
        script_content = """#!/bin/bash
echo "Iniciando Sistema de Gestión de Aeropuertos..."
source venv/bin/activate
python app.py
"""
        with open("start.sh", "w") as f:
            f.write(script_content)
        os.chmod("start.sh", 0o755)
    
    print("✅ Script de inicio creado")

def create_config_file():
    """Crea archivo de configuración de ejemplo"""
    config_content = """# Configuración del Sistema de Gestión de Aeropuertos
# Copia este archivo como .env y modifica los valores según tu entorno

# Entorno de ejecución
FLASK_ENV=development
FLASK_DEBUG=True

# Clave secreta (genera una nueva para producción)
SECRET_KEY=tu_clave_secreta_muy_larga_y_segura_aqui

# Base de datos
DATABASE_URL=sqlite:///aeropuertos.db

# Para producción con MySQL:
# DATABASE_URL=mysql://usuario:contraseña@localhost/aeropuertos

# Para producción con PostgreSQL:
# DATABASE_URL=postgresql://usuario:contraseña@localhost/aeropuertos

# Configuración del servidor
HOST=0.0.0.0
PORT=5000

# Configuración del aeropuerto (valores por defecto)
AIRPORT_NAME=Mi Aeropuerto
AIRPORT_CITY=Ciudad
AIRPORT_STATE=Estado
AIRPORT_COUNTRY=México
"""
    
    with open("config.env.example", "w") as f:
        f.write(config_content)
    
    print("✅ Archivo de configuración de ejemplo creado")

def show_final_instructions():
    """Muestra las instrucciones finales"""
    activation_cmd = get_activation_command()
    system = platform.system().lower()
    
    print("\n" + "=" * 60)
    print("  ¡INSTALACIÓN COMPLETADA EXITOSAMENTE! 🎉")
    print("=" * 60)
    print()
    print("📋 PRÓXIMOS PASOS:")
    print()
    print("1. Activar el entorno virtual:")
    print(f"   {activation_cmd}")
    print()
    print("2. Ejecutar la aplicación:")
    if system == "windows":
        print("   start.bat")
        print("   O manualmente: python app.py")
    else:
        print("   ./start.sh")
        print("   O manualmente: python app.py")
    print()
    print("3. Abrir el navegador en:")
    print("   http://127.0.0.1:5000")
    print()
    print("4. Iniciar sesión con:")
    print("   Usuario: admin")
    print("   Contraseña: 123456")
    print()
    print("📚 DOCUMENTACIÓN:")
    print("   - Manual de Usuario: Manual_de_Usuario.md")
    print("   - Guía de Instalación: Guia_Instalacion_Detallada.md")
    print("   - Diagramas del Sistema: Diagramas_Sistema.md")
    print("   - Resumen de Limpieza: RESUMEN_LIMPIEZA.md")
    print()
    print("🔧 CONFIGURACIÓN:")
    print("   - Archivo de ejemplo: config.env.example")
    print("   - Copia a .env y modifica según necesites")
    print()
    print("✨ CARACTERÍSTICAS PRINCIPALES:")
    print("   - Gestión de Aeronaves, Pilotos y Vuelos")
    print("   - Sistema de Confirmaciones Automáticas")
    print("   - Control de Acceso por Roles")
    print("   - Generación de Reportes PDF/Excel")
    print("   - Interfaz Responsiva y Moderna")
    print()
    print("=" * 60)

def main():
    """Función principal de instalación"""
    print_banner()
    
    # Verificaciones previas
    if not check_python_version():
        sys.exit(1)
    
    if not check_pip():
        sys.exit(1)
    
    # Verificar que requirements.txt existe
    if not Path("requirements.txt").exists():
        print("❌ Error: No se encontró requirements.txt")
        print("   Asegúrate de ejecutar este script desde el directorio del proyecto")
        sys.exit(1)
    
    # Proceso de instalación
    steps = [
        ("Verificando estructura del proyecto", verify_project_structure),
        ("Creando entorno virtual", create_virtual_environment),
        ("Instalando dependencias", install_dependencies),
        ("Configurando base de datos", setup_database),
        ("Creando archivos auxiliares", lambda: (create_start_script(), create_config_file(), True)),
    ]
    
    for step_name, step_func in steps:
        print(f"\n🔄 {step_name}...")
        if not step_func():
            print(f"❌ Error en: {step_name}")
            sys.exit(1)
    
    # Mostrar instrucciones finales
    show_final_instructions()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n❌ Instalación cancelada por el usuario")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Error inesperado: {e}")
        sys.exit(1)
