#!/usr/bin/env python3
"""
Script de verificación completa del sistema Windows
Ejecuta todas las verificaciones necesarias para asegurar funcionamiento
"""

import os
import sys
import platform
import subprocess
import time
from datetime import datetime

def print_header(title):
    """Imprime encabezado decorado"""
    print("\n" + "="*60)
    print(f"  {title}")
    print("="*60)

def print_status(item, status, details=""):
    """Imprime estado con formato"""
    symbols = {"OK": "✓", "ERROR": "✗", "WARNING": "⚠"}
    colors = {"OK": "", "ERROR": "", "WARNING": ""}  # Sin colores para Windows
    
    symbol = symbols.get(status, "?")
    print(f"  {symbol} {item}: {status}")
    if details:
        print(f"    {details}")

def check_platform():
    """Verifica plataforma"""
    print_header("VERIFICACIÓN DE PLATAFORMA")
    
    system = platform.system()
    version = platform.version()
    architecture = platform.architecture()[0]
    
    print(f"  Sistema: {system} {version}")
    print(f"  Arquitectura: {architecture}")
    
    if system.lower() == "windows":
        print_status("Plataforma", "OK", "Windows detectado correctamente")
        return True
    else:
        print_status("Plataforma", "ERROR", f"Requiere Windows, detectado: {system}")
        return False

def check_python():
    """Verifica instalación de Python"""
    print_header("VERIFICACIÓN DE PYTHON")
    
    try:
        version = sys.version
        major, minor = sys.version_info[:2]
        
        print(f"  Versión: Python {major}.{minor}")
        print(f"  Ejecutable: {sys.executable}")
        
        if major >= 3 and minor >= 9:
            print_status("Python", "OK", f"Versión {major}.{minor} es compatible")
            return True
        else:
            print_status("Python", "ERROR", f"Requiere Python 3.9+, encontrado {major}.{minor}")
            return False
            
    except Exception as e:
        print_status("Python", "ERROR", f"Error verificando Python: {e}")
        return False

def check_files():
    """Verifica archivos del sistema"""
    print_header("VERIFICACIÓN DE ARCHIVOS")
    
    base_path = os.path.dirname(os.path.abspath(__file__))
    all_ok = True
    
    # Archivos principales
    main_files = [
        ("main.py", "Interfaz principal"),
        ("assembly_generator.py", "Generador de ensamblador"),
        ("robot_lexical_analyzer.py", "Analizador léxico"),
        ("start_analyzer.bat", "Script de inicio"),
        ("repair_dosbox.bat", "Script de reparación")
    ]
    
    for file, desc in main_files:
        path = os.path.join(base_path, file)
        if os.path.exists(path):
            print_status(desc, "OK", file)
        else:
            print_status(desc, "ERROR", f"{file} no encontrado")
            all_ok = False
    
    # DOSBox y herramientas
    dosbox_path = os.path.join(base_path, "DOSBox2")
    dosbox_files = [
        ("dosbox.exe", "DOSBox ejecutable"),
        ("configuracion.conf", "Configuración DOSBox"),
        (os.path.join("Tasm", "TASM.EXE"), "Compilador TASM"),
        (os.path.join("Tasm", "TLINK.EXE"), "Enlazador TLINK")
    ]
    
    print("\n  DOSBox y herramientas:")
    for file, desc in dosbox_files:
        path = os.path.join(dosbox_path, file)
        if os.path.exists(path):
            print_status(desc, "OK", file)
        else:
            print_status(desc, "ERROR", f"{file} no encontrado")
            all_ok = False
    
    return all_ok

def check_permissions():
    """Verifica permisos de escritura"""
    print_header("VERIFICACIÓN DE PERMISOS")
    
    base_path = os.path.dirname(os.path.abspath(__file__))
    test_locations = [
        (base_path, "Directorio principal"),
        (os.path.join(base_path, "DOSBox2"), "Directorio DOSBox2"),
        (os.path.join(base_path, "DOSBox2", "Tasm"), "Directorio Tasm")
    ]
    
    all_ok = True
    
    for location, desc in test_locations:
        try:
            test_file = os.path.join(location, f"test_permisos_{int(time.time())}.tmp")
            with open(test_file, 'w') as f:
                f.write("test")
            os.remove(test_file)
            print_status(desc, "OK", "Escritura permitida")
        except (PermissionError, OSError) as e:
            print_status(desc, "ERROR", f"Sin permisos de escritura: {e}")
            all_ok = False
        except FileNotFoundError:
            print_status(desc, "WARNING", "Directorio no existe")
            all_ok = False
    
    return all_ok

def check_dosbox():
    """Verifica DOSBox"""
    print_header("VERIFICACIÓN DE DOSBOX")
    
    base_path = os.path.dirname(os.path.abspath(__file__))
    dosbox_exe = os.path.join(base_path, "DOSBox2", "dosbox.exe")
    
    if not os.path.exists(dosbox_exe):
        print_status("DOSBox", "ERROR", "dosbox.exe no encontrado")
        return False
    
    try:
        # Test básico de DOSBox
        print("  Probando DOSBox...")
        result = subprocess.run(
            [dosbox_exe, "-version"], 
            capture_output=True, 
            timeout=10, 
            text=True
        )
        
        if result.returncode == 0:
            print_status("DOSBox", "OK", "Se ejecuta correctamente")
            return True
        else:
            print_status("DOSBox", "ERROR", "No se ejecuta correctamente")
            print(f"    Salida: {result.stdout}")
            print(f"    Error: {result.stderr}")
            return False
            
    except subprocess.TimeoutExpired:
        print_status("DOSBox", "ERROR", "Timeout al ejecutar")
        return False
    except FileNotFoundError:
        print_status("DOSBox", "ERROR", "Archivo no encontrado")
        return False
    except Exception as e:
        print_status("DOSBox", "ERROR", f"Error inesperado: {e}")
        return False

