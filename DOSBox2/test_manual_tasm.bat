@echo off
echo ========================================
echo TEST MANUAL DE COMPILACION TASM
echo ========================================
cd Tasm
echo.
echo Archivos disponibles:
dir *.asm /b
echo.
echo Verificando herramientas:
if exist TASM.EXE (
    echo ✅ TASM.EXE encontrado
) else (
    echo ❌ TASM.EXE NO encontrado
    goto end
)

if exist TLINK.EXE (
    echo ✅ TLINK.EXE encontrado
) else (
    echo ❌ TLINK.EXE NO encontrado
    goto end
)

echo.
echo Compilando proteus_test_1752537570.asm...
echo.
echo [1] Ejecutando TASM...
TASM proteus_test_1752537570.asm
echo TASM terminó con código: %errorlevel%

if exist proteus_test_1752537570.obj (
    echo ✅ Archivo OBJ generado
    echo [2] Ejecutando TLINK...
    TLINK proteus_test_1752537570.obj
    echo TLINK terminó con código: %errorlevel%
    
    if exist proteus_test_1752537570.exe (
        echo ✅ Archivo EXE generado exitosamente!
        dir proteus_test_1752537570.exe
    ) else (
        echo ❌ Archivo EXE NO generado
    )
) else (
    echo ❌ Archivo OBJ NO generado por TASM
)

:end
echo.
echo Presiona cualquier tecla para continuar...
pause
