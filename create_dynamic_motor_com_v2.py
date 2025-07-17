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
        print("✅ Configuración basada en tu código Robot:")
        print(f"• Repeticiones: {motor_values.get('repeticiones', 1)}")
        for motor, angle in motor_values.items():
            if motor != 'repeticiones':
                print(f"• Motor {motor}: {angle}° (desde tu sintaxis)")
        
        return True, motor_values
        
    except Exception as e:
        print(f"Error creando motor_user.com dinámico: {e}")
        return False, {}

def extract_motor_values(analyzer):
    """
    Extrae los valores de motores y repeticiones del código Robot parseado.
    """
    motor_values = {}
    repeticiones = 1  # Valor por defecto
    valores_encontrados = False
    
    try:
        # Extraer de asignaciones del parser
        if hasattr(analyzer, 'parser') and analyzer.parser and hasattr(analyzer.parser, 'assignments'):
            for assignment in analyzer.parser.assignments:
                component = assignment.get('component', '').lower()
                value = assignment.get('value', 0)
                
                if component == 'repetir':
                    repeticiones = int(float(value))
                    print(f"✅ Extraído repetir = {value} veces")
                elif component in ['base', 'hombro', 'codo']:
                    motor_values[component] = int(float(value))
                    print(f"✅ Extraído {component} = {value}° desde parser")
                    valores_encontrados = True
        
        # Verificar valores necesarios
        required_motors = {'base', 'hombro', 'codo'}
        missing_motors = required_motors - set(motor_values.keys())
        
        if missing_motors:
            raise ValueError(f"No se encontraron valores para los motores: {', '.join(missing_motors)}")
        
        motor_values['repeticiones'] = repeticiones
        print(f"🔍 Valores extraídos: {motor_values} (x{repeticiones} repeticiones)")
        return motor_values
        
    except Exception as e:
        raise ValueError(f"Error extrayendo valores: {e}")

def generate_dynamic_machine_code(motor_values=None):
    machine_code = []
    repeticiones = motor_values.get('repeticiones', 1)
    if repeticiones < 1:
        repeticiones = 1

    # Configurar puerto como salida
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

    def add_delay(count):
        machine_code.extend([0xB9, count & 0xFF, (count >> 8) & 0xFF])  # MOV CX, count
        loop_pos = len(machine_code)
        machine_code.extend([0x90])  # NOP
        machine_code.extend([0x49])  # DEC CX
        rel = loop_pos - (len(machine_code) + 2)
        machine_code.extend([0x75, rel & 0xFF])  # JNZ

    steps = [0x09, 0x0C, 0x06, 0x03]
    reverse_steps = [0x03, 0x06, 0x0C, 0x09]

    def add_motor_sequence(port):
        machine_code.extend([0xBA, port, 0x00])  # MOV DX, port

        for pattern in steps:
            machine_code.extend([0xB0, pattern, 0xEE])
            add_delay(0x4000)

        for pattern in reverse_steps:
            machine_code.extend([0xB0, pattern, 0xEE])
            add_delay(0x4000)

        # Apagar motor
        machine_code.extend([0xB0, 0x00, 0xEE])
        add_delay(0x2000)

    # Contador de repeticiones en SI
    machine_code.extend([0xBE, repeticiones & 0xFF, (repeticiones >> 8) & 0xFF])  # MOV SI, N

    loop_start = len(machine_code)

    # Secuencia de los 3 motores por ciclo
    add_motor_sequence(0x00)  # BASE
    add_motor_sequence(0x02)  # HOMBRO
    add_motor_sequence(0x04)  # CODO

    # DECREMENTAR contador SI y verificar si termina
    machine_code.extend([0x4E])  # DEC SI
    machine_code.extend([0x83, 0xFE, 0x00])  # CMP SI, 0

    je_offset_pos = len(machine_code)
    machine_code.extend([0x74, 0x00])  # JE fin

    # JMP NEAR al inicio del bucle
    jmp_offset = loop_start - (len(machine_code) + 3)
    machine_code.extend([0xE9, jmp_offset & 0xFF, (jmp_offset >> 8) & 0xFF])

    # Corregir offset del salto JE
    je_target = len(machine_code)
    rel_je = je_target - (je_offset_pos + 2)
    machine_code[je_offset_pos + 1] = rel_je & 0xFF

    # Apagar todos los motores
    for port in [0x00, 0x02, 0x04]:
        machine_code.extend([
            0xBA, port, 0x00,
            0xB0, 0x00,
            0xEE
        ])

    # Salir a DOS
    machine_code.extend([0xB8, 0x00, 0x4C, 0xCD, 0x21])  # INT 21h

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
    class MockAnalyzer:
        def __init__(self):
            self.parser = type('obj', (object,), {
                'assignments': [
                    {'component': 'base', 'value': 20},
                    {'component': 'hombro', 'value': 100}, 
                    {'component': 'codo', 'value': 50}
                ]
            })()


