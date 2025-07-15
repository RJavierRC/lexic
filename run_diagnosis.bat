@echo off
REM Script de diagnóstico manual para DOSBox + TASM
echo ================================================
echo DIAGNOSTICO MANUAL DOSBOX + TASM
echo ================================================

echo.
echo 1. Verificando ubicación actual:
cd
echo.

echo 2. Verificando estructura de carpetas:
if exist DOSBox2 (
    echo    OK: Carpeta DOSBox2 existe
) else (
    echo    ERROR: Carpeta DOSBox2 no existe
    goto error
)

if exist DOSBox2\dosbox.exe (
    echo    OK: dosbox.exe encontrado
) else (
    echo    ERROR: dosbox.exe no encontrado
    goto error
)

if exist DOSBox2\configuracion.conf (
    echo    OK: configuracion.conf encontrado
) else (
    echo    ERROR: configuracion.conf no encontrado
    goto error
)

if exist DOSBox2\Tasm (
    echo    OK: Carpeta Tasm existe
) else (
    echo    ERROR: Carpeta Tasm no existe
    goto error
)

if exist DOSBox2\Tasm\TASM.EXE (
    echo    OK: TASM.EXE encontrado
) else (
    echo    ERROR: TASM.EXE no encontrado
    goto error
)

if exist DOSBox2\Tasm\TLINK.EXE (
    echo    OK: TLINK.EXE encontrado
) else (
    echo    ERROR: TLINK.EXE no encontrado
    goto error
)

echo.
echo 3. Ejecutando diagnóstico Python:
python diagnose_compilation.py

echo.
echo 4. Ejecutando test manual de compilación:
python test_manual_compilation.py

echo.
echo ================================================
echo DIAGNOSTICO COMPLETADO
echo ================================================
goto end

:error
echo.
echo ================================================
echo ERROR EN DIAGNOSTICO
echo ================================================
echo Verifica que todos los archivos estén presentes

:end
pause
