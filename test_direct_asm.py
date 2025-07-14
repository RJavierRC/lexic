#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test directo para generar ASM sin pasar por todo el pipeline
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from assembly_generator import AssemblyGenerator

def test_direct_asm_generation():
    """Test directo de generación ASM para verificar que funciona"""
    
    print("🔧 Test Directo de Generación ASM")
    print("="*40)
    
    try:
        # Crear generador directamente
        generator = AssemblyGenerator()
        
        # Generar código ASM para 3 motores
        print("🔨 Generando ASM para control de 3 motores...")
        asm_code = generator.generate_complete_program("test_directo")
        
        print("✅ ASM generado exitosamente")
        print(f"📏 Tamaño: {len(asm_code)} caracteres")
        
        # Guardar en archivo
        output_file = os.path.join("DOSBox2", "Tasm", "test_directo.asm")
        os.makedirs(os.path.dirname(output_file), exist_ok=True)
        
        with open(output_file, 'w', encoding='ascii', errors='ignore') as f:
            f.write(asm_code)
        
        print(f"💾 Archivo guardado: {output_file}")
        
        # Mostrar preview del código
        print("\n📄 Preview del código ASM:")
        print("-" * 50)
        lines = asm_code.split('\n')
        for i, line in enumerate(lines[:20]):  # Primeras 20 líneas
            print(f"{i+1:2d}: {line}")
        if len(lines) > 20:
            print(f"... y {len(lines) - 20} líneas más")
        print("-" * 50)
        
        # Verificar elementos clave
        required_elements = ["PORTA", "PORTB", "PORTC", "Config", "DATA_SEG", "CODE_SEG", "START"]
        missing = []
        for element in required_elements:
            if element not in asm_code:
                missing.append(element)
        
        if missing:
            print(f"⚠️ Elementos faltantes: {missing}")
            return False
        else:
            print("✅ Todos los elementos requeridos presentes")
            return True
            
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    success = test_direct_asm_generation()
    
    if success:
        print("\n🎉 Test exitoso - ASM generado correctamente")
        print("📝 Ahora puedes probar compilación manual en DOSBox:")
        print("   1. cd DOSBox2")
        print("   2. dosbox.exe")
        print("   3. mount c Tasm")
        print("   4. c:")
        print("   5. tasm test_directo.asm")
        print("   6. tlink test_directo.obj")
    else:
        print("\n❌ Test falló")
        sys.exit(1)
