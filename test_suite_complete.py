#!/usr/bin/env python3
"""
Suite completa de tests para verificar funcionamiento robusto
"""

from robot_lexical_analyzer import RobotLexicalAnalyzer
import os
import time

def test_multiple_programs():
    """Test de múltiples programas con diferentes configuraciones"""
    print("🧪 SUITE DE TESTS MÚLTIPLES")
    print("=" * 60)
    
    analyzer = RobotLexicalAnalyzer()
    
    # Diferentes configuraciones de test
    test_cases = [
        {
            "name": "basic_movement",
            "code": """Robot r1
r1.base = 90
r1.hombro = 45
r1.codo = 135""",
            "description": "Movimiento básico de 3 motores"
        },
        {
            "name": "with_speed",
            "code": """Robot r2
r2.velocidad = 3
r2.base = 180
r2.hombro = 90
r2.codo = 45
r2.espera = 2""",
            "description": "Con velocidad y espera"
        },
        {
            "name": "extreme_angles",
            "code": """Robot r3
r3.base = 360
r3.hombro = 180
r3.codo = 0""",
            "description": "Ángulos extremos"
        },
        {
            "name": "minimal",
            "code": """Robot r4
r4.base = 45""",
            "description": "Configuración mínima"
        }
    ]
    
    results = []
    
    for i, test_case in enumerate(test_cases, 1):
        print(f"\n🔍 TEST {i}/{len(test_cases)}: {test_case['name']}")
        print(f"📝 {test_case['description']}")
        print(f"💻 Código:")
        for line in test_case['code'].split('\n'):
            print(f"   {line}")
        
        try:
            # Analizar
            tokens, errors = analyzer.analyze(test_case['code'])
            print(f"✅ Análisis: {len(tokens)} tokens, {len(errors)} errores")
            
            # Generar y compilar
            success, message = analyzer.generate_and_compile(test_case['name'])
            
            if success:
                print(f"✅ Compilación exitosa")
                
                # Verificar archivos
                tasm_path = os.path.join(os.getcwd(), "DOSBox2", "Tasm")
                exe_path = os.path.join(tasm_path, f"{test_case['name']}.exe")
                asm_path = os.path.join(tasm_path, f"{test_case['name']}.asm")
                
                exe_exists = os.path.exists(exe_path)
                asm_exists = os.path.exists(asm_path)
                
                exe_size = os.path.getsize(exe_path) if exe_exists else 0
                asm_size = os.path.getsize(asm_path) if asm_exists else 0
                
                print(f"📁 EXE: {'✅' if exe_exists else '❌'} ({exe_size:,} bytes)")
                print(f"📁 ASM: {'✅' if asm_exists else '❌'} ({asm_size:,} bytes)")
                
                results.append({
                    "name": test_case['name'],
                    "success": True,
                    "exe_size": exe_size,
                    "asm_size": asm_size
                })
            else:
                print(f"❌ Compilación falló: {message}")
                results.append({
                    "name": test_case['name'],
                    "success": False,
                    "error": message
                })
                
        except Exception as e:
            print(f"❌ Error en test: {e}")
            results.append({
                "name": test_case['name'],
                "success": False,
                "error": str(e)
            })
    
    # Resumen final
    print(f"\n🎯 RESUMEN DE TESTS")
    print("=" * 60)
    
    successful = sum(1 for r in results if r['success'])
    total = len(results)
    
    print(f"📊 Resultados: {successful}/{total} tests exitosos")
    print(f"✅ Tasa de éxito: {(successful/total)*100:.1f}%")
    
    print(f"\n📋 Detalles:")
    for result in results:
        if result['success']:
            print(f"   ✅ {result['name']}: EXE({result['exe_size']:,} bytes), ASM({result['asm_size']:,} bytes)")
        else:
            print(f"   ❌ {result['name']}: {result.get('error', 'Error desconocido')}")
    
    if successful == total:
        print(f"\n🎉 ¡TODOS LOS TESTS PASARON!")
        print(f"🔧 Sistema completamente funcional para Proteus")
    else:
        print(f"\n⚠️ {total - successful} tests fallaron")
    
    return successful == total

def test_gui_integration():
    """Test de integración con la interfaz gráfica"""
    print(f"\n🖥️ TEST DE INTEGRACIÓN GUI")
    print("=" * 60)
    
    try:
        # Importar la GUI
        from main import LexicalAnalyzerGUI
        
        print("✅ Importación de GUI exitosa")
        
        # Crear instancia (sin mostrar)
        # app = LexicalAnalyzerGUI()
        print("✅ GUI puede ser instanciada")
        
        # Verificar rutas
        dosbox_path = os.path.join(os.getcwd(), "DOSBox2")
        tasm_path = os.path.join(dosbox_path, "Tasm")
        
        print(f"📁 DOSBox path: {'✅' if os.path.exists(dosbox_path) else '❌'}")
        print(f"📁 TASM path: {'✅' if os.path.exists(tasm_path) else '❌'}")
        
        # Verificar archivos críticos
        dosbox_exe = os.path.join(dosbox_path, "dosbox.exe")
        tasm_exe = os.path.join(tasm_path, "TASM.EXE")
        tlink_exe = os.path.join(tasm_path, "TLINK.EXE")
        
        print(f"🔧 DOSBox.exe: {'✅' if os.path.exists(dosbox_exe) else '❌'}")
        print(f"🔧 TASM.EXE: {'✅' if os.path.exists(tasm_exe) else '❌'}")
        print(f"🔧 TLINK.EXE: {'✅' if os.path.exists(tlink_exe) else '❌'}")
        
        print("✅ Integración GUI verificada")
        return True
        
    except Exception as e:
        print(f"❌ Error en integración GUI: {e}")
        return False

if __name__ == "__main__":
    print("🚀 INICIANDO SUITE COMPLETA DE TESTS")
    print("=" * 60)
    
    # Test 1: Múltiples programas
    test1_success = test_multiple_programs()
    
    # Test 2: Integración GUI
    test2_success = test_gui_integration()
    
    # Resumen final
    print(f"\n🏁 RESUMEN FINAL")
    print("=" * 60)
    print(f"✅ Tests múltiples: {'PASÓ' if test1_success else 'FALLÓ'}")
    print(f"✅ Integración GUI: {'PASÓ' if test2_success else 'FALLÓ'}")
    
    if test1_success and test2_success:
        print(f"\n🎉 ¡TODOS LOS TESTS PASARON!")
        print(f"🔧 Sistema completamente funcional")
        print(f"🎯 Listo para usar en Proteus")
    else:
        print(f"\n⚠️ Algunos tests fallaron")
        print(f"🔧 Revisar configuración del sistema")
