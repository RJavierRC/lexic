#!/usr/bin/env python3
"""
Test para generar robot_program3.exe y robot_program4.exe
"""

from robot_lexical_analyzer import RobotLexicalAnalyzer
import os

def test_robot_programs():
    """Genera los programas robot que el usuario necesita"""
    
    print("🧪 Generando robot_program3.exe y robot_program4.exe...")
    
    analyzer = RobotLexicalAnalyzer()
    
    # Código de prueba robótico
    test_code = """Robot r1
r1.velocidad = 2
r1.base = 45
r1.hombro = 120
r1.codo = 90
r1.espera = 1"""
    
    # Generar robot_program3
    print("\n⚡ Generando robot_program3.exe...")
    success3, msg3 = analyzer.generate_and_compile("robot_program3")
    if success3:
        print(f"✅ robot_program3.exe: {msg3}")
    else:
        print(f"❌ robot_program3.exe: {msg3}")
    
    # Generar robot_program4
    print("\n⚡ Generando robot_program4.exe...")
    success4, msg4 = analyzer.generate_and_compile("robot_program4")
    if success4:
        print(f"✅ robot_program4.exe: {msg4}")
    else:
        print(f"❌ robot_program4.exe: {msg4}")
    
    # Verificar archivos generados
    tasm_path = os.path.join(os.getcwd(), "DOSBox2", "Tasm")
    print(f"\n📁 Verificando archivos en {tasm_path}:")
    
    for program in ["robot_program3", "robot_program4"]:
        exe_file = os.path.join(tasm_path, f"{program}.exe")
        if os.path.exists(exe_file):
            size = os.path.getsize(exe_file)
            print(f"✅ {program}.exe - {size} bytes")
        else:
            print(f"❌ {program}.exe - NO ENCONTRADO")
    
    print("\n🎯 Test completado!")

if __name__ == "__main__":
    test_robot_programs()
