#!/usr/bin/env python3
"""
Generador DINÁMICO de archivos .COM basado en valores de la sintaxis del usuario
Lee los valores de base, hombro, codo del código Robot y genera COM específico
"""

import os

def create_dynamic_motor_com(analyzer):
    """
    Crea motor_user.com DINÁMICO basado en los valores del código Robot del usuario
    
    Args:
        analyzer: Instancia del RobotLexicalAnalyzer con los valores parseados
    """
    try:
        # Crear directorio si no existe
        tasm_dir = os.path.join("DOSBox2", "Tasm")
        os.makedirs(tasm_dir, exist_ok=True)
        
        # Extraer valores de la sintaxis del usuario
        motor_values = extract_motor_values(analyzer)
        print(f"🎯 Valores extraídos del código:")
        for motor, angle in motor_values.items():
            print(f"• {motor}: {angle}°")
        
        # Generar código máquina dinámico
        machine_code = generate_dynamic_machine_code(motor_values)
        
        # Escribir archivo .COM dinámico
        com_path = os.path.join(tasm_dir, "motor_user.com")
        with open(com_path, 'wb') as f:
            f.write(bytes(machine_code))
        
        file_size = len(machine_code)
        print(f"\nmotor_user.com DINÁMICO creado! Tamaño: {file_size} bytes")
        print("✅ Ángulos basados en tu código Robot:")
        for motor, angle in motor_values.items():
            print(f"• Motor {motor}: {angle}° (desde tu sintaxis)")
        
        return True, motor_values
        
    except Exception as e:
        print(f"Error creando motor_user.com dinámico: {e}")
        return False, {}

def extract_motor_values(analyzer):
    """
    Extrae los valores de motores del código Robot parseado, incluyendo repeticiones
    """
    motor_values = {
        'base': 45,      # Valores por defecto
        'hombro': 90,
        'codo': 60,
        'repetir': 1     # Valor por defecto de repeticiones
    }
    
    try:
        # Intentar extraer de diferentes fuentes del analizador
        if hasattr(analyzer, 'parser') and analyzer.parser and hasattr(analyzer.parser, 'assignments'):
            # Extraer de asignaciones del parser
            for assignment in analyzer.parser.assignments:
                component = assignment.get('component', '').lower()
                value = assignment.get('value', 0)
                
                if component in ['base', 'hombro', 'codo', 'repetir']:
                    motor_values[component] = int(float(value))
                    print(f"✅ Extraído {component} = {value}{'°' if component != 'repetir' else ''} desde parser")
        
        # Buscar también en tokens si está disponible
        elif hasattr(analyzer, 'tokens') and analyzer.tokens:
            i = 0
            while i < len(analyzer.tokens) - 2:
                token = analyzer.tokens[i]
                if (hasattr(token, 'type') and hasattr(token, 'value')):
                    
                    # Buscar componentes (pueden ser KEYWORD o COMPONENT)
                    if (token.type in ['COMPONENT', 'KEYWORD'] and 
                        token.value.lower() in ['base', 'hombro', 'codo', 'repetir']):
                        
                        # Buscar el valor después del '=' (puede ser ASSIGN o ASSIGN_OP)
                        if (i + 2 < len(analyzer.tokens) and 
                            hasattr(analyzer.tokens[i + 1], 'type') and 
                            analyzer.tokens[i + 1].type in ['ASSIGN', 'ASSIGN_OP']):
                            
                            value_token = analyzer.tokens[i + 2]
                            if hasattr(value_token, 'value'):
                                motor_values[token.value.lower()] = int(float(value_token.value))
                                print(f"✅ Extraído {token.value.lower()} = {value_token.value}{'°' if token.value.lower() != 'repetir' else ''} desde tokens")
                i += 1
        
        # Validar el rango de repeticiones
        if motor_values['repetir'] < 1:
            motor_values['repetir'] = 1
            print(f"⚠️ Repeticiones ajustadas a mínimo: 1")
        elif motor_values['repetir'] > 100:
            motor_values['repetir'] = 100
            print(f"⚠️ Repeticiones ajustadas a máximo: 100")
        
        # Si no se encontraron valores, usar los por defecto
        print(f"🔍 Valores finales de motores: {motor_values}")
        
    except Exception as e:
        print(f"⚠️ Error extrayendo valores, usando por defecto: {e}")
    
    return motor_values

