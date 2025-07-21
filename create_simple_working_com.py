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
    
    # Configure 8255 PPI for YOUR Proteus setup (0x0000-0x0003)
    machine_code.extend([0xBA, 0x03, 0x00])  # MOV DX, 0003h (Control register)
    machine_code.extend([0xB0, 0x80])        # MOV AL, 80h (All ports output)
    machine_code.extend([0xEE])              # OUT DX, AL
    
    # Move motors based on actual angles from your code
    print(f"🔧 Moving motors: Base={base_angle}°, Hombro={hombro_angle}°, Codo={codo_angle}°")
    
    stepper_sequence = [0x06, 0x0C, 0x09, 0x03]
    
    # Add infinite loop start (like noname.com)
    loop_start = len(machine_code)
    
    # BASE motor - move to specified angle (Port A = 0x0000)
    if base_angle > 0:
        steps = max(1, abs(base_angle) // 15)  # 1 step per 15 degrees
        machine_code.extend([0xBA, 0x00, 0x00])  # MOV DX, 0000h (Port A)
        for step_num in range(steps):
            step_value = stepper_sequence[step_num % 4]
            machine_code.extend([0xB0, step_value])  # MOV AL, step
            machine_code.extend([0xEE])              # OUT DX, AL
            machine_code.extend([0xB9, delay & 0xFF, (delay >> 8) & 0xFF])  # MOV CX, delay
            machine_code.extend([0xE2, 0xFE])        # LOOP $-2
    
    # HOMBRO motor - move to specified angle (Port B = 0x0001)
    if hombro_angle > 0:
        steps = max(1, abs(hombro_angle) // 15)
        machine_code.extend([0xBA, 0x01, 0x00])  # MOV DX, 0001h (Port B)
        for step_num in range(steps):
            step_value = stepper_sequence[step_num % 4]
            machine_code.extend([0xB0, step_value])  # MOV AL, step
            machine_code.extend([0xEE])              # OUT DX, AL
            machine_code.extend([0xB9, delay & 0xFF, (delay >> 8) & 0xFF])  # MOV CX, delay
            machine_code.extend([0xE2, 0xFE])        # LOOP $-2
    
    # CODO motor - move to specified angle (Port C = 0x0002)
    if codo_angle > 0:
        steps = max(1, abs(codo_angle) // 15)
        machine_code.extend([0xBA, 0x02, 0x00])  # MOV DX, 0002h (Port C)
        for step_num in range(steps):
            step_value = stepper_sequence[step_num % 4]
            machine_code.extend([0xB0, step_value])  # MOV AL, step
            machine_code.extend([0xEE])              # OUT DX, AL
            machine_code.extend([0xB9, delay & 0xFF, (delay >> 8) & 0xFF])  # MOV CX, delay
            machine_code.extend([0xE2, 0xFE])        # LOOP $-2
    
    # Return to home positions (correct ports 0x0000, 0x0001, 0x0002)
    for port in [0x00, 0x01, 0x02]:
        machine_code.extend([0xBA, port, 0x00])  # MOV DX, port
        machine_code.extend([0xB0, 0x00])        # MOV AL, 0
        machine_code.extend([0xEE])              # OUT DX, AL
        
        # Fast return delay
        machine_code.extend([0xB9, 0x55, 0x55])  # MOV CX, 5555h
        machine_code.extend([0xE2, 0xFE])        # LOOP $-2
    
    # INFINITE LOOP (like noname.com) - keeps motors moving continuously
    jmp_offset = loop_start - (len(machine_code) + 3)
    machine_code.extend([0xE9, jmp_offset & 0xFF, (jmp_offset >> 8) & 0xFF])  # JMP loop_start
    
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