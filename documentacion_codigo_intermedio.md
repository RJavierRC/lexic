# Generador de Código Intermedio - Cuádruplos para Lenguaje Robótico

## Descripción General

El generador de código intermedio convierte el código fuente del lenguaje robótico en una representación intermedia usando **cuádruplos**. Esta representación facilita la optimización y traducción posterior a código máquina.

## Estructura de Cuádruplos

Cada cuádruplo tiene la siguiente estructura:

| Campo | Descripción |
|-------|-------------|
| **#** | Número secuencial del cuádruplo |
| **OPERACION** | Tipo de operación a realizar |
| **ARG1** | Primer argumento u operando |
| **ARG2** | Segundo argumento u operando |
| **RESULTADO** | Variable o etiqueta resultado |
| **DESCRIPCION** | Descripción legible de la operación |

## Tipos de Operaciones Implementadas

### 1. DECLARAR
**Propósito**: Declaración de robots  
**Formato**: `DECLARAR robot - nombre_robot`  
**Ejemplo**:
```
| 0 | DECLARAR | robot | - | r1 | Declaración del robot r1 |
```

### 2. ASIG
**Propósito**: Asignación de valores a variables  
**Formato**: `ASIG valor - variable`  
**Ejemplo**:
```
| 1 | ASIG | 90 | - | base | base = 90 |
```

### 3. CALL
**Propósito**: Llamadas a funciones/movimientos  
**Formato**: `CALL componente valor robot`  
**Ejemplo**:
```
| 2 | CALL | base | 90 | r1 | Mueve base a 90° |
```

### 4. COMPARAR
**Propósito**: Comparaciones para control de flujo  
**Formato**: `COMPARAR variable valor temporal`  
**Ejemplo**:
```
| 3 | COMPARAR | CX1 | 0 | T1 | Compara si CX1 == 0 |
```

### 5. SALTO_CONDICIONAL
**Propósito**: Saltos condicionales basados en comparaciones  
**Formato**: `SALTO_CONDICIONAL condicion - etiqueta`  
**Ejemplo**:
```
| 4 | SALTO_CONDICIONAL | T1 | - | L2 | Si CX1 == 0 salta al final |
```

### 6. SALTO_INCONDICIONAL
**Propósito**: Saltos incondicionales (loops)  
**Formato**: `SALTO_INCONDICIONAL - - etiqueta`  
**Ejemplo**:
```
| 18 | SALTO_INCONDICIONAL | - | - | L1 | Vuelve al inicio del ciclo |
```

### 7. DECREMENTO
**Propósito**: Operaciones de decremento para contadores  
**Formato**: `DECREMENTO variable - variable`  
**Ejemplo**:
```
| 17 | DECREMENTO | CX1 | - | CX1 | Resta 1 al contador |
```

### 8. DECLARAR_ETIQUETA
**Propósito**: Declaración de etiquetas para saltos  
**Formato**: `DECLARAR_ETIQUETA - - etiqueta`  
**Ejemplo**:
```
| 2 | DECLARAR_ETIQUETA | - | - | L1 | Etiqueta de inicio del ciclo |
```

### 9. FIN
**Propósito**: Marcadores de fin de bloque  
**Formato**: `FIN - - etiqueta`  
**Ejemplo**:
```
| 19 | FIN | - | - | L2 | Fin del ciclo |
```

## Variables y Contadores Temporales

### Variables Temporales (T1, T2, ...)
- Almacenan resultados intermedios de comparaciones
- Se generan automáticamente según se necesiten
- Facilitan el manejo de expresiones complejas

### Contadores de Loop (CX1, CX2, ...)
- Controlan las repeticiones en ciclos
- Cada bloque `repetir` genera su propio contador
- Se decrementan automáticamente en cada iteración

### Etiquetas (L1, L2, ...)
- Marcan puntos de salto en el código
- Facilitan la implementación de estructuras de control
- Se generan en pares (inicio y fin de ciclo)

## Ejemplos Completos

### Ejemplo 1: Código Simple (Sin Repetición)
```robot
Robot r1
r1.base = 90
r1.espera = 1
```

**Cuádruplos generados**:
```
| # | OPERACION | ARG1   | ARG2 | RESULTADO | DESCRIPCION               |
|---|-----------|--------|------|-----------|---------------------------|
| 0 | DECLARAR  | robot  | -    | r1        | Declaración del robot r1  |
| 1 | ASIG      | 90     | -    | base      | base = 90                 |
| 2 | CALL      | base   | 90   | r1        | Mueve base a 90°          |
| 3 | ASIG      | 1.0    | -    | espera    | espera = 1.0              |
| 4 | CALL      | espera | 1.0  | r1        | Espera 1.0 segundos       |
```

