#!/bin/bash
# Script para limpiar archivos innecesarios del proyecto

echo "🧹 Limpiando proyecto aeroSys..."
echo ""

# Crear backup antes de eliminar
echo "📦 Creando backup de archivos a eliminar..."
mkdir -p .backup_limpieza_$(date +%Y%m%d_%H%M%S)
BACKUP_DIR=".backup_limpieza_$(date +%Y%m%d_%H%M%S)"

# Función para mover a backup antes de eliminar
backup_and_remove() {
    if [ -f "$1" ] || [ -d "$1" ]; then
        echo "  ✓ Respaldando y eliminando: $1"
        mv "$1" "$BACKUP_DIR/" 2>/dev/null
    fi
}

# 1. Archivos de documentación duplicados (DOCX y PDF)
echo ""
echo "📄 Eliminando documentación duplicada..."
backup_and_remove "Guia_Instalacion_Detallada.docx"
backup_and_remove "Guia_Instalacion_Detallada.pdf"
backup_and_remove "Manual_de_Usuario.docx"
backup_and_remove "Manual_de_Usuario.pdf"
backup_and_remove "custom-reference.docx"
backup_and_remove "reference.docx"

# 2. Carpeta temporal de LaTeX
echo ""
echo "📁 Eliminando carpetas temporales..."
backup_and_remove "media-203f20de19922b04"

# 3. Scripts de integración ya aplicados
echo ""
echo "🔧 Eliminando scripts de integración aplicados..."
backup_and_remove "CAMBIOS_MANUALES_VUELOS.txt"
backup_and_remove "INSTRUCCIONES_INTEGRACION_CONFIRMACIONES.md"
backup_and_remove "aplicar_cambios_vuelos.py"
backup_and_remove "aplicar_cambios_vuelos.sh"

# 4. Scripts de mejoras aplicadas
echo ""
echo "⚙️  Eliminando scripts de mejoras aplicadas..."
backup_and_remove "agregar_transiciones_suaves.py"

# 5. Archivos de cache de Python
echo ""
echo "🗑️  Eliminando archivos de cache..."
find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null
find . -type f -name "*.pyc" -delete 2>/dev/null
find . -type f -name "*.pyo" -delete 2>/dev/null
find . -type f -name "*.pyd" -delete 2>/dev/null

# 6. Archivos de backup antiguos
echo ""
echo "🔙 Eliminando backups antiguos de templates..."
find templates/ -name "*.backup*" -type f -delete 2>/dev/null
find templates/ -name "*.bak" -type f -delete 2>/dev/null

# Resumen
echo ""
echo "✅ Limpieza completada!"
echo ""
echo "📊 Resumen:"
echo "  - Archivos respaldados en: $BACKUP_DIR"
echo "  - Si todo funciona bien, puedes eliminar la carpeta de backup"
echo ""
echo "Para eliminar el backup después de verificar:"
echo "  rm -rf $BACKUP_DIR"
echo ""
echo "🎉 Proyecto limpio y organizado!"
