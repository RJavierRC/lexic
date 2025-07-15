#!/usr/bin/env python3
"""
Test del generador COM dinámico con valores específicos del usuario
"""

from robot_lexical_analyzer import RobotLexicalAnalyzer
import create_dynamic_motor_com

def test_dynamic_com():
    """Prueba el generador COM dinámico con valores del usuario"""
    
    # Código del usuario con valores específicos
    test_code = """Robot r1

r1.velocidad = 2       
r1.base = 45           
r1.hombro = 120        
r1.codo = 90           
r1.espera = 1"""
    
    print("🤖 TEST GENERADOR COM DINÁMICO")
    print("="*50)
    print(f"Código del usuario:\n{test_code}")
    print("="*50)
    
    # Crear analizador
    analyzer = RobotLexicalAnalyzer()
    
    # Analizar código
    tokens, errors = analyzer.analyze(test_code)
    
    print(f"\n📊 ANÁLISIS:")
    print(f"• Tokens: {len(tokens)}")
    print(f"• Errores: {len(errors)}")
    
    # Probar extracción de valores
    print(f"\n🔍 EXTRAYENDO VALORES PARA COM:")
    motor_values = create_dynamic_motor_com.extract_motor_values(analyzer)
    
    print(f"\n✅ VALORES EXTRAÍDOS:")
    for motor, angle in motor_values.items():
        print(f"• Motor {motor}: {angle}°")
    
    # Generar código máquina dinámico
    print(f"\n🚀 GENERANDO CÓDIGO MÁQUINA DINÁMICO...")
    machine_code = create_dynamic_motor_com.generate_dynamic_machine_code(motor_values)
    
    print(f"✅ Código máquina generado: {len(machine_code)} bytes")
    
    # Mostrar los primeros bytes para verificar
    print(f"\n🔍 PRIMEROS BYTES DEL CÓDIGO:")
    for i in range(min(20, len(machine_code))):
        print(f"  {i:2d}: 0x{machine_code[i]:02X}")
    
    # Verificar que cada motor tenga diferentes configuraciones
    print(f"\n🎯 VERIFICACIÓN DE DIFERENCIAS ENTRE MOTORES:")
    
    # Buscar patrones de loops para cada motor
    base_steps = create_dynamic_motor_com.calculate_steps_for_angle(motor_values['base'])
    hombro_steps = create_dynamic_motor_com.calculate_steps_for_angle(motor_values['hombro'])
    codo_steps = create_dynamic_motor_com.calculate_steps_for_angle(motor_values['codo'])
    
    print(f"• Motor BASE ({motor_values['base']}°): {base_steps} pasos")
    print(f"• Motor HOMBRO ({motor_values['hombro']}°): {hombro_steps} pasos")
    print(f"• Motor CODO ({motor_values['codo']}°): {codo_steps} pasos")
    
    if base_steps != hombro_steps or hombro_steps != codo_steps:
        print("✅ ¡CADA MOTOR TIENE DIFERENTES PASOS!")
    else:
        print("❌ Los motores tienen los mismos pasos")
    
    # Probar generación completa del COM
    print(f"\n📁 GENERANDO ARCHIVO .COM COMPLETO...")
    try:
        success = create_dynamic_motor_com.create_dynamic_com_from_analyzer(analyzer)
        if success:
            print("✅ Archivo .COM dinámico generado exitosamente")
        else:
            print("❌ Error generando archivo .COM")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    test_dynamic_com()
