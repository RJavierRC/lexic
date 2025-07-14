;Simple motor control for Proteus
;Compatible with 8086/8088
;Controls 3 stepper motors via 8255 PPI

.MODEL SMALL
.STACK 100h

.DATA
    ; No data needed

.CODE
MAIN PROC
    ; Initialize data segment
    MOV AX, @DATA
    MOV DS, AX
    
    ; Configure 8255 - All ports as output
    MOV DX, 0307h    ; Control port of 8255
    MOV AL, 80h      ; Configuration: all outputs
    OUT DX, AL
    
    ; Motor A (Base) - Simple step sequence
    MOV DX, 0300h    ; Port A
    MOV AL, 01h      ; Step 1
    OUT DX, AL
    CALL DELAY
    
    MOV AL, 03h      ; Step 2
    OUT DX, AL
    CALL DELAY
    
    MOV AL, 02h      ; Step 3
    OUT DX, AL
    CALL DELAY
    
    MOV AL, 00h      ; Step 4
    OUT DX, AL
    CALL DELAY
    
    ; Motor B (Shoulder) - Simple step sequence
    MOV DX, 0301h    ; Port B
    MOV AL, 01h      ; Step 1
    OUT DX, AL
    CALL DELAY
    
    MOV AL, 03h      ; Step 2
    OUT DX, AL
    CALL DELAY
    
    ; Motor C (Elbow) - Simple step sequence
    MOV DX, 0302h    ; Port C
    MOV AL, 01h      ; Step 1
    OUT DX, AL
    CALL DELAY
    
    MOV AL, 03h      ; Step 2
    OUT DX, AL
    CALL DELAY
    
    ; Exit program
    MOV AH, 4Ch
    MOV AL, 0
    INT 21h

DELAY PROC
    ; Simple delay loop
    PUSH CX
    MOV CX, 0FFFFh
DELAY_LOOP:
    NOP
    LOOP DELAY_LOOP
    POP CX
    RET
DELAY ENDP

MAIN ENDP
END MAIN