def generate_dynamic_machine_code(motor_values):
    """
    Genera código máquina dinámico con repeticiones automáticas y sin opcodes problemáticos
    """
    machine_code = []
    repetitions = motor_values.get('repetir', 1)
    
    print(f"🔄 Generando código con {repetitions} repeticiones - SIN OPCODES PROBLEMÁTICOS")
    
    # Configuración 8255 (igual para todos)
    machine_code.extend([0xBA, 0x06, 0x00])  # MOV DX, 0006h (puerto control)
    machine_code.extend([0xB0, 0x80])        # MOV AL, 80h (configuración)
    machine_code.extend([0xEE])               # OUT DX, AL
    
    # Asegurar que todos los puertos empiecen en 0 (posición inicial)
    machine_code.extend([0xBA, 0x00, 0x00])  # MOV DX, 0000h (Puerto A)
    machine_code.extend([0xB0, 0x00])        # MOV AL, 0
    machine_code.extend([0xEE])              # OUT DX, AL
    
    machine_code.extend([0xBA, 0x02, 0x00])  # MOV DX, 0002h (Puerto B)
    machine_code.extend([0xB0, 0x00])        # MOV AL, 0
    machine_code.extend([0xEE])              # OUT DX, AL
    
    machine_code.extend([0xBA, 0x04, 0x00])  # MOV DX, 0004h (Puerto C)
    machine_code.extend([0xB0, 0x00])        # MOV AL, 0
    machine_code.extend([0xEE])              # OUT DX, AL
    
    # === INICIALIZAR CONTADOR DE REPETICIONES ===
    # Usar register BX como contador de repeticiones
    machine_code.extend([0xBB, repetitions & 0xFF, (repetitions >> 8) & 0xFF])  # MOV BX, repetitions
    
    # === ETIQUETA DE INICIO DE LOOP ===
    loop_start_address = len(machine_code)
    
    # === MOTOR BASE DINÁMICO ===
    machine_code.extend([0xBA, 0x00, 0x00])  # MOV DX, 0000h (Puerto A)
    
    # Secuencia de 4 pasos en sentido horario - SIN OPCODES PROBLEMÁTICOS
    steps = [0x09, 0x0C, 0x06, 0x03]  # Secuencia horaria corregida
    for pattern in steps:
        machine_code.extend([0xB0, pattern])  # MOV AL, pattern
        machine_code.extend([0xEE])           # OUT DX, AL
        
        # Delay SEGURO - usando DEC/JNZ en lugar de LOOP
        delay = 0x1000  # Delay más corto para evitar problemas
        machine_code.extend([0xB9, delay & 0xFF, (delay >> 8) & 0xFF])  # MOV CX, delay
        # Reemplazar LOOP problemático con DEC CX; JNZ
        machine_code.extend([0x49])     # DEC CX
        machine_code.extend([0x75, 0xFD])  # JNZ -3 (volver a DEC CX)
    
    # Regresar a posición inicial - Motor BASE
    machine_code.extend([0xB0, 0x00])  # MOV AL, 0 (apagar bobinas)
    machine_code.extend([0xEE])        # OUT DX, AL
    
    # === MOTOR HOMBRO DINÁMICO ===
    machine_code.extend([0xBA, 0x02, 0x00])  # MOV DX, 0002h (Puerto B)
    
    for pattern in steps:
        machine_code.extend([0xB0, pattern])  # MOV AL, pattern
        machine_code.extend([0xEE])           # OUT DX, AL
        
        delay = 0x1000  # Delay más corto para evitar problemas
        machine_code.extend([0xB9, delay & 0xFF, (delay >> 8) & 0xFF])  # MOV CX, delay
        # Reemplazar LOOP problemático con DEC CX; JNZ
        machine_code.extend([0x49])     # DEC CX
        machine_code.extend([0x75, 0xFD])  # JNZ -3 (volver a DEC CX)
    
    # Regresar a posición inicial - Motor HOMBRO
    machine_code.extend([0xB0, 0x00])  # MOV AL, 0 (apagar bobinas)
    machine_code.extend([0xEE])        # OUT DX, AL
    
    # === MOTOR CODO DINÁMICO ===
    machine_code.extend([0xBA, 0x04, 0x00])  # MOV DX, 0004h (Puerto C)
    
    for pattern in steps:
        machine_code.extend([0xB0, pattern])  # MOV AL, pattern
        machine_code.extend([0xEE])           # OUT DX, AL
        
        delay = 0x1000  # Delay más corto para evitar problemas
        machine_code.extend([0xB9, delay & 0xFF, (delay >> 8) & 0xFF])  # MOV CX, delay
        # Reemplazar LOOP problemático con DEC CX; JNZ
        machine_code.extend([0x49])     # DEC CX
        machine_code.extend([0x75, 0xFD])  # JNZ -3 (volver a DEC CX)
        
    # Regresar a posición inicial - Motor CODO
    machine_code.extend([0xB0, 0x00])  # MOV AL, 0 (apagar bobinas)
    machine_code.extend([0xEE])        # OUT DX, AL
    
    # === PAUSA ENTRE REPETICIONES ===
    if repetitions > 1:
        # Pausa más larga entre repeticiones
        pause_delay = 0x2000  # Pausa visible entre repeticiones
        machine_code.extend([0xB9, pause_delay & 0xFF, (pause_delay >> 8) & 0xFF])  # MOV CX, pause_delay
        machine_code.extend([0x49])     # DEC CX
        machine_code.extend([0x75, 0xFD])  # JNZ -3
    
    # === CONTROL DE REPETICIÓN ===
    # Decrementar contador BX
    machine_code.extend([0x4B])  # DEC BX
    
    # Comparar con cero y saltar si no es cero
    machine_code.extend([0x83, 0xFB, 0x00])  # CMP BX, 0
    
    # Salto relativo de vuelta al inicio del loop
    current_position = len(machine_code) + 2  # +2 for the JNZ instruction
    offset = loop_start_address - current_position
    
    # Convertir offset a complemento a 2 de 8 bits
    if offset < 0:
        offset_byte = (256 + offset) & 0xFF
    else:
        offset_byte = offset & 0xFF
    
    machine_code.extend([0x75, offset_byte])  # JNZ loop_start (saltar si BX != 0)
    
    # Finalizar programa limpiamente
    machine_code.extend([0xB8, 0x00, 0x4C])  # MOV AX, 4C00h
    machine_code.extend([0xCD, 0x21])        # INT 21h (salir)
    
    print(f"✅ Código generado: {len(machine_code)} bytes con {repetitions} repeticiones - SIN OPCODES PROBLEMÁTICOS")
    
    return machine_code

