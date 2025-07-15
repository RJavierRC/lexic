; ----------------------------------------------
; CONTROL DINMICO DE TRES MOTORES PASO A PASO (8255)
; Programa: robot_dynamic
; Generado: 2025-07-14 20:53:12
; Basado en cdigo Robot del usuario
; ----------------------------------------------
; VALORES EXTRADOS DEL CDIGO:
;   r1.base = 45  25 pasos
;   r1.hombro = 90  50 pasos  
;   r1.codo = 60  33 pasos
;   r1.velocidad = 2
;   r1.espera = 1s
; ----------------------------------------------

CODE        SEGMENT

PORTA   EQU 00h            ; Direccin Puerto A - BASE
PORTB   EQU 02h          ; Direccin Puerto B - HOMBRO
PORTC   EQU 04h            ; Direccin Puerto C - CODO
Config  EQU 06h          ; Direccin registro de configuracin

        ORG 100H           ; Programa COM (para DOS Box o imagen binaria)

;------ Inicializacin del 8255 ------------------------
        MOV     DX, Config
        MOV     AL, 10000000B   ; 80h  A, B, C como salidas
        OUT     DX, AL

;=======================================================
START:
;======== MOTOR BASE (Puerto A) - 45 ===========================
        MOV     DX, PORTA
        ; Ejecutar 25 pasos para 45 grados
        MOV     CX, 25
BASE_LOOP:
        MOV     AL, 00000110B        ; Paso 1
        OUT     DX, AL
        MOV     BX, 3048
        CALL    DELAY_ROUTINE

        MOV     AL, 00001100B        ; Paso 2
        OUT     DX, AL
        MOV     BX, 3048
        CALL    DELAY_ROUTINE

        MOV     AL, 00001001B        ; Paso 3
        OUT     DX, AL
        MOV     BX, 3048
        CALL    DELAY_ROUTINE

        MOV     AL, 00000011B        ; Paso 4
        OUT     DX, AL
        MOV     BX, 3048
        CALL    DELAY_ROUTINE
        
        LOOP    BASE_LOOP

;======== MOTOR HOMBRO (Puerto B) - 90 ===========================
        MOV     DX, PORTB
        ; Ejecutar 50 pasos para 90 grados
        MOV     CX, 50
HOMBRO_LOOP:
        MOV     AL, 00000110B        ; Paso 1
        OUT     DX, AL
        MOV     BX, 3048
        CALL    DELAY_ROUTINE

        MOV     AL, 00001100B        ; Paso 2
        OUT     DX, AL
        MOV     BX, 3048
        CALL    DELAY_ROUTINE

        MOV     AL, 00001001B        ; Paso 3
        OUT     DX, AL
        MOV     BX, 3048
        CALL    DELAY_ROUTINE

        MOV     AL, 00000011B        ; Paso 4
        OUT     DX, AL
        MOV     BX, 3048
        CALL    DELAY_ROUTINE
        
        LOOP    HOMBRO_LOOP

;======== MOTOR CODO (Puerto C) - 60 ===========================
        MOV     DX, PORTC
        ; Ejecutar 33 pasos para 60 grados
        MOV     CX, 33
CODO_LOOP:
        MOV     AL, 00000110B        ; Paso 1
        OUT     DX, AL
        MOV     BX, 3048
        CALL    DELAY_ROUTINE

        MOV     AL, 00001100B        ; Paso 2
        OUT     DX, AL
        MOV     BX, 3048
        CALL    DELAY_ROUTINE

        MOV     AL, 00001001B        ; Paso 3
        OUT     DX, AL
        MOV     BX, 3048
        CALL    DELAY_ROUTINE

        MOV     AL, 00000011B        ; Paso 4
        OUT     DX, AL
        MOV     BX, 3048
        CALL    DELAY_ROUTINE
        
        LOOP    CODO_LOOP

        ; Terminar programa limpiamente
        MOV     AH, 4Ch
        MOV     AL, 0
        INT     21h

;=======================================================
; RUTINA DE DELAY DINMICA
; BX contiene el factor de delay
;=======================================================
DELAY_ROUTINE PROC
        PUSH    CX
        PUSH    AX
        MOV     CX, BX
DELAY_LOOP:
        NOP
        NOP
        LOOP    DELAY_LOOP
        POP     AX
        POP     CX
        RET
DELAY_ROUTINE ENDP

CODE        ENDS
        END START
