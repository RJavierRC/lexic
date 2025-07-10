@echo off
REM Script de inicio para el Analizador Léxico Robótico (Windows)
REM Uso: start_analyzer.bat

echo === Analizador Léxico Robótico ===
echo Iniciando aplicación...

REM Verificar si estamos en el directorio correcto
if not exist "main.py" (
    echo Error: No se encontró main.py
    echo Ejecuta este script desde el directorio del proyecto
    pause
    exit /b 1
)

REM Verificar Python
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Error: Python no está instalado o no está en el PATH
    pause
    exit /b 1
)

REM Ejecutar la aplicación
echo Ejecutando main.py...
python main.py

echo Aplicación terminada.
pause
