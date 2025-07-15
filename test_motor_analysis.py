#!/usr/bin/env python3
"""
Test directo del código de movimiento de motores
"""
import sys
import os

# Agregar el directorio actual al path
sys.path.append(os.getcwd())

from robot_lexical_analyzer import RobotLexicalAnalyzer

def test_motor_movement():
    """Prueba el código de movimiento de motores"""
    
    # Código de prueba
    test_code = """Robot r1

r1.velocidad = 2       
r1.base = 45           
r1.hombro = 120        
r1.codo = 90           
r1.espera = 1"""
    
    print("🤖 ===============================================")
    print("🤖 PRUEBA DE MOVIMIENTO DE MOTORES")
    print("🤖 ===============================================")
    print(f"📝 Código a analizar:")
    print(test_code)
    print("🤖 ===============================================")
    
    # Crear analizador
    analyzer = RobotLexicalAnalyzer()
    
    try:
        # Analizar código
        print("🔍 Analizando código...")
        tokens, errors = analyzer.analyze(test_code)
        
        print(f"\n📊 RESULTADOS DEL ANÁLISIS:")
        print(f"• Tokens encontrados: {len(tokens)}")
        print(f"• Errores encontrados: {len(errors)}")
        
        # Mostrar tokens
        if tokens:
            print(f"\n🎯 TOKENS DETECTADOS:")
            for i, token in enumerate(tokens, 1):
                print(f"{i:2}. {token}")
        
        # Mostrar errores
        if errors:
            print(f"\n❌ ERRORES DETECTADOS:")
            for i, error in enumerate(errors, 1):
                print(f"{i:2}. {error}")
        
        # Generar salida formateada
        print(f"\n📄 SALIDA COMPLETA:")
        print("=" * 50)
        output = analyzer.get_formatted_output()
        print(output)
        print("=" * 50)
        
        # Intentar generar código ensamblador
        print(f"\n⚙️ GENERANDO CÓDIGO ENSAMBLADOR...")
        try:
            asm_code, asm_error = analyzer.generate_assembly_code("test_motor")
            
            if asm_code and not asm_error:
                print(f"✅ Código ensamblador generado exitosamente")
                print(f"\n📋 CÓDIGO ENSAMBLADOR (primeras 20 líneas):")
                lines = asm_code.split('\n')
                for i, line in enumerate(lines[:20], 1):
                    print(f"{i:2}. {line}")
                if len(lines) > 20:
                    print(f"... y {len(lines) - 20} líneas más")
                
                # Verificar si contiene movimientos de motores
                print(f"\n🔍 VERIFICANDO MOVIMIENTOS DE MOTORES:")
                motor_commands = []
                for line in lines:
                    if any(port in line.upper() for port in ['0300', '0301', '0302']):
                        motor_commands.append(line.strip())
                
                if motor_commands:
                    print(f"✅ Se encontraron {len(motor_commands)} comandos de motor:")
                    for cmd in motor_commands:
                        print(f"   • {cmd}")
                else:
                    print(f"❌ NO se encontraron comandos de motor en el código ASM")
                    print(f"   Esto explica por qué no se mueven los motores")
                
            elif asm_error:
                print(f"❌ Error generando ASM: {asm_error}")
            else:
                print(f"❌ No se pudo generar código ensamblador")
                
        except Exception as asm_exception:
            print(f"❌ Excepción generando ASM: {asm_exception}")
        
        # Verificar sintaxis específica
        print(f"\n🔎 VERIFICACIÓN DE SINTAXIS:")
        
        # Verificar declaración de robot
        robot_declared = any('Robot' in str(token) and 'r1' in str(token) for token in tokens)
        print(f"• Robot declarado: {'✅' if robot_declared else '❌'}")
        
        # Verificar asignaciones
        assignments = [token for token in tokens if 'ASSIGNMENT' in str(token) or '=' in str(token)]
        print(f"• Asignaciones encontradas: {len(assignments)}")
        
        # Verificar componentes
        components = ['base', 'hombro', 'codo', 'velocidad', 'espera']
        found_components = []
        for component in components:
            if any(component in str(token) for token in tokens):
                found_components.append(component)
        
        print(f"• Componentes reconocidos: {found_components}")
        
        # Verificar valores numéricos
        numeric_values = [token for token in tokens if 'NUMBER' in str(token) or any(char.isdigit() for char in str(token))]
        print(f"• Valores numéricos: {len(numeric_values)}")
        
        return len(errors) == 0, errors
        
    except Exception as e:
        print(f"❌ Error durante el análisis: {e}")
        import traceback
        traceback.print_exc()
        return False, [str(e)]

if __name__ == "__main__":
    test_motor_movement()
