
; =====================================================
; CODIGO ENSAMBLADOR GENERADO AUTOMATICAMENTE
; Programa: test_diagnostico
; Fecha: 2025-07-14 14:31:33
; Generado desde cuadruplos del analizador robotico
; =====================================================

.MODEL SMALL

.STACK 100H

.DATA
    ; === CONFIGURACION DE PUERTOS ===
    PORTA  EQU 00H    ; Puerto para motor BASE
    PORTB  EQU 02H    ; Puerto para motor HOMBRO
    PORTC  EQU 04H    ; Puerto para motor CODO
    PORTD  EQU 06H    ; Puerto para motor GARRA
    PORTE  EQU 08H    ; Puerto para motor MUNECA
    PORTF  EQU 0AH    ; Puerto para VELOCIDAD
    CONFIG EQU 0CH    ; Puerto de configuracion
    
    ; === VARIABLES DEL PROGRAMA ===
    R1_STATUS DB 0  ; Estado del robot

.CODE
MAIN PROC
    ; === INICIALIZACION ===
    MOV AX, @DATA
    MOV DS, AX
    
    ; Configurar puertos como salidas
    MOV DX, CONFIG
    MOV AL, 10000000B  ; Todos los puertos como salidas
    OUT DX, AL
    
    ; === INICIO DEL PROGRAMA PRINCIPAL ===
    ; === DECLARACION DEL ROBOT R1 ===
        MOV AL, 2  ; Valor para velocidad
        MOV DX, PORTF  ; Puerto del velocidad
        OUT DX, AL  ; Enviar valor al velocidad
        ; === MOVER VELOCIDAD DEL ROBOT R1 ===
        MOV AL, 00000010B  ; Patron para velocidad
        MOV DX, PORTF  ; Puerto del velocidad
        OUT DX, AL  ; Mover velocidad a 2°
        MOV CX, 0FFFFH  ; Delay entre movimientos
    MOVE_DELAY:
        LOOP MOVE_DELAY
        MOV AL, 45  ; Valor para base
        MOV DX, PORTA  ; Puerto del base
        OUT DX, AL  ; Enviar valor al base
        ; === MOVER BASE DEL ROBOT R1 ===
        MOV AL, 00101101B  ; Patron para base
        MOV DX, PORTA  ; Puerto del base
        OUT DX, AL  ; Mover base a 45°
        MOV CX, 0FFFFH  ; Delay entre movimientos
    MOVE_DELAY:
        LOOP MOVE_DELAY
        MOV AL, 120  ; Valor para hombro
        MOV DX, PORTB  ; Puerto del hombro
        OUT DX, AL  ; Enviar valor al hombro
        ; === MOVER HOMBRO DEL ROBOT R1 ===
        MOV AL, 01111000B  ; Patron para hombro
        MOV DX, PORTB  ; Puerto del hombro
        OUT DX, AL  ; Mover hombro a 120°
        MOV CX, 0FFFFH  ; Delay entre movimientos
    MOVE_DELAY:
        LOOP MOVE_DELAY
        MOV AL, 90  ; Valor para codo
        MOV DX, PORTC  ; Puerto del codo
        OUT DX, AL  ; Enviar valor al codo
        ; === MOVER CODO DEL ROBOT R1 ===
        MOV AL, 01011010B  ; Patron para codo
        MOV DX, PORTC  ; Puerto del codo
        OUT DX, AL  ; Mover codo a 90°
        MOV CX, 0FFFFH  ; Delay entre movimientos
    MOVE_DELAY:
        LOOP MOVE_DELAY

    ; === FIN DEL PROGRAMA ===
    MOV AH, 4CH  ; Función de terminación
    MOV AL, 0    ; Código de salida
    INT 21H      ; Llamada al sistema
    
MAIN ENDP
END MAIN
