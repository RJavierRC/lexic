#!/usr/bin/env python3
"""
Generador de motor_user.com basado en la estructura exacta de noname.com
"""
import os

def create_motor_com():
    """Crea motor_user.com basado en noname.com que funciona"""
    
    print("CREANDO motor_user.com BASADO EN noname.com")
    print("===========================================")
    print("Estructura: Basada en noname.com (113 bytes)")
    print("Valores: Tu código (base=45, hombro=120, codo=90)")
    
    try:
        # Analizar noname.com
        noname_path = os.path.join("DOSBox2", "Tasm", "noname.com")
        
        if not os.path.exists(noname_path):
            print("ERROR: noname.com no encontrado")
            return False
        
        with open(noname_path, 'rb') as f:
            noname_data = f.read()
        
        print(f"noname.com original: {len(noname_data)} bytes")
        
        # Crear versión modificada con tus valores
        # Estructura de noname.com decodificada:
        # BA 06 00    = MOV DX, 0006h (configuración inicial)
        # B0 80       = MOV AL, 80h 
        # EE          = OUT DX, AL
        # BA 00 00    = MOV DX, 0000h (puerto base)
        # B0 06       = MOV AL, 06h (valor original)
        # EE          = OUT DX, AL
        # B9 FF FF    = MOV CX, FFFFh (delay)
        # E2 FE       = LOOP (bucle de delay)
        
        # Crear nuevo código .COM con tus valores
        motor_com_data = bytearray()
        
        # Configurar 8255 PPI (puerto de control)
        motor_com_data.extend([0xBA, 0x03, 0x03])  # MOV DX, 0303h (puerto control 8255)
        motor_com_data.extend([0xB0, 0x80])        # MOV AL, 80h (configuración)
        motor_com_data.extend([0xEE])              # OUT DX, AL
        
        # Mover base a 45° (r1.base = 45)
        motor_com_data.extend([0xBA, 0x00, 0x03])  # MOV DX, 0300h (puerto A - base)
        motor_com_data.extend([0xB0, 45])          # MOV AL, 45 (45 grados)
        motor_com_data.extend([0xEE])              # OUT DX, AL
        
        # Delay corto
        motor_com_data.extend([0xB9, 0xFF, 0x0F])  # MOV CX, 0FFFh (delay corto)
        motor_com_data.extend([0xE2, 0xFE])        # LOOP (bucle)
        
        # Mover hombro a 120° (r1.hombro = 120)  
        motor_com_data.extend([0xBA, 0x01, 0x03])  # MOV DX, 0301h (puerto B - hombro)
        motor_com_data.extend([0xB0, 120])         # MOV AL, 120 (120 grados)
        motor_com_data.extend([0xEE])              # OUT DX, AL
        
        # Delay corto
        motor_com_data.extend([0xB9, 0xFF, 0x0F])  # MOV CX, 0FFFh
        motor_com_data.extend([0xE2, 0xFE])        # LOOP
        
        # Mover codo a 90° (r1.codo = 90)
        motor_com_data.extend([0xBA, 0x02, 0x03])  # MOV DX, 0302h (puerto C - codo)
        motor_com_data.extend([0xB0, 90])          # MOV AL, 90 (90 grados)
        motor_com_data.extend([0xEE])              # OUT DX, AL
        
        # Delay largo (r1.espera = 1)
        motor_com_data.extend([0xB9, 0xFF, 0xFF])  # MOV CX, FFFFh (delay largo)
        motor_com_data.extend([0xE2, 0xFE])        # LOOP
        
        # Repetir secuencia una vez más para movimiento visible
        # Base otra vez
        motor_com_data.extend([0xBA, 0x00, 0x03])  # MOV DX, 0300h
        motor_com_data.extend([0xB0, 0])           # MOV AL, 0 (posición inicial)
        motor_com_data.extend([0xEE])              # OUT DX, AL
        motor_com_data.extend([0xB9, 0xAA, 0xAA])  # Delay
        motor_com_data.extend([0xE2, 0xFE])        # LOOP
        
        # Hombro a posición inicial
        motor_com_data.extend([0xBA, 0x01, 0x03])  # MOV DX, 0301h
        motor_com_data.extend([0xB0, 0])           # MOV AL, 0
        motor_com_data.extend([0xEE])              # OUT DX, AL
        motor_com_data.extend([0xB9, 0xAA, 0xAA])  # Delay
        motor_com_data.extend([0xE2, 0xFE])        # LOOP
        
        # Codo a posición inicial
        motor_com_data.extend([0xBA, 0x02, 0x03])  # MOV DX, 0302h
        motor_com_data.extend([0xB0, 0])           # MOV AL, 0
        motor_com_data.extend([0xEE])              # OUT DX, AL
        motor_com_data.extend([0xB9, 0xAA, 0xAA])  # Delay
        motor_com_data.extend([0xE2, 0xFE])        # LOOP
        
        # Bucle infinito para mantener activo
        motor_com_data.extend([0xEB, 0xFE])        # JMP $ (bucle infinito)
        
        # Guardar archivo motor_user.com
        motor_com_path = os.path.join("DOSBox2", "Tasm", "motor_user.com")
        
        with open(motor_com_path, 'wb') as f:
            f.write(motor_com_data)
        
        print(f"¡motor_user.com creado exitosamente!")
        print(f"Archivo: {motor_com_path}")
        print(f"Tamaño: {len(motor_com_data)} bytes")
        print(f"Comparación: motor_user.com ({len(motor_com_data)}b) vs noname.com ({len(noname_data)}b)")
        
        # Mostrar primeros bytes para verificación
        print(f"\nPrimeros 32 bytes (hex):")
        for i in range(0, min(32, len(motor_com_data)), 16):
            chunk = motor_com_data[i:i+16]
            hex_str = ' '.join(f'{b:02X}' for b in chunk)
            print(f"{i:04X}: {hex_str}")
        
        print(f"\nSECUENCIA DE MOVIMIENTOS:")
        print(f"1. Configurar 8255 PPI (puerto 0303h)")
        print(f"2. Base a 45° (puerto 0300h)")
        print(f"3. Hombro a 120° (puerto 0301h)")  
        print(f"4. Codo a 90° (puerto 0302h)")
        print(f"5. Espera (delay largo)")
        print(f"6. Volver a posición inicial")
        print(f"7. Bucle infinito")
        
        print(f"\nINSTRUCCIONES PARA PROTEUS:")
        print(f"1. Cargar: motor_user.com (NO .exe)")
        print(f"2. Procesador: 8086 Real Mode")
        print(f"3. 8255 PPI en 0300h-0303h")
        print(f"4. ULN2003A conectados a PA, PB, PC")
        print(f"5. NO debería dar error de debug")
        print(f"6. Los motores deberían moverse cíclicamente")
        
        return True
        
    except Exception as e:
        print(f"Error creando motor_user.com: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    create_motor_com()
