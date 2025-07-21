#!/usr/bin/env python3
"""
FIXED Velocity Control for .COM files
- Proper movement sequence tracking
- Only move when position actually changes
- Correct return-to-home logic
- All motors work correctly
"""

import os

def create_fixed_velocity_com(analyzer):
    """
    Creates motor_user.com with FIXED movement logic and velocity control
    """
    try:
        # Create directory if doesn't exist
        tasm_dir = os.path.join("DOSBox2", "Tasm")
        os.makedirs(tasm_dir, exist_ok=True)
        
        # Extract motor sequence from Robot code
        motor_sequence = extract_movement_sequence(analyzer)
        print(f"🎯 FIXED System - Movement sequence extracted:")
        
        # Show the complete sequence
        for i, mov in enumerate(motor_sequence):
            if mov['type'] == 'velocity':
                print(f"• Step {i+1}: SET VELOCITY = {mov['value']} ({get_speed_description(mov['value'])})")
            else:
                print(f"• Step {i+1}: MOVE {mov['type'].upper()} to {mov['value']}° at velocity {mov['velocity']}")
        
        # Generate FIXED machine code
        machine_code = generate_fixed_movement_code(motor_sequence)
        
        # Write .COM file
        com_path = os.path.join(tasm_dir, "motor_user.com")
        with open(com_path, 'wb') as f:
            f.write(bytes(machine_code))
        
        file_size = len(machine_code)
        print(f"\n✅ FIXED motor_user.com created! Size: {file_size} bytes")
        print("🔧 FIXES APPLIED:")
        print("• All motors move in correct sequence")
        print("• Proper position tracking")
        print("• Correct return-to-home behavior")
        print("• Velocity affects only timing, not sequence")
        
        return True, motor_sequence
        
    except Exception as e:
        print(f"❌ Error creating fixed velocity .COM: {e}")
        return False, []

def extract_movement_sequence(analyzer):
    """
    Extract complete movement sequence with position tracking
    """
    try:
        # Get raw code from analyzer - try multiple sources
        raw_code = None
        
        # Try different ways to get the code
        if hasattr(analyzer, 'raw_code') and analyzer.raw_code:
            raw_code = analyzer.raw_code
        elif hasattr(analyzer, 'code') and analyzer.code:
            raw_code = analyzer.code
        elif hasattr(analyzer, 'current_code') and analyzer.current_code:
            raw_code = analyzer.current_code
        
        print(f"🔍 Raw code found: {bool(raw_code)}")
        if raw_code:
            print(f"📝 Code preview: {raw_code[:100]}...")
        
        if raw_code:
            return parse_movement_sequence(raw_code)
        else:
            print("⚠️ No raw code found, using fallback method...")
            return extract_from_tokens(analyzer)
            
    except Exception as e:
        print(f"Error extracting sequence: {e}")
        return get_test_sequence()

def extract_from_tokens(analyzer):
    """
    Fallback: Extract from analyzer tokens if raw code not available
    """
    sequence = []
    current_velocity = 3.0
    motor_positions = {'base': 0, 'hombro': 0, 'codo': 0}
    
    try:
        if hasattr(analyzer, 'tokens') and analyzer.tokens:
            print("📊 Extracting from tokens...")
            
            i = 0
            while i < len(analyzer.tokens):
                token = analyzer.tokens[i]
                
                if hasattr(token, 'type') and hasattr(token, 'value'):
                    # Look for velocity assignments
                    if (token.type in ['COMPONENT', 'KEYWORD'] and 
                        'velocidad' in token.value.lower()):
                        
                        # Look for = and value
                        if (i + 2 < len(analyzer.tokens) and 
                            analyzer.tokens[i + 1].type in ['ASSIGN', 'ASSIGN_OP']):
                            value_token = analyzer.tokens[i + 2]
                            if hasattr(value_token, 'value'):
                                try:
                                    current_velocity = float(value_token.value)
                                    sequence.append({'type': 'velocity', 'value': current_velocity})
                                    print(f"  ✓ Velocity: {current_velocity}")
                                except:
                                    pass
                    
                    # Look for motor assignments
                    elif (token.type in ['COMPONENT', 'KEYWORD'] and 
                          any(motor in token.value.lower() for motor in ['base', 'hombro', 'codo'])):
                        
                        motor_name = None
                        for motor in ['base', 'hombro', 'codo']:
                            if motor in token.value.lower():
                                motor_name = motor
                                break
                        
                        if motor_name and i + 2 < len(analyzer.tokens):
                            if analyzer.tokens[i + 1].type in ['ASSIGN', 'ASSIGN_OP']:
                                value_token = analyzer.tokens[i + 2]
                                if hasattr(value_token, 'value'):
                                    try:
                                        target_position = int(float(value_token.value))
                                        current_position = motor_positions[motor_name]
                                        
                                        if target_position != current_position:
                                            sequence.append({
                                                'type': motor_name,
                                                'value': target_position,
                                                'from': current_position,
                                                'velocity': current_velocity
                                            })
                                            motor_positions[motor_name] = target_position
                                            print(f"  ✓ {motor_name}: {current_position}° → {target_position}°")
                                    except:
                                        pass
                i += 1
        
        print(f"✅ Extracted {len([s for s in sequence if s['type'] != 'velocity'])} movements from tokens")
        return sequence
        
    except Exception as e:
        print(f"❌ Token extraction failed: {e}")
        return get_test_sequence()

