@echo off
echo Compilacion robusta iniciada...
cd Tasm

if not exist "robot_program3.asm" (
    echo ERROR: Archivo ASM no encontrado
    exit /b 1
)

echo Ejecutando TASM...
TASM robot_program3.asm
if errorlevel 1 (
    echo ERROR: TASM fall
    exit /b 1
)

if not exist "robot_program3.obj" (
    echo ERROR: Archivo OBJ no generado
    exit /b 1
)

echo Ejecutando TLINK...
TLINK robot_program3.obj
if errorlevel 1 (
    echo ERROR: TLINK fall
    exit /b 1
)

if exist "robot_program3.exe" (
    echo SUCCESS: Ejecutable generado
    exit /b 0
) else (
    echo ERROR: Ejecutable no generado
    exit /b 1
)
