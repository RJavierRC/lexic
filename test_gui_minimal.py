#!/usr/bin/env python3
"""
Script de prueba para verificar que main.py funciona correctamente
"""

import sys
import os

# Agregar el directorio actual al path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def test_gui_import():
    """Prueba que se puede importar la GUI sin errores"""
    try:
        from main import LexicalAnalyzerGUI
        print("✓ La clase LexicalAnalyzerGUI se importó correctamente")
        return True
    except Exception as e:
        print(f"✗ Error al importar LexicalAnalyzerGUI: {e}")
        return False

def test_gui_creation():
    """Prueba que se puede crear una instancia de la GUI"""
    try:
        from main import LexicalAnalyzerGUI
        app = LexicalAnalyzerGUI()
        print("✓ La instancia de LexicalAnalyzerGUI se creó correctamente")
        # No llamamos a run() para evitar que se quede colgado
        return True
    except Exception as e:
        print(f"✗ Error al crear instancia de LexicalAnalyzerGUI: {e}")
        import traceback
        traceback.print_exc()
        return False

def test_dependencies():
    """Prueba que todas las dependencias están disponibles"""
    try:
        import tkinter as tk
        print("✓ tkinter está disponible")
        
        from robot_lexical_analyzer import RobotLexicalAnalyzer
        print("✓ RobotLexicalAnalyzer está disponible")
        
        return True
    except Exception as e:
        print(f"✗ Error con dependencias: {e}")
        return False

def main():
    print("=== Prueba de GUI - Analizador Léxico Robótico ===\n")
    
    # Verificar entorno
    print(f"Python: {sys.version}")
    print(f"DISPLAY: {os.environ.get('DISPLAY', 'No configurado')}")
    print()
    
    # Ejecutar pruebas
    tests = [
        test_dependencies,
        test_gui_import,
        test_gui_creation
    ]
    
    results = []
    for test in tests:
        print(f"Ejecutando {test.__name__}...")
        result = test()
        results.append(result)
        print()
    
    # Resumen
    passed = sum(results)
    total = len(results)
    print(f"=== Resumen: {passed}/{total} pruebas pasaron ===")
    
    if passed == total:
        print("¡Todas las pruebas pasaron! La GUI debería funcionar correctamente.")
        print("Para ejecutar la aplicación, usa: python3 main.py")
    else:
        print("Algunas pruebas fallaron. Revisa los errores anteriores.")

if __name__ == "__main__":
    main()
