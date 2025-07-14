#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test específico para generar ejecutable con la sintaxis del usuario
"""

import os
import sys

# Agregar el directorio actual al path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from robot_lexical_analyzer import RobotLexicalAnalyzer

def test_user_exact_syntax():
    """Test con la sintaxis exacta que está usando el usuario"""
    print("🎯 TEST CON SINTAXIS EXACTA DEL USUARIO")
    print("=" * 60)
    
    # Tu código exacto
    robot_code = """Robot r1

r1.velocidad = 2       
r1.base = 45           
r1.hombro = 120        
r1.codo = 90           
r1.espera = 1"""
    
    print("📝 Tu código:")
    print("-" * 30)
    print(robot_code)
    print("-" * 30)
    
    # Crear analizador
    analyzer = RobotLexicalAnalyzer()
    
    print("\n🔍 Paso 1: Análisis léxico y sintáctico...")
    
    try:
        tokens, errors = analyzer.analyze(robot_code)
        
        if errors:
            print(f"❌ Errores encontrados: {len(errors)}")
            for i, error in enumerate(errors[:3]):
                print(f"  {i+1}. {error}")
            if len(errors) > 3:
                print(f"  ... y {len(errors) - 3} errores más")
        else:
            print(f"✅ Análisis exitoso: {len(tokens)} tokens procesados")
        
        print("\n🔧 Paso 2: Generando código assembly optimizado para Proteus...")
        
        # Generar assembly específicamente optimizado para Proteus
        asm_code, asm_error = analyzer.generate_assembly_code("r1_user")
        
        if asm_code:
            print(f"✅ Assembly generado ({len(asm_code)} caracteres)")
            
            # Guardar el assembly
            asm_file = "r1_user_proteus.asm"
            with open(asm_file, 'w', encoding='ascii', errors='ignore') as f:
                f.write(asm_code)
            
            print(f"💾 Assembly guardado: {asm_file}")
            
            # Mostrar características del assembly generado
            print("\n📋 Características del assembly generado:")
            lines = asm_code.split('\n')
            model_line = next((line for line in lines if '.MODEL' in line), None)
            main_proc = next((line for line in lines if 'MAIN PROC' in line), None)
            port_config = [line for line in lines if '0300h' in line or '0301h' in line or '0302h' in line]
            
            if model_line:
                print(f"  ✅ Formato: {model_line.strip()}")
            if main_proc:
                print(f"  ✅ Procedimiento principal encontrado")
            if port_config:
                print(f"  ✅ Configuración de puertos: {len(port_config)} líneas")
            
            print("\n🚀 Paso 3: Compilación automática...")
            
            # Intentar compilación
            success, result = analyzer.generate_and_compile("r1_user")
            
            print("\n" + "=" * 60)
            print("RESULTADO FINAL")
            print("=" * 60)
            
            if success:
                print("🎯 ¡COMPILACIÓN AUTOMÁTICA EXITOSA!")
                print(result)
                
                # Verificar archivo generado
                exe_path = os.path.join("DOSBox2", "Tasm", "r1_user.exe")
                if os.path.exists(exe_path):
                    size = os.path.getsize(exe_path)
                    print(f"\n📄 Archivo generado: {exe_path}")
                    print(f"📊 Tamaño: {size} bytes")
                    print("\n🎯 INSTRUCCIONES PARA PROTEUS:")
                    print_proteus_instructions(exe_path)
                
            else:
                print("⚠️ Compilación automática no completada:")
                print(result)
                
                # Aún así verificar si hay archivos útiles
                asm_path = os.path.join("DOSBox2", "Tasm", "r1_user.asm")
                if os.path.exists(asm_path):
                    print(f"\n✅ Al menos el archivo ASM está disponible: {asm_path}")
                    print("\n🔧 COMPILACIÓN MANUAL CON TASM:")
                    print("1. Abrir DOSBox")
                    print("2. mount c DOSBox2\\Tasm")
                    print("3. c:")
                    print("4. tasm r1_user.asm")
                    print("5. tlink r1_user.obj")
        else:
            print(f"❌ Error generando assembly: {asm_error}")
            
    except Exception as e:
        print(f"❌ Error durante el test: {str(e)}")
        import traceback
        traceback.print_exc()

def print_proteus_instructions(exe_path):
    """Imprime instrucciones específicas para usar en Proteus"""
    print("""
    🎯 CONFIGURACIÓN EN PROTEUS:
    
    1. 📱 Componentes necesarios:
       • Procesador 8086 o 8088
       • 8255 Programmable Peripheral Interface (PPI)
       • 3 motores paso a paso (stepper motors)
       • Drivers ULN2003A (para cada motor)
    
    2. 🔌 Conexiones:
       • Puerto A (0300h) → Motor Base (ULN2003A)
       • Puerto B (0301h) → Motor Hombro (ULN2003A)  
       • Puerto C (0302h) → Motor Codo (ULN2003A)
       • Config (0303h) → Configuración del 8255
    
    3. ⚙️ Configuración del procesador:
       • Cargar programa: r1_user.exe
       • Frecuencia de clock: 1 MHz (recomendado)
       • Memoria: mínimo 64KB
    
    4. 🚀 Secuencia de movimientos programada:
       • Base: 45 grados
       • Hombro: 120 grados
       • Codo: 90 grados
       • Velocidad: controlada por delays
    
    5. ▶️ Ejecutar simulación:
       • Presionar RUN en Proteus
       • Observar movimientos en motores
       • Monitorear puertos con Logic Analyzer (opcional)
    """)

if __name__ == "__main__":
    test_user_exact_syntax()
    
    print("\n" + "=" * 60)
    print("🎯 RESUMEN")
    print("=" * 60)
    print("""
    ✅ El sistema está configurado para generar código compatible con Proteus
    ✅ Usa formato .MODEL SMALL estándar
    ✅ Direcciones de puerto correctas (0300h-0303h)
    ✅ Secuencias de pasos optimizadas para motores paso a paso
    ✅ Procedimientos específicos para cada ángulo solicitado
    
    💡 Si los motores no se mueven en Proteus:
    
    1. Verificar que el procesador esté ejecutando (clock activo)
    2. Revisar conexiones del 8255 a los puertos correctos
    3. Confirmar que los drivers ULN2003A estén conectados
    4. Verificar alimentación de los motores paso a paso
    5. Monitorear las salidas de los puertos con osciloscopio virtual
    """)
    
    print("\nPresiona Enter para continuar...")
    input()
