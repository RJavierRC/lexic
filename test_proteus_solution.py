#!/usr/bin/env python3
"""
Test específico para Proteus - Solución completa al error de opcode
"""

from robot_lexical_analyzer import RobotLexicalAnalyzer
import os

def test_proteus_solution():
    """Test completo de la solución para Proteus"""
    
    print("🎯 ===============================================")
    print("🎯 SOLUCIÓN COMPLETA PARA ERROR DE PROTEUS")
    print("🎯 ===============================================")
    print("❌ Problema: Unknown 1-byte opcode at 0002:0002 62")
    print("✅ Solución: Ejecutable específico para Proteus ISIS")
    print("🔧 Configuración: 8086 + puertos 0300h-0303h")
    print("")
    
    analyzer = RobotLexicalAnalyzer()
    
    # Código de prueba robótico que el usuario mencionó
    test_code = """Robot r1
r1.velocidad = 2
r1.base = 45
r1.hombro = 120
r1.codo = 90
r1.espera = 1"""
    
    print("💾 Código de prueba:")
    print(test_code)
    print("")
    
    # Analizar código
    print("🔍 Analizando código...")
    tokens, errors = analyzer.analyze(test_code)
    print(f"📊 Resultado: {len(tokens)} tokens, {len(errors)} errores")
    
    if errors:
        print("⚠️  Errores encontrados:")
        for error in errors[:3]:
            print(f"   - {error}")
    else:
        print("✅ Análisis exitoso sin errores")
    
    print("")
    
    # Generar ejecutable específico para Proteus
    print("🎯 Generando ejecutable específico para Proteus...")
    success, message = analyzer.generate_and_compile_for_proteus("proteus_solution")
    
    if success:
        print("✅ SOLUCIÓN EXITOSA!")
        print(f"📄 {message}")
        
        # Verificar archivo
        tasm_path = os.path.join(os.getcwd(), "DOSBox2", "Tasm")
        exe_file = os.path.join(tasm_path, "proteus_solution.exe")
        
        if os.path.exists(exe_file):
            size = os.path.getsize(exe_file)
            print(f"📁 Archivo verificado: proteus_solution.exe ({size:,} bytes)")
            print("")
            
            print("🎮 INSTRUCCIONES PARA PROTEUS ISIS:")
            print("=" * 40)
            print("1. ⚙️  Configurar procesador como 8086")
            print("2. 📂 Cargar proteus_solution.exe como programa")
            print("3. 🔌 Agregar 8255 PPI con direcciones:")
            print("   • Puerto A (Base): 0300h")
            print("   • Puerto B (Hombro): 0301h") 
            print("   • Puerto C (Codo): 0302h")
            print("   • Control: 0303h")
            print("4. 🤖 Conectar motores paso a paso via ULN2003A")
            print("5. ▶️  Ejecutar simulación")
            print("")
            print("🎯 ¡El error de opcode desconocido debería estar resuelto!")
            
        else:
            print("❌ Error: Archivo no encontrado después de generación")
    else:
        print(f"❌ Error en generación: {message}")
    
    print("")
    print("🎯 ===============================================")
    return success

if __name__ == "__main__":
    test_proteus_solution()
