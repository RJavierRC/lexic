# 🪟 Analizador Léxico - Windows Edition

## 🎯 Descripción
Analizador léxico especializado para lenguaje de control de brazo robótico, optimizado específicamente para Windows. Esta versión incluye compilación automática a código ensamblador x86 usando DOSBox y TASM.

## ⚡ Inicio Rápido

### 1. Ejecutar Aplicación
```batch
# Doble click en:
start_windows.bat

# O desde terminal:
python main.py
```

### 2. Usar la Interfaz
1. **Abrir**: Cargar archivo `.robot` de ejemplo
2. **Analizar**: Procesar código robótico
3. **Generar .exe**: Compilar a ejecutable
4. **Guardar**: Exportar resultados

## 🔧 Características Windows

### ✅ Funcionalidades Principales
- ✅ Interfaz gráfica optimizada para Windows
- ✅ Análisis léxico completo
- ✅ Análisis sintáctico avanzado  
- ✅ Validaciones semánticas
- ✅ Generación de código intermedio
- ✅ Compilación automática a .exe
- ✅ Tabla de símbolos
- ✅ Detección de errores mejorada

### 🛠️ Herramientas Integradas
- **DOSBox**: Emulador DOS integrado
- **TASM**: Turbo Assembler para x86
- **TLINK**: Linker para ejecutables
- **Tkinter**: Interfaz gráfica nativa

## 📁 Estructura del Proyecto

```
lexic/
├── 🪟 start_windows.bat          # Inicio Windows
├── 🐍 main.py                    # Aplicación principal  
├── 🔍 robot_lexical_analyzer.py  # Analizador léxico
├── 🎯 robot_tokens.py            # Tokens robóticos
├── ⚙️ assembly_generator.py      # Generador ensamblador
├── 🪟 windows_config.py          # Configuración Windows
├── 📂 DOSBox2/                   # Emulador DOS
│   ├── dosbox.exe               # Ejecutable DOSBox
│   └── Tasm/                    # Turbo Assembler
│       ├── TASM.EXE
│       ├── TLINK.EXE
│       └── *.asm, *.exe         # Archivos generados
└── 📋 test_*.robot              # Archivos de prueba
```

## 🤖 Lenguaje Robótico Soportado

### Componentes
```robot
base, hombro, codo, garra, muneca
```

### Comandos
```robot
girai, giraf, abre, cierra, mueve, espera, home
```

### Sintaxis Básica
```robot
inicio
    base { girai 90 }
    hombro { giraf 45 }
    garra { abre }
    espera 1000
fin
```

### Estructuras de Control
```robot
inicio
    if condicion then
        base { girai 90 }
    else
        base { giraf 90 }
    
    while contador < 5 do
        garra { abre }
        espera 500
        garra { cierra }
    
    secuencia movimiento1
        base { girai 45 }
        hombro { mueve 30 }
    secuencia
fin
```

## 🚀 Ejemplos de Uso

### Ejemplo 1: Movimiento Simple
```robot
// Movimiento básico del brazo
inicio
    home              // Posición inicial
    base { girai 90 }     // Girar base 90°
    hombro { giraf 45 }   // Levantar hombro 45°
    garra { abre }        // Abrir garra
    espera 1000          // Esperar 1 segundo
    garra { cierra }     // Cerrar garra
fin
```

### Ejemplo 2: Con Validaciones
```robot
inicio
    // Validación de límites automática
    base { girai 180 }     // ✅ Válido: dentro de rango
    hombro { giraf 120 }   // ❌ Error: fuera de rango (max 90°)
    
    // Variables automáticas
    var contador = 0
    while contador < 3 do
        garra { abre }
        espera 500
        garra { cierra }
        contador = contador + 1
fin
```

## 🎯 Validaciones Integradas

### Validaciones Léxicas
- ✅ Tokens válidos únicamente
- ✅ Comentarios: `//`, `/* */`, `#`
- ✅ Números enteros y decimales
- ✅ Identificadores válidos

