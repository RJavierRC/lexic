#!/usr/bin/env python3
"""
Debug específico para problemas de ejecución de motores
- Debug paso a paso de las condiciones de ejecución
- Verificación del orden y timing
- Corrección de la lógica de velocidades
"""

import os
import time

def create_dynamic_motor_com(analyzer):
    """
    Crea motor_user.com con DEBUG específico de ejecución
    """
    try:
        tasm_dir = os.path.join("DOSBox2", "Tasm")
        os.makedirs(tasm_dir, exist_ok=True)
        
        motor_values = extract_motor_values_enhanced(analyzer)
        
        print("🔍 === DEBUG DE EJECUCIÓN ESPECÍFICO ===")
        debug_execution_logic(motor_values)
        
        machine_code = generate_dynamic_machine_code(motor_values)
        
        com_path = os.path.join(tasm_dir, "motor_user.com")
        with open(com_path, 'wb') as f:
            f.write(bytes(machine_code))
        
        file_size = len(machine_code)
        print(f"\n✅ motor_user.com creado! Tamaño: {file_size} bytes")
        
        return True, motor_values
        
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()
        return False, {}

def debug_execution_logic(motor_values):
    """
    Debug específico de la lógica de ejecución
    """
    print("\n🔍 === ANÁLISIS DE LÓGICA DE EJECUCIÓN ===")
    
    movimientos = motor_values.get('movimientos', [])
    velocidad_actual = 1.0
    posiciones = {'base': 0, 'hombro': 0, 'codo': 0}
    velocidades_asignadas = {}
    
    print("📋 SECUENCIA PASO A PASO:")
    
    for i, mov in enumerate(movimientos):
        tipo = mov['tipo']
        valor = mov['valor']
        
        print(f"\n• Paso {i+1}: {mov}")
        
        if tipo == 'velocidad':
            velocidad_actual = valor
            print(f"  └─ Velocidad actualizada: {velocidad_actual}s")
            
        elif tipo in ['base', 'hombro', 'codo']:
            motor = tipo
            pos_actual = posiciones[motor]
            
            print(f"  └─ Motor: {motor}")
            print(f"      • Valor solicitado: {valor}°")
            print(f"      • Posición actual: {pos_actual}°")
            print(f"      • Velocidad actual: {velocidad_actual}s")
            
            # Verificar condiciones de IDA
            condicion_ida = valor > 0 and pos_actual == 0
            print(f"      • Condición IDA (valor > 0 AND pos_actual == 0): {condicion_ida}")
            print(f"        - valor > 0: {valor > 0}")
            print(f"        - pos_actual == 0: {pos_actual == 0}")
            
            if condicion_ida:
                print(f"      ✅ SE EJECUTARÁ IDA")
                velocidades_asignadas[motor] = velocidad_actual
                posiciones[motor] = valor
            else:
                print(f"      ❌ NO SE EJECUTARÁ IDA")
            
            # Verificar condiciones de REGRESO
            condicion_regreso = valor == 0 and pos_actual > 0
            print(f"      • Condición REGRESO (valor == 0 AND pos_actual > 0): {condicion_regreso}")
            print(f"        - valor == 0: {valor == 0}")
            print(f"        - pos_actual > 0: {pos_actual > 0}")
            
            if condicion_regreso:
                print(f"      ✅ SE EJECUTARÁ REGRESO")
            elif valor == 0:
                print(f"      ⚠️  REGRESO SOLICITADO PERO pos_actual = {pos_actual}")
    
    print(f"\n📊 RESUMEN DE EJECUCIÓN:")
    print(f"• Motores que harán IDA: {list(velocidades_asignadas.keys())}")
    print(f"• Velocidades asignadas: {velocidades_asignadas}")
    print(f"• Posiciones finales después de IDA: {posiciones}")
    
    # Simular secuencia de regreso
    print(f"\n🔙 ANÁLISIS DE REGRESO:")
    motores_regreso = []
    for mov in movimientos:
        if mov['tipo'] in ['base', 'hombro', 'codo'] and mov['valor'] == 0:
            motor = mov['tipo']
            if posiciones[motor] > 0:
                motores_regreso.append(motor)
                print(f"• {motor}: {posiciones[motor]}° → 0° (REGRESO)")
    
    print(f"• Orden de regreso: {list(reversed(list(velocidades_asignadas.keys())))}")

