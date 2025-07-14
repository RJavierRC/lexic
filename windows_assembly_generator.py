#!/usr/bin/env python3
"""
Generador de código ensamblador MEJORADO para Windows
Convierte cuádruplos a código ensamblador x86 para TASM con manejo robusto de errores
"""

import os
import subprocess
import tempfile
import glob
import platform
from datetime import datetime

class WindowsAssemblyGenerator:
    """Generador de ensamblador específicamente optimizado para Windows"""
    
    def __init__(self):
        # Variables de generación
        self.variables = {}
        self.labels = {}
        self.counters = {}
        self.temp_vars = {}
        self.code_lines = []
        self.data_lines = []
        
        # Verificación de plataforma
        self.is_windows = platform.system().lower() == 'windows'
        
        # Rutas del sistema
        self.base_path = os.path.dirname(os.path.abspath(__file__))
        self.dosbox_path = os.path.join(self.base_path, "DOSBox2")
        self.dosbox_exe = os.path.join(self.dosbox_path, "dosbox.exe")
        self.tasm_path = os.path.join(self.dosbox_path, "Tasm")
        self.config_file = os.path.join(self.dosbox_path, "configuracion.conf")
        
        # Puertos del robot
        self.ports = {
            'base': 'PORTA',
            'hombro': 'PORTB', 
            'codo': 'PORTC',
            'garra': 'PORTD',
            'muneca': 'PORTE',
            'velocidad': 'PORTF'
        }
        
        # Verificar sistema al inicializar
        self.system_status = self.verify_system()
        
    def verify_system(self):
        """Verificación completa del sistema"""
        print("Verificando sistema de compilación...")
        
        if not self.is_windows:
            return {
                'status': 'error',
                'message': 'Esta versión requiere Windows',
                'platform': platform.system()
            }
        
        # Verificar archivos críticos
        missing_files = []
        
        if not os.path.exists(self.dosbox_exe):
            missing_files.append("DOSBox (dosbox.exe)")
        
        if not os.path.exists(self.config_file):
            missing_files.append("Configuración (configuracion.conf)")
            
        tasm_exe = os.path.join(self.tasm_path, "TASM.EXE")
        if not os.path.exists(tasm_exe):
            missing_files.append("TASM (TASM.EXE)")
            
        tlink_exe = os.path.join(self.tasm_path, "TLINK.EXE")
        if not os.path.exists(tlink_exe):
            missing_files.append("TLINK (TLINK.EXE)")
        
        if missing_files:
            return {
                'status': 'error',
                'message': 'Archivos faltantes',
                'missing': missing_files
            }
        
        # Verificar permisos
        try:
            test_file = os.path.join(self.tasm_path, "test_permissions.tmp")
            with open(test_file, 'w') as f:
                f.write("test")
            os.remove(test_file)
        except (PermissionError, OSError):
            return {
                'status': 'warning',
                'message': 'Permisos insuficientes',
                'solution': 'Ejecutar como Administrador'
            }
        
        # Verificar DOSBox
        try:
            result = subprocess.run([self.dosbox_exe, "-version"], 
                                  capture_output=True, timeout=5, text=True)
            if result.returncode == 0:
                print("Sistema verificado correctamente")
                return {'status': 'ok', 'message': 'Sistema listo'}
            else:
                return {
                    'status': 'error',
                    'message': 'DOSBox no responde',
                    'solution': 'Verificar antivirus o ejecutar repair_dosbox.bat'
                }
        except subprocess.TimeoutExpired:
            return {
                'status': 'error',
                'message': 'DOSBox timeout',
                'solution': 'Verificar configuración'
            }
        except FileNotFoundError:
            return {
                'status': 'error',
                'message': 'DOSBox no encontrado',
                'solution': 'Verificar instalación'
            }
    
    def compile_to_exe(self, asm_code, output_name="robot_program"):
        """Compila código ensamblador a .exe con manejo robusto de errores"""
        
        # Verificar estado del sistema
        if self.system_status['status'] == 'error':
            return False, f"Error del sistema: {self.system_status['message']}"
        
        if self.system_status['status'] == 'warning':
            print(f"ADVERTENCIA: {self.system_status['message']}")
            print(f"SOLUCIÓN: {self.system_status.get('solution', 'Revisar configuración')}")
        
        try:
            # Crear archivo .asm
            asm_file = os.path.join(self.tasm_path, f"{output_name}.asm")
            with open(asm_file, 'w', encoding='utf-8') as f:
                f.write(asm_code)
            
            print(f"Archivo creado: {output_name}.asm")
            
            # Crear script de compilación mejorado
            compile_script = self.create_compile_script(output_name)
            script_file = os.path.join(self.dosbox_path, "compile_windows.bat")
            
            with open(script_file, 'w') as f:
                f.write(compile_script)
            
            # Ejecutar compilación con timeout y mejor manejo de errores
            cmd = [
                self.dosbox_exe, 
                "-conf", self.config_file,
                "-c", "mount c .", 
                "-c", "c:", 
                "-c", "compile_windows.bat", 
                "-c", "exit"
            ]
            
            print(f"Compilando {output_name}.exe...")
            print("Usando configuración personalizada...")
            
            result = subprocess.run(
                cmd, 
                cwd=self.dosbox_path, 
                capture_output=True, 
                text=True, 
                timeout=45  # Timeout más largo para compilaciones complejas
            )
            
            # Verificar resultado
            exe_file = os.path.join(self.tasm_path, f"{output_name}.exe")
            
            if os.path.exists(exe_file):
                print(f"Compilación exitosa: {output_name}.exe")
                return True, f"Ejecutable generado: {exe_file}"
            else:
                # Diagnosticar error específico
                error_details = self.diagnose_compilation_error(result, output_name)
                return False, error_details
                
        except subprocess.TimeoutExpired:
            return False, "Timeout en compilación. Posibles causas:\n- Antivirus bloqueando DOSBox\n- Configuración incorrecta\n- Sistema sobrecargado"
        
        except PermissionError:
            return False, "Error de permisos. Soluciones:\n1. Ejecutar como Administrador\n2. Agregar exclusión de antivirus\n3. Verificar permisos de carpeta"
        
        except Exception as e:
            return False, f"Error inesperado: {str(e)}\nEjecutar repair_dosbox.bat para reparar"
    
    def create_compile_script(self, output_name):
        """Crea script de compilación mejorado con mejor detección de errores"""
        return f"""@echo off
echo ================================================
echo COMPILACION DE {output_name.upper()}
echo ================================================

cd Tasm

echo Verificando archivos...
if not exist "{output_name}.asm" (
    echo ERROR: {output_name}.asm no encontrado
    goto error
)

if not exist "TASM.EXE" (
    echo ERROR: TASM.EXE no encontrado
    goto error
)

if not exist "TLINK.EXE" (
    echo ERROR: TLINK.EXE no encontrado
    goto error
)

echo Iniciando compilacion con TASM...
TASM {output_name}.asm
if errorlevel 1 (
    echo ERROR: Fallo en TASM
    echo Revisar sintaxis del codigo ensamblador
    goto error
)

echo Compilacion TASM exitosa
echo Iniciando enlazado con TLINK...
TLINK {output_name}.obj
if errorlevel 1 (
    echo ERROR: Fallo en TLINK
    echo Revisar referencias y simbolos
    goto error
)

echo Enlazado exitoso
if exist "{output_name}.exe" (
    echo ================================================
    echo COMPILACION COMPLETADA: {output_name}.exe
    echo ================================================
    goto success
) else (
    echo ERROR: No se genero el ejecutable
    goto error
)

:error
echo ================================================
echo ERROR EN COMPILACION
echo ================================================
goto end

:success
echo Compilacion exitosa
goto end

:end
"""
    
    def diagnose_compilation_error(self, result, output_name):
        """Diagnostica errores específicos de compilación"""
        error_details = f"Error en compilación de {output_name}:\n\n"
        
        # Verificar archivos intermedios
        obj_file = os.path.join(self.tasm_path, f"{output_name}.obj")
        map_file = os.path.join(self.tasm_path, f"{output_name}.map")
        
        if not os.path.exists(obj_file):
            error_details += "- TASM falló: Error en sintaxis del código ensamblador\n"
            error_details += "- Verificar estructura .MODEL, .STACK, .DATA, .CODE\n"
        elif not os.path.exists(map_file):
            error_details += "- TLINK falló: Error en enlazado\n"
            error_details += "- Verificar referencias de procedimientos\n"
        else:
            error_details += "- Archivos intermedios OK, pero no se generó .exe\n"
            error_details += "- Posible error de permisos o antivirus\n"
        
        # Agregar output de DOSBox si está disponible
        if result.stdout:
            error_details += f"\nSalida DOSBox:\n{result.stdout}\n"
        
        if result.stderr:
            error_details += f"\nErrores DOSBox:\n{result.stderr}\n"
        
        error_details += "\nSOLUCIONES RECOMENDADAS:\n"
        error_details += "1. Ejecutar repair_dosbox.bat\n"
        error_details += "2. Ejecutar como Administrador\n"
        error_details += "3. Agregar exclusión de antivirus para DOSBox2\n"
        error_details += "4. Verificar permisos de escritura\n"
        
        return error_details

# Mantener compatibilidad con el código existente
class AssemblyGenerator(WindowsAssemblyGenerator):
    """Alias para mantener compatibilidad"""
    pass
