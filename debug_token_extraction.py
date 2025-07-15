#!/usr/bin/env python3
"""
Test para verificar la extracción de valores del código Robot
"""

from robot_lexical_analyzer import RobotLexicalAnalyzer
from create_dynamic_asm_generator import generate_dynamic_asm_from_analyzer

def test_token_extraction():
    """Prueba la extracción de tokens del código Robot"""
    
    # Código de prueba con tus valores específicos
    test_code = """Robot r1

r1.velocidad = 2       
r1.base = 45           
r1.hombro = 120        
r1.codo = 90           
r1.espera = 1"""
    
    print("🔍 ANÁLISIS DE TOKENS")
    print("="*50)
    print(f"Código a analizar:\n{test_code}")
    print("="*50)
    
    # Crear analizador
    analyzer = RobotLexicalAnalyzer()
    
    # Analizar código
    tokens, errors = analyzer.analyze(test_code)
    
    print(f"\n📊 RESULTADOS DEL ANÁLISIS:")
    print(f"• Total de tokens: {len(tokens)}")
    print(f"• Errores encontrados: {len(errors)}")
    
    # Mostrar todos los tokens
    print(f"\n🔖 LISTA COMPLETA DE TOKENS:")
    for i, token in enumerate(tokens):
        if hasattr(token, 'type') and hasattr(token, 'value'):
            print(f"{i:2d}: {token.type:15} | {token.value}")
        else:
            print(f"{i:2d}: {type(token)} | {token}")
    
    # Buscar específicamente los componentes y valores
    print(f"\n🎯 BÚSQUEDA DE COMPONENTES Y VALORES:")
    i = 0
    found_values = {}
    
    while i < len(tokens) - 2:
        token = tokens[i]
        if hasattr(token, 'type') and hasattr(token, 'value'):
            if token.type == 'COMPONENT':
                component = token.value.lower()
                print(f"  Encontrado componente: {component}")
                
                # Buscar el valor después del '='
                if (i + 2 < len(tokens) and 
                    hasattr(tokens[i + 1], 'type') and 
                    tokens[i + 1].type == 'ASSIGN'):
                    
                    value_token = tokens[i + 2]
                    if hasattr(value_token, 'value'):
                        found_values[component] = value_token.value
                        print(f"    → {component} = {value_token.value}")
                    else:
                        print(f"    → Valor sin atributo 'value': {value_token}")
                else:
                    print(f"    → No se encontró '=' después de {component}")
        i += 1
    
    print(f"\n✅ VALORES EXTRAÍDOS:")
    for component, value in found_values.items():
        print(f"• {component}: {value}")
    
    # Probar el generador dinámico
    print(f"\n🚀 PROBANDO GENERADOR DINÁMICO:")
    try:
        asm_code = generate_dynamic_asm_from_analyzer(analyzer, "test_extraction")
        print("✅ Generador ejecutado exitosamente")
        
        # Mostrar solo las líneas relevantes
        lines = asm_code.split('\n')
        for line in lines:
            if 'VALORES EXTRAÍDOS' in line or '→' in line or 'pasos' in line:
                print(f"  {line}")
                
    except Exception as e:
        print(f"❌ Error en generador: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    test_token_extraction()
