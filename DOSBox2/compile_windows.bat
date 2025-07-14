@echo off
echo ================================================
echo ANALIZADOR LEXICO - COMPILACION WINDOWS
echo ================================================
echo Programa: ROBOT_PROGRAM.EXE
echo ================================================
cd Tasm
echo [1/3] Ejecutando TASM...
TASM robot_program.asm
if errorlevel 1 goto error
echo [2/3] Ejecutando TLINK...
TLINK robot_program.obj
if errorlevel 1 goto error
echo [3/3] Verificando resultado...
if exist "robot_program.exe" (
    echo OK robot_program.exe creado exitosamente
    goto success
) else (
    goto error
)

:success
echo ================================================
echo          COMPILACION EXITOSA
echo ================================================
goto end

:error
echo ================================================
echo         ERROR DE COMPILACION
echo ================================================
echo Error details:
echo - Verificar que TASM.EXE y TLINK.EXE esten disponibles
echo - Verificar sintaxis del codigo ensamblador
echo - Verificar permisos de escritura

:end
