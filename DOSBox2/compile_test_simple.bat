@echo off
echo Compilando test_proteus_simple.asm con DOSBox+TASM...
cd /d "%~dp0"

rem Crear archivo de configuración temporal para DOSBox
echo mount c Tasm > temp_dosbox.conf
echo c: >> temp_dosbox.conf
echo tasm test_proteus_simple.asm >> temp_dosbox.conf
echo tlink test_proteus_simple.obj >> temp_dosbox.conf
echo exit >> temp_dosbox.conf

rem Ejecutar DOSBox con los comandos
dosbox.exe -conf temp_dosbox.conf -noconsole

rem Limpiar archivo temporal
del temp_dosbox.conf

echo.
echo Compilacion completada. Busca test_proteus_simple.exe en la carpeta Tasm
pause
