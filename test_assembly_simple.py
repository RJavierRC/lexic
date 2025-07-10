#!/usr/bin/env python3
"""
Script de prueba simplificado para el generador de código ensamblador
"""

import os
import sys
sys.path.append('/home/xavier/lexic')

from robot_lexical_analyzer import RobotLexicalAnalyzer

def test_complete_workflow():
    """Prueba el flujo completo: análisis + generación de ensamblador"""
    print("=== PRUEBA COMPLETA DEL GENERADOR DE ENSAMBLADOR ===\n")
    
    # Código de prueba con sintaxis correcta
    code = """Robot r1
r1.base = 90
r1.hombro = 45
r1.espera = 2"""
    
    print("Código fuente:")
    for i, line in enumerate(code.split('\n'), 1):
        if line.strip():
            print(f"  {i}. {line}")
    
    # Crear analizador
    analyzer = RobotLexicalAnalyzer()
    
    # Analizar código
    print("\n1. Analizando código...")
    tokens, errors = analyzer.analyze(code)
    
    if errors:
        print(f"   ❌ Errores encontrados: {errors}")
        return False
    
    print(f"   ✅ Análisis exitoso: {len(tokens)} tokens procesados")
    
    # Verificar cuádruplos
    if not analyzer.intermediate_code_generator or not analyzer.intermediate_code_generator.cuadruplos:
        print("   ❌ No se generaron cuádruplos")
        return False
    
    print(f"   ✅ Cuádruplos generados: {len(analyzer.intermediate_code_generator.cuadruplos)}")
    
    # Mostrar cuádruplos
    print("\n2. Cuádruplos generados:")
    for i, cuadruplo in enumerate(analyzer.intermediate_code_generator.cuadruplos):
        print(f"   {i}: {cuadruplo.operacion} | {cuadruplo.arg1} | {cuadruplo.arg2} | {cuadruplo.resultado}")
    
    # Generar código ensamblador
    print("\n3. Generando código ensamblador...")
    
    try:
        asm_code, error = analyzer.generate_assembly_code("test_simple")
        
        if error:
            print(f"   ❌ Error al generar ensamblador: {error}")
            return False
        
        print("   ✅ Código ensamblador generado exitosamente")
        
        # Guardar el código
        output_file = "/home/xavier/lexic/DOSBox2/Tasm/test_simple.asm"
        try:
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(asm_code)
            print(f"   ✅ Código guardado en: {output_file}")
        except Exception as e:
            print(f"   ❌ Error al guardar: {str(e)}")
            return False
        
        # Mostrar parte del código generado
        print("\n4. Código ensamblador generado (primeras 30 líneas):")
        lines = asm_code.split('\n')
        for i, line in enumerate(lines[:30], 1):
            print(f"   {i:2d}: {line}")
        
        if len(lines) > 30:
            print(f"   ... y {len(lines) - 30} líneas más")
        
        return True
        
    except Exception as e:
        print(f"   ❌ Error inesperado: {str(e)}")
        return False

