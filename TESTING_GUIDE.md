# 🧪 Testing Guide for Velocity Improvements

## For Your Colleague - How to Test the New Velocity System

### Step 1: Get the Branch
```bash
# Clone the repository (if they don't have it)
git clone https://github.com/RJavierRC/lexic.git
cd lexic

# OR if they already have it, update and get the new branch
git fetch origin
git checkout velocity-improvements
```

### Step 2: Quick Test
```bash
# Run the test script to verify everything works
python test_improved_velocity.py
```

### Step 3: Test with GUI Application
1. **Run the main application**:
   ```bash
   python main.py
   ```

2. **Create test Robot code**:
   ```robot
   Robot r1
   r1.inicio
   r1.velocidad = 2      # SLOW movement
   r1.base = 45  
   r1.velocidad = 8      # FAST movement       
   r1.hombro = 120
   r1.velocidad = 10     # VERY FAST      
   r1.codo = 90       
   r1.velocidad = 3      # NORMAL speed (return)
   r1.base = 0         
   r1.hombro = 0        
   r1.codo = 0      
   r1.fin
   ```

3. **Generate .COM file**:
   - Click "📁 .COM" button
   - Enter a filename (e.g., `test_velocity`)
   - The system will generate `test_velocity.com`

### Step 4: Test in Proteus
1. **Load the .COM file** in Proteus ISIS
2. **Set up the circuit**:
   - 8086 processor in Real Mode
   - 8255 PPI at addresses 0300h-0303h
   - Connect stepper motors via ULN2003A drivers
3. **Run simulation**
4. **Expected behavior**:
   - Base motor moves SLOWLY to 45°
   - Hombro motor moves FAST to 120° 
   - Codo motor moves VERY FAST to 90°
   - All return at NORMAL speed to 0°

## 🔍 What to Look For

### ✅ SUCCESS Indicators:
- **Clear speed differences** between movements
- **Higher velocity numbers** = visibly faster movement
- **Lower velocity numbers** = visibly slower movement  
- **No "unknown opcode" errors** in Proteus
- **Smooth stepper motor movements**

### ❌ If Issues Occur:
- Check the generated .COM file exists in `DOSBox2/Tasm/`
- Verify 8255 PPI is at correct addresses (0300h-0303h)
- Ensure 8086 is in Real Mode (not Protected Mode)
- Check that stepper motors are connected properly

## 📊 Velocity Scale Reference

| Velocity Value | Speed Level | Visual Effect |
|---------------|-------------|---------------|
| `r1.velocidad = 1` | VERY SLOW | Clearly visible steps |
| `r1.velocidad = 2` | SLOW | Easy to follow |
| `r1.velocidad = 3` | NORMAL | Standard speed |
| `r1.velocidad = 5` | MODERATE | Noticeably faster |
| `r1.velocidad = 8` | FAST | Quick movement |
| `r1.velocidad = 10` | VERY FAST | Rapid movement |

## 🔄 Switching Back to Main Branch
```bash
# To return to the original system
git checkout main

# To go back to testing the improvements
git checkout velocity-improvements
```

## 🐛 Report Issues
If you find any problems:
1. **Screenshot** the Proteus simulation
2. **Share** the Robot code used
3. **Note** what behavior you expected vs. what happened
4. **Check** the console output for error messages

## 📁 Files Changed in This Branch
- `create_improved_velocity_com.py` - New velocity system
- `main.py` - Updated to use improved system  
- `test_improved_velocity.py` - Test script
- `VELOCITY_IMPROVEMENTS.md` - Technical details

---

**The key improvement**: **Higher numbers now mean FASTER movement** (much more intuitive!)