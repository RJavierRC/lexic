#!/usr/bin/env python3
"""
Test manual de compilación para detectar problemas específicos
"""

import os
import subprocess
import sys
from robot_lexical_analyzer import RobotLexicalAnalyzer

def test_manual_compilation():
    """Test manual paso a paso de la compilación"""
    print("TEST MANUAL DE COMPILACION")
    print("=" * 40)
    
    # 1. Verificar archivos necesarios
    print("\n1. VERIFICANDO ARCHIVOS:")
    required = [
        "DOSBox2/dosbox.exe",
        "DOSBox2/configuracion.conf", 
        "DOSBox2/Tasm/TASM.EXE",
        "DOSBox2/Tasm/TLINK.EXE"
    ]
    
    for file in required:
        exists = os.path.exists(file)
        print(f"   {file}: {'OK' if exists else 'FALTA'}")
        if not exists:
            print("ERROR: Archivo faltante, no se puede continuar")
            return False
    
    # 2. Crear código robot simple
    print("\n2. CREANDO CODIGO ROBOT SIMPLE:")
    robot_code = """inicio
    base { girai 45 }
    espera 500
fin"""
    print(f"   Código: {robot_code.strip()}")
    
    # 3. Analizar código
    print("\n3. ANALIZANDO CODIGO:")
    try:
        analyzer = RobotLexicalAnalyzer()
        tokens, errors = analyzer.analyze(robot_code)
        
        print(f"   Tokens: {len(tokens)}")
        print(f"   Errores: {len(errors)}")
        
        if errors:
            print(f"   Errores encontrados: {errors}")
            return False
        
        print("   Análisis exitoso")
        
    except Exception as e:
        print(f"   ERROR en análisis: {e}")
        return False
    
    # 4. Generar código ensamblador
    print("\n4. GENERANDO CODIGO ENSAMBLADOR:")
    try:
        asm_code, _ = analyzer.generate_assembly_code("test_manual")
        
        # Guardar para inspección
        asm_file = "DOSBox2/Tasm/test_manual.asm"
        with open(asm_file, 'w', encoding='utf-8') as f:
            f.write(asm_code)
        
        print(f"   Archivo ASM creado: {asm_file}")
        print(f"   Tamaño: {len(asm_code)} caracteres")
        print(f"   Primeras líneas:")
        for i, line in enumerate(asm_code.split('\n')[:5]):
            print(f"      {i+1}: {line}")
        
    except Exception as e:
        print(f"   ERROR generando ASM: {e}")
        return False
    
    # 5. Crear script de compilación simple
    print("\n5. CREANDO SCRIPT DE COMPILACION:")
    batch_script = """@echo off
echo === INICIANDO COMPILACION ===
cd Tasm
echo Ubicacion actual:
cd
echo.
echo Archivos antes de compilar:
dir test_manual.*
echo.
echo === EJECUTANDO TASM ===
TASM test_manual.asm
echo TASM return code: %errorlevel%
echo.
echo Archivos después de TASM:
dir test_manual.*
echo.
echo === EJECUTANDO TLINK ===
TLINK test_manual.obj
echo TLINK return code: %errorlevel%
echo.
echo Archivos finales:
dir test_manual.*
echo.
if exist test_manual.exe (
    echo === EXITO: EXE GENERADO ===
) else (
    echo === ERROR: EXE NO GENERADO ===
)
echo === FIN ===
"""
    
    batch_file = "DOSBox2/compile_manual.bat"
    with open(batch_file, 'w', encoding='utf-8') as f:
        f.write(batch_script)
    
    print(f"   Script creado: {batch_file}")
    
    # 6. Ejecutar DOSBox manualmente
    print("\n6. EJECUTANDO DOSBOX:")
    cmd = [
        "DOSBox2/dosbox.exe",
        "-conf", "DOSBox2/configuracion.conf",
        "-c", "mount c .",
        "-c", "c:",
        "-c", "compile_manual.bat",
        "-c", "exit"
    ]
    
    print(f"   Comando: {' '.join(cmd)}")
    
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=30, cwd=".")
        
        print(f"   Return code: {result.returncode}")
        print(f"   STDOUT:")
        if result.stdout:
            for line in result.stdout.split('\n'):
                if line.strip():
                    print(f"      {line}")
        
        print(f"   STDERR:")
        if result.stderr:
            for line in result.stderr.split('\n'):
                if line.strip():
                    print(f"      {line}")
        
    except subprocess.TimeoutExpired:
        print("   ERROR: Timeout después de 30 segundos")
        return False
    except Exception as e:
        print(f"   ERROR ejecutando DOSBox: {e}")
        return False
    
    # 7. Verificar resultado
    print("\n7. VERIFICANDO RESULTADO:")
    exe_file = "DOSBox2/Tasm/test_manual.exe"
    obj_file = "DOSBox2/Tasm/test_manual.obj"
    
    print(f"   test_manual.asm: {'OK' if os.path.exists(asm_file) else 'FALTA'}")
    print(f"   test_manual.obj: {'OK' if os.path.exists(obj_file) else 'FALTA'}")
    print(f"   test_manual.exe: {'OK' if os.path.exists(exe_file) else 'FALTA'}")
    
    if os.path.exists(exe_file):
        size = os.path.getsize(exe_file)
        print(f"   Tamaño EXE: {size} bytes")
        print("\nCOMPILACION EXITOSA!")
        return True
    else:
        print("\nCOMPILACION FALLO!")
        return False

def clean_test_files():
    """Limpia archivos de prueba"""
    files_to_clean = [
        "DOSBox2/Tasm/test_manual.asm",
        "DOSBox2/Tasm/test_manual.obj", 
        "DOSBox2/Tasm/test_manual.exe",
        "DOSBox2/compile_manual.bat"
    ]
    
    for file in files_to_clean:
        if os.path.exists(file):
            os.remove(file)
            print(f"Limpiado: {file}")

if __name__ == "__main__":
    try:
        success = test_manual_compilation()
        
        print(f"\nRESULTADO: {'EXITO' if success else 'FALLO'}")
        
        clean_input = input("\n¿Limpiar archivos de prueba? (s/n): ")
        if clean_input.lower() == 's':
            clean_test_files()
            
    except Exception as e:
        print(f"Error crítico: {e}")
        import traceback
        traceback.print_exc()
    
    input("\nPresiona Enter para salir...")