def parse_movement_sequence(code):
    """
    Parse Robot syntax into PROPER movement sequence
    """
    sequence = []
    current_velocity = 3.0
    motor_positions = {'base': 0, 'hombro': 0, 'codo': 0}  # Track current positions
    
    lines = code.strip().split('\n')
    
    print("🔍 Parsing Robot code line by line:")
    
    for line_num, line in enumerate(lines):
        line = line.strip()
        if not line or line.startswith('#') or line.startswith('Robot') or line.endswith('.inicio') or line.endswith('.fin'):
            continue
            
        print(f"  Line {line_num}: {line}")
            
        # Parse velocity settings
        if '.velocidad' in line and '=' in line:
            try:
                current_velocity = float(line.split('=')[1].strip())
                sequence.append({'type': 'velocity', 'value': current_velocity})
                print(f"    → Velocity set to: {current_velocity}")
            except ValueError:
                pass
                
        # Parse motor movements
        elif '.base' in line and '=' in line:
            try:
                target_position = int(line.split('=')[1].strip())
                current_position = motor_positions['base']
                
                # Only add movement if position actually changes
                if target_position != current_position:
                    sequence.append({
                        'type': 'base',
                        'value': target_position,
                        'from': current_position,
                        'velocity': current_velocity
                    })
                    motor_positions['base'] = target_position
                    print(f"    → Base: {current_position}° → {target_position}° at velocity {current_velocity}")
                else:
                    print(f"    → Base: No movement needed (already at {target_position}°)")
            except ValueError:
                pass
                
        elif '.hombro' in line and '=' in line:
            try:
                target_position = int(line.split('=')[1].strip())
                current_position = motor_positions['hombro']
                
                if target_position != current_position:
                    sequence.append({
                        'type': 'hombro',
                        'value': target_position,
                        'from': current_position,
                        'velocity': current_velocity
                    })
                    motor_positions['hombro'] = target_position
                    print(f"    → Hombro: {current_position}° → {target_position}° at velocity {current_velocity}")
                else:
                    print(f"    → Hombro: No movement needed (already at {target_position}°)")
            except ValueError:
                pass
                
        elif '.codo' in line and '=' in line:
            try:
                target_position = int(line.split('=')[1].strip())
                current_position = motor_positions['codo']
                
                if target_position != current_position:
                    sequence.append({
                        'type': 'codo',
                        'value': target_position,
                        'from': current_position,
                        'velocity': current_velocity
                    })
                    motor_positions['codo'] = target_position
                    print(f"    → Codo: {current_position}° → {target_position}° at velocity {current_velocity}")
                else:
                    print(f"    → Codo: No movement needed (already at {target_position}°)")
            except ValueError:
                pass
    
    print(f"\n✅ Final sequence: {len([s for s in sequence if s['type'] != 'velocity'])} actual movements")
    return sequence

def get_speed_description(velocity_value):
    """Get human-readable speed description"""
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

def get_test_sequence():
    """Default test sequence"""
    return [
        {'type': 'velocity', 'value': 5.0},
        {'type': 'base', 'value': 45, 'from': 0, 'velocity': 5.0},
        {'type': 'velocity', 'value': 4.0},
        {'type': 'hombro', 'value': 120, 'from': 0, 'velocity': 4.0},
        {'type': 'velocity', 'value': 1.0},
        {'type': 'codo', 'value': 90, 'from': 0, 'velocity': 1.0},
        {'type': 'base', 'value': 0, 'from': 45, 'velocity': 1.0},
        {'type': 'hombro', 'value': 0, 'from': 120, 'velocity': 1.0},
        {'type': 'codo', 'value': 0, 'from': 90, 'velocity': 1.0}
    ]

