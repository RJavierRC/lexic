# 🤖 Analizador Léxico para Brazo Robótico - Multiplataforma

Este proyecto es un analizador léxico, sintáctico y semántico especializado para el control de brazos robóticos, **completamente funcional en macOS, Windows y Linux**.

## � Compatibilidad Multiplataforma

### 🍎 **macOS (Darwin)**
- ✅ Análisis completo (léxico, sintáctico, semántico)
- ✅ Generación de código intermedio (cuádruplos)
- ✅ Generación de código ensamblador (.asm)
- ✅ Interfaz gráfica optimizada para macOS
- ❌ Compilación a .exe (usar Windows/Linux para esto)
- 💡 **Botón especial:** "Ver ASM" para generar código ensamblador

### 🪟 **Windows**
- ✅ Todas las funciones disponibles
- ✅ Compilación nativa a ejecutables .exe
- ✅ Integración completa con DOSBox + TASM
- ✅ Compatible con Proteus
- 💡 **Botón especial:** "Generar .EXE" para compilación completa

### 🐧 **Linux**
- ✅ Todas las funciones disponibles
- ✅ Compilación a .exe via DOSBox + TASM
- ✅ Entorno de desarrollo robusto
- 💡 **Botón especial:** "Compilar" para generar ejecutables

## 🚀 Inicio Rápido

### Opción 1: Script Universal (Recomendado)
```bash
# Funciona en cualquier sistema operativo
python3 start_universal.py
```

### Opción 2: Scripts Específicos
```bash
# macOS
./start_analyzer_macos.sh

# Linux
./start_analyzer_linux.sh

# Windows
start_analyzer_windows.bat
```

### Opción 3: Manual
```bash
# Activar entorno virtual
source .venv/bin/activate  # macOS/Linux
# O: .venv\Scripts\activate.bat  # Windows

# Ejecutar
TK_SILENCE_DEPRECATION=1 python main.py  # macOS/Linux
# O: python main.py  # Windows
```

## 🎯 Detección Automática de Sistema

La aplicación **detecta automáticamente** tu sistema operativo y adapta la interfaz:

- **macOS:** Botón "Ver ASM" + tema optimizado
- **Windows:** Botón "Generar .EXE" + funcionalidad completa
- **Linux:** Botón "Compilar" + DOSBox integrado

## 📝 Probar la Aplicación

1. **Ejecutar:** `python3 start_universal.py`
2. **Cargar ejemplo:** Botón "Abrir" → `ejemplo_macos.robot`
3. **Analizar:** Presiona "Analizar" (F5)
4. **Generar código:** 
   - macOS: "Ver ASM"
   - Windows/Linux: "Generar .EXE" o "Compilar"

## 🔧 Sintaxis del Lenguaje Robótico

```robot
// Declarar robot
Robot nombre_robot

// Configurar repeticiones
nombre_robot.repetir = N

// Bloque de código
nombre_robot.inicio
    nombre_robot.velocidad = valor
    nombre_robot.componente = valor
    nombre_robot.espera = tiempo
nombre_robot.fin
```

### 🤖 Componentes Soportados
- **base:** 0-360° (rotación completa)
- **hombro:** 0-180° (articulación limitada)
- **codo:** 0-180° (articulación limitada)  
- **garra:** 0-90° (apertura/cierre)
- **muneca:** 0-360° (rotación completa)
- **velocidad:** 0.1-10.0 (velocidad de movimiento)
- **repetir:** 1-100 (repeticiones)
- **espera:** 0.1-60.0 (segundos de pausa)

## 🎨 Interfaz Adaptativa

La interfaz se adapta automáticamente a cada sistema operativo:

### macOS 🍎
- Colores y temas nativos de macOS
- Botón "Ver ASM" destacado en amarillo
- Optimizaciones para Retina displays
- Manejo especial de warnings de tkinter

### Windows 🪟
- Botón "Generar .EXE" destacado en verde
- Integración completa con herramientas nativas
- Soporte para rutas de Windows

### Linux 🐧
- Botón "Compilar" con funcionalidad completa
- Optimizado para entornos de desarrollo
- Compatible con diferentes distribuciones

## 📊 Características Destacadas

- **🔍 Análisis Multinivel:** Léxico + Sintáctico + Semántico
- **🛡️ Validaciones Avanzadas:** Rangos, duplicados, declaraciones
- **⚙️ Código Intermedio:** Generación de cuádruplos optimizada
- **🖥️ Interfaz Intuitiva:** Editor con números de línea
- **🌍 Multiplataforma:** Un solo código, tres sistemas
- **🚀 Auto-detección:** Configuración automática por SO
- **📝 Retroalimentación:** Mensajes detallados de error

## 📁 Archivos de Ejemplo

- `ejemplo_macos.robot` - Ejemplo optimizado para probar
- `test_robot_code.robot` - Ejemplo complejo con múltiples características
- `test_completo.robot` - Suite de pruebas exhaustiva

## 🆘 Solución de Problemas

### Interfaz en Gris (macOS)
La nueva versión **ya no tiene este problema**. Usa tkinter básico optimizado.

### Python no encontrado
```bash
# macOS con Homebrew
brew install python@3.9

# Linux (Ubuntu/Debian)
sudo apt update && sudo apt install python3 python3-venv

# Windows
# Descargar desde python.org
```

### Problemas de Entorno Virtual
```bash
# Recrear entorno virtual
rm -rf .venv
python3 -m venv .venv
source .venv/bin/activate  # o .venv\Scripts\activate.bat en Windows
```

### DOSBox no encontrado (Windows/Linux)
- Asegúrate que la carpeta `DOSBox2/` esté presente
- En Linux: verifica permisos de ejecución
- En Windows: verifica que `dosbox.exe` exista

## 🏆 Ventajas de la Versión Multiplataforma

- **✨ Una sola aplicación** para todos los sistemas
- **🎯 Detección automática** de capacidades
- **🎨 Interfaz adaptativa** por sistema operativo
- **🔧 Configuración automática** de herramientas
- **📱 Experiencia nativa** en cada plataforma
- **🚀 Fácil distribución** y uso

¡El analizador está **100% optimizado** para funcionar perfectamente en macOS, Windows y Linux!
