#!/usr/bin/env python3
"""
Script de depuración para main.py
"""

import traceback
import sys

try:
    print("🔍 Iniciando depuración de main.py...")
    
    # Verificar importaciones
    print("1. Verificando importaciones...")
    import tkinter as tk
    print("   ✅ tkinter importado")
    
    from tkinter import ttk, filedialog, messagebox, scrolledtext, simpledialog
    print("   ✅ componentes de tkinter importados")
    
    import os
    print("   ✅ os importado")
    
    from robot_lexical_analyzer import RobotLexicalAnalyzer
    print("   ✅ RobotLexicalAnalyzer importado")
    
    # Verificar GUI
    print("2. Creando interfaz gráfica...")
    from main import LexicalAnalyzerGUI
    print("   ✅ LexicalAnalyzerGUI importado")
    
    app = LexicalAnalyzerGUI()
    print("   ✅ GUI creada")
    
    # Verificar funciones críticas
    print("3. Verificando funciones...")
    if hasattr(app.analyzer, 'generate_assembly_code'):
        print("   ✅ generate_assembly_code disponible")
    else:
        print("   ❌ generate_assembly_code NO disponible")
    
    if hasattr(app.analyzer, 'generate_and_compile'):
        print("   ✅ generate_and_compile disponible")
    else:
        print("   ❌ generate_and_compile NO disponible")
    
    # Probar ejecutar GUI
    print("4. Iniciando GUI...")
    print("   Si la ventana no aparece, puede ser un problema de display en SSH/terminal")
    print("   En Ubuntu, asegúrate de tener DISPLAY configurado o ejecutar desde GUI")
    
    # Solo ejecutar si tenemos display
    if 'DISPLAY' in os.environ:
        print("   ✅ DISPLAY detectado, ejecutando GUI...")
        app.run()
    else:
        print("   ⚠️ No hay DISPLAY, GUI no se puede ejecutar desde terminal SSH")
        print("   Ejecuta desde el entorno gráfico de Ubuntu")

except Exception as e:
    print(f"❌ Error: {e}")
    print("📋 Traceback completo:")
    traceback.print_exc()
