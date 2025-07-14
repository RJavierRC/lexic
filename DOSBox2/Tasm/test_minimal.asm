; Minimal test file to verify TASM functionality
DATA_SEG    SEGMENT
DATA_SEG    ENDS

CODE_SEG    SEGMENT
   ASSUME CS: CODE_SEG, DS: DATA_SEG

    START:
        MOV   AX, DATA_SEG
        MOV   DS, AX
        
        ; Simple test - just terminate
        MOV    AH,4CH
        MOV    AL,0
        INT    21H
CODE_SEG    ENDS
   END  START
