#!/usr/bin/env python3
"""
Generador de código ASM DINÁMICO basado en valores del usuario
Lee los valores de la sintaxis Robot y genera código ASM personalizado
"""

import os
from datetime import datetime

class DynamicASMGenerator:
    """Generador de código ASM dinámico basado en valores del usuario"""
    
    def __init__(self):
        self.port_addresses = {
            'base': '00h',      # Puerto A del 8255 (como en tu ASM exitoso)
            'hombro': '02h',    # Puerto B del 8255
            'codo': '04h',      # Puerto C del 8255  
            'config': '06h'     # Puerto de configuración del 8255
        }
    
    def generate_dynamic_asm(self, analyzer, program_name="robot_dynamic"):
        """
        Genera código ASM dinámico basado en los valores del analizador
        """
        # Extraer valores del código del usuario
        motor_values = self.extract_motor_values(analyzer)
        
        print(f"🎯 Generando ASM con valores dinámicos:")
        for component, value in motor_values.items():
            print(f"• {component}: {value}")
        
        # Generar código ASM
        asm_code = self.create_asm_code(motor_values, program_name)
        
        return asm_code
    
    def extract_motor_values(self, analyzer):
        """
        Extrae valores de motores del código Robot parseado
        """
        motor_values = {
            'base': 45,
            'hombro': 90, 
            'codo': 60,
            'velocidad': 2,
            'espera': 1
        }
        
        try:
            # Extraer de tokens del analizador
            if hasattr(analyzer, 'tokens') and analyzer.tokens:
                i = 0
                while i < len(analyzer.tokens) - 2:
                    token = analyzer.tokens[i]
                    if (hasattr(token, 'type') and hasattr(token, 'value')):
                        
                        # Buscar componentes (pueden ser KEYWORD o COMPONENT)
                        if token.type in ['COMPONENT', 'KEYWORD']:
                            component = token.value.lower()
                            if component in motor_values:
                                # Buscar el valor después del '=' (puede ser ASSIGN o ASSIGN_OP)
                                if (i + 2 < len(analyzer.tokens) and 
                                    hasattr(analyzer.tokens[i + 1], 'type') and 
                                    analyzer.tokens[i + 1].type in ['ASSIGN', 'ASSIGN_OP']):
                                    
                                    value_token = analyzer.tokens[i + 2]
                                    if hasattr(value_token, 'value'):
                                        try:
                                            motor_values[component] = float(value_token.value)
                                            print(f"✅ Extraído {component} = {value_token.value}")
                                        except ValueError:
                                            print(f"⚠️ Valor inválido para {component}: {value_token.value}")
                    i += 1
                    
        except Exception as e:
            print(f"⚠️ Error extrayendo valores: {e}")
        
        return motor_values
    
    def create_asm_code(self, motor_values, program_name):
        """
        Crea código ASM personalizado basado en los valores
        """
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Calcular pasos dinámicos
        base_steps = self.angle_to_steps(motor_values['base'])
        hombro_steps = self.angle_to_steps(motor_values['hombro'])  
        codo_steps = self.angle_to_steps(motor_values['codo'])
        
        # Calcular delays dinámicos
        base_delay = self.calculate_delay(motor_values['velocidad'], motor_values['espera'])
        hombro_delay = self.calculate_delay(motor_values['velocidad'], motor_values['espera'])
        codo_delay = self.calculate_delay(motor_values['velocidad'], motor_values['espera'])
        
        asm_code = f"""; ----------------------------------------------
; CONTROL DINÁMICO DE TRES MOTORES PASO A PASO (8255)
; Programa: {program_name}
; Generado: {timestamp}
; Basado en código Robot del usuario
; ----------------------------------------------
; VALORES EXTRAÍDOS DEL CÓDIGO:
;   r1.base = {motor_values['base']}° → {base_steps} pasos
;   r1.hombro = {motor_values['hombro']}° → {hombro_steps} pasos  
;   r1.codo = {motor_values['codo']}° → {codo_steps} pasos
;   r1.velocidad = {motor_values['velocidad']}
;   r1.espera = {motor_values['espera']}s
; ----------------------------------------------

CODE        SEGMENT

PORTA   EQU {self.port_addresses['base']}            ; Dirección Puerto A - BASE
PORTB   EQU {self.port_addresses['hombro']}          ; Dirección Puerto B - HOMBRO
PORTC   EQU {self.port_addresses['codo']}            ; Dirección Puerto C - CODO
Config  EQU {self.port_addresses['config']}          ; Dirección registro de configuración

        ORG 100H           ; Programa COM (para DOS Box o imagen binaria)

;------ Inicialización del 8255 ------------------------
        MOV     DX, Config
        MOV     AL, 10000000B   ; 80h → A, B, C como salidas
        OUT     DX, AL

;=======================================================
START:
;======== MOTOR BASE (Puerto A) - {motor_values['base']}° ===========================
        MOV     DX, PORTA
        ; Ejecutar {base_steps} pasos para {motor_values['base']} grados
        MOV     CX, {base_steps}
BASE_LOOP:
        MOV     AL, 00000110B        ; Paso 1
        OUT     DX, AL
        MOV     BX, {base_delay}
        CALL    DELAY_ROUTINE

        MOV     AL, 00001100B        ; Paso 2
        OUT     DX, AL
        MOV     BX, {base_delay}
        CALL    DELAY_ROUTINE

        MOV     AL, 00001001B        ; Paso 3
        OUT     DX, AL
        MOV     BX, {base_delay}
        CALL    DELAY_ROUTINE

        MOV     AL, 00000011B        ; Paso 4
        OUT     DX, AL
        MOV     BX, {base_delay}
        CALL    DELAY_ROUTINE
        
        LOOP    BASE_LOOP

;======== MOTOR HOMBRO (Puerto B) - {motor_values['hombro']}° ===========================
        MOV     DX, PORTB
        ; Ejecutar {hombro_steps} pasos para {motor_values['hombro']} grados
        MOV     CX, {hombro_steps}
HOMBRO_LOOP:
        MOV     AL, 00000110B        ; Paso 1
        OUT     DX, AL
        MOV     BX, {hombro_delay}
        CALL    DELAY_ROUTINE

        MOV     AL, 00001100B        ; Paso 2
        OUT     DX, AL
        MOV     BX, {hombro_delay}
        CALL    DELAY_ROUTINE

        MOV     AL, 00001001B        ; Paso 3
        OUT     DX, AL
        MOV     BX, {hombro_delay}
        CALL    DELAY_ROUTINE

        MOV     AL, 00000011B        ; Paso 4
        OUT     DX, AL
        MOV     BX, {hombro_delay}
        CALL    DELAY_ROUTINE
        
        LOOP    HOMBRO_LOOP

;======== MOTOR CODO (Puerto C) - {motor_values['codo']}° ===========================
        MOV     DX, PORTC
        ; Ejecutar {codo_steps} pasos para {motor_values['codo']} grados
        MOV     CX, {codo_steps}
CODO_LOOP:
        MOV     AL, 00000110B        ; Paso 1
        OUT     DX, AL
        MOV     BX, {codo_delay}
        CALL    DELAY_ROUTINE

        MOV     AL, 00001100B        ; Paso 2
        OUT     DX, AL
        MOV     BX, {codo_delay}
        CALL    DELAY_ROUTINE

        MOV     AL, 00001001B        ; Paso 3
        OUT     DX, AL
        MOV     BX, {codo_delay}
        CALL    DELAY_ROUTINE

        MOV     AL, 00000011B        ; Paso 4
        OUT     DX, AL
        MOV     BX, {codo_delay}
        CALL    DELAY_ROUTINE
        
        LOOP    CODO_LOOP

        ; Terminar programa limpiamente
        MOV     AH, 4Ch
        MOV     AL, 0
        INT     21h

;=======================================================
; RUTINA DE DELAY DINÁMICA
; BX contiene el factor de delay
;=======================================================
DELAY_ROUTINE PROC
        PUSH    CX
        PUSH    AX
        MOV     CX, BX
DELAY_LOOP:
        NOP
        NOP
        LOOP    DELAY_LOOP
        POP     AX
        POP     CX
        RET
DELAY_ROUTINE ENDP

CODE        ENDS
        END START
"""

        return asm_code
    
    def angle_to_steps(self, angle):
        """
        Convierte ángulo a número de pasos
        """
        # Motor paso a paso estándar: 1.8° por paso
        steps_per_degree = 200 / 360  # ≈ 0.56 pasos por grado
        steps = max(1, int(angle * steps_per_degree))
        return min(steps, 50)  # Limitar pasos para evitar archivos muy grandes
    
    def calculate_delay(self, velocidad, espera):
        """
        Calcula delay basado en velocidad y tiempo de espera
        """
        base_delay = 0x1000
        
        # Velocidad más alta = delay menor
        velocity_factor = max(1, int(velocidad))
        delay = base_delay // velocity_factor
        
        # Tiempo de espera afecta el delay
        wait_factor = max(1, int(espera * 1000))
        delay = min(delay + wait_factor, 0xFFFF)
        
        return delay

