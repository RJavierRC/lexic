#!/usr/bin/env python3
"""
Create .COM based on WORKING robot.asm from your friend
This uses the PROVEN patterns and sequences that work
"""

import os

def create_working_robot_com(analyzer=None):
    """Create .COM following EXACT robot.asm sequence with Robot syntax control"""
    
    # Extract Robot code values
    robot_values = extract_robot_values(analyzer) if analyzer else get_default_values()
    print(f"🎯 Robot values: Base={robot_values['base']}°, Hombro={robot_values['hombro']}°, Codo={robot_values['codo']}°")
    print(f"⚡ Velocidades: {robot_values['velocidades']}")
    
    # Build machine code using EXACT robot.asm structure
    machine_code = []
    
    # Initialize 8255 (exactly like robot.asm line 6-8)
    machine_code.extend([0xBA, 0x06, 0x00])  # MOV DX, 06h
    machine_code.extend([0xB0, 0x80])        # MOV AL, 80h (10000000b)
    machine_code.extend([0xEE])              # OUT DX, AL
    
    # Repetition counter (exactly like robot.asm line 10)
    repetitions = robot_values.get('repetitions', 2)
    machine_code.extend([0xBE, repetitions & 0xFF, (repetitions >> 8) & 0xFF])  # MOV SI, repetitions
    
    # Main loop start (CICLO1:)
    loop_start = len(machine_code)
    
    print("🤖 Following EXACT robot.asm sequence...")
    
    # === EXACT ROBOT.ASM SEQUENCE with Robot syntax mapping ===
    
    # Get velocities for each motor from Robot syntax
    base_velocity = get_delay_function(robot_values['velocidades'][0] if robot_values['velocidades'] else 2)
    hombro_velocity = get_delay_function(robot_values['velocidades'][1] if len(robot_values['velocidades']) > 1 else 3)
    codo_velocity = get_delay_function(robot_values['velocidades'][2] if len(robot_values['velocidades']) > 2 else 5)
    
    print(f"🎯 Motor velocities: Base={base_velocity}, Hombro={hombro_velocity}, Codo={codo_velocity}")
    
    # MOTOR BASE CONTROL (Lines 12-32: Port 0x00)
    print(f"🔧 BASE Motor: {robot_values['base']}° with {base_velocity}")
    machine_code.extend([0xBA, 0x00, 0x00])  # MOV DX, 00h
    
    # 4-step sequence for BASE motor (lines 12-27)
    patterns_base = [0x0C, 0x06, 0x03, 0x09]  # Exact from robot.asm
    steps_base = max(1, abs(robot_values['base']) // 15)  # More steps for larger angles
    
    for i in range(steps_base):
        pattern = patterns_base[i % len(patterns_base)]
        machine_code.extend([0xB0, pattern])    # MOV AL, pattern
        machine_code.extend([0xEE])             # OUT DX, AL
        add_delay_call(machine_code, base_velocity)
    
    # BASE motor reset (lines 29-32)
    machine_code.extend([0xBA, 0x00, 0x00])  # MOV DX, 00h
    machine_code.extend([0xB0, 0xC0])        # MOV AL, 11000000b
    machine_code.extend([0xEE])              # OUT DX, AL
    add_delay_call(machine_code, base_velocity)
    
    # MOTOR HOMBRO CONTROL (Lines 34-41: Port 0x02)
    print(f"🔧 HOMBRO Motor: {robot_values['hombro']}° with {hombro_velocity}")
    machine_code.extend([0xBA, 0x02, 0x00])  # MOV DX, 02h
    
    # HOMBRO sequence (lines 34-37)
    machine_code.extend([0xB0, 0x0C])        # MOV AL, 00001100b
    machine_code.extend([0xEE])              # OUT DX, AL
    add_delay_call(machine_code, hombro_velocity)
    
    # HOMBRO sequence (lines 39-41)
    machine_code.extend([0xB0, 0x06])        # MOV AL, 00000110b
    machine_code.extend([0xEE])              # OUT DX, AL
    add_delay_call(machine_code, hombro_velocity)
    
    # HOMBRO reset sequence (lines 43-46)
    machine_code.extend([0xBA, 0x02, 0x00])  # MOV DX, 02h
    machine_code.extend([0xB0, 0xC0])        # MOV AL, 11000000b
    machine_code.extend([0xEE])              # OUT DX, AL
    add_delay_call(machine_code, codo_velocity)  # Use codo velocity for transition
    
    # MOTOR CODO CONTROL (Lines 48-82: Complex sequence with both ports)
    print(f"🔧 CODO Motor: {robot_values['codo']}° with {codo_velocity}")
    steps_codo = max(2, abs(robot_values['codo']) // 20)  # More steps for codo
    
    # Complex sequence from robot.asm lines 48-82 - CONTROLS THE THIRD MOTOR
    codo_sequence = [
        (0x02, 0x90),  # Line 48-51: Port 02h, pattern 10010000b
        (0x02, 0x0C),  # Line 54-56: Port 02h, pattern 00001100b  
        (0x02, 0x09),  # Line 58-60: Port 02h, pattern 00001001b
        (0x00, 0x90),  # Line 62-65: Port 00h, pattern 10010000b
        (0x00, 0x03),  # Line 67-70: Port 00h, pattern 00000011b
        (0x00, 0x06),  # Line 72-74: Port 00h, pattern 00000110b
        (0x00, 0x0C),  # Line 76-78: Port 00h, pattern 00001100b
        (0x00, 0x09),  # Line 80-82: Port 00h, pattern 00001001b
    ]
    
    # Execute CODO sequence multiple times based on angle
    for step in range(steps_codo):
        port, pattern = codo_sequence[step % len(codo_sequence)]
        machine_code.extend([0xBA, port, 0x00])  # MOV DX, port
        machine_code.extend([0xB0, pattern])     # MOV AL, pattern
        machine_code.extend([0xEE])              # OUT DX, AL
        add_delay_call(machine_code, codo_velocity)
    
    print(f"✅ All 3 motors controlled: Base({steps_base} steps), Hombro(2 steps), Codo({steps_codo} steps)")
    
    # Loop control (exactly like robot.asm lines 84-86)
    machine_code.extend([0x4E])                      # DEC SI
    machine_code.extend([0x74, 0x03])                # JZ SALIR_CICLO1 (+3)
    jmp_offset = loop_start - (len(machine_code) + 3)
    machine_code.extend([0xE9, jmp_offset & 0xFF, (jmp_offset >> 8) & 0xFF])  # JMP CICLO1
    
    # Infinite loop at end (exactly like robot.asm lines 90-91: FIN: JMP FIN)
    machine_code.extend([0xEB, 0xFE])                # JMP $ (infinite loop)
    
    # Write .COM file
    tasm_dir = os.path.join("DOSBox2", "Tasm")
    os.makedirs(tasm_dir, exist_ok=True)
    
    com_path = os.path.join(tasm_dir, "motor_user.com")
    with open(com_path, 'wb') as f:
        f.write(bytes(machine_code))
    
    print(f"✅ EXACT robot.asm sequence .COM created: {len(machine_code)} bytes")
    print("🎯 Follows EXACT working robot.asm structure with Robot syntax velocities!")
    print("📍 Location: DOSBox2/Tasm/motor_user.com")
    
    return True

def extract_robot_values(analyzer):
    """Extract values from Robot code using BOTH parser and raw_code"""
    values = {
        'base': 45, 'hombro': 90, 'codo': 60,
        'velocidades': [2, 3, 4],
        'repetitions': 2
    }
    
    try:
        # Method 1: Extract from parser assignments (preferred)
        if hasattr(analyzer, 'parser') and analyzer.parser and hasattr(analyzer.parser, 'assignments'):
            velocidades = []
            for assignment in analyzer.parser.assignments:
                component = assignment.get('component', '').lower()
                value = assignment.get('value', 0)
                
                if component in ['base', 'hombro', 'codo']:
                    values[component] = int(float(value))
                    print(f"✅ Parser: {component} = {value}°")
                elif component == 'velocidad':
                    velocidades.append(float(value))
                    print(f"✅ Parser: velocidad = {value}")
                elif component == 'repetir':
                    values['repetitions'] = int(float(value))
            
            if velocidades:
                values['velocidades'] = velocidades[:3]
        
        # Method 2: Extract from raw code as backup
        raw_code = getattr(analyzer, 'raw_code', '') or getattr(analyzer, 'code', '')
        if raw_code and not hasattr(analyzer, 'parser'):
            velocidades = []
            lines = raw_code.split('\n')
            
            for line in lines:
                line = line.strip()
                if '.base' in line and '=' in line:
                    values['base'] = int(float(line.split('=')[1].strip()))
                elif '.hombro' in line and '=' in line:
                    values['hombro'] = int(float(line.split('=')[1].strip()))
                elif '.codo' in line and '=' in line:
                    values['codo'] = int(float(line.split('=')[1].strip()))
                elif '.velocidad' in line and '=' in line:
                    velocidades.append(float(line.split('=')[1].strip()))
                elif '.repetir' in line and '=' in line:
                    values['repetitions'] = int(float(line.split('=')[1].strip()))
            
            if velocidades:
                values['velocidades'] = velocidades[:3]
        
        print(f"📝 Final extracted: {values}")
                
    except Exception as e:
        print(f"⚠️ Using defaults due to: {e}")
    
    return values

def get_default_values():
    """Default test values"""
    return {
        'base': 45, 'hombro': 120, 'codo': 90,
        'velocidades': [4, 7, 9],
        'repetitions': 2
    }

def get_delay_function(velocity):
    """Map velocity to robot.asm delay function"""
    if velocity >= 9:
        return "DELAY2"  # Fastest (CX = 0FFFh)
    elif velocity >= 7:
        return "DELAY3"  # Fast (CX = 0FFFh)  
    elif velocity >= 5:
        return "DELAY4"  # Slow (CX = 0FFFFh)
    else:
        return "DELAY5"  # Slowest (CX = 0FFFFh)

def add_delay_call(machine_code, delay_function):
    """Add delay based on robot.asm DELAY functions"""
    # Exact delay cycles from robot.asm
    if delay_function == "DELAY2":
        delay_cycles = 0x0FFF    # robot.asm line 100
    elif delay_function == "DELAY3":
        delay_cycles = 0x0FFF    # robot.asm line 106
    elif delay_function == "DELAY4":
        delay_cycles = 0xFFFF    # robot.asm line 112
    elif delay_function == "DELAY5":
        delay_cycles = 0xFFFF    # robot.asm line 118
    else:
        delay_cycles = 0x0FFF    # Default to DELAY2
    
    # Inline delay loop (exactly like robot.asm DELAY functions)
    machine_code.extend([0xB9, delay_cycles & 0xFF, (delay_cycles >> 8) & 0xFF])  # MOV CX, delay_cycles
    machine_code.extend([0xE2, 0xFE])  # LOOP $-2 (LOOP instruction)

# Compatibility function  
def create_dynamic_com_from_analyzer_fixed(analyzer):
    """Main function for main.py compatibility"""
    try:
        return create_working_robot_com(analyzer)
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

if __name__ == "__main__":
    # Test
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
r1.fin"""
            # Also add parser simulation
            self.parser = type('obj', (object,), {
                'assignments': [
                    {'component': 'velocidad', 'value': 4},
                    {'component': 'base', 'value': 45},
                    {'component': 'velocidad', 'value': 7}, 
                    {'component': 'hombro', 'value': 120},
                    {'component': 'velocidad', 'value': 9},
                    {'component': 'codo', 'value': 90}
                ]
            })()
    
    print("🧪 Testing WORKING robot.asm based system...")
    mock = MockAnalyzer()
    create_working_robot_com(mock)