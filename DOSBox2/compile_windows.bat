@echo off
echo ================================================
echo ANALIZADOR LEXICO - COMPILACION AUTOMATICA
echo ================================================
echo Programa: PROTEUS_TEST_1752537570.EXE
echo ================================================
cd Tasm
echo [1/4] Verificando archivos...
if not exist "TASM.EXE" (
    echo  TASM.EXE no encontrado
    goto error
)
if not exist "TLINK.EXE" (
    echo  TLINK.EXE no encontrado  
    goto error
)
if not exist "proteus_test_1752537570.asm" (
    echo  proteus_test_1752537570.asm no encontrado
    goto error
)
echo  Archivos verificados

echo [2/4] Ejecutando TASM...
TASM proteus_test_1752537570.asm
if errorlevel 1 (
    echo  Error en TASM
    goto error
)
echo  TASM completado

echo [3/4] Ejecutando TLINK...
TLINK /t proteus_test_1752537570.obj
if errorlevel 1 (
    echo  Error en TLINK modo /t, intentando modo estndar...
    TLINK proteus_test_1752537570.obj,proteus_test_1752537570.exe,,
    if errorlevel 1 (
        echo  Error en TLINK modo estndar
        goto error
    )
)
echo  TLINK completado

echo [4/4] Verificando resultado...
if exist "proteus_test_1752537570.exe" (
    echo  proteus_test_1752537570.exe creado exitosamente
    dir proteus_test_1752537570.exe
    goto success
) else (
    echo  proteus_test_1752537570.exe no se gener
    goto error
)

:success
echo ================================================
echo          COMPILACION EXITOSA
echo ================================================
echo  Ejecutable listo para Proteus
echo  Ubicacin: %cd%\proteus_test_1752537570.exe
goto end

:error
echo ================================================
echo         ERROR DE COMPILACION  
echo ================================================
echo  Diagnstico:
if exist "proteus_test_1752537570.asm" echo  Archivo ASM:  OK
if not exist "proteus_test_1752537570.asm" echo  Archivo ASM:  FALTA
if exist "proteus_test_1752537570.obj" echo  Archivo OBJ:  OK  
if not exist "proteus_test_1752537570.obj" echo  Archivo OBJ:  FALTA
if exist "proteus_test_1752537570.exe" echo  Archivo EXE:  OK
if not exist "proteus_test_1752537570.exe" echo  Archivo EXE:  FALTA
echo.
echo  Compile manualmente: TASM proteus_test_1752537570.asm ^&^& TLINK proteus_test_1752537570.obj

:end
