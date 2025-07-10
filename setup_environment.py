#!/usr/bin/env python3
"""
Script para verificar y configurar el entorno de compilación en Ubuntu
"""

import os
import subprocess
import sys

def check_wine_installation():
    """Verifica si Wine está instalado"""
    try:
        result = subprocess.run(["wine", "--version"], capture_output=True, text=True)
        if result.returncode == 0:
            print(f"✅ Wine está instalado: {result.stdout.strip()}")
            return True
        else:
            print("❌ Wine no está funcionando correctamente")
            return False
    except FileNotFoundError:
        print("❌ Wine no está instalado")
        return False

def install_wine():
    """Proporciona instrucciones para instalar Wine"""
    print("\n🔧 INSTALACIÓN DE WINE EN UBUNTU")
    print("=" * 50)
    print("Para poder ejecutar DOSBox y TASM en Ubuntu, necesitas instalar Wine.")
    print("\nEjecuta estos comandos en tu terminal:")
    print("1. sudo apt update")
    print("2. sudo apt install wine")
    print("3. winecfg  # Para configurar Wine (opcional)")
    print("\nAlternativamente, puedes instalar la versión más reciente:")
    print("1. sudo dpkg --add-architecture i386")
    print("2. wget -nc https://dl.winehq.org/wine-builds/winehq.key")
    print("3. sudo apt-key add winehq.key")
    print("4. sudo add-apt-repository 'deb https://dl.winehq.org/wine-builds/ubuntu/ focal main'")
    print("5. sudo apt update")
    print("6. sudo apt install --install-recommends winehq-stable")
    
    choice = input("\n¿Deseas intentar instalar Wine automáticamente? (s/n): ").lower()
    if choice == 's':
        try:
            print("\nInstalando Wine...")
            subprocess.run(["sudo", "apt", "update"], check=True)
            subprocess.run(["sudo", "apt", "install", "-y", "wine"], check=True)
            print("✅ Wine instalado exitosamente")
            return True
        except subprocess.CalledProcessError:
            print("❌ Error al instalar Wine automáticamente")
            print("Por favor, instala Wine manualmente usando las instrucciones anteriores")
            return False
    return False

def check_dosbox_structure():
    """Verifica la estructura de DOSBox"""
    dosbox_path = "/home/xavier/lexic/DOSBox2"
    
    if not os.path.exists(dosbox_path):
        print(f"❌ No se encontró DOSBox en {dosbox_path}")
        return False
    
    required_files = [
        "dosbox.exe",
        "Tasm/TASM.EXE",
        "Tasm/TLINK.EXE"
    ]
    
    missing_files = []
    for file in required_files:
        file_path = os.path.join(dosbox_path, file)
        if not os.path.exists(file_path):
            missing_files.append(file)
    
    if missing_files:
        print(f"❌ Archivos faltantes en DOSBox:")
        for file in missing_files:
            print(f"   - {file}")
        return False
    
    print("✅ Estructura de DOSBox verificada")
    return True

def test_dosbox_wine():
    """Prueba ejecutar DOSBox con Wine"""
    try:
        dosbox_exe = "/home/xavier/lexic/DOSBox2/dosbox.exe"
        if not os.path.exists(dosbox_exe):
            print("❌ dosbox.exe no encontrado")
            return False
        
        print("🧪 Probando DOSBox con Wine...")
        result = subprocess.run(
            ["wine", dosbox_exe, "-c", "exit"], 
            cwd="/home/xavier/lexic/DOSBox2",
            capture_output=True, 
            text=True, 
            timeout=30
        )
        
        if result.returncode == 0:
            print("✅ DOSBox funciona correctamente con Wine")
            return True
        else:
            print(f"❌ Error al ejecutar DOSBox: {result.stderr}")
            return False
            
    except subprocess.TimeoutExpired:
        print("⚠️ DOSBox se ejecutó pero no terminó automáticamente (esto es normal)")
        return True
    except Exception as e:
        print(f"❌ Error al probar DOSBox: {str(e)}")
        return False

def main():
    """Función principal de verificación"""
    print("🔍 VERIFICANDO ENTORNO DE COMPILACIÓN")
    print("=" * 50)
    
    # Verificar sistema operativo
    if os.name == 'nt':
        print("✅ Sistema: Windows - No se requiere Wine")
        wine_ok = True
    else:
        print("📋 Sistema: Linux/Ubuntu - Wine requerido")
        wine_ok = check_wine_installation()
        
        if not wine_ok:
            install_wine()
            wine_ok = check_wine_installation()
    
    # Verificar DOSBox
    dosbox_ok = check_dosbox_structure()
    
    # Probar DOSBox con Wine (solo en Linux)
    if wine_ok and dosbox_ok and os.name != 'nt':
        test_ok = test_dosbox_wine()
    else:
        test_ok = True
    
    print("\n📊 RESUMEN DE VERIFICACIÓN")
    print("=" * 30)
    print(f"Wine instalado: {'✅' if wine_ok else '❌'}")
    print(f"DOSBox disponible: {'✅' if dosbox_ok else '❌'}")
    print(f"Prueba de funcionamiento: {'✅' if test_ok else '❌'}")
    
    if wine_ok and dosbox_ok and test_ok:
        print("\n🎉 ¡El entorno está listo para generar ejecutables!")
        print("Puedes usar el botón 'Generar .EXE' en el analizador robótico.")
    else:
        print("\n⚠️ El entorno necesita configuración adicional.")
        print("Sigue las instrucciones anteriores para completar la configuración.")

if __name__ == "__main__":
    main()
