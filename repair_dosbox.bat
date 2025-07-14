@echo off
echo ================================================
echo REPARACION AUTOMATICA DOSBOX + TASM  
echo ================================================

echo 1. Verificando permisos...
icacls DOSBox2 /grant %USERNAME%:(OI)(CI)F >nul 2>&1
if errorlevel 1 (
    echo    ADVERTENCIA: No se pudieron otorgar permisos
    echo    Ejecuta este script como Administrador
) else (
    echo    OK: Permisos otorgados
)

echo.
echo 2. Respaldando configuración original...
if exist DOSBox2\configuracion.conf (
    copy DOSBox2\configuracion.conf DOSBox2\configuracion_backup.conf >nul
    echo    OK: Respaldo creado
) else (
    echo    ADVERTENCIA: configuracion.conf no encontrado
)

echo.
echo 3. Creando configuración mínima de emergencia...
(
echo [sdl]
echo fullscreen=false
echo output=surface
echo autolock=true
echo.
echo [dosbox]
echo machine=svga_s3
echo memsize=16
echo.
echo [render]
echo frameskip=0
echo aspect=false
echo scaler=normal2x
echo.
echo [cpu]
echo core=auto
echo cputype=auto
echo cycles=auto
echo.
echo [dos]
echo xms=true
echo ems=true
echo umb=true
echo.
echo [autoexec]
echo # Configuracion minima para compilacion
) > DOSBox2\configuracion_emergencia.conf
echo    OK: Configuración de emergencia creada

echo.
echo 4. Verificando archivos esenciales...
if exist DOSBox2\dosbox.exe (
    echo    OK: dosbox.exe encontrado
) else (
    echo    ERROR: dosbox.exe no encontrado
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
echo 5. Test básico de DOSBox...
echo    Ejecutando DOSBox con configuración mínima...
DOSBox2\dosbox.exe -conf DOSBox2\configuracion_emergencia.conf -c "mount c ." -c "c:" -c "dir DOSBox2" -c "exit" >nul 2>&1

if errorlevel 1 (
    echo    ERROR: DOSBox no se ejecuta correctamente
    echo.
    echo    POSIBLES SOLUCIONES:
    echo    1. Ejecutar como Administrador
    echo    2. Agregar exclusión de antivirus para DOSBox2
    echo    3. Instalar Visual C++ Redistributable
    echo    4. Verificar que Windows esté actualizado
    goto error
) else (
    echo    OK: DOSBox se ejecuta correctamente
)

echo.
echo 6. Test de compilación simple...
echo    Creando archivo de prueba...

REM Crear código ASM simple
(
echo .MODEL SMALL
echo .STACK 100h
echo .DATA
echo .CODE
echo MAIN PROC
echo     MOV AH, 4CH
echo     INT 21H
echo MAIN ENDP
echo END MAIN
) > DOSBox2\Tasm\test_repair.asm

REM Crear script de compilación
(
echo @echo off
echo cd Tasm
echo echo Compilando test_repair.asm...
echo TASM test_repair.asm
echo if errorlevel 1 goto error
echo echo Linking test_repair.obj...
echo TLINK test_repair.obj
echo if errorlevel 1 goto error
echo echo Test exitoso
echo goto end
echo :error
echo echo ERROR en compilacion
echo :end
) > DOSBox2\test_compile.bat

echo    Ejecutando test de compilación...
DOSBox2\dosbox.exe -conf DOSBox2\configuracion_emergencia.conf -c "mount c ." -c "c:" -c "test_compile.bat" -c "exit" >nul 2>&1

if exist DOSBox2\Tasm\test_repair.exe (
    echo    OK: Test de compilación exitoso
    del DOSBox2\Tasm\test_repair.asm >nul 2>&1
    del DOSBox2\Tasm\test_repair.obj >nul 2>&1
    del DOSBox2\Tasm\test_repair.exe >nul 2>&1
    del DOSBox2\test_compile.bat >nul 2>&1
) else (
    echo    ERROR: Test de compilación falló
    echo    Los archivos .ASM se pueden crear pero no compilar
    goto error
)

echo.
echo 7. Aplicando configuración reparada...
copy DOSBox2\configuracion_emergencia.conf DOSBox2\configuracion.conf >nul
echo    OK: Configuración reparada aplicada

echo.
echo ================================================
echo          REPARACION EXITOSA
echo ================================================
echo.
echo El sistema DOSBox + TASM ha sido reparado.
echo Puedes ejecutar el analizador normalmente.
echo.
echo Archivos creados:
echo - DOSBox2\configuracion_backup.conf (respaldo original)
echo - DOSBox2\configuracion_emergencia.conf (configuración mínima)
echo - DOSBox2\configuracion.conf (configuración activa)
echo.
goto end

:error
echo.
echo ================================================
echo         ERROR EN REPARACION
echo ================================================
echo.
echo La reparación automática no pudo completarse.
echo.
echo PASOS MANUALES REQUERIDOS:
echo.
echo 1. PERMISOS:
echo    - Clic derecho en carpeta del proyecto
echo    - Propiedades ^> Seguridad ^> Editar
echo    - Dar control total a tu usuario
echo.
echo 2. ANTIVIRUS:
echo    - Abrir Windows Defender
echo    - Exclusiones ^> Agregar exclusión
echo    - Agregar carpeta: %CD%\DOSBox2
echo.
echo 3. ADMINISTRADOR:
echo    - Clic derecho en start_windows.bat
echo    - "Ejecutar como administrador"
echo.
echo 4. REINSTALAR DEPENDENCIAS:
echo    - Descargar Visual C++ Redistributable
echo    - Instalar versiones x86 y x64
echo.
goto end

:end
echo.
pause
