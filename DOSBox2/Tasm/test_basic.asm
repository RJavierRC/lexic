; Test simple basado en codigo.asm que funciona
PORTA   EQU 00H

DATA_SEG    SEGMENT
DATA_SEG    ENDS

CODE_SEG    SEGMENT
   ASSUME CS: CODE_SEG, DS:DATA_SEG

    START:
        MOV   AX, DATA_SEG
        MOV   DS, AX

        ; Codigo simple - solo un puerto
        MOV   DX, PORTA
        MOV   AL, 06H
        OUT   DX, AL

        MOV    AH,4CH
        MOV    AL,0
        INT    21H
CODE_SEG    ENDS
   END  START