def test_with_loops():
    """Prueba con código que incluye bucles"""
    print("\n\n=== PRUEBA CON BUCLES ===\n")
    
    code = """Robot r1
r1.repetir = 3
r1.inicio
r1.base = 90
r1.hombro = 45
r1.fin"""
    
    print("Código fuente:")
    for i, line in enumerate(code.split('\n'), 1):
        if line.strip():
            print(f"  {i}. {line}")
    
    # Crear analizador
    analyzer = RobotLexicalAnalyzer()
    
    # Analizar código
    print("\n1. Analizando código...")
    tokens, errors = analyzer.analyze(code)
    
    if errors:
        print(f"   ❌ Errores encontrados: {errors}")
        return False
    
    print(f"   ✅ Análisis exitoso: {len(tokens)} tokens procesados")
    
    # Generar código ensamblador
    print("\n2. Generando código ensamblador...")
    
    try:
        asm_code, error = analyzer.generate_assembly_code("test_loops")
        
        if error:
            print(f"   ❌ Error al generar ensamblador: {error}")
            return False
        
        print("   ✅ Código ensamblador generado exitosamente")
        
        # Guardar el código
        output_file = "/home/xavier/lexic/DOSBox2/Tasm/test_loops.asm"
        try:
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(asm_code)
            print(f"   ✅ Código guardado en: {output_file}")
        except Exception as e:
            print(f"   ❌ Error al guardar: {str(e)}")
            return False
        
        # Contar líneas importantes
        lines = asm_code.split('\n')
        labels = [line for line in lines if ':' in line and not line.strip().startswith(';')]
        moves = [line for line in lines if 'MOV' in line.upper()]
        
        print(f"   📊 Estadísticas del código generado:")
        print(f"      • Total de líneas: {len(lines)}")
        print(f"      • Etiquetas: {len(labels)}")
        print(f"      • Instrucciones MOV: {len(moves)}")
        
        return True
        
    except Exception as e:
        print(f"   ❌ Error inesperado: {str(e)}")
        return False

def verify_dosbox_structure():
    """Verifica la estructura de DOSBox"""
    print("\n\n=== VERIFICACIÓN DE DOSBOX ===\n")
    
    dosbox_path = "/home/xavier/lexic/DOSBox2"
    tasm_path = os.path.join(dosbox_path, "Tasm")
    
    print(f"Verificando estructura en: {dosbox_path}")
    
    # Verificar directorios
    if not os.path.exists(dosbox_path):
        print(f"❌ DOSBox no encontrado en: {dosbox_path}")
        return False
    
    if not os.path.exists(tasm_path):
        print(f"❌ Directorio Tasm no encontrado en: {tasm_path}")
        return False
    
    print(f"✅ Directorio DOSBox encontrado")
    print(f"✅ Directorio Tasm encontrado")
    
    # Verificar archivos clave
    required_files = ["TASM.EXE", "TLINK.EXE", "dosbox.exe"]
    
    for file in required_files:
        if file == "dosbox.exe":
            file_path = os.path.join(dosbox_path, file)
        else:
            file_path = os.path.join(tasm_path, file)
        
        if os.path.exists(file_path):
            print(f"✅ {file} encontrado")
        else:
            print(f"❌ {file} no encontrado")
    
    # Listar archivos .asm existentes
    asm_files = [f for f in os.listdir(tasm_path) if f.endswith('.asm')]
    if asm_files:
        print(f"\n📄 Archivos .asm encontrados: {len(asm_files)}")
        for f in asm_files:
            print(f"   • {f}")
    
    return True

def main():
    """Ejecuta todas las pruebas"""
    print("GENERADOR DE CÓDIGO ENSAMBLADOR - PRUEBAS")
    print("=" * 60)
    
    results = []
    
    # Prueba 1: Flujo completo básico
    results.append(test_complete_workflow())
    
    # Prueba 2: Con bucles
    results.append(test_with_loops())
    
    # Prueba 3: Verificación de DOSBox
    results.append(verify_dosbox_structure())
    
    # Resumen
    print("\n" + "=" * 60)
    print("RESUMEN DE PRUEBAS")
    print("=" * 60)
    
    passed = sum(results)
    total = len(results)
    
    print(f"✅ Pruebas exitosas: {passed}/{total}")
    
    if passed == total:
        print("\n🎉 ¡Todas las pruebas pasaron!")
        print("🔧 El generador está listo para usar")
        print("📁 Los archivos .asm están en DOSBox2/Tasm/")
        print("💡 Puede usar el botón 'Generar .EXE' en la interfaz gráfica")
    else:
        print(f"\n⚠️  {total - passed} pruebas fallaron")
        print("🔍 Revise los errores antes de continuar")

if __name__ == "__main__":
    main()
