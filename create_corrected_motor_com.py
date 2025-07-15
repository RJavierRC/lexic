#!/usr/bin/env python3
"""
Generador CORREGIDO de motor_user.com con escalado y timing ajustados
"""
import os

def create_corrected_motor_com():
    """Crea motor_user.com corregido con escalado 2x y puerto C activo"""
    
    print("CREANDO motor_user.com CORREGIDO")
    print("================================")
    print("CORRECCIONES:")
    print("• Escalado 2x: 45° → 90 en código (para obtener 45° real)")
    print("• Hombro: Reducir de 135° a 60° real")
    print("• Codo: Activar puerto C con valores más altos")
    print("• Delays diferenciados por motor")
    
    try:
        # Crear código .COM corregido
        motor_com_data = bytearray()
        
        # === CONFIGURACIÓN INICIAL EXTENDIDA ===
        print("Fase 1: Configuración 8255 PPI")
        
        # Configurar 8255 PPI con secuencia extendida
        motor_com_data.extend([0xBA, 0x03, 0x03])  # MOV DX, 0303h (puerto control)
        motor_com_data.extend([0xB0, 0x80])        # MOV AL, 80h (modo 0, todos salida)
        motor_com_data.extend([0xEE])              # OUT DX, AL
        
        # Verificación configuración
        motor_com_data.extend([0xB9, 0xFF, 0xFF])  # Delay estabilización
        motor_com_data.extend([0xE2, 0xFE])        # LOOP
        
        # === RESET INICIAL TODOS LOS PUERTOS ===
        print("Fase 2: Reset inicial")
        
        # Reset puerto A (Base)
        motor_com_data.extend([0xBA, 0x00, 0x03])  # MOV DX, 0300h
        motor_com_data.extend([0xB0, 0])           # MOV AL, 0
        motor_com_data.extend([0xEE])              # OUT DX, AL
        
        # Reset puerto B (Hombro)
        motor_com_data.extend([0xBA, 0x01, 0x03])  # MOV DX, 0301h
        motor_com_data.extend([0xB0, 0])           # MOV AL, 0
        motor_com_data.extend([0xEE])              # OUT DX, AL
        
        # Reset puerto C (Codo)
        motor_com_data.extend([0xBA, 0x02, 0x03])  # MOV DX, 0302h
        motor_com_data.extend([0xB0, 0])           # MOV AL, 0
        motor_com_data.extend([0xEE])              # OUT DX, AL
        
        # Delay de estabilización inicial
        motor_com_data.extend([0xB9, 0xFF, 0x7F])  # Delay largo
        motor_com_data.extend([0xE2, 0xFE])        # LOOP
        
        # === MOVIMIENTO 1: BASE CORREGIDA ===
        print("Fase 3: Base 45° (con escalado 2x)")
        
        # Base: 45° real = 90 en código (factor 2x)
        motor_com_data.extend([0xBA, 0x00, 0x03])  # MOV DX, 0300h (puerto A)
        motor_com_data.extend([0xB0, 90])          # MOV AL, 90 (45° * 2)
        motor_com_data.extend([0xEE])              # OUT DX, AL
        
        # Delay extra largo para base
        motor_com_data.extend([0xB9, 0xFF, 0xFF])  # Delay máximo
        motor_com_data.extend([0xE2, 0xFE])        # LOOP
        motor_com_data.extend([0xB9, 0xFF, 0xFF])  # Segundo delay
        motor_com_data.extend([0xE2, 0xFE])        # LOOP
        
        # === MOVIMIENTO 2: HOMBRO CONTROLADO ===
        print("Fase 4: Hombro 60° (controlado)")
        
        # Hombro: 60° (no 135°)
        motor_com_data.extend([0xBA, 0x01, 0x03])  # MOV DX, 0301h (puerto B)
        motor_com_data.extend([0xB0, 120])         # MOV AL, 120 (60° * 2)
        motor_com_data.extend([0xEE])              # OUT DX, AL
        
        # Delay controlado para hombro
        motor_com_data.extend([0xB9, 0xFF, 0xFF])  # Delay largo
        motor_com_data.extend([0xE2, 0xFE])        # LOOP
        motor_com_data.extend([0xB9, 0xFF, 0x7F])  # Delay medio
        motor_com_data.extend([0xE2, 0xFE])        # LOOP
        
        # === MOVIMIENTO 3: CODO FORZADO ===
        print("Fase 5: Codo 30° (forzado)")
        
        # Codo: Múltiples intentos con valores escalados
        for attempt in [60, 80, 100, 120]:  # Valores crecientes
            motor_com_data.extend([0xBA, 0x02, 0x03])  # MOV DX, 0302h (puerto C)
            motor_com_data.extend([0xB0, attempt])     # MOV AL, attempt
            motor_com_data.extend([0xEE])              # OUT DX, AL
            
            # Delay largo entre intentos
            motor_com_data.extend([0xB9, 0xFF, 0x7F])  # Delay largo
            motor_com_data.extend([0xE2, 0xFE])        # LOOP
        
        # === SECUENCIA DE VERIFICACIÓN ===
        print("Fase 6: Secuencia de verificación")
        
        # Verificar todos los puertos están activos
        for port_offset in [0x00, 0x01, 0x02]:  # Puertos A, B, C
            for value in [50, 100, 150]:  # Valores de prueba
                motor_com_data.extend([0xBA, port_offset, 0x03])  # MOV DX, 030Xh
                motor_com_data.extend([0xB0, value])              # MOV AL, value
                motor_com_data.extend([0xEE])                     # OUT DX, AL
                motor_com_data.extend([0xB9, 0xFF, 0x3F])         # Delay medio
                motor_com_data.extend([0xE2, 0xFE])               # LOOP
        
        # === SECUENCIA FINAL OPTIMIZADA ===
        print("Fase 7: Secuencia final")
        
        # Valores finales corregidos con escalado
        final_values = [
            (0x00, 90),   # Base: 45° real
            (0x01, 120),  # Hombro: 60° real  
            (0x02, 60)    # Codo: 30° real
        ]
        
        for port_offset, value in final_values:
            motor_com_data.extend([0xBA, port_offset, 0x03])  # MOV DX, 030Xh
            motor_com_data.extend([0xB0, value])              # MOV AL, value
            motor_com_data.extend([0xEE])                     # OUT DX, AL
            
            # Delay diferenciado por motor
            if port_offset == 0x02:  # Codo necesita más tiempo
                motor_com_data.extend([0xB9, 0xFF, 0xFF])  # Delay máximo
                motor_com_data.extend([0xE2, 0xFE])        # LOOP
                motor_com_data.extend([0xB9, 0xFF, 0xFF])  # Segundo delay
                motor_com_data.extend([0xE2, 0xFE])        # LOOP
            else:
                motor_com_data.extend([0xB9, 0xFF, 0x7F])  # Delay normal
                motor_com_data.extend([0xE2, 0xFE])        # LOOP
        
        # Bucle infinito
        motor_com_data.extend([0xEB, 0xFE])  # JMP $ (bucle infinito)
        
        # Guardar archivo
        motor_com_path = os.path.join("DOSBox2", "Tasm", "motor_user.com")
        
        with open(motor_com_path, 'wb') as f:
            f.write(motor_com_data)
        
        print(f"\n¡motor_user.com CORREGIDO creado!")
        print(f"Archivo: {motor_com_path}")
        print(f"Tamaño: {len(motor_com_data)} bytes")
        
        print(f"\nCORRECCIONES APLICADAS:")
        print(f"✅ Base: 45° → código 90 (escalado 2x)")
        print(f"✅ Hombro: 60° → código 120 (reducido de 135°)")
        print(f"✅ Codo: Múltiples intentos 60-120 (forzado)")
        print(f"✅ Delays diferenciados por motor")
        print(f"✅ Secuencia de verificación añadida")
        
        print(f"\nRESULTADOS ESPERADOS:")
        print(f"• Base: ~45° (no 22.5°)")
        print(f"• Hombro: ~60° (no 135°)")
        print(f"• Codo: ~30° (debería moverse)")
        
        print(f"\nSI EL PROBLEMA PERSISTE:")
        print(f"• Motor 1: Factor puede ser diferente a 2x")
        print(f"• Motor 2: Verificar que no sobrepase límites")
        print(f"• Motor 3: Puerto C puede tener conexión física diferente")
        
        return True
        
    except Exception as e:
        print(f"Error creando motor_user.com corregido: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    create_corrected_motor_com()
