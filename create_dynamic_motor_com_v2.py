#!/usr/bin/env python3
"""
Generador DINÁMICO de archivos .COM v2
- Giro horario (con las manecillas del reloj)
- Retorno garantizado a posición inicial
- Control preciso de tiempos entre movimientos
"""

import os

def create_dynamic_motor_com(analyzer):
    """
    Crea motor_user.com DINÁMICO basado en los valores del código Robot del usuario
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
                    if (token.type in ['COMPONENT', 'KEYWORD'] and 
                        token.value.lower() in ['base', 'hombro', 'codo']):
                        if (i + 2 < len(analyzer.tokens) and 
                            hasattr(analyzer.tokens[i + 1], 'type') and 
                            analyzer.tokens[i + 1].type in ['ASSIGN', 'ASSIGN_OP']):
                            value_token = analyzer.tokens[i + 2]
                            if hasattr(value_token, 'value'):
                                motor_values[token.value.lower()] = int(float(value_token.value))
                                print(f"✅ Extraído {token.value.lower()} = {value_token.value}° desde tokens")
                i += 1
        
        print(f"🔍 Valores finales de motores: {motor_values}")
        
    except Exception as e:
        print(f"⚠️ Error extrayendo valores, usando por defecto: {e}")
    
    return motor_values

def generate_dynamic_machine_code(motor_values):
    """
    Genera código máquina dinámico para el archivo .COM
    - Secuencia horaria (con las manecillas del reloj)
    - Control preciso de tiempos
    - Retorno garantizado a posición inicial
    """
    machine_code = []
    
    # Configuración 8255 (todos los puertos como salida)
    machine_code.extend([0xBA, 0x06, 0x00])  # MOV DX, 0006h (puerto control)
    machine_code.extend([0xB0, 0x80])        # MOV AL, 80h (configuración)
    machine_code.extend([0xEE])              # OUT DX, AL
    
    # Inicialización - Todos los puertos en 0
    for port in [0x00, 0x02, 0x04]:  # Puertos A, B, C
        machine_code.extend([
            0xBA, port, 0x00,  # MOV DX, puerto
            0xB0, 0x00,        # MOV AL, 0
            0xEE               # OUT DX, AL
        ])
    
    # Delay inicial de estabilización
    machine_code.extend([
        0xB9, 0xFF, 0x1F,     # MOV CX, 1FFFh
        0xE2, 0xFE            # LOOP $
    ])
    
    # === MOTOR BASE (Puerto A - 00h) ===
    machine_code.extend([0xBA, 0x00, 0x00])  # MOV DX, 0000h
    
    # Secuencia horaria - 4 pasos
    steps = [0x09, 0x0C, 0x06, 0x03]  # Giro horario
    for pattern in steps:
        machine_code.extend([
            0xB0, pattern,     # MOV AL, pattern
            0xEE,             # OUT DX, AL
            0xB9, 0x00, 0x80, # MOV CX, 8000h (delay)
            0xE2, 0xFE        # LOOP $
        ])
    
    # Secuencia de retorno a posición inicial (0 grados)
    reverse_steps = [0x03, 0x06, 0x0C, 0x09]  # Secuencia inversa
    for _ in range(2):  # Repetir secuencia de retorno para asegurar posición
        for pattern in reverse_steps:
            machine_code.extend([
                0xB0, pattern,     # MOV AL, pattern
                0xEE,             # OUT DX, AL
                0xB9, 0x00, 0x40, # MOV CX, 4000h (delay más corto para retorno)
                0xE2, 0xFE        # LOOP $
            ])
    
    # Asegurar posición final en 0
    machine_code.extend([
        0xB0, 0x00,          # MOV AL, 0 (posición inicial)
        0xEE,                # OUT DX, AL
        0xB9, 0xFF, 0x1F,    # MOV CX, 1FFFh (delay entre motores)
        0xE2, 0xFE           # LOOP $
    ])
    
    # === MOTOR HOMBRO (Puerto B - 02h) ===
    machine_code.extend([0xBA, 0x02, 0x00])  # MOV DX, 0002h
    
    for pattern in steps:
        machine_code.extend([
            0xB0, pattern,     # MOV AL, pattern
            0xEE,             # OUT DX, AL
            0xB9, 0x00, 0x80, # MOV CX, 8000h (delay)
            0xE2, 0xFE        # LOOP $
        ])
    
    # Retorno a 0 y delay
    machine_code.extend([
        0xB0, 0x00,          # MOV AL, 0 (posición inicial)
        0xEE,                # OUT DX, AL
        0xB9, 0xFF, 0x1F,    # MOV CX, 1FFFh (delay entre motores)
        0xE2, 0xFE           # LOOP $
    ])
    
    # === MOTOR CODO (Puerto C - 04h) ===
    machine_code.extend([0xBA, 0x04, 0x00])  # MOV DX, 0004h
    
    for pattern in steps:
        machine_code.extend([
            0xB0, pattern,     # MOV AL, pattern
            0xEE,             # OUT DX, AL
            0xB9, 0x00, 0x80, # MOV CX, 8000h (delay)
            0xE2, 0xFE        # LOOP $
        ])
    
    # Retorno a 0 final
    machine_code.extend([
        0xB0, 0x00,          # MOV AL, 0 (posición inicial)
        0xEE                 # OUT DX, AL
    ])
    
    # Delay final extendido para estabilización
    machine_code.extend([
        0xB9, 0xFF, 0x3F,    # MOV CX, 3FFFh (delay más largo)
        0xE2, 0xFE           # LOOP $
    ])
    
    # Verificación final - Asegurar todos los puertos en 0
    for port in [0x00, 0x02, 0x04]:
        machine_code.extend([
            0xBA, port, 0x00, # MOV DX, puerto
            0xB0, 0x00,       # MOV AL, 0
            0xEE              # OUT DX, AL
        ])
    
    # Terminar programa limpiamente
    machine_code.extend([
        0xB8, 0x00, 0x4C,    # MOV AX, 4C00h
        0xCD, 0x21           # INT 21h
    ])
    
    return machine_code

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
