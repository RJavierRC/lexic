#!/usr/bin/env python3
"""
Script de prueba para el analizador léxico y sintáctico
"""

from robot_lexical_analyzer import RobotLexicalAnalyzer

def test_analyzer_with_file(filename):
    """Prueba el analizador con un archivo específico"""
    print(f"\n{'='*60}")
    print(f"PROBANDO ARCHIVO: {filename}")
    print('='*60)
    
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            source_code = file.read()
        
        analyzer = RobotLexicalAnalyzer()
        tokens, errors = analyzer.analyze(source_code)
        
        # Mostrar resultado formateado
        print(analyzer.get_formatted_output())
        
    except FileNotFoundError:
        print(f"❌ Error: No se pudo encontrar el archivo '{filename}'")
    except Exception as e:
        print(f"❌ Error inesperado: {e}")

def main():
    """Función principal"""
    print("🤖 ANALIZADOR LÉXICO Y SINTÁCTICO - PRUEBAS")
    
    # Lista de archivos de prueba
    test_files = [
        'ejemplo_tabla_simbolos.robot',
        'test_unknown_tokens.robot', 
        'test_completo.robot',
        'test_errors.robot'
    ]
    
    for test_file in test_files:
        test_analyzer_with_file(test_file)
        print("\n" + "="*60)
        input("Presiona Enter para continuar con el siguiente archivo...")

if __name__ == "__main__":
    main()
