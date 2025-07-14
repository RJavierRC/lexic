@echo off
REM Script de inicio para Windows
REM Analizador Léxico para Brazo Robótico

echo 🤖 Iniciando Analizador Léxico para Brazo Robótico en Windows...
echo 📁 Directorio: %CD%

REM Verificar que estemos en el directorio correcto
if not exist "main.py" (
    echo ❌ Error: No se encontró main.py
    echo    Asegúrate de estar en el directorio del proyecto
    pause
    exit /b 1
)

REM Verificar entorno virtual
if not exist ".venv" (
    echo ⚠️  No se encontró entorno virtual (.venv^)
    echo    Creando entorno virtual...
    python -m venv .venv
    echo ✅ Entorno virtual creado
)

REM Activar entorno virtual
echo 🔄 Activando entorno virtual...
call .venv\Scripts\activate.bat

REM Verificar Python
echo 🐍 Versión de Python:
python --version

REM Mostrar funcionalidades para Windows
echo.
echo 🪟 MODO WINDOWS DETECTADO:
echo    ✅ Análisis léxico, sintáctico y semántico completo
echo    ✅ Generación de código intermedio (cuádruplos^) 
echo    ✅ Generación de código ensamblador (.asm^)
echo    ✅ Compilación a ejecutable .EXE (nativo^)
echo    ✅ Todas las funcionalidades disponibles
echo    💡 Usa 'Generar .EXE' para compilar completamente
echo.

REM Verificar DOSBox
if exist "DOSBox2" (
    echo ✅ DOSBox encontrado - Compilación .EXE disponible
) else (
    echo ⚠️  DOSBox no encontrado - Solo generación ASM disponible
    echo    Para compilación completa, asegúrate que DOSBox2\ esté presente
)

REM Ejecutar aplicación
echo 🚀 Iniciando aplicación...
echo.

python main.py

echo.
echo 👋 Analizador cerrado. ¡Hasta luego!
pause