def extract_motor_values_enhanced(analyzer):
    """Extracción con debug mínimo"""
    try:
        raw_code = getattr(analyzer, 'raw_code', '') or getattr(analyzer, 'code', '')
        
        if raw_code:
            return parse_robot_syntax_complete(raw_code)
        else:
            return extract_motor_values_original(analyzer)
        
    except Exception as e:
        print(f"❌ Error en extracción: {e}")
        return {
            'movimientos': [
                {'tipo': 'velocidad', 'valor': 2.0},
                {'tipo': 'base', 'valor': 45},
                {'tipo': 'velocidad', 'valor': 1.5},
                {'tipo': 'hombro', 'valor': 120},
                {'tipo': 'velocidad', 'valor': 3.0},
                {'tipo': 'codo', 'valor': 90},
                {'tipo': 'base', 'valor': 0},
                {'tipo': 'hombro', 'valor': 0},
                {'tipo': 'codo', 'valor': 0}
            ],
            'repeticiones': 1
        }

def parse_robot_syntax_complete(code):
    """Parser básico"""
    movimientos = []
    repeticiones = 1
    variables = {}
    
    lines = code.strip().split('\n')
    
    # Variables
    for line in lines:
        line = line.strip()
        if '=' in line and not ('.' in line):
            try:
                var_name = line.split('=')[0].strip()
                var_value = float(line.split('=')[1].strip())
                variables[var_name] = var_value
            except:
                pass
    
    # Comandos
    for line in lines:
        line = line.strip()
        if not line or line.startswith('#') or line.startswith('Robot') or line.endswith('.inicio') or line.endswith('.fin'):
            continue
            
        if '.velocidad' in line and '=' in line:
            try:
                valor_str = line.split('=')[1].strip()
                valor = variables.get(valor_str, float(valor_str))
                movimientos.append({'tipo': 'velocidad', 'valor': valor})
            except:
                pass
                
        elif '.base' in line and '=' in line:
            try:
                valor = int(line.split('=')[1].strip())
                movimientos.append({'tipo': 'base', 'valor': valor})
            except:
                pass
                
        elif '.hombro' in line and '=' in line:
            try:
                valor = int(line.split('=')[1].strip())
                movimientos.append({'tipo': 'hombro', 'valor': valor})
            except:
                pass
                
        elif '.codo' in line and '=' in line:
            try:
                valor = int(line.split('=')[1].strip())
                movimientos.append({'tipo': 'codo', 'valor': valor})
            except:
                pass
                
        elif '.repetir' in line and '=' in line:
            try:
                repeticiones = int(line.split('=')[1].strip())
            except:
                pass
    
    return {
        'movimientos': movimientos,
        'repeticiones': repeticiones,
        'variables': variables
    }

def extract_motor_values_original(analyzer):
    """Fallback original"""
    return {'movimientos': [], 'repeticiones': 1}

def delay_count(segundos):
    """Cálculo de delay corregido"""
    ciclos_por_iteracion = 5
    ciclos_totales = int(segundos * 3_000_000)
    iteraciones = ciclos_totales // ciclos_por_iteracion
    return max(5000, iteraciones)

def calculate_steps_for_motor(motor, grados):
    """Cálculo de pasos CORREGIDO"""
    step_angles = {
        'base': 45,    
        'hombro': 30,  
        'codo': 30     
    }
    
    if motor not in step_angles:
        return 4
    
    step_angle = step_angles[motor]
    pasos_exactos = grados / step_angle
    pasos_enteros = int(pasos_exactos)
    
    # ASEGURAR que si hay movimiento, hay al menos 1 paso
    if grados > 0 and pasos_enteros == 0:
        pasos_enteros = 1
    
    return pasos_enteros

