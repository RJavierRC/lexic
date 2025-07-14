#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generador de Assembly específicamente optimizado para Proteus
Usa formato .MODEL SMALL y direcciones de puerto estándar
"""

from datetime import datetime

class ProteusAssemblyGenerator:
    """Generador de código assembly compatible con Proteus"""
    
    def __init__(self):
        # Direcciones de puerto estándar para Proteus/8255
        self.port_addresses = {
            'base': '0300h',      # Port A del 8255
            'hombro': '0301h',    # Port B del 8255  
            'codo': '0302h',      # Port C del 8255
            'config': '0303h'     # Puerto de configuración del 8255
        }
        
        # Patrones de pasos para motores paso a paso
        self.step_patterns = [
            '01h',  # Paso 1: 0001
            '03h',  # Paso 2: 0011  
            '02h',  # Paso 3: 0010
            '06h',  # Paso 4: 0110
            '04h',  # Paso 5: 0100
            '0Ch',  # Paso 6: 1100
            '08h',  # Paso 7: 1000
            '09h'   # Paso 8: 1001
        ]
    
    def generate_from_robot_data(self, robot_commands, program_name="robot_control"):
        """Genera assembly a partir de comandos de robot analizados"""
        
        # Extraer datos de los comandos
        motor_values = {}
        delay_value = 1000  # Delay por defecto
        
        for command in robot_commands:
            if 'base' in command:
                motor_values['base'] = command['base']
            elif 'hombro' in command:
                motor_values['hombro'] = command['hombro']
            elif 'codo' in command:
                motor_values['codo'] = command['codo']
            elif 'espera' in command:
                delay_value = int(command['espera'] * 1000)  # Convertir a ms
        
        return self.generate_proteus_compatible(motor_values, delay_value, program_name)
    
    def generate_proteus_compatible(self, motor_values, delay_ms=1000, program_name="robot_control"):
        """Genera código assembly completamente compatible con Proteus"""
        
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        asm_code = f""";===============================================
; CONTROL DE MOTORES PARA SIMULACION PROTEUS
; Programa: {program_name}
; Generado: {timestamp}
; Compatible: 8086/8088 + 8255 PPI
;===============================================

.MODEL SMALL
.STACK 100h

.DATA
    ; Variables del programa
    motor_base     DB ?    ; Estado motor base
    motor_hombro   DB ?    ; Estado motor hombro  
    motor_codo     DB ?    ; Estado motor codo
    delay_count    DW ?    ; Contador de delay

.CODE
MAIN PROC
    ; Inicializar segmento de datos
    MOV AX, @DATA
    MOV DS, AX
    
    ; Configurar 8255 PPI - Todos los puertos como salida
    MOV DX, {self.port_addresses['config']}  ; Puerto de configuración
    MOV AL, 80h              ; Configuración: todos outputs
    OUT DX, AL
    
    ; Mensaje de inicio (opcional para debug)
    ; MOV AH, 09h
    ; LEA DX, start_msg
    ; INT 21h
"""

        # Generar movimientos para cada motor
        if 'base' in motor_values:
            asm_code += f"""
    ; === CONTROL MOTOR BASE ===
    ; Mover base a {motor_values['base']} grados
    MOV DX, {self.port_addresses['base']}  ; Puerto A (Base)
    CALL MOVE_BASE_{motor_values['base']}
"""

        if 'hombro' in motor_values:
            asm_code += f"""
    ; === CONTROL MOTOR HOMBRO ===
    ; Mover hombro a {motor_values['hombro']} grados
    MOV DX, {self.port_addresses['hombro']}  ; Puerto B (Hombro)
    CALL MOVE_HOMBRO_{motor_values['hombro']}
"""

        if 'codo' in motor_values:
            asm_code += f"""
    ; === CONTROL MOTOR CODO ===
    ; Mover codo a {motor_values['codo']} grados
    MOV DX, {self.port_addresses['codo']}  ; Puerto C (Codo)
    CALL MOVE_CODO_{motor_values['codo']}
"""

        # Finalización del programa
        asm_code += """
    ; === FINALIZACION ===
    ; Apagar todos los motores
    MOV DX, 0300h
    MOV AL, 00h
    OUT DX, AL
    
    MOV DX, 0301h  
    MOV AL, 00h
    OUT DX, AL
    
    MOV DX, 0302h
    MOV AL, 00h
    OUT DX, AL
    
    ; Salir del programa
    MOV AH, 4Ch
    MOV AL, 0
    INT 21h
MAIN ENDP

"""

        # Generar procedimientos de movimiento
        asm_code += self.generate_movement_procedures(motor_values, delay_ms)
        
        # Procedimiento de delay
        asm_code += f"""
;===============================================
; PROCEDIMIENTO DE DELAY
;===============================================
DELAY PROC
    PUSH CX
    PUSH AX
    MOV CX, {delay_ms:04X}h    ; Delay de {delay_ms} ciclos
