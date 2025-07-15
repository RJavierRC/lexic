@echo off
echo ================================================
echo      ANALIZADOR LEXICO ROBOTICO - WINDOWS
echo ================================================

REM Verificar si Python está instalado
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python no encontrado
    echo.
    echo Por favor instala Python 3.9+ desde:
    echo https://python.org/downloads/
    echo.
    echo Asegurate de marcar "Add to PATH" durante la instalacion
    pause
    exit /b 1
)

echo Python detectado correctamente

REM Verificar estructura del proyecto
if not exist main.py (
    echo ERROR: main.py no encontrado
    echo Ejecuta este script desde la carpeta del proyecto
    pause
    exit /b 1
)

if not exist DOSBox2\dosbox.exe (
    echo ERROR: DOSBox no encontrado en DOSBox2\
    echo.
    echo SOLUCION: Ejecutar repair_dosbox.bat primero
    echo.
    pause
    exit /b 1
)

if not exist DOSBox2\Tasm\TASM.EXE (
    echo ERROR: TASM no encontrado
    echo.
    echo SOLUCION: Verificar carpeta DOSBox2\Tasm\
    echo.
    pause
    exit /b 1
)

REM Verificar configuración
if not exist DOSBox2\configuracion.conf (
    echo ADVERTENCIA: configuracion.conf no encontrado
    echo Creando configuración básica...
    if exist repair_dosbox.bat call repair_dosbox.bat
)

echo Verificaciones completadas

REM Configurar entorno
set PYTHONPATH=%CD%
set DOSBOX_PATH=%CD%\DOSBox2

echo.
echo Iniciando Analizador Léxico Robótico...
echo.

REM Intentar iniciar con manejo de errores
python main.py

if errorlevel 1 (
    echo.
    echo ================================================
    echo            ERROR AL INICIAR
    echo ================================================
    echo.
    echo El programa se cerró con errores.
    echo.
    echo SOLUCIONES POSIBLES:
    echo.
    echo 1. PERMISOS:
    echo    - Ejecutar como Administrador
    echo    - Clic derecho en start_analyzer.bat
    echo    - "Ejecutar como administrador"
    echo.
    echo 2. ANTIVIRUS:
    echo    - Agregar exclusión para DOSBox2
    echo    - Windows Defender ^> Exclusiones
    echo    - Agregar carpeta: %CD%\DOSBox2
    echo.
    echo 3. REPARACION:
    echo    - Ejecutar: repair_dosbox.bat
    echo    - Luego reintentar
    echo.
    echo 4. DEPENDENCIAS:
    echo    - Instalar Visual C++ Redistributable
    echo    - Versiones x86 y x64
    echo.
    pause
    exit /b 1
)

echo.
echo Programa cerrado correctamente
pause
