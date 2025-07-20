#!/usr/bin/env python3
"""
Generador DINÁMICO de archivos .COM v3
- Control preciso de velocidades por motor
- Sintaxis completa del robot con velocidades
- Compatibilidad con el sistema existente
"""

import os
import time

def create_dynamic_motor_com(analyzer):
    """
    Crea motor_user.com DINÁMICO basado en los valores del código Robot del usuario
    """
    try:
        # Crear directorio si no existe
        tasm_dir = os.path.join("DOSBox2", "Tasm")
        os.makedirs(tasm_dir, exist_ok=True)
        
        # Extraer valores de la sintaxis del usuario
        motor_values = extract_motor_values_enhanced(analyzer)
        print(f"🎯 Secuencia extraída del código:")
        
        # Mostrar secuencia detectada
        for i, mov in enumerate(motor_values.get('movimientos', [])):
            print(f"• {i+1}. {mov['tipo']}: {mov['valor']}")
        
        # Generar código máquina dinámico con velocidades
        machine_code = generate_dynamic_machine_code(motor_values)
        
        # Escribir archivo .COM dinámico
        com_path = os.path.join(tasm_dir, "motor_user.com")
        with open(com_path, 'wb') as f:
            f.write(bytes(machine_code))
        
        file_size = len(machine_code)
        print(f"\nmotor_user.com DINÁMICO creado! Tamaño: {file_size} bytes")
        print("✅ Configuración basada en tu código Robot:")
        print(f"• Repeticiones: {motor_values.get('repeticiones', 1)}")
        print(f"• Total de comandos: {len(motor_values.get('movimientos', []))}")
        
        return True, motor_values
        
    except Exception as e:
        print(f"Error creando motor_user.com dinámico: {e}")
        return False, {}

def extract_motor_values_enhanced(analyzer):
    """
    Extrae la secuencia completa de movimientos y velocidades del código Robot
    """
    motor_values = {
        'movimientos': [],
        'repeticiones': 1
    }
    
    try:
        # Intentar extraer del código crudo si está disponible
        raw_code = getattr(analyzer, 'raw_code', '') or getattr(analyzer, 'code', '')
        
        if raw_code:
            print("🔍 Parseando código Robot completo...")
            motor_values = parse_robot_syntax_complete(raw_code)
        else:
            # Fallback al método original
            print("🔍 Usando método de extracción original...")
            motor_values = extract_motor_values_original(analyzer)
        
        print(f"✅ Secuencia extraída: {len(motor_values.get('movimientos', []))} comandos")
        return motor_values
        
    except Exception as e:
        print(f"Error extrayendo valores: {e}")
        # Retornar valores por defecto
        return {
            'movimientos': [
                {'tipo': 'velocidad', 'valor': 1.0},
                {'tipo': 'base', 'valor': 45},
                {'tipo': 'hombro', 'valor': 90}, 
                {'tipo': 'codo', 'valor': 45},
                {'tipo': 'base', 'valor': 0},
                {'tipo': 'hombro', 'valor': 0},
                {'tipo': 'codo', 'valor': 0}
            ],
            'repeticiones': 1
        }

def parse_robot_syntax_complete(code):
    """
    Parsea la sintaxis completa del robot incluyendo velocidades
    """
    movimientos = []
    repeticiones = 1
    
    lines = code.strip().split('\n')
    
    for line in lines:
        line = line.strip()
        if not line or line.startswith('#') or line.startswith('Robot') or line.endswith('.inicio') or line.endswith('.fin'):
            continue
            
        # Detectar asignaciones con velocidad
        if '.velocidad' in line and '=' in line:
            try:
                valor = float(line.split('=')[1].strip())
                movimientos.append({'tipo': 'velocidad', 'valor': valor})
                print(f"  ✓ Velocidad: {valor}s")
            except ValueError:
                pass
                
        elif '.base' in line and '=' in line:
            try:
                valor = int(line.split('=')[1].strip())
                movimientos.append({'tipo': 'base', 'valor': valor})
                print(f"  ✓ Base: {valor}°")
            except ValueError:
                pass
                
        elif '.hombro' in line and '=' in line:
            try:
                valor = int(line.split('=')[1].strip())
                movimientos.append({'tipo': 'hombro', 'valor': valor})
                print(f"  ✓ Hombro: {valor}°")
            except ValueError:
                pass
                
        elif '.codo' in line and '=' in line:
            try:
                valor = int(line.split('=')[1].strip())
                movimientos.append({'tipo': 'codo', 'valor': valor})
                print(f"  ✓ Codo: {valor}°")
            except ValueError:
                pass
                
        elif '.repetir' in line and '=' in line:
            try:
                repeticiones = int(line.split('=')[1].strip())
                print(f"  ✓ Repeticiones: {repeticiones}")
            except ValueError:
                pass
    
    return {
        'movimientos': movimientos,
        'repeticiones': repeticiones
    }

