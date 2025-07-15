#!/usr/bin/env python3
"""
Test de generación de ejecutable para Proteus con la sintaxis del usuario
"""

from robot_lexical_analyzer import RobotLexicalAnalyzer
import os

def test_user_syntax():
    """Prueba con la sintaxis exacta del usuario"""
    print("🧪 Iniciando test de sintaxis del usuario para Proteus...")
    
    # Crear analizador
    analyzer = RobotLexicalAnalyzer()
    
    # Código del usuario exacto
    user_code = """Robot r1
r1.velocidad = 2
r1.base = 45
r1.hombro = 120
r1.codo = 90
r1.espera = 1"""
    
    print(f"📝 Código a analizar:")
    print(user_code)
    print("=" * 50)
    
    try:
        # Analizar el código
        print("🔍 Analizando código...")
        tokens, errors = analyzer.analyze(user_code)
        
        print(f"✅ Análisis completado:")
        print(f"   • Tokens encontrados: {len(tokens)}")
        print(f"   • Errores: {len(errors)}")
        
        if errors:
            print("\n⚠️ Errores encontrados:")
            for error in errors[:3]:
                print(f"   • {error}")
        
        # Generar y compilar
        print(f"\n⚙️ Generando ejecutable con ProteusAssemblyGenerator...")
        success, message = analyzer.generate_and_compile("r1_user")
        
        if success:
            print(f"✅ ¡COMPILACIÓN EXITOSA!")
            print(f"📁 Archivo generado: r1_user.exe")
            
            # Verificar archivos generados
            tasm_path = os.path.join(os.getcwd(), "DOSBox2", "Tasm")
            exe_path = os.path.join(tasm_path, "r1_user.exe")
            asm_path = os.path.join(tasm_path, "r1_user.asm")
            
            if os.path.exists(exe_path):
                size = os.path.getsize(exe_path)
                print(f"📊 Tamaño del .exe: {size:,} bytes")
            
            if os.path.exists(asm_path):
                print(f"📄 Archivo ASM también generado")
                
                # Mostrar primeras líneas del ASM para verificar formato
                with open(asm_path, 'r', encoding='ascii', errors='ignore') as f:
                    asm_content = f.read()
                    lines = asm_content.split('\n')
                    print(f"\n🔍 Verificando formato ASM (primeras 10 líneas):")
                    for i, line in enumerate(lines[:10]):
                        print(f"   {i+1:2}: {line}")
                    
                    # Verificar que sea formato Proteus (.MODEL SMALL)
                    if ".MODEL SMALL" in asm_content:
                        print(f"✅ Formato correcto: .MODEL SMALL detectado")
                    else:
                        print(f"⚠️ Advertencia: .MODEL SMALL no encontrado")
                        
                    # Verificar direcciones de puerto
                    if "0300h" in asm_content:
                        print(f"✅ Direcciones de puerto Proteus correctas (0300h)")
                    else:
                        print(f"⚠️ Advertencia: direcciones de puerto no encontradas")
            
            print(f"\n🎯 Para usar en Proteus:")
            print(f"   1. Cargar r1_user.exe en el simulador")
            print(f"   2. Configurar 8255 PPI en direcciones 0300h-0303h")
            print(f"   3. Conectar motores a puertos A, B, C")
            print(f"   4. Ejecutar programa")
            print(f"\n🎯 ¡COMPILACIÓN AUTOMÁTICA EXITOSA!")
            
        else:
            print(f"❌ Error en compilación: {message}")
            
    except Exception as e:
        print(f"❌ Error durante la prueba: {str(e)}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    test_user_syntax()
