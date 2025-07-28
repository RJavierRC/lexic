# 🤖 Integración RoboDK - Generador de Archivos .mod

## Nueva Funcionalidad: Compilador Robot → RoboDK

Esta branch (`feature/robodk-mod-generator`) añade la capacidad de generar archivos `.mod` compatibles con RoboDK directamente desde tu sintaxis robótica.

## 🚀 ¿Qué es Nuevo?

### ✨ Generador de Archivos .mod
- **Convierte tu sintaxis Robot** → **Archivos RAPID para RoboDK**
- **Botón nuevo en la interfaz:** `🤖 .MOD` (también tecla F9)
- **Compatibilidad total** con RoboDK y robots ABB
- **Procedimientos dinámicos** basados en los valores de tu código

### 🎯 Flujo de Trabajo
```
Código Robot (.robot) → Analizador → Generador .mod → RoboDK → Simulación
```

## 📋 Instalación y Prueba

### 1. Cambiar a la nueva branch:
```bash
git checkout feature/robodk-mod-generator
```

### 2. Ejecutar el programa:
```bash
python main.py
```

### 3. Probar la funcionalidad:
1. Abrir el archivo `ejemplo_robodk.robot` (incluido)
2. Hacer clic en el botón `🤖 .MOD` o presionar F9
3. Dar nombre al archivo (ej: `mi_robot.mod`)
4. ¡Listo! El archivo se genera automáticamente

## 🤖 Ejemplo de Uso

### Código Robot de Entrada:
```robot
Robot brazo_industrial
brazo_industrial.base = 90
brazo_industrial.hombro = 45
brazo_industrial.codo = 60
brazo_industrial.muneca = 30
brazo_industrial.garra = 15
brazo_industrial.velocidad = rapida
```

### Archivo .mod Generado:
```rapid
%%%
  VERSION:1
  LANGUAGE:ENGLISH
%%%
MODULE MOD_BRAZO_INDUSTRIALProgram

    ! Tool variables: 
    PERS tooldata RobotiQ2F85Gripper(FullyClosed) := [TRUE,[[0.000,0.000,130.000],[1.00000000,0.00000000,0.00000000,0.00000000]],[1,[0,0,20],[1,0,0,0],0,0,0.005]];

    ! Reference variables:
    PERS wobjdata Frame2 := [FALSE, TRUE, "", [[0,0,0],[1,0,0,0]],[[-140.437,-738.971,5.234],[1.00000000,0.00000000,0.00000000,0.00000000]]];

    PROC base()
        ConfJ \On;
        ConfL \Off;
        MoveAbsJ [[0.000000,0.000000,0.000000,0.000000,0.000000,-0.000000],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v500,z1,RobotiQ2F85Gripper(FullyClosed) \WObj:=Frame2;
        MoveAbsJ [[90.000000,0.000000,0.000000,0.000000,0.000000,-0.000000],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v500,z1,RobotiQ2F85Gripper(FullyClosed) \WObj:=Frame2;
        MoveAbsJ [[-90.000000,0.000000,0.000000,0.000000,0.000000,-0.000000],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v500,z1,RobotiQ2F85Gripper(FullyClosed) \WObj:=Frame2;
        MoveAbsJ [[0.000000,0.000000,0.000000,0.000000,0.000000,-0.000000],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v500,z1,RobotiQ2F85Gripper(FullyClosed) \WObj:=Frame2;
    ENDPROC

    PROC hombro()
        ConfJ \On;
        ConfL \Off;
        MoveAbsJ [[0.000000,0.000000,0.000000,0.000000,0.000000,-0.000000],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v500,z1,RobotiQ2F85Gripper(FullyClosed) \WObj:=Frame2;
        MoveAbsJ [[0.000000,45.000000,0.000000,0.000000,0.000000,-0.000000],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v500,z1,RobotiQ2F85Gripper(FullyClosed) \WObj:=Frame2;
        MoveAbsJ [[0.000000,-45.000000,0.000000,0.000000,0.000000,-0.000000],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v500,z1,RobotiQ2F85Gripper(FullyClosed) \WObj:=Frame2;
        MoveAbsJ [[0.000000,0.000000,0.000000,0.000000,0.000000,-0.000000],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]],v500,z1,RobotiQ2F85Gripper(FullyClosed) \WObj:=Frame2;
    ENDPROC

    PROC Main()
        ConfJ \On;
        ConfL \Off;
        ! Program generated from Robot syntax on 25/07/2025 15:30:45
        ! Robot: brazo_industrial
        ! Extracted values: base=90°, hombro=45°, codo=60°, muneca=30°, garra=15°
        
        base;
        hombro;
        codo;
        muneca;
        garra;
    ENDPROC

ENDMODULE
```

