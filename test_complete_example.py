#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from robot_lexical_analyzer import RobotLexicalAnalyzer

def test_complete_example():
    """Prueba el ejemplo completo de sintaxis extendida"""
    
    # El código exacto que enviaste
    test_code = """# Declaración del robot
Robot r1
r1.velocidad = 2

# Rutina de manufactura: tomar pieza y colocarla
inicio tomar_y_colocar repetir 3 veces
    # Posición inicial - sobre la pieza
    r1.base = 45
    r1.hombro = 120
    r1.codo = 90
    espera 1
    
    # Bajar y agarrar pieza
    r1.codo = 45
    r1.garra = 20
    espera 0.5
    
    # Levantar pieza
    r1.codo = 90
    r1.hombro = 90
    espera 1
    
    # Mover a posición de destino
    r1.base = 180
    r1.hombro = 100
    espera 1.5
    
    # Soltar pieza
    r1.codo = 60
    r1.garra = 90
    espera 0.5
    
    # Volver a posición inicial
    r1.base = 0
    r1.hombro = 180
    r1.codo = 180
fin

# Rutina de seguridad
inicio posicion_segura
    r1.velocidad = 1
    r1.base = 0
    r1.hombro = 90
    r1.codo = 90
    r1.garra = 0
fin"""
    
    print("=== PRUEBA EJEMPLO COMPLETO ===")
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
    success = test_complete_example()
    print(f"\n{'✅ PRUEBA EXITOSA' if success else '❌ PRUEBA FALLIDA'}")
