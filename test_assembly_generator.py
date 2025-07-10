#!/usr/bin/env python3
"""
Script de prueba para el generador de código ensamblador
"""

from robot_lexical_analyzer import RobotLexicalAnalyzer
from assembly_generator import AssemblyGenerator, DOSBoxController

def test_assembly_generation():
    """Prueba la generación de código ensamblador"""
    print("=== PRUEBA DE GENERACIÓN DE CÓDIGO ENSAMBLADOR ===\n")
    
    # Código de prueba
    code = """Robot r1
r1.repetir = 2
r1.inicio
r1.velocidad = 2
r1.base = 90
r1.hombro = 45
r1.espera = 1
r1.fin"""
    
    print("Código fuente:")
    for i, line in enumerate(code.split('\n'), 1):
        if line.strip():
            print(f"  {i}. {line}")
    
    # Analizar código
    analyzer = RobotLexicalAnalyzer()
    tokens, errors = analyzer.analyze(code)
    
    if errors:
        print(f"\n❌ Errores en el análisis: {errors}")
        return False
    
    print(f"\n✅ Análisis exitoso: {len(tokens)} tokens procesados")
    
    # Generar código ensamblador
    if analyzer.intermediate_code_generator and analyzer.intermediate_code_generator.cuadruplos:
        print(f"✅ Cuádruplos generados: {len(analyzer.intermediate_code_generator.cuadruplos)}")
        
        # Generar código ensamblador
        generator = AssemblyGenerator()
        asm_code = generator.generate_assembly(analyzer.intermediate_code_generator.cuadruplos, "test_robot")
        
        print("\n=== CÓDIGO ENSAMBLADOR GENERADO ===")
        print(asm_code)
        
        # Guardar código ensamblador
        output_file = "/home/xavier/lexic/DOSBox2/Tasm/test_robot.asm"
        try:
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(asm_code)
            print(f"\n✅ Código ensamblador guardado en: {output_file}")
            
            return True
        except Exception as e:
            print(f"\n❌ Error al guardar: {str(e)}")
            return False
    else:
        print("\n❌ No se generaron cuádruplos")
        return False

def test_simple_code():
    """Prueba con código más simple"""
    print("\n\n=== PRUEBA CON CÓDIGO SIMPLE ===\n")
    
    code = """Robot r1
r1.base = 90
r1.hombro = 45
r1.espera = 2"""
    
    print("Código fuente:")
    for i, line in enumerate(code.split('\n'), 1):
        if line.strip():
            print(f"  {i}. {line}")
    
    # Analizar código
    analyzer = RobotLexicalAnalyzer()
    tokens, errors = analyzer.analyze(code)
    
    if errors:
        print(f"\n❌ Errores en el análisis: {errors}")
        return False
    
    print(f"\n✅ Análisis exitoso: {len(tokens)} tokens procesados")
    
    # Generar código ensamblador
    if analyzer.intermediate_code_generator and analyzer.intermediate_code_generator.cuadruplos:
        print(f"✅ Cuádruplos generados: {len(analyzer.intermediate_code_generator.cuadruplos)}")
        
        # Generar código ensamblador
        asm_code, error = analyzer.generate_assembly_code("simple_robot")
        
        if error:
            print(f"\n❌ Error al generar ensamblador: {error}")
            return False
        
        print("\n=== CÓDIGO ENSAMBLADOR GENERADO ===")
        print(asm_code)
        
        # Guardar código ensamblador
        output_file = "/home/xavier/lexic/DOSBox2/Tasm/simple_robot.asm"
        try:
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(asm_code)
            print(f"\n✅ Código ensamblador guardado en: {output_file}")
            
            return True
        except Exception as e:
            print(f"\n❌ Error al guardar: {str(e)}")
            return False
    else:
        print("\n❌ No se generaron cuádruplos")
        return False

def test_dosbox_integration():
    """Prueba la integración con DOSBox (solo si está disponible)"""
    print("\n\n=== PRUEBA DE INTEGRACIÓN CON DOSBOX ===\n")
    
    # Verificar si DOSBox está disponible
    dosbox_path = "/home/xavier/lexic/DOSBox2"
    if not os.path.exists(dosbox_path):
        print(f"❌ DOSBox no encontrado en: {dosbox_path}")
        return False
    
    print(f"✅ DOSBox encontrado en: {dosbox_path}")
    
    # Verificar archivos de TASM
    tasm_files = ["TASM.EXE", "TLINK.EXE"]
    tasm_path = os.path.join(dosbox_path, "Tasm")
    
    for file in tasm_files:
        file_path = os.path.join(tasm_path, file)
        if os.path.exists(file_path):
            print(f"✅ {file} encontrado")
        else:
            print(f"❌ {file} no encontrado en: {file_path}")
            return False
    
    print("\n✅ Todos los archivos de TASM están disponibles")
    print("ℹ️  La compilación automática requiere wine en Linux")
    
    return True

def main():
    """Ejecuta todas las pruebas"""
    print("PRUEBAS DEL GENERADOR DE CÓDIGO ENSAMBLADOR")
    print("=" * 60)
    
    results = []
    
    # Prueba 1: Generación básica
    results.append(test_assembly_generation())
    
    # Prueba 2: Código simple
    results.append(test_simple_code())
    
    # Prueba 3: Integración DOSBox
    results.append(test_dosbox_integration())
    
    # Resumen
    print("\n" + "=" * 60)
    print("RESUMEN DE PRUEBAS")
    print("=" * 60)
    
    passed = sum(results)
    total = len(results)
    
    print(f"✅ Pruebas exitosas: {passed}/{total}")
    print(f"❌ Pruebas fallidas: {total - passed}/{total}")
    
    if passed == total:
        print("\n🎉 ¡Todas las pruebas pasaron exitosamente!")
        print("🔧 El generador de código ensamblador está listo para usar")
    else:
        print("\n⚠️  Algunas pruebas fallaron")
        print("🔍 Revise los errores antes de continuar")
    
    return passed == total

if __name__ == "__main__":
    import os
    main()
