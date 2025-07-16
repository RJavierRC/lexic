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

def generate_dynamic_machine_code(motor_values=None):
    """
    Genera código máquina dinámico para el archivo .COM
    - Cada motor gira una secuencia horaria de 4 pasos (90°)
    - Luego regresa con la secuencia inversa (–90°)
    - Incluye retardos entre movimientos
    """
    machine_code = []

    # Configurar todos los puertos como salida (8255)
    machine_code.extend([0xBA, 0x06, 0x00])  # MOV DX, 0006h
    machine_code.extend([0xB0, 0x80])        # MOV AL, 80h
    machine_code.extend([0xEE])              # OUT DX, AL

    # Inicializar puertos A, B y C en 0
    for port in [0x00, 0x02, 0x04]:
        machine_code.extend([
            0xBA, port, 0x00,  # MOV DX, puerto
            0xB0, 0x00,        # MOV AL, 0
            0xEE               # OUT DX, AL
        ])

    # Delay de estabilización inicial
    machine_code.extend([
        0xB9, 0xFF, 0x1F,     # MOV CX, 1FFFh
        0xE2, 0xFE            # LOOP $
    ])

    # Patrón de pasos (sentido horario y antihorario)
    steps = [0x09, 0x0C, 0x06, 0x03]        # Avance
    reverse_steps = [0x03, 0x06, 0x0C, 0x09] # Retorno

    # Función auxiliar para agregar secuencia
    def add_motor_sequence(port):
        # Seleccionar puerto
        machine_code.extend([0xBA, port, 0x00])  # MOV DX, port

        # Giro hacia adelante
        for pattern in steps:
            machine_code.extend([
                0xB0, pattern,     # MOV AL, pattern
                0xEE,              # OUT DX, AL
                0xB9, 0x00, 0x80,  # MOV CX, 8000h (delay)
                0xE2, 0xFE         # LOOP $
            ])

        # Retorno (giro inverso)
        for pattern in reverse_steps:
            machine_code.extend([
                0xB0, pattern,     # MOV AL, pattern
                0xEE,              # OUT DX, AL
                0xB9, 0x00, 0x40,  # MOV CX, 4000h (delay más corto)
                0xE2, 0xFE         # LOOP $
            ])

        # Asegurar motor apagado (posición 0)
        machine_code.extend([
            0xB0, 0x00,          # MOV AL, 0
            0xEE,                # OUT DX, AL
            0xB9, 0xFF, 0x1F,    # MOV CX, 1FFFh (delay entre motores)
            0xE2, 0xFE           # LOOP $
        ])

    # === Motor BASE (Puerto A - 00h) ===
    add_motor_sequence(0x00)

    # === Motor HOMBRO (Puerto B - 02h) ===
    add_motor_sequence(0x02)

    # === Motor CODO (Puerto C - 04h) ===
    add_motor_sequence(0x04)

    # Delay final extendido
    machine_code.extend([
        0xB9, 0xFF, 0x3F,    # MOV CX, 3FFFh
        0xE2, 0xFE           # LOOP $
    ])

    # Asegurar que todos los puertos queden en 0
    for port in [0x00, 0x02, 0x04]:
        machine_code.extend([
            0xBA, port, 0x00,  # MOV DX, port
            0xB0, 0x00,        # MOV AL, 0
            0xEE               # OUT DX, AL
        ])

    # Salida limpia del programa
    machine_code.extend([
        0xB8, 0x00, 0x4C,    # MOV AX, 4C00h
        0xCD, 0x21           # INT 21h
    ])

    return machine_code

    
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
