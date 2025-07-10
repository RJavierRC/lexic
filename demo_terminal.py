#!/usr/bin/env python3
"""
Versión simplificada para probar el generador de .asm desde terminal
"""

from robot_lexical_analyzer import RobotLexicalAnalyzer

def main():
    print("🤖 GENERADOR DE CÓDIGO ENSAMBLADOR - VERSIÓN TERMINAL")
    print("=" * 60)
    
    # Código de ejemplo
    codigo_ejemplo = """Robot r1
r1.repetir = 2
r1.inicio
r1.base = 90
r1.hombro = 45
r1.espera = 1
r1.fin"""
    
    print("📝 Código fuente:")
    for i, line in enumerate(codigo_ejemplo.split('\n'), 1):
        print(f"  {i}. {line}")
    
    # Analizar
    print("\n🔍 Analizando código...")
    analyzer = RobotLexicalAnalyzer()
    tokens, errors = analyzer.analyze(codigo_ejemplo)
    
    if errors:
        print(f"❌ Errores encontrados: {errors}")
        return
    
    print(f"✅ Análisis exitoso: {len(tokens)} tokens")
    
    # Generar código ensamblador
    print("\n🔧 Generando código ensamblador...")
    asm_code, error = analyzer.generate_assembly_code("demo_robot")
    
    if error:
        print(f"❌ Error: {error}")
        return
    
    print("✅ Código ensamblador generado")
    
    # Guardar archivo
    asm_file = "/home/xavier/lexic/DOSBox2/Tasm/demo_robot.asm"
    with open(asm_file, 'w', encoding='utf-8') as f:
        f.write(asm_code)
    
    print(f"\n📁 Archivo guardado: {asm_file}")
    
    # Mostrar resumen del código
    lines = asm_code.split('\n')
    print(f"📊 Líneas de código: {len(lines)}")
    print(f"📊 Tamaño: {len(asm_code)} caracteres")
    
    print("\n🎯 SIGUIENTE PASO:")
    print("• En Ubuntu: El archivo .asm está listo")
    print("• En Windows: Copia el proyecto y ejecuta 'Generar .EXE' para obtener el .exe")
    print("• Para Proteus: Usa el archivo .exe generado en Windows")
    
    print("\n📄 VISTA PREVIA DEL CÓDIGO GENERADO (primeras 20 líneas):")
    print("-" * 50)
    for i, line in enumerate(lines[:20], 1):
        print(f"{i:2}: {line}")
    if len(lines) > 20:
        print(f"... ({len(lines)} líneas totales)")
    print("-" * 50)

if __name__ == "__main__":
    main()
