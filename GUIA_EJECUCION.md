# Guía de Ejecución - Analizador Léxico Robótico

## Descripción del Problema Resuelto

El archivo `main.py` no se ejecutaba porque faltaba la sección `if __name__ == "__main__":` que es necesaria para iniciar la aplicación. Esta sección ahora está incluida y la aplicación funciona correctamente.

## Cómo Ejecutar la Aplicación

### En Ubuntu/Linux:

1. **Usando Python directamente:**
   ```bash
   cd /home/xavier/lexic
   python3 main.py
   ```

2. **Usando el entorno virtual (recomendado):**
   ```bash
   cd /home/xavier/lexic
   source .venv/bin/activate
   python main.py
   ```

3. **Usando VSCode Task:**
   - Presiona `Ctrl+Shift+P`
   - Escribe "Tasks: Run Task"
   - Selecciona "Run Lexical Analyzer"

### En Windows:

1. **Doble clic en main.py** (si Python está asociado con archivos .py)

2. **Desde Command Prompt:**
   ```cmd
   cd C:\path\to\lexic
   python main.py
   ```

3. **Desde PowerShell:**
   ```powershell
   cd C:\path\to\lexic
   python main.py
   ```

## Características de la Aplicación

### Funcionalidades principales:
- **Editor de código** con numeración de líneas para código robótico
- **Análisis léxico, sintáctico y semántico** completo
- **Generación de cuádruplos** (código intermedio)
- **Generación de código ensamblador** (.asm)
- **Compilación a ejecutable** (.exe) usando TASM/TLINK
- **Interfaz gráfica intuitiva** con botones y menús

### Botones disponibles:
- **Abrir Archivo**: Cargar código robótico desde archivo
- **Guardar**: Guardar el código actual
- **Analizar**: Ejecutar análisis completo del código
- **Generar .EXE**: Convertir código a ejecutable para Proteus
- **Limpiar**: Limpiar todas las ventanas

## Generación de Ejecutables

### En Ubuntu:
- Se genera el archivo `.asm` correctamente
- La compilación a `.exe` puede fallar por limitaciones de Wine/DOSBox
- **Recomendación**: Transferir el proyecto a Windows para compilar

### En Windows:
- Proceso completo desde código fuente hasta `.exe`
- Compatible con Proteus para simulación de brazo robótico

## Lenguaje Robótico Soportado

```robot
# Ejemplo de código robótico
inicio
    base { giraf 90 }
    hombro { girai 45 }
    codo { mueve 30 }
    garra { abre 100 }
    espera 1000
    garra { cierra 50 }
    home
fin
```

### Componentes soportados:
- `base`, `hombro`, `codo`, `garra`, `muneca`

### Comandos soportados:
- `girai`, `giraf`, `abre`, `cierra`, `mueve`, `espera`
- `inicio`, `fin`, `home`
- Control de flujo: `if/then/else`, `while`

### Comentarios:
- `//` Comentario de línea
- `/* */` Comentario de bloque  
- `#` Comentario de línea

## Solución de Problemas

### Si la GUI no se abre:
1. Verificar que tienes un entorno gráfico activo
2. Verificar que `$DISPLAY` esté configurado
3. Ejecutar el script de prueba: `python3 test_gui_minimal.py`

### Si faltan dependencias:
```bash
# Instalar tkinter en Ubuntu/Debian
sudo apt install python3-tk

# Verificar instalación
python3 -c "import tkinter; print('tkinter OK')"
```

### Si la compilación falla:
1. **En Ubuntu**: Usar solo para generar `.asm`, compilar en Windows
2. **En Windows**: Verificar que DOSBox2 esté en la carpeta del proyecto
3. **Manual**: Usar TASM/TLINK directamente en DOSBox

## Archivos Importantes

- `main.py`: Interfaz gráfica principal
- `robot_lexical_analyzer.py`: Lógica del analizador
- `assembly_generator.py`: Generador de código ensamblador
- `DOSBox2/Tasm/`: Herramientas de compilación
- `test_*.robot`: Ejemplos de código robótico

## Notas Técnicas

- La aplicación usa `tkinter` para la interfaz gráfica
- Los ejecutables generados son compatibles con Proteus
- El código ensamblador generado es para arquitectura x86
- Compatible con Python 3.8+

---

**Desarrollado para el control de brazo robótico con análisis léxico, sintáctico y semántico completo.**