def generate_dynamic_machine_code(motor_values=None):
    """
    Genera código máquina con CORRECCIÓN de la lógica de ejecución
    """
    machine_code = []
    repeticiones = motor_values.get('repeticiones', 1)
    if repeticiones < 1:
        repeticiones = 1

    movimientos = motor_values.get('movimientos', [])
    
    def add_delay(segundos):
        if segundos <= 0:
            return
        
        total_count = delay_count(segundos)
        
        while total_count > 0:
            cx = min(total_count, 65535)
            machine_code.extend([0xB9, cx & 0xFF, (cx >> 8) & 0xFF])
            
            loop_start = len(machine_code)
            machine_code.extend([0x90])  # NOP
            machine_code.extend([0x49])  # DEC CX
            
            rel_offset = loop_start - (len(machine_code) + 2)
            machine_code.extend([0x75, rel_offset & 0xFF])
            
            total_count -= cx

    # Secuencias originales que funcionaban
    steps_forward = [0x09, 0x0C, 0x06, 0x03]
    steps_backward = [0x03, 0x06, 0x0C, 0x09]

    def generar_movimiento_motor(port, motor_name, grados_objetivo, direccion_positiva, velocidad_seg):
        """Genera movimiento con pasos corregidos"""
        if direccion_positiva:
            secuencia_base = steps_forward
            pasos_necesarios = calculate_steps_for_motor(motor_name, grados_objetivo)
            
            # CORRECCIÓN: Generar secuencia exacta
            secuencia_completa = []
            for i in range(pasos_necesarios):
                step_index = i % len(secuencia_base)
                secuencia_completa.append(secuencia_base[step_index])
            
            tiempo_total = velocidad_seg
            tiempo_por_paso = tiempo_total / len(secuencia_completa) if len(secuencia_completa) > 0 else 0
            
            print(f"   🎯 IDA {motor_name}: {grados_objetivo}° → {pasos_necesarios} pasos reales")
            print(f"      • Secuencia: {len(secuencia_completa)} comandos")
            print(f"      • Tiempo: {tiempo_total}s total ({tiempo_por_paso:.3f}s/paso)")
            
        else:
            secuencia_base = steps_backward
            pasos_necesarios = calculate_steps_for_motor(motor_name, grados_objetivo)
            
            # CORRECCIÓN: Asegurar que regreso tenga EXACTAMENTE los mismos pasos que ida
            secuencia_completa = []
            for i in range(pasos_necesarios):
                step_index = i % len(secuencia_base)
                secuencia_completa.append(secuencia_base[step_index])
                
            tiempo_total = 0.05
            tiempo_por_paso = tiempo_total / len(secuencia_completa) if len(secuencia_completa) > 0 else 0
            
            print(f"   🏃 REGRESO {motor_name}: {grados_objetivo}° → {pasos_necesarios} pasos (mismo que IDA)")
        
        # MOV DX, port
        machine_code.extend([0xBA, port, 0x00])
        
        for step in secuencia_completa:
            # MOV AL, step
            machine_code.extend([0xB0, step])
            # OUT DX, AL
            machine_code.extend([0xEE])
            add_delay(tiempo_por_paso)

    # Inicialización original
    machine_code.extend([0xBA, 0x06, 0x00])
    machine_code.extend([0xB0, 0x80])
    machine_code.extend([0xEE])

    for port in [0x00, 0x02, 0x04]:
        machine_code.extend([
            0xBA, port, 0x00,
            0xB0, 0x00,
            0xEE
        ])

    machine_code.extend([0xBE, repeticiones & 0xFF, (repeticiones >> 8) & 0xFF])
    loop_start = len(machine_code)

    # PROCESAMIENTO CORREGIDO
    posiciones = {'base': 0, 'hombro': 0, 'codo': 0}
    grados_objetivo = {'base': 0, 'hombro': 0, 'codo': 0}
    puertos = {'base': 0x00, 'hombro': 0x02, 'codo': 0x04}
    velocidades_motores = {}
    orden_movimientos = []
    velocidad_actual = 1.0
    
    print(f"\n🚀 === EJECUTANDO MOVIMIENTOS IDA ===")
    
    # FASE 1: IDA - CORRECCIÓN de lógica de velocidades
    for mov in movimientos:
        tipo = mov['tipo']
        valor = mov['valor']
        
        if tipo == 'velocidad':
            velocidad_actual = valor
            print(f"\n⚙️  Nueva velocidad: {velocidad_actual}s (para PRÓXIMO motor)")
            
        elif tipo in ['base', 'hombro', 'codo']:
            motor = tipo
            puerto = puertos[motor]
            pos_actual = posiciones[motor]
            
            print(f"\n🔍 Evaluando {motor.upper()}:")
            print(f"   • Valor: {valor}°, Posición actual: {pos_actual}°")
            print(f"   • Condición IDA: valor > 0 AND pos_actual == 0")
            print(f"   • Evaluación: {valor} > 0 AND {pos_actual} == 0 = {valor > 0 and pos_actual == 0}")
            
            if valor > 0 and pos_actual == 0:
                # EJECUTAR IDA
                grados_objetivo[motor] = valor
                velocidades_motores[motor] = velocidad_actual
                orden_movimientos.append(motor)
                
                print(f"   ✅ EJECUTANDO IDA con velocidad {velocidad_actual}s")
                generar_movimiento_motor(puerto, motor, valor, True, velocidad_actual)
                posiciones[motor] = valor
                
            elif valor == 0:
                print(f"   ⏭️  Comando de regreso (se procesará después)")
            else:
                print(f"   ⚠️  No cumple condiciones para IDA")

    print(f"\n🔙 === EJECUTANDO MOVIMIENTOS REGRESO ===")
    print(f"Orden de movimientos IDA: {orden_movimientos}")
    print(f"Orden de regreso será: {list(reversed(orden_movimientos))}")
    
    # FASE 2: REGRESO - orden inverso
    motores_a_regresar = []
    
    for mov in movimientos:
        if mov['tipo'] in ['base', 'hombro', 'codo'] and mov['valor'] == 0:
            motor = mov['tipo']
            if posiciones[motor] > 0:
                motores_a_regresar.append(motor)

    print(f"Motores que necesitan regreso: {motores_a_regresar}")

    for motor in reversed(orden_movimientos):
        if motor in motores_a_regresar:
            puerto = puertos[motor]
            grados_a_regresar = grados_objetivo[motor]
            
            print(f"\n🔄 EJECUTANDO REGRESO {motor.upper()}")
            generar_movimiento_motor(puerto, motor, grados_a_regresar, False, 0)
            posiciones[motor] = 0

    # Finalización original
    machine_code.extend([0x4E])
    machine_code.extend([0x83, 0xFE, 0x00])
    je_offset_pos = len(machine_code)
    machine_code.extend([0x74, 0x00])

    jmp_offset = loop_start - (len(machine_code) + 3)
    machine_code.extend([0xE9, jmp_offset & 0xFF, (jmp_offset >> 8) & 0xFF])
    
    rel_je = len(machine_code) - (je_offset_pos + 2)
    machine_code[je_offset_pos + 1] = rel_je & 0xFF

    for port in [0x00, 0x02, 0x04]:
        machine_code.extend([
            0xBA, port, 0x00,
            0xB0, 0x00,
            0xEE
        ])

    machine_code.extend([0xB8, 0x00, 0x4C])
    machine_code.extend([0xCD, 0x21])

    print(f"\n✅ Código generado: {len(machine_code)} bytes")
    return machine_code

def create_dynamic_com_from_analyzer(analyzer):
    """Función principal"""
    try:
        success, motor_values = create_dynamic_motor_com(analyzer)
        return success
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

if __name__ == "__main__":
    print("🔍 Testing Motor Controller con Debug de Ejecución...")
    
    class TestAnalyzer:
        def __init__(self):
            self.raw_code = """Robot r1
r1.inicio
r1.velocidad = 2.0
r1.base = 45  
r1.velocidad = 1.5         
r1.hombro = 120
r1.velocidad = 3.0       
r1.codo = 90       
r1.base = 0         
r1.hombro = 0        
r1.codo = 0      
r1.fin"""
    
    test_analyzer = TestAnalyzer()
    create_dynamic_com_from_analyzer(test_analyzer)