#!/usr/bin/env python3
"""
Detector de problemas de plataforma y solucionador
"""

import os
import platform
import subprocess

def detect_platform_issue():
    """Detecta problemas específicos de plataforma"""
    print("DETECTOR DE PROBLEMAS DE PLATAFORMA")
    print("=" * 50)
    
    current_os = platform.system()
    print(f"Sistema operativo detectado: {current_os}")
    print(f"Arquitectura: {platform.architecture()[0]}")
    print(f"Versión: {platform.version()}")
    
    if current_os != "Windows":
        print("\n❌ PROBLEMA DETECTADO:")
        print(f"   Este proyecto está configurado para Windows")
        print(f"   Pero está ejecutándose en {current_os}")
        print(f"   El archivo DOSBox2/dosbox.exe es un ejecutable de Windows")
        print(f"   y no puede ejecutarse en {current_os}")
        
        print("\n🔧 SOLUCIONES POSIBLES:")
        
        if current_os == "Darwin":  # macOS
            print("\n   OPCION 1 - Instalar DOSBox nativo para macOS:")
            print("   1. Instalar Homebrew si no lo tienes:")
            print("      /bin/bash -c \"$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)\"")
            print("   2. Instalar DOSBox:")
            print("      brew install dosbox")
            print("   3. El analizador se adaptará automáticamente")
            
            print("\n   OPCION 2 - Usar Wine para ejecutar DOSBox de Windows:")
            print("   1. Instalar Wine:")
            print("      brew install wine")
            print("   2. El sistema usará Wine automáticamente")
            
            print("\n   OPCION 3 - Usar en Windows (Recomendado):")
            print("   1. Ejecutar este proyecto en una máquina Windows")
            print("   2. O usar una máquina virtual Windows")
            print("   3. O usar Windows Subsystem for Linux (WSL)")
            
        elif current_os == "Linux":
            print("\n   OPCION 1 - Instalar DOSBox nativo para Linux:")
            print("   Ubuntu/Debian:")
            print("      sudo apt update && sudo apt install dosbox")
            print("   CentOS/RHEL:")
            print("      sudo yum install dosbox")
            print("   Arch:")
            print("      sudo pacman -S dosbox")
            
            print("\n   OPCION 2 - Usar Wine para ejecutar DOSBox de Windows:")
            print("   Ubuntu/Debian:")
            print("      sudo apt install wine")
            print("   El sistema usará Wine automáticamente")
            
        print("\n📋 PRÓXIMOS PASOS:")
        print("   1. Elige una de las opciones anteriores")
        print("   2. Instala las herramientas necesarias")
        print("   3. Ejecuta el proyecto nuevamente")
        print("   4. O transfiere el proyecto a Windows para uso nativo")
        
        return False
    else:
        print("✅ Sistema Windows detectado - Configuración correcta")
        return True

def check_dosbox_availability():
    """Verifica si DOSBox está disponible en el sistema"""
    print("\nVERIFICANDO DISPONIBILIDAD DE DOSBOX:")
    
    # Verificar DOSBox nativo
    try:
        result = subprocess.run(['dosbox', '-version'], capture_output=True, text=True, timeout=10)
        if result.returncode == 0:
            print("✅ DOSBox nativo encontrado en el sistema")
            print(f"   Versión: {result.stdout.strip()}")
            return "native"
    except:
        print("❌ DOSBox nativo no encontrado")
    
    # Verificar Wine
    try:
        result = subprocess.run(['wine', '--version'], capture_output=True, text=True, timeout=10)
        if result.returncode == 0:
            print("✅ Wine encontrado en el sistema")
            print(f"   Versión: {result.stdout.strip()}")
            return "wine"
    except:
        print("❌ Wine no encontrado")
    
    return None

def create_platform_specific_solution():
    """Crea una solución específica para la plataforma actual"""
    current_os = platform.system()
    
    if current_os == "Windows":
        print("Sistema Windows - No se requieren cambios")
        return
    
    dosbox_method = check_dosbox_availability()
    
    if dosbox_method == "native":
        print("\n🔧 CREANDO ADAPTADOR PARA DOSBOX NATIVO...")
        create_native_dosbox_adapter()
    elif dosbox_method == "wine":
        print("\n🔧 CREANDO ADAPTADOR PARA WINE...")
        create_wine_adapter()
    else:
        print("\n❌ No se encontró método para ejecutar DOSBox")
        print("   Instala DOSBox nativo o Wine según las instrucciones anteriores")

