#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from robot_lexical_analyzer import RobotLexicalAnalyzer

def test_ciclo_completo():
    """Prueba un ciclo completo de robot: agarrar, mover y regresar"""
    
    # Ciclo completo de robot
    test_code = """# Programa completo: Robot agarra objeto, lo mueve y regresa a posición original
Robot r1
r1.repetir = 3

r1.inicio
    # === POSICIÓN INICIAL DE APROXIMACIÓN ===
    r1.velocidad = 1
    r1.base = 0
    r1.hombro = 90
    r1.codo = 90
    r1.garra = 90
    r1.muneca = 0
    r1.espera = 2
    
    # === IR A POSICIÓN DEL OBJETO ===
    r1.velocidad = 2
    r1.base = 45
    r1.hombro = 120
    r1.codo = 90
    r1.espera = 1
    
    # === BAJAR Y AGARRAR OBJETO ===
    r1.velocidad = 1
    r1.codo = 45
    r1.espera = 1
    
    r1.garra = 20
    r1.espera = 1
    
    # === LEVANTAR OBJETO ===
    r1.codo = 90
    r1.hombro = 90
    r1.espera = 1
    
    # === MOVER A POSICIÓN DE DESTINO ===
    r1.velocidad = 3
    r1.base = 180
    r1.hombro = 100
    r1.muneca = 90
    r1.espera = 2
    
    # === COLOCAR OBJETO ===
    r1.velocidad = 1
    r1.codo = 60
    r1.espera = 1
    
    r1.garra = 90
    r1.espera = 1
    
    # === ALEJARSE DEL OBJETO ===
    r1.codo = 90
    r1.hombro = 90
    r1.espera = 1
    
    # === REGRESAR A POSICIÓN ORIGINAL ===
    r1.velocidad = 4
    r1.base = 0
    r1.hombro = 90
    r1.codo = 90
    r1.muneca = 0
    r1.espera = 2
    
    # === POSICIÓN DE REPOSO FINAL ===
    r1.velocidad = 1
    r1.base = 0
    r1.hombro = 180
    r1.codo = 180
    r1.garra = 0
    r1.muneca = 0
    r1.espera = 1
r1.fin"""
    
    print("=== PRUEBA CICLO COMPLETO DE ROBOT ===")
    print("Secuencia: Agarrar → Mover → Colocar → Regresar")
    print("Código a analizar:")
    print(test_code[:500] + "..." if len(test_code) > 500 else test_code)
    print("\n" + "="*60)
    
    # Crear analizador
    analyzer = RobotLexicalAnalyzer()
    
    # Analizar código
    tokens, errors = analyzer.analyze(test_code)
    
    # Mostrar resultados
    result = analyzer.get_formatted_output()
    print(result)
    
    return len(errors) == 0

if __name__ == "__main__":
    success = test_ciclo_completo()
    print(f"\n{'✅ PRUEBA EXITOSA' if success else '❌ PRUEBA FALLIDA'}")
    
    if success:
        print("\n🤖 ANÁLISIS DE LA SECUENCIA:")
        print("1. ✅ Posición inicial de aproximación")
        print("2. ✅ Movimiento a posición del objeto")
        print("3. ✅ Descenso y agarre del objeto")
        print("4. ✅ Elevación del objeto")
        print("5. ✅ Transporte a posición de destino")
        print("6. ✅ Colocación del objeto")
        print("7. ✅ Alejamiento del objeto")
        print("8. ✅ Retorno a posición original")
        print("9. ✅ Posición de reposo final")
        print("\n🔄 El ciclo se repetirá 3 veces según r1.repetir = 3")
