@echo off
echo =========================================
echo ANALIZADOR LEXICO - BRAZO ROBOTICO
echo Windows Edition - Sistema Robusto
echo =========================================
echo.
echo Iniciando aplicacion...
echo.

python main.py

if errorlevel 1 (
    echo.
    echo ERROR: La aplicacion no se pudo iniciar
    echo Verificando sistema...
    echo.
    python test_suite_complete.py
    echo.
    echo Presiona cualquier tecla para salir...
    pause >nul
) else (
    echo.
    echo Aplicacion cerrada correctamente
)
