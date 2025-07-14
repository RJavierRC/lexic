@echo off
echo === TEST DOSBOX + TASM ===
echo Ejecutando DOSBox con TASM...
DOSBox2\dosbox.exe -c "mount c ." -c "c:" -c "cd Tasm" -c "TASM test_diagnostico.asm" -c "TLINK test_diagnostico.obj" -c "dir test_diagnostico.*" -c "exit"
echo.
echo Verificando resultado...
if exist "DOSBox2\Tasm\test_diagnostico.exe" (
    echo EXITO: test_diagnostico.exe creado via DOSBox
    dir "DOSBox2\Tasm\test_diagnostico.exe"
) else (
    echo ERROR: exe no creado
)
pause
