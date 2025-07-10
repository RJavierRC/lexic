@echo off
cd Tasm
echo Compilando test_simple.asm...
TASM test_simple.asm
if errorlevel 1 goto error
echo Enlazando test_simple.obj...
TLINK test_simple.obj
if errorlevel 1 goto error
echo Compilación exitosa: test_simple.exe generado
goto end
:error
echo Error en la compilación
:end
pause
