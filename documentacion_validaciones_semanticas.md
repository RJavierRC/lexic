# Documentación Técnica - Validaciones Semánticas del Analizador Robótico

Este documento explica detalladamente cómo están implementadas las validaciones semánticas A, B, C y D en el código fuente del analizador léxico, sintáctico y semántico para el lenguaje de control de brazo robótico.

## Arquitectura del Analizador Semántico

El análisis semántico se implementa en la clase `SemanticAnalyzer` ubicada en el archivo `robot_lexical_analyzer.py` (líneas 763-870). Esta clase trabaja con la tabla de símbolos generada por el parser sintáctico para validar las reglas semánticas del lenguaje.

### Estructura Principal:

```python
class SemanticAnalyzer:
    def __init__(self):
        self.errors = []
        self.warnings = []
        self.declared_robots = {}  # {nombre_robot: línea_declaración}
        self.robot_assignments = {}  # {nombre_robot: {componente: [líneas_asignación]}}
```

## Validación A: Declaración Única de Robots

### Implementación Técnica:
- **Método**: `_check_declaration_uniqueness(parser)` (líneas 805-817)
- **Estructura de datos**: `robot_declarations = {}` (diccionario local)
- **Algoritmo**: Iteración simple con detección de duplicados

### Código Específico:
```python
def _check_declaration_uniqueness(self, parser):
    """Verifica que no haya declaraciones duplicadas de robots"""
    robot_declarations = {}
    
    for i, simbolo in enumerate(parser.tabla_simbolos):
        if simbolo.es_declaracion:  # Solo símbolos de declaración
            robot_name = simbolo.id
            if robot_name in robot_declarations:
                # Error: declaración duplicada encontrada
                linea_anterior = robot_declarations[robot_name]
                linea_actual = simbolo.linea if simbolo.linea else "desconocida"
                self.errors.append(f"Error semántico en línea {linea_actual}: Robot '{robot_name}' ya fue declarado previamente en línea {linea_anterior}")
            else:
                robot_declarations[robot_name] = simbolo.linea
```

### Funcionamiento:
1. **Recorre la tabla de símbolos** buscando símbolos marcados como `es_declaracion = True`
2. **Mantiene un diccionario** `robot_declarations` que mapea nombre_robot → línea_de_declaración
3. **Detecta duplicados** verificando si el nombre ya existe en el diccionario
4. **Genera error específico** indicando líneas de conflicto

## Validación B: Asignaciones Únicas por Componente

### Implementación Técnica:
- **Método**: `_check_assignment_uniqueness(parser)` (líneas 819-825)
- **Estado actual**: Método implementado pero inactivo (comentado)
- **Razón**: Permitir secuencias de movimiento complejas en rutinas

### Código Específico:
```python
def _check_assignment_uniqueness(self, parser):
    """Verifica que no haya asignaciones duplicadas para el mismo componente (solo fuera de rutinas)"""
    # En el contexto de rutinas robóticas, es válido tener múltiples asignaciones
    # al mismo componente en diferentes momentos de la secuencia.
    # Esta validación se omite para permitir secuencias de movimiento complejas.
    pass
```

### Diseño Conceptual (si se activara):
```python
# Implementación conceptual para validación estricta:
def _check_assignment_uniqueness_strict(self, parser):
    robot_component_assignments = {}  # {robot: {componente: [líneas]}}
    
    for simbolo in parser.tabla_simbolos:
        if not simbolo.es_declaracion and simbolo.metodo not in ['inicio', 'fin']:
            robot = simbolo.id
            component = simbolo.metodo
            line = simbolo.linea
            
            if robot not in robot_component_assignments:
                robot_component_assignments[robot] = {}
            if component not in robot_component_assignments[robot]:
                robot_component_assignments[robot][component] = []
            
            robot_component_assignments[robot][component].append(line)
            
            # Verificar si hay múltiples asignaciones
            if len(robot_component_assignments[robot][component]) > 1:
                self.errors.append(f"Error: Asignación duplicada a '{robot}.{component}'")
```

## Validación C: Valores Dentro de Rangos Válidos

### Implementación Técnica:
- **Método**: `_check_value_ranges(parser)` (líneas 827-849)
- **Estructura de datos**: `COMPONENT_RANGES` (diccionario global, líneas 8-16)
- **Algoritmo**: Validación numérica con rangos predefinidos

