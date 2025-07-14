#!/usr/bin/env python3
"""
Script de diagnóstico para identificar problemas de compilación
"""

import os
import subprocess
import sys
from robot_lexical_analyzer import RobotLexicalAnalyzer

def diagnosticar_sistema():
    """Diagnóstico completo del sistema de compilación"""
    print("=" * 60)
    print("DIAGNÓSTICO DE SISTEMA DE COMPILACIÓN")
    print("=" * 60)
    
    # 1. Verificar archivos críticos
    print("\n1. VERIFICANDO ARCHIVOS CRÍTICOS:")
    archivos_criticos = [
        "DOSBox2/dosbox.exe",
        "DOSBox2/Tasm/TASM.EXE", 
        "DOSBox2/Tasm/TLINK.EXE",
        "robot_lexical_analyzer.py",
        "assembly_generator.py"
    ]
    
    for archivo in archivos_criticos:
        existe = os.path.exists(archivo)
        print(f"   {archivo}: {'✓ OK' if existe else '❌ FALTA'}")
        if existe:
            size = os.path.getsize(archivo)
            print(f"     Tamaño: {size} bytes")
    
    # 2. Test de código robot simple
    print("\n2. PROBANDO CÓDIGO ROBOT SIMPLE:")
    codigo_test = """Robot r1
r1.velocidad = 2
r1.base = 45
r1.hombro = 120
r1.codo = 90
r1.espera = 1"""
    
    print(f"   Código de prueba:\n{codigo_test}")
    
    try:
        analyzer = RobotLexicalAnalyzer()
        tokens, errors = analyzer.analyze(codigo_test)
        print(f"   Análisis: {'✓ OK' if not errors else '❌ ERRORES'}")
        print(f"   Tokens: {len(tokens)}")
        if errors:
            print(f"   Errores: {errors[:3]}")
    except Exception as e:
        print(f"   ❌ Error en análisis: {e}")
        return False
    
    # 3. Test de generación de ensamblador
    print("\n3. PROBANDO GENERACIÓN DE ENSAMBLADOR:")
    try:
        asm_code, error = analyzer.generate_assembly_code("test_diagnostico")
        if error:
            print(f"   ❌ Error generando ASM: {error}")
            return False
        else:
            print("   ✓ Código ensamblador generado exitosamente")
            print(f"   Tamaño: {len(asm_code)} caracteres")
            # Guardar para inspección
            with open("DOSBox2/Tasm/test_diagnostico.asm", 'w') as f:
                f.write(asm_code)
            print("   ✓ Archivo test_diagnostico.asm guardado")
    except Exception as e:
        print(f"   ❌ Error generando ASM: {e}")
        return False
    
    # 4. Test de DOSBox directo
    print("\n4. PROBANDO DOSBOX DIRECTAMENTE:")
    try:
        cmd = ["DOSBox2/dosbox.exe", "-version"]
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
        print(f"   Return code: {result.returncode}")
        if result.stdout:
            print(f"   Salida: {result.stdout[:100]}...")
        if result.stderr:
            print(f"   Error: {result.stderr[:100]}...")
    except subprocess.TimeoutExpired:
        print("   ❌ DOSBox no responde (timeout)")
        return False
    except Exception as e:
        print(f"   ❌ Error ejecutando DOSBox: {e}")
        return False
    
    # 5. Test de compilación manual
    print("\n5. PROBANDO COMPILACIÓN MANUAL:")
    try:
        # Crear script simple
        script_content = """@echo off
echo === INICIO TEST COMPILACION ===
cd Tasm
echo Directorio actual:
cd
echo.
echo Archivos disponibles:
dir test_diagnostico.*
echo.
echo === EJECUTANDO TASM ===
TASM test_diagnostico.asm
echo TASM return code: %errorlevel%
echo.
echo === EJECUTANDO TLINK ===
TLINK test_diagnostico.obj
echo TLINK return code: %errorlevel%
echo.
echo === RESULTADO FINAL ===
if exist test_diagnostico.exe (
    echo ✓ EXITO: test_diagnostico.exe creado
) else (
    echo ❌ ERROR: exe no creado
)
echo === FIN TEST ===
"""
        
        with open("DOSBox2/test_manual.bat", 'w') as f:
            f.write(script_content)
        
        # Ejecutar con DOSBox
        cmd = [
            "DOSBox2/dosbox.exe",
            "-c", "mount c .",
            "-c", "c:",
            "-c", "test_manual.bat",
            "-c", "exit"
        ]
        
        print("   Ejecutando compilación manual...")
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=30, cwd=".")
        
        print(f"   Return code: {result.returncode}")
        
        # Verificar resultado
        exe_file = "DOSBox2/Tasm/test_diagnostico.exe"
        if os.path.exists(exe_file):
            size = os.path.getsize(exe_file)
            print(f"   ✓ ÉXITO: test_diagnostico.exe creado ({size} bytes)")
            return True
        else:
            print("   ❌ ERROR: exe no fue creado")
            print("   Salida DOSBox:")
            if result.stdout:
                print(f"   STDOUT: {result.stdout}")
            if result.stderr:
                print(f"   STDERR: {result.stderr}")
            return False
            
    except Exception as e:
        print(f"   ❌ Error en compilación manual: {e}")
        return False

def diagnosticar_analizador():
    """Diagnóstico específico del analizador"""
    print("\n" + "=" * 60)
    print("DIAGNÓSTICO DEL ANALIZADOR")
    print("=" * 60)
    
    try:
        from assembly_generator import DOSBoxController
        print("✓ Importación de DOSBoxController exitosa")
        
        controller = DOSBoxController()
        print(f"✓ DOSBoxController creado")
        print(f"   DOSBox path: {controller.dosbox_path}")
        print(f"   TASM path: {controller.tasm_path}")
        print(f"   DOSBox exe: {controller.dosbox_exe}")
        
        # Test con código simple
        simple_asm = """.MODEL SMALL
.STACK 100h
.DATA
.CODE
MAIN PROC
    MOV AH, 4CH
    INT 21H
MAIN ENDP
END MAIN"""
        
        print("\nProbando compilación con DOSBoxController...")
        success, message = controller.compile_assembly(simple_asm, "test_controller")
        print(f"Resultado: {success}")
        print(f"Mensaje: {message}")
        
        return success
        
    except Exception as e:
        print(f"❌ Error en DOSBoxController: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    print("Iniciando diagnóstico completo...")
    
    sistema_ok = diagnosticar_sistema()
    analizador_ok = diagnosticar_analizador()
    
    print("\n" + "=" * 60)
    print("RESUMEN DEL DIAGNÓSTICO")
    print("=" * 60)
    print(f"Sistema de archivos: {'✓ OK' if sistema_ok else '❌ ERROR'}")
    print(f"Analizador/Compilador: {'✓ OK' if analizador_ok else '❌ ERROR'}")
    
    if sistema_ok and analizador_ok:
        print("\n🎉 SISTEMA COMPLETAMENTE FUNCIONAL")
        print("El problema puede estar en la GUI o en la llamada específica")
    else:
        print("\n⚠️ PROBLEMAS DETECTADOS")
        print("Revisar los errores específicos arriba")
    
    input("\nPresiona Enter para continuar...")
