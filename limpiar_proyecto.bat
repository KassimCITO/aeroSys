@echo off
REM Script para limpiar archivos innecesarios del proyecto en Windows

echo ====================================
echo    Limpiando proyecto aeroSys
echo ====================================
echo.

REM Crear carpeta de backup
set BACKUP_DIR=.backup_limpieza_%date:~-4,4%%date:~-7,2%%date:~-10,2%_%time:~0,2%%time:~3,2%%time:~6,2%
set BACKUP_DIR=%BACKUP_DIR: =0%
mkdir "%BACKUP_DIR%" 2>nul

echo Backup creado en: %BACKUP_DIR%
echo.

REM 1. Archivos de documentación duplicados
echo [1/5] Eliminando documentacion duplicada...
if exist "Guia_Instalacion_Detallada.docx" move "Guia_Instalacion_Detallada.docx" "%BACKUP_DIR%\" >nul 2>&1
if exist "Guia_Instalacion_Detallada.pdf" move "Guia_Instalacion_Detallada.pdf" "%BACKUP_DIR%\" >nul 2>&1
if exist "Manual_de_Usuario.docx" move "Manual_de_Usuario.docx" "%BACKUP_DIR%\" >nul 2>&1
if exist "Manual_de_Usuario.pdf" move "Manual_de_Usuario.pdf" "%BACKUP_DIR%\" >nul 2>&1
if exist "custom-reference.docx" move "custom-reference.docx" "%BACKUP_DIR%\" >nul 2>&1
if exist "reference.docx" move "reference.docx" "%BACKUP_DIR%\" >nul 2>&1

REM 2. Carpeta temporal
echo [2/5] Eliminando carpetas temporales...
if exist "media-203f20de19922b04" move "media-203f20de19922b04" "%BACKUP_DIR%\" >nul 2>&1

REM 3. Scripts de integración
echo [3/5] Eliminando scripts de integracion aplicados...
if exist "CAMBIOS_MANUALES_VUELOS.txt" move "CAMBIOS_MANUALES_VUELOS.txt" "%BACKUP_DIR%\" >nul 2>&1
if exist "INSTRUCCIONES_INTEGRACION_CONFIRMACIONES.md" move "INSTRUCCIONES_INTEGRACION_CONFIRMACIONES.md" "%BACKUP_DIR%\" >nul 2>&1
if exist "aplicar_cambios_vuelos.py" move "aplicar_cambios_vuelos.py" "%BACKUP_DIR%\" >nul 2>&1
if exist "aplicar_cambios_vuelos.sh" move "aplicar_cambios_vuelos.sh" "%BACKUP_DIR%\" >nul 2>&1

REM 4. Scripts de mejoras
echo [4/5] Eliminando scripts de mejoras aplicadas...
if exist "agregar_transiciones_suaves.py" move "agregar_transiciones_suaves.py" "%BACKUP_DIR%\" >nul 2>&1

REM 5. Cache de Python
echo [5/5] Eliminando archivos de cache...
for /d /r %%d in (__pycache__) do @if exist "%%d" rd /s /q "%%d" 2>nul
del /s /q *.pyc 2>nul
del /s /q *.pyo 2>nul
del /s /q *.pyd 2>nul

REM Backups antiguos
for /r templates %%f in (*.backup*) do del "%%f" 2>nul
for /r templates %%f in (*.bak) do del "%%f" 2>nul

echo.
echo ====================================
echo    Limpieza completada!
echo ====================================
echo.
echo Archivos respaldados en: %BACKUP_DIR%
echo.
echo Si todo funciona bien, puedes eliminar:
echo   rd /s /q "%BACKUP_DIR%"
echo.
pause
