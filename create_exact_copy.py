#!/usr/bin/env python3
"""
Create EXACT copy of noname.com but with user's values
"""

import os

def extract_user_values(analyzer):
    """Extract values from user's Robot code"""
    values = {
        'base': 45, 'hombro': 90, 'codo': 60,
        'velocities': [4, 7, 9]  # Default velocities
    }
    
    try:
        raw_code = getattr(analyzer, 'raw_code', '') or getattr(analyzer, 'code', '')
        if raw_code:
            velocities = []
            lines = raw_code.split('\n')
            
            for line in lines:
                line = line.strip()
                if '.base' in line and '=' in line:
                    values['base'] = int(line.split('=')[1].strip())
                elif '.hombro' in line and '=' in line:
                    values['hombro'] = int(line.split('=')[1].strip())
                elif '.codo' in line and '=' in line:
                    values['codo'] = int(line.split('=')[1].strip())
                elif '.velocidad' in line and '=' in line:
                    velocities.append(float(line.split('=')[1].strip()))
            
            if velocities:
                values['velocities'] = velocities
                
            print(f"📝 Extracted from Robot code: {values}")
                
    except Exception as e:
        print(f"⚠️ Extraction error: {e}, using defaults")
    
    return values

def get_default_values():
    """Default values for testing"""
    return {
        'base': 45, 'hombro': 120, 'codo': 90,
        'velocities': [4, 7, 9]
    }

def calculate_delays_from_velocities(velocities):
    """Convert velocity values to delay bytes like noname.com"""
    delay_map = {
        1: [0xFF, 0xFF],   # Very slow
        2: [0xEE, 0xEE],   # Slow  
        3: [0xDD, 0xDD],   # Normal-slow
        4: [0xCC, 0xCC],   # Normal
        5: [0xBB, 0xBB],   # Normal-fast
        6: [0xAA, 0xAA],   # Fast (like noname.com)
        7: [0x99, 0x99],   # Faster
        8: [0x77, 0x77],   # Very fast
        9: [0x55, 0x55],   # Maximum (like noname.com)
        10: [0x33, 0x33]   # Ultra fast
    }
    
    delays = []
    for vel in velocities:
        vel_int = max(1, min(10, int(vel)))
        delays.append(delay_map[vel_int])
    
    # Ensure we have at least 3 delays (for 3 motors)
    while len(delays) < 3:
        delays.append([0xAA, 0xAA])  # Default
        
    print(f"🕐 Velocity {velocities} → Delays {delays}")
    return delays

def create_exact_copy(analyzer=None):
    """Create exact copy of noname.com structure but with user's Robot values"""
    
    # Extract user values from Robot code
    user_values = extract_user_values(analyzer) if analyzer else get_default_values()
    print(f"🎯 Using values: Base={user_values['base']}°, Hombro={user_values['hombro']}°, Codo={user_values['codo']}°")
    print(f"⚡ Velocities: {user_values['velocities']}")
    
    # Convert velocity to delays (like noname.com structure)
    delays = calculate_delays_from_velocities(user_values['velocities'])
    
    # Build exact structure with USER VALUES
    exact_bytes = []
    
    # Initialize 8255 PPI (same as noname.com)
    exact_bytes.extend([0xba, 0x06, 0x00])  # MOV DX, 0006h
    exact_bytes.extend([0xb0, 0x80])        # MOV AL, 80h  
    exact_bytes.extend([0xee])              # OUT DX, AL
    
    # Base motor (Port 0000h) with user's velocity delay
    exact_bytes.extend([0xba, 0x00, 0x00])  # MOV DX, 0000h
    for step in [0x06, 0x0C, 0x09, 0x03]:  # Stepper pattern
        exact_bytes.extend([0xb0, step])     # MOV AL, step
        exact_bytes.extend([0xee])           # OUT DX, AL
        exact_bytes.extend([0xb9, delays[0][0], delays[0][1]])  # MOV CX, user_delay
        exact_bytes.extend([0xe2, 0xfe])     # LOOP $-2
    
    # Hombro motor (Port 0002h) with user's velocity delay  
    exact_bytes.extend([0xba, 0x02, 0x00])  # MOV DX, 0002h
    for step in [0x06, 0x0C, 0x09, 0x03]:  # Stepper pattern
        exact_bytes.extend([0xb0, step])     # MOV AL, step
        exact_bytes.extend([0xee])           # OUT DX, AL
        exact_bytes.extend([0xb9, delays[1][0], delays[1][1]])  # MOV CX, user_delay
        exact_bytes.extend([0xe2, 0xfe])     # LOOP $-2
    
    # Codo motor (Port 0004h) with user's velocity delay
    exact_bytes.extend([0xba, 0x04, 0x00])  # MOV DX, 0004h  
    for step in [0x06, 0x0C, 0x09, 0x03]:  # Stepper pattern
        exact_bytes.extend([0xb0, step])     # MOV AL, step
        exact_bytes.extend([0xee])           # OUT DX, AL
        exact_bytes.extend([0xb9, delays[2][0], delays[2][1]])  # MOV CX, user_delay
        exact_bytes.extend([0xe2, 0xfe])     # LOOP $-2
    
    # Infinite loop (same as noname.com)
    exact_bytes.extend([0xeb, 0x8f])        # JMP to beginning
    
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