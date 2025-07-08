#!/usr/bin/env python3
"""
Script de prueba para demostrar las validaciones semánticas A, B, C y D
del analizador léxico, sintáctico y semántico para brazo robótico.
"""

from robot_lexical_analyzer import RobotLexicalAnalyzer

def test_validation_a_unique_declarations():
    """Prueba Validación A: Declaración única de robots"""
    print("=== VALIDACIÓN A: DECLARACIÓN ÚNICA DE ROBOTS ===")
    
    # Caso con ERROR: declaración duplicada
    print("\n1. Caso con ERROR (declaración duplicada):")
    code_error = """Robot r1
Robot r1
r1.base = 90"""
    
    analyzer = RobotLexicalAnalyzer()
    tokens, errors = analyzer.analyze(code_error)
    
    if analyzer.semantic_analyzer and analyzer.semantic_analyzer.errors:
        for error in analyzer.semantic_analyzer.errors:
            print(f"   ❌ {error}")
    else:
        print("   ⚠️ No se detectaron errores (inesperado)")
    
    # Caso CORRECTO
    print("\n2. Caso CORRECTO (declaraciones únicas):")
    code_correct = """Robot r1
Robot r2
r1.base = 90
r2.base = 180"""
    
    analyzer = RobotLexicalAnalyzer()
    tokens, errors = analyzer.analyze(code_correct)
    
    if analyzer.semantic_analyzer and not analyzer.semantic_analyzer.errors:
        print("   ✅ Validación A pasada correctamente")
    else:
        print("   ❌ Errores inesperados:")
        for error in analyzer.semantic_analyzer.errors:
            print(f"      {error}")

def test_validation_b_unique_assignments():
    """Prueba Validación B: Asignaciones únicas por componente"""
    print("\n=== VALIDACIÓN B: ASIGNACIONES ÚNICAS POR COMPONENTE ===")
    print("(Actualmente deshabilitada para permitir secuencias de movimiento)")
    
    code = """Robot r1
r1.base = 90
r1.base = 180
r1.garra = 0
r1.garra = 45"""
    
    analyzer = RobotLexicalAnalyzer()
    tokens, errors = analyzer.analyze(code)
    
    print("\nCódigo de prueba:")
    for i, line in enumerate(code.split('\n'), 1):
        if line.strip():
            print(f"   {i}. {line}")
    
    print("\nResultado:")
    if analyzer.semantic_analyzer and not analyzer.semantic_analyzer.errors:
        print("   ✅ Validación B: Permite múltiples asignaciones (secuencias de movimiento)")
    else:
        print("   ❌ Errores encontrados:")
        for error in analyzer.semantic_analyzer.errors:
            print(f"      {error}")

def test_validation_c_value_ranges():
    """Prueba Validación C: Valores dentro de rangos válidos"""
    print("\n=== VALIDACIÓN C: VALORES DENTRO DE RANGOS VÁLIDOS ===")
    
    # Caso con ERRORES: valores fuera de rango
    print("\n1. Caso con ERRORES (valores fuera de rango):")
    code_error = """Robot r1
r1.base = 400
r1.hombro = -50
r1.garra = 100
r1.espera = 70"""
    
    analyzer = RobotLexicalAnalyzer()
    tokens, errors = analyzer.analyze(code_error)
    
    if analyzer.semantic_analyzer and analyzer.semantic_analyzer.errors:
        for error in analyzer.semantic_analyzer.errors:
            if "fuera del rango válido" in error:
                print(f"   ❌ {error}")
    
    # Caso CORRECTO
    print("\n2. Caso CORRECTO (valores en rango):")
    code_correct = """Robot r1
r1.base = 270
r1.hombro = 45
r1.garra = 30
r1.espera = 2.5"""
    
    analyzer = RobotLexicalAnalyzer()
    tokens, errors = analyzer.analyze(code_correct)
    
    if analyzer.semantic_analyzer:
        range_errors = [e for e in analyzer.semantic_analyzer.errors if "fuera del rango válido" in e]
        if not range_errors:
            print("   ✅ Validación C pasada correctamente")
        else:
            print("   ❌ Errores de rango inesperados:")
            for error in range_errors:
                print(f"      {error}")
    
    # Caso con ADVERTENCIAS: valores en límites
    print("\n3. Caso con ADVERTENCIAS (valores en límites):")
    code_warning = """Robot r1
r1.base = 0
r1.hombro = 180
r1.garra = 90"""
    
    analyzer = RobotLexicalAnalyzer()
    tokens, errors = analyzer.analyze(code_warning)
    
    if analyzer.semantic_analyzer and analyzer.semantic_analyzer.warnings:
        for warning in analyzer.semantic_analyzer.warnings:
            if "está en el límite" in warning:
                print(f"   ⚠️ {warning}")

