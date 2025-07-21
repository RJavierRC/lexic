#!/usr/bin/env python3
"""
Test script for improved velocity system
"""

from create_improved_velocity_com import create_improved_velocity_com
import os

class TestAnalyzer:
    """Mock analyzer with your exact syntax"""
    def __init__(self):
        self.raw_code = """Robot r1
r1.inicio
r1.velocidad = 0.5
r1.base = 45  
r1.velocidad = 1         
r1.hombro = 120
r1.velocidad = 2       
r1.codo = 90       
r1.base = 0         
r1.hombro = 0        
r1.codo = 0      
r1.fin"""

def main():
    print("🧪 TESTING IMPROVED VELOCITY SYSTEM")
    print("=" * 50)
    
    # Test with your exact syntax
    analyzer = TestAnalyzer()
    
    print("📝 Testing with your Robot code:")
    print(analyzer.raw_code)
    print("=" * 50)
    
    # Create improved .COM file
    success, motor_values = create_improved_velocity_com(analyzer)
    
    if success:
        print("\n✅ SUCCESS! Improved .COM file created")
        print("📁 File location: DOSBox2/Tasm/motor_user.com")
        
        # Check file exists and size
        com_path = os.path.join("DOSBox2", "Tasm", "motor_user.com")
        if os.path.exists(com_path):
            size = os.path.getsize(com_path)
            print(f"📏 File size: {size} bytes")
            
            # Show what changed
            print("\n🚀 NEW VELOCITY BEHAVIOR:")
            print("• r1.velocidad = 0.5 → VERY SLOW (was fast)")
            print("• r1.velocidad = 1   → VERY SLOW (was fast)")  
            print("• r1.velocidad = 2   → SLOW (was slow)")
            print()
            print("🔄 SUGGESTED CHANGES for better visibility:")
            print("Replace your velocidad values with:")
            print("• r1.velocidad = 2   # SLOW")
            print("• r1.velocidad = 5   # NORMAL") 
            print("• r1.velocidad = 10  # FAST")
            print()
            print("🎯 Test in Proteus:")
            print("1. Load motor_user.com")
            print("2. 8086 Real Mode processor") 
            print("3. 8255 PPI at 0300h-0303h")
            print("4. Watch for different motor speeds!")
            
        else:
            print("❌ File not created")
    else:
        print("❌ FAILED to create improved .COM file")

if __name__ == "__main__":
    main()