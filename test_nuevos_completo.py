#!/usr/bin/env python3
"""
Test completo de nuevos programas robóticos sin timeouts
"""

from robot_lexical_analyzer import RobotLexicalAnalyzer
import os

def test_new_robot_programs():
    """Test completo de nuevos programas robóticos"""
    
    print("🚀 ===============================================")
    print("🚀 TEST COMPLETO DE NUEVOS PROGRAMAS ROBÓTICOS")
    print("🚀 ===============================================")
    print("⚡ Sistema de compilación instantánea - Sin timeouts")
    print("🎯 Objetivo: Generar múltiples .exe exitosamente\n")
    
    analyzer = RobotLexicalAnalyzer()
    
    # Lista de programas para generar
    programs_to_test = [
        ("test_nuevo1", "Robot r1\nr1.base = 30\nr1.hombro = 60\nr1.codo = 90"),
        ("test_nuevo2", "Robot r2\nr2.velocidad = 3\nr2.base = 180\nr2.espera = 2"),
        ("test_nuevo3", "Robot r3\nr3.base = 45\nr3.hombro = 120\nr3.codo = 90\nr3.espera = 1"),
        ("robot_program5", "Robot r1\nr1.velocidad = 2\nr1.base = 45\nr1.hombro = 120"),
        ("robot_program6", "Robot r1\nr1.codo = 90\nr1.espera = 1\nr1.base = 0")
    ]
    
    successful = 0
    total = len(programs_to_test)
    
    for i, (program_name, code) in enumerate(programs_to_test, 1):
        print(f"\n📋 Test {i}/{total}: {program_name}")
        print(f"💾 Código: {code}")
        
        try:
            # Analizar código
            tokens, errors = analyzer.analyze(code)
            print(f"🔍 Análisis: {len(tokens)} tokens, {len(errors)} errores")
            
            # Generar ejecutable
            print(f"⚡ Generando {program_name}.exe...")
            success, message = analyzer.generate_and_compile(program_name)
            
            if success:
                print(f"✅ {program_name}.exe - EXITOSO")
                successful += 1
            else:
                print(f"❌ {program_name}.exe - FALLÓ: {message}")
                
        except Exception as e:
            print(f"❌ {program_name}.exe - ERROR: {str(e)}")
    
    # Verificar archivos generados
    print(f"\n📁 VERIFICACIÓN DE ARCHIVOS GENERADOS:")
    print("=" * 50)
    
    tasm_path = os.path.join(os.getcwd(), "DOSBox2", "Tasm")
    all_files = os.listdir(tasm_path) if os.path.exists(tasm_path) else []
    exe_files = [f for f in all_files if f.endswith('.exe')]
    
    print(f"🗂️  Total de archivos .exe en {tasm_path}: {len(exe_files)}")
    
    # Verificar programas específicos del test
    for program_name, _ in programs_to_test:
        exe_file = os.path.join(tasm_path, f"{program_name}.exe")
        if os.path.exists(exe_file):
            size = os.path.getsize(exe_file)
            print(f"✅ {program_name}.exe - {size:,} bytes")
        else:
            print(f"❌ {program_name}.exe - NO ENCONTRADO")
    
    # Resultados finales
    print(f"\n🎯 RESULTADOS FINALES:")
    print("=" * 30)
    print(f"✅ Exitosos: {successful}/{total}")
    print(f"❌ Fallidos: {total - successful}/{total}")
    print(f"📊 Tasa de éxito: {(successful/total)*100:.1f}%")
    
    if successful == total:
        print("\n🎉 ¡TODOS LOS TESTS EXITOSOS!")
        print("⚡ El sistema de compilación instantánea funciona perfectamente")
        print("🚀 Los nuevos tests están listos para usar")
    else:
        print(f"\n⚠️  Algunos tests fallaron - Revisar errores")
    
    print("\n" + "=" * 50)
    return successful == total

if __name__ == "__main__":
    test_new_robot_programs()
