;Test assembly code
PORTA   EQU 00H
PORTB   EQU 02H
PORTC   EQU 04H
Config  EQU 06H

DATA_SEG    SEGMENT
DATA_SEG    ENDS

CODE_SEG    SEGMENT
   ASSUME CS: CODE_SEG, DS:DATA_SEG

    START:
        MOV   AX, DATA_SEG
        MOV   DS, AX
        MOV   DX, PORTA
        MOV   AL, 06H
        OUT   DX, AL
        MOV    AH,4CH
        MOV    AL,0
        INT    21H
CODE_SEG    ENDS
   END  START
