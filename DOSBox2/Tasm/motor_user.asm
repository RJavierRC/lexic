;===============================================
; MOTOR CONTROL - .COM FORMAT FOR PROTEUS
; Based on working noname.com format
;===============================================

.MODEL TINY
.CODE
ORG 100h

START:
    ; Configure 8255 PPI
    MOV DX, 0303h
    MOV AL, 80h
    OUT DX, AL
    
    ; Move base to 45 degrees
    MOV DX, 0300h
    MOV AL, 45
    OUT DX, AL
    
    ; Short delay
    MOV CX, 500
L1: LOOP L1
    
    ; Move shoulder to 120 degrees
    MOV DX, 0301h
    MOV AL, 120
    OUT DX, AL
    
    ; Short delay
    MOV CX, 500
L2: LOOP L2
    
    ; Move elbow to 90 degrees
    MOV DX, 0302h
    MOV AL, 90
    OUT DX, AL
    
    ; Wait 1 second
    MOV CX, 5000
L3: LOOP L3
    
    ; Exit
    MOV AH, 4Ch
    INT 21h

END START