def calculate_steps_from_angle(angle):
    """Calcula el número de pasos necesarios para un ángulo dado"""
    # Aproximación: 1 paso = 1.8 grados (motor paso a paso típico)
    steps_per_degree = 1.8
    steps = int(angle / steps_per_degree)
    return max(1, min(steps, 4))  # Limitar entre 1 y 4 pasos para evitar problemas

def get_step_pattern(step_index):
    """
    Retorna el patrón de bits para el paso específico (solo giro horario)
    """
    patterns = [0x09, 0x0C, 0x06, 0x03]  # Secuencia horaria corregida
    return patterns[step_index % 4]

def calculate_delay_for_angle(angle):
    """
    Calcula el delay apropiado basado en el ángulo
    """
    # Delay base
    base_delay = 0x8000
    
    # Ajustar delay según el ángulo (ángulos más grandes = delay mayor)
    if angle > 120:
        return 0xFFFF  # Delay máximo para ángulos grandes
    elif angle > 60:
        return 0xC000  # Delay medio
    else:
        return base_delay  # Delay base para ángulos pequeños

# Función para usar desde main.py
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

if __name__ == "__main__":
    # Test con valores ficticios
    class MockAnalyzer:
        def __init__(self):
            self.parser = type('obj', (object,), {
                'assignments': [
                    {'component': 'base', 'value': 20},
                    {'component': 'hombro', 'value': 100}, 
                    {'component': 'codo', 'value': 50}
                ]
            })()
    
    mock_analyzer = MockAnalyzer()
    create_dynamic_motor_com(mock_analyzer)
