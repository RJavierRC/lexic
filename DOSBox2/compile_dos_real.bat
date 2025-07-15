@echo off
echo === COMPILACION DOS REAL PARA 8086 ===
cd /d "C:\Users\marco\Desktop\lexic\DOSBox2\Tasm"

echo Compilando motor_movement.asm en modo DOS...
TASM.EXE /m2 motor_movement.asm
if errorlevel 1 goto error

echo Enlazando motor_movement.obj...
TLINK.EXE /t motor_movement.obj
if errorlevel 1 goto error

if exist motor_movement.com (
    echo Renombrando .com a .exe para Proteus
    copy motor_movement.com motor_movement.exe
    echo Ejecutable DOS REAL generado: motor_movement.exe
    dir motor_movement.exe
    exit /b 0
) else (
    echo Intentando enlace tradicional...
    TLINK.EXE motor_movement.obj
    if exist motor_movement.exe (
        echo Ejecutable DOS generado: motor_movement.exe
        dir motor_movement.exe
        exit /b 0
    ) else (
        goto error
    )
)

:error
echo Error en compilacion DOS REAL
exit /b 1
