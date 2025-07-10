
; =====================================================
; CÓDIGO ENSAMBLADOR GENERADO AUTOMÁTICAMENTE
; Programa: demo_robot
; Fecha: 2025-07-10 14:07:05
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
    CX1 DW 2  ; Contador

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
        MOV CX1, 2  ; Inicializar contador
    L1:
        ; === COMPARAR CX1 CON 0 ===
        CMP CX1, 0  ; Comparar CX1 con 0
        MOV T1, 0  ; Asumir falso
        JNE COMP_END_T1  ; Si no son iguales, saltar
        MOV T1, 1  ; Son iguales, verdadero
    COMP_END_T1:
        ; === SALTO CONDICIONAL ===
        CMP T1, 1  ; Verificar condición
        JE L2  ; Saltar si es verdadero
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
        DEC CX1  ; Decrementar CX1
        JMP L1  ; Salto incondicional
    L2:
        ; === FIN DEL BLOQUE ===

    ; === FIN DEL PROGRAMA ===
    MOV AH, 4CH  ; Función de terminación
    MOV AL, 0    ; Código de salida
    INT 21H      ; Llamada al sistema
    
MAIN ENDP
END MAIN
