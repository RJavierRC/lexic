@echo off
echo === COMPILACION PARA PROTEUS ===
cd "C:\Users\marco\Desktop\lexic\DOSBox2\Tasm"

echo Compilando robot_proteus1.asm con TASM...
TASM.EXE robot_proteus1.asm /zi /l
if errorlevel 1 goto error

echo Enlazando robot_proteus1.obj con TLINK...
TLINK.EXE robot_proteus1.obj
if errorlevel 1 goto error

if exist robot_proteus1.exe (
    echo Ejecutable robot_proteus1.exe generado para Proteus
    dir robot_proteus1.exe
    echo === COMPILACION EXITOSA ===
    exit /b 0
) else (
    echo Ejecutable no generado
    goto error
)

:error
echo Error en compilacion
exit /b 1