### Ejemplo 2: Código con Repetición
```robot
Robot r1
r1.repetir = 3
r1.inicio
r1.base = 45
r1.espera = 1
r1.fin
```

**Cuádruplos generados**:
```
| #  | OPERACION           | ARG1   | ARG2 | RESULTADO | DESCRIPCION                    |
|----|---------------------|--------|------|-----------|--------------------------------|
| 0  | DECLARAR            | robot  | -    | r1        | Declaración del robot r1       |
| 1  | ASIG                | 3      | -    | CX1       | Contador del loop = 3          |
| 2  | DECLARAR_ETIQUETA   | -      | -    | L1        | Etiqueta de inicio del ciclo   |
| 3  | COMPARAR            | CX1    | 0    | T1        | Compara si CX1 == 0            |
| 4  | SALTO_CONDICIONAL   | T1     | -    | L2        | Si CX1 == 0 salta al final     |
| 5  | ASIG                | 45     | -    | base      | base = 45                      |
| 6  | CALL                | base   | 45   | r1        | Mueve base a 45°               |
| 7  | ASIG                | 1.0    | -    | espera    | espera = 1.0                   |
| 8  | CALL                | espera | 1.0  | r1        | Espera 1.0 segundos            |
| 9  | DECREMENTO          | CX1    | -    | CX1       | Resta 1 al contador            |
| 10 | SALTO_INCONDICIONAL | -      | -    | L1        | Vuelve al inicio del ciclo     |
| 11 | FIN                 | -      | -    | L2        | Fin del ciclo                  |
```

## Algoritmo de Generación

### Proceso Principal
1. **Inicialización**: Se resetean todos los contadores
2. **Recorrido**: Se procesa cada símbolo de la tabla de símbolos
3. **Análisis**: Se determina el tipo de operación según el símbolo
4. **Generación**: Se crean los cuádruplos correspondientes
5. **Optimización**: Se manejan casos especiales (loops, etiquetas)

### Manejo de Repeticiones
1. **Detección**: `r1.repetir = N` → Crear contador `CX1`
2. **Inicio**: `r1.inicio` → Crear etiquetas `L1` (inicio) y `L2` (fin)
3. **Comparación**: Verificar si contador llegó a 0
4. **Cuerpo**: Generar cuádruplos para comandos internos
5. **Decremento**: Restar 1 al contador
6. **Salto**: Volver al inicio del ciclo
7. **Fin**: Marcar el final del ciclo

### Manejo de Múltiples Robots
- Cada robot mantiene su propio contexto
- Los cuádruplos especifican claramente qué robot ejecuta cada acción
- Las declaraciones se procesan secuencialmente

## Ventajas del Código Intermedio

1. **Independencia de Máquina**: No está ligado a una arquitectura específica
2. **Optimización**: Facilita la aplicación de optimizaciones
3. **Depuración**: Permite análisis detallado del flujo de ejecución
4. **Portabilidad**: Puede traducirse a diferentes lenguajes objetivo
5. **Comprensión**: Representa el código de forma más lineal y clara

## Implementación Técnica

### Clase `Cuadruplo`
```python
class Cuadruplo:
    def __init__(self, numero, operacion, arg1, arg2, resultado, descripcion):
        self.numero = numero
        self.operacion = operacion
        self.arg1 = arg1 if arg1 is not None else "-"
        self.arg2 = arg2 if arg2 is not None else "-"
        self.resultado = resultado if resultado is not None else "-"
        self.descripcion = descripcion
```

### Clase `IntermediateCodeGenerator`
- **Métodos principales**:
  - `generar_codigo_intermedio()`: Procesa la tabla de símbolos
  - `agregar_cuadruplo()`: Crea nuevos cuádruplos
  - `generar_etiqueta()`: Genera etiquetas únicas
  - `generar_temporal()`: Genera variables temporales
  - `get_formatted_table()`: Formatea la salida

### Integración con el Analizador
- Se ejecuta después del análisis semántico
- Utiliza la tabla de símbolos como entrada
- Se integra en la salida del analizador principal
- Disponible tanto en GUI como en línea de comandos

## Casos de Uso Futuros

1. **Optimización**: Eliminación de código muerto, optimización de loops
2. **Traducción**: Conversión a código de ensamblador específico
3. **Simulación**: Ejecución virtual del programa robótico
4. **Verificación**: Análisis de propiedades temporales y de seguridad
5. **Debugger**: Herramientas de depuración paso a paso
