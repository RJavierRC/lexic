#!/usr/bin/env python3
"""
Test para generar ejecutable DOS REAL que resuelva el error de Proteus
"""

from robot_lexical_analyzer import RobotLexicalAnalyzer
import os

def test_dos_real_for_proteus():
    """Genera ejecutable DOS REAL para resolver error de opcode en Proteus"""
    
    print("🎯" + "="*70)
    print("🎯 GENERANDO EJECUTABLE DOS REAL PARA PROTEUS")
    print("🎯" + "="*70)
    print("❌ Problema: Unknown 1-byte opcode at 0002:0002 62")
    print("✅ Solución: Ejecutable MS-DOS auténtico para 8086")
    print()
    
    analyzer = RobotLexicalAnalyzer()
    
    # Código robótico de prueba
    code = """Robot r1
r1.velocidad = 2
r1.base = 45
r1.hombro = 120
r1.codo = 90
r1.espera = 1"""
    
    print("💾 Código de prueba:")
    print(code)
    print()
    
    # Analizar código
    print("🔍 Analizando código...")
    tokens, errors = analyzer.analyze(code)
    print(f"📊 Resultado: {len(tokens)} tokens, {len(errors)} errores")
    
    if errors:
        print("⚠️  Errores encontrados:", errors)
    else:
        print("✅ Análisis exitoso sin errores")
    
    print()
    
    # Generar ejecutable DOS REAL
    print("🎯 Generando ejecutable DOS REAL para Proteus...")
    success, message = analyzer.generate_and_compile_dos_real("dos_real_proteus")
    
    if success:
        print("✅ GENERACIÓN EXITOSA!")
        print("📄", message)
        
        # Verificar archivo
        tasm_path = os.path.join(os.getcwd(), "DOSBox2", "Tasm")
        exe_file = os.path.join(tasm_path, "dos_real_proteus.exe")
        
        if os.path.exists(exe_file):
            size = os.path.getsize(exe_file)
            print(f"📁 Archivo verificado: dos_real_proteus.exe ({size:,} bytes)")
            
            # Leer y mostrar información del header
            with open(exe_file, 'rb') as f:
                header = f.read(64)
            
            if header[0:2] == b'MZ':
                print("✅ Header DOS válido (MZ signature)")
                print("✅ Formato: MS-DOS Executable")
            else:
                print("⚠️  Header no estándar")
                
        else:
            print("❌ Archivo no encontrado")
    else:
        print("❌ GENERACIÓN FALLÓ!")
        print("📄", message)
    
    print()
    print("🎮 INSTRUCCIONES PARA PROTEUS ISIS:")
    print("="*50)
    print("1. 🖥️  CONFIGURACIÓN DEL PROCESADOR:")
    print("   • Seleccionar: 8086 (Real Mode)")
    print("   • NO usar: 8088, 80286, x86")
    print("   • Frecuencia: 4.77MHz o 8MHz")
    
    print("\n2. 📂 CARGAR PROGRAMA:")
    print("   • Archivo: dos_real_proteus.exe")
    print("   • Ubicación: DOSBox2/Tasm/")
    print("   • Verificar: Ejecutable MS-DOS")
    
    print("\n3. 🔌 CONFIGURAR 8255 PPI:")
    print("   • Componente: 8255A-5")
    print("   • Dirección base: 0300h")
    print("   • Puerto A (Base): 0300h")
    print("   • Puerto B (Hombro): 0301h")
    print("   • Puerto C (Codo): 0302h")
    print("   • Control: 0303h")
    
    print("\n4. 🤖 CONECTAR MOTORES:")
    print("   • Driver: ULN2003A por motor")
    print("   • Tipo: Motores paso a paso")
    print("   • Conexión: Según datasheet ULN2003A")
    
    print("\n5. ▶️  EJECUTAR:")
    print("   • Iniciar simulación")
    print("   • Verificar movimiento de motores")
    print("   • El error de opcode debería desaparecer")
    
    print("\n" + "🎯" + "="*70)
    print("🎯 ¡EJECUTABLE DOS REAL LISTO PARA PROTEUS!")
    print("🎯" + "="*70)

if __name__ == "__main__":
    test_dos_real_for_proteus()