def extract_motor_values_original(analyzer):
    """
    Método original de extracción (fallback)
    """
    motor_values = {'movimientos': [], 'repeticiones': 1}
    repeticiones = 1
    valores_encontrados = False
    
    try:
        if hasattr(analyzer, 'parser') and analyzer.parser and hasattr(analyzer.parser, 'assignments'):
            for assignment in analyzer.parser.assignments:
                component = assignment.get('component', '').lower()
                value = assignment.get('value', 0)
                
                if component == 'repetir':
                    repeticiones = int(float(value))
                elif component in ['base', 'hombro', 'codo']:
                    # Convertir formato antiguo a nuevo
                    motor_values['movimientos'].append({
                        'tipo': 'velocidad', 
                        'valor': 1.0  # Velocidad por defecto
                    })
                    motor_values['movimientos'].append({
                        'tipo': component, 
                        'valor': int(float(value))
                    })
                    valores_encontrados = True
        
        motor_values['repeticiones'] = repeticiones
        return motor_values
        
    except Exception as e:
        raise ValueError(f"Error extrayendo valores: {e}")

def generate_dynamic_machine_code(motor_values=None):
    """
    Genera código máquina dinámico basado en la secuencia de movimientos
    """
    machine_code = []

    repeticiones = motor_values.get('repeticiones', 1)
    if repeticiones < 1:
        repeticiones = 1

    # Obtener secuencia de movimientos
    movimientos = motor_values.get('movimientos', [])
    
    # Calcular iteraciones de delay para 3 MHz
    def delay_count(segundos):
        ciclos_por_iteracion = 5
        ciclos_totales = int(segundos * 3_000_000)
        return max(1, ciclos_totales // ciclos_por_iteracion)

    def add_delay(segundos):
        if segundos <= 0:
            return
        
        total_count = delay_count(segundos)
        while total_count > 0:
            cx = min(total_count, 65535)
            machine_code.extend([0xB9, cx & 0xFF, (cx >> 8) & 0xFF])  # MOV CX, cx
            loop_pos = len(machine_code)
            machine_code.extend([0x90])  # NOP
            machine_code.extend([0x49])  # DEC CX
            rel = loop_pos - (len(machine_code) + 2)
            machine_code.extend([0x75, rel & 0xFF])  # JNZ
            total_count -= cx

    # Secuencias de pasos
    steps_forward = [0x09, 0x0C, 0x06, 0x03]  # Horario
    steps_backward = [0x03, 0x06, 0x0C, 0x09]  # Antihorario

    def generar_movimiento_motor(port, direccion_positiva, velocidad_seg):
        """Genera movimiento con velocidad específica"""
        if velocidad_seg <= 0:
            velocidad_seg = 0.1
            
        secuencia = steps_forward if direccion_positiva else steps_backward
        tiempo_por_paso = velocidad_seg / len(secuencia)
        
        # MOV DX, port
        machine_code.extend([0xBA, port, 0x00])
        
        for i, step in enumerate(secuencia):
            # MOV AL, step
            machine_code.extend([0xB0, step])
            # OUT DX, AL  
            machine_code.extend([0xEE])
            
            # Delay entre pasos (excepto el último)
            if i < len(secuencia) - 1:
                add_delay(tiempo_por_paso)

    # Configurar puerto 6h como salida
    machine_code.extend([0xBA, 0x06, 0x00])  # MOV DX, 0006h
    machine_code.extend([0xB0, 0x80])        # MOV AL, 80h
    machine_code.extend([0xEE])              # OUT DX, AL

    # Inicializar motores en 0
    for port in [0x00, 0x02, 0x04]:
        machine_code.extend([
            0xBA, port, 0x00,
            0xB0, 0x00,
            0xEE
        ])

    add_delay(0.1)

    # Bucle de repeticiones
    machine_code.extend([0xBE, repeticiones & 0xFF, (repeticiones >> 8) & 0xFF])  # MOV SI, repeticiones
    loop_start = len(machine_code)

    # PROCESAR SECUENCIA DE MOVIMIENTOS
    posiciones = {'base': 0, 'hombro': 0, 'codo': 0}
    puertos = {'base': 0x00, 'hombro': 0x02, 'codo': 0x04}
    velocidades_motores = {}  # Guardar velocidad específica de cada motor
    orden_movimientos = []    # Guardar orden de motores para retorno inverso
    velocidad_actual = 1.0
    
    print("=== GENERANDO CÓDIGO PARA SECUENCIA ===")
    
    # FASE 1: Movimientos de IDA (con velocidades específicas)
    for mov in movimientos:
        tipo = mov['tipo']
        valor = mov['valor']
        
        if tipo == 'velocidad':
            velocidad_actual = valor
            print(f"Velocidad establecida: {velocidad_actual}s")
            
        elif tipo in ['base', 'hombro', 'codo']:
            motor = tipo
            puerto = puertos[motor]
            pos_actual = posiciones[motor]
            
            if valor > 0 and pos_actual == 0:
                # Movimiento IDA - Asociar velocidad actual con este motor
                velocidades_motores[motor] = velocidad_actual
                orden_movimientos.append(motor)
                
                print(f"{motor.upper()}: 0° → {valor}° en {velocidad_actual}s")
                generar_movimiento_motor(puerto, True, velocidad_actual)
                posiciones[motor] = valor
                add_delay(0.2)  # Pausa entre motores
                
            elif valor == 0 and pos_actual > 0:
                # Este caso se procesará en FASE 2
                pass
    
    # FASE 2: Movimientos de REGRESO (orden inverso, velocidad rápida)
    print("\n=== RETORNO EN ORDEN INVERSO ===")
    motores_a_regresar = []
    
    # Recopilar motores que necesitan regresar a 0
    for mov in movimientos:
        tipo = mov['tipo']
        valor = mov['valor']
        
        if tipo in ['base', 'hombro', 'codo'] and valor == 0:
            motor = tipo
            if posiciones[motor] > 0:  # Solo si está en posición diferente de 0
                motores_a_regresar.append(motor)
    
    # Retornar en orden inverso al orden de movimiento
    for motor in reversed(orden_movimientos):
        if motor in motores_a_regresar:
            puerto = puertos[motor]
            pos_actual = posiciones[motor]
            tiempo_regreso = 0.2  # Retorno rápido fijo
            
            print(f"{motor.upper()}: {pos_actual}° → 0° en {tiempo_regreso}s (RETORNO)")
            generar_movimiento_motor(puerto, False, tiempo_regreso)
            posiciones[motor] = 0
            add_delay(0.2)  # Pausa entre motores

    print("=== CÓDIGO GENERADO ===")

    # Control del bucle de repeticiones
    machine_code.extend([0x4E])                # DEC SI
    machine_code.extend([0x83, 0xFE, 0x00])    # CMP SI, 0
    je_offset_pos = len(machine_code)
    machine_code.extend([0x74, 0x00])          # JE fin

    # JMP al inicio del ciclo
    jmp_offset = loop_start - (len(machine_code) + 3)
    machine_code.extend([0xE9, jmp_offset & 0xFF, (jmp_offset >> 8) & 0xFF])
    
    # Calcular offset para JE
    rel_je = len(machine_code) - (je_offset_pos + 2)
    machine_code[je_offset_pos + 1] = rel_je & 0xFF

    # Apagar motores al final
    for port in [0x00, 0x02, 0x04]:
        machine_code.extend([
            0xBA, port, 0x00,
            0xB0, 0x00,
            0xEE
        ])

    # Salida a DOS
    machine_code.extend([0xB8, 0x00, 0x4C])
    machine_code.extend([0xCD, 0x21])

    print(f"Código máquina generado: {len(machine_code)} bytes")
    return machine_code

# Función para usar desde main.py (mantener compatibilidad)
def create_dynamic_com_from_analyzer(analyzer):
    """
    Función principal para crear .COM dinámico desde el analizador
    """
    try:
        success, motor_values = create_dynamic_motor_com(analyzer)
        return success
    except Exception as e:
        print(f"Error en create_dynamic_com_from_analyzer: {e}")
        return False
