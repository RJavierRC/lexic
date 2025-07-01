#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from robot_lexical_analyzer import RobotLexicalAnalyzer

def test_sintaxis_simple():
    """Prueba la nueva sintaxis con un ejemplo simple"""
    
    test_code = """Robot r1
r1.repetir = 2
r1.velocidad = 3

r1.inicio
    r1.base = 90
    r1.hombro = 45
    r1.espera 2
    
    r1.garra = 50
    r1.espera 1
r1.fin"""
    
    print("=== PRUEBA SINTAXIS SIMPLE ===")
    print("Código a analizar:")
    print(test_code)
    print("\n" + "="*50)
    
    # Crear analizador
    analyzer = RobotLexicalAnalyzer()
    
    # Analizar código
    tokens, errors = analyzer.analyze(test_code)
    
    # Mostrar resultados
    result = analyzer.get_formatted_output()
    print(result)
    
    return len(errors) == 0

if __name__ == "__main__":
    success = test_sintaxis_simple()
    print(f"\n{'✅ PRUEBA EXITOSA' if success else '❌ PRUEBA FALLIDA'}")