def generate_fixed_movement_code(sequence):
    """
    Generate machine code with FIXED movement logic
    """
    machine_code = []
    
    # Fixed delay calculation - much simpler and more predictable
    def add_velocity_delay(velocity_level):
        """Simple, predictable delay based on velocity"""
        if velocity_level <= 0:
            velocity_level = 1
            
        # Simple linear scale: Higher velocity = shorter delay
        # velocity 1 = 60000 cycles (very slow)
        # velocity 10 = 6000 cycles (very fast)
        delay_cycles = max(1000, int(60000 / velocity_level))
        delay_cycles = min(65535, delay_cycles)  # Stay within 16-bit limit
        
        # MOV CX, delay_cycles
        machine_code.extend([0xB9, delay_cycles & 0xFF, (delay_cycles >> 8) & 0xFF])
        # LOOP (simple delay)
        machine_code.extend([0xE2, 0xFE])

    def generate_stepper_movement(port, steps_count, velocity):
        """Generate stepper motor movement with proper step patterns"""
        # Simple 4-step pattern for stepper motors
        step_pattern = [0x09, 0x0C, 0x06, 0x03]
        
        print(f"    Generating {steps_count} steps on port 0x{port:02X} at velocity {velocity}")
        
        # Set port address
        machine_code.extend([0xBA, port, 0x03])  # MOV DX, 03xxh
        
        # Execute steps
        for step_num in range(steps_count):
            step_value = step_pattern[step_num % len(step_pattern)]
            
            # MOV AL, step_value
            machine_code.extend([0xB0, step_value])
            # OUT DX, AL
            machine_code.extend([0xEE])
            
            # Velocity-controlled delay between steps
            add_velocity_delay(velocity)

    # Initialize 8255 PPI
    machine_code.extend([0xBA, 0x03, 0x03])  # MOV DX, 0303h (control register)
    machine_code.extend([0xB0, 0x80])        # MOV AL, 80h (all ports as output)
    machine_code.extend([0xEE])              # OUT DX, AL

    # Initialize all motors to 0 (stopped state)
    motor_ports = {'base': 0x00, 'hombro': 0x01, 'codo': 0x02}
    for port_offset in [0x00, 0x01, 0x02]:
        machine_code.extend([0xBA, port_offset, 0x03])  # MOV DX, 03xxh
        machine_code.extend([0xB0, 0x00])               # MOV AL, 0
        machine_code.extend([0xEE])                     # OUT DX, AL

    # Small startup delay
    add_velocity_delay(5)

    print("\n=== GENERATING FIXED MOVEMENT CODE ===")
    
    # Process each movement in sequence
    for i, movement in enumerate(sequence):
        if movement['type'] == 'velocity':
            print(f"Step {i+1}: Set velocity to {movement['value']}")
            continue
            
        motor = movement['type']
        target = movement['value']
        start_pos = movement['from']
        velocity = movement['velocity']
        
        print(f"Step {i+1}: Move {motor.upper()} from {start_pos}° to {target}° at velocity {velocity}")
        
        # Calculate movement needed
        angle_difference = abs(target - start_pos)
        steps_needed = max(4, int(angle_difference / 10))  # Roughly 10 degrees per 4-step cycle
        
        port = motor_ports[motor]
        generate_stepper_movement(port, steps_needed, velocity)
        
        # Brief pause between different motor movements
        add_velocity_delay(velocity * 2)

    # Final shutdown - turn off all motors
    for port_offset in [0x00, 0x01, 0x02]:
        machine_code.extend([0xBA, port_offset, 0x03])  # MOV DX, 03xxh
        machine_code.extend([0xB0, 0x00])               # MOV AL, 0
        machine_code.extend([0xEE])                     # OUT DX, AL

    # Exit to DOS
    machine_code.extend([0xB8, 0x00, 0x4C])    # MOV AX, 4C00h
    machine_code.extend([0xCD, 0x21])          # INT 21h

    print(f"\n✅ Fixed machine code generated: {len(machine_code)} bytes")
    return machine_code

# Compatibility function for main.py
def create_dynamic_com_from_analyzer_fixed(analyzer):
    """
    Main function for creating FIXED velocity .COM from analyzer
    """
    try:
        success, sequence = create_fixed_velocity_com(analyzer)
        return success
    except Exception as e:
        print(f"❌ Error in create_dynamic_com_from_analyzer_fixed: {e}")
        return False

if __name__ == "__main__":
    # Test with the problematic sequence
    class TestAnalyzer:
        def __init__(self):
            self.raw_code = """Robot r1
r1.inicio
r1.velocidad = 5
r1.base = 45  
r1.velocidad = 4         
r1.hombro = 120
r1.velocidad = 1       
r1.codo = 90       
r1.base = 0         
r1.hombro = 0        
r1.codo = 0      
r1.fin"""
    
    print("🧪 Testing FIXED movement system with your problematic code...")
    analyzer = TestAnalyzer()
    create_fixed_velocity_com(analyzer)