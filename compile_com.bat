@echo off
cd DOSBox2\Tasm
echo Compilando motor_user.asm a formato .COM...
TASM.EXE motor_user.asm
if exist motor_user.obj (
    echo Enlazando a formato .COM...
    TLINK.EXE /t motor_user.obj
    if exist motor_user.com (
        echo motor_user.com generado exitosamente
        dir motor_user.com
    ) else (
        echo Error generando .COM
    )
    del motor_user.obj
) else (
    echo Error en ensamblado
)
pause
