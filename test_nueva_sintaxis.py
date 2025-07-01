#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from robot_lexical_analyzer import RobotLexicalAnalyzer

def test_nueva_sintaxis():
    """Prueba la nueva sintaxis del lenguaje robótico"""
    
    # El código con sintaxis consistente usando '=' en todas las instrucciones
    test_code = """# Ejemplo con la nueva sintaxis
Robot r1
r1.repetir = 3

r1.inicio
    r1.velocidad = 1
    r1.base = 45
    r1.hombro = 120
    r1.codo = 90
    r1.espera = 1

    r1.velocidad = 2
    r1.codo = 45
    r1.garra = 20
    r1.espera = 1

    r1.velocidad = 3
    r1.codo = 90
    r1.hombro = 90
    r1.espera = 1
    
    r1.velocidad = 4
    r1.base = 180
    r1.hombro = 100
    r1.espera = 1
    
    r1.velocidad = 5
    r1.codo = 60
    r1.garra = 80
    r1.espera = 1  
r1.fin"""
    
    print("=== PRUEBA NUEVA SINTAXIS ===")
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
    success = test_nueva_sintaxis()
    print(f"\n{'✅ PRUEBA EXITOSA' if success else '❌ PRUEBA FALLIDA'}")
