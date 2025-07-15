#!/usr/bin/env python3
"""
Generador automático para Proteus con el código de motores del usuario
"""
import os
from robot_lexical_analyzer import RobotLexicalAnalyzer

def generate_motor_executable():
    """Genera el ejecutable para el código de motores del usuario"""
    
    # Código del usuario
    user_code = """Robot r1

r1.velocidad = 2       
r1.base = 45           
r1.hombro = 120        
r1.codo = 90           
r1.espera = 1"""
    
    print("🤖 ===============================================")
    print("🤖 GENERANDO EJECUTABLE PARA PROTEUS")
    print("🤖 ===============================================")
    print("📝 Código del usuario:")
    print(user_code)
    print("🤖 ===============================================")
    
    # Crear analizador
    analyzer = RobotLexicalAnalyzer()
    
    try:
        # Analizar código
        print("🔍 Analizando código...")
        tokens, errors = analyzer.analyze(user_code)
        
        if errors:
            print(f"❌ Errores encontrados: {len(errors)}")
            for error in errors:
                print(f"   • {error}")
            return False
        
        print(f"✅ Código válido - {len(tokens)} tokens encontrados")
        
        # Generar ejecutable DOS Real
        print("🎯 Generando ejecutable DOS Real para Proteus...")
        success, message = analyzer.generate_and_compile_dos_real("motor_movement")
        
        if success:
            # Verificar archivo generado
            tasm_path = os.path.join(os.getcwd(), "DOSBox2", "Tasm")
            exe_path = os.path.join(tasm_path, "motor_movement.exe")
            
            if os.path.exists(exe_path):
                file_size = os.path.getsize(exe_path)
                
                print(f"✅ ¡EJECUTABLE GENERADO EXITOSAMENTE!")
                print(f"📁 Archivo: motor_movement.exe")
                print(f"📂 Ubicación: {exe_path}")
                print(f"📏 Tamaño: {file_size} bytes")
                
                # Verificar header MZ
                with open(exe_path, 'rb') as f:
                    header = f.read(2)
                    if header == b'MZ':
                        print(f"✅ Header MZ válido - MS-DOS ejecutable auténtico")
                    else:
                        print(f"⚠️ Header: {header} (esperado: MZ)")
                
                print(f"\n🎯 CONFIGURACIÓN PROTEUS REQUERIDA:")
                print(f"=" * 50)
                print(f"1. 🖥️  PROCESADOR: 8086 (NO 8088, NO x86)")
                print(f"   • Modelo: 8086 Real Mode")
                print(f"   • Frecuencia: 4.77MHz (estándar)")
                print(f"   • Configuración: Real Mode")
                print(f"\n2. 🔌 8255 PPI (Programmable Peripheral Interface):")
                print(f"   • Dirección base: 0300h")
                print(f"   • Puerto A (PA): 0300h → Control Base")
                print(f"   • Puerto B (PB): 0301h → Control Hombro")
                print(f"   • Puerto C (PC): 0302h → Control Codo")
                print(f"   • Control: 0303h → Configuración")
                print(f"\n3. 🤖 MOTORES PASO A PASO:")
                print(f"   • 3 motores conectados vía ULN2003A")
                print(f"   • Base: ULN2003A conectado a PA (0300h)")
                print(f"   • Hombro: ULN2003A conectado a PB (0301h)")
                print(f"   • Codo: ULN2003A conectado a PC (0302h)")
                print(f"\n4. 📂 CARGAR PROGRAMA:")
                print(f"   • Archivo: motor_movement.exe")
                print(f"   • Formato: MS-DOS executable")
                print(f"   • Cargar en: 8086 processor")
                print(f"\n5. ⚡ SECUENCIA DE MOVIMIENTOS ESPERADA:")
                print(f"   • Configurar velocidad a 2")
                print(f"   • Mover base a 45°")
                print(f"   • Mover hombro a 120°")
                print(f"   • Mover codo a 90°")
                print(f"   • Esperar 1 segundo")
                print(f"=" * 50)
                
                # Mostrar código ASM relevante
                print(f"\n📋 VERIFICANDO COMANDOS DE MOTOR EN ASM:")
                asm_code, _ = analyzer.generate_assembly_code("motor_movement")
                if asm_code:
                    motor_lines = []
                    lines = asm_code.split('\n')
                    for i, line in enumerate(lines):
                        if any(port in line.upper() for port in ['0300', '0301', '0302', 'OUT DX']):
                            motor_lines.append(f"   {i+1:3}. {line.strip()}")
                    
                    if motor_lines:
                        print(f"✅ Comandos de motor encontrados en ASM:")
                        for cmd in motor_lines[:10]:  # Mostrar primeros 10
                            print(cmd)
                        if len(motor_lines) > 10:
                            print(f"   ... y {len(motor_lines) - 10} comandos más")
                    else:
                        print(f"⚠️ No se encontraron comandos OUT DX en el ASM")
                
                return True
            else:
                print(f"❌ Archivo no encontrado: {exe_path}")
                return False
        else:
            print(f"❌ Error generando ejecutable: {message}")
            return False
            
    except Exception as e:
        print(f"❌ Error durante la generación: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    generate_motor_executable()