### Estructura de Rangos:
```python
COMPONENT_RANGES = {
    'base': {'min': 0, 'max': 360, 'description': 'gira de 0 a 360°'},
    'hombro': {'min': 0, 'max': 180, 'description': 'gira de 0 a 180°'},
    'codo': {'min': 0, 'max': 180, 'description': 'gira de 0 a 180°'},
    'garra': {'min': 0, 'max': 90, 'description': 'abre y cierra de 0 a 90°'},
    'muneca': {'min': 0, 'max': 360, 'description': 'gira de 0 a 360°'},
    'velocidad': {'min': 0.1, 'max': 10.0, 'description': 'tiempo por movimiento de 0.1 a 10 segundos'},
    'repetir': {'min': 1, 'max': 100, 'description': 'número de repeticiones de 1 a 100'},
    'espera': {'min': 0.1, 'max': 60.0, 'description': 'tiempo de espera de 0.1 a 60 segundos'}
}
```

### Código Específico:
```python
def _check_value_ranges(self, parser):
    """Verifica que los valores asignados estén dentro de los rangos válidos"""
    for simbolo in parser.tabla_simbolos:
        if not simbolo.es_declaracion:  # Solo asignaciones, no declaraciones
            component = simbolo.metodo
            value = simbolo.valor
            robot_name = simbolo.id
            linea = simbolo.linea if simbolo.linea else "desconocida"
            
            if component in COMPONENT_RANGES:
                range_info = COMPONENT_RANGES[component]
                min_val = range_info['min']
                max_val = range_info['max']
                
                try:
                    numeric_value = float(value)
                    if numeric_value < min_val or numeric_value > max_val:
                        # Error: valor fuera de rango
                        self.errors.append(f"Error semántico en línea {linea}: Valor {numeric_value} para '{robot_name}.{component}' fuera del rango válido [{min_val}, {max_val}] - {range_info['description']}")
                    elif numeric_value == min_val or numeric_value == max_val:
                        # Advertencia: valor en el límite
                        self.warnings.append(f"Advertencia en línea {linea}: Valor {numeric_value} para '{robot_name}.{component}' está en el límite del rango válido")
                except ValueError:
                    # Error: valor no numérico
                    self.errors.append(f"Error semántico en línea {linea}: Valor '{value}' para '{robot_name}.{component}' no es un número válido")
```

### Funcionamiento:
1. **Itera sobre cada símbolo** de la tabla excluyendo declaraciones
2. **Busca el componente** en `COMPONENT_RANGES`
3. **Convierte el valor** a float para comparación numérica
4. **Valida rangos** generando errores para valores fuera de rango
5. **Genera advertencias** para valores en los límites exactos
6. **Maneja errores** de conversión numérica

## Validación D: Robots Correctamente Declarados

### Implementación Técnica:
- **Método**: `_check_undeclared_robots(parser)` (líneas 851-859)
- **Estructura de datos**: `self.declared_robots` (diccionario de instancia)
- **Algoritmo**: Verificación de existencia antes de uso

### Código Específico:
```python
def _check_undeclared_robots(self, parser):
    """Verifica que todos los robots usados en asignaciones hayan sido declarados"""
    for simbolo in parser.tabla_simbolos:
        # Excluir comandos especiales y símbolos de declaración
        if not simbolo.es_declaracion and simbolo.id not in ['ESP'] and simbolo.metodo not in ['inicio', 'fin']:
            robot_name = simbolo.id
            linea = simbolo.linea if simbolo.linea else "desconocida"
            if robot_name not in self.declared_robots:
                self.errors.append(f"Error semántico en línea {linea}: Robot '{robot_name}' usado sin haber sido declarado")
```

### Método de Apoyo - Registro de Declaraciones:
```python
def _check_robot_declarations(self, parser):
    """Verifica las declaraciones de robots en la tabla de símbolos"""
    for simbolo in parser.tabla_simbolos:
        if simbolo.es_declaracion:
            robot_name = simbolo.id
            if robot_name not in self.declared_robots:
                self.declared_robots[robot_name] = 'declarado'
                self.robot_assignments[robot_name] = {}
```

### Funcionamiento:
1. **Primera pasada**: `_check_robot_declarations()` registra todos los robots declarados
2. **Segunda pasada**: `_check_undeclared_robots()` verifica uso válido
3. **Filtros aplicados**: Excluye declaraciones, comandos especiales ('ESP') y comandos de control ('inicio', 'fin')
4. **Detección de error**: Si un robot se usa sin estar en `self.declared_robots`

## Flujo de Ejecución del Análisis Semántico

