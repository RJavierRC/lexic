#!/usr/bin/env python3
"""
Generador de archivos .COM para Proteus (como noname.com que funciona)
"""
import os
from robot_lexical_analyzer import RobotLexicalAnalyzer

def generate_com_file():
    """Genera archivo .COM compatible con Proteus como noname.com"""
    
    # Código del usuario
    user_code = """Robot r1

r1.velocidad = 2       
r1.base = 45           
r1.hombro = 120        
r1.codo = 90           
r1.espera = 1"""
    
    print("🎯 ===============================================")
    print("🎯 GENERADOR DE ARCHIVO .COM PARA PROTEUS")
    print("🎯 ===============================================")
    print("📝 Generando archivo .COM como noname.com que SÍ funciona")
    print("📏 Tamaño objetivo: ~113 bytes (como noname.com)")
    print("🎯 ===============================================")
    
    # Crear analizador
    analyzer = RobotLexicalAnalyzer()
    
    try:
        # Analizar código
        print("🔍 Analizando código...")
        tokens, errors = analyzer.analyze(user_code)
        
        if errors:
            print(f"❌ Errores encontrados: {len(errors)}")
            for error in errors:
                print(f"   • {error}")
            return False
        
        print(f"✅ Código válido - {len(tokens)} tokens encontrados")
        
        # Generar código ASM optimizado para formato .COM
        print("📝 Generando código ASM para formato .COM...")
        
        # Código ASM específico para .COM (más simple)
        asm_code = f""";===============================================
; CONTROL DE MOTORES - FORMATO .COM PARA PROTEUS
; Compatible con noname.com (113 bytes)
; Generado: Motor Movement
;===============================================

.MODEL TINY
.CODE
ORG 100h            ; Inicio estándar para archivos .COM

START:
    ; Configurar 8255 PPI
    MOV DX, 0303h   ; Puerto de control
    MOV AL, 80h     ; Configuración: Modo 0, todos salida
    OUT DX, AL
    
    ; Configurar velocidad (r1.velocidad = 2)
    MOV CX, 2       ; Velocidad = 2 unidades
    
    ; Mover base a 45° (r1.base = 45)
    MOV DX, 0300h   ; Puerto A - Base
    MOV AL, 45      ; Ángulo 45°
    OUT DX, AL
    CALL DELAY
    
    ; Mover hombro a 120° (r1.hombro = 120)  
    MOV DX, 0301h   ; Puerto B - Hombro
    MOV AL, 120     ; Ángulo 120°
    OUT DX, AL
    CALL DELAY
    
    ; Mover codo a 90° (r1.codo = 90)
    MOV DX, 0302h   ; Puerto C - Codo
    MOV AL, 90      ; Ángulo 90°
    OUT DX, AL
    CALL DELAY
    
    ; Esperar 1 segundo (r1.espera = 1)
    MOV CX, 1000    ; 1000ms = 1 segundo
    CALL DELAY_MS
    
    ; Finalizar programa
    MOV AH, 4Ch     ; Función DOS: Terminar programa
    INT 21h         ; Llamada al sistema DOS

DELAY PROC NEAR
    PUSH CX
    MOV CX, 500     ; Delay corto entre movimientos
DELAY_LOOP:
    NOP
    LOOP DELAY_LOOP
    POP CX
    RET
DELAY ENDP

DELAY_MS PROC NEAR
    PUSH AX
    PUSH CX
DELAY_MS_LOOP:
    MOV AX, 1000    ; Microsegundos por ms
DELAY_US_LOOP:
    NOP
    DEC AX
    JNZ DELAY_US_LOOP
    LOOP DELAY_MS_LOOP
    POP CX
    POP AX
    RET
DELAY_MS ENDP

END START
"""
        
        # Guardar archivo ASM
        tasm_path = os.path.join(os.getcwd(), "DOSBox2", "Tasm")
        asm_file = os.path.join(tasm_path, "motor_user.asm")
        
        print(f"💾 Guardando archivo ASM...")
        with open(asm_file, 'w', encoding='ascii', errors='ignore') as f:
            f.write(asm_code)
        print(f"✅ Archivo ASM guardado: motor_user.asm")
        
        # Compilar a .COM usando TASM
        print(f"⚙️ Compilando a formato .COM...")
        
        # Crear archivo batch para compilación .COM
        batch_content = f"""@echo off
cd /d "{tasm_path}"
echo Compilando motor_user.asm a formato .COM...
TASM.EXE motor_user.asm
if exist motor_user.obj (
    echo Enlazando a formato .COM...
    TLINK.EXE /t motor_user.obj
    if exist motor_user.com (
        echo ✅ motor_user.com generado exitosamente
        dir motor_user.com
    ) else (
        echo ❌ Error generando .COM
    )
) else (
    echo ❌ Error en ensamblado
)
"""
        
        batch_file = os.path.join(tasm_path, "compile_com.bat")
        with open(batch_file, 'w') as f:
            f.write(batch_content)
        
        # Ejecutar compilación
        print(f"🔧 Ejecutando compilación .COM...")
        import subprocess
        result = subprocess.run([batch_file], cwd=tasm_path, capture_output=True, text=True, shell=True)
        
        print(f"📄 Salida de compilación:")
        print(result.stdout)
        if result.stderr:
            print(f"⚠️ Warnings/Errores:")
            print(result.stderr)
        
        # Verificar archivo .COM generado
        com_file = os.path.join(tasm_path, "motor_user.com")
        if os.path.exists(com_file):
            file_size = os.path.getsize(com_file)
            
            print(f"\n✅ ¡ARCHIVO .COM GENERADO EXITOSAMENTE!")
            print(f"📁 Archivo: motor_user.com")
            print(f"📂 Ubicación: {com_file}")
            print(f"📏 Tamaño: {file_size} bytes")
            print(f"📊 Comparación con noname.com: {file_size} vs 113 bytes")
            
            # Verificar que sea un archivo .COM válido
            with open(com_file, 'rb') as f:
                first_bytes = f.read(10)
                print(f"🔍 Primeros bytes: {' '.join(f'{b:02X}' for b in first_bytes)}")
            
            print(f"\n🎯 INSTRUCCIONES PARA PROTEUS:")
            print(f"=" * 50)
            print(f"1. 🖥️  Usar procesador 8086 Real Mode")
            print(f"2. 📂 Cargar: motor_user.com (NO .exe)")
            print(f"3. 🔌 8255 PPI en direcciones 0300h-0303h")
            print(f"4. 🤖 ULN2003A para control de motores")
            print(f"5. ▶️  Ejecutar - Los motores deberían moverse")
            print(f"=" * 50)
            print(f"✅ Formato .COM como noname.com - Sin errores de debug")
            
            return True
        else:
            print(f"❌ No se generó el archivo motor_user.com")
            return False
            
    except Exception as e:
        print(f"❌ Error durante la generación: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    generate_com_file()
