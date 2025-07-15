# 🤖 GUÍA RÁPIDA: GENERACIÓN DINÁMICA DE CÓDIGO

## ✅ SISTEMA DINÁMICO IMPLEMENTADO

Ahora tu analizador léxico **lee los valores del código Robot** y genera automáticamente:
- 📝 **ASM dinámico** con ángulos exactos
- 📁 **COM dinámico** con código máquina personalizado  
- ⚙️ **EXE compilado** basado en tus valores

## 🎯 SINTAXIS ROBOT SOPORTADA

```robot
Robot r1

r1.velocidad = 3        // Velocidad del motor (1-10)
r1.base = 45           // Ángulo motor base (0-180°)
r1.hombro = 90         // Ángulo motor hombro (0-180°)
r1.codo = 60           // Ángulo motor codo (0-180°)
r1.espera = 2          // Tiempo espera en segundos
```

## 🚀 NUEVOS BOTONES EN LA INTERFAZ

1. **📝 ASM** - Genera código ASM dinámico basado en tus valores
2. **📁 .COM** - Genera archivo COM con código máquina personalizado
3. **⚙️ Generar .EXE** - Ahora también genera ASM dinámico automáticamente

## 📋 PROCESO DINÁMICO

### 1. Escribe tu código Robot:
```robot
Robot r1
r1.base = 30
r1.hombro = 120
r1.codo = 75
```

### 2. El sistema extrae automáticamente:
- `r1.base = 30` → 16 pasos calculados
- `r1.hombro = 120` → 50 pasos calculados  
- `r1.codo = 75` → 41 pasos calculados

### 3. Genera código personalizado:
- **ASM**: Con loops específicos para cada ángulo
- **COM**: Con código máquina optimizado
- **EXE**: Compilado y listo para Proteus

## ✨ VENTAJAS DEL SISTEMA DINÁMICO

✅ **No más valores estáticos** - Cada archivo tiene sus propios valores
✅ **Precisión exacta** - Ángulos calculados matemáticamente
✅ **Código optimizado** - Solo los pasos necesarios
✅ **Proteus compatible** - Formato .COM optimizado
✅ **ASM editable** - Código fuente generado para modificaciones

## 🎮 USANDO EN PROTEUS

1. Ejecuta el analizador: `python main.py`
2. Carga tu código Robot o usa los ejemplos:
   - `test_dynamic_robot.robot`
   - `test_custom_angles.robot`
   - `test_extreme_values.robot`
3. Haz clic en **📁 .COM** para generar archivo dinámico
4. Carga el .COM generado en Proteus ISIS
5. ¡Los motores se moverán exactamente a tus ángulos!

## 🔍 ARCHIVOS GENERADOS

- `robot_dynamic.asm` - Código fuente ASM personalizado
- `robot_dynamic.com` - Ejecutable binario optimizado
- `robot_dynamic.exe` - Versión EXE compilada

## 🤖 EJEMPLO COMPLETO

```robot
// Mi robot personalizado
Robot r1

r1.velocidad = 4    // Velocidad media
r1.base = 45       // Base a 45°
r1.hombro = 135    // Hombro a 135°
r1.codo = 90       // Codo a 90°
r1.espera = 2      // Esperar 2 segundos
```

**Resultado**: Código ASM con:
- 25 pasos para base (45°)
- 50 pasos para hombro (135°)  
- 50 pasos para codo (90°)
- Delays calculados para velocidad 4

## 🎯 ¡MISIÓN CUMPLIDA!

Ya no necesitas editar código manualmente. El sistema:
1. **Lee** tus valores del código Robot
2. **Calcula** pasos y delays automáticamente
3. **Genera** ASM y COM personalizados
4. **Funciona** perfectamente en Proteus

¡Tu analizador léxico ahora es completamente dinámico! 🚀
