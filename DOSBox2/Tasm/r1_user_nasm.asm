global _start\n;===============================================
; CONTROL DE MOTORES PARA SIMULACION PROTEUS
; Programa: r1_user
; Generado: 2025-07-14 17:09:29
; Compatible: 8086/8088 + 8255 PPI
;===============================================

.MODEL SMALL
.STACK 100h

.DATA
    ; Variables del programa
    motor_base     DB ?    ; Estado motor base
    motor_hombro   DB ?    ; Estado motor hombro  
    motor_codo     DB ?    ; Estado motor codo
    delay_count    DW ?    ; Contador de delay

.CODE
MAIN PROC
    ; Inicializar segmento de datos
    MOV AX, @DATA
    MOV DS, AX
    
    ; Configurar 8255 PPI - Todos los puertos como salida
    MOV DX, 0303h  ; Puerto de configuracin
    MOV AL, 80h              ; Configuracin: todos outputs
    OUT DX, AL
    
    ; Mensaje de inicio (opcional para debug)
    ; MOV AH, 09h
    ; LEA DX, start_msg
    ; INT 21h

    ; === CONTROL MOTOR BASE ===
    ; Mover base a 45.0 grados
    MOV DX, 0300h  ; Puerto A (Base)
    CALL MOVE_BASE_45.0

    ; === CONTROL MOTOR HOMBRO ===
    ; Mover hombro a 120.0 grados
    MOV DX, 0301h  ; Puerto B (Hombro)
    CALL MOVE_HOMBRO_120.0

    ; === CONTROL MOTOR CODO ===
    ; Mover codo a 90.0 grados
    MOV DX, 0302h  ; Puerto C (Codo)
    CALL MOVE_CODO_90.0

    ; === FINALIZACION ===
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
; PROCEDIMIENTO MOTOR BASE - 45.0 GRADOS
;===============================================
MOVE_BASE_45.0 PROC
    PUSH CX
    PUSH AX
    
    ; Ejecutar 25 pasos para 45.0 grados
    MOV CX, 25            ; Nmero de pasos
STEP_LOOP_BASE_45.0:
    MOV AL, 01h         ; Patrn de paso 1
    OUT DX, AL
    CALL SHORT_DELAY
    MOV AL, 03h         ; Patrn de paso 2
    OUT DX, AL
    CALL SHORT_DELAY
    MOV AL, 02h         ; Patrn de paso 3
    OUT DX, AL
    CALL SHORT_DELAY
    MOV AL, 06h         ; Patrn de paso 4
    OUT DX, AL
    CALL SHORT_DELAY
    LOOP STEP_LOOP_BASE_45.0
    
    POP AX
    POP CX
    RET
MOVE_BASE_45.0 ENDP

;===============================================
; PROCEDIMIENTO MOTOR HOMBRO - 120.0 GRADOS
;===============================================
MOVE_HOMBRO_120.0 PROC
    PUSH CX
    PUSH AX
    
    ; Ejecutar 66 pasos para 120.0 grados
    MOV CX, 66            ; Nmero de pasos
STEP_LOOP_HOMBRO_120.0:
    MOV AL, 01h         ; Patrn de paso 1
    OUT DX, AL
    CALL SHORT_DELAY
    MOV AL, 03h         ; Patrn de paso 2
    OUT DX, AL
    CALL SHORT_DELAY
    MOV AL, 02h         ; Patrn de paso 3
    OUT DX, AL
    CALL SHORT_DELAY
    MOV AL, 06h         ; Patrn de paso 4
    OUT DX, AL
    CALL SHORT_DELAY
    LOOP STEP_LOOP_HOMBRO_120.0
    
    POP AX
    POP CX
    RET
MOVE_HOMBRO_120.0 ENDP

;===============================================
; PROCEDIMIENTO MOTOR CODO - 90.0 GRADOS
;===============================================
MOVE_CODO_90.0 PROC
    PUSH CX
    PUSH AX
    
    ; Ejecutar 50 pasos para 90.0 grados
    MOV CX, 50            ; Nmero de pasos
STEP_LOOP_CODO_90.0:
    MOV AL, 01h         ; Patrn de paso 1
    OUT DX, AL
    CALL SHORT_DELAY
    MOV AL, 03h         ; Patrn de paso 2
    OUT DX, AL
    CALL SHORT_DELAY
    MOV AL, 02h         ; Patrn de paso 3
    OUT DX, AL
    CALL SHORT_DELAY
    MOV AL, 06h         ; Patrn de paso 4
    OUT DX, AL
    CALL SHORT_DELAY
    LOOP STEP_LOOP_CODO_90.0
    
    POP AX
    POP CX
    RET
MOVE_CODO_90.0 ENDP

;===============================================
; PROCEDIMIENTO DE DELAY
;===============================================
DELAY PROC
    PUSH CX
    PUSH AX
    MOV CX, 03E8h    ; Delay de 1000 ciclos
DELAY_LOOP:
    NOP                        ; No operation
    LOOP DELAY_LOOP
    POP AX
    POP CX
    RET
DELAY ENDP

SHORT_DELAY PROC
    PUSH CX
    MOV CX, 1000h              ; Delay corto
SHORT_DELAY_LOOP:
    NOP
    LOOP SHORT_DELAY_LOOP
    POP CX
    RET
SHORT_DELAY ENDP

END MAIN
