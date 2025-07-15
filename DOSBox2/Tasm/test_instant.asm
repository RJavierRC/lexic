.MODEL SMALL
.STACK 100h
.DATA
.CODE
MAIN PROC
    mov ax, @data
    mov ds, ax
    
    ; Programa finalizado
    mov ah, 4Ch
    int 21h
MAIN ENDP
END MAIN
