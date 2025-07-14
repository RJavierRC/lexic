#!/usr/bin/env python3
"""
Script de diagnóstico para problemas de compilación DOSBox + TASM
"""

import os
import subprocess
import sys

def diagnose_compilation_issue():
    """Diagnostica problemas de compilación"""
    print("DIAGNOSTICO DE COMPILACION DOSBOX + TASM")
    print("=" * 50)
    
    # 1. Verificar estructura de archivos
    print("\n1. VERIFICANDO ESTRUCTURA DE ARCHIVOS:")
    required_files = {
        "DOSBox2/dosbox.exe": "Ejecutable DOSBox",
        "DOSBox2/configuracion.conf": "Archivo de configuración",
        "DOSBox2/Tasm/TASM.EXE": "Ensamblador TASM",
        "DOSBox2/Tasm/TLINK.EXE": "Linker TLINK"
    }
    
    all_ok = True
    for file_path, description in required_files.items():
        if os.path.exists(file_path):
            size = os.path.getsize(file_path)
            print(f"   OK {file_path} ({size} bytes) - {description}")
        else:
            print(f"   FALTA {file_path} - {description}")
            all_ok = False
    
    if not all_ok:
        print("\nERROR: Archivos faltantes. Verifica la instalación de DOSBox2.")
        return False
    
    # 2. Verificar permisos de escritura
    print("\n2. VERIFICANDO PERMISOS:")
    test_file = "DOSBox2/Tasm/test_write.tmp"
    try:
        with open(test_file, 'w') as f:
            f.write("test")
        os.remove(test_file)
        print("   OK Permisos de escritura en Tasm/")
    except Exception as e:
        print(f"   ERROR Permisos de escritura: {e}")
        return False
    
    # 3. Test básico de DOSBox
    print("\n3. TEST BASICO DE DOSBOX:")
    try:
        # Crear script de prueba simple
        test_script = """@echo off
echo TEST DOSBOX FUNCIONANDO
cd Tasm
dir
echo FIN DEL TEST
"""
        script_path = "DOSBox2/test_dosbox.bat"
        with open(script_path, 'w') as f:
            f.write(test_script)
        
        # Ejecutar DOSBox con timeout corto
        cmd = [
            "DOSBox2/dosbox.exe",
            "-conf", "DOSBox2/configuracion.conf",
            "-c", "mount c .",
            "-c", "c:",
            "-c", "test_dosbox.bat",
            "-c", "exit"
        ]
        
        print(f"   Ejecutando: {' '.join(cmd)}")
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=15, cwd=".")
        
        print(f"   Return code: {result.returncode}")
        if result.stdout:
            print(f"   STDOUT: {result.stdout[:200]}...")
        if result.stderr:
            print(f"   STDERR: {result.stderr[:200]}...")
        
        # Limpiar archivo de prueba
        if os.path.exists(script_path):
            os.remove(script_path)
            
        if result.returncode == 0:
            print("   OK DOSBox se ejecuta correctamente")
        else:
            print(f"   ERROR DOSBox falló con código: {result.returncode}")
            return False
            
    except subprocess.TimeoutExpired:
        print("   ERROR DOSBox timeout (>15s)")
        return False
    except Exception as e:
        print(f"   ERROR ejecutando DOSBox: {e}")
        return False
    
    # 4. Test específico de TASM
    print("\n4. TEST DE TASM:")
    try:
        # Crear código ensamblador de prueba simple
        test_asm = """.MODEL SMALL
.STACK 100h
.DATA
.CODE
MAIN PROC
    MOV AH, 4CH
    INT 21H
MAIN ENDP
END MAIN
"""
        
        asm_file = "DOSBox2/Tasm/test.asm"
        with open(asm_file, 'w') as f:
            f.write(test_asm)
        
        # Script para compilar en DOSBox
        compile_script = """@echo off
echo COMPILANDO ARCHIVO DE PRUEBA
cd Tasm
echo Listando archivos:
dir test.*
echo Ejecutando TASM:
TASM test.asm
if errorlevel 1 goto error_tasm
echo TASM OK, ejecutando TLINK:
TLINK test.obj
if errorlevel 1 goto error_tlink
echo TLINK OK
dir test.*
echo COMPILACION EXITOSA
goto end
:error_tasm
echo ERROR EN TASM
goto end
:error_tlink
echo ERROR EN TLINK
goto end
:end
"""
        
        script_path = "DOSBox2/compile_test.bat"
        with open(script_path, 'w') as f:
            f.write(compile_script)
        
        # Ejecutar compilación de prueba
        cmd = [
            "DOSBox2/dosbox.exe",
            "-conf", "DOSBox2/configuracion.conf",
            "-c", "mount c .",
            "-c", "c:",
            "-c", "compile_test.bat",
            "-c", "exit"
        ]
        
        print(f"   Ejecutando compilación de prueba...")
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=20, cwd=".")
        
        print(f"   Return code: {result.returncode}")
        if result.stdout:
            print(f"   STDOUT: {result.stdout}")
        if result.stderr:
            print(f"   STDERR: {result.stderr}")
        
        # Verificar si se generó el ejecutable
        exe_file = "DOSBox2/Tasm/test.exe"
        if os.path.exists(exe_file):
            print("   OK test.exe generado exitosamente")
            os.remove(exe_file)  # Limpiar
        else:
            print("   ERROR test.exe no se generó")
        
        # Limpiar archivos de prueba
        for file in ["DOSBox2/Tasm/test.asm", "DOSBox2/Tasm/test.obj", "DOSBox2/compile_test.bat"]:
            if os.path.exists(file):
                os.remove(file)
                
    except Exception as e:
        print(f"   ERROR en test de TASM: {e}")
        return False
    
    print("\n" + "=" * 50)
    print("DIAGNOSTICO COMPLETADO")
    print("\nSi todos los tests son OK, el problema puede estar en:")
    print("1. El código ensamblador generado")
    print("2. Los nombres de archivos con caracteres especiales")
    print("3. Rutas muy largas")
    print("4. Antivirus bloqueando DOSBox")
    
    return True

def create_simple_test():
    """Crea un test simple para verificar la compilación"""
    print("\nCREANDO TEST SIMPLE...")
    
    # Código robot simple
    robot_code = """inicio
    base { girai 90 }
    espera 1000
fin"""
    
    try:
        from robot_lexical_analyzer import RobotLexicalAnalyzer
        analyzer = RobotLexicalAnalyzer()
        
        print("Analizando código robot...")
        tokens, errors = analyzer.analyze(robot_code)
        
        if errors:
            print(f"Errores en análisis: {errors}")
            return False
        
        print("Generando código ensamblador...")
        success, message = analyzer.generate_and_compile("test_simple")
        
        if success:
            print("TEST EXITOSO: Compilación funcionó correctamente")
        else:
            print(f"TEST FALLÓ: {message}")
            
        return success
        
    except Exception as e:
        print(f"Error en test simple: {e}")
        return False

if __name__ == "__main__":
    print("Iniciando diagnóstico completo...\n")
    
    success = diagnose_compilation_issue()
    
    if success:
        print("\nEjecutando test simple de compilación...")
        create_simple_test()
    
    input("\nPresiona Enter para continuar...")