### Método Principal: `analyze(parser)` (líneas 774-794)
```python
def analyze(self, parser):
    """Realiza el análisis semántico basado en los resultados del parser sintáctico"""
    self.errors = []
    self.warnings = []
    self.declared_robots = {}
    self.robot_assignments = {}
    
    # 1. Verificar declaraciones de robots y asignaciones
    self._check_robot_declarations(parser)
    
    # 2. Verificar unicidad de declaraciones (Validación A)
    self._check_declaration_uniqueness(parser)
    
    # 3. Verificar unicidad de asignaciones (Validación B)
    self._check_assignment_uniqueness(parser)
    
    # 4. Verificar rangos de valores (Validación C)
    self._check_value_ranges(parser)
    
    # 5. Verificar robots no declarados (Validación D)
    self._check_undeclared_robots(parser)
    
    return len(self.errors) == 0
```

### Orden de Ejecución:
1. **Inicialización** de estructuras de datos
2. **Registro** de declaraciones de robots
3. **Validación A**: Unicidad de declaraciones
4. **Validación B**: Unicidad de asignaciones (actualmente deshabilitada)
5. **Validación C**: Rangos de valores
6. **Validación D**: Robots declarados antes de uso
7. **Retorno** del estado de validez (sin errores = True)

## Integración con el Analizador Principal

### Punto de Invocación (líneas 525-534 en `analyze()`)
```python
# Realizar análisis semántico SIEMPRE que tengamos tabla de símbolos
if self.parser and self.parser.tabla_simbolos:
    self.semantic_analyzer = SemanticAnalyzer()
    self.semantic_valid = self.semantic_analyzer.analyze(self.parser)
    if self.semantic_analyzer.errors:
        self.errors.extend(self.semantic_analyzer.errors)
    if self.semantic_analyzer.warnings:
        self.warnings.extend(self.semantic_analyzer.warnings)
```

### Condiciones para Ejecutar:
- **Parser sintáctico exitoso**: `self.parser` existe
- **Tabla de símbolos disponible**: `self.parser.tabla_simbolos` no está vacía
- **Independiente de errores sintácticos**: Se ejecuta incluso si hay errores sintácticos menores

## Estructura de la Tabla de Símbolos

### Clase `Simbolo` (líneas 17-30)
```python
class Simbolo:
    def __init__(self, id, metodo, parametro, valor, es_declaracion=False, linea=None):
        self.id = id           # Identificador: r1, r2, etc.
        self.metodo = metodo   # base, hombro, codo, garra, etc. o "DECLARACION"
        self.parametro = parametro  # parámetro fijo como 1
        self.valor = valor     # valor numérico asignado o "-" para declaraciones
        self.es_declaracion = es_declaracion  # True si es una declaración de robot
        self.linea = linea     # Número de línea donde aparece el símbolo
```

### Ejemplos de Símbolos:
- **Declaración**: `Simbolo('r1', 'DECLARACION', '-', '-', es_declaracion=True, linea=1)`
- **Asignación**: `Simbolo('r1', 'base', 1, 90, es_declaracion=False, linea=3)`
- **Control**: `Simbolo('r1', 'inicio', '-', '-', es_declaracion=False, linea=5)`

## Manejo de Errores y Advertencias

### Tipos de Mensajes:
- **Errores semánticos**: Violaciones que impiden la ejecución del programa
- **Advertencias**: Situaciones potencialmente problemáticas pero no fatales

### Formato de Mensajes:
```python
# Error típico
f"Error semántico en línea {linea}: Robot '{robot_name}' ya fue declarado previamente en línea {linea_anterior}"

# Advertencia típica  
f"Advertencia en línea {linea}: Valor {numeric_value} para '{robot_name}.{component}' está en el límite del rango válido"
```

## Conclusión

Las validaciones semánticas A, B, C y D están implementadas como métodos específicos dentro de la clase `SemanticAnalyzer`, cada uno responsable de una regla semántica particular:

- **A**: `_check_declaration_uniqueness()` - Evita robots duplicados
- **B**: `_check_assignment_uniqueness()` - Control de asignaciones (deshabilitado)
- **C**: `_check_value_ranges()` - Validación de rangos físicos
- **D**: `_check_undeclared_robots()` - Verificación de declaración previa

El sistema utiliza la tabla de símbolos como fuente de verdad y mantiene estructuras de datos auxiliares para rastrear el estado semántico del programa, proporcionando mensajes de error detallados con información de línea y contexto específico.
