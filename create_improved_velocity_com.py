#!/usr/bin/env python3
"""
IMPROVED Velocity Control for .COM files
- Higher numbers = FASTER movement (more intuitive)
- Simpler delays that work better in Proteus
- More visible speed differences
- Better stepper motor control
"""

import os
import time

def create_improved_velocity_com(analyzer):
    """
    Creates motor_user.com with IMPROVED velocity control
    """
    try:
        # Create directory if doesn't exist
        tasm_dir = os.path.join("DOSBox2", "Tasm")
        os.makedirs(tasm_dir, exist_ok=True)
        
        # Extract motor sequence from Robot code
        motor_values = extract_motor_sequence_improved(analyzer)
        print(f"🎯 IMPROVED Velocity System - Sequence extracted:")
        
        # Show detected sequence with NEW velocity logic
        for i, mov in enumerate(motor_values.get('movements', [])):
            if mov['type'] == 'velocity':
                print(f"• {i+1}. VELOCITY: {mov['value']} (Speed Level: {get_speed_description(mov['value'])})")
            else:
                print(f"• {i+1}. {mov['type'].upper()}: {mov['value']}°")
        
        # Generate IMPROVED machine code
        machine_code = generate_improved_velocity_code(motor_values)
        
        # Write .COM file
        com_path = os.path.join(tasm_dir, "motor_user.com")
        with open(com_path, 'wb') as f:
            f.write(bytes(machine_code))
        
        file_size = len(machine_code)
        print(f"\n✅ IMPROVED motor_user.com created! Size: {file_size} bytes")
        print("🚀 NEW Velocity System:")
        print("• HIGHER numbers = FASTER movement")
        print("• LOWER numbers = SLOWER movement")
        print("• More visible speed differences in Proteus")
        
        return True, motor_values
        
    except Exception as e:
        print(f"❌ Error creating improved velocity .COM: {e}")
        return False, {}

def extract_motor_sequence_improved(analyzer):
    """
    Extracts complete motor sequence maintaining order
    """
    motor_values = {
        'movements': [],
        'repetitions': 1
    }
    
    try:
        # Try to get raw code from analyzer
        raw_code = getattr(analyzer, 'raw_code', '') or getattr(analyzer, 'code', '')
        
        if raw_code:
            print("🔍 Parsing Robot syntax with IMPROVED velocity logic...")
            motor_values = parse_robot_syntax_improved(raw_code)
        else:
            # Fallback to default sequence
            print("🔍 Using default sequence...")
            motor_values = get_default_sequence()
        
        print(f"✅ Sequence extracted: {len(motor_values.get('movements', []))} commands")
        return motor_values
        
    except Exception as e:
        print(f"Error extracting values: {e}")
        return get_default_sequence()

def parse_robot_syntax_improved(code):
    """
    Parse Robot syntax with improved velocity handling
    """
    movements = []
    repetitions = 1
    
    lines = code.strip().split('\n')
    
    for line in lines:
        line = line.strip()
        if not line or line.startswith('#') or line.startswith('Robot') or line.endswith('.inicio') or line.endswith('.fin'):
            continue
            
        # Parse velocity settings
        if '.velocidad' in line and '=' in line:
            try:
                value = float(line.split('=')[1].strip())
                movements.append({'type': 'velocity', 'value': value})
                print(f"  ✓ Velocity: {value} → {get_speed_description(value)}")
            except ValueError:
                pass
                
        # Parse motor positions
        elif '.base' in line and '=' in line:
            try:
                value = int(line.split('=')[1].strip())
                movements.append({'type': 'base', 'value': value})
                print(f"  ✓ Base: {value}°")
            except ValueError:
                pass
                
        elif '.hombro' in line and '=' in line:
            try:
                value = int(line.split('=')[1].strip())
                movements.append({'type': 'hombro', 'value': value})
                print(f"  ✓ Hombro: {value}°")
            except ValueError:
                pass
                
        elif '.codo' in line and '=' in line:
            try:
                value = int(line.split('=')[1].strip())
                movements.append({'type': 'codo', 'value': value})
                print(f"  ✓ Codo: {value}°")
            except ValueError:
                pass
                
        elif '.repetir' in line and '=' in line:
            try:
                repetitions = int(line.split('=')[1].strip())
                print(f"  ✓ Repetitions: {repetitions}")
            except ValueError:
                pass
    
    return {
        'movements': movements,
        'repetitions': repetitions
    }