# Función para integrar con robot_lexical_analyzer.py
def generate_dynamic_asm_from_analyzer(analyzer, program_name="robot_dynamic"):
    """
    Función principal para generar ASM dinámico desde el analizador
    """
    generator = DynamicASMGenerator()
    return generator.generate_dynamic_asm(analyzer, program_name)

if __name__ == "__main__":
    # Test con valores ficticios
    class MockAnalyzer:
        def __init__(self):
            class MockToken:
                def __init__(self, token_type, value):
                    self.type = token_type
                    self.value = value
            
            self.tokens = [
                MockToken('IDENTIFIER', 'r1'),
                MockToken('DOT', '.'),
                MockToken('COMPONENT', 'base'),
                MockToken('ASSIGN', '='),
                MockToken('NUMBER', '20'),
                MockToken('IDENTIFIER', 'r1'),
                MockToken('DOT', '.'),
                MockToken('COMPONENT', 'hombro'),
                MockToken('ASSIGN', '='),
                MockToken('NUMBER', '100'),
                MockToken('IDENTIFIER', 'r1'),
                MockToken('DOT', '.'),
                MockToken('COMPONENT', 'codo'),
                MockToken('ASSIGN', '='),
                MockToken('NUMBER', '50')
            ]
    
    mock_analyzer = MockAnalyzer()
    asm_code = generate_dynamic_asm_from_analyzer(mock_analyzer, "test_dynamic")
    print("=== CÓDIGO ASM GENERADO ===")
    print(asm_code)
