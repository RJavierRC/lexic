; ----------------------------------------------
; CONTROL DE TRES MOTORES PASO A PASO (8255)
; Programa: motores_robot
; Fecha: 2025-07-14 14:45:02
; Generado automaticamente desde sintaxis robotica
;   - Motor A (BASE): bits 0-3 del Puerto A  (00h)
;   - Motor B (HOMBRO): bits 0-3 del Puerto B  (02h)
;   - Motor C (CODO): bits 0-3 del Puerto C  (04h)
;   Config 8255 = 80h - todos los puertos salida, modo 0
; ----------------------------------------------
CODE        SEGMENT
PORTA   EQU 00H            ; Direccion Puerto A (BASE)
PORTB   EQU 02H            ; Direccion Puerto B (HOMBRO)
PORTC   EQU 04H            ; Direccion Puerto C (CODO)
Config  EQU 06H            ; Direccion registro de configuracion
        ORG 100H           ; Programa COM (para DOS Box o imagen binaria)

;------ Inicializacion del 8255 ------------------------
        MOV     DX, Config
        MOV     AL, 10000000B   ; 80h - A, B, C como salidas
        OUT     DX, AL

;=======================================================
START:

;======== MOTOR A (BASE) ===========================
        MOV     DX, PORTA
        MOV     AL, 00000110B        ; Paso 1
        OUT     DX, AL
        MOV     CX, 0FFFFH
loopy1A: LOOP    loopy1A

        MOV     AL, 00001100B        ; Paso 2
        OUT     DX, AL
        MOV     CX, 0FFFFH
loopy2A: LOOP    loopy2A

        MOV     AL, 00001001B        ; Paso 3
        OUT     DX, AL
        MOV     CX, 0FFFFH
loopy3A: LOOP    loopy3A

        MOV     AL, 00000011B        ; Paso 4
        OUT     DX, AL
        MOV     CX, 0FFFFH
loopy4A: LOOP    loopy4A

;======== MOTOR B (HOMBRO) ===========================
        MOV     DX, PORTB
        MOV     AL, 00000110B        ; Paso 1
        OUT     DX, AL
        MOV     CX, 0FFFFH
loopy1B: LOOP    loopy1B

        MOV     AL, 00001100B        ; Paso 2
        OUT     DX, AL
        MOV     CX, 0FFFFH
loopy2B: LOOP    loopy2B

        MOV     AL, 00001001B        ; Paso 3
        OUT     DX, AL
        MOV     CX, 0FFFFH
loopy3B: LOOP    loopy3B

        MOV     AL, 00000011B        ; Paso 4
        OUT     DX, AL
        MOV     CX, 0FFFFH
loopy4B: LOOP    loopy4B

;======== MOTOR C (CODO) ===========================
        MOV     DX, PORTC
        MOV     AL, 00000110B        ; Paso 1
        OUT     DX, AL
        MOV     CX, 0FFFFH
loopy1C: LOOP    loopy1C

        MOV     AL, 00001100B        ; Paso 2
        OUT     DX, AL
        MOV     CX, 0FFFFH
loopy2C: LOOP    loopy2C

        MOV     AL, 00001001B        ; Paso 3
        OUT     DX, AL
        MOV     CX, 0FFFFH
loopy3C: LOOP    loopy3C

        MOV     AL, 00000011B        ; Paso 4
        OUT     DX, AL
        MOV     CX, 0FFFFH
loopy4C: LOOP    loopy4C

        ; === FIN DEL PROGRAMA ===
        MOV     AH, 4CH
        INT     21H

CODE    ENDS
        END     START
