@echo off
REM ===============================================
REM ANALIZADOR LEXICO - WINDOWS EDITION
REM ===============================================
echo.
echo  ██████  ██████   ██████  ██████   ██████  ████████ 
echo  ██   ██ ██    ██ ██   ██ ██    ██    ██       ██    
echo  ██████  ██    ██ ██████  ██    ██    ██       ██    
echo  ██   ██ ██    ██ ██   ██ ██    ██    ██       ██    
echo  ██   ██  ██████  ██████   ██████     ██       ██    
echo.
echo  ANALIZADOR LEXICO PARA BRAZO ROBOTICO
echo  Windows Edition v5.0
echo ===============================================

REM Verificar Python
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python no esta instalado
    echo.
    echo Instala Python desde: https://python.org
    pause
    exit /b 1
)

REM Verificar archivos del proyecto
if not exist "main.py" (
    echo ERROR: main.py no encontrado
    echo Asegurate de estar en la carpeta correcta del proyecto
    pause
    exit /b 1
)

if not exist "DOSBox2\dosbox.exe" (
    echo ERROR: DOSBox no encontrado
    echo Verifica que la carpeta DOSBox2 este completa
    pause
    exit /b 1
)

if not exist "DOSBox2\configuracion.conf" (
    echo ERROR: Archivo de configuracion no encontrado
    echo Verifica que configuracion.conf este en DOSBox2
    pause
    exit /b 1
)

REM Ejecutar la aplicación
echo Iniciando Analizador Lexico Windows...
echo.
python main.py

REM Mostrar resultado
if errorlevel 1 (
    echo.
    echo La aplicación terminó con errores
) else (
    echo.
    echo Aplicación cerrada exitosamente
)

echo.
echo Presiona cualquier tecla para cerrar...
pause >nul
