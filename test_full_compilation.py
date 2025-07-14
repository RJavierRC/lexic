#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test de compilación ASM con TASM usando DOSBox
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from assembly_generator import AssemblyGenerator, DOSBoxController

def test_full_compilation():
    """Probar generación completa ASM -> TASM -> EXE"""
    
    print("🚀 Test de Compilación Completa: ASM → TASM → EXE")
    print("="*55)
    
    try:
        # 1. Generar código ASM
        print("🔧 Paso 1: Generando código ASM...")
        generator = AssemblyGenerator()
        asm_code = generator.generate_complete_program("robot_motors")
        
        print("✅ Código ASM generado exitosamente")
        
        # 2. Inicializar controlador DOSBox
        print("\n🔧 Paso 2: Inicializando DOSBox...")
        controller = DOSBoxController()
        
        # 3. Compilar con TASM
        print("🔧 Paso 3: Compilando con TASM...")
        success, message = controller.compile_assembly(asm_code, "robot_motors")
        
        if success:
            print("✅ Compilación exitosa!")
            print(f"📄 Resultado: {message}")
            
            # 4. Verificar archivos generados
            print("\n🔧 Paso 4: Verificando archivos generados...")
            files = controller.get_generated_files()
            
            if files:
                print("📁 Archivos generados:")
                for file in files:
                    print(f"  ✅ {file}")
            else:
                print("⚠️ No se encontraron archivos generados")
                
        else:
            print(f"❌ Error en compilación: {message}")
            return False
            
        return True
        
    except Exception as e:
        print(f"❌ Error en test completo: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    print("🚀 Test de Compilación Completa")
    print("="*40)
    
    success = test_full_compilation()
    
    if success:
        print("\n✅ Test completo exitoso - ¡Robot ASM/EXE generado!")
    else:
        print("\n❌ Test falló")
        sys.exit(1)
