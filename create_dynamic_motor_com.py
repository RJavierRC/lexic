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
    Extrae los valores de motores del código Robot parseado
    """
    motor_values = {
        'base': 45,      # Valores por defecto
        'hombro': 90,
        'codo': 60
    }
    
    try:
        # Intentar extraer de diferentes fuentes del analizador
        if hasattr(analyzer, 'parser') and analyzer.parser and hasattr(analyzer.parser, 'assignments'):
            # Extraer de asignaciones del parser
            for assignment in analyzer.parser.assignments:
                component = assignment.get('component', '').lower()
                value = assignment.get('value', 0)
                
                if component in ['base', 'hombro', 'codo']:
                    motor_values[component] = int(float(value))
                    print(f"✅ Extraído {component} = {value}° desde parser")
        
        # Buscar también en tokens si está disponible
        elif hasattr(analyzer, 'tokens') and analyzer.tokens:
            i = 0
            while i < len(analyzer.tokens) - 2:
                token = analyzer.tokens[i]
                if (hasattr(token, 'type') and hasattr(token, 'value')):
                    
                    # Buscar componentes (pueden ser KEYWORD o COMPONENT)
                    if (token.type in ['COMPONENT', 'KEYWORD'] and 
                        token.value.lower() in ['base', 'hombro', 'codo']):
                        
                        # Buscar el valor después del '=' (puede ser ASSIGN o ASSIGN_OP)
                        if (i + 2 < len(analyzer.tokens) and 
                            hasattr(analyzer.tokens[i + 1], 'type') and 
                            analyzer.tokens[i + 1].type in ['ASSIGN', 'ASSIGN_OP']):
                            
                            value_token = analyzer.tokens[i + 2]
                            if hasattr(value_token, 'value'):
                                motor_values[token.value.lower()] = int(float(value_token.value))
                                print(f"✅ Extraído {token.value.lower()} = {value_token.value}° desde tokens")
                i += 1
        
        # Si no se encontraron valores, usar los por defecto
        print(f"🔍 Valores finales de motores: {motor_values}")
        
    except Exception as e:
        print(f"⚠️ Error extrayendo valores, usando por defecto: {e}")
    
    return motor_values

def generate_dynamic_machine_code(motor_values):
    """
    Genera código máquina dinámico basado en los valores de motores
    """
    machine_code = []
    
    # Configuración 8255 (igual para todos)
    machine_code.extend([0xBA, 0x06, 0x00])  # MOV DX, 0006h (puerto control)
    machine_code.extend([0xB0, 0x80])        # MOV AL, 80h (configuración)
    machine_code.extend([0xEE])               # OUT DX, AL
    
    # === MOTOR BASE DINÁMICO ===
    base_angle = motor_values.get('base', 45)
    base_steps = calculate_steps_for_angle(base_angle)
    
    machine_code.extend([0xBA, 0x00, 0x00])  # MOV DX, 0000h (Puerto A)
    
    for step in range(base_steps):
        pattern = get_step_pattern(step % 4)  # Ciclo de 4 patrones
        machine_code.extend([0xB0, pattern])  # MOV AL, pattern
        machine_code.extend([0xEE])           # OUT DX, AL
        
        # Delay proporcional al ángulo
        delay = calculate_delay_for_angle(base_angle)
        machine_code.extend([0xB9, delay & 0xFF, (delay >> 8) & 0xFF])  # MOV CX, delay
        machine_code.extend([0xE2, 0xFE])     # LOOP $
    
    # === MOTOR HOMBRO DINÁMICO ===
    hombro_angle = motor_values.get('hombro', 90)
    hombro_steps = calculate_steps_for_angle(hombro_angle)
    
    machine_code.extend([0xBA, 0x02, 0x00])  # MOV DX, 0002h (Puerto B)
    
    for step in range(hombro_steps):
        pattern = get_step_pattern(step % 4)
        machine_code.extend([0xB0, pattern])  # MOV AL, pattern
        machine_code.extend([0xEE])           # OUT DX, AL
        
        delay = calculate_delay_for_angle(hombro_angle)
        machine_code.extend([0xB9, delay & 0xFF, (delay >> 8) & 0xFF])  # MOV CX, delay
        machine_code.extend([0xE2, 0xFE])     # LOOP $
    
    # === MOTOR CODO DINÁMICO ===
    codo_angle = motor_values.get('codo', 60)
    codo_steps = calculate_steps_for_angle(codo_angle)
    
    machine_code.extend([0xBA, 0x04, 0x00])  # MOV DX, 0004h (Puerto C)
    
    for step in range(codo_steps):
        pattern = get_step_pattern(step % 4)
        machine_code.extend([0xB0, pattern])  # MOV AL, pattern
        machine_code.extend([0xEE])           # OUT DX, AL
        
        delay = calculate_delay_for_angle(codo_angle)
        machine_code.extend([0xB9, delay & 0xFF, (delay >> 8) & 0xFF])  # MOV CX, delay
        machine_code.extend([0xE2, 0xFE])     # LOOP $
    
    # Finalizar programa limpiamente
    machine_code.extend([0xB8, 0x00, 0x4C])  # MOV AX, 4C00h
    machine_code.extend([0xCD, 0x21])        # INT 21h (salir)
    
    return machine_code

def calculate_steps_for_angle(angle):
    """
    Calcula el número de pasos necesarios para un ángulo dado
    Basado en motores paso a paso estándar
    """
    # Motor paso a paso típico: 1.8° por paso (200 pasos = 360°)
    steps_per_degree = 200 / 360  # ≈ 0.56 pasos por grado
    steps = max(1, int(angle * steps_per_degree))
    
    # Limitar a un rango razonable pero permitir diferencias
    return min(steps, 50)  # Máximo 50 pasos para mantener archivos pequeños pero permitir variación

def get_step_pattern(step_index):
    """
    Retorna el patrón de bits para el paso específico
    """
    patterns = [0x06, 0x0C, 0x09, 0x03]  # Secuencia estándar de motor paso a paso
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
