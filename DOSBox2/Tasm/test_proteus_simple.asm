.MODEL SMALL
.STACK 100h

.DATA
    ; Variables del programa

.CODE
MAIN PROC
    ; Inicializar segmento de datos
    MOV AX, @DATA
    MOV DS, AX
    
    ; Configurar 8255 PPI - Modo 0, todos como salida
    MOV DX, 0303h  ; Puerto de control
    MOV AL, 80h    ; Configuración: todos outputs
    OUT DX, AL
    
    ; === MOTOR BASE - 45 GRADOS ===
    MOV DX, 0300h  ; Puerto A (Base)
    MOV CX, 25     ; 25 pasos para 45 grados
    
LOOP_BASE:
    MOV AL, 01h
    OUT DX, AL
    CALL DELAY
    MOV AL, 03h
    OUT DX, AL
    CALL DELAY
    MOV AL, 02h
    OUT DX, AL
    CALL DELAY
    MOV AL, 06h
    OUT DX, AL
    CALL DELAY
    LOOP LOOP_BASE
    
    ; === MOTOR HOMBRO - 120 GRADOS ===
    MOV DX, 0301h  ; Puerto B (Hombro)
    MOV CX, 67     ; 67 pasos para 120 grados
    
LOOP_HOMBRO:
    MOV AL, 01h
    OUT DX, AL
    CALL DELAY
    MOV AL, 03h
    OUT DX, AL
    CALL DELAY
    MOV AL, 02h
    OUT DX, AL
    CALL DELAY
    MOV AL, 06h
    OUT DX, AL
    CALL DELAY
    LOOP LOOP_HOMBRO
    
    ; === MOTOR CODO - 90 GRADOS ===
    MOV DX, 0302h  ; Puerto C (Codo)
    MOV CX, 50     ; 50 pasos para 90 grados
    
LOOP_CODO:
    MOV AL, 01h
    OUT DX, AL
    CALL DELAY
    MOV AL, 03h
    OUT DX, AL
    CALL DELAY
    MOV AL, 02h
    OUT DX, AL
    CALL DELAY
    MOV AL, 06h
    OUT DX, AL
    CALL DELAY
    LOOP LOOP_CODO
    
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
    
    ; Terminar programa
    MOV AH, 4Ch
    MOV AL, 0
    INT 21h
MAIN ENDP

; Procedimiento de delay
DELAY PROC
    PUSH CX
    PUSH AX
    
    MOV CX, 0FFFFh
DELAY_LOOP:
    NOP
    NOP
    LOOP DELAY_LOOP
    
    POP AX
    POP CX
    RET
DELAY ENDP

END MAIN
