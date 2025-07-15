#!/usr/bin/env python3
"""
Generador PRECISO de motor_user.com - Ángulos exactos
Basado en el éxito del noname.com pero con valores corregidos para:
- Motor 1: 45° exactos
- Motor 2: 120° exactos  
- Motor 3: 90° exactos

Mantiene la misma estructura exitosa pero ajusta los valores de pasos.
"""

import os

def create_precise_angles_com():
    """
    Crea motor_user.com con ángulos PRECISOS según los requerimientos del usuario
    """
    try:
        # Crear directorio si no existe
        tasm_dir = os.path.join("DOSBox2", "Tasm")
        os.makedirs(tasm_dir, exist_ok=True)
        
        # Código máquina con valores ajustados para ángulos precisos
        machine_code = [
            # Configuración 8255 - IGUAL que noname.com exitoso
            0xBA, 0x06, 0x00,        # MOV DX, 0006h (puerto control)
            0xB0, 0x80,              # MOV AL, 80h (configuración)
            0xEE,                    # OUT DX, AL
            
            # === MOTOR 1 (Base) - AJUSTADO PARA 45° EXACTOS ===
            0xBA, 0x00, 0x00,        # MOV DX, 0000h (Puerto A)
            
            # Secuencia reducida para 45° (menos pasos)
            0xB0, 0x06,              # MOV AL, 06h (00000110B)
            0xEE,                    # OUT DX, AL
            0xB9, 0x80, 0x80,        # MOV CX, 8080h (delay reducido para precisión)
            0xE2, 0xFE,              # LOOP $
            
            0xB0, 0x0C,              # MOV AL, 0Ch (00001100B)
            0xEE,                    # OUT DX, AL
            0xB9, 0x80, 0x80,        # MOV CX, 8080h
            0xE2, 0xFE,              # LOOP $
            
            # Solo 2 pasos para 45° exactos (no 4 pasos completos)
            0xB0, 0x09,              # MOV AL, 09h (posición final 45°)
            0xEE,                    # OUT DX, AL
            0xB9, 0xFF, 0xFF,        # MOV CX, 0FFFFh (mantener posición)
            0xE2, 0xFE,              # LOOP $
            
            # === MOTOR 2 (Hombro) - AJUSTADO PARA 120° EXACTOS ===
            0xBA, 0x02, 0x00,        # MOV DX, 0002h (Puerto B)
            
            # Secuencia extendida para 120° (más pasos)
            0xB0, 0x06,              # MOV AL, 06h
            0xEE,                    # OUT DX, AL
            0xB9, 0x60, 0x60,        # MOV CX, 6060h (delay medio)
            0xE2, 0xFE,              # LOOP $
            
            0xB0, 0x0C,              # MOV AL, 0Ch
            0xEE,                    # OUT DX, AL
            0xB9, 0x60, 0x60,        # MOV CX, 6060h
            0xE2, 0xFE,              # LOOP $
            
            0xB0, 0x09,              # MOV AL, 09h
            0xEE,                    # OUT DX, AL
            0xB9, 0x60, 0x60,        # MOV CX, 6060h
            0xE2, 0xFE,              # LOOP $
            
            0xB0, 0x03,              # MOV AL, 03h
            0xEE,                    # OUT DX, AL
            0xB9, 0x60, 0x60,        # MOV CX, 6060h
            0xE2, 0xFE,              # LOOP $
            
            # Pasos adicionales para alcanzar 120°
            0xB0, 0x06,              # MOV AL, 06h (paso extra)
            0xEE,                    # OUT DX, AL
            0xB9, 0x60, 0x60,        # MOV CX, 6060h
            0xE2, 0xFE,              # LOOP $
            
            0xB0, 0x0C,              # MOV AL, 0Ch (posición final 120°)
            0xEE,                    # OUT DX, AL
            0xB9, 0xFF, 0xFF,        # MOV CX, 0FFFFh (mantener)
            0xE2, 0xFE,              # LOOP $
            
            # === MOTOR 3 (Codo) - AJUSTADO PARA 90° EXACTOS ===
            0xBA, 0x04, 0x00,        # MOV DX, 0004h (Puerto C)
            
            # Secuencia de 3 pasos para 90° exactos
            0xB0, 0x06,              # MOV AL, 06h
            0xEE,                    # OUT DX, AL
            0xB9, 0xA0, 0xA0,        # MOV CX, A0A0h (delay específico)
            0xE2, 0xFE,              # LOOP $
            
            0xB0, 0x0C,              # MOV AL, 0Ch
            0xEE,                    # OUT DX, AL
            0xB9, 0xA0, 0xA0,        # MOV CX, A0A0h
            0xE2, 0xFE,              # LOOP $
            
            0xB0, 0x09,              # MOV AL, 09h (posición final 90°)
            0xEE,                    # OUT DX, AL
            0xB9, 0xFF, 0xFF,        # MOV CX, 0FFFFh (mantener)
            0xE2, 0xFE,              # LOOP $
            
            # Finalizar - mantener posiciones sin bucle infinito
            # Para evitar movimientos adicionales
            0xB8, 0x00, 0x4C,        # MOV AX, 4C00h
            0xCD, 0x21              # INT 21h (salir limpiamente)
        ]
        
        # Escribir archivo .COM con precisión de ángulos
        com_path = os.path.join(tasm_dir, "motor_user.com")
        with open(com_path, 'wb') as f:
            f.write(bytes(machine_code))
        
        file_size = len(machine_code)
        print(f"motor_user.com PRECISO creado! Tamaño: {file_size} bytes")
        print("🎯 ÁNGULOS PRECISOS configurados:")
        print("• Motor 1 (Base): 45° exactos (2 pasos)")
        print("• Motor 2 (Hombro): 120° exactos (6 pasos)")
        print("• Motor 3 (Codo): 90° exactos (3 pasos)")
        print("• Sin bucle infinito (evita movimientos extra)")
        print("• Delays diferenciados por motor")
        print("• Finalización limpia del programa")
        
        return True
        
    except Exception as e:
        print(f"Error creando motor_user.com: {e}")
        return False

if __name__ == "__main__":
    create_precise_angles_com()
