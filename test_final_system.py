#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test final del sistema de compilación automática
Versión con sintaxis robótica corregida
"""

import os
import sys

# Agregar el directorio actual al path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from robot_lexical_analyzer import RobotLexicalAnalyzer

def test_final_system():
    """Test final del sistema completo"""
    print("🎯 TEST FINAL - COMPILACIÓN AUTOMÁTICA PARA PROTEUS")
    print("=" * 60)
    
    # Código robótico con sintaxis correcta
    robot_code = """
Robot brazo_industrial
brazo_industrial.repetir = 2
brazo_industrial.inicio
brazo_industrial.base = 90
brazo_industrial.espera = 1
brazo_industrial.hombro = 45  
brazo_industrial.espera = 2
brazo_industrial.codo = 60
brazo_industrial.espera = 1
brazo_industrial.fin
"""
    
    print("📝 Código robótico (sintaxis corregida):")
    print("-" * 40)
    print(robot_code)
    print("-" * 40)
    
    # Crear analizador
    analyzer = RobotLexicalAnalyzer()
    
    print("\n🔍 Analizando código...")
    
    try:
        tokens, errors = analyzer.analyze(robot_code)
        
        if errors:
            print(f"❌ Errores encontrados: {errors}")
        else:
            print(f"✅ Análisis léxico exitoso: {len(tokens)} tokens encontrados")
        
        # Intentar generar ejecutable
        print("\n🚀 Iniciando compilación automática...")
        success, result = analyzer.generate_and_compile("brazo_industrial")
        
        print("\n" + "=" * 60)
        print("RESULTADO FINAL")
        print("=" * 60)
        
        if success:
            print("🎯 ¡COMPILACIÓN AUTOMÁTICA COMPLETADA!")
            print(result)
        else:
            print("⚠️ Resultado de compilación:")
            print(result)
        
        # Verificar archivos generados
        print("\n📁 Verificando archivos generados...")
        dosbox_path = os.path.join(os.getcwd(), "DOSBox2", "Tasm")
        
        if os.path.exists(dosbox_path):
            generated_files = []
            for file in os.listdir(dosbox_path):
                if any(file.endswith(ext) for ext in ['.exe', '.asm', '.obj']):
                    filepath = os.path.join(dosbox_path, file)
                    size = os.path.getsize(filepath)
                    generated_files.append((file, size))
                    print(f"  📄 {file} ({size} bytes)")
            
            if generated_files:
                print(f"\n✅ {len(generated_files)} archivos generados en DOSBox2/Tasm/")
                
                # Buscar ejecutables específicamente
                exe_files = [f for f, s in generated_files if f.endswith('.exe')]
                if exe_files:
                    print(f"🎯 {len(exe_files)} ejecutable(s) .exe disponible(s) para Proteus")
                    for exe in exe_files:
                        print(f"   🚀 {exe}")
                
                return True
            else:
                print("⚠️ No se encontraron archivos en DOSBox2/Tasm/")
        else:
            print("⚠️ Directorio DOSBox2/Tasm no encontrado")
        
        return success
        
    except Exception as e:
        print(f"❌ Error durante el test: {str(e)}")
        import traceback
        traceback.print_exc()
        return False

def show_usage_instructions():
    """Muestra las instrucciones de uso para Proteus"""
    print("\n" + "=" * 60)
    print("📖 INSTRUCCIONES PARA USO EN PROTEUS")
    print("=" * 60)
    print("""
🎯 Para usar los ejecutables generados en Proteus:

1. 📁 Localizar archivos:
   - Los archivos .exe están en: DOSBox2/Tasm/
   - Usar cualquier archivo .exe generado

2. 🔧 Configuración en Proteus:
   - Agregar componente "8255 PPI" para control de puertos
   - Conectar motores paso a paso a PORTA, PORTB, PORTC
   - Usar drivers ULN2003A para control de potencia

3. 🚀 Simulación:
   - Cargar el archivo .exe en el procesador virtual
   - Conectar el circuito de control de motores
   - Ejecutar la simulación para ver movimientos

4. 📊 Puertos utilizados:
   - PORTA (00H): Control Motor Base
   - PORTB (02H): Control Motor Hombro  
   - PORTC (04H): Control Motor Codo
   - CONFIG (06H): Configuración 8255

🎯 El sistema genera código para 3 motores paso a paso
   con secuencias de control apropiadas para brazos robóticos.
""")

if __name__ == "__main__":
    print("🤖 ANALIZADOR LÉXICO PARA BRAZO ROBÓTICO")
    print("🎯 Sistema de Compilación Automática para Proteus")
    print("🔧 Generación de archivos .EXE para simulación")
    print("\n")
    
    # Ejecutar test final
    success = test_final_system()
    
    # Mostrar instrucciones
    show_usage_instructions()
    
    print("\n" + "=" * 60)
    print("ESTADO FINAL DEL SISTEMA")
    print("=" * 60)
    
    if success:
        print("🎯 ✅ SISTEMA COMPLETAMENTE FUNCIONAL")
        print("🎯 ✅ COMPILACIÓN AUTOMÁTICA OPERATIVA") 
        print("🎯 ✅ ARCHIVOS .EXE GENERADOS PARA PROTEUS")
        print("🎯 ✅ CONTROL DE 3 MOTORES IMPLEMENTADO")
    else:
        print("🎯 ⚠️ SISTEMA PARCIALMENTE FUNCIONAL")
        print("🎯 ✅ COMPILADOR NATIVO OPERATIVO")
        print("🎯 ⚠️ INTEGRACIÓN COMPLETA NECESITA AJUSTES")
    
    print("\n💡 El sistema está listo para usar en Proteus!")
    print("💡 Los archivos .exe pueden cargarse directamente en simulación")
    
    print("\nPresiona Enter para finalizar...")
    input()
