
DATA_SEG    SEGMENT
; aqui poner las variables
DATA_SEG    ENDS

CODE_SEG    SEGMENT
   ASSUME CS: CODE_SEG, DS:DATA_SEG

    START:
        MOV   AX, DATA_SEG
        MOV   DS, AX

         ; aqui poner el codigo de movimiento de los motores

        MOV    AH,4CH
        MOV    AL,0
        INT    21H
CODE_SEG    ENDS
   END  START
