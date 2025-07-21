#!/usr/bin/env python3
"""
Create EXACT copy of noname.com but with user's values
"""

import os

def create_exact_copy():
    """Create exact copy of noname.com structure"""
    
    # EXACT hex from working noname.com
    exact_bytes = [
        0xba, 0x06, 0x00,  # MOV DX, 0006h
        0xb0, 0x80,        # MOV AL, 80h  
        0xee,              # OUT DX, AL
        
        # Port 0000h sequence
        0xba, 0x00, 0x00,  # MOV DX, 0000h
        0xb0, 0x06,        # MOV AL, 06h
        0xee,              # OUT DX, AL
        0xb9, 0xff, 0xff,  # MOV CX, FFFFh
        0xe2, 0xfe,        # LOOP $-2
        
        0xb0, 0x0c,        # MOV AL, 0Ch
        0xee,              # OUT DX, AL
        0xb9, 0xff, 0xff,  # MOV CX, FFFFh  
        0xe2, 0xfe,        # LOOP $-2
        
        0xb0, 0x09,        # MOV AL, 09h
        0xee,              # OUT DX, AL
        0xb9, 0xff, 0xff,  # MOV CX, FFFFh
        0xe2, 0xfe,        # LOOP $-2
        
        0xb0, 0x03,        # MOV AL, 03h
        0xee,              # OUT DX, AL
        0xb9, 0xff, 0xff,  # MOV CX, FFFFh
        0xe2, 0xfe,        # LOOP $-2
        
        # Port 0002h sequence  
        0xba, 0x02, 0x00,  # MOV DX, 0002h
        0xb0, 0x06,        # MOV AL, 06h
        0xee,              # OUT DX, AL
        0xb9, 0xaa, 0xaa,  # MOV CX, AAAAh
        0xe2, 0xfe,        # LOOP $-2
        
        0xb0, 0x0c,        # MOV AL, 0Ch
        0xee,              # OUT DX, AL
        0xb9, 0xaa, 0xaa,  # MOV CX, AAAAh
        0xe2, 0xfe,        # LOOP $-2
        
        0xb0, 0x09,        # MOV AL, 09h
        0xee,              # OUT DX, AL
        0xb9, 0xaa, 0xaa,  # MOV CX, AAAAh
        0xe2, 0xfe,        # LOOP $-2
        
        0xb0, 0x03,        # MOV AL, 03h
        0xee,              # OUT DX, AL
        0xb9, 0xaa, 0xaa,  # MOV CX, AAAAh
        0xe2, 0xfe,        # LOOP $-2
        
        # Port 0004h sequence
        0xba, 0x04, 0x00,  # MOV DX, 0004h
        0xb0, 0x06,        # MOV AL, 06h
        0xee,              # OUT DX, AL
        0xb9, 0x55, 0x55,  # MOV CX, 5555h
        0xe2, 0xfe,        # LOOP $-2
        
        0xb0, 0x0c,        # MOV AL, 0Ch
        0xee,              # OUT DX, AL
        0xb9, 0x55, 0x55,  # MOV CX, 5555h
        0xe2, 0xfe,        # LOOP $-2
        
        0xb0, 0x09,        # MOV AL, 09h
        0xee,              # OUT DX, AL
        0xb9, 0x55, 0x55,  # MOV CX, 5555h
        0xe2, 0xfe,        # LOOP $-2
        
        0xb0, 0x03,        # MOV AL, 03h
        0xee,              # OUT DX, AL
        0xb9, 0x55, 0x55,  # MOV CX, 5555h
        0xe2, 0xfe,        # LOOP $-2
        
        # Infinite loop
        0xeb, 0x8f         # JMP to beginning
    ]
    
    # Create directory
    tasm_dir = os.path.join("DOSBox2", "Tasm")
    os.makedirs(tasm_dir, exist_ok=True)
    
    # Write exact copy
    com_path = os.path.join(tasm_dir, "motor_user.com")
    with open(com_path, 'wb') as f:
        f.write(bytes(exact_bytes))
    
    print(f"✅ EXACT copy created: {len(exact_bytes)} bytes")
    print("🎯 This should work EXACTLY like noname.com")
    print("📍 Location: DOSBox2/Tasm/motor_user.com")
    
    # Verify against original
    original_path = os.path.join(tasm_dir, "noname.com")
    if os.path.exists(original_path):
        with open(original_path, 'rb') as f:
            original_bytes = f.read()
        
        print(f"🔍 Original: {len(original_bytes)} bytes")
        print(f"🔍 Copy: {len(exact_bytes)} bytes")
        
        if exact_bytes == list(original_bytes):
            print("✅ PERFECT MATCH!")
        else:
            print("❌ Different - checking first difference...")
            for i, (orig, copy) in enumerate(zip(original_bytes, exact_bytes)):
                if orig != copy:
                    print(f"First diff at byte {i}: orig={orig:02X} copy={copy:02X}")
                    break
    
    return True

if __name__ == "__main__":
    create_exact_copy()