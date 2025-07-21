#!/usr/bin/env python3
"""
SIMPLE working .COM generator based on noname.com structure
No complex delays - just direct motor control that works in Proteus
"""

import os

def create_simple_working_com(analyzer):
    """Create working motor_user.com based on noname.com structure"""
    try:
        tasm_dir = os.path.join("DOSBox2", "Tasm")
        os.makedirs(tasm_dir, exist_ok=True)
        
        # Extract values from user code
        motor_values = extract_simple_values(analyzer)
        print(f"🎯 Simple system - extracted values:")
        print(f"• Base: {motor_values['base']}°")
        print(f"• Hombro: {motor_values['hombro']}°") 
        print(f"• Codo: {motor_values['codo']}°")
        print(f"• Velocity: {motor_values['velocidad']}")
        
        # Generate SIMPLE machine code like noname.com
        machine_code = generate_simple_code(motor_values)
        
        # Write .COM file
        com_path = os.path.join(tasm_dir, "motor_user.com")
        with open(com_path, 'wb') as f:
            f.write(bytes(machine_code))
        
        print(f"✅ Simple motor_user.com created! Size: {len(machine_code)} bytes")
        print("🚀 Based on working noname.com structure")
        
        return True, motor_values
        
    except Exception as e:
        print(f"❌ Error: {e}")
        return False, {}

def extract_simple_values(analyzer):
    """Extract motor values from analyzer"""
    values = {'base': 45, 'hombro': 90, 'codo': 60, 'velocidad': 3}
    
    try:
        # Try to get raw code
        raw_code = getattr(analyzer, 'raw_code', '') or getattr(analyzer, 'code', '')
        
        if raw_code:
            lines = raw_code.split('\n')
            for line in lines:
                line = line.strip()
                if '.base' in line and '=' in line:
                    try:
                        values['base'] = int(line.split('=')[1].strip())
                    except: pass
                elif '.hombro' in line and '=' in line:
                    try:
                        values['hombro'] = int(line.split('=')[1].strip())
                    except: pass
                elif '.codo' in line and '=' in line:
                    try:
                        values['codo'] = int(line.split('=')[1].strip())
                    except: pass
                elif '.velocidad' in line and '=' in line:
                    try:
                        values['velocidad'] = float(line.split('=')[1].strip())
                    except: pass
                        
        print(f"📝 Extracted: base={values['base']}°, hombro={values['hombro']}°, codo={values['codo']}°")
        
    except Exception as e:
        print(f"⚠️ Extraction error, using defaults: {e}")
    
    return values

def generate_simple_code(values):
    """Generate simple machine code like noname.com - NO CPU overload"""
    
    base_angle = values['base']
    hombro_angle = values['hombro']
    codo_angle = values['codo']
    velocity = values['velocidad']
    
    # Use EXACT delays from working noname.com
    # Higher velocity = shorter delay
    if velocity >= 8:
        delay = 0x5555  # Fast (like noname.com)
    elif velocity >= 4:
        delay = 0xAAAA  # Normal (like noname.com)
    else:
        delay = 0xFFFF  # Slow (like noname.com)
        
    machine_code = []
    
    # EXACT structure from working noname.com
    # Configure 8255 PPI
    machine_code.extend([0xBA, 0x06, 0x00])  # MOV DX, 0006h (like noname.com)
    machine_code.extend([0xB0, 0x80])        # MOV AL, 80h
    machine_code.extend([0xEE])              # OUT DX, AL
    
    # Use EXACT stepper patterns from noname.com
    stepper_pattern = [0x06, 0x0C, 0x09, 0x03]  # 4-step pattern
    
    # Move BASE motor with stepper pattern
    machine_code.extend([0xBA, 0x00, 0x00])  # MOV DX, 0000h
    for step in stepper_pattern:
        machine_code.extend([0xB0, step])    # MOV AL, step
        machine_code.extend([0xEE])          # OUT DX, AL
        machine_code.extend([0xB9, delay & 0xFF, (delay >> 8) & 0xFF])  # MOV CX, delay
        machine_code.extend([0xE2, 0xFE])    # LOOP $-2
    
    # Move HOMBRO motor with stepper pattern
    machine_code.extend([0xBA, 0x02, 0x00])  # MOV DX, 0002h
    for step in stepper_pattern:
        machine_code.extend([0xB0, step])    # MOV AL, step
        machine_code.extend([0xEE])          # OUT DX, AL
        machine_code.extend([0xB9, delay & 0xFF, (delay >> 8) & 0xFF])  # MOV CX, delay
        machine_code.extend([0xE2, 0xFE])    # LOOP $-2
    
    # Move CODO motor with stepper pattern
    machine_code.extend([0xBA, 0x04, 0x00])  # MOV DX, 0004h
    for step in stepper_pattern:
        machine_code.extend([0xB0, step])    # MOV AL, step
        machine_code.extend([0xEE])          # OUT DX, AL
        machine_code.extend([0xB9, delay & 0xFF, (delay >> 8) & 0xFF])  # MOV CX, delay
        machine_code.extend([0xE2, 0xFE])    # LOOP $-2
    
    # Return to home positions (like noname.com)
    for port in [0x00, 0x02, 0x04]:
        machine_code.extend([0xBA, port, 0x00])  # MOV DX, port
        machine_code.extend([0xB0, 0x00])        # MOV AL, 0
        machine_code.extend([0xEE])              # OUT DX, AL
        
        # Fast return delay (like noname.com)
        machine_code.extend([0xB9, 0x55, 0x55])  # MOV CX, 5555h
        machine_code.extend([0xE2, 0xFE])        # LOOP $-2
    
    # Exit
    machine_code.extend([0xB8, 0x00, 0x4C])  # MOV AX, 4C00h
    machine_code.extend([0xCD, 0x21])        # INT 21h
    
    print(f"📦 Generated {len(machine_code)} bytes - simple and fast!")
    return machine_code

# Main function for compatibility
def create_dynamic_com_from_analyzer_fixed(analyzer):
    """Compatibility function for main.py"""
    try:
        success, values = create_simple_working_com(analyzer)
        return success
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

if __name__ == "__main__":
    # Test
    class TestAnalyzer:
        def __init__(self):
            self.raw_code = """Robot r1
r1.inicio
r1.velocidad = 5
r1.base = 45  
r1.hombro = 120
r1.codo = 90       
r1.fin"""
    
    print("🧪 Testing SIMPLE working system...")
    analyzer = TestAnalyzer()
    create_simple_working_com(analyzer)