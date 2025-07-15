; Programa para Proteus ISIS - test_proteus
; Compatible con procesador 8086
; Configurado para puertos 0300h-0303h (8255 PPI)

.MODEL SMALL
.STACK 200h

.DATA
    ; Configuracin del 8255 PPI
    PORT_A      EQU 0300h    ; Puerto A (Motor Base)
    PORT_B      EQU 0301h    ; Puerto B (Motor Hombro) 
    PORT_C      EQU 0302h    ; Puerto C (Motor Codo)
    CONTROL_REG EQU 0303h    ; Registro de control 8255
    
    ; Configuracin: Todos los puertos como salida
    CONFIG_8255 DB  80h      ; 10000000b - Modo 0, todos salida
    
    ; Variables del robot
    base_pos    DW  0        ; Posicin actual base
    hombro_pos  DW  0        ; Posicin actual hombro
    codo_pos    DW  0        ; Posicin actual codo
    velocidad   DW  2        ; Velocidad por defecto
    
    ; Secuencias de pasos para motores
    paso_seq    DB  01h, 03h, 02h, 06h, 04h, 0Ch, 08h, 09h
    
    ; Mensaje de inicio
    msg_inicio  DB  'Robot test_proteus iniciado$'

.CODE
MAIN PROC
    mov ax, @data
    mov ds, ax
    
    ; Configurar 8255 PPI
    mov dx, CONTROL_REG
    mov al, CONFIG_8255
    out dx, al
    
    ; Inicializar puertos
    mov dx, PORT_A
    mov al, 0
    out dx, al
    
    mov dx, PORT_B  
    mov al, 0
    out dx, al
    
    mov dx, PORT_C
    mov al, 0
    out dx, al
    
    ; Mostrar mensaje de inicio
    mov dx, OFFSET msg_inicio
    mov ah, 09h
    int 21h
    
    ; Programa principal del robot
    call ROBOT_SEQUENCE
    
    ; Esperar tecla y terminar
    mov ah, 01h
    int 21h
    
    ; Terminar programa
    mov ah, 4Ch
    int 21h
MAIN ENDP

; Secuencia principal del robot
ROBOT_SEQUENCE PROC
    ; Configurar velocidad
    mov ax, velocidad
    push ax
    
    ; Mover base a 45 grados
    mov ax, 45
    call MOVER_BASE
    
    ; Esperar
    call DELAY_1S
    
    ; Mover hombro a 120 grados
    mov ax, 120
    call MOVER_HOMBRO
    
    ; Esperar
    call DELAY_1S
    
    ; Mover codo a 90 grados
    mov ax, 90
    call MOVER_CODO
    
    ; Esperar
    call DELAY_1S
    
    ; Retornar a home
    call ROBOT_HOME
    
    ret
ROBOT_SEQUENCE ENDP

; Mover motor de la base
MOVER_BASE PROC
    push ax
    push dx
    push cx
    
    mov dx, PORT_A
    mov cx, 8        ; 8 pasos por revolucin simplificado
    
LOOP_BASE:
    mov al, 01h      ; Patrn simple para Proteus
    out dx, al
    call DELAY_MOTOR
    
    mov al, 03h
    out dx, al  
    call DELAY_MOTOR
    
    mov al, 02h
    out dx, al
    call DELAY_MOTOR
    
    mov al, 00h
    out dx, al
    call DELAY_MOTOR
    
    loop LOOP_BASE
    
    pop cx
    pop dx
    pop ax
    ret
MOVER_BASE ENDP

; Mover motor del hombro
MOVER_HOMBRO PROC
    push ax
    push dx
    push cx
    
    mov dx, PORT_B
    mov cx, 8
    
LOOP_HOMBRO:
    mov al, 01h
    out dx, al
    call DELAY_MOTOR
    
    mov al, 03h
    out dx, al
    call DELAY_MOTOR
    
    mov al, 02h
    out dx, al
    call DELAY_MOTOR
    
    mov al, 00h
    out dx, al
    call DELAY_MOTOR
    
    loop LOOP_HOMBRO
    
    pop cx
    pop dx
    pop ax
    ret
MOVER_HOMBRO ENDP

; Mover motor del codo
MOVER_CODO PROC
    push ax
    push dx
    push cx
    
    mov dx, PORT_C
    mov cx, 8
    
LOOP_CODO:
    mov al, 01h
    out dx, al
    call DELAY_MOTOR
    
    mov al, 03h
    out dx, al
    call DELAY_MOTOR
    
    mov al, 02h
    out dx, al
    call DELAY_MOTOR
    
    mov al, 00h
    out dx, al
    call DELAY_MOTOR
    
    loop LOOP_CODO
    
    pop cx
    pop dx
    pop ax
    ret
MOVER_CODO ENDP

; Retornar robot a posicin home
ROBOT_HOME PROC
    ; Apagar todos los motores
    mov dx, PORT_A
    mov al, 0
    out dx, al
    
    mov dx, PORT_B
    mov al, 0
    out dx, al
    
    mov dx, PORT_C
    mov al, 0
    out dx, al
    
    ret
ROBOT_HOME ENDP

; Delay para motores
DELAY_MOTOR PROC
    push cx
    mov cx, 0FFFFh
DELAY_LOOP1:
    nop
    loop DELAY_LOOP1
    pop cx
    ret
DELAY_MOTOR ENDP

; Delay de 1 segundo
DELAY_1S PROC
    push cx
    push dx
    
    mov cx, 100      ; Repetir 100 veces
DELAY_1S_LOOP:
    push cx
    mov cx, 0FFFFh
DELAY_1S_INNER:
    nop
    loop DELAY_1S_INNER
    pop cx
    loop DELAY_1S_LOOP
    
    pop dx
    pop cx
    ret
DELAY_1S ENDP

END MAIN
