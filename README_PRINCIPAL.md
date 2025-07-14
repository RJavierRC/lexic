# 🤖 Analizador Léxico para Brazo Robótico

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![Multiplataforma](https://img.shields.io/badge/Plataforma-macOS%20%7C%20Windows%20%7C%20Linux-green.svg)](https://github.com/)
[![Tkinter](https://img.shields.io/badge/GUI-Tkinter-yellow.svg)](https://docs.python.org/3/library/tkinter.html)

Un analizador léxico, sintáctico y semántico completo diseñado específicamente para el control de brazos robóticos. Incluye generación de código intermedio (cuádruplos) y código ensamblador compatible con TASM.

## 🚀 Inicio Rápido

```bash
# Un comando para cualquier sistema operativo
python3 start_universal.py
```

## 🌍 Compatibilidad Total

| Sistema | Análisis | Código ASM | Compilar .EXE | Estado |
|---------|----------|------------|---------------|--------|
| 🍎 **macOS** | ✅ | ✅ | ❌ | **Funcional** |
| 🪟 **Windows** | ✅ | ✅ | ✅ | **Completo** |
| 🐧 **Linux** | ✅ | ✅ | ✅ | **Completo** |

## ✨ Características Principales

- **🔍 Análisis Multinivel:** Léxico, sintáctico y semántico
- **⚙️ Código Intermedio:** Generación de cuádruplos optimizada
- **🖥️ Interfaz Adaptativa:** Se adapta automáticamente a cada SO
- **🛡️ Validaciones Avanzadas:** Rangos, duplicados, tipos
- **📊 Retroalimentación Detallada:** Errores específicos y útiles
- **🎨 Editor Avanzado:** Números de línea y resaltado
- **🌍 Multiplataforma:** Un código, tres sistemas

## 🎯 Detección Automática

La aplicación detecta tu sistema operativo y configura la interfaz automáticamente:

### 🍎 macOS
- Botón "**Ver ASM**" (amarillo)
- Tema nativo de macOS
- Optimizado para Retina

### 🪟 Windows  
- Botón "**Generar .EXE**" (verde)
- Compilación nativa completa
- Compatible con Proteus

### 🐧 Linux
- Botón "**Compilar**" (verde)
- DOSBox + TASM integrado
- Entorno robusto

## 📝 Sintaxis del Lenguaje

```robot
// Declaración de robot
Robot mi_robot

// Configuración de repeticiones
mi_robot.repetir = 5

// Bloque de comandos
mi_robot.inicio
    mi_robot.velocidad = 2.5
    mi_robot.base = 90
    mi_robot.hombro = 120
    mi_robot.codo = 45
    mi_robot.garra = 30
    mi_robot.espera = 1.0
mi_robot.fin
```

## 🤖 Componentes Robóticos

| Componente | Rango | Descripción |
|------------|-------|-------------|
| `base` | 0-360° | Rotación completa |
| `hombro` | 0-180° | Articulación limitada |
| `codo` | 0-180° | Articulación limitada |
| `garra` | 0-90° | Apertura/cierre |
| `muneca` | 0-360° | Rotación completa |
| `velocidad` | 0.1-10.0 | Velocidad de movimiento |
| `repetir` | 1-100 | Número de repeticiones |
| `espera` | 0.1-60.0 | Tiempo de pausa (segundos) |

## 🔧 Instalación y Uso

### Método 1: Script Universal (Recomendado)
```bash
git clone <repositorio>
cd lexic
python3 start_universal.py
```

### Método 2: Manual
```bash
# Crear entorno virtual
python3 -m venv .venv

# Activar entorno virtual
source .venv/bin/activate  # macOS/Linux
.venv\Scripts\activate.bat  # Windows

# Ejecutar aplicación
python main.py
```

### Método 3: Scripts Específicos
```bash
# macOS
./start_analyzer_macos.sh

# Linux  
./start_analyzer_linux.sh

# Windows
start_analyzer_windows.bat
```

## 📁 Estructura del Proyecto

```
lexic/
├── main.py                     # Interfaz gráfica principal
├── robot_lexical_analyzer.py   # Analizador principal
├── robot_tokens.py            # Definición de tokens
├── assembly_generator.py      # Generador de código ASM
├── start_universal.py         # Script de inicio universal
├── ejemplo_macos.robot        # Ejemplo de código
├── README_macOS.md           # Documentación completa
└── DOSBox2/                  # Herramientas de compilación
    └── Tasm/                 # TASM y utilidades
```

## 📊 Análisis y Validaciones

### Análisis Léxico
- Reconocimiento de tokens específicos para robótica
- Detección de tokens desconocidos
- Manejo de comentarios y espacios en blanco

### Análisis Sintáctico  
- Validación de estructura de bloques
- Verificación de sintaxis correcta
- Detección de errores de gramática

### Análisis Semántico
- Validación de rangos de valores
- Detección de robots no declarados
- Verificación de declaraciones duplicadas
- Validación de tipos de datos

### Código Intermedio
- Generación de cuádruplos optimizada
- Variables temporales automáticas
- Etiquetas y saltos estructurados

## 🎮 Interfaz de Usuario

### Editor
- **Números de línea** automáticos
- **Resaltado** de sintaxis
- **Deshacer/Rehacer** integrado
- **Búsqueda** y reemplazo

### Resultados
- **Análisis detallado** con estadísticas
- **Tabla de símbolos** completa
- **Cuádruplos** generados
- **Código ensamblador** formateado

### Controles
- **Atajos de teclado** estándar
- **Menús contextuales**
- **Barra de estado** informativa
- **Botones adaptativos** por SO

## 🆘 Solución de Problemas

### Error: "No se ven los botones" (macOS)
✅ **Solucionado** en la nueva versión usando tkinter básico optimizado.

### Error: "Python no encontrado"
```bash
# macOS
brew install python@3.9

# Ubuntu/Debian
sudo apt install python3 python3-venv

# Windows
# Descargar desde python.org
```

### Error: "Entorno virtual corrupto"
```bash
rm -rf .venv
python3 -m venv .venv
```

### Warning: "Tkinter deprecated" (macOS)
✅ **Automáticamente silenciado** en todos los scripts de inicio.

## 🏗️ Desarrollo

### Contribuir
1. Fork el proyecto
2. Crear branch: `git checkout -b feature/nueva-caracteristica`
3. Commit: `git commit -m 'Agregar nueva característica'`
4. Push: `git push origin feature/nueva-caracteristica`
5. Crear Pull Request

### Testing
```bash
# Ejecutar pruebas
python test_analyzer.py
python test_semantic_validations.py
```

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver `LICENSE` para más detalles.

## 👥 Autores

- **Desarrollador Principal** - Analizador léxico y interfaz
- **Contribuidores** - Validaciones semánticas y optimizaciones

## 🙏 Agradecimientos

- Comunidad de Python por las excelentes librerías
- Desarrolladores de tkinter por la interfaz multiplataforma
- Comunidad de robótica por la inspiración

---

**¡El analizador léxico más completo para robótica, funcionando perfectamente en macOS, Windows y Linux!** 🚀
