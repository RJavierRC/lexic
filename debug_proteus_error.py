#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test específico para la sintaxis del usuario y diagnóstico de errores de Proteus
"""

import os
import sys

# Agregar el directorio actual al path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from robot_lexical_analyzer import RobotLexicalAnalyzer

def test_user_syntax():
    """Test con la sintaxis exacta del usuario"""
    print("🔍 DIAGNÓSTICO DE ERRORES PROTEUS")
    print("=" * 50)
    
    # Código exacto del usuario
    robot_code = """Robot r1

r1.velocidad = 2       
r1.base = 45           
r1.hombro = 120        
r1.codo = 90           
r1.espera = 1"""
    
    print("📝 Código del usuario:")
    print("-" * 30)
    print(robot_code)
    print("-" * 30)
    
    # Crear analizador
    analyzer = RobotLexicalAnalyzer()
    
    print("\n🔍 Analizando código...")
    
    try:
        tokens, errors = analyzer.analyze(robot_code)
        
        print(f"\n📊 Tokens encontrados: {len(tokens)}")
        for i, token in enumerate(tokens[:10]):  # Mostrar primeros 10 tokens
            print(f"  {i+1:2d}. {token}")
        
        if errors:
            print(f"\n❌ Errores encontrados ({len(errors)}):")
            for i, error in enumerate(errors):
                print(f"  {i+1}. {error}")
        else:
            print("\n✅ Análisis léxico exitoso - sin errores")
        
        # Generar código assembly
        print("\n🔧 Generando código assembly...")
        asm_code, asm_error = analyzer.generate_assembly_code("r1_test")
        
        if asm_code:
            print(f"✅ Assembly generado ({len(asm_code)} caracteres)")
            
            # Mostrar las primeras líneas del assembly
            lines = asm_code.split('\n')
            print("\n📄 Primeras líneas del assembly:")
            for i, line in enumerate(lines[:15]):
                if line.strip():
                    print(f"  {i+1:2d}: {line}")
            
            # Guardar el assembly para inspección
            asm_file = "debug_assembly.asm"
            with open(asm_file, 'w', encoding='ascii', errors='ignore') as f:
                f.write(asm_code)
            print(f"\n💾 Assembly guardado en: {asm_file}")
            
            # Intentar compilar
            print("\n🚀 Intentando compilación...")
            success, result = analyzer.generate_and_compile("r1_test")
            
            if success:
                print("✅ Compilación exitosa!")
                print(result)
            else:
                print("⚠️ Problemas en compilación:")
                print(result)
                
                # Verificar si al menos se generó el ASM
                dosbox_path = os.path.join(os.getcwd(), "DOSBox2", "Tasm")
                asm_path = os.path.join(dosbox_path, "r1_test.asm")
                if os.path.exists(asm_path):
                    print(f"✅ Al menos el archivo ASM fue generado: {asm_path}")
        else:
            print(f"❌ Error generando assembly: {asm_error}")
            
    except Exception as e:
        print(f"❌ Error durante el test: {str(e)}")
        import traceback
        traceback.print_exc()

def analyze_proteus_error():
    """Analiza específicamente el error de Proteus"""
    print("\n" + "=" * 50)
    print("🔍 ANÁLISIS DEL ERROR DE PROTEUS")
    print("=" * 50)
    
    print("""
📋 Error observado en Proteus:
   • "Unknown 1-byte opcode at 0002:0002 62"
   • El programa carga pero no ejecuta correctamente
   • Los motores no se mueven

🔍 Posibles causas:
   1. Código assembly incompatible con el procesador simulado
   2. Instrucciones no soportadas por el entorno 8086/8088
   3. Formato de ejecutable incorrecto
   4. Configuración de puertos incorrecta

💡 Soluciones a implementar:
   1. Generar código más simple y compatible
   2. Usar solo instrucciones básicas 8086
   3. Simplificar la secuencia de control de motores
   4. Verificar configuración del 8255 PPI
""")

def generate_simple_assembly():
    """Genera un assembly muy simple para Proteus"""
    print("\n" + "=" * 50)
    print("🔧 GENERANDO ASSEMBLY SIMPLIFICADO")
    print("=" * 50)
    
    # Assembly muy básico y compatible
    simple_asm = """;Simple motor control for Proteus
;Compatible with 8086/8088
;Controls 3 stepper motors via 8255 PPI

.MODEL SMALL
.STACK 100h

.DATA
    ; No data needed

.CODE
MAIN PROC
    ; Initialize data segment
    MOV AX, @DATA
    MOV DS, AX
    
    ; Configure 8255 - All ports as output
    MOV DX, 0307h    ; Control port of 8255
    MOV AL, 80h      ; Configuration: all outputs
    OUT DX, AL
    
    ; Motor A (Base) - Simple step sequence
    MOV DX, 0300h    ; Port A
    MOV AL, 01h      ; Step 1
    OUT DX, AL
    CALL DELAY
    
    MOV AL, 03h      ; Step 2
    OUT DX, AL
    CALL DELAY
    
    MOV AL, 02h      ; Step 3
    OUT DX, AL
    CALL DELAY
    
    MOV AL, 00h      ; Step 4
    OUT DX, AL
    CALL DELAY
    
    ; Motor B (Shoulder) - Simple step sequence
    MOV DX, 0301h    ; Port B
    MOV AL, 01h      ; Step 1
    OUT DX, AL
    CALL DELAY
    
    MOV AL, 03h      ; Step 2
    OUT DX, AL
    CALL DELAY
    
    ; Motor C (Elbow) - Simple step sequence
    MOV DX, 0302h    ; Port C
    MOV AL, 01h      ; Step 1
    OUT DX, AL
    CALL DELAY
    
    MOV AL, 03h      ; Step 2
    OUT DX, AL
    CALL DELAY
    
    ; Exit program
    MOV AH, 4Ch
    MOV AL, 0
    INT 21h

DELAY PROC
    ; Simple delay loop
    PUSH CX
    MOV CX, 0FFFFh
DELAY_LOOP:
    NOP
    LOOP DELAY_LOOP
    POP CX
    RET
DELAY ENDP

MAIN ENDP
END MAIN
"""
    
    # Guardar el assembly simplificado
    simple_file = "proteus_compatible.asm"
    with open(simple_file, 'w', encoding='ascii', errors='ignore') as f:
        f.write(simple_asm)
    
    print(f"✅ Assembly simplificado generado: {simple_file}")
    print("\n🎯 Características del assembly simplificado:")
    print("  • Usa formato .MODEL SMALL estándar")
    print("  • Solo instrucciones básicas 8086")
    print("  • Configuración correcta del 8255")
    print("  • Direcciones de puerto estándar")
    print("  • Secuencias de pasos simples")
    
    return simple_asm

if __name__ == "__main__":
    # Test del código del usuario
    test_user_syntax()
    
    # Análisis del error de Proteus
    analyze_proteus_error()
    
    # Generar assembly simplificado
    generate_simple_assembly()
    
    print("\n" + "=" * 60)
    print("📋 RECOMENDACIONES PARA PROTEUS")
    print("=" * 60)
    print("""
1. 🔧 Usar el archivo 'proteus_compatible.asm' generado
2. 🎯 Configurar Proteus con:
   • Procesador 8086 o 8088
   • Direcciones de puerto: 0300h-0303h para 8255
   • Conectar motores a puertos A, B, C del 8255
3. 🚀 Cargar el .exe en el procesador virtual
4. ⚡ Verificar que el clock del procesador esté activo
5. 📊 Monitorear las salidas de los puertos durante la simulación
""")
    
    print("\nPresiona Enter para continuar...")
    input()