### Validaciones Sintácticas  
- ✅ Estructura `inicio...fin`
- ✅ Llaves balanceadas `{}`
- ✅ Comandos con parámetros correctos
- ✅ Estructuras de control válidas

### Validaciones Semánticas
- ✅ Límites de movimiento por componente
- ✅ Comandos válidos por componente
- ✅ Variables declaradas antes de uso
- ✅ Tipos de datos consistentes
- ✅ Unicidad de declaraciones

## 📊 Tabla de Símbolos

| Componente | Comandos Válidos | Rango de Valores |
|------------|------------------|------------------|
| base       | girai, giraf     | -180° a +180°    |
| hombro     | girai, giraf     | -90° a +90°      |
| codo       | girai, giraf     | -120° a +120°    |
| garra      | abre, cierra     | 0 (cerrada) / 1 (abierta) |
| muneca     | girai, giraf     | -90° a +90°      |

## 🔧 Compilación a Ejecutable

### Proceso Automático
1. **Análisis**: Código → Tokens → AST
2. **Validación**: Semántica + Límites
3. **Código Intermedio**: Generación de cuádruplos
4. **Ensamblador**: Traducción a x86 Assembly
5. **Compilación**: TASM + TLINK → .exe

### Archivos Generados
```
DOSBox2/Tasm/
├── programa.asm     # Código ensamblador
├── programa.obj     # Archivo objeto
├── programa.exe     # ✅ Ejecutable final
└── programa.map     # Mapa de memoria
```

## ⚠️ Requisitos del Sistema

### Windows
- ✅ **SO**: Windows 7/8/10/11
- ✅ **Python**: 3.7 o superior
- ✅ **Memoria**: 512 MB RAM mínimo
- ✅ **Espacio**: 100 MB libres

### Incluido en el Proyecto
- ✅ **DOSBox**: Emulador DOS portable
- ✅ **TASM**: Turbo Assembler 16-bit
- ✅ **TLINK**: Turbo Linker
- ✅ **Ejemplos**: Archivos .robot de prueba

## 🐛 Solución de Problemas

### Error: "DOSBox no encontrado"
```batch
# Verificar que existe:
DOSBox2\dosbox.exe

# Si no existe, descargar DOSBox desde:
# https://www.dosbox.com/
```

### Error: "Python no instalado"
```batch
# Descargar Python desde:
# https://python.org/downloads/

# Verificar instalación:
python --version
```

### Error: "Compilación fallida"
1. Verificar que `DOSBox2/Tasm/` contiene:
   - `TASM.EXE`
   - `TLINK.EXE`
2. Ejecutar como administrador si es necesario
3. Verificar permisos de escritura en la carpeta

## 🎨 Capturas de Pantalla

```
┌─ Analizador Léxico - Windows Edition ────────────────────┐
│                                                          │
│  📂 Abrir    💾 Guardar    🔍 Analizar    🧹 Limpiar     │
│  ⚙️ Generar .exe                                         │
│                                                          │
│  ┌─ Editor de Código ─────────────────────────────────┐  │
│  │ 1  inicio                                          │  │
│  │ 2      base { girai 90 }                           │  │
│  │ 3      garra { abre }                              │  │
│  │ 4      espera 1000                                 │  │
│  │ 5  fin                                             │  │
│  └────────────────────────────────────────────────────┘  │
│                                                          │
│  ┌─ Resultados del Análisis ─────────────────────────┐   │
│  │ ✅ Análisis léxico completado                      │   │
│  │ ✅ Análisis sintáctico válido                      │   │  
│  │ ✅ Validaciones semánticas exitosas                │   │
│  │ ✅ robot_program.exe generado                      │   │
│  └────────────────────────────────────────────────────┘  │
└──────────────────────────────────────────────────────────┘
```

## 📞 Soporte

Para problemas o sugerencias:
1. Verificar la documentación
2. Revisar archivos de ejemplo en `test_*.robot`
3. Consultar logs de error en la interfaz

## 🏷️ Versión
**Windows Edition v5.0** - Optimizada para Windows con compilación automática

---
*Desarrollado para el curso de Compiladores - Optimizado para Windows* 🪟
