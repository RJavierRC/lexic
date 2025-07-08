# Ejemplos Prácticos de Validaciones Semánticas

## Ejemplo 1: Validación A - Declaración Única de Robots

### Código con ERROR (declaración duplicada):
```robot
Robot r1
Robot r1
r1.base = 90
```

### Resultado del análisis:
```
❌ Error semántico en línea 2: Robot 'r1' ya fue declarado previamente en línea 1
```

### Código CORRECTO:
```robot
Robot r1
Robot r2
r1.base = 90
r2.base = 180
```

---

## Ejemplo 2: Validación B - Asignaciones Únicas por Componente
*(Actualmente deshabilitada para permitir secuencias de movimiento)*

### Código que sería ERROR si estuviera habilitada:
```robot
Robot r1
r1.base = 90
r1.base = 180  # Asignación duplicada al mismo componente
```

### Razón para deshabilitar:
En rutinas robóticas es común tener secuencias como:
```robot
Robot r1
r1.inicio
r1.base = 0      # Posición inicial
r1.garra = 0     # Abrir garra
r1.base = 90     # Mover a posición de objeto
r1.garra = 90    # Cerrar garra
r1.base = 180    # Mover a posición de destino
r1.garra = 0     # Abrir garra
r1.fin
```

---

## Ejemplo 3: Validación C - Valores Dentro de Rangos Válidos

### Código con ERRORES (valores fuera de rango):
```robot
Robot r1
r1.base = 400      # ERROR: base solo acepta 0-360°
r1.hombro = -50    # ERROR: hombro solo acepta 0-180°
r1.garra = 100     # ERROR: garra solo acepta 0-90°
r1.espera = 70     # ERROR: espera solo acepta 0.1-60 segundos
```

### Resultado del análisis:
```
❌ Error semántico en línea 2: Valor 400.0 para 'r1.base' fuera del rango válido [0, 360] - gira de 0 a 360°
❌ Error semántico en línea 3: Valor -50.0 para 'r1.hombro' fuera del rango válido [0, 180] - gira de 0 a 180°
❌ Error semántico en línea 4: Valor 100.0 para 'r1.garra' fuera del rango válido [0, 90] - abre y cierra de 0 a 90°
❌ Error semántico en línea 5: Valor 70.0 para 'r1.espera' fuera del rango válido [0.1, 60.0] - tiempo de espera de 0.1 a 60 segundos
```

### Código CORRECTO:
```robot
Robot r1
r1.base = 270     # ✅ Dentro del rango 0-360°
r1.hombro = 45    # ✅ Dentro del rango 0-180°
r1.garra = 30     # ✅ Dentro del rango 0-90°
r1.espera = 2.5   # ✅ Dentro del rango 0.1-60 segundos
```

### Código con ADVERTENCIAS (valores en límites):
```robot
Robot r1
r1.base = 0       # ⚠️ Advertencia: valor en el límite
r1.hombro = 180   # ⚠️ Advertencia: valor en el límite
r1.garra = 90     # ⚠️ Advertencia: valor en el límite
```

---

## Ejemplo 4: Validación D - Robots Correctamente Declarados

### Código con ERROR (robot no declarado):
```robot
r1.base = 90      # ERROR: r1 no fue declarado
r2.hombro = 45    # ERROR: r2 no fue declarado
```

### Resultado del análisis:
```
❌ Error semántico en línea 1: Robot 'r1' usado sin haber sido declarado
❌ Error semántico en línea 2: Robot 'r2' usado sin haber sido declarado
```

### Código CORRECTO:
```robot
Robot r1
Robot r2
r1.base = 90      # ✅ r1 fue declarado
r2.hombro = 45    # ✅ r2 fue declarado
```

---

## Ejemplo Completo: Todas las Validaciones

### Código con MÚLTIPLES ERRORES:
```robot
Robot r1
Robot r1          # ERROR A: Declaración duplicada
r1.base = 400     # ERROR C: Valor fuera de rango
r2.hombro = 45    # ERROR D: Robot no declarado
```

### Resultado del análisis:
```
❌ Error semántico en línea 2: Robot 'r1' ya fue declarado previamente en línea 1
❌ Error semántico en línea 3: Valor 400.0 para 'r1.base' fuera del rango válido [0, 360] - gira de 0 a 360°
❌ Error semántico en línea 4: Robot 'r2' usado sin haber sido declarado
```

### Código COMPLETAMENTE CORRECTO:
```robot
Robot r1
Robot r2
r1.repetir = 3
r1.inicio
    r1.base = 0
    r1.hombro = 90
    r1.codo = 45
    r1.muneca = 180
    r1.garra = 0
    r1.espera = 1.0
    r1.base = 90
    r1.garra = 30
    r1.espera = 0.5
    r1.base = 180
    r1.garra = 0
r1.fin
r2.base = 270
r2.hombro = 135
```

### Resultado del análisis:
```
✅ ANÁLISIS SINTÁCTICO: CORRECTO
✅ ANÁLISIS SEMÁNTICO: CORRECTO
El programa cumple con todas las reglas semánticas:
• Declaración única de robots
• Asignaciones únicas por componente
• Valores dentro de rangos válidos
• Robots correctamente declarados
```

---

## Rangos Válidos por Componente

| Componente | Rango Mínimo | Rango Máximo | Descripción |
|------------|--------------|--------------|-------------|
| base       | 0            | 360          | gira de 0 a 360° |
| hombro     | 0            | 180          | gira de 0 a 180° |
| codo       | 0            | 180          | gira de 0 a 180° |
| garra      | 0            | 90           | abre y cierra de 0 a 90° |
| muneca     | 0            | 360          | gira de 0 a 360° |
| velocidad  | 0.1          | 10.0         | tiempo por movimiento de 0.1 a 10 segundos |
| repetir    | 1            | 100          | número de repeticiones de 1 a 100 |
| espera     | 0.1          | 60.0         | tiempo de espera de 0.1 a 60 segundos |

---

## Casos Especiales

### Comandos de Control (excluidos de validación D):
```robot
Robot r1
r1.inicio     # ✅ No requiere validación de declaración
r1.fin        # ✅ No requiere validación de declaración
```

### Valores Decimales:
```robot
Robot r1
r1.base = 90.5    # ✅ Acepta decimales
r1.espera = 1.75  # ✅ Acepta decimales
```

### Valores en Límites:
```robot
Robot r1
r1.base = 0       # ⚠️ Advertencia: en límite inferior
r1.base = 360     # ⚠️ Advertencia: en límite superior
r1.garra = 45     # ✅ Valor normal dentro del rango
```
