global _start\n;Test assembly code
PORTA   EQU 00H
PORTB   EQU 02H
PORTC   EQU 04H
Config  EQU 06H

section .data


section .text


    START:
        MOV   AX, DATA_SEG
        MOV   DS, AX
        MOV   DX, PORTA
        MOV   AL, 06H
        OUT   DX, AL
        MOV    AH,4CH
        MOV    AL,0
        INT    21H


