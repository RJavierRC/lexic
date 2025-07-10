#!/usr/bin/env python3
"""
Script de verificación para identificar el problema
"""

print("=== VERIFICACIÓN DEL MÓDULO ROBOT_LEXICAL_ANALYZER ===\n")

try:
    print("1. Importando módulo...")
    from robot_lexical_analyzer import RobotLexicalAnalyzer
    print("   ✅ Importación exitosa")
    
    print("\n2. Creando instancia...")
    analyzer = RobotLexicalAnalyzer()
    print("   ✅ Instancia creada exitosamente")
    
    print("\n3. Verificando métodos disponibles...")
    methods = [m for m in dir(analyzer) if not m.startswith('_')]
    print(f"   📊 Métodos disponibles: {len(methods)}")
    
    for method in sorted(methods):
        print(f"      • {method}")
    
    print("\n4. Verificando métodos específicos...")
    if hasattr(analyzer, 'generate_assembly_code'):
        print("   ✅ generate_assembly_code disponible")
    else:
        print("   ❌ generate_assembly_code NO disponible")
    
    if hasattr(analyzer, 'compile_to_executable'):
        print("   ✅ compile_to_executable disponible")
    else:
        print("   ❌ compile_to_executable NO disponible")
    
    if hasattr(analyzer, 'generate_and_compile'):
        print("   ✅ generate_and_compile disponible")
    else:
        print("   ❌ generate_and_compile NO disponible")
    
    print("\n5. Probando análisis básico...")
    code = "Robot r1\nr1.base = 90"
    tokens, errors = analyzer.analyze(code)
    print(f"   ✅ Análisis exitoso: {len(tokens)} tokens, {len(errors)} errores")
    
    print("\n6. Verificando generación de cuádruplos...")
    if analyzer.intermediate_code_generator:
        cuadruplos = analyzer.intermediate_code_generator.cuadruplos
        print(f"   ✅ Cuádruplos generados: {len(cuadruplos)}")
    else:
        print("   ❌ No se generaron cuádruplos")
    
except Exception as e:
    print(f"❌ Error: {str(e)}")
    import traceback
    traceback.print_exc()
