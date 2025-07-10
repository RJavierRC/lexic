.MODEL SMALL

.STACK 100H
.DATA
PORTA  EQU 00H    ; Dirección del Puerto A
PORTB  EQU 02H    ; Dirección del Puerto B
PORTC  EQU 04H    ; Dirección del Puerto C
Config EQU 06H    ; Dirección de la palabra de configuración

.CODE
  MOV DX, Config
  MOV AL, 10000000B  ; Configurar Puertos A, B y C como salidas en modo 0
  OUT DX, AL

START:
  MOV BX, 1         ; Inicializar el contador a 4

ciclo1:
  ; Mover motor en Puerto A
  MOV DX, PORTA
  MOV AL, 00001100B
  OUT DX, AL        

  MOV CX, 0FFFFH
loopy1:
  loop loopy1

  MOV AL, 00000110B
  OUT DX, AL
  
  MOV CX, 0FFFFH     ; Delay 
loopy2:
  loop loopy2

  MOV AL, 00000011B
  OUT DX, AL

  MOV CX, 0FFFFH     ; Delay again
loopy3:
  loop loopy3

  MOV AL, 00001001B
  OUT DX, AL

  MOV CX, 0FFFFH     ; Delay again
loopy4:
  loop loopy4

  DEC BX             ; Decrementar el contador
  JNZ ciclo1         ; Pasar al ciclo2
 
  
           ; Ir a ciclo2
MOV BX, 1
ciclo2:
  ; Mover motor en Puerto B
  MOV DX, PORTB
  MOV AL, 00001100B
  OUT DX, AL        

  MOV CX, 0FFFFH
loopy5:
  loop loopy5

  MOV AL, 00000110B
  OUT DX, AL
  
  MOV CX, 0FFFFH     ; Delay 
loopy6:
  loop loopy6

  MOV AL, 00000011B
  OUT DX, AL

  MOV CX, 0FFFFH     ; Delay again
loopy7:
  loop loopy7

  MOV AL, 00001001B
  OUT DX, AL

  MOV CX, 0FFFFH     ; Delay again
loopy8:
  loop loopy8

  DEC BX             ; Decrementar el contador
  JNZ ciclo2         ; Pasar al ciclo3

 
 MOV BX, 1
ciclo3:
  ; Mover motor en Puerto C
  MOV DX, PORTC
  MOV AL, 00001100B
  OUT DX, AL        

  MOV CX, 0FFFFH
loopy9:
  loop loopy9

  MOV AL, 00000110B
  OUT DX, AL
  
  MOV CX, 0FFFFH     ; Delay 
loopy10:
  loop loopy10

  MOV AL, 00000011B
  OUT DX, AL

  MOV CX, 0FFFFH     ; Delay again
loopy11:
  loop loopy11

  MOV AL, 00001001B
  OUT DX, AL

  MOV CX, 0FFFFH     ; Delay again
loopy12:
  loop loopy12

  DEC BX             ; Decrementar el contador
  JNZ ciclo3         ; Pasar al ciclo3
  RET

END