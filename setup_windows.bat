REM =====================================================
REM CONFIGURACION AUTOMATICA PARA WINDOWS
REM Analizador Lexico - Windows Edition v5.0
REM =====================================================

@echo off
echo Configurando Analizador Lexico para Windows...
echo.

REM Verificar Python
echo [1/4] Verificando Python...
python --version >nul 2>&1
if errorlevel 1 (
    echo Python no encontrado
    echo Descarga Python desde: https://python.org
    pause
    exit /b 1
) else (
    echo Python encontrado
)

REM Verificar archivos del proyecto  
echo [2/4] Verificando archivos del proyecto...
if not exist "main.py" (
    echo main.py no encontrado
    exit /b 1
)
if not exist "robot_lexical_analyzer.py" (
    echo robot_lexical_analyzer.py no encontrado
    exit /b 1
)
echo Archivos del proyecto verificados

REM Verificar DOSBox
echo [3/4] Verificando DOSBox y TASM...
if not exist "DOSBox2\dosbox.exe" (
    echo DOSBox no encontrado en DOSBox2\dosbox.exe
    exit /b 1
)
if not exist "DOSBox2\Tasm\TASM.EXE" (
    echo TASM no encontrado en DOSBox2\Tasm\TASM.EXE
    exit /b 1
)
if not exist "DOSBox2\configuracion.conf" (
    echo Archivo de configuracion no encontrado
    exit /b 1
)
echo Herramientas de compilación verificadas

REM Test rápido
echo [4/4] Ejecutando test de configuración...
python test_windows_setup.py
if errorlevel 1 (
    echo Test falló
    pause
    exit /b 1
)

echo.
echo ===============================================
echo CONFIGURACION COMPLETADA EXITOSAMENTE
echo ===============================================
echo.
echo Para ejecutar el analizador:
echo   start_windows.bat
echo.
echo O directamente:
echo   python main.py
echo.
pause