def check_compilation():
    """Test de compilación simple"""
    print_header("TEST DE COMPILACIÓN")
    
    base_path = os.path.dirname(os.path.abspath(__file__))
    dosbox_path = os.path.join(base_path, "DOSBox2")
    tasm_path = os.path.join(dosbox_path, "Tasm")
    dosbox_exe = os.path.join(dosbox_path, "dosbox.exe")
    config_file = os.path.join(dosbox_path, "configuracion.conf")
    
    if not all(os.path.exists(p) for p in [dosbox_exe, config_file]):
        print_status("Test compilación", "ERROR", "Archivos faltantes")
        return False
    
    try:
        # Crear código ASM simple
        test_asm = """
.MODEL SMALL
.STACK 100h
.DATA
.CODE
MAIN PROC
    MOV AH, 4CH
    INT 21H
MAIN ENDP
END MAIN
"""
        asm_file = os.path.join(tasm_path, "test_verify.asm")
        with open(asm_file, 'w') as f:
            f.write(test_asm)
        
        # Crear script de compilación
        compile_script = """@echo off
cd Tasm
TASM test_verify.asm >nul 2>&1
if errorlevel 1 goto error
TLINK test_verify.obj >nul 2>&1
if errorlevel 1 goto error
echo SUCCESS
goto end
:error
echo ERROR
:end
"""
        script_file = os.path.join(dosbox_path, "test_verify.bat")
        with open(script_file, 'w') as f:
            f.write(compile_script)
        
        print("  Ejecutando test de compilación...")
        
        # Ejecutar DOSBox
        cmd = [
            dosbox_exe,
            "-conf", config_file,
            "-c", "mount c .",
            "-c", "c:",
            "-c", "test_verify.bat",
            "-c", "exit"
        ]
        
        result = subprocess.run(
            cmd,
            cwd=dosbox_path,
            capture_output=True,
            timeout=30,
            text=True
        )
        
        # Verificar resultado
        exe_file = os.path.join(tasm_path, "test_verify.exe")
        
        if os.path.exists(exe_file):
            print_status("Test compilación", "OK", "Compilación exitosa")
            
            # Limpiar archivos de test
            for ext in ['.asm', '.obj', '.exe', '.map']:
                try:
                    os.remove(os.path.join(tasm_path, f"test_verify{ext}"))
                except:
                    pass
            try:
                os.remove(script_file)
            except:
                pass
                
            return True
        else:
            print_status("Test compilación", "ERROR", "No se generó ejecutable")
            print(f"    Salida DOSBox: {result.stdout}")
            return False
            
    except Exception as e:
        print_status("Test compilación", "ERROR", f"Error en test: {e}")
        return False

def generate_report():
    """Genera reporte completo"""
    print_header("REPORTE DE VERIFICACIÓN")
    
    print(f"  Fecha: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"  Sistema: {platform.system()} {platform.version()}")
    print(f"  Python: {sys.version}")
    print(f"  Directorio: {os.path.dirname(os.path.abspath(__file__))}")
    
    # Ejecutar todas las verificaciones
    results = {}
    results['platform'] = check_platform()
    results['python'] = check_python()
    results['files'] = check_files()
    results['permissions'] = check_permissions()
    results['dosbox'] = check_dosbox()
    results['compilation'] = check_compilation()
    
    # Resumen
    print_header("RESUMEN")
    
    total_tests = len(results)
    passed_tests = sum(results.values())
    
    print(f"  Tests ejecutados: {total_tests}")
    print(f"  Tests exitosos: {passed_tests}")
    print(f"  Tests fallidos: {total_tests - passed_tests}")
    
    if passed_tests == total_tests:
        print("\n  🎉 SISTEMA COMPLETAMENTE FUNCIONAL")
        print("  El analizador debería funcionar correctamente")
    else:
        print("\n  ⚠️  SISTEMA CON PROBLEMAS")
        print("  Revisar errores arriba y ejecutar repair_dosbox.bat")
        print("  O seguir GUIA_ERRORES_WINDOWS.md")
    
    return passed_tests == total_tests

if __name__ == "__main__":
    print("VERIFICADOR DEL SISTEMA ANALIZADOR LÉXICO")
    print("Versión: Windows Optimizada")
    print(f"Ejecutándose en: {os.path.dirname(os.path.abspath(__file__))}")
    
    try:
        success = generate_report()
        sys.exit(0 if success else 1)
    except KeyboardInterrupt:
        print("\n\nVerificación cancelada por el usuario")
        sys.exit(1)
    except Exception as e:
        print(f"\nError inesperado: {e}")
        sys.exit(1)
