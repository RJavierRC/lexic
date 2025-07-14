#!/usr/bin/env python3
"""
Script de inicio universal para el Analizador Léxico
Detecta automáticamente el sistema operativo y configura el entorno apropiado
"""

import os
import sys
import platform
import subprocess

def print_banner():
    """Muestra el banner de inicio"""
    system_icons = {
        'Darwin': '🍎',
        'Linux': '🐧', 
        'Windows': '🪟'
    }
    
    system = platform.system()
    icon = system_icons.get(system, '💻')
    
    print("=" * 60)
    print("🤖 ANALIZADOR LÉXICO PARA BRAZO ROBÓTICO")
    print("   Versión 5.0 - Multiplataforma")
    print("=" * 60)
    print(f"{icon} Sistema detectado: {system}")
    print(f"📁 Directorio: {os.getcwd()}")
    print()

def check_files():
    """Verifica que los archivos necesarios existan"""
    required_files = ['main.py', 'robot_lexical_analyzer.py', 'robot_tokens.py']
    missing_files = []
    
    for file in required_files:
        if not os.path.exists(file):
            missing_files.append(file)
    
    if missing_files:
        print("❌ Error: Archivos faltantes:")
        for file in missing_files:
            print(f"   - {file}")
        print("\n   Asegúrate de estar en el directorio correcto del proyecto")
        return False
    
    print("✅ Todos los archivos necesarios encontrados")
    return True

def setup_venv():
    """Configura el entorno virtual"""
    if not os.path.exists('.venv'):
        print("⚠️  Entorno virtual no encontrado")
        print("🔄 Creando entorno virtual...")
        try:
            subprocess.run([sys.executable, '-m', 'venv', '.venv'], check=True)
            print("✅ Entorno virtual creado exitosamente")
        except subprocess.CalledProcessError:
            print("❌ Error creando entorno virtual")
            return False
    else:
        print("✅ Entorno virtual encontrado")
    
    return True

def get_python_executable():
    """Obtiene la ruta del ejecutable de Python del entorno virtual"""
    system = platform.system()
    
    if system == 'Windows':
        return os.path.join('.venv', 'Scripts', 'python.exe')
    else:
        return os.path.join('.venv', 'bin', 'python')

def show_system_capabilities():
    """Muestra las capacidades según el sistema operativo"""
    system = platform.system()
    
    print("🔧 FUNCIONALIDADES DISPONIBLES:")
    print("   ✅ Análisis léxico, sintáctico y semántico")
    print("   ✅ Generación de código intermedio (cuádruplos)")
    print("   ✅ Generación de código ensamblador (.asm)")
    print("   ✅ Interfaz gráfica intuitiva")
    print("   ✅ Validaciones avanzadas")
    
    if system == 'Darwin':  # macOS
        print("   ⚠️  Compilación .EXE no disponible")
        print("   💡 Usa el botón 'Ver ASM' para generar código")
        print()
        print("🍎 OPTIMIZACIONES PARA macOS:")
        print("   • Interfaz adaptada para macOS")
        print("   • Colores y temas optimizados")
        print("   • Funcionalidad completa de análisis")
        
    elif system == 'Windows':
        print("   ✅ Compilación .EXE disponible")
        print("   💡 Usa 'Generar .EXE' para compilar")
        print()
        print("🪟 FUNCIONALIDADES COMPLETAS EN WINDOWS:")
        print("   • Compilación nativa con DOSBox/TASM")
        print("   • Generación de archivos .exe ejecutables")
        print("   • Compatible con Proteus")
        
    elif system == 'Linux':
        print("   ✅ Compilación .EXE disponible (via DOSBox)")
        print("   💡 Usa 'Compilar' para generar ejecutables")
        print()
        print("🐧 FUNCIONALIDADES COMPLETAS EN LINUX:")
        print("   • Compilación con DOSBox/TASM")
        print("   • Generación de archivos .exe")
        print("   • Entorno de desarrollo robusto")
    
    # Verificar DOSBox
    if os.path.exists('DOSBox2'):
        print("   ✅ DOSBox encontrado - Compilación completa disponible")
    else:
        if system != 'Darwin':
            print("   ⚠️  DOSBox no encontrado - Solo generación ASM")
    
    print()

def run_application():
    """Ejecuta la aplicación principal"""
    python_exe = get_python_executable()
    
    if not os.path.exists(python_exe):
        print(f"❌ Error: Python no encontrado en {python_exe}")
        print("   Intenta recrear el entorno virtual")
        return False
    
    print("🚀 Iniciando aplicación...")
    print("   Presiona Ctrl+C para salir")
    print()
    
    try:
        # Configurar variables de entorno
        env = os.environ.copy()
        env['TK_SILENCE_DEPRECATION'] = '1'  # Silenciar warnings de tkinter en macOS
        
        # Ejecutar la aplicación
        subprocess.run([python_exe, 'main.py'], env=env)
        
    except KeyboardInterrupt:
        print("\n⏹️  Aplicación interrumpida por el usuario")
    except Exception as e:
        print(f"\n❌ Error ejecutando la aplicación: {e}")
        return False
    
    return True

def main():
    """Función principal"""
    print_banner()
    
    # Verificar archivos
    if not check_files():
        input("Presiona Enter para salir...")
        sys.exit(1)
    
    # Configurar entorno virtual
    if not setup_venv():
        input("Presiona Enter para salir...")
        sys.exit(1)
    
    # Mostrar capacidades del sistema
    show_system_capabilities()
    
    # Ejecutar aplicación
    print("🎯 ¿Listo para iniciar? (Presiona Enter para continuar)")
    input()
    
    success = run_application()
    
    print()
    print("👋 ¡Hasta luego!")
    
    if not success:
        input("Presiona Enter para salir...")
        sys.exit(1)

if __name__ == "__main__":
    main()
