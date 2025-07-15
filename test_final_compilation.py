#!/usr/bin/env python3
"""
Test final para compilación con DOSBox+TASM mejorado
"""

from robot_lexical_analyzer import RobotLexicalAnalyzer
import os
import time

def test_final_compilation():
    """Prueba final de compilación con diagnósticos"""
    print("🧪 TEST FINAL - Compilación DOSBox+TASM Mejorada")
    print("=" * 60)
    
    # Crear analizador
    analyzer = RobotLexicalAnalyzer()
    
    # Código del usuario exacto
    user_code = """Robot r1
r1.velocidad = 2
r1.base = 45
r1.hombro = 120
r1.codo = 90
r1.espera = 1"""
    
    print(f"📝 Código:")
    print(user_code)
    print("=" * 60)
    
    try:
        # Usar un nombre único con timestamp
        timestamp = str(int(time.time()))
        program_name = f"proteus_test_{timestamp}"
        
        print(f"🔍 Analizando código...")
        tokens, errors = analyzer.analyze(user_code)
        print(f"✅ Tokens: {len(tokens)}, Errores: {len(errors)}")
        
        print(f"\n⚙️ Generando {program_name}.exe...")
        success, message = analyzer.generate_and_compile(program_name)
        
        if success:
            print(f"✅ ¡COMPILACIÓN EXITOSA!")
            print(f"📄 Mensaje: {message}")
            
            # Verificar archivos generados
            tasm_path = os.path.join(os.getcwd(), "DOSBox2", "Tasm")
            exe_path = os.path.join(tasm_path, f"{program_name}.exe")
            asm_path = os.path.join(tasm_path, f"{program_name}.asm")
            obj_path = os.path.join(tasm_path, f"{program_name}.obj")
            
            print(f"\n📊 Verificación de archivos:")
            if os.path.exists(exe_path):
                size = os.path.getsize(exe_path)
                print(f"✅ {program_name}.exe: {size:,} bytes")
            else:
                print(f"❌ {program_name}.exe: NO ENCONTRADO")
                
            if os.path.exists(asm_path):
                size = os.path.getsize(asm_path)
                print(f"✅ {program_name}.asm: {size:,} bytes")
            else:
                print(f"❌ {program_name}.asm: NO ENCONTRADO")
                
            if os.path.exists(obj_path):
                size = os.path.getsize(obj_path)
                print(f"✅ {program_name}.obj: {size:,} bytes")
            else:
                print(f"⚠️ {program_name}.obj: NO ENCONTRADO (normal después de linking)")
                
            print(f"\n🎯 RESULTADO FINAL:")
            print(f"   • Ejecutable: {program_name}.exe LISTO PARA PROTEUS")
            print(f"   • Ubicación: DOSBox2\\Tasm\\")
            print(f"   • Formato: DOS/16-bit compatible")
            print(f"   • Motores: Base(45°), Hombro(120°), Codo(90°)")
            
        else:
            print(f"❌ ERROR: {message}")
            
    except Exception as e:
        print(f"❌ EXCEPCIÓN: {str(e)}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    test_final_compilation()
