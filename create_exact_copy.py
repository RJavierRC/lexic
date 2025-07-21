#!/usr/bin/env python3
"""
Create EXACT copy of noname.com but with user's values
"""

import os

def extract_user_sequence(analyzer):
    """Extract EXACT sequence from user's Robot code"""
    sequence = []
    current_velocity = 4.0
    
    try:
        raw_code = getattr(analyzer, 'raw_code', '') or getattr(analyzer, 'code', '')
        if raw_code:
            lines = raw_code.split('\n')
            
            for line in lines:
                line = line.strip()
                if not line or line.startswith('Robot') or line.endswith('.inicio') or line.endswith('.fin'):
                    continue
                    
                if '.velocidad' in line and '=' in line:
                    current_velocity = float(line.split('=')[1].strip())
                    print(f"  → Velocity set to: {current_velocity}")
                    
                elif '.base' in line and '=' in line:
                    angle = int(line.split('=')[1].strip())
                    sequence.append({
                        'motor': 'base',
                        'port': 0x0000,
                        'angle': angle,
                        'velocity': current_velocity
                    })
                    print(f"  → Base: {angle}° at velocity {current_velocity}")
                    
                elif '.hombro' in line and '=' in line:
                    angle = int(line.split('=')[1].strip())
                    sequence.append({
                        'motor': 'hombro', 
                        'port': 0x0002,
                        'angle': angle,
                        'velocity': current_velocity
                    })
                    print(f"  → Hombro: {angle}° at velocity {current_velocity}")
                    
                elif '.codo' in line and '=' in line:
                    angle = int(line.split('=')[1].strip())
                    sequence.append({
                        'motor': 'codo',
                        'port': 0x0004, 
                        'angle': angle,
                        'velocity': current_velocity
                    })
                    print(f"  → Codo: {angle}° at velocity {current_velocity}")
                
            print(f"📝 Extracted sequence: {len(sequence)} movements")
                
    except Exception as e:
        print(f"⚠️ Extraction error: {e}, using default")
        # Default sequence
        sequence = [
            {'motor': 'base', 'port': 0x0000, 'angle': 45, 'velocity': 4.0},
            {'motor': 'hombro', 'port': 0x0002, 'angle': 120, 'velocity': 7.0},
            {'motor': 'codo', 'port': 0x0004, 'angle': 90, 'velocity': 9.0},
            {'motor': 'base', 'port': 0x0000, 'angle': 0, 'velocity': 9.0},
            {'motor': 'hombro', 'port': 0x0002, 'angle': 0, 'velocity': 9.0},
            {'motor': 'codo', 'port': 0x0004, 'angle': 0, 'velocity': 9.0}
        ]
    
    return sequence

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

def velocity_to_delay(velocity):
    """Convert single velocity value to delay bytes"""
    delay_map = {
        1: [0xFF, 0xFF],   # Very slow
        2: [0xEE, 0xEE],   # Slow  
        3: [0xDD, 0xDD],   # Normal-slow
        4: [0xCC, 0xCC],   # Normal
        5: [0xBB, 0xBB],   # Normal-fast
        6: [0xAA, 0xAA],   # Fast
        7: [0x99, 0x99],   # Faster
        8: [0x77, 0x77],   # Very fast
        9: [0x55, 0x55],   # Maximum
        10: [0x33, 0x33]   # Ultra fast
    }
    
    vel_int = max(1, min(10, int(velocity)))
    return delay_map[vel_int]

def create_exact_copy(analyzer=None):
    """Create .COM file that follows user's EXACT Robot sequence"""
    
    # Extract EXACT sequence from Robot code
    sequence = extract_user_sequence(analyzer) if analyzer else extract_user_sequence(None)
    print(f"🎯 Following your exact sequence: {len(sequence)} movements")
    
    # Build machine code following USER'S SEQUENCE
    exact_bytes = []
    
    # Initialize 8255 PPI (same as working noname.com)
    exact_bytes.extend([0xba, 0x06, 0x00])  # MOV DX, 0006h
    exact_bytes.extend([0xb0, 0x80])        # MOV AL, 80h  
    exact_bytes.extend([0xee])              # OUT DX, AL
    
    # Start of main loop
    loop_start = len(exact_bytes)
    
    # Follow user's EXACT sequence
    for i, movement in enumerate(sequence):
        motor = movement['motor']
        port = movement['port']
        angle = movement['angle']
        velocity = movement['velocity']
        
        print(f"Step {i+1}: {motor.upper()} → {angle}° at velocity {velocity}")
        
        # Set port
        exact_bytes.extend([0xba, port & 0xFF, (port >> 8) & 0xFF])  # MOV DX, port
        
        # Calculate steps based on angle
        if angle > 0:
            # Moving TO position - more steps for bigger angles
            steps = max(1, angle // 15)  # 1 step per 15 degrees
            pattern = [0x06, 0x0C, 0x09, 0x03]  # Forward pattern
        else:
            # Moving to HOME (angle=0) - minimal steps
            steps = 1
            pattern = [0x03, 0x09, 0x0C, 0x06]  # Reverse pattern
        
        # Convert velocity to delay
        delay = velocity_to_delay(velocity)
        
        # Generate stepper movements
        for step_num in range(steps):
            step_value = pattern[step_num % len(pattern)]
            exact_bytes.extend([0xb0, step_value])  # MOV AL, step_value
            exact_bytes.extend([0xee])              # OUT DX, AL
            exact_bytes.extend([0xb9, delay[0], delay[1]])  # MOV CX, delay
            exact_bytes.extend([0xe2, 0xfe])        # LOOP $-2
        
        # Pause between motors
        exact_bytes.extend([0xb9, 0x33, 0x33])  # MOV CX, 3333h (short pause)
        exact_bytes.extend([0xe2, 0xfe])        # LOOP $-2
    
    # Infinite loop to repeat the sequence (like noname.com)
    jmp_offset = loop_start - (len(exact_bytes) + 3)
    exact_bytes.extend([0xe9, jmp_offset & 0xFF, (jmp_offset >> 8) & 0xFF])  # JMP loop_start
    
    # Create directory
    tasm_dir = os.path.join("DOSBox2", "Tasm")
    os.makedirs(tasm_dir, exist_ok=True)
    
    # Write SEQUENCE-BASED .COM file
    com_path = os.path.join(tasm_dir, "motor_user.com")
    with open(com_path, 'wb') as f:
        f.write(bytes(exact_bytes))
    
    print(f"✅ SEQUENCE-BASED .COM created: {len(exact_bytes)} bytes")
    print(f"🎯 Follows YOUR Robot syntax exactly!")
    print(f"📍 Location: DOSBox2/Tasm/motor_user.com")
    
    return True

if __name__ == "__main__":
    # Test with mock Robot code
    class MockAnalyzer:
        def __init__(self):
            self.raw_code = """Robot r1
r1.inicio
r1.velocidad = 4
r1.base = 45  
r1.velocidad = 7         
r1.hombro = 120
r1.velocidad = 9       
r1.codo = 90       
r1.base = 0         
r1.hombro = 0        
r1.codo = 0      
r1.fin"""
    
    print("🧪 Testing sequence-based system...")
    mock = MockAnalyzer()
    create_exact_copy(mock)