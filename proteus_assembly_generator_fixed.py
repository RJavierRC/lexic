#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generador de Assembly específicamente optimizado para Proteus - VERSIÓN CORREGIDA
Usa formato .MODEL SMALL y direcciones de puerto estándar sin problemas de formato
"""

from datetime import datetime

class ProteusAssemblyGeneratorFixed:
    """Generador de código assembly compatible con Proteus - VERSIÓN CORREGIDA"""
    
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
            '06h'   # Paso 4: 0110
        ]
    
    def generate_from_robot_data(self, robot_commands, program_name="robot_control"):
        """Genera assembly a partir de comandos de robot analizados"""
        
        # Extraer datos de los comandos
        motor_values = {}
        delay_value = 1000  # Delay por defecto
        
        for command in robot_commands:
            if 'base' in command:
                motor_values['base'] = int(float(command['base']))  # Convertir a entero
            elif 'hombro' in command:
                motor_values['hombro'] = int(float(command['hombro']))
            elif 'codo' in command:
                motor_values['codo'] = int(float(command['codo']))
            elif 'espera' in command:
                delay_value = int(command['espera'] * 1000)  # Convertir a ms
        
        return self.generate_proteus_compatible(motor_values, delay_value, program_name)
    
    def generate_proteus_compatible(self, motor_values, delay_ms=1000, program_name="robot_control"):
        """Genera código assembly completamente compatible con Proteus - SIN PROBLEMAS DE FORMATO"""
        
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # INICIO DEL CÓDIGO - SIN LÍNEAS EXTRAÑAS
        asm_code = f""";===============================================
; CONTROL DE MOTORES PARA SIMULACION PROTEUS
; Programa: {program_name}
; Generado: {timestamp}
; Compatible: 8086/8088 + 8255 PPI
;===============================================

.MODEL SMALL
.STACK 100h

.DATA
    motor_base     DB ?
    motor_hombro   DB ?  
    motor_codo     DB ?
    delay_count    DW ?

.CODE
MAIN PROC
    ; Inicializar segmento de datos
    MOV AX, @DATA
    MOV DS, AX
    
    ; Configurar 8255 PPI como outputs
    MOV DX, {self.port_addresses['config']}
    MOV AL, 80h
    OUT DX, AL
"""

        # Generar movimientos para cada motor con nombres simples
        if 'base' in motor_values:
            angle = motor_values['base']
            asm_code += f"""
    ; Control motor base - {angle} grados
    MOV DX, {self.port_addresses['base']}
    CALL MOVE_BASE
"""

        if 'hombro' in motor_values:
            angle = motor_values['hombro']
            asm_code += f"""
    ; Control motor hombro - {angle} grados  
    MOV DX, {self.port_addresses['hombro']}
    CALL MOVE_HOMBRO
"""

        if 'codo' in motor_values:
            angle = motor_values['codo']
            asm_code += f"""
    ; Control motor codo - {angle} grados
    MOV DX, {self.port_addresses['codo']}
    CALL MOVE_CODO
"""

        # Finalización del programa
        asm_code += """
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

        # Generar procedimientos de movimiento SIMPLES
        asm_code += self.generate_movement_procedures_fixed(motor_values)
        
        # Procedimiento de delay
        asm_code += """
;===============================================
; PROCEDIMIENTO DE DELAY
;===============================================
DELAY PROC
    PUSH CX
    PUSH AX
    MOV CX, 03E8h
DELAY_LOOP:
    NOP
    LOOP DELAY_LOOP
    POP AX
    POP CX
    RET
DELAY ENDP

SHORT_DELAY PROC
    PUSH CX
    MOV CX, 0100h
SHORT_DELAY_LOOP:
    NOP
    LOOP SHORT_DELAY_LOOP
    POP CX
    RET
SHORT_DELAY ENDP

END MAIN
"""
        
        return asm_code
    
    def generate_movement_procedures_fixed(self, motor_values):
        """Genera procedimientos de movimiento con nombres SIMPLES"""
        procedures = ""
        
        if 'base' in motor_values:
            angle = motor_values['base']
            steps = self.calculate_steps(angle, 360)
            procedures += f"""
;===============================================
; PROCEDIMIENTO MOTOR BASE
;===============================================
MOVE_BASE PROC
    PUSH CX
    PUSH AX
    
    MOV CX, {steps}
STEP_LOOP_BASE:
    MOV AL, 01h
    OUT DX, AL
    CALL SHORT_DELAY
    MOV AL, 03h
    OUT DX, AL
    CALL SHORT_DELAY
    MOV AL, 02h
    OUT DX, AL
    CALL SHORT_DELAY
    MOV AL, 06h
    OUT DX, AL
    CALL SHORT_DELAY
    LOOP STEP_LOOP_BASE
    
    POP AX
    POP CX
    RET
MOVE_BASE ENDP
"""
        
        if 'hombro' in motor_values:
            angle = motor_values['hombro']
            steps = self.calculate_steps(angle, 180)
            procedures += f"""
;===============================================
; PROCEDIMIENTO MOTOR HOMBRO
;===============================================
MOVE_HOMBRO PROC
    PUSH CX
    PUSH AX
    
    MOV CX, {steps}
STEP_LOOP_HOMBRO:
    MOV AL, 01h
    OUT DX, AL
    CALL SHORT_DELAY
    MOV AL, 03h
    OUT DX, AL
    CALL SHORT_DELAY
    MOV AL, 02h
    OUT DX, AL
    CALL SHORT_DELAY
    MOV AL, 06h
    OUT DX, AL
    CALL SHORT_DELAY
    LOOP STEP_LOOP_HOMBRO
    
    POP AX
    POP CX
    RET
MOVE_HOMBRO ENDP
"""
            
        if 'codo' in motor_values:
            angle = motor_values['codo']
            steps = self.calculate_steps(angle, 180)
            procedures += f"""
;===============================================
; PROCEDIMIENTO MOTOR CODO
;===============================================
MOVE_CODO PROC
    PUSH CX
    PUSH AX
    
    MOV CX, {steps}
STEP_LOOP_CODO:
    MOV AL, 01h
    OUT DX, AL
    CALL SHORT_DELAY
    MOV AL, 03h
    OUT DX, AL
    CALL SHORT_DELAY
    MOV AL, 02h
    OUT DX, AL
    CALL SHORT_DELAY
    MOV AL, 06h
    OUT DX, AL
    CALL SHORT_DELAY
    LOOP STEP_LOOP_CODO
    
    POP AX
    POP CX
    RET
MOVE_CODO ENDP
"""
        
        return procedures
    
    def calculate_steps(self, angle, max_angle):
        """Calcula el número de pasos para un ángulo dado"""
        # Motores paso a paso típicos: 200 pasos por revolución (1.8° por paso)
        steps_per_revolution = 200
        steps_per_degree = steps_per_revolution / 360
        
        # Calcular pasos necesarios
        steps = int(angle * steps_per_degree)
        
        # Asegurar valores mínimos/máximos
        return max(1, min(steps, int(max_angle * steps_per_degree)))
    
    def get_motor_info(self):
        """Retorna información sobre la configuración de motores"""
        return {
            'port_addresses': self.port_addresses,
            'step_patterns': self.step_patterns,
            'compatible_with': ['Proteus ISIS', '8086/8088', '8255 PPI']
        }
