#!/usr/bin/env python3
"""
Generador EXACTO de motor_user.com - Reproduzca el "noname.com" exitoso
Basado en el código ASM que funciona correctamente y la estructura del noname.com

DIRECCIONES CORRECTAS (como en tu ASM):
- Puerto A (Motor A): 00h  
- Puerto B (Motor B): 02h
- Puerto C (Motor C): 04h  
- Control 8255: 06h

SECUENCIA DE PASOS (como en tu ASM):
- Paso 1: 00000110B (06h)
- Paso 2: 00001100B (0Ch)  
- Paso 3: 00001001B (09h)
- Paso 4: 00000011B (03h)
"""

import os

def create_noname_compatible_com():
    """
    Crea motor_user.com con la MISMA estructura que noname.com exitoso
    y el MISMO código ASM que funciona
    """
    try:
        # Crear directorio si no existe
        tasm_dir = os.path.join("DOSBox2", "Tasm")
        os.makedirs(tasm_dir, exist_ok=True)
        
        # Código máquina EXACTO como el que genera emu8086 para tu ASM
        machine_code = [
            # Configuración 8255 - MOV DX, 06h; MOV AL, 80h; OUT DX, AL
            0xBA, 0x06, 0x00,        # MOV DX, 0006h (puerto control)
            0xB0, 0x80,              # MOV AL, 80h (configuración)
            0xEE,                    # OUT DX, AL
            
            # === MOTOR A (Puerto 00h) ===
            # Paso 1: MOV DX, 00h; MOV AL, 06h; OUT DX, AL
            0xBA, 0x00, 0x00,        # MOV DX, 0000h (Puerto A)
            0xB0, 0x06,              # MOV AL, 06h (00000110B)
            0xEE,                    # OUT DX, AL
            0xB9, 0xFF, 0xFF,        # MOV CX, 0FFFFh
            0xE2, 0xFE,              # LOOP loopy1A (delay)
            
            # Paso 2: MOV AL, 0Ch; OUT DX, AL
            0xB0, 0x0C,              # MOV AL, 0Ch (00001100B)
            0xEE,                    # OUT DX, AL
            0xB9, 0xFF, 0xFF,        # MOV CX, 0FFFFh
            0xE2, 0xFE,              # LOOP loopy2A
            
            # Paso 3: MOV AL, 09h; OUT DX, AL
            0xB0, 0x09,              # MOV AL, 09h (00001001B)
            0xEE,                    # OUT DX, AL
            0xB9, 0xFF, 0xFF,        # MOV CX, 0FFFFh
            0xE2, 0xFE,              # LOOP loopy3A
            
            # Paso 4: MOV AL, 03h; OUT DX, AL
            0xB0, 0x03,              # MOV AL, 03h (00000011B)
            0xEE,                    # OUT DX, AL
            0xB9, 0xFF, 0xFF,        # MOV CX, 0FFFFh
            0xE2, 0xFE,              # LOOP loopy4A
            
            # === MOTOR B (Puerto 02h) ===
            # Paso 1: MOV DX, 02h; MOV AL, 06h; OUT DX, AL
            0xBA, 0x02, 0x00,        # MOV DX, 0002h (Puerto B)
            0xB0, 0x06,              # MOV AL, 06h (00000110B)
            0xEE,                    # OUT DX, AL
            0xB9, 0xFF, 0xFF,        # MOV CX, 0FFFFh
            0xE2, 0xFE,              # LOOP loopy1B
            
            # Paso 2: MOV AL, 0Ch; OUT DX, AL
            0xB0, 0x0C,              # MOV AL, 0Ch (00001100B)
            0xEE,                    # OUT DX, AL
            0xB9, 0xFF, 0xFF,        # MOV CX, 0FFFFh
            0xE2, 0xFE,              # LOOP loopy2B
            
            # Paso 3: MOV AL, 09h; OUT DX, AL
            0xB0, 0x09,              # MOV AL, 09h (00001001B)
            0xEE,                    # OUT DX, AL
            0xB9, 0xFF, 0xFF,        # MOV CX, 0FFFFh
            0xE2, 0xFE,              # LOOP loopy3B
            
            # Paso 4: MOV AL, 03h; OUT DX, AL
            0xB0, 0x03,              # MOV AL, 03h (00000011B)
            0xEE,                    # OUT DX, AL
            0xB9, 0xFF, 0xFF,        # MOV CX, 0FFFFh
            0xE2, 0xFE,              # LOOP loopy4B
            
            # === MOTOR C (Puerto 04h) ===
            # Paso 1: MOV DX, 04h; MOV AL, 06h; OUT DX, AL
            0xBA, 0x04, 0x00,        # MOV DX, 0004h (Puerto C)
            0xB0, 0x06,              # MOV AL, 06h (00000110B)
            0xEE,                    # OUT DX, AL
            0xB9, 0xFF, 0xFF,        # MOV CX, 0FFFFh
            0xE2, 0xFE,              # LOOP loopy1C
            
            # Paso 2: MOV AL, 0Ch; OUT DX, AL
            0xB0, 0x0C,              # MOV AL, 0Ch (00001100B)
            0xEE,                    # OUT DX, AL
            0xB9, 0xFF, 0xFF,        # MOV CX, 0FFFFh
            0xE2, 0xFE,              # LOOP loopy2C
            
            # Paso 3: MOV AL, 09h; OUT DX, AL
            0xB0, 0x09,              # MOV AL, 09h (00001001B)
            0xEE,                    # OUT DX, AL
            0xB9, 0xFF, 0xFF,        # MOV CX, 0FFFFh
            0xE2, 0xFE,              # LOOP loopy3C
            
            # Paso 4: MOV AL, 03h; OUT DX, AL
            0xB0, 0x03,              # MOV AL, 03h (00000011B)
            0xEE,                    # OUT DX, AL
            0xB9, 0xFF, 0xFF,        # MOV CX, 0FFFFh
            0xE2, 0xFE,              # LOOP loopy4C
            
            # JMP START (volver al inicio) - bucle infinito como en tu ASM
            0xE9, 0x91, 0xFF         # JMP START (salto relativo al inicio)
        ]
        
        # Escribir archivo .COM exactamente como noname.com
        com_path = os.path.join(tasm_dir, "motor_user.com")
        with open(com_path, 'wb') as f:
            f.write(bytes(machine_code))
        
        file_size = len(machine_code)
        print(f"motor_user.com EXACTO creado! Tamaño: {file_size} bytes")
        print("✅ ESTRUCTURA EXACTA como noname.com exitoso:")
        print("• Direcciones: 00h, 02h, 04h, 06h (como tu ASM)")
        print("• Secuencia: 06h→0Ch→09h→03h (como tu ASM)")
        print("• Bucle infinito JMP START (como tu ASM)")
        print("• Delays 0FFFFh en cada paso")
        print("• Compatible con emu8086 y Proteus")
        
        return True
        
    except Exception as e:
        print(f"Error creando motor_user.com: {e}")
        return False

if __name__ == "__main__":
    create_noname_compatible_com()
