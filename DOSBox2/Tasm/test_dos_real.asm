; Programa DOS REAL para 8086 - test_dos_real
; Compatible con MS-DOS y Proteus ISIS
; Formato: .COM o .EXE pequeno

.MODEL TINY
.CODE
ORG 100h        ; Inicio para formato .COM

START:
    ; Configurar segmento de datos
    mov ax, cs
    mov ds, ax
    mov es, ax
    
    ; Mostrar mensaje de inicio
    mov dx, OFFSET msg_inicio
    mov ah, 09h
    int 21h
    
    ; Configurar 8255 PPI
    ; Puerto de control = 0303h
    mov dx, 0303h
    mov al, 80h     ; Configuracion: todos los puertos como salida
    out dx, al
    
    ; Inicializar puertos
    mov dx, 0300h   ; Puerto A (Base)
    mov al, 0
    out dx, al
    
    mov dx, 0301h   ; Puerto B (Hombro)
    mov al, 0
    out dx, al
    
    mov dx, 0302h   ; Puerto C (Codo)
    mov al, 0
    out dx, al
    
    ; Secuencia de movimientos del robot
    call MOVER_BASE
    call DELAY
    
    call MOVER_HOMBRO
    call DELAY
    
    call MOVER_CODO
    call DELAY
    
    ; Retornar a home
    call ROBOT_HOME
    
    ; Mostrar mensaje final
    mov dx, OFFSET msg_fin
    mov ah, 09h
    int 21h
    
    ; Terminar programa (DOS real)
    mov ah, 4Ch
    mov al, 0
    int 21h

; Procedimiento para mover base
MOVER_BASE PROC NEAR
    mov dx, 0300h   ; Puerto A
    mov cx, 10      ; 10 pasos
    
LOOP_BASE:
    mov al, 01h
    out dx, al
    call DELAY_CORTO
    
    mov al, 03h
    out dx, al
    call DELAY_CORTO
    
    mov al, 02h
    out dx, al
    call DELAY_CORTO
    
    mov al, 06h
    out dx, al
    call DELAY_CORTO
    
    loop LOOP_BASE
    ret
MOVER_BASE ENDP

; Procedimiento para mover hombro
MOVER_HOMBRO PROC NEAR
    mov dx, 0301h   ; Puerto B
    mov cx, 8       ; 8 pasos
    
LOOP_HOMBRO:
    mov al, 01h
    out dx, al
    call DELAY_CORTO
    
    mov al, 03h
    out dx, al
    call DELAY_CORTO
    
    mov al, 02h
    out dx, al
    call DELAY_CORTO
    
    mov al, 06h
    out dx, al
    call DELAY_CORTO
    
    loop LOOP_HOMBRO
    ret
MOVER_HOMBRO ENDP

; Procedimiento para mover codo
MOVER_CODO PROC NEAR
    mov dx, 0302h   ; Puerto C
    mov cx, 6       ; 6 pasos
    
LOOP_CODO:
    mov al, 01h
    out dx, al
    call DELAY_CORTO
    
    mov al, 03h
    out dx, al
    call DELAY_CORTO
    
    mov al, 02h
    out dx, al
    call DELAY_CORTO
    
    mov al, 06h
    out dx, al
    call DELAY_CORTO
    
    loop LOOP_CODO
    ret
MOVER_CODO ENDP

; Retornar robot a home
ROBOT_HOME PROC NEAR
    mov dx, 0300h
    mov al, 0
    out dx, al
    
    mov dx, 0301h
    mov al, 0
    out dx, al
    
    mov dx, 0302h
    mov al, 0
    out dx, al
    ret
ROBOT_HOME ENDP

; Delay corto para pasos
DELAY_CORTO PROC NEAR
    push cx
    mov cx, 1000h
DELAY_LOOP1:
    nop
    nop
    loop DELAY_LOOP1
    pop cx
    ret
DELAY_CORTO ENDP

; Delay largo
DELAY PROC NEAR
    push cx
    mov cx, 8000h
DELAY_LOOP2:
    nop
    nop
    nop
    loop DELAY_LOOP2
    pop cx
    ret
DELAY ENDP

; Datos del programa
msg_inicio  DB 'Robot test_dos_real iniciado', 0Dh, 0Ah, '$'
msg_fin     DB 'Robot completado', 0Dh, 0Ah, '$'

END START
