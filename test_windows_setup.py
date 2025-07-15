#!/usr/bin/env python3
"""
Test de validación para la versión Windows del Analizador Léxico
Verifica que todos los componentes estén funcionando correctamente
"""

import os
import sys
import platform

def test_windows_setup():
    """Prueba la configuración específica de Windows"""
    print("Testing Windows Edition Setup")
    print("=" * 50)
    
    # 1. Verificar sistema operativo
    print(f"Sistema Operativo: {platform.system()}")
    if platform.system() != "Windows":
        print("ADVERTENCIA: Ejecutándose en", platform.system())
        print("   Esta versión está optimizada para Windows")
    else:
        print("Sistema Windows detectado")
    
    # 2. Verificar archivos principales
    required_files = [
        "main.py",
        "robot_lexical_analyzer.py", 
        "robot_tokens.py",
        "assembly_generator.py",
        "windows_config.py"
    ]
    
    print("\nVerificando archivos del proyecto:")
    for file in required_files:
        if os.path.exists(file):
            print(f"   OK {file}")
        else:
            print(f"   FALTA {file}")
    
    # 3. Verificar DOSBox y herramientas
    dosbox_files = [
        "DOSBox2/dosbox.exe",
        "DOSBox2/configuracion.conf",
        "DOSBox2/Tasm/TASM.EXE", 
        "DOSBox2/Tasm/TLINK.EXE"
    ]
    
    print("\nVerificando herramientas de compilación:")
    for file in dosbox_files:
        if os.path.exists(file):
            print(f"   OK {file}")
        else:
            print(f"   FALTA {file}")
    
    # 4. Verificar archivos de prueba
    test_files = [f for f in os.listdir(".") if f.endswith(".robot")]
    print(f"\nArchivos de prueba encontrados: {len(test_files)}")
    for file in test_files[:5]:  # Mostrar solo los primeros 5
        print(f"   {file}")
    if len(test_files) > 5:
        print(f"   ... y {len(test_files) - 5} más")
    
    # 5. Test de importación
    print("\nVerificando importaciones Python:")
    try:
        import tkinter
        print("   OK tkinter")
    except ImportError:
        print("   FALTA tkinter")
    
    try:
        from windows_config import SYSTEM_INFO
        print("   OK windows_config")
        print(f"      {SYSTEM_INFO['name']} v{SYSTEM_INFO['version']}")
    except ImportError as e:
        print(f"   ERROR windows_config: {e}")
    
    try:
        from robot_lexical_analyzer import RobotLexicalAnalyzer
        print("   OK robot_lexical_analyzer")
    except ImportError as e:
        print(f"   ERROR robot_lexical_analyzer: {e}")
    
    try:
        from assembly_generator import DOSBoxController
        print("   OK assembly_generator")
    except ImportError as e:
        print(f"   ERROR assembly_generator: {e}")
    
    print("\n" + "=" * 50)
    print("Test de configuración Windows completado")
    print("\nPara ejecutar la aplicación:")
    print("   Windows: start_windows.bat")
    print("   Python:  python main.py")

def test_simple_analysis():
    """Prueba rápida del analizador"""
    print("\nTest rápido del analizador:")
    
    sample_code = """
inicio
    base { girai 90 }
    garra { abre }
    espera 1000
    garra { cierra }
fin
"""
    
    try:
        from robot_lexical_analyzer import RobotLexicalAnalyzer
        analyzer = RobotLexicalAnalyzer()
        
        # Test léxico
        tokens = analyzer.tokenize(sample_code)
        print(f"   OK Análisis léxico: {len(tokens)} tokens")
        
        # Test sintáctico
        success, message = analyzer.parse(sample_code)
        if success:
            print("   OK Análisis sintáctico: Éxito")
        else:
            print(f"   ERROR Análisis sintáctico: {message}")
        
        print("   OK Test básico completado")
        
    except Exception as e:
        print(f"   ERROR en test: {e}")

if __name__ == "__main__":
    test_windows_setup()
    test_simple_analysis()
    
    print("\n¡Listo para usar el Analizador Léxico Windows Edition!")
