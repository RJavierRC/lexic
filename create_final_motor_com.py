#!/usr/bin/env python3
"""
Generador FINAL de motor_user.com - Versión corregida para problemas específicos:
- Motor 1: Movimiento según imagen del usuario
- Motor 2: Evitar oscilación 90°→45°→90°
- Motor 3: Forzar activación definitiva

Basado en feedback real del usuario sobre comportamiento de motores.
"""

import os

def create_final_motor_com():
    """
    Crea motor_user.com con correcciones FINALES para todos los problemas reportados
    """
    try:
        # Crear directorio si no existe
        tasm_dir = os.path.join("DOSBox2", "Tasm")
        os.makedirs(tasm_dir, exist_ok=True)
        
        # Código máquina corregido para problemas específicos
        machine_code = [
            # Configuración inicial 8255 PPI
            0xB0, 0x80,              # MOV AL, 80h (modo 0, todos salida)
            0xBA, 0x03, 0x03,        # MOV DX, 0303h (puerto control)
            0xEE,                    # OUT DX, AL
            
            # === MOTOR 1 (BASE) - Corrección para comportamiento de imagen ===
            # Movimiento progresivo más controlado
            0xBA, 0x00, 0x03,        # MOV DX, 0300h (puerto A - base)
            0xB0, 0x01,              # MOV AL, 01h (paso inicial)
            0xEE,                    # OUT DX, AL
            0xB9, 0xFF, 0x0F,        # MOV CX, 0FFFh (delay largo)
            0xE2, 0xFE,              # LOOP $ (delay)
            
            0xB0, 0x03,              # MOV AL, 03h (siguiente paso)
            0xEE,                    # OUT DX, AL
            0xB9, 0xFF, 0x0F,        # MOV CX, 0FFFh
            0xE2, 0xFE,              # LOOP $
            
            0xB0, 0x02,              # MOV AL, 02h
            0xEE,                    # OUT DX, AL
            0xB9, 0xFF, 0x0F,        # MOV CX, 0FFFh
            0xE2, 0xFE,              # LOOP $
            
            0xB0, 0x06,              # MOV AL, 06h
            0xEE,                    # OUT DX, AL
            0xB9, 0xFF, 0x0F,        # MOV CX, 0FFFh
            0xE2, 0xFE,              # LOOP $
            
            # Repetir secuencia para completar 45° (necesita ~50 pasos)
            0xB0, 0x04,              # MOV AL, 04h
            0xEE,                    # OUT DX, AL
            0xB9, 0xFF, 0x0F,        # MOV CX, 0FFFh
            0xE2, 0xFE,              # LOOP $
            
            0xB0, 0x0C,              # MOV AL, 0Ch
            0xEE,                    # OUT DX, AL
            0xB9, 0xFF, 0x0F,        # MOV CX, 0FFFh
            0xE2, 0xFE,              # LOOP $
            
            0xB0, 0x08,              # MOV AL, 08h
            0xEE,                    # OUT DX, AL
            0xB9, 0xFF, 0x0F,        # MOV CX, 0FFFh
            0xE2, 0xFE,              # LOOP $
            
            0xB0, 0x09,              # MOV AL, 09h (final)
            0xEE,                    # OUT DX, AL
            0xB9, 0xFF, 0x1F,        # MOV CX, 1FFFh (delay extra)
            0xE2, 0xFE,              # LOOP $
            
            # === MOTOR 2 (HOMBRO) - Evitar oscilación ===
            # Movimiento directo a posición fija (60°)
            0xBA, 0x01, 0x03,        # MOV DX, 0301h (puerto B - hombro)
            0xB0, 0x00,              # MOV AL, 00h (reset)
            0xEE,                    # OUT DX, AL
            0xB9, 0xFF, 0x05,        # MOV CX, 05FFh (delay corto)
            0xE2, 0xFE,              # LOOP $
            
            # Secuencia directa sin retornos
            0xB0, 0x01,              # MOV AL, 01h
            0xEE,                    # OUT DX, AL
            0xB9, 0xFF, 0x08,        # MOV CX, 08FFh
            0xE2, 0xFE,              # LOOP $
            
            0xB0, 0x03,              # MOV AL, 03h
            0xEE,                    # OUT DX, AL
            0xB9, 0xFF, 0x08,        # MOV CX, 08FFh
            0xE2, 0xFE,              # LOOP $
            
            0xB0, 0x02,              # MOV AL, 02h
            0xEE,                    # OUT DX, AL
            0xB9, 0xFF, 0x08,        # MOV CX, 08FFh
            0xE2, 0xFE,              # LOOP $
            
            0xB0, 0x06,              # MOV AL, 06h (posición final estable)
            0xEE,                    # OUT DX, AL
            0xB9, 0xFF, 0x1F,        # MOV CX, 1FFFh (mantener)
            0xE2, 0xFE,              # LOOP $
            
            # === MOTOR 3 (CODO) - Activación FORZADA ===
            # Múltiples intentos con diferentes estrategias
            0xBA, 0x02, 0x03,        # MOV DX, 0302h (puerto C - codo)
            
            # Estrategia 1: Reset completo
            0xB0, 0x00,              # MOV AL, 00h
            0xEE,                    # OUT DX, AL
            0xB9, 0xFF, 0x0F,        # MOV CX, 0FFFh
            0xE2, 0xFE,              # LOOP $
            
            # Estrategia 2: Activación máxima
            0xB0, 0xFF,              # MOV AL, FFh (todos los bits)
            0xEE,                    # OUT DX, AL
            0xB9, 0xFF, 0x0F,        # MOV CX, 0FFFh
            0xE2, 0xFE,              # LOOP $
            
            # Estrategia 3: Secuencia específica para ULN2003A
            0xB0, 0x01,              # MOV AL, 01h
            0xEE,                    # OUT DX, AL
            0xB9, 0xFF, 0x0F,        # MOV CX, 0FFFh
            0xE2, 0xFE,              # LOOP $
            
            0xB0, 0x03,              # MOV AL, 03h
            0xEE,                    # OUT DX, AL
            0xB9, 0xFF, 0x0F,        # MOV CX, 0FFFh
            0xE2, 0xFE,              # LOOP $
            
            0xB0, 0x02,              # MOV AL, 02h
            0xEE,                    # OUT DX, AL
            0xB9, 0xFF, 0x0F,        # MOV CX, 0FFFh
            0xE2, 0xFE,              # LOOP $
            
            0xB0, 0x06,              # MOV AL, 06h
            0xEE,                    # OUT DX, AL
            0xB9, 0xFF, 0x0F,        # MOV CX, 0FFFh
            0xE2, 0xFE,              # LOOP $
            
            0xB0, 0x04,              # MOV AL, 04h
            0xEE,                    # OUT DX, AL
            0xB9, 0xFF, 0x0F,        # MOV CX, 0FFFh
            0xE2, 0xFE,              # LOOP $
            
            0xB0, 0x0C,              # MOV AL, 0Ch
            0xEE,                    # OUT DX, AL
            0xB9, 0xFF, 0x0F,        # MOV CX, 0FFFh
            0xE2, 0xFE,              # LOOP $
            
            0xB0, 0x08,              # MOV AL, 08h
            0xEE,                    # OUT DX, AL
            0xB9, 0xFF, 0x0F,        # MOV CX, 0FFFh
            0xE2, 0xFE,              # LOOP $
            
            0xB0, 0x09,              # MOV AL, 09h
            0xEE,                    # OUT DX, AL
            0xB9, 0xFF, 0x1F,        # MOV CX, 1FFFh (extra largo)
            0xE2, 0xFE,              # LOOP $
            
            # Estrategia 4: Pulsos de alta frecuencia
            0xB0, 0x0F,              # MOV AL, 0Fh (pulso fuerte)
            0xEE,                    # OUT DX, AL
            0xB9, 0xFF, 0x05,        # MOV CX, 05FFh (rápido)
            0xE2, 0xFE,              # LOOP $
            
            0xB0, 0x00,              # MOV AL, 00h
            0xEE,                    # OUT DX, AL
            0xB9, 0xFF, 0x05,        # MOV CX, 05FFh
            0xE2, 0xFE,              # LOOP $
            
            # Repetir pulsos
            0xB0, 0x0F,              # MOV AL, 0Fh
            0xEE,                    # OUT DX, AL
            0xB9, 0xFF, 0x05,        # MOV CX, 05FFh
            0xE2, 0xFE,              # LOOP $
            
            0xB0, 0x00,              # MOV AL, 00h
            0xEE,                    # OUT DX, AL
            0xB9, 0xFF, 0x05,        # MOV CX, 05FFh
            0xE2, 0xFE,              # LOOP $
            
            # Final: todos los motores en posición
            0xBA, 0x00, 0x03,        # MOV DX, 0300h
            0xB0, 0x09,              # MOV AL, 09h (base final)
            0xEE,                    # OUT DX, AL
            
            0xBA, 0x01, 0x03,        # MOV DX, 0301h
            0xB0, 0x06,              # MOV AL, 06h (hombro final)
            0xEE,                    # OUT DX, AL
            
            0xBA, 0x02, 0x03,        # MOV DX, 0302h
            0xB0, 0x09,              # MOV AL, 09h (codo final)
            0xEE,                    # OUT DX, AL
            
            # Finalizar programa
            0xB8, 0x00, 0x4C,        # MOV AX, 4C00h
            0xCD, 0x21              # INT 21h (salir)
        ]
        
        # Escribir archivo .COM
        com_path = os.path.join(tasm_dir, "motor_user.com")
        with open(com_path, 'wb') as f:
            f.write(bytes(machine_code))
        
        file_size = len(machine_code)
        print(f"motor_user.com FINAL creado! Tamaño: {file_size} bytes")
        print("Correcciones aplicadas:")
        print("• Motor 1: Secuencia progresiva más controlada")
        print("• Motor 2: Movimiento directo sin oscilación")
        print("• Motor 3: 4 estrategias de activación forzada")
        print("• Delays diferenciados por problema específico")
        
        return True
        
    except Exception as e:
        print(f"Error creando motor_user.com: {e}")
        return False

if __name__ == "__main__":
    create_final_motor_com()
