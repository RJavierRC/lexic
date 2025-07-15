;===============================================
; CONTROL DE MOTORES PARA SIMULACION PROTEUS
; Programa: test_nuevo3
; Generado: 2025-07-14 18:19:00
; Compatible: 8086/8088 + 8255 PPI
;===============================================

.MODEL SMALL
.STACK 100h

.DATA
    motor_base     DB ?
    motor_hombro   DB ?  
    motor_codo     DB ?
    delay_count    DW ?

.CODE
MAIN PROC
    ; Inicializar segmento de datos
    MOV AX, @DATA
    MOV DS, AX
    
    ; Configurar 8255 PPI como outputs
    MOV DX, 0303h
    MOV AL, 80h
    OUT DX, AL

    ; Control motor base - 45 grados
    MOV DX, 0300h
    CALL MOVE_BASE

    ; Control motor hombro - 120 grados  
    MOV DX, 0301h
    CALL MOVE_HOMBRO

    ; Control motor codo - 90 grados
    MOV DX, 0302h
    CALL MOVE_CODO

    ; Apagar todos los motores
    MOV DX, 0300h
    MOV AL, 00h
    OUT DX, AL
    MOV DX, 0301h  
    MOV AL, 00h
    OUT DX, AL
    MOV DX, 0302h
    MOV AL, 00h
    OUT DX, AL
    
    ; Salir del programa
    MOV AH, 4Ch
    MOV AL, 0
    INT 21h
MAIN ENDP


;===============================================
; PROCEDIMIENTO MOTOR BASE
;===============================================
MOVE_BASE PROC
    PUSH CX
    PUSH AX
    
    MOV CX, 25
STEP_LOOP_BASE:
    MOV AL, 01h
    OUT DX, AL
    CALL SHORT_DELAY
    MOV AL, 03h
    OUT DX, AL
    CALL SHORT_DELAY
    MOV AL, 02h
    OUT DX, AL
    CALL SHORT_DELAY
    MOV AL, 06h
    OUT DX, AL
    CALL SHORT_DELAY
    LOOP STEP_LOOP_BASE
    
    POP AX
    POP CX
    RET
MOVE_BASE ENDP

;===============================================
; PROCEDIMIENTO MOTOR HOMBRO
;===============================================
MOVE_HOMBRO PROC
    PUSH CX
    PUSH AX
    
    MOV CX, 66
STEP_LOOP_HOMBRO:
    MOV AL, 01h
    OUT DX, AL
    CALL SHORT_DELAY
    MOV AL, 03h
    OUT DX, AL
    CALL SHORT_DELAY
    MOV AL, 02h
    OUT DX, AL
    CALL SHORT_DELAY
    MOV AL, 06h
    OUT DX, AL
    CALL SHORT_DELAY
    LOOP STEP_LOOP_HOMBRO
    
    POP AX
    POP CX
    RET
MOVE_HOMBRO ENDP

;===============================================
; PROCEDIMIENTO MOTOR CODO
;===============================================
MOVE_CODO PROC
    PUSH CX
    PUSH AX
    
    MOV CX, 50
STEP_LOOP_CODO:
    MOV AL, 01h
    OUT DX, AL
    CALL SHORT_DELAY
    MOV AL, 03h
    OUT DX, AL
    CALL SHORT_DELAY
    MOV AL, 02h
    OUT DX, AL
    CALL SHORT_DELAY
    MOV AL, 06h
    OUT DX, AL
    CALL SHORT_DELAY
    LOOP STEP_LOOP_CODO
    
    POP AX
    POP CX
    RET
MOVE_CODO ENDP

;===============================================
; PROCEDIMIENTO DE DELAY
;===============================================
DELAY PROC
    PUSH CX
    PUSH AX
    MOV CX, 03E8h
DELAY_LOOP:
    NOP
    LOOP DELAY_LOOP
    POP AX
    POP CX
    RET
DELAY ENDP

SHORT_DELAY PROC
    PUSH CX
    MOV CX, 0100h
SHORT_DELAY_LOOP:
    NOP
    LOOP SHORT_DELAY_LOOP
    POP CX
    RET
SHORT_DELAY ENDP

END MAIN
