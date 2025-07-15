#!/usr/bin/env python3
"""
Generador de archivos .COM usando DOSBox (como se hizo noname.com)
"""
import os
import subprocess
import time

def generate_com_with_dosbox():
    """Genera archivo .COM usando DOSBox como se hizo noname.com"""
    
    print("GENERADOR .COM USANDO DOSBOX")
    print("=============================")
    print("Generando motor_user.com usando DOSBox (como noname.com)")
    
    try:
        # Código ASM optimizado para .COM
        asm_code = """;===============================================
; MOTOR CONTROL - .COM FORMAT FOR PROTEUS
; Based on working noname.com format
;===============================================

.MODEL TINY
.CODE
ORG 100h

START:
    ; Configure 8255 PPI
    MOV DX, 0303h
    MOV AL, 80h
    OUT DX, AL
    
    ; Move base to 45 degrees
    MOV DX, 0300h
    MOV AL, 45
    OUT DX, AL
    
    ; Short delay
    MOV CX, 500
L1: LOOP L1
    
    ; Move shoulder to 120 degrees
    MOV DX, 0301h
    MOV AL, 120
    OUT DX, AL
    
    ; Short delay
    MOV CX, 500
L2: LOOP L2
    
    ; Move elbow to 90 degrees
    MOV DX, 0302h
    MOV AL, 90
    OUT DX, AL
    
    ; Wait 1 second
    MOV CX, 5000
L3: LOOP L3
    
    ; Exit
    MOV AH, 4Ch
    INT 21h

END START
"""
        
        # Guardar archivo ASM
        tasm_path = os.path.join(os.getcwd(), "DOSBox2", "Tasm")
        asm_file = os.path.join(tasm_path, "motor_user.asm")
        
        print("Guardando motor_user.asm...")
        with open(asm_file, 'w', encoding='ascii') as f:
            f.write(asm_code)
        print("ASM guardado exitosamente")
        
        # Crear configuración DOSBox
        dosbox_conf = """[dos]
break=false

[cpu]
core=auto
cputype=auto
cycles=auto

[autoexec]
mount c Tasm
c:
echo Compilando motor_user.asm a formato .COM...
TASM motor_user.asm
if exist motor_user.obj TLINK /t motor_user.obj
if exist motor_user.com echo motor_user.com creado exitosamente
if exist motor_user.com dir motor_user.com
exit
"""
        
        conf_file = os.path.join(os.getcwd(), "DOSBox2", "compile_com.conf")
        with open(conf_file, 'w', encoding='ascii') as f:
            f.write(dosbox_conf)
        
        # Ejecutar DOSBox
        dosbox_exe = os.path.join(os.getcwd(), "DOSBox2", "dosbox.exe")
        
        print("Ejecutando DOSBox para compilar...")
        print("DOSBox compilará motor_user.asm a motor_user.com...")
        
        if os.path.exists(dosbox_exe):
            # Ejecutar DOSBox con configuración
            result = subprocess.run([
                dosbox_exe, 
                "-conf", conf_file,
                "-noconsole"
            ], cwd=os.path.join(os.getcwd(), "DOSBox2"), 
            timeout=30)
            
            print("DOSBox terminado")
            
            # Verificar si se creó el archivo .COM
            com_file = os.path.join(tasm_path, "motor_user.com")
            
            if os.path.exists(com_file):
                file_size = os.path.getsize(com_file)
                
                print(f"\n¡EXITO! motor_user.com generado")
                print(f"Archivo: motor_user.com")
                print(f"Tamaño: {file_size} bytes")
                print(f"Ubicación: {com_file}")
                
                # Comparar con noname.com
                noname_file = os.path.join(tasm_path, "noname.com")
                if os.path.exists(noname_file):
                    noname_size = os.path.getsize(noname_file)
                    print(f"Comparación: motor_user.com ({file_size}b) vs noname.com ({noname_size}b)")
                
                # Mostrar primeros bytes
                with open(com_file, 'rb') as f:
                    first_bytes = f.read(16)
                    print(f"Primeros bytes: {' '.join(f'{b:02X}' for b in first_bytes)}")
                
                # Comparar con noname.com
                if os.path.exists(noname_file):
                    with open(noname_file, 'rb') as f:
                        noname_bytes = f.read(16)
                        print(f"noname.com:     {' '.join(f'{b:02X}' for b in noname_bytes)}")
                
                print(f"\nINSTRUCCIONES PARA PROTEUS:")
                print(f"1. Usar motor_user.com en lugar de motor_movement.exe")
                print(f"2. Procesador: 8086 Real Mode")
                print(f"3. 8255 PPI en 0300h-0303h")
                print(f"4. NO debería dar error de 'debug information'")
                
                return True
            else:
                print("No se creó motor_user.com")
                
                # Verificar archivos en directorio
                print("Archivos en Tasm:")
                try:
                    files = os.listdir(tasm_path)
                    for f in files:
                        if "motor_user" in f:
                            print(f"  {f}")
                except:
                    pass
                
                return False
        else:
            print(f"DOSBox no encontrado en: {dosbox_exe}")
            return False
            
    except subprocess.TimeoutExpired:
        print("DOSBox timeout - probablemente terminó correctamente")
        
        # Verificar si se creó el archivo después del timeout
        com_file = os.path.join(tasm_path, "motor_user.com")
        if os.path.exists(com_file):
            file_size = os.path.getsize(com_file)
            print(f"¡motor_user.com creado! Tamaño: {file_size} bytes")
            return True
        return False
        
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    generate_com_with_dosbox()
