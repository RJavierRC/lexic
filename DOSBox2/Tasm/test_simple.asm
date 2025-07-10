
; =====================================================
; CÓDIGO ENSAMBLADOR GENERADO AUTOMÁTICAMENTE
; Programa: test_simple
; Fecha: 2025-07-10 13:56:44
; Generado desde cuádruplos del analizador robótico
; =====================================================

.MODEL SMALL

.STACK 100H

.DATA
    ; === CONFIGURACIÓN DE PUERTOS ===
    PORTA  EQU 00H    ; Puerto para motor BASE
    PORTB  EQU 02H    ; Puerto para motor HOMBRO
    PORTC  EQU 04H    ; Puerto para motor CODO
    PORTD  EQU 06H    ; Puerto para motor GARRA
    PORTE  EQU 08H    ; Puerto para motor MUÑECA
    PORTF  EQU 0AH    ; Puerto para VELOCIDAD
    CONFIG EQU 0CH    ; Puerto de configuración
    
    ; === VARIABLES DEL PROGRAMA ===
    R1_STATUS DB 0  ; Estado del robot

.CODE
MAIN PROC
    ; === INICIALIZACIÓN ===
    MOV AX, @DATA
    MOV DS, AX
    
    ; Configurar puertos como salidas
    MOV DX, CONFIG
    MOV AL, 10000000B  ; Todos los puertos como salidas
    OUT DX, AL
    
    ; === INICIO DEL PROGRAMA PRINCIPAL ===
    ; === DECLARACIÓN DEL ROBOT R1 ===
        MOV AL, 90  ; Valor para base
        MOV DX, PORTA  ; Puerto del base
        OUT DX, AL  ; Enviar valor al base
        ; === MOVER BASE DEL ROBOT R1 ===
        MOV AL, 01011010B  ; Patrón para base
        MOV DX, PORTA  ; Puerto del base
        OUT DX, AL  ; Mover base a 90°
        MOV CX, 0FFFFH  ; Delay entre movimientos
    MOVE_DELAY:
        LOOP MOVE_DELAY
        MOV AL, 45  ; Valor para hombro
        MOV DX, PORTB  ; Puerto del hombro
        OUT DX, AL  ; Enviar valor al hombro
        ; === MOVER HOMBRO DEL ROBOT R1 ===
        MOV AL, 00101101B  ; Patrón para hombro
        MOV DX, PORTB  ; Puerto del hombro
        OUT DX, AL  ; Mover hombro a 45°
        MOV CX, 0FFFFH  ; Delay entre movimientos
    MOVE_DELAY:
        LOOP MOVE_DELAY

    ; === FIN DEL PROGRAMA ===
    MOV AH, 4CH  ; Función de terminación
    MOV AL, 0    ; Código de salida
    INT 21H      ; Llamada al sistema
    
MAIN ENDP
END MAIN
