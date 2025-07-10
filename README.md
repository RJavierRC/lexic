# Analizador Léxico y Sintáctico para Brazo Robótico

Un analizador léxico y sintáctico especializado para lenguaje de control de brazo robótico, desarrollado en Python con interfaz gráfica usando tkinter.

## 🚀 Inicio Rápido

### Ubuntu/Linux:
```bash
# Método 1: Script de inicio
./start_analyzer.sh

# Método 2: Directo con Python
python3 main.py

# Método 3: Con entorno virtual
source .venv/bin/activate
python main.py
```

### Windows:
```cmd
# Método 1: Script de inicio
start_analyzer.bat

# Método 2: Directo con Python
python main.py

# Método 3: Doble clic en main.py
```

## Características

- **Analizador Léxico Especializado**: Reconoce todos los tokens del lenguaje robótico
- **Analizador Sintáctico**: Valida la gramática específica del lenguaje con retroalimentación paso a paso
- **Validación de Gramática**: Implementa la gramática S → ID ID INSTS con validación completa
- **Detección de Errores**: Errores léxicos y sintácticos con posición exacta

## Nueva Sintaxis Soportada

### Gramática Formal:
```
S → ID ID INSTS
ID → Robot | identificador
INSTS → INST INSTS | ε  
INST → identificador.componente = valor
```

### Sintaxis del Lenguaje:
```robot
Robot r3
r3.base = 120
r3.hombro = 60
r3.codo = 30
r3.garra = 90
```

### Validaciones Implementadas:
1. **Declaración obligatoria**: Debe comenzar con `Robot nombre_robot`
2. **Consistencia de nombres**: Todas las instrucciones deben usar el mismo nombre de robot
3. **Componentes válidos**: Solo acepta: base, hombro, codo, garra, muneca
4. **Sintaxis correcta**: Valida la estructura `robot.componente = valor`
5. **Valores numéricos**: Acepta enteros y decimales (con advertencias para valores > 360°)

## Ejemplos de Uso

### ✅ Código Correcto:
```robot
Robot r3
r3.base = 120
r3.hombro = 60
r3.codo = 30
r3.garra = 90
```
**Resultado**: ✅ ANÁLISIS SINTÁCTICO: CORRECTO

### ❌ Código con Errores:
```robot
Robot r3
r3.base = 120
r2.hombro = 60        // Error: nombre incorrecto
r3.pierna = 30        // Error: componente inválido
r3.garra              // Error: falta = y valor
```
**Resultado**: ❌ ANÁLISIS SINTÁCTICO: ERRORES ENCONTRADOS

## Estructura del Proyecto

```
lexic/
├── main.py                      # Interfaz gráfica principal
├── robot_lexical_analyzer.py    # Analizador léxico y sintáctico
├── robot_tokens.py              # Definición de tokens robóticos
├── test_new_syntax.robot        # Ejemplo de sintaxis correcta
├── test_errors.robot            # Ejemplo con errores para prueba
├── test_robot_code.robot        # Sintaxis antigua (compatibilidad)
└── README.md                    # Este archivo
```

## Requisitos

- Python 3.6 o superior
- tkinter (incluido con Python por defecto)

## Instalación y Ejecución

### Instalar dependencias (si es necesario):
```bash
# En Ubuntu/Debian
sudo apt-get install python3-tk

# En Red Hat/CentOS/Fedora
sudo yum install tkinter
# o
sudo dnf install python3-tkinter
```

### Ejecución:
```bash
# Navegar al directorio del proyecto
cd /home/xavier/lexic

# Ejecutar la aplicación
python main.py
```

## Uso de la Aplicación

1. **Abrir archivo**: Usa el botón "Abrir Archivo" o Ctrl+O para cargar un archivo .robot, .arm, .rb o .txt
2. **Escribir código**: Usa el editor con numeración de líneas para escribir código robótico
3. **Analizar**: Presiona "Analizar" o F5 para procesar el código
4. **Ver resultados**: Los tokens, componentes, comandos y estadísticas aparecerán en el panel derecho
5. **Guardar**: Usa "Guardar" o Ctrl+S para guardar tu trabajo
6. **Limpiar**: Usa "Limpiar" o Ctrl+L para limpiar editor y resultados

## Archivo de Prueba

El proyecto incluye `test_robot_code.robot` que contiene ejemplos de:
- Configuración de componentes del brazo
- Comandos de movimiento básicos y avanzados
- Secuencias de pick and place
- Estructuras de control (if, while)
- Diferentes tipos de comentarios
- Valores numéricos variados
- Funciones de emergencia

## Atajos de Teclado

- **Ctrl+N**: Nuevo archivo
- **Ctrl+O**: Abrir archivo
- **Ctrl+S**: Guardar archivo
- **Ctrl+Shift+S**: Guardar como
- **F5**: Analizar código
- **Ctrl+L**: Limpiar todo

## Tokens Reconocidos

El analizador reconoce los siguientes tipos de tokens:

- **KEYWORD**: Palabras clave del lenguaje robótico
- **IDENTIFIER**: Nombres definidos por el usuario
- **INTEGER_LITERAL**: Números enteros (incluyendo negativos)
- **FLOAT_LITERAL**: Números decimales
- **BOOLEAN_LITERAL**: Valores booleanos (verdadero/falso)
- **COMMENT_SINGLE**: Comentarios de línea (//)
- **COMMENT_MULTI**: Comentarios de bloque (/* */)
- **COMMENT_HASH**: Comentarios con # 
- **Operadores**: Asignación, comparación, aritméticos, lógicos
- **Delimitadores**: Llaves, paréntesis, corchetes, separadores

## Validaciones Especiales

El analizador incluye validaciones específicas para robótica:

1. **Componentes requeridos**: Verifica que se definan componentes básicos
2. **Estructura de bloques**: Valida que cada componente tenga su bloque de definición
3. **Rangos de valores**: Advierte sobre valores angulares > 360 grados
4. **Balanceado de llaves**: Verifica que todas las llaves estén correctamente cerradas

## Salida del Análisis

La aplicación muestra:
1. **Información del lenguaje** y versión
2. **Errores léxicos** (si los hay) con posición exacta
3. **Advertencias** sobre posibles problemas
4. **Lista completa de tokens** con descripción
5. **Componentes robóticos detectados**
6. **Comandos de movimiento utilizados**
7. **Estadísticas detalladas** con distribución de tokens

## Desarrollo

Para modificar o extender el analizador:

1. **Agregar nuevos tokens robóticos**: Modifica `robot_tokens.py`
2. **Cambiar lógica de análisis**: Edita `robot_lexical_analyzer.py`
3. **Modificar interfaz**: Actualiza `main.py`
4. **Agregar componentes**: Añade a `ROBOT_KEYWORDS` en `robot_tokens.py`

## Extensibilidad

El analizador está diseñado para ser fácilmente extensible:
- Agregar nuevos componentes robóticos
- Incluir comandos adicionales de movimiento
- Implementar validaciones más complejas
- Soporte para múltiples brazos robóticos

---

**Nota**: Este analizador está optimizado para lenguajes de control de brazo robótico pero puede ser adaptado para otros tipos de robots modificando los patrones de tokens y palabras clave.