DELAY_LOOP:
    NOP                        ; No operation
    LOOP DELAY_LOOP
    POP AX
    POP CX
    RET
DELAY ENDP

SHORT_DELAY PROC
    PUSH CX
    MOV CX, 1000h              ; Delay corto
SHORT_DELAY_LOOP:
    NOP
    LOOP SHORT_DELAY_LOOP
    POP CX
    RET
SHORT_DELAY ENDP

END MAIN
"""
        
        return asm_code
    
    def generate_movement_procedures(self, motor_values, delay_ms):
        """Genera los procedimientos de movimiento específicos para cada motor"""
        procedures = ""
        
        # Procedimiento para motor base
        if 'base' in motor_values:
            angle = motor_values['base']
            steps = self.calculate_steps_for_angle(angle)
            
            procedures += f"""
;===============================================
; PROCEDIMIENTO MOTOR BASE - {angle} GRADOS
;===============================================
MOVE_BASE_{angle} PROC
    PUSH CX
    PUSH AX
    
    ; Ejecutar {steps} pasos para {angle} grados
    MOV CX, {steps}            ; Número de pasos
STEP_LOOP_BASE_{angle}:
"""
            
            # Generar secuencia de pasos
            for i, pattern in enumerate(self.step_patterns[:4]):  # 4 pasos básicos
                procedures += f"""    MOV AL, {pattern}         ; Patrón de paso {i+1}
    OUT DX, AL
    CALL SHORT_DELAY
"""
            
            procedures += f"""    LOOP STEP_LOOP_BASE_{angle}
    
    POP AX
    POP CX
    RET
MOVE_BASE_{angle} ENDP
"""

        # Procedimiento para motor hombro
        if 'hombro' in motor_values:
            angle = motor_values['hombro']
            steps = self.calculate_steps_for_angle(angle)
            
            procedures += f"""
;===============================================
; PROCEDIMIENTO MOTOR HOMBRO - {angle} GRADOS
;===============================================
MOVE_HOMBRO_{angle} PROC
    PUSH CX
    PUSH AX
    
    ; Ejecutar {steps} pasos para {angle} grados
    MOV CX, {steps}            ; Número de pasos
STEP_LOOP_HOMBRO_{angle}:
"""
            
            # Generar secuencia de pasos
            for i, pattern in enumerate(self.step_patterns[:4]):
                procedures += f"""    MOV AL, {pattern}         ; Patrón de paso {i+1}
    OUT DX, AL
    CALL SHORT_DELAY
"""
            
            procedures += f"""    LOOP STEP_LOOP_HOMBRO_{angle}
    
    POP AX
    POP CX
    RET
MOVE_HOMBRO_{angle} ENDP
"""

        # Procedimiento para motor codo
        if 'codo' in motor_values:
            angle = motor_values['codo']
            steps = self.calculate_steps_for_angle(angle)
            
            procedures += f"""
;===============================================
; PROCEDIMIENTO MOTOR CODO - {angle} GRADOS
;===============================================
MOVE_CODO_{angle} PROC
    PUSH CX
    PUSH AX
    
    ; Ejecutar {steps} pasos para {angle} grados
    MOV CX, {steps}            ; Número de pasos
STEP_LOOP_CODO_{angle}:
"""
            
            # Generar secuencia de pasos
            for i, pattern in enumerate(self.step_patterns[:4]):
                procedures += f"""    MOV AL, {pattern}         ; Patrón de paso {i+1}
    OUT DX, AL
    CALL SHORT_DELAY
"""
            
            procedures += f"""    LOOP STEP_LOOP_CODO_{angle}
    
    POP AX
    POP CX
    RET
MOVE_CODO_{angle} ENDP
"""
        
        return procedures
    
    def calculate_steps_for_angle(self, angle):
        """Calcula el número de pasos necesarios para un ángulo dado"""
        # Asumiendo motor paso a paso de 1.8° por paso (200 pasos por revolución)
        steps_per_degree = 200 / 360  # aproximadamente 0.56 pasos por grado
        steps = int(angle * steps_per_degree)
        return max(1, steps)  # Mínimo 1 paso

# Test del generador
if __name__ == "__main__":
    generator = ProteusAssemblyGenerator()
    
    # Datos de prueba basados en la sintaxis del usuario
    test_commands = [
        {'base': 45},
        {'hombro': 120},
        {'codo': 90},
        {'espera': 1}
    ]
    
    asm_code = generator.generate_from_robot_data(test_commands, "r1_proteus")
    
    print("=== CÓDIGO ASSEMBLY PARA PROTEUS ===")
    print(asm_code)
    
    # Guardar el código
    with open("r1_proteus.asm", 'w', encoding='ascii', errors='ignore') as f:
        f.write(asm_code)
    
    print(f"\n✅ Código guardado en: r1_proteus.asm")
    print(f"📏 Tamaño: {len(asm_code)} caracteres")