## 📂 Archivos Nuevos

### `robodk_mod_generator.py`
- **Clase:** `RoboDKModGenerator`
- **Función principal:** Convierte sintaxis Robot a formato RAPID
- **Características:**
  - Análisis automático de valores de motores
  - Generación de procedimientos dinámicos
  - Mapeo de velocidades (rapida→v500, lenta→v50)
  - Compatible con robot ABB IRB140 y Robotiq 2F-85 Gripper

### Modificaciones en `main.py`
- **Nuevo botón:** `🤖 .MOD` en la interfaz
- **Nuevo método:** `generate_mod_file()`
- **Nuevo método:** `show_mod_content()` para vista previa
- **Atajo de teclado:** F9 para generar .mod
- **Menú:** Opción "🤖 Generar .MOD" en menú Análisis

### `ejemplo_robodk.robot`
- Archivo de ejemplo listo para probar
- Incluye todos los componentes soportados
- Sintaxis completa y válida

## 🎮 Uso en RoboDK

### 1. Generar el archivo .mod
1. Escribir código Robot en el editor
2. Presionar `🤖 .MOD` o F9
3. Nombrar el archivo
4. ¡Archivo .mod generado!

### 2. Importar en RoboDK
1. Abrir RoboDK
2. Cargar robot ABB IRB140-6/0.8
3. File → Load → [tu_archivo].mod
4. El programa aparecerá en el árbol de proyecto
5. ¡Ejecutar simulación!

## 🔧 Componentes Soportados

### Articulaciones del Robot:
- **base** → Articulación 1 (θ₁) - Rotación horizontal
- **hombro** → Articulación 2 (θ₂) - Elevación del brazo  
- **codo** → Articulación 3 (θ₃) - Articulación intermedia
- **muneca** → Articulación 4 (θ₄) - Rotación de muñeca
- **garra** → Articulación 5 (θ₅) - Control del gripper

### Velocidades:
- **rapida** → v500 (velocidad alta)
- **lenta** → v50 (velocidad de precisión)
- **Numérico** → v[valor] (personalizado)

## ✅ Funcionalidades Implementadas

- ✅ **Análisis automático** de sintaxis Robot
- ✅ **Generación de procedimientos** por componente
- ✅ **Mapeo de articulaciones** a movimientos RAPID
- ✅ **Control de velocidad** configurable
- ✅ **Interfaz gráfica integrada** (botón + menú + atajo)
- ✅ **Vista previa** del archivo generado
- ✅ **Compatibilidad total** con RoboDK
- ✅ **Herramienta ABB** (Robotiq 2F-85 Gripper)
- ✅ **Referencias de trabajo** (Frame2) configuradas

## 🧪 Testing

### Comandos para probar:

```bash
# 1. Cambiar a la branch
git checkout feature/robodk-mod-generator

# 2. Probar el generador independiente
python robodk_mod_generator.py

# 3. Ejecutar la aplicación completa
python main.py

# 4. Abrir archivo de ejemplo en la interfaz
# Archivo → Abrir → ejemplo_robodk.robot
# Luego: 🤖 .MOD button
```

## 🔄 Workflow Completo

```
1. Escribir código Robot  → Editor de código
2. Analizar sintaxis      → Analizador léxico
3. Generar .mod           → RoboDKModGenerator  
4. Importar en RoboDK     → File → Load
5. Simular movimientos    → RoboDK execution
6. ¡Ver robot moverse!    → Basado en tu código
```

## 📊 Ventajas de esta Integración

### Para el Proyecto:
- **Completa la demostración** de simulador + compilador
- **Interfaz semi-automatizada** como requería el proyecto
- **Validación práctica** de la compilación
- **Diferenciación técnica** del proyecto

### Para el Usuario:
- **Flujo simplificado:** Robot syntax → RoboDK simulación
- **Sin programación RAPID manual**
- **Validación visual** de movimientos
- **Testing de algoritmos** robóticos

## 🎯 Próximos Pasos

Una vez probada esta branch:

1. **Merge a main** si todo funciona correctamente
2. **Actualizar documentación** principal
3. **Añadir a reporte** como funcionalidad completada
4. **Demo completa** para presentación

---

**🤖 ¡La integración Robot → RoboDK está lista para probar!**