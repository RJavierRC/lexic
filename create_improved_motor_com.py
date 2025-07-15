#!/usr/bin/env python3
"""
Generador mejorado de motor_user.com para mover TODOS los motores
"""
import os

def create_improved_motor_com():
    """Crea motor_user.com mejorado que mueve todos los motores secuencialmente"""
    
    print("CREANDO motor_user.com MEJORADO")
    print("===============================")
    print("Objetivo: Mover TODOS los motores con valores visibles")
    print("Base: 21.2° (funciona) → 45°")
    print("Hombro: 120° → 60° (más seguro)")  
    print("Codo: 90° → 30° (más seguro)")
    
    try:
        # Crear nuevo código .COM con valores ajustados y delays largos
        motor_com_data = bytearray()
        
        # === CONFIGURACIÓN INICIAL ===
        # Configurar 8255 PPI (puerto de control)
        motor_com_data.extend([0xBA, 0x03, 0x03])  # MOV DX, 0303h (puerto control 8255)
        motor_com_data.extend([0xB0, 0x80])        # MOV AL, 80h (todos puertos como salida)
        motor_com_data.extend([0xEE])              # OUT DX, AL
        
        # Delay inicial largo para estabilización
        motor_com_data.extend([0xB9, 0xFF, 0xFF])  # MOV CX, FFFFh
        motor_com_data.extend([0xE2, 0xFE])        # LOOP (delay largo)
        
        # === SECUENCIA 1: MOTORES A POSICIÓN INICIAL (0°) ===
        print("Secuencia 1: Todos a posición inicial")
        
        # Base a 0°
        motor_com_data.extend([0xBA, 0x00, 0x03])  # MOV DX, 0300h (puerto A - base)
        motor_com_data.extend([0xB0, 0])           # MOV AL, 0 (0 grados)
        motor_com_data.extend([0xEE])              # OUT DX, AL
        motor_com_data.extend([0xB9, 0xFF, 0x7F])  # Delay largo
        motor_com_data.extend([0xE2, 0xFE])        # LOOP
        
        # Hombro a 0°
        motor_com_data.extend([0xBA, 0x01, 0x03])  # MOV DX, 0301h (puerto B - hombro)
        motor_com_data.extend([0xB0, 0])           # MOV AL, 0 (0 grados)
        motor_com_data.extend([0xEE])              # OUT DX, AL
        motor_com_data.extend([0xB9, 0xFF, 0x7F])  # Delay largo
        motor_com_data.extend([0xE2, 0xFE])        # LOOP
        
        # Codo a 0°
        motor_com_data.extend([0xBA, 0x02, 0x03])  # MOV DX, 0302h (puerto C - codo)
        motor_com_data.extend([0xB0, 0])           # MOV AL, 0 (0 grados)
        motor_com_data.extend([0xEE])              # OUT DX, AL
        motor_com_data.extend([0xB9, 0xFF, 0x7F])  # Delay largo
        motor_com_data.extend([0xE2, 0xFE])        # LOOP
        
        # === SECUENCIA 2: MOVER CADA MOTOR INDIVIDUALMENTE ===
        print("Secuencia 2: Movimientos individuales con delays largos")
        
        # 1. Mover SOLO la base a 45° (como tu código original)
        motor_com_data.extend([0xBA, 0x00, 0x03])  # MOV DX, 0300h (puerto A - base)
        motor_com_data.extend([0xB0, 45])          # MOV AL, 45 (45 grados)
        motor_com_data.extend([0xEE])              # OUT DX, AL
        
        # Delay muy largo para que se vea el movimiento
        motor_com_data.extend([0xB9, 0xFF, 0xFF])  # MOV CX, FFFFh (delay máximo)
        motor_com_data.extend([0xE2, 0xFE])        # LOOP
        motor_com_data.extend([0xB9, 0xFF, 0xFF])  # Segundo delay
        motor_com_data.extend([0xE2, 0xFE])        # LOOP
        
        # 2. Mover SOLO el hombro a 60° (valor más conservador)
        motor_com_data.extend([0xBA, 0x01, 0x03])  # MOV DX, 0301h (puerto B - hombro)
        motor_com_data.extend([0xB0, 60])          # MOV AL, 60 (60 grados - más seguro que 120)
        motor_com_data.extend([0xEE])              # OUT DX, AL
        
        # Delay muy largo
        motor_com_data.extend([0xB9, 0xFF, 0xFF])  # MOV CX, FFFFh
        motor_com_data.extend([0xE2, 0xFE])        # LOOP
        motor_com_data.extend([0xB9, 0xFF, 0xFF])  # Segundo delay
        motor_com_data.extend([0xE2, 0xFE])        # LOOP
        
        # 3. Mover SOLO el codo a 30° (valor más conservador)
        motor_com_data.extend([0xBA, 0x02, 0x03])  # MOV DX, 0302h (puerto C - codo)
        motor_com_data.extend([0xB0, 30])          # MOV AL, 30 (30 grados - más seguro que 90)
        motor_com_data.extend([0xEE])              # OUT DX, AL
        
        # Delay muy largo
        motor_com_data.extend([0xB9, 0xFF, 0xFF])  # MOV CX, FFFFh
        motor_com_data.extend([0xE2, 0xFE])        # LOOP
        motor_com_data.extend([0xB9, 0xFF, 0xFF])  # Segundo delay
        motor_com_data.extend([0xE2, 0xFE])        # LOOP
        
        # === SECUENCIA 3: VALORES DE PRUEBA INCREMENTALES ===
        print("Secuencia 3: Pruebas incrementales")
        
        # Hombro valores incrementales para prueba
        for angle in [10, 20, 40, 60]:
            motor_com_data.extend([0xBA, 0x01, 0x03])  # MOV DX, 0301h
            motor_com_data.extend([0xB0, angle])       # MOV AL, angle
            motor_com_data.extend([0xEE])              # OUT DX, AL
            motor_com_data.extend([0xB9, 0xFF, 0x3F])  # Delay medio
            motor_com_data.extend([0xE2, 0xFE])        # LOOP
        
        # Codo valores incrementales para prueba
        for angle in [5, 15, 25, 30]:
            motor_com_data.extend([0xBA, 0x02, 0x03])  # MOV DX, 0302h
            motor_com_data.extend([0xB0, angle])       # MOV AL, angle
            motor_com_data.extend([0xEE])              # OUT DX, AL
            motor_com_data.extend([0xB9, 0xFF, 0x3F])  # Delay medio
            motor_com_data.extend([0xE2, 0xFE])        # LOOP
        
        # === BUCLE INFINITO FINAL ===
        # Bucle infinito para mantener el programa activo
        motor_com_data.extend([0xEB, 0xFE])        # JMP $ (bucle infinito)
        
        # Guardar archivo motor_user.com
        motor_com_path = os.path.join("DOSBox2", "Tasm", "motor_user.com")
        
        with open(motor_com_path, 'wb') as f:
            f.write(motor_com_data)
        
        print(f"\n¡motor_user.com MEJORADO creado!")
        print(f"Archivo: {motor_com_path}")
        print(f"Tamaño: {len(motor_com_data)} bytes")
        
        print(f"\nSECUENCIA DE MOVIMIENTOS MEJORADA:")
        print(f"1. Configurar 8255 PPI")
        print(f"2. Todos motores a 0° (posición inicial)")
        print(f"3. Base a 45° (DELAY LARGO)")
        print(f"4. Hombro a 60° (DELAY LARGO)")
        print(f"5. Codo a 30° (DELAY LARGO)")
        print(f"6. Pruebas incrementales hombro: 10°, 20°, 40°, 60°")
        print(f"7. Pruebas incrementales codo: 5°, 15°, 25°, 30°")
        print(f"8. Bucle infinito")
        
        print(f"\nCAMBIOS PRINCIPALES:")
        print(f"• Delays 4x más largos entre movimientos")
        print(f"• Valores más conservadores (60° vs 120°, 30° vs 90°)")
        print(f"• Secuencia individual por motor")
        print(f"• Pruebas incrementales para verificar respuesta")
        print(f"• Posición inicial a 0° para todos")
        
        print(f"\nINSTRUCCIONES PROTEUS:")
        print(f"1. Usar motor_user.com (reemplazar el anterior)")
        print(f"2. Verificar que todos los ULN2003A estén conectados")
        print(f"3. Verificar que los 3 motores tengan alimentación")
        print(f"4. Observar secuencia: Base → Hombro → Codo")
        
        return True
        
    except Exception as e:
        print(f"Error creando motor_user.com mejorado: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    create_improved_motor_com()