def create_native_dosbox_adapter():
    """Crea un adaptador para usar DOSBox nativo"""
    adapter_code = '''#!/usr/bin/env python3
"""
Adaptador para DOSBox nativo en sistemas Unix
"""
import os
import subprocess
from assembly_generator import DOSBoxController

class NativeDOSBoxController(DOSBoxController):
    """Controlador para DOSBox nativo en Unix"""
    
    def __init__(self, dosbox_path=None):
        # Para DOSBox nativo, no necesitamos la ruta específica
        super().__init__(dosbox_path)
        self.dosbox_exe = "dosbox"  # Usar DOSBox del sistema
    
    def compile_assembly(self, asm_code, output_name="robot_program"):
        """Compila usando DOSBox nativo"""
        try:
            # Crear archivo .asm
            asm_file = os.path.join(self.tasm_path, f"{output_name}.asm")
            with open(asm_file, 'w', encoding='utf-8') as f:
                f.write(asm_code)
            
            # Configurar DOSBox para compilación
            config_content = f"""
[autoexec]
mount c {os.getcwd()}
c:
cd Tasm
TASM {output_name}.asm
TLINK {output_name}.obj
exit
"""
            
            config_file = f"/tmp/dosbox_{output_name}.conf"
            with open(config_file, 'w') as f:
                f.write(config_content)
            
            # Ejecutar DOSBox nativo
            cmd = [self.dosbox_exe, "-conf", config_file]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
            
            # Verificar resultado
            exe_file = os.path.join(self.tasm_path, f"{output_name}.exe")
            if os.path.exists(exe_file):
                return True, f"Ejecutable {output_name}.exe generado exitosamente"
            else:
                return False, f"Error en compilación: {result.stderr}"
                
        except Exception as e:
            return False, f"Error: {str(e)}"
'''
    
    with open("native_dosbox_adapter.py", 'w') as f:
        f.write(adapter_code)
    
    print("✅ Adaptador para DOSBox nativo creado: native_dosbox_adapter.py")

def create_wine_adapter():
    """Crea un adaptador para usar Wine"""
    adapter_code = '''#!/usr/bin/env python3
"""
Adaptador para DOSBox con Wine
"""
import os
import subprocess
from assembly_generator import DOSBoxController

class WineDOSBoxController(DOSBoxController):
    """Controlador para DOSBox usando Wine"""
    
    def compile_assembly(self, asm_code, output_name="robot_program"):
        """Compila usando DOSBox con Wine"""
        try:
            # Crear archivo .asm
            asm_file = os.path.join(self.tasm_path, f"{output_name}.asm")
            with open(asm_file, 'w', encoding='utf-8') as f:
                f.write(asm_code)
            
            # Script de compilación
            batch_script = f"""@echo off
cd Tasm
TASM {output_name}.asm
TLINK {output_name}.obj
"""
            
            batch_file = os.path.join(self.dosbox_path, "compile_wine.bat")
            with open(batch_file, 'w') as f:
                f.write(batch_script)
            
            # Ejecutar DOSBox con Wine
            cmd = [
                "wine", self.dosbox_exe,
                "-conf", self.config_file,
                "-c", "mount c .",
                "-c", "c:",
                "-c", "compile_wine.bat",
                "-c", "exit"
            ]
            
            result = subprocess.run(cmd, cwd=self.dosbox_path, capture_output=True, text=True, timeout=30)
            
            # Verificar resultado
            exe_file = os.path.join(self.tasm_path, f"{output_name}.exe")
            if os.path.exists(exe_file):
                return True, f"Ejecutable {output_name}.exe generado exitosamente"
            else:
                return False, f"Error en compilación: {result.stderr}"
                
        except Exception as e:
            return False, f"Error: {str(e)}"
'''
    
    with open("wine_dosbox_adapter.py", 'w') as f:
        f.write(adapter_code)
    
    print("✅ Adaptador para Wine creado: wine_dosbox_adapter.py")

if __name__ == "__main__":
    print("Ejecutando detector de problemas de plataforma...\n")
    
    is_windows = detect_platform_issue()
    
    if not is_windows:
        create_platform_specific_solution()
    
    print("\n" + "=" * 50)
    print("DETECCIÓN COMPLETADA")
    print("\nSi estás desarrollando en macOS/Linux pero el destino final")
    print("es Windows, considera usar la versión multiplataforma o")
    print("transferir el proyecto a Windows para pruebas finales.")
    
    input("\nPresiona Enter para continuar...")