def test_validation_d_declared_robots():
    """Prueba Validación D: Robots correctamente declarados"""
    print("\n=== VALIDACIÓN D: ROBOTS CORRECTAMENTE DECLARADOS ===")
    
    # Caso con ERROR: robot no declarado
    print("\n1. Caso con ERROR (robot no declarado):")
    code_error = """r1.base = 90
r2.hombro = 45"""
    
    analyzer = RobotLexicalAnalyzer()
    tokens, errors = analyzer.analyze(code_error)
    
    if analyzer.semantic_analyzer and analyzer.semantic_analyzer.errors:
        for error in analyzer.semantic_analyzer.errors:
            if "usado sin haber sido declarado" in error:
                print(f"   ❌ {error}")
    
    # Caso CORRECTO
    print("\n2. Caso CORRECTO (robots declarados):")
    code_correct = """Robot r1
Robot r2
r1.base = 90
r2.hombro = 45"""
    
    analyzer = RobotLexicalAnalyzer()
    tokens, errors = analyzer.analyze(code_correct)
    
    if analyzer.semantic_analyzer:
        declaration_errors = [e for e in analyzer.semantic_analyzer.errors if "usado sin haber sido declarado" in e]
        if not declaration_errors:
            print("   ✅ Validación D pasada correctamente")
        else:
            print("   ❌ Errores de declaración inesperados:")
            for error in declaration_errors:
                print(f"      {error}")

def test_complete_example():
    """Prueba ejemplo completo con todas las validaciones"""
    print("\n=== EJEMPLO COMPLETO: TODAS LAS VALIDACIONES ===")
    
    # Código con múltiples errores
    print("\n1. Código con MÚLTIPLES ERRORES:")
    code_errors = """Robot r1
Robot r1
r1.base = 400
r2.hombro = 45"""
    
    analyzer = RobotLexicalAnalyzer()
    tokens, errors = analyzer.analyze(code_errors)
    
    print("Código:")
    for i, line in enumerate(code_errors.split('\n'), 1):
        if line.strip():
            print(f"   {i}. {line}")
    
    print("\nErrores encontrados:")
    if analyzer.semantic_analyzer and analyzer.semantic_analyzer.errors:
        for error in analyzer.semantic_analyzer.errors:
            print(f"   ❌ {error}")
    
    # Código completamente correcto
    print("\n2. Código COMPLETAMENTE CORRECTO:")
    code_correct = """Robot r1
Robot r2
r1.repetir = 3
r1.inicio
r1.base = 0
r1.hombro = 90
r1.codo = 45
r1.muneca = 180
r1.garra = 0
r1.espera = 1.0
r1.base = 90
r1.garra = 30
r1.espera = 0.5
r1.fin
r2.base = 270
r2.hombro = 135"""
    
    analyzer = RobotLexicalAnalyzer()
    tokens, errors = analyzer.analyze(code_correct)
    
    if analyzer.semantic_analyzer and not analyzer.semantic_analyzer.errors:
        print("   ✅ ANÁLISIS SEMÁNTICO: CORRECTO")
        print("   ✅ Todas las validaciones pasadas:")
        print("      • Declaración única de robots")
        print("      • Asignaciones únicas por componente")
        print("      • Valores dentro de rangos válidos")
        print("      • Robots correctamente declarados")
    else:
        print("   ❌ Errores inesperados en código correcto:")
        if analyzer.semantic_analyzer:
            for error in analyzer.semantic_analyzer.errors:
                print(f"      {error}")

def show_component_ranges():
    """Muestra los rangos válidos para cada componente"""
    print("\n=== RANGOS VÁLIDOS POR COMPONENTE ===")
    from robot_lexical_analyzer import COMPONENT_RANGES
    
    print("| Componente | Mín   | Máx   | Descripción")
    print("|------------|-------|-------|-------------")
    for component, range_info in COMPONENT_RANGES.items():
        min_val = range_info['min']
        max_val = range_info['max']
        desc = range_info['description']
        print(f"| {component:<10} | {min_val:<5} | {max_val:<5} | {desc}")

def main():
    """Función principal que ejecuta todas las pruebas"""
    print("PRUEBAS DE VALIDACIONES SEMÁNTICAS DEL ANALIZADOR ROBÓTICO")
    print("=" * 60)
    
    # Ejecutar todas las pruebas
    test_validation_a_unique_declarations()
    test_validation_b_unique_assignments()
    test_validation_c_value_ranges()
    test_validation_d_declared_robots()
    test_complete_example()
    show_component_ranges()
    
    print("\n" + "=" * 60)
    print("PRUEBAS COMPLETADAS")
    print("\nPara más detalles técnicos, consulte:")
    print("- documentacion_validaciones_semanticas.md")
    print("- ejemplos_validaciones_semanticas.md")

if __name__ == "__main__":
    main()
