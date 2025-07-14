#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test de generación de código ASM para motores
Basado en el archivo mycode.asm proporcionado
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from assembly_generator import AssemblyGenerator

def test_motor_asm_generation():
    """Probar la generación de ASM para control de 3 motores"""
    
    print("🔧 Iniciando test de generación ASM para motores...")
    
    try:
        # Crear generador
        generator = AssemblyGenerator()
        
        # En lugar de procesar código robot, llamar directamente al generador completo
        print("🔨 Generando código ASM para control de 3 motores...")
        asm_code = generator.generate_complete_program("motores_robot")
        
        print("\n" + "="*60)
        print("📄 CÓDIGO ASM GENERADO:")
        print("="*60)
        print(asm_code)
        print("="*60)
        
        # Verificar que contiene elementos clave
        required_elements = [
            "DATA_SEG",
            "CODE_SEG", 
            "PORTA",
            "PORTB", 
            "PORTC",
            "CONFIG",
            "MOTOR A",
            "MOTOR B", 
            "MOTOR C",
            "00000110B",
            "00001100B",
            "00001001B",
            "00000011B"
        ]
        
        print("\n🔍 Verificando elementos requeridos:")
        missing = []
        for element in required_elements:
            if element in asm_code:
                print(f"✅ {element}")
            else:
                print(f"❌ {element}")
                missing.append(element)
        
        if missing:
            print(f"\n⚠️ Elementos faltantes: {missing}")
        else:
            print("\n🎉 ¡Todos los elementos requeridos están presentes!")
            
        # Guardar archivo para prueba
        test_file = "test_motors.asm"
        with open(test_file, 'w', encoding='ascii', errors='ignore') as f:
            f.write(asm_code)
        print(f"\n💾 Código guardado en: {test_file}")
        
        return True, asm_code
        
    except Exception as e:
        print(f"❌ Error en test: {e}")
        import traceback
        traceback.print_exc()
        return False, str(e)

if __name__ == "__main__":
    print("🚀 Test de Generación ASM para Control de Motores")
    print("="*50)
    
    success, result = test_motor_asm_generation()
    
    if success:
        print("\n✅ Test completado exitosamente")
    else:
        print(f"\n❌ Test falló: {result}")
        sys.exit(1)
