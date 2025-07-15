#!/usr/bin/env python3
"""
Generador de archivos .COM para Proteus (versión simplificada sin emojis)
"""
import os
import subprocess
from robot_lexical_analyzer import RobotLexicalAnalyzer

def generate_com_file_simple():
    """Genera archivo .COM compatible con Proteus como noname.com"""
    
    print("GENERADOR DE ARCHIVO .COM PARA PROTEUS")
    print("=====================================")
    print("Generando archivo .COM como noname.com que SI funciona")
    print("Tamaño objetivo: ~113 bytes (como noname.com)")
    print("=====================================")
    
    try:
        # Código ASM específico para .COM (más simple)
        asm_code = """;===============================================
; CONTROL DE MOTORES - FORMATO .COM PARA PROTEUS
; Compatible con noname.com (113 bytes)
;===============================================

.MODEL TINY
.CODE
ORG 100h            ; Inicio estándar para archivos .COM

START:
    ; Configurar 8255 PPI
    MOV DX, 0303h   ; Puerto de control
    MOV AL, 80h     ; Configuración: Modo 0, todos salida
    OUT DX, AL
    
    ; Mover base a 45° (r1.base = 45)
    MOV DX, 0300h   ; Puerto A - Base
    MOV AL, 45      ; Ángulo 45°
    OUT DX, AL
    
    ; Pequeño delay
    MOV CX, 1000
DELAY1:
    NOP
    LOOP DELAY1
    
    ; Mover hombro a 120° (r1.hombro = 120)  
    MOV DX, 0301h   ; Puerto B - Hombro
    MOV AL, 120     ; Ángulo 120°
    OUT DX, AL
    
    ; Pequeño delay
    MOV CX, 1000
DELAY2:
    NOP
    LOOP DELAY2
    
    ; Mover codo a 90° (r1.codo = 90)
    MOV DX, 0302h   ; Puerto C - Codo
    MOV AL, 90      ; Ángulo 90°
    OUT DX, AL
    
    ; Esperar (r1.espera = 1)
    MOV CX, 5000    ; Delay más largo
DELAY3:
    NOP
    LOOP DELAY3
    
    ; Finalizar programa
    MOV AH, 4Ch     ; Función DOS: Terminar programa
    INT 21h         ; Llamada al sistema DOS

END START
"""
        
        # Guardar archivo ASM
        tasm_path = os.path.join(os.getcwd(), "DOSBox2", "Tasm")
        asm_file = os.path.join(tasm_path, "motor_user.asm")
        
        print("Guardando archivo ASM...")
        with open(asm_file, 'w', encoding='ascii', errors='ignore') as f:
            f.write(asm_code)
        print("Archivo ASM guardado: motor_user.asm")
        
        # Crear archivo batch simplificado para compilación .COM
        batch_content = """@echo off
cd DOSBox2\\Tasm
echo Compilando motor_user.asm a formato .COM...
TASM.EXE motor_user.asm
if exist motor_user.obj (
    echo Enlazando a formato .COM...
    TLINK.EXE /t motor_user.obj
    if exist motor_user.com (
        echo motor_user.com generado exitosamente
        dir motor_user.com
    ) else (
        echo Error generando .COM
    )
    del motor_user.obj
) else (
    echo Error en ensamblado
)
pause
"""
        
        batch_file = os.path.join(os.getcwd(), "compile_com.bat")
        with open(batch_file, 'w', encoding='ascii') as f:
            f.write(batch_content)
        
        print("Ejecutando compilación .COM...")
        print("Archivo batch creado: compile_com.bat")
        
        # Ejecutar el batch
        result = subprocess.run([batch_file], shell=True, capture_output=True, text=True)
        
        print("Salida de compilación:")
        print(result.stdout)
        if result.stderr:
            print("Warnings/Errores:")
            print(result.stderr)
        
        # Verificar archivo .COM generado
        com_file = os.path.join(tasm_path, "motor_user.com")
        if os.path.exists(com_file):
            file_size = os.path.getsize(com_file)
            
            print("\n¡ARCHIVO .COM GENERADO EXITOSAMENTE!")
            print(f"Archivo: motor_user.com")
            print(f"Ubicación: {com_file}")
            print(f"Tamaño: {file_size} bytes")
            print(f"Comparación con noname.com: {file_size} vs 113 bytes")
            
            # Verificar contenido
            with open(com_file, 'rb') as f:
                first_bytes = f.read(10)
                print(f"Primeros bytes (hex): {' '.join(f'{b:02X}' for b in first_bytes)}")
            
            print("\nINSTRUCCIONES PARA PROTEUS:")
            print("=" * 50)
            print("1. Usar procesador 8086 Real Mode")
            print("2. Cargar: motor_user.com (NO .exe)")
            print("3. 8255 PPI en direcciones 0300h-0303h")
            print("4. ULN2003A para control de motores")
            print("5. Ejecutar - Los motores deberían moverse")
            print("=" * 50)
            print("Formato .COM como noname.com - Sin errores de debug")
            
            return True
        else:
            print("No se generó el archivo motor_user.com")
            
            # Intentar compilación manual paso a paso
            print("\nIntentando compilación manual...")
            
            os.chdir(tasm_path)
            
            # Paso 1: TASM
            print("Ejecutando TASM...")
            tasm_result = subprocess.run(['TASM.EXE', 'motor_user.asm'], 
                                       capture_output=True, text=True)
            print(f"TASM salida: {tasm_result.stdout}")
            if tasm_result.stderr:
                print(f"TASM errores: {tasm_result.stderr}")
            
            # Paso 2: TLINK
            if os.path.exists('motor_user.obj'):
                print("Ejecutando TLINK...")
                tlink_result = subprocess.run(['TLINK.EXE', '/t', 'motor_user.obj'], 
                                            capture_output=True, text=True)
                print(f"TLINK salida: {tlink_result.stdout}")
                if tlink_result.stderr:
                    print(f"TLINK errores: {tlink_result.stderr}")
                
                if os.path.exists('motor_user.com'):
                    file_size = os.path.getsize('motor_user.com')
                    print(f"¡EXITO! motor_user.com generado: {file_size} bytes")
                    return True
            
            return False
            
    except Exception as e:
        print(f"Error durante la generación: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    generate_com_file_simple()
