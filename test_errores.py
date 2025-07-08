#!/usr/bin/env python3
"""
Script de prueba para verificar el comportamiento con errores sintácticos
"""

from robot_lexical_analyzer import RobotLexicalAnalyzer

def test_codigo_con_errores():
    """Prueba con código que tiene errores sintácticos"""
    print("=== PRUEBA CON ERRORES SINTÁCTICOS ===")
    
    # Código con errores sintácticos
    code_error = """Robot r1
r1.base = 90 90  # Error: valor duplicado
r2.hombro = 45   # Error: robot no declarado
r1.invalid = 30  # Error: componente no válido
r1.base =        # Error: falta valor"""
    
    print("Código con errores:")
    for i, line in enumerate(code_error.split('\n'), 1):
        if line.strip():
            print(f"  {i}. {line}")
    
    analyzer = RobotLexicalAnalyzer()
    tokens, errors = analyzer.analyze(code_error)
    
    print("\n" + analyzer.get_formatted_output())

def test_codigo_sin_errores():
    """Prueba con código válido"""
    print("\n" + "="*60)
    print("=== PRUEBA CON CÓDIGO VÁLIDO ===")
    
    # Código sin errores
    code_valid = """Robot r1
r1.repetir = 2
r1.inicio
r1.base = 90
r1.hombro = 45
r1.espera = 1
r1.fin"""
    
    print("Código válido:")
    for i, line in enumerate(code_valid.split('\n'), 1):
        if line.strip():
            print(f"  {i}. {line}")
    
    analyzer = RobotLexicalAnalyzer()
    tokens, errors = analyzer.analyze(code_valid)
    
    print("\n" + analyzer.get_formatted_output())

def test_codigo_con_tokens_desconocidos():
    """Prueba con tokens desconocidos"""
    print("\n" + "="*60)
    print("=== PRUEBA CON TOKENS DESCONOCIDOS ===")
    
    # Código con tokens desconocidos
    code_unknown = """Robot r1
r1.base = 90 & 45  # Caracter & desconocido
r1.hombro = @30    # Caracter @ desconocido"""
    
    print("Código con tokens desconocidos:")
    for i, line in enumerate(code_unknown.split('\n'), 1):
        if line.strip():
            print(f"  {i}. {line}")
    
    analyzer = RobotLexicalAnalyzer()
    tokens, errors = analyzer.analyze(code_unknown)
    
    print("\n" + analyzer.get_formatted_output())

def main():
    """Función principal"""
    print("PRUEBAS DE MANEJO DE ERRORES")
    print("=" * 60)
    
    try:
        test_codigo_con_errores()
        test_codigo_sin_errores()
        test_codigo_con_tokens_desconocidos()
        
        print("\n" + "=" * 60)
        print("✅ TODAS LAS PRUEBAS COMPLETADAS")
        print("\nComportamiento esperado:")
        print("• Con errores: Solo muestra errores, NO tabla de símbolos ni cuádruplos")
        print("• Sin errores: Muestra análisis completo con todas las tablas")
        print("• Con tokens desconocidos: Muestra errores léxicos específicos")
        
    except Exception as e:
        print(f"❌ Error durante las pruebas: {str(e)}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
