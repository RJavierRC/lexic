;-----------------------------------------------
; CONTROL DE TRES MOTORES PASO A PASO
; Programa: robot_program
; Fecha: 2025-07-14 14:54:47
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

        ; MOTOR A (BASE) - Secuencia de pasos
        MOV   DX, PORTA
        MOV   AL, 00000110B
        OUT   DX, AL
        MOV   CX, 0FFFFH
loopy1: LOOP  loopy1

        MOV   AL, 00001100B
        OUT   DX, AL
        MOV   CX, 0FFFFH
loopy2: LOOP  loopy2

        MOV   AL, 00001001B
        OUT   DX, AL
        MOV   CX, 0FFFFH
loopy3: LOOP  loopy3

        MOV   AL, 00000011B
        OUT   DX, AL
        MOV   CX, 0FFFFH
loopy4: LOOP  loopy4

        ; MOTOR B (HOMBRO) - Secuencia de pasos
        MOV   DX, PORTB
        MOV   AL, 00000110B
        OUT   DX, AL
        MOV   CX, 0FFFFH
loopy5: LOOP  loopy5

        MOV   AL, 00001100B
        OUT   DX, AL
        MOV   CX, 0FFFFH
loopy6: LOOP  loopy6

        MOV   AL, 00001001B
        OUT   DX, AL
        MOV   CX, 0FFFFH
loopy7: LOOP  loopy7

        MOV   AL, 00000011B
        OUT   DX, AL
        MOV   CX, 0FFFFH
loopy8: LOOP  loopy8

        ; MOTOR C (CODO) - Secuencia de pasos
        MOV   DX, PORTC
        MOV   AL, 00000110B
        OUT   DX, AL
        MOV   CX, 0FFFFH
loopy9: LOOP  loopy9

        MOV   AL, 00001100B
        OUT   DX, AL
        MOV   CX, 0FFFFH
loopy10: LOOP  loopy10

        MOV   AL, 00001001B
        OUT   DX, AL
        MOV   CX, 0FFFFH
loopy11: LOOP  loopy11

        MOV   AL, 00000011B
        OUT   DX, AL
        MOV   CX, 0FFFFH
loopy12: LOOP  loopy12

        ; Terminar programa
        MOV    AH,4CH
        MOV    AL,0
        INT    21H
CODE_SEG    ENDS
   END  START
