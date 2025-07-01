#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from robot_lexical_analyzer import RobotLexicalAnalyzer

def test_routine():
    """Prueba rutinas básicas"""
    
    # Código de prueba con rutina simple
    test_code = """
    Robot r1
    r1.velocidad = 2
    
    inicio posicion_home repetir 2 veces
        r1.base = 0
        r1.hombro = 90
        espera 1.0
    fin
    
    r1.garra = 50
    """
    
    print("=== PRUEBA DE RUTINAS ===")
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
    success = test_routine()
    print(f"\n{'✅ PRUEBA EXITOSA' if success else '❌ PRUEBA FALLIDA'}")
