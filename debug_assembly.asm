;-----------------------------------------------
; CONTROL DE TRES MOTORES PASO A PASO
; Programa: r1_test
; Fecha: 2025-07-14 17:06:15
; Generado automaticamente para control de 3 motores
;-----------------------------------------------

; Definiciones de puertos 8255 (fuera de segmentos)
PORTA   EQU 00H    ; Puerto A - Motor BASE
PORTB   EQU 02H    ; Puerto B - Motor HOMBRO 
PORTC   EQU 04H    ; Puerto C - Motor CODO
Config  EQU 06H    ; Registro de configuracion

DATA_SEG    SEGMENT
; Variables del programa (si las hubiera)
DATA_SEG    ENDS

CODE_SEG    SEGMENT
   ASSUME CS: CODE_SEG, DS:DATA_SEG

    START:
        MOV   AX, DATA_SEG
        MOV   DS, AX

        ; Configurar 8255 - todos los puertos como salida
        MOV   DX, Config
        MOV   AL, 10000000B
        OUT   DX, AL

        ; MOTOR A (BASE) - Secuencia de pasos (solo giro horario)
        MOV   DX, PORTA
        MOV   AL, 00000011B    ; Paso 1
        OUT   DX, AL
        MOV   CX, 0FFFFH
loopy1: LOOP  loopy1

        MOV   AL, 00000110B    ; Paso 2
        OUT   DX, AL
        MOV   CX, 0FFFFH
loopy2: LOOP  loopy2

        ; MOTOR B (HOMBRO) - Secuencia de pasos (solo giro horario)
        MOV   DX, PORTB
        MOV   AL, 00000011B    ; Paso 1
        OUT   DX, AL
        MOV   CX, 0FFFFH
loopy5: LOOP  loopy5

        MOV   AL, 00000110B    ; Paso 2
        OUT   DX, AL
        MOV   CX, 0FFFFH
loopy6: LOOP  loopy6

        ; MOTOR C (CODO) - Secuencia de pasos (solo giro horario)
        MOV   DX, PORTC
        MOV   AL, 00000011B    ; Paso 1
        OUT   DX, AL
        MOV   CX, 0FFFFH
loopy9: LOOP  loopy9

        MOV   AL, 00000110B    ; Paso 2
        OUT   DX, AL
        MOV   CX, 0FFFFH
loopy10: LOOP  loopy10

        ; Terminar programa
        MOV    AH,4CH
        MOV    AL,0
        INT    21H
CODE_SEG    ENDS
   END  START
