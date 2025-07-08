#!/usr/bin/env python3
"""
Script de prueba para verificar la generación de cuádruplos (código intermedio)
"""

from robot_lexical_analyzer import RobotLexicalAnalyzer

def test_cuadruplos_sin_repeticion():
    """Prueba generación de cuádruplos para código sin repetición"""
    print("=== PRUEBA 1: CÓDIGO SIN REPETICIÓN ===")
    
    code = """Robot r1
r1.base = 90
r1.hombro = 45
r1.espera = 2"""
    
    print("Código fuente:")
    for i, line in enumerate(code.split('\n'), 1):
        if line.strip():
            print(f"  {i}. {line}")
    
    analyzer = RobotLexicalAnalyzer()
    tokens, errors = analyzer.analyze(code)
    
    if analyzer.intermediate_code_generator:
        print("\n" + analyzer.intermediate_code_generator.get_formatted_table())
    else:
        print("❌ No se generó código intermedio")

def test_cuadruplos_con_repeticion():
    """Prueba generación de cuádruplos para código con repetición"""
    print("\n=== PRUEBA 2: CÓDIGO CON REPETICIÓN ===")
    
    code = """Robot r1
r1.repetir = 3
r1.inicio
r1.velocidad = 2
r1.base = 45
r1.hombro = 120
r1.codo = 60
r1.garra = 80
r1.espera = 1
r1.fin"""
    
    print("Código fuente:")
    for i, line in enumerate(code.split('\n'), 1):
        if line.strip():
            print(f"  {i}. {line}")
    
    analyzer = RobotLexicalAnalyzer()
    tokens, errors = analyzer.analyze(code)
    
    if analyzer.intermediate_code_generator:
        print("\n" + analyzer.intermediate_code_generator.get_formatted_table())
    else:
        print("❌ No se generó código intermedio")

def test_cuadruplos_multiples_robots():
    """Prueba generación de cuádruplos para múltiples robots"""
    print("\n=== PRUEBA 3: MÚLTIPLES ROBOTS ===")
    
    code = """Robot r1
Robot r2
r1.base = 90
r2.hombro = 45
r1.espera = 1
r2.garra = 30"""
    
    print("Código fuente:")
    for i, line in enumerate(code.split('\n'), 1):
        if line.strip():
            print(f"  {i}. {line}")
    
    analyzer = RobotLexicalAnalyzer()
    tokens, errors = analyzer.analyze(code)
    
    if analyzer.intermediate_code_generator:
        print("\n" + analyzer.intermediate_code_generator.get_formatted_table())
    else:
        print("❌ No se generó código intermedio")

def test_analisis_completo():
    """Prueba análisis completo incluyendo tabla de símbolos y cuádruplos"""
    print("\n=== PRUEBA 4: ANÁLISIS COMPLETO ===")
    
    code = """Robot r1
r1.repetir = 2
r1.inicio
r1.base = 0
r1.garra = 0
r1.espera = 0.5
r1.base = 90
r1.garra = 45
r1.espera = 1
r1.fin"""
    
    print("Código fuente:")
    for i, line in enumerate(code.split('\n'), 1):
        if line.strip():
            print(f"  {i}. {line}")
    
    analyzer = RobotLexicalAnalyzer()
    tokens, errors = analyzer.analyze(code)
    
    # Mostrar solo la parte de tabla de símbolos y cuádruplos
    output = analyzer.get_formatted_output()
    lines = output.split('\n')
    
    # Buscar donde empieza la tabla de símbolos
    start_symbols = -1
    start_quadruples = -1
    for i, line in enumerate(lines):
        if "TABLA DE SÍMBOLOS" in line:
            start_symbols = i
        elif "TABLA DE CUÁDRUPLOS" in line:
            start_quadruples = i
            break
    
    if start_symbols >= 0:
        print("\n" + '\n'.join(lines[start_symbols:start_quadruples + 30]))

def main():
    """Función principal"""
    print("PRUEBAS DEL GENERADOR DE CÓDIGO INTERMEDIO (CUÁDRUPLOS)")
    print("=" * 60)
    
    try:
        test_cuadruplos_sin_repeticion()
        test_cuadruplos_con_repeticion()
        test_cuadruplos_multiples_robots()
        test_analisis_completo()
        
        print("\n" + "=" * 60)
        print("✅ TODAS LAS PRUEBAS COMPLETADAS")
        print("\nTipos de operaciones implementadas:")
        print("• DECLARAR: Declaración de robots")
        print("• ASIG: Asignación de valores")
        print("• CALL: Llamadas a funciones/movimientos")
        print("• COMPARAR: Comparaciones para control de flujo")
        print("• SALTO_CONDICIONAL: Saltos condicionales")
        print("• SALTO_INCONDICIONAL: Saltos incondicionales")
        print("• DECREMENTO: Operaciones de decremento")
        print("• DECLARAR_ETIQUETA: Declaración de etiquetas")
        print("• FIN: Marcadores de fin de bloque")
        
    except Exception as e:
        print(f"❌ Error durante las pruebas: {str(e)}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