def get_speed_description(velocity_value):
    """
    Get human-readable speed description
    """
    if velocity_value <= 1:
        return "VERY SLOW"
    elif velocity_value <= 2:
        return "SLOW"
    elif velocity_value <= 5:
        return "NORMAL"
    elif velocity_value <= 8:
        return "FAST"
    else:
        return "VERY FAST"

def get_default_sequence():
    """
    Default sequence for testing
    """
    return {
        'movements': [
            {'type': 'velocity', 'value': 3.0},
            {'type': 'base', 'value': 45},
            {'type': 'velocity', 'value': 5.0}, 
            {'type': 'hombro', 'value': 120},
            {'type': 'velocity', 'value': 8.0},
            {'type': 'codo', 'value': 90},
            {'type': 'velocity', 'value': 10.0},
            {'type': 'base', 'value': 0},
            {'type': 'hombro', 'value': 0},
            {'type': 'codo', 'value': 0}
        ],
        'repetitions': 1
    }

def generate_improved_velocity_code(motor_values=None):
    """
    Generate machine code with IMPROVED velocity control
    Higher numbers = FASTER movement
    """
    machine_code = []

    repetitions = motor_values.get('repetitions', 1)
    if repetitions < 1:
        repetitions = 1

    movements = motor_values.get('movements', [])
    
    # IMPROVED delay calculation - simpler and more effective for Proteus
    def calculate_delay_cycles(velocity_level):
        """
        Convert velocity level to delay cycles
        Higher velocity = Lower delay = Faster movement
        """
        if velocity_level <= 0:
            velocity_level = 1
        
        # Base delay: 65535 cycles (slowest)
        # Higher velocity divides this number = shorter delay = faster
        base_delay = 65535
        delay_cycles = max(100, int(base_delay / velocity_level))
        
        print(f"    Velocity {velocity_level} → Delay: {delay_cycles} cycles")
        return min(65535, delay_cycles)

    def add_improved_delay(velocity_level):
        """Add delay based on velocity level"""
        delay_cycles = calculate_delay_cycles(velocity_level)
        
        # MOV CX, delay_cycles
        machine_code.extend([0xB9, delay_cycles & 0xFF, (delay_cycles >> 8) & 0xFF])
        
        # Simple delay loop: LOOP instruction
        machine_code.extend([0xE2, 0xFE])  # LOOP $-2 (decrements CX and jumps if CX != 0)

    # Stepper motor step patterns (more steps for smoother movement)
    step_patterns = {
        'forward': [0x09, 0x0C, 0x06, 0x03, 0x09, 0x0C, 0x06, 0x03],  # 8 steps for smoother motion
        'backward': [0x03, 0x06, 0x0C, 0x09, 0x03, 0x06, 0x0C, 0x09]
    }

    def generate_motor_movement_improved(port, direction_positive, velocity_level, angle):
        """Generate improved motor movement with velocity control"""
        pattern = step_patterns['forward'] if direction_positive else step_patterns['backward']
        
        # Calculate steps needed based on angle (simplified)
        steps_needed = max(1, int(abs(angle) / 5))  # Roughly 5 degrees per full pattern
        
        print(f"    Motor Port 0x{port:02X}: {angle}° in {steps_needed} patterns at velocity {velocity_level}")
        
        # Set port
        machine_code.extend([0xBA, port, 0x03])  # MOV DX, 03xxh
        
        # Execute patterns
        for pattern_round in range(steps_needed):
            for step in pattern:
                # MOV AL, step
                machine_code.extend([0xB0, step])
                # OUT DX, AL
                machine_code.extend([0xEE])
                
                # Velocity-controlled delay between steps
                add_improved_delay(velocity_level)

    # Initialize 8255 PPI
    machine_code.extend([0xBA, 0x03, 0x03])  # MOV DX, 0303h (control port)
    machine_code.extend([0xB0, 0x80])        # MOV AL, 80h (all ports output)
    machine_code.extend([0xEE])              # OUT DX, AL

    # Initialize all motors to 0
    for port in [0x00, 0x01, 0x02]:
        machine_code.extend([0xBA, port, 0x03])  # MOV DX, 03xxh
        machine_code.extend([0xB0, 0x00])        # MOV AL, 0
        machine_code.extend([0xEE])              # OUT DX, AL

    # Small initial delay
    add_improved_delay(5)

    # Main repetition loop
    machine_code.extend([0xBE, repetitions & 0xFF, (repetitions >> 8) & 0xFF])  # MOV SI, repetitions
    loop_start = len(machine_code)

    # Process movement sequence
    motor_ports = {'base': 0x00, 'hombro': 0x01, 'codo': 0x02}
    current_velocity = 3.0  # Default velocity
    
    print("\n=== GENERATING IMPROVED VELOCITY CODE ===")
    
    for mov in movements:
        mov_type = mov['type']
        value = mov['value']
        
        if mov_type == 'velocity':
            current_velocity = value
            print(f"🚀 Velocity set to: {value} ({get_speed_description(value)})")
            
        elif mov_type in motor_ports:
            port = motor_ports[mov_type]
            direction = value > 0  # Positive angle = forward
            
            print(f"🔧 Moving {mov_type.upper()} to {value}° at velocity {current_velocity}")
            generate_motor_movement_improved(port, direction, current_velocity, value)
            
            # Pause between different motors
            add_improved_delay(current_velocity * 0.5)

    # End of repetition loop
    machine_code.extend([0x4E])                # DEC SI
    machine_code.extend([0x83, 0xFE, 0x00])    # CMP SI, 0
    je_offset_pos = len(machine_code)
    machine_code.extend([0x74, 0x00])          # JE end
    
    # Jump back to loop start
    jmp_offset = loop_start - (len(machine_code) + 3)
    machine_code.extend([0xE9, jmp_offset & 0xFF, (jmp_offset >> 8) & 0xFF])
    
    # Calculate JE offset
    rel_je = len(machine_code) - (je_offset_pos + 2)
    machine_code[je_offset_pos + 1] = rel_je & 0xFF

    # Turn off all motors at end
    for port in [0x00, 0x01, 0x02]:
        machine_code.extend([0xBA, port, 0x03])  # MOV DX, 03xxh  
        machine_code.extend([0xB0, 0x00])        # MOV AL, 0
        machine_code.extend([0xEE])              # OUT DX, AL

    # Exit to DOS
    machine_code.extend([0xB8, 0x00, 0x4C])    # MOV AX, 4C00h
    machine_code.extend([0xCD, 0x21])          # INT 21h

    print(f"\n✅ Improved machine code generated: {len(machine_code)} bytes")
    return machine_code

# Compatibility function for main.py
def create_dynamic_com_from_analyzer_improved(analyzer):
    """
    Main function for creating improved velocity .COM from analyzer
    """
    try:
        success, motor_values = create_improved_velocity_com(analyzer)
        return success
    except Exception as e:
        print(f"❌ Error in create_dynamic_com_from_analyzer_improved: {e}")
        return False

if __name__ == "__main__":
    # Test with default sequence
    class MockAnalyzer:
        def __init__(self):
            self.raw_code = """Robot r1
r1.inicio
r1.velocidad = 2
r1.base = 45
r1.velocidad = 5
r1.hombro = 120
r1.velocidad = 8
r1.codo = 90
r1.base = 0
r1.hombro = 0
r1.codo = 0
r1.fin"""
    
    print("🧪 Testing IMPROVED velocity system...")
    mock = MockAnalyzer()
    create_improved_velocity_com(mock)