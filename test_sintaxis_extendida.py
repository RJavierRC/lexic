#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from robot_lexical_analyzer import RobotLexicalAnalyzer

def test_extended_syntax():
    """Prueba la sintaxis extendida del analizador"""
    
    # Código de prueba con la nueva sintaxis
    test_code = """
    // Ejemplo completo de sintaxis extendida
    Robot r1
    
    // Configuración inicial  
    r1.velocidad = 2.5
    r1.base = 90
    r1.hombro = 45
    
    // Comando de espera simple
    espera 1.5
    
    // Rutina con repeticiones
    inicio tomar_y_colocar repetir 3 veces
        r1.base = 45
        espera 1.0
        r1.garra = 20
        r1.hombro = 90
    fin
    
    // Más configuraciones
    r1.muneca = 180
    espera 0.8
    """
    
    print("=== PRUEBA DE SINTAXIS EXTENDIDA ===")
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
    success = test_extended_syntax()
    print(f"\n{'✅ PRUEBA EXITOSA' if success else '❌ PRUEBA FALLIDA'}")
