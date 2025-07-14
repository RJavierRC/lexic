@echo off
echo === TEST DIRECTO TASM ===
cd DOSBox2\Tasm
echo Archivos antes de compilar:
dir test_diagnostico.*
echo.
echo Ejecutando TASM...
TASM test_diagnostico.asm
echo Return code TASM: %errorlevel%
echo.
echo Archivos despues de TASM:
dir test_diagnostico.*
echo.
echo Ejecutando TLINK...
TLINK test_diagnostico.obj
echo Return code TLINK: %errorlevel%
echo.
echo Archivos finales:
dir test_diagnostico.*
echo.
if exist test_diagnostico.exe (
    echo EXITO: test_diagnostico.exe creado
) else (
    echo ERROR: exe no creado
)
pause
