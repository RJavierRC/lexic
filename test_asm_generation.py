#!/usr/bin/env python3
"""
Prueba específica de generación de código ensamblador
"""

from robot_lexical_analyzer import RobotLexicalAnalyzer

def main():
    print("🔧 PRUEBA DE GENERACIÓN DE CÓDIGO ENSAMBLADOR")
    print("=" * 60)
    
    # Código simple para probar
    codigo = """Robot r1
r1.base = 90
r1.hombro = 45
r1.espera = 2"""
    
    print("📝 Código fuente:")
    for i, line in enumerate(codigo.split('\n'), 1):
        print(f"  {i}. {line}")
    
    # Analizar
    analyzer = RobotLexicalAnalyzer()
    tokens, errors = analyzer.analyze(codigo)
    
    if errors:
        print(f"❌ Errores: {errors}")
        return
    
    print(f"✅ Análisis exitoso: {len(tokens)} tokens")
    
    # Verificar que el método existe
    if hasattr(analyzer, 'generate_assembly_code'):
        print("✅ Método generate_assembly_code disponible")
        
        # Generar código ensamblador
        asm_code, error = analyzer.generate_assembly_code("test_simple")
        
        if error:
            print(f"❌ Error generando ensamblador: {error}")
        else:
            print("✅ Código ensamblador generado exitosamente")
            print("\n📄 CÓDIGO ENSAMBLADOR:")
            print("-" * 40)
            print(asm_code)
            print("-" * 40)
            
            # Compilar
            success, message = analyzer.compile_to_executable(asm_code, "test_simple")
            
            if success:
                print(f"✅ Compilación exitosa: {message}")
            else:
                print(f"❌ Error en compilación: {message}")
    else:
        print("❌ Método generate_assembly_code NO disponible")
        print("Métodos disponibles:")
        methods = [m for m in dir(analyzer) if not m.startswith('_') and callable(getattr(analyzer, m))]
        for method in methods:
            print(f"  - {method}")

if __name__ == "__main__":
    main()
